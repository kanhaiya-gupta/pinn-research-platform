"""
Generalization Parameters
Parameters for improving model generalization and transfer learning.
"""

GENERALIZATION_PARAMETERS_DICT = {
    # Regularization Parameters
    'l1_regularization': {
        'name': 'L1 Regularization',
        'description': 'L1 regularization coefficient',
        'unit': 'dimensionless',
        'default': 0.0,
        'range': [0.0, 1.0],
        'category': 'regularization_parameters',
        'generalization_method': 'sparsity'
    },
    'l2_regularization': {
        'name': 'L2 Regularization',
        'description': 'L2 regularization coefficient',
        'unit': 'dimensionless',
        'default': 1e-6,
        'range': [0.0, 1e-3],
        'category': 'regularization_parameters',
        'generalization_method': 'weight_decay'
    },
    'dropout_rate': {
        'name': 'Dropout Rate',
        'description': 'Dropout rate for regularization',
        'unit': 'dimensionless',
        'default': 0.1,
        'range': [0.0, 0.5],
        'category': 'regularization_parameters',
        'generalization_method': 'dropout'
    },
    'batch_normalization': {
        'name': 'Batch Normalization',
        'description': 'Whether to use batch normalization',
        'unit': 'dimensionless',
        'default': True,
        'range': [True, False],
        'category': 'regularization_parameters',
        'generalization_method': 'normalization'
    },
    
    # Data Augmentation Parameters
    'noise_level': {
        'name': 'Noise Level',
        'description': 'Level of noise for data augmentation',
        'unit': 'dimensionless',
        'default': 0.01,
        'range': [0.0, 0.1],
        'category': 'data_augmentation_parameters',
        'generalization_method': 'noise_injection'
    },
    'scaling_factor': {
        'name': 'Scaling Factor',
        'description': 'Scaling factor for data augmentation',
        'unit': 'dimensionless',
        'default': 0.1,
        'range': [0.0, 1.0],
        'category': 'data_augmentation_parameters',
        'generalization_method': 'scaling'
    },
    'rotation_angle': {
        'name': 'Rotation Angle',
        'description': 'Rotation angle for data augmentation',
        'unit': 'degrees',
        'default': 5.0,
        'range': [0.0, 45.0],
        'category': 'data_augmentation_parameters',
        'generalization_method': 'rotation'
    },
    'translation_range': {
        'name': 'Translation Range',
        'description': 'Translation range for data augmentation',
        'unit': 'dimensionless',
        'default': 0.1,
        'range': [0.0, 1.0],
        'category': 'data_augmentation_parameters',
        'generalization_method': 'translation'
    },
    
    # Cross-Validation Parameters
    'cross_validation_folds': {
        'name': 'Cross Validation Folds',
        'description': 'Number of folds for cross validation',
        'unit': 'dimensionless',
        'default': 5,
        'range': [2, 10],
        'category': 'cross_validation_parameters',
        'generalization_method': 'cross_validation'
    },
    'stratified_sampling': {
        'name': 'Stratified Sampling',
        'description': 'Whether to use stratified sampling',
        'unit': 'dimensionless',
        'default': True,
        'range': [True, False],
        'category': 'cross_validation_parameters',
        'generalization_method': 'cross_validation'
    },
    'leave_one_out': {
        'name': 'Leave One Out',
        'description': 'Whether to use leave-one-out validation',
        'unit': 'dimensionless',
        'default': False,
        'range': [True, False],
        'category': 'cross_validation_parameters',
        'generalization_method': 'cross_validation'
    },
    
    # Transfer Learning Parameters
    'transfer_learning': {
        'name': 'Transfer Learning',
        'description': 'Whether to use transfer learning',
        'unit': 'dimensionless',
        'default': False,
        'range': [True, False],
        'category': 'transfer_learning_parameters',
        'generalization_method': 'transfer_learning'
    },
    'pretrained_model': {
        'name': 'Pretrained Model',
        'description': 'Path to pretrained model',
        'unit': 'dimensionless',
        'default': '',
        'range': ['', 'path_to_model'],
        'category': 'transfer_learning_parameters',
        'generalization_method': 'transfer_learning'
    },
    'fine_tuning_layers': {
        'name': 'Fine Tuning Layers',
        'description': 'Number of layers to fine-tune',
        'unit': 'dimensionless',
        'default': 2,
        'range': [0, 10],
        'category': 'transfer_learning_parameters',
        'generalization_method': 'transfer_learning'
    },
    'freeze_layers': {
        'name': 'Freeze Layers',
        'description': 'Whether to freeze pretrained layers',
        'unit': 'dimensionless',
        'default': True,
        'range': [True, False],
        'category': 'transfer_learning_parameters',
        'generalization_method': 'transfer_learning'
    },
    
    # Domain Adaptation Parameters
    'domain_adaptation': {
        'name': 'Domain Adaptation',
        'description': 'Whether to use domain adaptation',
        'unit': 'dimensionless',
        'default': False,
        'range': [True, False],
        'category': 'domain_adaptation_parameters',
        'generalization_method': 'domain_adaptation'
    },
    'domain_loss_weight': {
        'name': 'Domain Loss Weight',
        'description': 'Weight for domain adaptation loss',
        'unit': 'dimensionless',
        'default': 1.0,
        'range': [0.0, 10.0],
        'category': 'domain_adaptation_parameters',
        'generalization_method': 'domain_adaptation'
    },
    'adversarial_training': {
        'name': 'Adversarial Training',
        'description': 'Whether to use adversarial training',
        'unit': 'dimensionless',
        'default': False,
        'range': [True, False],
        'category': 'domain_adaptation_parameters',
        'generalization_method': 'domain_adaptation'
    },
    
    # Ensemble Parameters
    'ensemble_size': {
        'name': 'Ensemble Size',
        'description': 'Number of models in ensemble',
        'unit': 'dimensionless',
        'default': 5,
        'range': [2, 20],
        'category': 'ensemble_parameters',
        'generalization_method': 'ensemble_learning'
    },
    'ensemble_method': {
        'name': 'Ensemble Method',
        'description': 'Method for ensemble combination',
        'unit': 'dimensionless',
        'default': 'average',
        'range': ['average', 'weighted', 'stacking', 'boosting'],
        'category': 'ensemble_parameters',
        'generalization_method': 'ensemble_learning'
    },
    'bootstrap_sampling': {
        'name': 'Bootstrap Sampling',
        'description': 'Whether to use bootstrap sampling',
        'unit': 'dimensionless',
        'default': True,
        'range': [True, False],
        'category': 'ensemble_parameters',
        'generalization_method': 'ensemble_learning'
    },
    
    # Physics-Informed Parameters
    'physics_weight': {
        'name': 'Physics Weight',
        'description': 'Weight for physics-informed terms',
        'unit': 'dimensionless',
        'default': 1.0,
        'range': [0.0, 10.0],
        'category': 'physics_informed_parameters',
        'generalization_method': 'physics_informed'
    },
    'boundary_weight': {
        'name': 'Boundary Weight',
        'description': 'Weight for boundary conditions',
        'unit': 'dimensionless',
        'default': 1.0,
        'range': [0.0, 10.0],
        'category': 'physics_informed_parameters',
        'generalization_method': 'physics_informed'
    },
    'initial_weight': {
        'name': 'Initial Weight',
        'description': 'Weight for initial conditions',
        'unit': 'dimensionless',
        'default': 1.0,
        'range': [0.0, 10.0],
        'category': 'physics_informed_parameters',
        'generalization_method': 'physics_informed'
    },
    'data_weight': {
        'name': 'Data Weight',
        'description': 'Weight for observational data',
        'unit': 'dimensionless',
        'default': 1.0,
        'range': [0.0, 10.0],
        'category': 'physics_informed_parameters',
        'generalization_method': 'physics_informed'
    },
    
    # Multi-Scale Parameters
    'multi_scale_training': {
        'name': 'Multi-Scale Training',
        'description': 'Whether to use multi-scale training',
        'unit': 'dimensionless',
        'default': False,
        'range': [True, False],
        'category': 'multi_scale_parameters',
        'generalization_method': 'multi_scale'
    },
    'scale_factors': {
        'name': 'Scale Factors',
        'description': 'Scale factors for multi-scale training',
        'unit': 'dimensionless',
        'default': [0.5, 1.0, 2.0],
        'range': [0.1, 10.0],
        'category': 'multi_scale_parameters',
        'generalization_method': 'multi_scale'
    },
    'scale_weights': {
        'name': 'Scale Weights',
        'description': 'Weights for different scales',
        'unit': 'dimensionless',
        'default': [1.0, 1.0, 1.0],
        'range': [0.0, 10.0],
        'category': 'multi_scale_parameters',
        'generalization_method': 'multi_scale'
    },
    
    # Curriculum Learning Parameters
    'curriculum_learning': {
        'name': 'Curriculum Learning',
        'description': 'Whether to use curriculum learning',
        'unit': 'dimensionless',
        'default': False,
        'range': [True, False],
        'category': 'curriculum_parameters',
        'generalization_method': 'curriculum_learning'
    },
    'difficulty_metric': {
        'name': 'Difficulty Metric',
        'description': 'Metric for measuring sample difficulty',
        'unit': 'dimensionless',
        'default': 'loss',
        'range': ['loss', 'gradient', 'uncertainty'],
        'category': 'curriculum_parameters',
        'generalization_method': 'curriculum_learning'
    },
    'curriculum_schedule': {
        'name': 'Curriculum Schedule',
        'description': 'Schedule for curriculum progression',
        'unit': 'dimensionless',
        'default': 'linear',
        'range': ['linear', 'exponential', 'step'],
        'category': 'curriculum_parameters',
        'generalization_method': 'curriculum_learning'
    },
    
    # Validation Parameters
    'validation_frequency': {
        'name': 'Validation Frequency',
        'description': 'Frequency of validation during training',
        'unit': 'dimensionless',
        'default': 100,
        'range': [10, 1000],
        'category': 'validation_parameters',
        'generalization_method': 'validation'
    },
    'early_stopping': {
        'name': 'Early Stopping',
        'description': 'Whether to use early stopping',
        'unit': 'dimensionless',
        'default': True,
        'range': [True, False],
        'category': 'validation_parameters',
        'generalization_method': 'validation'
    },
    'patience': {
        'name': 'Patience',
        'description': 'Patience for early stopping',
        'unit': 'dimensionless',
        'default': 100,
        'range': [10, 1000],
        'category': 'validation_parameters',
        'generalization_method': 'validation'
    },
    
    # Model Selection Parameters
    'model_selection': {
        'name': 'Model Selection',
        'description': 'Method for model selection',
        'unit': 'dimensionless',
        'default': 'validation_loss',
        'range': ['validation_loss', 'aic', 'bic', 'cross_validation'],
        'category': 'model_selection_parameters',
        'generalization_method': 'model_selection'
    },
    'hyperparameter_tuning': {
        'name': 'Hyperparameter Tuning',
        'description': 'Method for hyperparameter tuning',
        'unit': 'dimensionless',
        'default': 'grid_search',
        'range': ['grid_search', 'random_search', 'bayesian', 'genetic'],
        'category': 'model_selection_parameters',
        'generalization_method': 'model_selection'
    }
}

