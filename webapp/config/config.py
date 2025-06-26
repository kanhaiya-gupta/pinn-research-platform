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
            }
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
        
        # Architecture recommendations for each purpose
        self.ARCHITECTURE_RECOMMENDATIONS = {
            'forward_problems': {
                'hidden_activation': 'tanh',
                'output_activation': 'linear',
                'optimizer': 'adam',
                'notes': 'Use tanh for smooth solutions, linear output for continuous fields'
            },
            'inverse_problems': {
                'hidden_activation': 'tanh',
                'output_activation': 'linear',
                'optimizer': 'adam',
                'notes': 'Stable training with tanh, careful parameter initialization'
            },
            'data_assimilation': {
                'hidden_activation': 'tanh',
                'output_activation': 'linear',
                'optimizer': 'adam',
                'notes': 'Balance between data fitting and physics constraints'
            },
            'control_optimization': {
                'hidden_activation': 'tanh',
                'output_activation': 'linear',
                'optimizer': 'adam',
                'notes': 'Focus on control parameter optimization'
            },
            'sparse_data': {
                'hidden_activation': 'tanh',
                'output_activation': 'linear',
                'optimizer': 'adam',
                'notes': 'Physics-informed regularization for sparse data'
            },
            'uncertainty': {
                'hidden_activation': 'tanh',
                'output_activation': 'linear',
                'optimizer': 'adam',
                'notes': 'Monte Carlo or ensemble methods for uncertainty'
            },
            'multiphysics': {
                'hidden_activation': 'tanh',
                'output_activation': 'linear',
                'optimizer': 'adam',
                'notes': 'Coupled physics with balanced loss weights'
            },
            'efficiency': {
                'hidden_activation': 'tanh',
                'output_activation': 'linear',
                'optimizer': 'adam',
                'notes': 'Optimize for computational speed and memory'
            },
            'generalization': {
                'hidden_activation': 'tanh',
                'output_activation': 'linear',
                'optimizer': 'adam',
                'notes': 'Focus on transfer learning and domain adaptation'
            },
            'scientific_discovery': {
                'hidden_activation': 'tanh',
                'output_activation': 'linear',
                'optimizer': 'adam',
                'notes': 'Discover new physical laws and relationships'
            }
        }
        
        # Training recommendations for each purpose
        self.TRAINING_RECOMMENDATIONS = {
            'forward_problems': {
                'learning_rate': '0.001',
                'scheduler': 'constant',
                'loss_weights': {
                    'physics': 1.0,
                    'boundary': 1.0,
                    'initial': 1.0
                },
                'sampling': {
                    'interior': 1000,
                    'boundary': 200,
                    'initial': 200
                },
                'notes': 'Standard PINN training with balanced loss weights'
            },
            'inverse_problems': {
                'learning_rate': '0.001',
                'scheduler': 'step',
                'loss_weights': {
                    'physics': 1.0,
                    'boundary': 1.0,
                    'initial': 1.0,
                    'data': 10.0
                },
                'sampling': {
                    'interior': 1000,
                    'boundary': 200,
                    'initial': 200,
                    'data': 100
                },
                'notes': 'Higher weight on data loss for parameter identification'
            },
            'data_assimilation': {
                'learning_rate': '0.001',
                'scheduler': 'constant',
                'loss_weights': {
                    'physics': 1.0,
                    'boundary': 1.0,
                    'initial': 1.0,
                    'data': 5.0
                },
                'sampling': {
                    'interior': 1000,
                    'boundary': 200,
                    'initial': 200,
                    'data': 200
                },
                'notes': 'Balance physics and observational data'
            },
            'control_optimization': {
                'learning_rate': '0.001',
                'scheduler': 'cosine',
                'loss_weights': {
                    'physics': 1.0,
                    'boundary': 1.0,
                    'initial': 1.0,
                    'control': 2.0
                },
                'sampling': {
                    'interior': 1000,
                    'boundary': 200,
                    'initial': 200
                },
                'notes': 'Optimize control parameters with physics constraints'
            },
            'sparse_data': {
                'learning_rate': '0.001',
                'scheduler': 'constant',
                'loss_weights': {
                    'physics': 2.0,
                    'boundary': 1.0,
                    'initial': 1.0,
                    'data': 1.0
                },
                'sampling': {
                    'interior': 2000,
                    'boundary': 400,
                    'initial': 400,
                    'data': 50
                },
                'notes': 'Higher physics weight to compensate for sparse data'
            },
            'uncertainty': {
                'learning_rate': '0.001',
                'scheduler': 'constant',
                'loss_weights': {
                    'physics': 1.0,
                    'boundary': 1.0,
                    'initial': 1.0
                },
                'sampling': {
                    'interior': 1000,
                    'boundary': 200,
                    'initial': 200
                },
                'notes': 'Monte Carlo dropout or ensemble methods'
            },
            'multiphysics': {
                'learning_rate': '0.001',
                'scheduler': 'constant',
                'loss_weights': {
                    'physics': 1.0,
                    'boundary': 1.0,
                    'initial': 1.0,
                    'coupling': 1.0
                },
                'sampling': {
                    'interior': 1500,
                    'boundary': 300,
                    'initial': 300
                },
                'notes': 'Coupled physics with balanced coupling terms'
            },
            'efficiency': {
                'learning_rate': '0.001',
                'scheduler': 'constant',
                'loss_weights': {
                    'physics': 1.0,
                    'boundary': 1.0,
                    'initial': 1.0
                },
                'sampling': {
                    'interior': 500,
                    'boundary': 100,
                    'initial': 100
                },
                'notes': 'Optimize for speed with reduced sampling'
            },
            'generalization': {
                'learning_rate': '0.001',
                'scheduler': 'cosine',
                'loss_weights': {
                    'physics': 1.0,
                    'boundary': 1.0,
                    'initial': 1.0
                },
                'sampling': {
                    'interior': 1000,
                    'boundary': 200,
                    'initial': 200
                },
                'notes': 'Focus on transfer learning and domain adaptation'
            },
            'scientific_discovery': {
                'learning_rate': '0.001',
                'scheduler': 'constant',
                'loss_weights': {
                    'physics': 1.0,
                    'boundary': 1.0,
                    'initial': 1.0
                },
                'sampling': {
                    'interior': 1000,
                    'boundary': 200,
                    'initial': 200
                },
                'notes': 'Discover new physical laws and relationships'
            }
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
        return ALL_PURPOSE_PARAMETERS.get(purpose, {})
    
    def get_equation_parameters(self, purpose: str, eq_id: str) -> Dict[str, Any]:
        """Get equation-specific parameters for a given purpose and equation."""
        # Get general parameters for the purpose
        general_params = ALL_PURPOSE_PARAMETERS.get(purpose, {})
        
        # Define equation-specific parameter mappings
        equation_params = self._get_equation_specific_parameters(purpose, eq_id)
        
        # Combine general and equation-specific parameters
        combined_params = {**general_params, **equation_params}
        
        return combined_params
    
    def _get_equation_specific_parameters(self, purpose: str, eq_id: str) -> Dict[str, Any]:
        """Get equation-specific parameters for forward problems."""
        if purpose == 'forward_problems':
            return self._get_forward_problems_equation_params(eq_id)
        # Add other purposes as needed
        return {}
    
    def _get_forward_problems_equation_params(self, eq_id: str) -> Dict[str, Any]:
        """Get equation-specific parameters for forward problems equations."""
        equation_params = {
            'burgers': {
                'viscosity': {
                    'name': 'Viscosity (ν)',
                    'description': 'Dynamic viscosity coefficient in Burgers equation',
                    'unit': 'Pa·s',
                    'default': 0.01,
                    'range': [1e-6, 1e-1],
                    'category': 'fluid_properties',
                    'equation': '∂u/∂t + u∂u/∂x = ν∂²u/∂x²'
                },
                'domain_size': {
                    'name': 'Domain Size',
                    'description': 'Spatial domain length',
                    'unit': 'm',
                    'default': 1.0,
                    'range': [0.1, 10.0],
                    'category': 'domain_properties'
                },
                'time_duration': {
                    'name': 'Time Duration',
                    'description': 'Simulation time duration',
                    'unit': 's',
                    'default': 1.0,
                    'range': [0.1, 10.0],
                    'category': 'temporal_properties'
                }
            },
            
            'heat': {
                'thermal_diffusivity': {
                    'name': 'Thermal Diffusivity (α)',
                    'description': 'Thermal diffusivity coefficient in heat equation',
                    'unit': 'm²/s',
                    'default': 1e-5,
                    'range': [1e-8, 1e-3],
                    'category': 'thermal_properties',
                    'equation': '∂u/∂t = α∂²u/∂x²'
                },
                'domain_size': {
                    'name': 'Domain Size',
                    'description': 'Spatial domain length',
                    'unit': 'm',
                    'default': 1.0,
                    'range': [0.1, 10.0],
                    'category': 'domain_properties'
                },
                'time_duration': {
                    'name': 'Time Duration',
                    'description': 'Simulation time duration',
                    'unit': 's',
                    'default': 1.0,
                    'range': [0.1, 10.0],
                    'category': 'temporal_properties'
                }
            },
            
            'wave': {
                'wave_speed': {
                    'name': 'Wave Speed (c)',
                    'description': 'Wave propagation speed in wave equation',
                    'unit': 'm/s',
                    'default': 340.0,
                    'range': [1.0, 10000.0],
                    'category': 'wave_properties',
                    'equation': '∂²u/∂t² = c²∂²u/∂x²'
                },
                'domain_size': {
                    'name': 'Domain Size',
                    'description': 'Spatial domain length',
                    'unit': 'm',
                    'default': 1.0,
                    'range': [0.1, 10.0],
                    'category': 'domain_properties'
                },
                'time_duration': {
                    'name': 'Time Duration',
                    'description': 'Simulation time duration',
                    'unit': 's',
                    'default': 2.0,
                    'range': [0.1, 10.0],
                    'category': 'temporal_properties'
                }
            },
            
            'shm': {
                'natural_frequency': {
                    'name': 'Natural Frequency (ω)',
                    'description': 'Natural frequency in simple harmonic motion',
                    'unit': 'rad/s',
                    'default': 1.0,
                    'range': [0.1, 100.0],
                    'category': 'mechanical_properties',
                    'equation': 'd²x/dt² + ω²x = 0'
                },
                'amplitude': {
                    'name': 'Amplitude',
                    'description': 'Oscillation amplitude',
                    'unit': 'm',
                    'default': 1.0,
                    'range': [0.1, 10.0],
                    'category': 'mechanical_properties'
                },
                'time_duration': {
                    'name': 'Time Duration',
                    'description': 'Simulation time duration',
                    'unit': 's',
                    'default': 10.0,
                    'range': [1.0, 100.0],
                    'category': 'temporal_properties'
                }
            },
            
            'helmholtz': {
                'wavenumber': {
                    'name': 'Wavenumber (k)',
                    'description': 'Wavenumber in Helmholtz equation',
                    'unit': '1/m',
                    'default': 1.0,
                    'range': [0.01, 100.0],
                    'category': 'wave_properties',
                    'equation': '∇²u + k²u = 0'
                },
                'domain_size': {
                    'name': 'Domain Size',
                    'description': 'Spatial domain length',
                    'unit': 'm',
                    'default': 1.0,
                    'range': [0.1, 10.0],
                    'category': 'domain_properties'
                }
            },
            
            'navier_stokes': {
                'viscosity': {
                    'name': 'Viscosity (μ)',
                    'description': 'Dynamic viscosity in Navier-Stokes equations',
                    'unit': 'Pa·s',
                    'default': 0.001,
                    'range': [1e-6, 1e-1],
                    'category': 'fluid_properties'
                },
                'density': {
                    'name': 'Density (ρ)',
                    'description': 'Fluid density',
                    'unit': 'kg/m³',
                    'default': 1000.0,
                    'range': [1.0, 20000.0],
                    'category': 'fluid_properties'
                },
                'domain_size': {
                    'name': 'Domain Size',
                    'description': 'Spatial domain dimensions',
                    'unit': 'm',
                    'default': 1.0,
                    'range': [0.1, 10.0],
                    'category': 'domain_properties'
                },
                'time_duration': {
                    'name': 'Time Duration',
                    'description': 'Simulation time duration',
                    'unit': 's',
                    'default': 1.0,
                    'range': [0.1, 10.0],
                    'category': 'temporal_properties'
                }
            },
            
            'schrodinger': {
                'planck_constant': {
                    'name': 'Planck Constant (ℏ)',
                    'description': 'Reduced Planck constant',
                    'unit': 'J·s',
                    'default': 1.055e-34,
                    'range': [1e-35, 1e-33],
                    'category': 'quantum_properties'
                },
                'mass': {
                    'name': 'Mass (m)',
                    'description': 'Particle mass',
                    'unit': 'kg',
                    'default': 9.109e-31,
                    'range': [1e-32, 1e-29],
                    'category': 'quantum_properties'
                },
                'potential_strength': {
                    'name': 'Potential Strength',
                    'description': 'Strength of potential energy',
                    'unit': 'J',
                    'default': 1e-20,
                    'range': [1e-25, 1e-15],
                    'category': 'quantum_properties'
                },
                'domain_size': {
                    'name': 'Domain Size',
                    'description': 'Spatial domain length',
                    'unit': 'm',
                    'default': 1e-9,
                    'range': [1e-12, 1e-6],
                    'category': 'domain_properties'
                },
                'time_duration': {
                    'name': 'Time Duration',
                    'description': 'Simulation time duration',
                    'unit': 's',
                    'default': 1e-15,
                    'range': [1e-18, 1e-12],
                    'category': 'temporal_properties'
                }
            },
            
            'maxwell': {
                'permittivity': {
                    'name': 'Permittivity (ε)',
                    'description': 'Electric permittivity',
                    'unit': 'F/m',
                    'default': 8.854e-12,
                    'range': [1e-13, 1e-10],
                    'category': 'electromagnetic_properties'
                },
                'magnetic_permeability': {
                    'name': 'Magnetic Permeability (μ)',
                    'description': 'Magnetic permeability',
                    'unit': 'H/m',
                    'default': 1.257e-6,
                    'range': [1e-7, 1e-5],
                    'category': 'electromagnetic_properties'
                },
                'domain_size': {
                    'name': 'Domain Size',
                    'description': 'Spatial domain dimensions',
                    'unit': 'm',
                    'default': 1.0,
                    'range': [0.1, 10.0],
                    'category': 'domain_properties'
                },
                'time_duration': {
                    'name': 'Time Duration',
                    'description': 'Simulation time duration',
                    'unit': 's',
                    'default': 1e-9,
                    'range': [1e-12, 1e-6],
                    'category': 'temporal_properties'
                }
            },
            
            'heat_transfer': {
                'thermal_conductivity': {
                    'name': 'Thermal Conductivity (k)',
                    'description': 'Thermal conductivity coefficient',
                    'unit': 'W/(m·K)',
                    'default': 50.0,
                    'range': [0.01, 1000.0],
                    'category': 'thermal_properties'
                },
                'density': {
                    'name': 'Density (ρ)',
                    'description': 'Material density',
                    'unit': 'kg/m³',
                    'default': 1000.0,
                    'range': [1.0, 20000.0],
                    'category': 'material_properties'
                },
                'specific_heat': {
                    'name': 'Specific Heat (c_p)',
                    'description': 'Specific heat capacity',
                    'unit': 'J/(kg·K)',
                    'default': 1000.0,
                    'range': [100.0, 10000.0],
                    'category': 'thermal_properties'
                },
                'heat_source': {
                    'name': 'Heat Source (Q)',
                    'description': 'Heat source/sink term',
                    'unit': 'W/m³',
                    'default': 0.0,
                    'range': [-1e6, 1e6],
                    'category': 'thermal_properties'
                },
                'domain_size': {
                    'name': 'Domain Size',
                    'description': 'Spatial domain dimensions',
                    'unit': 'm',
                    'default': 1.0,
                    'range': [0.1, 10.0],
                    'category': 'domain_properties'
                },
                'time_duration': {
                    'name': 'Time Duration',
                    'description': 'Simulation time duration',
                    'unit': 's',
                    'default': 1.0,
                    'range': [0.1, 10.0],
                    'category': 'temporal_properties'
                }
            },
            
            'elastic': {
                'elastic_modulus': {
                    'name': 'Elastic Modulus (E)',
                    'description': 'Young\'s modulus of elasticity',
                    'unit': 'GPa',
                    'default': 200.0,
                    'range': [0.1, 1000.0],
                    'category': 'mechanical_properties'
                },
                'poisson_ratio': {
                    'name': 'Poisson Ratio (ν)',
                    'description': 'Poisson\'s ratio',
                    'unit': 'dimensionless',
                    'default': 0.3,
                    'range': [0.0, 0.5],
                    'category': 'mechanical_properties'
                },
                'density': {
                    'name': 'Density (ρ)',
                    'description': 'Material density',
                    'unit': 'kg/m³',
                    'default': 1000.0,
                    'range': [1.0, 20000.0],
                    'category': 'material_properties'
                },
                'domain_size': {
                    'name': 'Domain Size',
                    'description': 'Spatial domain dimensions',
                    'unit': 'm',
                    'default': 1.0,
                    'range': [0.1, 10.0],
                    'category': 'domain_properties'
                }
            },
            
            'phase_field': {
                'mobility': {
                    'name': 'Mobility (M)',
                    'description': 'Phase field mobility coefficient',
                    'unit': 'm²/(J·s)',
                    'default': 1e-3,
                    'range': [1e-6, 1e-1],
                    'category': 'phase_field'
                },
                'interface_thickness': {
                    'name': 'Interface Thickness (ε)',
                    'description': 'Phase field interface thickness parameter',
                    'unit': 'm',
                    'default': 1e-6,
                    'range': [1e-9, 1e-3],
                    'category': 'phase_field'
                },
                'free_energy_barrier': {
                    'name': 'Free Energy Barrier (W)',
                    'description': 'Free energy barrier for phase transitions',
                    'unit': 'J/m³',
                    'default': 1e6,
                    'range': [1e3, 1e9],
                    'category': 'phase_field'
                },
                'domain_size': {
                    'name': 'Domain Size',
                    'description': 'Spatial domain dimensions',
                    'unit': 'm',
                    'default': 1e-3,
                    'range': [1e-6, 1e-1],
                    'category': 'domain_properties'
                },
                'time_duration': {
                    'name': 'Time Duration',
                    'description': 'Simulation time duration',
                    'unit': 's',
                    'default': 1.0,
                    'range': [0.1, 10.0],
                    'category': 'temporal_properties'
                }
            },
            
            'reaction_diffusion': {
                'diffusion_coefficient': {
                    'name': 'Diffusion Coefficient (D)',
                    'description': 'Diffusion coefficient for transport',
                    'unit': 'm²/s',
                    'default': 1e-9,
                    'range': [1e-12, 1e-6],
                    'category': 'transport_properties'
                },
                'reaction_rate': {
                    'name': 'Reaction Rate (k)',
                    'description': 'Chemical reaction rate constant',
                    'unit': '1/s',
                    'default': 1e-3,
                    'range': [1e-6, 1e0],
                    'category': 'chemical_properties'
                },
                'domain_size': {
                    'name': 'Domain Size',
                    'description': 'Spatial domain dimensions',
                    'unit': 'm',
                    'default': 1.0,
                    'range': [0.1, 10.0],
                    'category': 'domain_properties'
                },
                'time_duration': {
                    'name': 'Time Duration',
                    'description': 'Simulation time duration',
                    'unit': 's',
                    'default': 1.0,
                    'range': [0.1, 10.0],
                    'category': 'temporal_properties'
                }
            },
            
            'poroelasticity': {
                'permeability': {
                    'name': 'Permeability (κ)',
                    'description': 'Material permeability',
                    'unit': 'm²',
                    'default': 1e-12,
                    'range': [1e-20, 1e-8],
                    'category': 'poroelastic_properties'
                },
                'biot_coefficient': {
                    'name': 'Biot Coefficient (α)',
                    'description': 'Biot coefficient for poroelasticity',
                    'unit': 'dimensionless',
                    'default': 0.8,
                    'range': [0.0, 1.0],
                    'category': 'poroelastic_properties'
                },
                'elastic_modulus': {
                    'name': 'Elastic Modulus (E)',
                    'description': 'Young\'s modulus of elasticity',
                    'unit': 'GPa',
                    'default': 200.0,
                    'range': [0.1, 1000.0],
                    'category': 'mechanical_properties'
                },
                'poisson_ratio': {
                    'name': 'Poisson Ratio (ν)',
                    'description': 'Poisson\'s ratio',
                    'unit': 'dimensionless',
                    'default': 0.3,
                    'range': [0.0, 0.5],
                    'category': 'mechanical_properties'
                },
                'domain_size': {
                    'name': 'Domain Size',
                    'description': 'Spatial domain dimensions',
                    'unit': 'm',
                    'default': 1.0,
                    'range': [0.1, 10.0],
                    'category': 'domain_properties'
                },
                'time_duration': {
                    'name': 'Time Duration',
                    'description': 'Simulation time duration',
                    'unit': 's',
                    'default': 1.0,
                    'range': [0.1, 10.0],
                    'category': 'temporal_properties'
                }
            },
            
            'viscoelasticity': {
                'relaxation_time': {
                    'name': 'Relaxation Time (τ)',
                    'description': 'Viscoelastic relaxation time',
                    'unit': 's',
                    'default': 1.0,
                    'range': [1e-3, 1e3],
                    'category': 'viscoelastic_properties'
                },
                'retardation_time': {
                    'name': 'Retardation Time (τ_r)',
                    'description': 'Viscoelastic retardation time',
                    'unit': 's',
                    'default': 0.1,
                    'range': [1e-4, 1e2],
                    'category': 'viscoelastic_properties'
                },
                'elastic_modulus': {
                    'name': 'Elastic Modulus (E)',
                    'description': 'Young\'s modulus of elasticity',
                    'unit': 'GPa',
                    'default': 200.0,
                    'range': [0.1, 1000.0],
                    'category': 'mechanical_properties'
                },
                'domain_size': {
                    'name': 'Domain Size',
                    'description': 'Spatial domain dimensions',
                    'unit': 'm',
                    'default': 1.0,
                    'range': [0.1, 10.0],
                    'category': 'domain_properties'
                },
                'time_duration': {
                    'name': 'Time Duration',
                    'description': 'Simulation time duration',
                    'unit': 's',
                    'default': 1.0,
                    'range': [0.1, 10.0],
                    'category': 'temporal_properties'
                }
            },
            
            'radiative_transfer': {
                'absorption_coefficient': {
                    'name': 'Absorption Coefficient (κ)',
                    'description': 'Radiation absorption coefficient',
                    'unit': '1/m',
                    'default': 1.0,
                    'range': [1e-3, 1e3],
                    'category': 'radiation_properties'
                },
                'scattering_coefficient': {
                    'name': 'Scattering Coefficient (σ)',
                    'description': 'Radiation scattering coefficient',
                    'unit': '1/m',
                    'default': 0.1,
                    'range': [1e-4, 1e2],
                    'category': 'radiation_properties'
                },
                'domain_size': {
                    'name': 'Domain Size',
                    'description': 'Spatial domain dimensions',
                    'unit': 'm',
                    'default': 1.0,
                    'range': [0.1, 10.0],
                    'category': 'domain_properties'
                }
            },
            
            'shallow_water': {
                'gravity': {
                    'name': 'Gravity (g)',
                    'description': 'Acceleration due to gravity',
                    'unit': 'm/s²',
                    'default': 9.81,
                    'range': [1.0, 20.0],
                    'category': 'geophysical_properties'
                },
                'coriolis_parameter': {
                    'name': 'Coriolis Parameter (f)',
                    'description': 'Coriolis parameter for geophysical flows',
                    'unit': '1/s',
                    'default': 1e-4,
                    'range': [1e-5, 1e-3],
                    'category': 'geophysical_properties'
                },
                'domain_size': {
                    'name': 'Domain Size',
                    'description': 'Spatial domain dimensions',
                    'unit': 'm',
                    'default': 1000.0,
                    'range': [100.0, 10000.0],
                    'category': 'domain_properties'
                },
                'time_duration': {
                    'name': 'Time Duration',
                    'description': 'Simulation time duration',
                    'unit': 's',
                    'default': 3600.0,
                    'range': [100.0, 86400.0],
                    'category': 'temporal_properties'
                }
            }
        }
        
        return equation_params.get(eq_id, {})
    
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