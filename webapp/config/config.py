"""
Configuration for the PINN web application.
This module provides access to equations, parameters, and application settings.
"""

import os
from pathlib import Path
from typing import Dict, Any, List

# Import from new modular structure
from .equations import ALL_PURPOSE_EQUATIONS, SUPPORTED_EQUATIONS
from .parameters import ALL_PURPOSE_PARAMETERS, SUPPORTED_PARAMETERS

class Config:
    """Configuration class for PINN web application."""
    
    def __init__(self):
        # Base directory
        self.BASE_DIR = Path(__file__).parent.parent
        
        # API configuration
        self.API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")
        
        # PINN purposes
        self.PINN_PURPOSES = {
            'forward_problems': {
                'name': 'Forward Problems',
                'description': 'Solve differential equations with known parameters',
                'icon': 'fas fa-arrow-right',
                'color': 'primary',
                'equations': ALL_PURPOSE_EQUATIONS.get('forward_problems', {}),
                'parameters': ALL_PURPOSE_PARAMETERS.get('forward_problems', {})
            },
            'inverse_problems': {
                'name': 'Inverse Problems',
                'description': 'Identify unknown parameters from observational data',
                'icon': 'fas fa-search',
                'color': 'success',
                'equations': ALL_PURPOSE_EQUATIONS.get('inverse_problems', {}),
                'parameters': ALL_PURPOSE_PARAMETERS.get('inverse_problems', {})
            },
            'data_assimilation': {
                'name': 'Data Assimilation',
                'description': 'Integrate observational data into physical models',
                'icon': 'fas fa-database',
                'color': 'info',
                'equations': ALL_PURPOSE_EQUATIONS.get('data_assimilation', {}),
                'parameters': ALL_PURPOSE_PARAMETERS.get('data_assimilation', {})
            },
            'control_optimization': {
                'name': 'Control & Optimization',
                'description': 'Optimal control and parameter optimization',
                'icon': 'fas fa-sliders-h',
                'color': 'warning',
                'equations': ALL_PURPOSE_EQUATIONS.get('control_optimization', {}),
                'parameters': ALL_PURPOSE_PARAMETERS.get('control_optimization', {})
            },
            'sparse_data': {
                'name': 'Sparse Data Learning',
                'description': 'Learn from limited or sparse observational data',
                'icon': 'fas fa-chart-line',
                'color': 'secondary',
                'equations': ALL_PURPOSE_EQUATIONS.get('sparse_data', {}),
                'parameters': ALL_PURPOSE_PARAMETERS.get('sparse_data', {})
            },
            'uncertainty': {
                'name': 'Uncertainty Quantification',
                'description': 'Quantify and propagate uncertainty in physical systems',
                'icon': 'fas fa-question-circle',
                'color': 'dark',
                'equations': ALL_PURPOSE_EQUATIONS.get('uncertainty', {}),
                'parameters': ALL_PURPOSE_PARAMETERS.get('uncertainty', {})
            },
            'multiphysics': {
                'name': 'Multiphysics',
                'description': 'Coupled physical phenomena and multiphysics systems',
                'icon': 'fas fa-link',
                'color': 'danger',
                'equations': ALL_PURPOSE_EQUATIONS.get('multiphysics', {}),
                'parameters': ALL_PURPOSE_PARAMETERS.get('multiphysics', {})
            },
            'efficiency': {
                'name': 'Computational Efficiency',
                'description': 'Optimize computational efficiency and performance',
                'icon': 'fas fa-tachometer-alt',
                'color': 'primary',
                'equations': ALL_PURPOSE_EQUATIONS.get('efficiency', {}),
                'parameters': ALL_PURPOSE_PARAMETERS.get('efficiency', {})
            },
            'generalization': {
                'name': 'Model Generalization',
                'description': 'Improve model generalization and transfer learning',
                'icon': 'fas fa-expand-arrows-alt',
                'color': 'success',
                'equations': ALL_PURPOSE_EQUATIONS.get('generalization', {}),
                'parameters': ALL_PURPOSE_PARAMETERS.get('generalization', {})
            },
            'scientific_discovery': {
                'name': 'Scientific Discovery',
                'description': 'Discover new physical laws and relationships',
                'icon': 'fas fa-microscope',
                'color': 'info',
                'equations': ALL_PURPOSE_EQUATIONS.get('scientific_discovery', {}),
                'parameters': ALL_PURPOSE_PARAMETERS.get('scientific_discovery', {})
            },
            'astrophysics': {
                'name': 'Astrophysics',
                'description': 'Astrophysical and cosmological equations and simulations',
                'icon': 'fas fa-star',
                'color': 'purple',
                'equations': ALL_PURPOSE_EQUATIONS.get('astrophysics', {}),
                'parameters': ALL_PURPOSE_PARAMETERS.get('astrophysics', {})
            },
        }
        
        # Legacy support - flatten all equations and parameters
        self.SUPPORTED_EQUATIONS = SUPPORTED_EQUATIONS
        self.SUPPORTED_PARAMETERS = SUPPORTED_PARAMETERS
        
        # Default parameters (legacy support)
        self.DEFAULT_PARAMETERS = self._create_default_parameters()
        
        # Training parameters
        self.TRAINING_PARAMETERS = {
            'epochs': 1000,
            'learning_rate': 0.001,
            'batch_size': 32,
            'optimizer': 'adam',
            'activation': 'tanh',
            'hidden_layers': [50, 50, 50, 50],
            'early_stopping_patience': 100,
            'validation_split': 0.2
        }
        
        # Model architecture parameters
        self.ARCHITECTURE_PARAMETERS = {
            'input_dim': 2,
            'output_dim': 1,
            'hidden_layers': [50, 50, 50, 50],
            'activation': 'tanh',
            'dropout_rate': 0.1,
            'batch_normalization': True
        }
        
        # Simulation parameters
        self.SIMULATION_PARAMETERS = {
            'time_steps': 100,
            'spatial_points': 100,
            'temporal_points': 100,
            'collocation_points': 1000,
            'boundary_points': 100,
            'initial_points': 100
        }
    
    def _create_default_parameters(self) -> Dict[str, Dict[str, Any]]:
        """Create default parameters for legacy support."""
        default_params = {}
        
        # Create default parameters for each equation
        for eq_id, eq_info in self.SUPPORTED_EQUATIONS.items():
            default_params[eq_id] = {
                'epochs': 1000,
                'learning_rate': 0.001,
                'batch_size': 32,
                'optimizer': 'adam',
                'activation': 'tanh',
                'hidden_layers': [50, 50, 50, 50],
                'early_stopping_patience': 100,
                'validation_split': 0.2
            }
            
            # Add equation-specific parameters from the flat SUPPORTED_PARAMETERS
            for param_id, param_info in self.SUPPORTED_PARAMETERS.items():
                if isinstance(param_info, dict) and 'default' in param_info:
                    # Add parameters that might be relevant to this equation
                    if param_id not in default_params[eq_id]:
                        default_params[eq_id][param_id] = param_info['default']
        
        return default_params
    
    def get_equations_by_purpose(self, purpose: str) -> Dict[str, Any]:
        """Get equations for a specific purpose."""
        return self.PINN_PURPOSES.get(purpose, {}).get('equations', {})
    
    def get_parameters_by_purpose(self, purpose: str) -> Dict[str, Any]:
        """Get parameters for a specific purpose."""
        return self.PINN_PURPOSES.get(purpose, {}).get('parameters', {})
    
    def get_purpose_info(self, purpose: str) -> Dict[str, Any]:
        """Get information about a specific purpose."""
        return self.PINN_PURPOSES.get(purpose, {})
    
    def get_all_purposes(self) -> Dict[str, Any]:
        """Get all PINN purposes."""
        return self.PINN_PURPOSES
    
    def get_equation_info(self, eq_id: str) -> Dict[str, Any]:
        """Get information about a specific equation."""
        return self.SUPPORTED_EQUATIONS.get(eq_id, {})
    
    def get_parameter_info(self, param_id: str) -> Dict[str, Any]:
        """Get information about a specific parameter."""
        return self.SUPPORTED_PARAMETERS.get(param_id, {})
    
    def get_default_parameters(self, eq_id: str) -> Dict[str, Any]:
        """Get default parameters for a specific equation."""
        return self.DEFAULT_PARAMETERS.get(eq_id, {})
    
    def get_training_parameters(self) -> Dict[str, Any]:
        """Get training parameters."""
        return self.TRAINING_PARAMETERS
    
    def get_architecture_parameters(self) -> Dict[str, Any]:
        """Get architecture parameters."""
        return self.ARCHITECTURE_PARAMETERS
    
    def get_simulation_parameters(self) -> Dict[str, Any]:
        """Get simulation parameters."""
        return self.SIMULATION_PARAMETERS

# Create global config instance
config = Config() 