# Equation-specific parameters for generalization equations
GENERALIZATION_EQUATION_PARAMETERS = {
    'generalization_burgers': {
        'viscosity': {
            'name': 'Viscosity (ν)',
            'description': 'Dynamic viscosity coefficient for Burgers equation',
            'unit': 'm²/s',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'fluid_properties',
            'generalization_method': 'parameter_variation'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for Burgers equation',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'generalization_method': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for Burgers equation',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties',
            'generalization_method': 'temporal_scaling'
        },
        'initial_condition': {
            'name': 'Initial Condition',
            'description': 'Type of initial condition for Burgers equation',
            'unit': 'dimensionless',
            'default': 'sinusoidal',
            'range': ['sinusoidal', 'gaussian', 'step'],
            'category': 'initial_conditions',
            'generalization_method': 'condition_variation'
        },
        'boundary_condition': {
            'name': 'Boundary Condition',
            'description': 'Type of boundary condition for Burgers equation',
            'unit': 'dimensionless',
            'default': 'periodic',
            'range': ['periodic', 'dirichlet', 'neumann'],
            'category': 'boundary_conditions',
            'generalization_method': 'condition_variation'
        }
    },
    'generalization_heat': {
        'thermal_diffusivity': {
            'name': 'Thermal Diffusivity (α)',
            'description': 'Thermal diffusivity coefficient for heat equation',
            'unit': 'm²/s',
            'default': 1e-5,
            'range': [1e-6, 1e-4],
            'category': 'thermal_properties',
            'generalization_method': 'parameter_variation'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for heat equation',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'generalization_method': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for heat equation',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties',
            'generalization_method': 'temporal_scaling'
        },
        'initial_temperature': {
            'name': 'Initial Temperature',
            'description': 'Initial temperature for heat equation',
            'unit': '°C',
            'default': 0.0,
            'range': [-100.0, 100.0],
            'category': 'initial_conditions',
            'generalization_method': 'condition_variation'
        },
        'boundary_temperature': {
            'name': 'Boundary Temperature',
            'description': 'Boundary temperature for heat equation',
            'unit': '°C',
            'default': 100.0,
            'range': [0.0, 500.0],
            'category': 'boundary_conditions',
            'generalization_method': 'condition_variation'
        }
    },
    'generalization_wave': {
        'wave_speed': {
            'name': 'Wave Speed (c)',
            'description': 'Wave propagation speed for wave equation',
            'unit': 'm/s',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'wave_properties',
            'generalization_method': 'parameter_variation'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for wave equation',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'generalization_method': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for wave equation',
            'unit': 's',
            'default': 2.0,
            'range': [0.5, 10.0],
            'category': 'temporal_properties',
            'generalization_method': 'temporal_scaling'
        },
        'initial_displacement': {
            'name': 'Initial Displacement',
            'description': 'Type of initial displacement for wave equation',
            'unit': 'dimensionless',
            'default': 'gaussian',
            'range': ['gaussian', 'sinusoidal', 'pulse'],
            'category': 'initial_conditions',
            'generalization_method': 'condition_variation'
        },
        'boundary_condition': {
            'name': 'Boundary Condition',
            'description': 'Type of boundary condition for wave equation',
            'unit': 'dimensionless',
            'default': 'absorbing',
            'range': ['absorbing', 'reflecting', 'periodic'],
            'category': 'boundary_conditions',
            'generalization_method': 'condition_variation'
        }
    },
    'generalization_shm': {
        'natural_frequency': {
            'name': 'Natural Frequency (ω)',
            'description': 'Natural frequency for simple harmonic motion',
            'unit': 'rad/s',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'mechanical_properties',
            'generalization_method': 'parameter_variation'
        },
        'damping_ratio': {
            'name': 'Damping Ratio (ζ)',
            'description': 'Damping ratio for simple harmonic motion',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'mechanical_properties',
            'generalization_method': 'parameter_variation'
        },
        'initial_amplitude': {
            'name': 'Initial Amplitude',
            'description': 'Initial amplitude for simple harmonic motion',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'initial_conditions',
            'generalization_method': 'condition_variation'
        },
        'initial_phase': {
            'name': 'Initial Phase',
            'description': 'Initial phase for simple harmonic motion',
            'unit': 'rad',
            'default': 0.0,
            'range': [0.0, 2*3.14159],
            'category': 'initial_conditions',
            'generalization_method': 'condition_variation'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for simple harmonic motion',
            'unit': 's',
            'default': 10.0,
            'range': [1.0, 100.0],
            'category': 'temporal_properties',
            'generalization_method': 'temporal_scaling'
        }
    },
    'generalization_helmholtz': {
        'wavenumber': {
            'name': 'Wavenumber (k)',
            'description': 'Wavenumber for Helmholtz equation',
            'unit': '1/m',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'wave_properties',
            'generalization_method': 'parameter_variation'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for Helmholtz equation',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'generalization_method': 'spatial_scaling'
        },
        'boundary_condition': {
            'name': 'Boundary Condition',
            'description': 'Type of boundary condition for Helmholtz equation',
            'unit': 'dimensionless',
            'default': 'dirichlet',
            'range': ['dirichlet', 'neumann', 'mixed'],
            'category': 'boundary_conditions',
            'generalization_method': 'condition_variation'
        },
        'source_strength': {
            'name': 'Source Strength',
            'description': 'Strength of source term in Helmholtz equation',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'source_terms',
            'generalization_method': 'parameter_variation'
        },
        'absorption_coefficient': {
            'name': 'Absorption Coefficient',
            'description': 'Absorption coefficient for Helmholtz equation',
            'unit': '1/m',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'material_properties',
            'generalization_method': 'parameter_variation'
        }
    },
    'generalization_navier_stokes': {
        'reynolds_number': {
            'name': 'Reynolds Number (Re)',
            'description': 'Reynolds number for Navier-Stokes equations',
            'unit': 'dimensionless',
            'default': 100.0,
            'range': [1.0, 1000.0],
            'category': 'flow_properties',
            'generalization_method': 'parameter_variation'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for Navier-Stokes equations',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'generalization_method': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for Navier-Stokes equations',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties',
            'generalization_method': 'temporal_scaling'
        },
        'inlet_velocity': {
            'name': 'Inlet Velocity',
            'description': 'Inlet velocity for Navier-Stokes equations',
            'unit': 'm/s',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'boundary_conditions',
            'generalization_method': 'condition_variation'
        },
        'pressure_gradient': {
            'name': 'Pressure Gradient',
            'description': 'Pressure gradient for Navier-Stokes equations',
            'unit': 'Pa/m',
            'default': 0.0,
            'range': [-10.0, 10.0],
            'category': 'boundary_conditions',
            'generalization_method': 'condition_variation'
        }
    },
    'generalization_schrodinger': {
        'planck_constant': {
            'name': 'Planck Constant (ℏ)',
            'description': 'Reduced Planck constant for Schrödinger equation',
            'unit': 'J·s',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'quantum_properties',
            'generalization_method': 'parameter_variation'
        },
        'mass': {
            'name': 'Mass (m)',
            'description': 'Particle mass for Schrödinger equation',
            'unit': 'kg',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'quantum_properties',
            'generalization_method': 'parameter_variation'
        },
        'potential_strength': {
            'name': 'Potential Strength',
            'description': 'Strength of potential energy for Schrödinger equation',
            'unit': 'J',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'quantum_properties',
            'generalization_method': 'parameter_variation'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for Schrödinger equation',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'generalization_method': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for Schrödinger equation',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties',
            'generalization_method': 'temporal_scaling'
        }
    },
    'generalization_maxwell': {
        'permittivity': {
            'name': 'Permittivity (ε)',
            'description': 'Electric permittivity for Maxwell equations',
            'unit': 'F/m',
            'default': 8.85e-12,
            'range': [1e-12, 1e-10],
            'category': 'electromagnetic_properties',
            'generalization_method': 'parameter_variation'
        },
        'permeability': {
            'name': 'Permeability (μ)',
            'description': 'Magnetic permeability for Maxwell equations',
            'unit': 'H/m',
            'default': 1.26e-6,
            'range': [1e-7, 1e-5],
            'category': 'electromagnetic_properties',
            'generalization_method': 'parameter_variation'
        },
        'conductivity': {
            'name': 'Conductivity (σ)',
            'description': 'Electrical conductivity for Maxwell equations',
            'unit': 'S/m',
            'default': 1e-6,
            'range': [1e-8, 1e-4],
            'category': 'electromagnetic_properties',
            'generalization_method': 'parameter_variation'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for Maxwell equations',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'generalization_method': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for Maxwell equations',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties',
            'generalization_method': 'temporal_scaling'
        }
    },
    'generalization_heat_transfer': {
        'thermal_conductivity': {
            'name': 'Thermal Conductivity (k)',
            'description': 'Thermal conductivity for heat transfer equation',
            'unit': 'W/(m·K)',
            'default': 50.0,
            'range': [1.0, 500.0],
            'category': 'thermal_properties',
            'generalization_method': 'parameter_variation'
        },
        'density': {
            'name': 'Density (ρ)',
            'description': 'Material density for heat transfer equation',
            'unit': 'kg/m³',
            'default': 2700.0,
            'range': [100.0, 10000.0],
            'category': 'material_properties',
            'generalization_method': 'parameter_variation'
        },
        'specific_heat': {
            'name': 'Specific Heat (c_p)',
            'description': 'Specific heat capacity for heat transfer equation',
            'unit': 'J/(kg·K)',
            'default': 900.0,
            'range': [100.0, 5000.0],
            'category': 'thermal_properties',
            'generalization_method': 'parameter_variation'
        },
        'heat_source': {
            'name': 'Heat Source (Q)',
            'description': 'Heat source term for heat transfer equation',
            'unit': 'W/m³',
            'default': 0.0,
            'range': [0.0, 1000000.0],
            'category': 'source_terms',
            'generalization_method': 'parameter_variation'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for heat transfer equation',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'generalization_method': 'spatial_scaling'
        }
    },
    'generalization_elastic': {
        'young_modulus': {
            'name': 'Young Modulus (E)',
            'description': 'Young modulus for elasticity equations',
            'unit': 'Pa',
            'default': 200e9,
            'range': [1e9, 1000e9],
            'category': 'mechanical_properties',
            'generalization_method': 'parameter_variation'
        },
        'poisson_ratio': {
            'name': 'Poisson Ratio (ν)',
            'description': 'Poisson ratio for elasticity equations',
            'unit': 'dimensionless',
            'default': 0.3,
            'range': [0.0, 0.5],
            'category': 'mechanical_properties',
            'generalization_method': 'parameter_variation'
        },
        'density': {
            'name': 'Density (ρ)',
            'description': 'Material density for elasticity equations',
            'unit': 'kg/m³',
            'default': 2700.0,
            'range': [100.0, 10000.0],
            'category': 'material_properties',
            'generalization_method': 'parameter_variation'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for elasticity equations',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'generalization_method': 'spatial_scaling'
        },
        'applied_force': {
            'name': 'Applied Force',
            'description': 'Applied force for elasticity equations',
            'unit': 'N',
            'default': 1000.0,
            'range': [100.0, 10000.0],
            'category': 'boundary_conditions',
            'generalization_method': 'condition_variation'
        }
    },
    'generalization_phase_field': {
        'mobility': {
            'name': 'Mobility (M)',
            'description': 'Phase field mobility coefficient',
            'unit': 'm²/(J·s)',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'phase_field_properties',
            'generalization_method': 'parameter_variation'
        },
        'interface_thickness': {
            'name': 'Interface Thickness',
            'description': 'Thickness of phase interface',
            'unit': 'm',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'phase_field_properties',
            'generalization_method': 'parameter_variation'
        },
        'free_energy_barrier': {
            'name': 'Free Energy Barrier',
            'description': 'Free energy barrier for phase transition',
            'unit': 'J/m³',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'phase_field_properties',
            'generalization_method': 'parameter_variation'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for phase field equation',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'generalization_method': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for phase field equation',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties',
            'generalization_method': 'temporal_scaling'
        }
    },
    'generalization_reaction_diffusion': {
        'diffusion_coefficient': {
            'name': 'Diffusion Coefficient (D)',
            'description': 'Diffusion coefficient for reaction-diffusion equation',
            'unit': 'm²/s',
            'default': 1e-9,
            'range': [1e-10, 1e-8],
            'category': 'transport_properties',
            'generalization_method': 'parameter_variation'
        },
        'reaction_rate': {
            'name': 'Reaction Rate (k)',
            'description': 'Chemical reaction rate for reaction-diffusion equation',
            'unit': '1/s',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'chemical_properties',
            'generalization_method': 'parameter_variation'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for reaction-diffusion equation',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'generalization_method': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for reaction-diffusion equation',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties',
            'generalization_method': 'temporal_scaling'
        },
        'initial_concentration': {
            'name': 'Initial Concentration',
            'description': 'Initial concentration for reaction-diffusion equation',
            'unit': 'dimensionless',
            'default': 0.5,
            'range': [0.0, 1.0],
            'category': 'initial_conditions',
            'generalization_method': 'condition_variation'
        }
    },
    'generalization_poroelasticity': {
        'permeability': {
            'name': 'Permeability (k)',
            'description': 'Hydraulic permeability for poroelasticity equations',
            'unit': 'm²',
            'default': 1e-12,
            'range': [1e-15, 1e-9],
            'category': 'poroelastic_properties',
            'generalization_method': 'parameter_variation'
        },
        'porosity': {
            'name': 'Porosity (φ)',
            'description': 'Material porosity for poroelasticity equations',
            'unit': 'dimensionless',
            'default': 0.2,
            'range': [0.01, 0.5],
            'category': 'poroelastic_properties',
            'generalization_method': 'parameter_variation'
        },
        'biot_coefficient': {
            'name': 'Biot Coefficient (α)',
            'description': 'Biot coefficient for poroelasticity equations',
            'unit': 'dimensionless',
            'default': 0.8,
            'range': [0.1, 1.0],
            'category': 'poroelastic_properties',
            'generalization_method': 'parameter_variation'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for poroelasticity equations',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'generalization_method': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for poroelasticity equations',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties',
            'generalization_method': 'temporal_scaling'
        }
    },
    'generalization_viscoelasticity': {
        'elastic_modulus': {
            'name': 'Elastic Modulus (E)',
            'description': 'Elastic modulus for viscoelasticity equation',
            'unit': 'Pa',
            'default': 1e9,
            'range': [1e8, 1e10],
            'category': 'mechanical_properties',
            'generalization_method': 'parameter_variation'
        },
        'viscosity': {
            'name': 'Viscosity (η)',
            'description': 'Viscosity for viscoelasticity equation',
            'unit': 'Pa·s',
            'default': 1e6,
            'range': [1e5, 1e7],
            'category': 'mechanical_properties',
            'generalization_method': 'parameter_variation'
        },
        'relaxation_time': {
            'name': 'Relaxation Time (τ)',
            'description': 'Relaxation time for viscoelasticity equation',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'mechanical_properties',
            'generalization_method': 'parameter_variation'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for viscoelasticity equation',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'generalization_method': 'spatial_scaling'
        },
        'applied_strain': {
            'name': 'Applied Strain',
            'description': 'Applied strain for viscoelasticity equation',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'boundary_conditions',
            'generalization_method': 'condition_variation'
        }
    },
    'generalization_radiative_transfer': {
        'absorption_coefficient': {
            'name': 'Absorption Coefficient (κ)',
            'description': 'Absorption coefficient for radiative transfer equation',
            'unit': '1/m',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'optical_properties',
            'generalization_method': 'parameter_variation'
        },
        'scattering_coefficient': {
            'name': 'Scattering Coefficient (σ)',
            'description': 'Scattering coefficient for radiative transfer equation',
            'unit': '1/m',
            'default': 0.1,
            'range': [0.01, 1.0],
            'category': 'optical_properties',
            'generalization_method': 'parameter_variation'
        },
        'refractive_index': {
            'name': 'Refractive Index (n)',
            'description': 'Refractive index for radiative transfer equation',
            'unit': 'dimensionless',
            'default': 1.5,
            'range': [1.0, 3.0],
            'category': 'optical_properties',
            'generalization_method': 'parameter_variation'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for radiative transfer equation',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'generalization_method': 'spatial_scaling'
        },
        'source_intensity': {
            'name': 'Source Intensity',
            'description': 'Source intensity for radiative transfer equation',
            'unit': 'W/m²',
            'default': 1000.0,
            'range': [100.0, 10000.0],
            'category': 'source_terms',
            'generalization_method': 'parameter_variation'
        }
    },
    'generalization_shallow_water': {
        'gravity': {
            'name': 'Gravity (g)',
            'description': 'Gravitational acceleration for shallow water equations',
            'unit': 'm/s²',
            'default': 9.81,
            'range': [1.0, 20.0],
            'category': 'geophysical_properties',
            'generalization_method': 'parameter_variation'
        },
        'water_depth': {
            'name': 'Water Depth (h)',
            'description': 'Average water depth for shallow water equations',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'geophysical_properties',
            'generalization_method': 'parameter_variation'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for shallow water equations',
            'unit': 'm',
            'default': 100.0,
            'range': [10.0, 1000.0],
            'category': 'domain_properties',
            'generalization_method': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for shallow water equations',
            'unit': 's',
            'default': 10.0,
            'range': [1.0, 100.0],
            'category': 'temporal_properties',
            'generalization_method': 'temporal_scaling'
        },
        'initial_wave_height': {
            'name': 'Initial Wave Height',
            'description': 'Initial wave height for shallow water equations',
            'unit': 'm',
            'default': 0.1,
            'range': [0.01, 1.0],
            'category': 'initial_conditions',
            'generalization_method': 'condition_variation'
        }
    },
    'generalization_magnetohydrodynamics': {
        'magnetic_field': {
            'name': 'Magnetic Field (B)',
            'description': 'Magnetic field strength for MHD equations',
            'unit': 'T',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'electromagnetic_properties',
            'generalization_method': 'parameter_variation'
        },
        'plasma_density': {
            'name': 'Plasma Density (ρ)',
            'description': 'Plasma density for MHD equations',
            'unit': '1/m³',
            'default': 1e19,
            'range': [1e18, 1e20],
            'category': 'plasma_properties',
            'generalization_method': 'parameter_variation'
        },
        'temperature': {
            'name': 'Temperature (T)',
            'description': 'Plasma temperature for MHD equations',
            'unit': 'K',
            'default': 1e6,
            'range': [1e5, 1e7],
            'category': 'thermal_properties',
            'generalization_method': 'parameter_variation'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for MHD equations',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'generalization_method': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for MHD equations',
            'unit': 's',
            'default': 1e-6,
            'range': [1e-7, 1e-5],
            'category': 'temporal_properties',
            'generalization_method': 'temporal_scaling'
        }
    },
    'generalization_thermoelasticity': {
        'thermal_expansion': {
            'name': 'Thermal Expansion (α)',
            'description': 'Thermal expansion coefficient for thermoelasticity equations',
            'unit': '1/K',
            'default': 2.3e-5,
            'range': [1e-6, 1e-4],
            'category': 'thermal_properties',
            'generalization_method': 'parameter_variation'
        },
        'thermal_conductivity': {
            'name': 'Thermal Conductivity (k)',
            'description': 'Thermal conductivity for thermoelasticity equations',
            'unit': 'W/(m·K)',
            'default': 50.0,
            'range': [1.0, 500.0],
            'category': 'thermal_properties',
            'generalization_method': 'parameter_variation'
        },
        'elastic_modulus': {
            'name': 'Elastic Modulus (E)',
            'description': 'Elastic modulus for thermoelasticity equations',
            'unit': 'Pa',
            'default': 200e9,
            'range': [1e9, 1000e9],
            'category': 'mechanical_properties',
            'generalization_method': 'parameter_variation'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for thermoelasticity equations',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'generalization_method': 'spatial_scaling'
        },
        'temperature_difference': {
            'name': 'Temperature Difference (ΔT)',
            'description': 'Temperature difference for thermoelasticity equations',
            'unit': 'K',
            'default': 100.0,
            'range': [10.0, 1000.0],
            'category': 'thermal_properties',
            'generalization_method': 'parameter_variation'
        }
    },
    'generalization_advection_diffusion': {
        'velocity': {
            'name': 'Velocity (v)',
            'description': 'Flow velocity for advection-diffusion equation',
            'unit': 'm/s',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'flow_properties',
            'generalization_method': 'parameter_variation'
        },
        'diffusion_coefficient': {
            'name': 'Diffusion Coefficient (D)',
            'description': 'Diffusion coefficient for advection-diffusion equation',
            'unit': 'm²/s',
            'default': 1e-9,
            'range': [1e-10, 1e-8],
            'category': 'transport_properties',
            'generalization_method': 'parameter_variation'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for advection-diffusion equation',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'generalization_method': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for advection-diffusion equation',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties',
            'generalization_method': 'temporal_scaling'
        },
        'initial_concentration': {
            'name': 'Initial Concentration',
            'description': 'Initial concentration for advection-diffusion equation',
            'unit': 'kg/m³',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'initial_conditions',
            'generalization_method': 'condition_variation'
        }
    },
    'generalization_elastic_wave': {
        'p_wave_speed': {
            'name': 'P-Wave Speed (c_p)',
            'description': 'P-wave propagation speed for elastic wave equation',
            'unit': 'm/s',
            'default': 5000.0,
            'range': [1000.0, 10000.0],
            'category': 'wave_properties',
            'generalization_method': 'parameter_variation'
        },
        's_wave_speed': {
            'name': 'S-Wave Speed (c_s)',
            'description': 'S-wave propagation speed for elastic wave equation',
            'unit': 'm/s',
            'default': 3000.0,
            'range': [500.0, 6000.0],
            'category': 'wave_properties',
            'generalization_method': 'parameter_variation'
        },
        'density': {
            'name': 'Density (ρ)',
            'description': 'Material density for elastic wave equation',
            'unit': 'kg/m³',
            'default': 2700.0,
            'range': [1000.0, 8000.0],
            'category': 'material_properties',
            'generalization_method': 'parameter_variation'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for elastic wave equation',
            'unit': 'm',
            'default': 1000.0,
            'range': [100.0, 10000.0],
            'category': 'domain_properties',
            'generalization_method': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for elastic wave equation',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties',
            'generalization_method': 'temporal_scaling'
        }
    },
    'generalization_fluid_structure_interaction': {
        'fluid_density': {
            'name': 'Fluid Density (ρ)',
            'description': 'Density of the fluid in FSI problems',
            'unit': 'kg/m³',
            'default': 1000.0,
            'range': [100.0, 2000.0],
            'category': 'material_properties',
            'generalization_method': 'parameter_variation'
        },
        'fluid_viscosity': {
            'name': 'Fluid Viscosity (μ)',
            'description': 'Viscosity of the fluid in FSI problems',
            'unit': 'Pa·s',
            'default': 1e-3,
            'range': [1e-4, 1e-2],
            'category': 'material_properties',
            'generalization_method': 'parameter_variation'
        },
        'structure_modulus': {
            'name': 'Structure Modulus (E)',
            'description': 'Elastic modulus of the structure in FSI problems',
            'unit': 'Pa',
            'default': 200e9,
            'range': [1e9, 1000e9],
            'category': 'mechanical_properties',
            'generalization_method': 'parameter_variation'
        },
        'coupling_strength': {
            'name': 'Coupling Strength',
            'description': 'Strength of fluid-structure coupling',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'coupling_parameters',
            'generalization_method': 'parameter_variation'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for FSI problems',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'generalization_method': 'spatial_scaling'
        }
    },
    'generalization_electromagnetic_thermal': {
        'electrical_conductivity': {
            'name': 'Electrical Conductivity (σ)',
            'description': 'Electrical conductivity for EM-thermal problems',
            'unit': 'S/m',
            'default': 1e7,
            'range': [1e6, 1e8],
            'category': 'electromagnetic_properties',
            'generalization_method': 'parameter_variation'
        },
        'thermal_conductivity': {
            'name': 'Thermal Conductivity (k)',
            'description': 'Thermal conductivity for EM-thermal problems',
            'unit': 'W/(m·K)',
            'default': 50.0,
            'range': [1.0, 500.0],
            'category': 'thermal_properties',
            'generalization_method': 'parameter_variation'
        },
        'joule_heating_coefficient': {
            'name': 'Joule Heating Coefficient',
            'description': 'Coefficient for Joule heating in EM-thermal problems',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'thermal_properties',
            'generalization_method': 'parameter_variation'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for EM-thermal problems',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'generalization_method': 'spatial_scaling'
        },
        'applied_current': {
            'name': 'Applied Current',
            'description': 'Applied current for EM-thermal problems',
            'unit': 'A',
            'default': 100.0,
            'range': [10.0, 1000.0],
            'category': 'electromagnetic_properties',
            'generalization_method': 'parameter_variation'
        }
    },
    'generalization_biomechanical_transport': {
        'tissue_modulus': {
            'name': 'Tissue Modulus (E)',
            'description': 'Elastic modulus of biological tissue',
            'unit': 'Pa',
            'default': 1e6,
            'range': [1e5, 1e7],
            'category': 'mechanical_properties',
            'generalization_method': 'parameter_variation'
        },
        'diffusion_coefficient': {
            'name': 'Diffusion Coefficient (D)',
            'description': 'Diffusion coefficient for transport in tissue',
            'unit': 'm²/s',
            'default': 1e-9,
            'range': [1e-10, 1e-8],
            'category': 'transport_properties',
            'generalization_method': 'parameter_variation'
        },
        'permeability': {
            'name': 'Permeability (k)',
            'description': 'Permeability of tissue for transport',
            'unit': 'm²',
            'default': 1e-12,
            'range': [1e-15, 1e-9],
            'category': 'transport_properties',
            'generalization_method': 'parameter_variation'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for biomechanical transport',
            'unit': 'm',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'domain_properties',
            'generalization_method': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for biomechanical transport',
            'unit': 's',
            'default': 3600.0,
            'range': [100.0, 10000.0],
            'category': 'temporal_properties',
            'generalization_method': 'temporal_scaling'
        }
    },
    'generalization_geophysical_flow': {
        'coriolis_parameter': {
            'name': 'Coriolis Parameter (f)',
            'description': 'Coriolis parameter for geophysical flows',
            'unit': '1/s',
            'default': 1e-4,
            'range': [1e-5, 1e-3],
            'category': 'geophysical_properties',
            'generalization_method': 'parameter_variation'
        },
        'gravity': {
            'name': 'Gravity (g)',
            'description': 'Gravitational acceleration for geophysical flows',
            'unit': 'm/s²',
            'default': 9.81,
            'range': [1.0, 20.0],
            'category': 'geophysical_properties',
            'generalization_method': 'parameter_variation'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for geophysical flows',
            'unit': 'm',
            'default': 1000000.0,
            'range': [100000.0, 10000000.0],
            'category': 'domain_properties',
            'generalization_method': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for geophysical flows',
            'unit': 's',
            'default': 86400.0,
            'range': [3600.0, 604800.0],
            'category': 'temporal_properties',
            'generalization_method': 'temporal_scaling'
        },
        'initial_velocity': {
            'name': 'Initial Velocity',
            'description': 'Initial velocity for geophysical flows',
            'unit': 'm/s',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'initial_conditions',
            'generalization_method': 'condition_variation'
        }
    },
    'generalization_atmospheric_oceanic': {
        'atmospheric_pressure': {
            'name': 'Atmospheric Pressure',
            'description': 'Atmospheric pressure for coupled atmospheric-oceanic models',
            'unit': 'Pa',
            'default': 101325.0,
            'range': [50000.0, 200000.0],
            'category': 'geophysical_properties',
            'generalization_method': 'parameter_variation'
        },
        'ocean_depth': {
            'name': 'Ocean Depth',
            'description': 'Average ocean depth for coupled models',
            'unit': 'm',
            'default': 1000.0,
            'range': [100.0, 10000.0],
            'category': 'geophysical_properties',
            'generalization_method': 'parameter_variation'
        },
        'temperature_gradient': {
            'name': 'Temperature Gradient',
            'description': 'Vertical temperature gradient in the atmosphere',
            'unit': 'K/m',
            'default': 0.0065,
            'range': [0.001, 0.02],
            'category': 'geophysical_properties',
            'generalization_method': 'parameter_variation'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for atmospheric-oceanic models',
            'unit': 'm',
            'default': 1000000.0,
            'range': [100000.0, 10000000.0],
            'category': 'domain_properties',
            'generalization_method': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for atmospheric-oceanic models',
            'unit': 's',
            'default': 86400.0,
            'range': [3600.0, 604800.0],
            'category': 'temporal_properties',
            'generalization_method': 'temporal_scaling'
        }
    },
    'generalization_nuclear_thermal': {
        'fission_rate': {
            'name': 'Fission Rate',
            'description': 'Nuclear fission rate for nuclear-thermal models',
            'unit': '1/(m³·s)',
            'default': 1e18,
            'range': [1e17, 1e19],
            'category': 'nuclear_properties',
            'generalization_method': 'parameter_variation'
        },
        'thermal_conductivity': {
            'name': 'Thermal Conductivity (k)',
            'description': 'Thermal conductivity for nuclear-thermal models',
            'unit': 'W/(m·K)',
            'default': 50.0,
            'range': [1.0, 500.0],
            'category': 'thermal_properties',
            'generalization_method': 'parameter_variation'
        },
        'heat_capacity': {
            'name': 'Heat Capacity (c_p)',
            'description': 'Heat capacity for nuclear-thermal models',
            'unit': 'J/(kg·K)',
            'default': 1000.0,
            'range': [100.0, 5000.0],
            'category': 'thermal_properties',
            'generalization_method': 'parameter_variation'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for nuclear-thermal models',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'generalization_method': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for nuclear-thermal models',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties',
            'generalization_method': 'temporal_scaling'
        }
    },
    'generalization_quantum_mechanical': {
        'planck_constant': {
            'name': 'Planck Constant (ħ)',
            'description': 'Reduced Planck constant for quantum mechanical models',
            'unit': 'J·s',
            'default': 1.055e-34,
            'range': [1e-35, 1e-33],
            'category': 'quantum_properties',
            'generalization_method': 'parameter_variation'
        },
        'mass': {
            'name': 'Particle Mass (m)',
            'description': 'Particle mass for quantum mechanical models',
            'unit': 'kg',
            'default': 9.11e-31,
            'range': [1e-32, 1e-29],
            'category': 'quantum_properties',
            'generalization_method': 'parameter_variation'
        },
        'potential_energy': {
            'name': 'Potential Energy (V)',
            'description': 'Potential energy for quantum mechanical models',
            'unit': 'J',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'quantum_properties',
            'generalization_method': 'parameter_variation'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for quantum mechanical models',
            'unit': 'm',
            'default': 1e-9,
            'range': [1e-10, 1e-8],
            'category': 'domain_properties',
            'generalization_method': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for quantum mechanical models',
            'unit': 's',
            'default': 1e-12,
            'range': [1e-13, 1e-11],
            'category': 'temporal_properties',
            'generalization_method': 'temporal_scaling'
        }
    },
    'generalization_phase_field_allen_cahn': {
        'mobility': {
            'name': 'Mobility (M)',
            'description': 'Phase field mobility for Allen-Cahn equation',
            'unit': 'm²/(J·s)',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'phase_field_properties',
            'generalization_method': 'parameter_variation'
        },
        'interface_thickness': {
            'name': 'Interface Thickness',
            'description': 'Thickness of the phase interface',
            'unit': 'm',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'phase_field_properties',
            'generalization_method': 'parameter_variation'
        },
        'free_energy_barrier': {
            'name': 'Free Energy Barrier',
            'description': 'Free energy barrier for phase transition',
            'unit': 'J/m³',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'phase_field_properties',
            'generalization_method': 'parameter_variation'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for Allen-Cahn equation',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'generalization_method': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for Allen-Cahn equation',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties',
            'generalization_method': 'temporal_scaling'
        }
    },
    'generalization_phase_field_cahn_hilliard': {
        'mobility': {
            'name': 'Mobility (M)',
            'description': 'Phase field mobility for Cahn-Hilliard equation',
            'unit': 'm²/(J·s)',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'phase_field_properties',
            'generalization_method': 'parameter_variation'
        },
        'interface_thickness': {
            'name': 'Interface Thickness',
            'description': 'Thickness of the phase interface',
            'unit': 'm',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'phase_field_properties',
            'generalization_method': 'parameter_variation'
        },
        'free_energy_barrier': {
            'name': 'Free Energy Barrier',
            'description': 'Free energy barrier for phase transition',
            'unit': 'J/m³',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'phase_field_properties',
            'generalization_method': 'parameter_variation'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for Cahn-Hilliard equation',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'generalization_method': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for Cahn-Hilliard equation',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties',
            'generalization_method': 'temporal_scaling'
        }
    },
    'generalization_solidification_stefan': {
        'thermal_diffusivity': {
            'name': 'Thermal Diffusivity (α)',
            'description': 'Thermal diffusivity coefficient for solidification-stefan equation',
            'unit': 'm²/s',
            'default': 1e-5,
            'range': [1e-6, 1e-4],
            'category': 'thermal_properties',
            'generalization_method': 'parameter_variation'
        },
        'latent_heat': {
            'name': 'Latent Heat',
            'description': 'Latent heat for solidification-stefan equation',
            'unit': 'J/kg',
            'default': 3.34e5,
            'range': [1e5, 1e6],
            'category': 'thermal_properties',
            'generalization_method': 'parameter_variation'
        },
        'melting_temperature': {
            'name': 'Melting Temperature',
            'description': 'Melting temperature for solidification-stefan equation',
            'unit': 'K',
            'default': 273.15,
            'range': [200.0, 400.0],
            'category': 'thermal_properties',
            'generalization_method': 'parameter_variation'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for solidification-stefan equation',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'generalization_method': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for solidification-stefan equation',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties',
            'generalization_method': 'temporal_scaling'
        }
    },
    'generalization_grain_growth': {
        'mobility': {
            'name': 'Mobility',
            'description': 'Mobility for grain growth equation',
            'unit': 'm²/(J·s)',
            'default': 1e-12,
            'range': [1e-13, 1e-11],
            'category': 'material_properties',
            'generalization_method': 'parameter_variation'
        },
        'grain_boundary_energy': {
            'name': 'Grain Boundary Energy',
            'description': 'Grain boundary energy for grain growth equation',
            'unit': 'J/m²',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'material_properties',
            'generalization_method': 'parameter_variation'
        },
        'initial_grain_size': {
            'name': 'Initial Grain Size',
            'description': 'Initial grain size for grain growth equation',
            'unit': 'm',
            'default': 1e-5,
            'range': [1e-6, 1e-4],
            'category': 'material_properties',
            'generalization_method': 'parameter_variation'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for grain growth equation',
            'unit': 'm',
            'default': 1e-3,
            'range': [1e-4, 1e-2],
            'category': 'domain_properties',
            'generalization_method': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for grain growth equation',
            'unit': 's',
            'default': 3600.0,
            'range': [100.0, 10000.0],
            'category': 'temporal_properties',
            'generalization_method': 'temporal_scaling'
        }
    },
    'generalization_sintering': {
        'diffusion_coefficient': {
            'name': 'Diffusion Coefficient',
            'description': 'Diffusion coefficient for sintering equation',
            'unit': 'm²/s',
            'default': 1e-15,
            'range': [1e-16, 1e-14],
            'category': 'transport_properties',
            'generalization_method': 'parameter_variation'
        },
        'surface_energy': {
            'name': 'Surface Energy',
            'description': 'Surface energy for sintering equation',
            'unit': 'J/m²',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'material_properties',
            'generalization_method': 'parameter_variation'
        },
        'initial_porosity': {
            'name': 'Initial Porosity',
            'description': 'Initial porosity for sintering equation',
            'unit': 'dimensionless',
            'default': 0.4,
            'range': [0.1, 0.6],
            'category': 'material_properties',
            'generalization_method': 'parameter_variation'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for sintering equation',
            'unit': 'm',
            'default': 1e-3,
            'range': [1e-4, 1e-2],
            'category': 'domain_properties',
            'generalization_method': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for sintering equation',
            'unit': 's',
            'default': 3600.0,
            'range': [100.0, 10000.0],
            'category': 'temporal_properties',
            'generalization_method': 'temporal_scaling'
        }
    },
    'generalization_laser_heat_source': {
        'laser_power': {
            'name': 'Laser Power',
            'description': 'Laser power for laser heat source equation',
            'unit': 'W',
            'default': 1000.0,
            'range': [100.0, 10000.0],
            'category': 'source_terms',
            'generalization_method': 'parameter_variation'
        },
        'beam_radius': {
            'name': 'Beam Radius',
            'description': 'Beam radius for laser heat source equation',
            'unit': 'm',
            'default': 0.001,
            'range': [1e-4, 1e-2],
            'category': 'source_terms',
            'generalization_method': 'parameter_variation'
        },
        'absorption_coefficient': {
            'name': 'Absorption Coefficient',
            'description': 'Absorption coefficient for laser heat source equation',
            'unit': 'dimensionless',
            'default': 0.8,
            'range': [0.1, 1.0],
            'category': 'material_properties',
            'generalization_method': 'parameter_variation'
        },
        'scan_speed': {
            'name': 'Scan Speed',
            'description': 'Scan speed for laser heat source equation',
            'unit': 'm/s',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'source_terms',
            'generalization_method': 'parameter_variation'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for laser heat source equation',
            'unit': 'm',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'domain_properties',
            'generalization_method': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for laser heat source equation',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties',
            'generalization_method': 'temporal_scaling'
        }
    },
    'generalization_melt_pool_dynamics': {
        'surface_tension': {
            'name': 'Surface Tension',
            'description': 'Surface tension for melt pool dynamics',
            'unit': 'N/m',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'material_properties',
            'generalization_method': 'parameter_variation'
        },
        'viscosity': {
            'name': 'Viscosity',
            'description': 'Material viscosity for melt pool dynamics',
            'unit': 'Pa·s',
            'default': 1e-3,
            'range': [1e-4, 1e-2],
            'category': 'material_properties',
            'generalization_method': 'parameter_variation'
        },
        'density': {
            'name': 'Density',
            'description': 'Material density for melt pool dynamics',
            'unit': 'kg/m³',
            'default': 7000.0,
            'range': [1000.0, 20000.0],
            'category': 'material_properties',
            'generalization_method': 'parameter_variation'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for melt pool dynamics',
            'unit': 'm',
            'default': 0.001,
            'range': [1e-4, 1e-2],
            'category': 'domain_properties',
            'generalization_method': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for melt pool dynamics',
            'unit': 's',
            'default': 0.001,
            'range': [1e-4, 1e-2],
            'category': 'temporal_properties',
            'generalization_method': 'temporal_scaling'
        }
    },
    'generalization_crystal_plasticity': {
        'critical_resolved_shear_stress': {
            'name': 'Critical Resolved Shear Stress',
            'description': 'Critical resolved shear stress for crystal plasticity',
            'unit': 'Pa',
            'default': 1e6,
            'range': [1e5, 1e7],
            'category': 'material_properties',
            'generalization_method': 'parameter_variation'
        },
        'shear_modulus': {
            'name': 'Shear Modulus',
            'description': 'Shear modulus for crystal plasticity',
            'unit': 'Pa',
            'default': 80e9,
            'range': [10e9, 500e9],
            'category': 'material_properties',
            'generalization_method': 'parameter_variation'
        },
        'burgers_vector': {
            'name': 'Burgers Vector',
            'description': 'Burgers vector for crystal plasticity',
            'unit': 'm',
            'default': 2.5e-10,
            'range': [1e-10, 1e-9],
            'category': 'material_properties',
            'generalization_method': 'parameter_variation'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for crystal plasticity',
            'unit': 'm',
            'default': 1e-5,
            'range': [1e-6, 1e-4],
            'category': 'domain_properties',
            'generalization_method': 'spatial_scaling'
        },
        'applied_strain_rate': {
            'name': 'Applied Strain Rate',
            'description': 'Applied strain rate for crystal plasticity',
            'unit': '1/s',
            'default': 1e-3,
            'range': [1e-4, 1e-2],
            'category': 'material_properties',
            'generalization_method': 'parameter_variation'
        }
    },
    'generalization_diffusion_solids': {
        'diffusion_coefficient': {
            'name': 'Diffusion Coefficient',
            'description': 'Diffusion coefficient for diffusion-solids equation',
            'unit': 'm²/s',
            'default': 1e-15,
            'range': [1e-16, 1e-14],
            'category': 'transport_properties',
            'generalization_method': 'parameter_variation'
        },
        'activation_energy': {
            'name': 'Activation Energy',
            'description': 'Activation energy for diffusion-solids equation',
            'unit': 'J/mol',
            'default': 1e5,
            'range': [1e4, 1e6],
            'category': 'material_properties',
            'generalization_method': 'parameter_variation'
        },
        'temperature': {
            'name': 'Temperature',
            'description': 'Temperature for diffusion-solids equation',
            'unit': 'K',
            'default': 1000.0,
            'range': [300.0, 2000.0],
            'category': 'thermal_properties',
            'generalization_method': 'parameter_variation'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for diffusion-solids equation',
            'unit': 'm',
            'default': 1e-3,
            'range': [1e-4, 1e-2],
            'category': 'domain_properties',
            'generalization_method': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for diffusion-solids equation',
            'unit': 's',
            'default': 3600.0,
            'range': [100.0, 10000.0],
            'category': 'temporal_properties',
            'generalization_method': 'temporal_scaling'
        }
    },
    'generalization_precipitation_nucleation': {
        'nucleation_rate': {
            'name': 'Nucleation Rate',
            'description': 'Nucleation rate for precipitation-nucleation equation',
            'unit': '1/(m³·s)',
            'default': 1e12,
            'range': [1e11, 1e13],
            'category': 'material_properties',
            'generalization_method': 'parameter_variation'
        },
        'critical_radius': {
            'name': 'Critical Radius',
            'description': 'Critical radius for precipitation-nucleation equation',
            'unit': 'm',
            'default': 1e-9,
            'range': [1e-10, 1e-8],
            'category': 'material_properties',
            'generalization_method': 'parameter_variation'
        },
        'interfacial_energy': {
            'name': 'Interfacial Energy',
            'description': 'Interfacial energy for precipitation-nucleation equation',
            'unit': 'J/m²',
            'default': 0.1,
            'range': [0.01, 1.0],
            'category': 'material_properties',
            'generalization_method': 'parameter_variation'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for precipitation-nucleation equation',
            'unit': 'm',
            'default': 1e-6,
            'range': [1e-7, 1e-5],
            'category': 'domain_properties',
            'generalization_method': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for precipitation-nucleation equation',
            'unit': 's',
            'default': 3600.0,
            'range': [100.0, 10000.0],
            'category': 'temporal_properties',
            'generalization_method': 'temporal_scaling'
        }
    },
    'generalization_residual_stress': {
        'thermal_expansion': {
            'name': 'Thermal Expansion (α)',
            'description': 'Thermal expansion coefficient for residual stress equation',
            'unit': '1/K',
            'default': 2.3e-5,
            'range': [1e-6, 1e-4],
            'category': 'thermal_properties',
            'generalization_method': 'parameter_variation'
        },
        'elastic_modulus': {
            'name': 'Elastic Modulus (E)',
            'description': 'Elastic modulus for residual stress equation',
            'unit': 'Pa',
            'default': 200e9,
            'range': [1e9, 1000e9],
            'category': 'material_properties',
            'generalization_method': 'parameter_variation'
        },
        'temperature_gradient': {
            'name': 'Temperature Gradient',
            'description': 'Temperature gradient for residual stress equation',
            'unit': 'K/m',
            'default': 100.0,
            'range': [10.0, 1000.0],
            'category': 'thermal_properties',
            'generalization_method': 'parameter_variation'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for residual stress equation',
            'unit': 'm',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'domain_properties',
            'generalization_method': 'spatial_scaling'
        },
        'cooling_rate': {
            'name': 'Cooling Rate',
            'description': 'Cooling rate for residual stress equation',
            'unit': 'K/s',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'thermal_properties',
            'generalization_method': 'parameter_variation'
        }
    },
    'generalization_microstructure_evolution': {
        'phase_field_mobility': {
            'name': 'Phase Field Mobility',
            'description': 'Mobility for microstructure evolution',
            'unit': 'm²/(J·s)',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'material_properties',
            'generalization_method': 'parameter_variation'
        },
        'interface_energy': {
            'name': 'Interface Energy',
            'description': 'Interface energy for microstructure evolution',
            'unit': 'J/m²',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'material_properties',
            'generalization_method': 'parameter_variation'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for microstructure evolution',
            'unit': 'm',
            'default': 1e-5,
            'range': [1e-6, 1e-4],
            'category': 'domain_properties',
            'generalization_method': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for microstructure evolution',
            'unit': 's',
            'default': 3600.0,
            'range': [100.0, 10000.0],
            'category': 'temporal_properties',
            'generalization_method': 'temporal_scaling'
        },
        'temperature': {
            'name': 'Temperature',
            'description': 'Temperature for microstructure evolution',
            'unit': 'K',
            'default': 1000.0,
            'range': [300.0, 2000.0],
            'category': 'thermal_properties',
            'generalization_method': 'parameter_variation'
        }
    },
    'generalization_additive_manufacturing': {
        'laser_power': {
            'name': 'Laser Power',
            'description': 'Laser power for additive manufacturing',
            'unit': 'W',
            'default': 1000.0,
            'range': [100.0, 10000.0],
            'category': 'source_terms',
            'generalization_method': 'parameter_variation'
        },
        'scan_speed': {
            'name': 'Scan Speed',
            'description': 'Scan speed for additive manufacturing',
            'unit': 'm/s',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'source_terms',
            'generalization_method': 'parameter_variation'
        },
        'layer_thickness': {
            'name': 'Layer Thickness',
            'description': 'Layer thickness for additive manufacturing',
            'unit': 'm',
            'default': 0.0001,
            'range': [1e-5, 1e-3],
            'category': 'source_terms',
            'generalization_method': 'parameter_variation'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for additive manufacturing',
            'unit': 'm',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'domain_properties',
            'generalization_method': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for additive manufacturing',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties',
            'generalization_method': 'temporal_scaling'
        }
    },
    'generalization_material_processing': {
        'heating_rate': {
            'name': 'Heating Rate',
            'description': 'Heating rate for material processing',
            'unit': 'K/s',
            'default': 10.0,
            'range': [1.0, 100.0],
            'category': 'thermal_properties',
            'generalization_method': 'parameter_variation'
        },
        'cooling_rate': {
            'name': 'Cooling Rate',
            'description': 'Cooling rate for material processing',
            'unit': 'K/s',
            'default': 5.0,
            'range': [0.5, 50.0],
            'category': 'thermal_properties',
            'generalization_method': 'parameter_variation'
        },
        'processing_temperature': {
            'name': 'Processing Temperature',
            'description': 'Temperature for material processing',
            'unit': 'K',
            'default': 1000.0,
            'range': [300.0, 2000.0],
            'category': 'thermal_properties',
            'generalization_method': 'parameter_variation'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for material processing',
            'unit': 'm',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'domain_properties',
            'generalization_method': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for material processing',
            'unit': 's',
            'default': 3600.0,
            'range': [100.0, 10000.0],
            'category': 'temporal_properties',
            'generalization_method': 'temporal_scaling'
        }
    }
} 