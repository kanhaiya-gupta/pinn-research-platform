"""
ForwardProblems Trainer for PINN Research Platform.

This module provides training functionality for forward problems using PINNs.
"""

import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from typing import Dict, Any, Tuple, Optional, Callable
import time
from pathlib import Path
import json

from utils.loggers import get_purpose_logger


class ForwardProblemsTrainer:
    """Trainer class for forward problems using PINNs."""

    def __init__(self, model: nn.Module, purpose: str, equation: str):
        """Initialize the forward problems trainer.

        Args:
            model (nn.Module): PINN model to train.
            purpose (str): PINN purpose (e.g., 'forward_problems').
            equation (str): Equation type (e.g., 'heat', 'wave', 'burgers').
        """
        self.model = model
        self.purpose = purpose
        self.equation = equation
        self.logger = get_purpose_logger(purpose, equation)
        
        # Training state
        self.optimizer = None
        self.scheduler = None
        self.training_history = {
            'physics_loss': [],
            'boundary_loss': [],
            'initial_loss': [],
            'total_loss': [],
            'epochs': []
        }
        
        self.logger.log_purpose_specific_info("ForwardProblems Trainer initialized")

    def setup_optimizer(self, learning_rate: float = 0.001, 
                       optimizer_type: str = "adam") -> None:
        """Setup optimizer for training.

        Args:
            learning_rate (float): Learning rate for optimization.
            optimizer_type (str): Type of optimizer ('adam', 'sgd', 'adamw', 'adam_lbfgs', 'lbfgs').
        """
        if optimizer_type.lower() == "adam":
            self.optimizer = optim.Adam(self.model.parameters(), lr=learning_rate)
        elif optimizer_type.lower() == "sgd":
            self.optimizer = optim.SGD(self.model.parameters(), lr=learning_rate)
        elif optimizer_type.lower() == "adamw":
            self.optimizer = optim.AdamW(self.model.parameters(), lr=learning_rate)
        elif optimizer_type.lower() == "lbfgs":
            self.optimizer = optim.LBFGS(self.model.parameters(), lr=learning_rate, max_iter=20)
        elif optimizer_type.lower() == "adam_lbfgs":
            # For adam_lbfgs, we'll use Adam initially and can switch to LBFGS later
            self.optimizer = optim.Adam(self.model.parameters(), lr=learning_rate)
            self.optimizer_type = "adam_lbfgs"  # Store for potential switching
        else:
            raise ValueError(f"Unsupported optimizer type: {optimizer_type}")
        
        self.logger.log_equation_specific_info(f"Optimizer {optimizer_type} setup with lr={learning_rate}")

    def setup_scheduler(self, scheduler_type: str = "step", 
                       step_size: int = 1000, gamma: float = 0.9) -> None:
        """Setup learning rate scheduler.

        Args:
            scheduler_type (str): Type of scheduler ('step', 'cosine', 'plateau').
            step_size (int): Step size for step scheduler.
            gamma (float): Gamma value for step scheduler.
        """
        if self.optimizer is None:
            raise ValueError("Optimizer must be setup before scheduler")
        
        if scheduler_type.lower() == "step":
            self.scheduler = optim.lr_scheduler.StepLR(
                self.optimizer, step_size=step_size, gamma=gamma
            )
        elif scheduler_type.lower() == "cosine":
            self.scheduler = optim.lr_scheduler.CosineAnnealingLR(
                self.optimizer, T_max=step_size
            )
        elif scheduler_type.lower() == "plateau":
            self.scheduler = optim.lr_scheduler.ReduceLROnPlateau(
                self.optimizer, mode='min', factor=gamma, patience=step_size//10
            )
        
        self.logger.log_equation_specific_info(f"Scheduler {scheduler_type} setup")

    def train_step(self, train_data: Dict[str, torch.Tensor],
                  physics_fn: Callable, weights: Dict[str, float]) -> Dict[str, float]:
        """Perform a single training step.

        Args:
            train_data (Dict[str, torch.Tensor]): Training data.
            physics_fn (Callable): Physics function.
            weights (Dict[str, float]): Loss weights.

        Returns:
            Dict[str, float]: Loss values for this step.
        """
        # Handle LBFGS optimizer which requires a closure
        if isinstance(self.optimizer, optim.LBFGS):
            def closure():
                self.optimizer.zero_grad()
                
                # Extract data points using the correct keys from data generator
                x_interior = train_data['x'][:, 0:1]  # First column is x
                t_interior = train_data['x'][:, 1:2]  # Second column is t
                x_bc = train_data['x_bc'][:, 0:1]     # First column is x
                t_bc = train_data['x_bc'][:, 1:2]     # Second column is t
                u_bc = train_data['u_bc']
                x_ic = train_data['x_ic'][:, 0:1]     # First column is x
                t_ic = train_data['x_ic'][:, 1:2]     # Second column is t
                u_ic = train_data['u_ic']
                
                # Physics loss (PDE residual)
                x_t_combined = torch.cat([x_interior, t_interior], dim=1)
                u_interior = self.model(x_t_combined)
                physics_residual = physics_fn(x_interior, t_interior, u_interior)
                physics_loss = torch.mean(physics_residual**2)
                
                # Boundary condition loss
                x_t_bc_combined = torch.cat([x_bc, t_bc], dim=1)
                u_bc_pred = self.model(x_t_bc_combined)
                boundary_loss = torch.mean((u_bc_pred - u_bc)**2)
                
                # Initial condition loss
                x_t_ic_combined = torch.cat([x_ic, t_ic], dim=1)
                u_ic_pred = self.model(x_t_ic_combined)
                initial_loss = torch.mean((u_ic_pred - u_ic)**2)
                
                # Total loss with weights
                total_loss = (weights['physics'] * physics_loss + 
                             weights['boundary'] * boundary_loss + 
                             weights['initial'] * initial_loss)
                
                # Backward pass
                total_loss.backward()
                return total_loss
            
            # LBFGS step
            self.optimizer.step(closure)
            
            # For LBFGS, we need to compute losses again for logging
            with torch.no_grad():
                x_interior = train_data['x'][:, 0:1]
                t_interior = train_data['x'][:, 1:2]
                x_bc = train_data['x_bc'][:, 0:1]
                t_bc = train_data['x_bc'][:, 1:2]
                u_bc = train_data['u_bc']
                x_ic = train_data['x_ic'][:, 0:1]
                t_ic = train_data['x_ic'][:, 1:2]
                u_ic = train_data['u_ic']
                
                x_t_combined = torch.cat([x_interior, t_interior], dim=1)
                u_interior = self.model(x_t_combined)
                physics_residual = physics_fn(x_interior, t_interior, u_interior)
                physics_loss = torch.mean(physics_residual**2)
                
                x_t_bc_combined = torch.cat([x_bc, t_bc], dim=1)
                u_bc_pred = self.model(x_t_bc_combined)
                boundary_loss = torch.mean((u_bc_pred - u_bc)**2)
                
                x_t_ic_combined = torch.cat([x_ic, t_ic], dim=1)
                u_ic_pred = self.model(x_t_ic_combined)
                initial_loss = torch.mean((u_ic_pred - u_ic)**2)
                
                total_loss = (weights['physics'] * physics_loss + 
                             weights['boundary'] * boundary_loss + 
                             weights['initial'] * initial_loss)
            
            return {
                'physics_loss': physics_loss.item(),
                'boundary_loss': boundary_loss.item(),
                'initial_loss': initial_loss.item(),
                'total_loss': total_loss.item()
            }
        
        else:
            # Standard optimizer (Adam, SGD, etc.)
            self.optimizer.zero_grad()
            
            # Extract data points using the correct keys from data generator
            x_interior = train_data['x'][:, 0:1]  # First column is x
            t_interior = train_data['x'][:, 1:2]  # Second column is t
            x_bc = train_data['x_bc'][:, 0:1]     # First column is x
            t_bc = train_data['x_bc'][:, 1:2]     # Second column is t
            u_bc = train_data['u_bc']
            x_ic = train_data['x_ic'][:, 0:1]     # First column is x
            t_ic = train_data['x_ic'][:, 1:2]     # Second column is t
            u_ic = train_data['u_ic']
            
            # Physics loss (PDE residual)
            x_t_combined = torch.cat([x_interior, t_interior], dim=1)
            u_interior = self.model(x_t_combined)
            physics_residual = physics_fn(x_interior, t_interior, u_interior)
            physics_loss = torch.mean(physics_residual**2)
            
            # Boundary condition loss
            x_t_bc_combined = torch.cat([x_bc, t_bc], dim=1)
            u_bc_pred = self.model(x_t_bc_combined)
            boundary_loss = torch.mean((u_bc_pred - u_bc)**2)
            
            # Initial condition loss
            x_t_ic_combined = torch.cat([x_ic, t_ic], dim=1)
            u_ic_pred = self.model(x_t_ic_combined)
            initial_loss = torch.mean((u_ic_pred - u_ic)**2)
            
            # Total loss with weights
            total_loss = (weights['physics'] * physics_loss + 
                         weights['boundary'] * boundary_loss + 
                         weights['initial'] * initial_loss)
            
            # Backward pass
            total_loss.backward()
            self.optimizer.step()
            
            if self.scheduler is not None:
                if isinstance(self.scheduler, optim.lr_scheduler.ReduceLROnPlateau):
                    self.scheduler.step(total_loss)
                else:
                    self.scheduler.step()
            
            return {
                'physics_loss': physics_loss.item(),
                'boundary_loss': boundary_loss.item(),
                'initial_loss': initial_loss.item(),
                'total_loss': total_loss.item()
            }

    def train(self, train_data: Dict[str, torch.Tensor], 
              physics_fn: Callable, epochs: int = 10000,
              weights: Optional[Dict[str, float]] = None,
              save_interval: int = 1000, save_path: Optional[str] = None,
              progress_callback: Optional[Callable] = None) -> Dict[str, list]:
        """Train the PINN model.

        Args:
            train_data (Dict[str, torch.Tensor]): Training data.
            physics_fn (Callable): Physics function.
            epochs (int): Number of training epochs.
            weights (Dict[str, float], optional): Loss weights.
            save_interval (int): Interval for saving checkpoints.
            save_path (str, optional): Path to save checkpoints.

        Returns:
            Dict[str, list]: Training history.
        """
        if weights is None:
            weights = {'physics': 1.0, 'boundary': 1.0, 'initial': 1.0}
        
        # Log training start
        training_params = {
            'epochs': epochs,
            'weights': weights,
            'save_interval': save_interval,
            'equation': self.equation,
            'purpose': self.purpose
        }
        self.logger.log_training_start(training_params)
        
        start_time = time.time()
        
        for epoch in range(epochs):
            # Training step
            losses = self.train_step(train_data, physics_fn, weights)
            
            # Store history
            for key, value in losses.items():
                self.training_history[key].append(value)
            self.training_history['epochs'].append(epoch)
            
            # Call progress callback if provided
            if progress_callback is not None:
                progress_callback(epoch, losses)
            
            # Log progress (more frequent for live training)
            if epoch % 50 == 0:  # Log every 50 epochs for smoother plotting
                self.logger.log_training_progress(
                    epoch, epochs, losses.get('physics_loss', 0.0), losses['total_loss']
                )
            
            # Save checkpoint
            if save_path and epoch % save_interval == 0:
                self.save_checkpoint(save_path, epoch, losses)
        
        training_time = time.time() - start_time
        self.logger.log_training_complete(losses['total_loss'], training_time)
        
        return self.training_history

    def save_checkpoint(self, save_path: str, epoch: int, losses: Dict[str, float]) -> None:
        """Save training checkpoint.

        Args:
            save_path (str): Path to save checkpoint.
            epoch (int): Current epoch.
            losses (Dict[str, float]): Current loss values.
        """
        checkpoint = {
            'epoch': epoch,
            'model_state_dict': self.model.state_dict(),
            'optimizer_state_dict': self.optimizer.state_dict(),
            'losses': losses,
            'training_history': self.training_history,
            'purpose': self.purpose,
            'equation': self.equation
        }
        
        if self.scheduler is not None:
            checkpoint['scheduler_state_dict'] = self.scheduler.state_dict()
        
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        torch.save(checkpoint, f"{save_path}_epoch_{epoch}.pt")
        
        self.logger.log_equation_specific_info(f"Checkpoint saved at epoch {epoch}")

    def load_checkpoint(self, checkpoint_path: str) -> int:
        """Load training checkpoint.

        Args:
            checkpoint_path (str): Path to checkpoint file.

        Returns:
            int: Epoch number from checkpoint.
        """
        checkpoint = torch.load(checkpoint_path)
        
        self.model.load_state_dict(checkpoint['model_state_dict'])
        self.optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
        
        if 'scheduler_state_dict' in checkpoint and self.scheduler is not None:
            self.scheduler.load_state_dict(checkpoint['scheduler_state_dict'])
        
        self.training_history = checkpoint['training_history']
        
        epoch = checkpoint['epoch']
        self.logger.log_equation_specific_info(f"Checkpoint loaded from epoch {epoch}")
        
        return epoch 