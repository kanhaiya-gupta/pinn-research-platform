"""
Data Generator Module for PINN Research Platform.

This module provides data generation and loading functionality for PINN training and testing.
Now supports both on-the-fly generation and loading pre-generated data from the data/ folder.
"""

import torch
import numpy as np
from typing import Dict, Tuple, Optional, List, Any
from pathlib import Path
import json

from utils.loggers import get_general_logger
from utils.physics import get_physics_function, get_initial_condition, get_boundary_condition
from utils.data_loader import PINNDataLoader, load_training_data


class DataGenerator:
    """Data generator for PINN training and testing."""

    def __init__(self, logger_name: str = "data_generator", use_pre_generated: bool = True):
        """Initialize data generator.

        Args:
            logger_name (str): Name for the logger.
            use_pre_generated (bool): Whether to use pre-generated data from data/ folder
        """
        self.logger = get_general_logger(logger_name)
        self.use_pre_generated = use_pre_generated
        
        if self.use_pre_generated:
            try:
                self.data_loader = PINNDataLoader()
                self.logger.info("Data Generator initialized with pre-generated data support")
            except FileNotFoundError:
                self.logger.warning("Pre-generated data not found. Falling back to on-the-fly generation.")
                self.use_pre_generated = False
        else:
            self.logger.info("Data Generator initialized for on-the-fly generation")

    def generate_grid_data(self, x_range: Tuple[float, float], t_range: Tuple[float, float],
                          nx: int = 100, nt: int = 100) -> Dict[str, np.ndarray]:
        """Generate regular grid data.

        Args:
            x_range (Tuple[float, float]): Spatial domain range.
            t_range (Tuple[float, float]): Temporal domain range.
            nx (int): Number of spatial points.
            nt (int): Number of temporal points.

        Returns:
            Dict[str, np.ndarray]: Grid data.
        """
        x_min, x_max = x_range
        t_min, t_max = t_range
        
        x = np.linspace(x_min, x_max, nx)
        t = np.linspace(t_min, t_max, nt)
        
        X, T = np.meshgrid(x, t, indexing='ij')
        
        data = {
            'x': X.flatten().reshape(-1, 1),
            't': T.flatten().reshape(-1, 1),
            'x_grid': X,
            't_grid': T,
            'nx': nx,
            'nt': nt,
            'x_range': x_range,
            't_range': t_range
        }
        
        self.logger.info(f"Generated grid data: {nx}x{nt} points")
        return data

    def load_pre_generated_data(self, purpose: str, equation: str) -> Dict[str, torch.Tensor]:
        """
        Load pre-generated training data from the data/ folder.
        
        Args:
            purpose (str): Purpose category (e.g., 'forward_problems')
            equation (str): Equation name (e.g., 'heat')
            
        Returns:
            Dict[str, torch.Tensor]: Training data in the format expected by PINN trainers
        """
        try:
            # Load data using the data loader
            data = self.data_loader.get_training_data_dict(purpose, equation, as_tensors=True)
            
            # Convert to the format expected by existing trainers
            training_data = {
                'x': torch.cat([data['x_interior'].unsqueeze(1), data['t_interior'].unsqueeze(1)], dim=1),
                't': data['t_interior'].unsqueeze(1),
                'x_bc': torch.cat([data['x_bc'].unsqueeze(1), data['t_bc'].unsqueeze(1)], dim=1),
                't_bc': data['t_bc'].unsqueeze(1),
                'x_ic': torch.cat([data['x_ic'].unsqueeze(1), data['t_ic'].unsqueeze(1)], dim=1),
                't_ic': data['t_ic'].unsqueeze(1),
                'u_bc': data['u_bc'].unsqueeze(1),
                'u_ic': data['u_ic'].unsqueeze(1),
                'equation_type': equation,
                'purpose': purpose,
                'metadata': data['metadata']
            }
            
            # Add data points if available (for inverse problems, data assimilation, etc.)
            if 'x_data' in data:
                training_data['x_data'] = torch.cat([data['x_data'].unsqueeze(1), data['t_data'].unsqueeze(1)], dim=1)
                training_data['t_data'] = data['t_data'].unsqueeze(1)
                if 'u_data' in data:
                    training_data['u_data'] = data['u_data'].unsqueeze(1)
                elif 'u1_data' in data and 'u2_data' in data:
                    training_data['u1_data'] = data['u1_data'].unsqueeze(1)
                    training_data['u2_data'] = data['u2_data'].unsqueeze(1)
            
            # Get physics function for the equation
            physics_fn = get_physics_function(equation)
            
            # Create physics function with parameters from metadata
            def physics_function(x, t, u):
                params = data['metadata'].get('parameters', {})
                return physics_fn(x, t, u, **params)
            
            training_data['physics_fn'] = physics_function
            
            self.logger.info(f"Loaded pre-generated data for {purpose}/{equation}")
            return training_data
            
        except Exception as e:
            self.logger.error(f"Failed to load pre-generated data for {purpose}/{equation}: {e}")
            self.logger.info("Falling back to on-the-fly generation")
            return self.generate_training_data_on_the_fly(purpose, equation)

    def generate_training_data_on_the_fly(self, purpose: str, equation: str, 
                                        x_range: Tuple[float, float] = (0.0, 1.0),
                                        t_range: Tuple[float, float] = (0.0, 1.0),
                                        n_interior: int = 1000, n_boundary: int = 200, n_initial: int = 200,
                                        **kwargs) -> Dict[str, torch.Tensor]:
        """Generate training data on-the-fly (fallback method).

        Args:
            purpose (str): Purpose category
            equation (str): Equation name
            x_range (Tuple[float, float]): Spatial domain range.
            t_range (Tuple[float, float]): Temporal domain range.
            n_interior (int): Number of interior points.
            n_boundary (int): Number of boundary points.
            n_initial (int): Number of initial condition points.
            **kwargs: Additional parameters for physics function.

        Returns:
            Dict[str, torch.Tensor]: Training data.
        """
        x_min, x_max = x_range
        t_min, t_max = t_range
        
        # Generate interior points
        x_interior = torch.rand(n_interior, 1) * (x_max - x_min) + x_min
        t_interior = torch.rand(n_interior, 1) * (t_max - t_min) + t_min
        
        # Generate boundary points (left and right boundaries)
        n_boundary_each = n_boundary // 2
        t_boundary = torch.rand(n_boundary, 1) * (t_max - t_min) + t_min
        
        x_boundary_left = torch.full((n_boundary_each, 1), x_min)
        x_boundary_right = torch.full((n_boundary_each, 1), x_max)
        x_boundary = torch.cat([x_boundary_left, x_boundary_right], dim=0)
        
        # Generate initial condition points
        x_initial = torch.rand(n_initial, 1) * (x_max - x_min) + x_min
        t_initial = torch.full((n_initial, 1), t_min)
        
        # Get physics function
        physics_fn = get_physics_function(equation)
        
        # Create physics function with parameters
        def physics_function(x, t, u):
            return physics_fn(x, t, u, **kwargs)
        
        training_data = {
            'x': torch.cat([x_interior, t_interior], dim=1),
            't': t_interior,
            'x_bc': torch.cat([x_boundary, t_boundary], dim=1),
            't_bc': t_boundary,
            'x_ic': torch.cat([x_initial, t_initial], dim=1),
            't_ic': t_initial,
            'physics_fn': physics_function,
            'equation_type': equation,
            'purpose': purpose,
            'n_interior': n_interior,
            'n_boundary': n_boundary,
            'n_initial': n_initial
        }
        
        self.logger.info(f"Generated training data on-the-fly: {n_interior} interior, {n_boundary} boundary, {n_initial} initial points")
        return training_data

    def generate_training_data(self, purpose: str, equation: str, 
                             x_range: Tuple[float, float] = (0.0, 1.0),
                             t_range: Tuple[float, float] = (0.0, 1.0),
                             n_interior: int = 1000, n_boundary: int = 200, n_initial: int = 200,
                             **kwargs) -> Dict[str, torch.Tensor]:
        """Generate or load training data for PINN.

        Args:
            purpose (str): Purpose category (e.g., 'forward_problems')
            equation (str): Equation name (e.g., 'heat')
            x_range (Tuple[float, float]): Spatial domain range.
            t_range (Tuple[float, float]): Temporal domain range.
            n_interior (int): Number of interior points.
            n_boundary (int): Number of boundary points.
            n_initial (int): Number of initial condition points.
            **kwargs: Additional parameters for physics function.

        Returns:
            Dict[str, torch.Tensor]: Training data.
        """
        if self.use_pre_generated:
            return self.load_pre_generated_data(purpose, equation)
        else:
            return self.generate_training_data_on_the_fly(purpose, equation, x_range, t_range, 
                                                        n_interior, n_boundary, n_initial, **kwargs)

    def get_available_data(self) -> Dict[str, list]:
        """Get overview of available pre-generated data.
        
        Returns:
            Dict[str, list]: Dictionary mapping purposes to available equations
        """
        if self.use_pre_generated:
            return self.data_loader.get_available_data()
        else:
            return {}

    def get_data_info(self, purpose: str, equation: str) -> Dict[str, Any]:
        """Get information about available data for an equation.
        
        Args:
            purpose (str): Purpose category
            equation (str): Equation name
            
        Returns:
            Dict[str, Any]: Data information
        """
        if self.use_pre_generated:
            return self.data_loader.get_data_info(purpose, equation)
        else:
            return {'purpose': purpose, 'equation': equation, 'data_type': 'on_the_fly'}

    def generate_boundary_condition_data(self, x_boundary: torch.Tensor, t_boundary: torch.Tensor,
                                       bc_type: str = "dirichlet", **kwargs) -> torch.Tensor:
        """Generate boundary condition data.

        Args:
            x_boundary (torch.Tensor): Boundary spatial coordinates.
            t_boundary (torch.Tensor): Boundary temporal coordinates.
            bc_type (str): Type of boundary condition.
            **kwargs: Additional parameters for boundary condition.

        Returns:
            torch.Tensor: Boundary condition values.
        """
        if bc_type.lower() == "dirichlet":
            # Simple zero boundary condition
            u_bc = torch.zeros_like(x_boundary)
        elif bc_type.lower() == "neumann":
            # Zero gradient boundary condition
            u_bc = torch.zeros_like(x_boundary)
        else:
            raise ValueError(f"Unsupported boundary condition type: {bc_type}")
        
        return u_bc

    def generate_initial_condition_data(self, x_initial: torch.Tensor, t_initial: torch.Tensor,
                                      ic_type: str = "gaussian", **kwargs) -> torch.Tensor:
        """Generate initial condition data.

        Args:
            x_initial (torch.Tensor): Initial condition spatial coordinates.
            t_initial (torch.Tensor): Initial condition temporal coordinates.
            ic_type (str): Type of initial condition.
            **kwargs: Additional parameters for initial condition.

        Returns:
            torch.Tensor: Initial condition values.
        """
        ic_fn = get_initial_condition(ic_type)
        u_ic = ic_fn(x_initial, t_initial, **kwargs)
        return u_ic

    def generate_test_data(self, x_range: Tuple[float, float], t_range: Tuple[float, float],
                          nx_test: int = 200, nt_test: int = 200,
                          equation_type: str = "heat", **kwargs) -> Dict[str, np.ndarray]:
        """Generate test data for evaluation.

        Args:
            x_range (Tuple[float, float]): Spatial domain range.
            t_range (Tuple[float, float]): Temporal domain range.
            nx_test (int): Number of test spatial points.
            nt_test (int): Number of test temporal points.
            equation_type (str): Type of differential equation.
            **kwargs: Additional parameters.

        Returns:
            Dict[str, np.ndarray]: Test data.
        """
        # Generate test grid
        test_data = self.generate_grid_data(x_range, t_range, nx_test, nt_test)
        
        # Add equation type
        test_data['equation_type'] = equation_type
        
        self.logger.info(f"Generated test data: {nx_test}x{nt_test} points")
        return test_data

    def generate_analytical_solution(self, x: np.ndarray, t: np.ndarray,
                                   equation_type: str = "heat", **kwargs) -> np.ndarray:
        """Generate analytical solution for comparison.

        Args:
            x (np.ndarray): Spatial coordinates.
            t (np.ndarray): Temporal coordinates.
            equation_type (str): Type of differential equation.
            **kwargs: Additional parameters.

        Returns:
            np.ndarray: Analytical solution.
        """
        if equation_type.lower() == "heat":
            # Heat equation analytical solution: u(x,t) = exp(-π²t) * sin(πx)
            u_analytical = np.exp(-np.pi**2 * t) * np.sin(np.pi * x)
        elif equation_type.lower() == "wave":
            # Wave equation analytical solution: u(x,t) = sin(πx) * cos(πt)
            u_analytical = np.sin(np.pi * x) * np.cos(np.pi * t)
        elif equation_type.lower() == "advection":
            # Advection equation analytical solution: u(x,t) = sin(π(x-t))
            u_analytical = np.sin(np.pi * (x - t))
        else:
            # Default to zero solution
            u_analytical = np.zeros_like(x)
            self.logger.warning(f"No analytical solution available for {equation_type}")
        
        return u_analytical

    def save_data(self, data: Dict[str, Any], save_path: str) -> None:
        """Save generated data to file.

        Args:
            data (Dict[str, Any]): Data to save.
            save_path (str): Path to save data.
        """
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        
        # Convert tensors to numpy arrays for saving
        save_data = {}
        for key, value in data.items():
            if isinstance(value, torch.Tensor):
                save_data[key] = value.detach().numpy()
            elif callable(value):
                # Skip functions
                continue
            else:
                save_data[key] = value
        
        np.savez(save_path, **save_data)
        self.logger.info(f"Data saved to {save_path}")

    def load_data(self, load_path: str) -> Dict[str, Any]:
        """Load data from file.

        Args:
            load_path (str): Path to load data from.

        Returns:
            Dict[str, Any]: Loaded data.
        """
        data = np.load(load_path)
        loaded_data = {}
        
        for key in data.keys():
            loaded_data[key] = data[key]
        
        self.logger.info(f"Data loaded from {load_path}")
        return loaded_data

    def create_dataset_summary(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a summary of the dataset.

        Args:
            data (Dict[str, Any]): Dataset.

        Returns:
            Dict[str, Any]: Dataset summary.
        """
        summary = {
            'total_points': 0,
            'spatial_range': None,
            'temporal_range': None,
            'equation_type': data.get('equation_type', 'unknown'),
            'data_types': list(data.keys())
        }
        
        if 'x' in data and 't' in data:
            if isinstance(data['x'], torch.Tensor):
                x_data = data['x'].detach().numpy()
                t_data = data['t'].detach().numpy()
            else:
                x_data = data['x']
                t_data = data['t']
            
            summary['total_points'] = len(x_data)
            summary['spatial_range'] = (float(x_data.min()), float(x_data.max()))
            summary['temporal_range'] = (float(t_data.min()), float(t_data.max()))
        
        return summary 