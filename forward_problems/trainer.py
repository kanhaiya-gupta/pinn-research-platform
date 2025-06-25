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
            optimizer_type (str): Type of optimizer ('adam', 'sgd', 'adamw').
        """
        if optimizer_type.lower() == "adam":
            self.optimizer = optim.Adam(self.model.parameters(), lr=learning_rate)
        elif optimizer_type.lower() == "sgd":
            self.optimizer = optim.SGD(self.model.parameters(), lr=learning_rate)
        elif optimizer_type.lower() == "adamw":
            self.optimizer = optim.AdamW(self.model.parameters(), lr=learning_rate)
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
        self.optimizer.zero_grad()
        
        # Compute losses (implement specific loss computation for this purpose)
        # This is a placeholder - implement specific logic for each purpose
        total_loss = torch.tensor(0.0, requires_grad=True)
        
        # Backward pass
        total_loss.backward()
        self.optimizer.step()
        
        if self.scheduler is not None:
            if isinstance(self.scheduler, optim.lr_scheduler.ReduceLROnPlateau):
                self.scheduler.step(total_loss)
            else:
                self.scheduler.step()
        
        return {
            'total_loss': total_loss.item()
        }

    def train(self, train_data: Dict[str, torch.Tensor], 
              physics_fn: Callable, epochs: int = 10000,
              weights: Optional[Dict[str, float]] = None,
              save_interval: int = 1000, save_path: Optional[str] = None) -> Dict[str, list]:
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
            
            # Log progress
            if epoch % 100 == 0:
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
