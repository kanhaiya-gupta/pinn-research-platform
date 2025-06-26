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
        'viscosity': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'm²/s'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'time_duration': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 's'},
        'initial_condition': {'default': 'sinusoidal', 'range': ['sinusoidal', 'gaussian', 'step'], 'unit': 'dimensionless'},
        'boundary_condition': {'default': 'periodic', 'range': ['periodic', 'dirichlet', 'neumann'], 'unit': 'dimensionless'}
    },
    'generalization_heat': {
        'thermal_diffusivity': {'default': 1e-5, 'range': [1e-6, 1e-4], 'unit': 'm²/s'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'time_duration': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 's'},
        'initial_temperature': {'default': 0.0, 'range': [-100.0, 100.0], 'unit': '°C'},
        'boundary_temperature': {'default': 100.0, 'range': [0.0, 500.0], 'unit': '°C'}
    },
    'generalization_wave': {
        'wave_speed': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm/s'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'time_duration': {'default': 2.0, 'range': [0.5, 10.0], 'unit': 's'},
        'initial_displacement': {'default': 'gaussian', 'range': ['gaussian', 'sinusoidal', 'pulse'], 'unit': 'dimensionless'},
        'boundary_condition': {'default': 'absorbing', 'range': ['absorbing', 'reflecting', 'periodic'], 'unit': 'dimensionless'}
    },
    'generalization_shm': {
        'natural_frequency': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'rad/s'},
        'damping_ratio': {'default': 0.1, 'range': [0.0, 1.0], 'unit': 'dimensionless'},
        'initial_amplitude': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'initial_phase': {'default': 0.0, 'range': [0.0, 2*3.14159], 'unit': 'rad'},
        'time_duration': {'default': 10.0, 'range': [1.0, 100.0], 'unit': 's'}
    },
    'generalization_helmholtz': {
        'wavenumber': {'default': 1.0, 'range': [0.1, 10.0], 'unit': '1/m'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'boundary_condition': {'default': 'dirichlet', 'range': ['dirichlet', 'neumann', 'mixed'], 'unit': 'dimensionless'},
        'source_strength': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'dimensionless'},
        'absorption_coefficient': {'default': 0.1, 'range': [0.0, 1.0], 'unit': '1/m'}
    },
    'generalization_navier_stokes': {
        'reynolds_number': {'default': 100.0, 'range': [1.0, 1000.0], 'unit': 'dimensionless'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'time_duration': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 's'},
        'inlet_velocity': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm/s'},
        'pressure_gradient': {'default': 0.0, 'range': [-10.0, 10.0], 'unit': 'Pa/m'}
    },
    'generalization_schrodinger': {
        'planck_constant': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'J·s'},
        'mass': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'kg'},
        'potential_strength': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'J'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'time_duration': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 's'}
    },
    'generalization_maxwell': {
        'permittivity': {'default': 8.85e-12, 'range': [1e-12, 1e-10], 'unit': 'F/m'},
        'permeability': {'default': 1.26e-6, 'range': [1e-7, 1e-5], 'unit': 'H/m'},
        'conductivity': {'default': 1e-6, 'range': [1e-8, 1e-4], 'unit': 'S/m'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'time_duration': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 's'}
    },
    'generalization_heat_transfer': {
        'thermal_conductivity': {'default': 50.0, 'range': [1.0, 500.0], 'unit': 'W/(m·K)'},
        'density': {'default': 2700.0, 'range': [100.0, 10000.0], 'unit': 'kg/m³'},
        'specific_heat': {'default': 900.0, 'range': [100.0, 5000.0], 'unit': 'J/(kg·K)'},
        'heat_source': {'default': 0.0, 'range': [0.0, 1000000.0], 'unit': 'W/m³'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'}
    },
    'generalization_elastic': {
        'young_modulus': {'default': 200e9, 'range': [1e9, 1000e9], 'unit': 'Pa'},
        'poisson_ratio': {'default': 0.3, 'range': [0.0, 0.5], 'unit': 'dimensionless'},
        'density': {'default': 2700.0, 'range': [100.0, 10000.0], 'unit': 'kg/m³'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'applied_force': {'default': 1000.0, 'range': [100.0, 10000.0], 'unit': 'N'}
    },
    'generalization_phase_field': {
        'mobility': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm²/(J·s)'},
        'interface_thickness': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'm'},
        'free_energy_barrier': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'J/m³'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'time_duration': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 's'}
    },
    'generalization_reaction_diffusion': {
        'diffusion_coefficient': {'default': 1e-9, 'range': [1e-10, 1e-8], 'unit': 'm²/s'},
        'reaction_rate': {'default': 1.0, 'range': [0.1, 10.0], 'unit': '1/s'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'time_duration': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 's'},
        'initial_concentration': {'default': 0.5, 'range': [0.0, 1.0], 'unit': 'dimensionless'}
    },
    'generalization_poroelasticity': {
        'permeability': {'default': 1e-12, 'range': [1e-15, 1e-9], 'unit': 'm²'},
        'porosity': {'default': 0.2, 'range': [0.01, 0.5], 'unit': 'dimensionless'},
        'biot_coefficient': {'default': 0.8, 'range': [0.1, 1.0], 'unit': 'dimensionless'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'time_duration': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 's'}
    },
    'generalization_viscoelasticity': {
        'elastic_modulus': {'default': 1e9, 'range': [1e8, 1e10], 'unit': 'Pa'},
        'viscosity': {'default': 1e6, 'range': [1e5, 1e7], 'unit': 'Pa·s'},
        'relaxation_time': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 's'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'applied_strain': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'}
    },
    'generalization_radiative_transfer': {
        'absorption_coefficient': {'default': 1.0, 'range': [0.1, 10.0], 'unit': '1/m'},
        'scattering_coefficient': {'default': 0.1, 'range': [0.01, 1.0], 'unit': '1/m'},
        'refractive_index': {'default': 1.5, 'range': [1.0, 3.0], 'unit': 'dimensionless'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'source_intensity': {'default': 1000.0, 'range': [100.0, 10000.0], 'unit': 'W/m²'}
    },
    'generalization_shallow_water': {
        'gravity': {'default': 9.81, 'range': [1.0, 20.0], 'unit': 'm/s²'},
        'water_depth': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'domain_size': {'default': 100.0, 'range': [10.0, 1000.0], 'unit': 'm'},
        'time_duration': {'default': 10.0, 'range': [1.0, 100.0], 'unit': 's'},
        'initial_wave_height': {'default': 0.1, 'range': [0.01, 1.0], 'unit': 'm'}
    },
    'generalization_magnetohydrodynamics': {
        'magnetic_field': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'T'},
        'plasma_density': {'default': 1e19, 'range': [1e18, 1e20], 'unit': '1/m³'},
        'temperature': {'default': 1e6, 'range': [1e5, 1e7], 'unit': 'K'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'time_duration': {'default': 1e-6, 'range': [1e-7, 1e-5], 'unit': 's'}
    },
    'generalization_thermoelasticity': {
        'thermal_expansion': {'default': 2.3e-5, 'range': [1e-6, 1e-4], 'unit': '1/K'},
        'thermal_conductivity': {'default': 50.0, 'range': [1.0, 500.0], 'unit': 'W/(m·K)'},
        'elastic_modulus': {'default': 200e9, 'range': [1e9, 1000e9], 'unit': 'Pa'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'temperature_difference': {'default': 100.0, 'range': [10.0, 1000.0], 'unit': 'K'}
    },
    'generalization_advection_diffusion': {
        'velocity': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm/s'},
        'diffusion_coefficient': {'default': 1e-9, 'range': [1e-10, 1e-8], 'unit': 'm²/s'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'time_duration': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 's'},
        'initial_concentration': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'kg/m³'}
    },
    'generalization_elastic_wave': {
        'p_wave_speed': {'default': 5000.0, 'range': [1000.0, 10000.0], 'unit': 'm/s'},
        's_wave_speed': {'default': 3000.0, 'range': [500.0, 6000.0], 'unit': 'm/s'},
        'density': {'default': 2700.0, 'range': [1000.0, 8000.0], 'unit': 'kg/m³'},
        'domain_size': {'default': 1000.0, 'range': [100.0, 10000.0], 'unit': 'm'},
        'time_duration': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 's'}
    },
    'generalization_fluid_structure_interaction': {
        'fluid_density': {'default': 1000.0, 'range': [100.0, 2000.0], 'unit': 'kg/m³'},
        'fluid_viscosity': {'default': 1e-3, 'range': [1e-4, 1e-2], 'unit': 'Pa·s'},
        'structure_modulus': {'default': 200e9, 'range': [1e9, 1000e9], 'unit': 'Pa'},
        'coupling_strength': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'dimensionless'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'}
    },
    'generalization_electromagnetic_thermal': {
        'electrical_conductivity': {'default': 1e7, 'range': [1e6, 1e8], 'unit': 'S/m'},
        'thermal_conductivity': {'default': 50.0, 'range': [1.0, 500.0], 'unit': 'W/(m·K)'},
        'joule_heating_coefficient': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'dimensionless'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'applied_current': {'default': 100.0, 'range': [10.0, 1000.0], 'unit': 'A'}
    },
    'generalization_biomechanical_transport': {
        'tissue_modulus': {'default': 1e6, 'range': [1e5, 1e7], 'unit': 'Pa'},
        'diffusion_coefficient': {'default': 1e-9, 'range': [1e-10, 1e-8], 'unit': 'm²/s'},
        'permeability': {'default': 1e-12, 'range': [1e-15, 1e-9], 'unit': 'm²'},
        'domain_size': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'm'},
        'time_duration': {'default': 3600.0, 'range': [100.0, 10000.0], 'unit': 's'}
    },
    'generalization_geophysical_flow': {
        'coriolis_parameter': {'default': 1e-4, 'range': [1e-5, 1e-3], 'unit': '1/s'},
        'gravity': {'default': 9.81, 'range': [1.0, 20.0], 'unit': 'm/s²'},
        'domain_size': {'default': 1000000.0, 'range': [100000.0, 10000000.0], 'unit': 'm'},
        'time_duration': {'default': 86400.0, 'range': [3600.0, 604800.0], 'unit': 's'},
        'initial_velocity': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm/s'}
    },
    'generalization_atmospheric_oceanic': {
        'atmospheric_pressure': {'default': 101325.0, 'range': [50000.0, 200000.0], 'unit': 'Pa'},
        'ocean_depth': {'default': 1000.0, 'range': [100.0, 10000.0], 'unit': 'm'},
        'temperature_gradient': {'default': 0.0065, 'range': [0.001, 0.02], 'unit': 'K/m'},
        'domain_size': {'default': 1000000.0, 'range': [100000.0, 10000000.0], 'unit': 'm'},
        'time_duration': {'default': 86400.0, 'range': [3600.0, 604800.0], 'unit': 's'}
    },
    'generalization_nuclear_thermal': {
        'fission_rate': {'default': 1e18, 'range': [1e17, 1e19], 'unit': '1/(m³·s)'},
        'thermal_conductivity': {'default': 50.0, 'range': [1.0, 500.0], 'unit': 'W/(m·K)'},
        'heat_capacity': {'default': 1000.0, 'range': [100.0, 5000.0], 'unit': 'J/(kg·K)'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'time_duration': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 's'}
    },
    'generalization_quantum_mechanical': {
        'planck_constant': {'default': 1.055e-34, 'range': [1e-35, 1e-33], 'unit': 'J·s'},
        'mass': {'default': 9.11e-31, 'range': [1e-32, 1e-29], 'unit': 'kg'},
        'potential_energy': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'J'},
        'domain_size': {'default': 1e-9, 'range': [1e-10, 1e-8], 'unit': 'm'},
        'time_duration': {'default': 1e-12, 'range': [1e-13, 1e-11], 'unit': 's'}
    },
    'generalization_phase_field_allen_cahn': {
        'mobility': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm²/(J·s)'},
        'interface_thickness': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'm'},
        'free_energy_barrier': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'J/m³'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'time_duration': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 's'}
    },
    'generalization_phase_field_cahn_hilliard': {
        'mobility': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm²/(J·s)'},
        'interface_thickness': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'm'},
        'free_energy_barrier': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'J/m³'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'time_duration': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 's'}
    },
    'generalization_solidification_stefan': {
        'thermal_diffusivity': {'default': 1e-5, 'range': [1e-6, 1e-4], 'unit': 'm²/s'},
        'latent_heat': {'default': 3.34e5, 'range': [1e5, 1e6], 'unit': 'J/kg'},
        'melting_temperature': {'default': 273.15, 'range': [200.0, 400.0], 'unit': 'K'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'time_duration': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 's'}
    },
    'generalization_grain_growth': {
        'mobility': {'default': 1e-12, 'range': [1e-13, 1e-11], 'unit': 'm²/(J·s)'},
        'grain_boundary_energy': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'J/m²'},
        'initial_grain_size': {'default': 1e-5, 'range': [1e-6, 1e-4], 'unit': 'm'},
        'domain_size': {'default': 1e-3, 'range': [1e-4, 1e-2], 'unit': 'm'},
        'time_duration': {'default': 3600.0, 'range': [100.0, 10000.0], 'unit': 's'}
    },
    'generalization_sintering': {
        'diffusion_coefficient': {'default': 1e-15, 'range': [1e-16, 1e-14], 'unit': 'm²/s'},
        'surface_energy': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'J/m²'},
        'initial_porosity': {'default': 0.4, 'range': [0.1, 0.6], 'unit': 'dimensionless'},
        'domain_size': {'default': 1e-3, 'range': [1e-4, 1e-2], 'unit': 'm'},
        'time_duration': {'default': 3600.0, 'range': [100.0, 10000.0], 'unit': 's'}
    },
    'generalization_laser_heat_source': {
        'laser_power': {'default': 1000.0, 'range': [100.0, 10000.0], 'unit': 'W'},
        'beam_radius': {'default': 0.001, 'range': [1e-4, 1e-2], 'unit': 'm'},
        'absorption_coefficient': {'default': 0.8, 'range': [0.1, 1.0], 'unit': 'dimensionless'},
        'scan_speed': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'm/s'},
        'domain_size': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'm'}
    },
    'generalization_melt_pool_dynamics': {
        'surface_tension': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'N/m'},
        'viscosity': {'default': 1e-3, 'range': [1e-4, 1e-2], 'unit': 'Pa·s'},
        'density': {'default': 7000.0, 'range': [1000.0, 20000.0], 'unit': 'kg/m³'},
        'domain_size': {'default': 0.001, 'range': [1e-4, 1e-2], 'unit': 'm'},
        'time_duration': {'default': 0.001, 'range': [1e-4, 1e-2], 'unit': 's'}
    },
    'generalization_crystal_plasticity': {
        'critical_resolved_shear_stress': {'default': 1e6, 'range': [1e5, 1e7], 'unit': 'Pa'},
        'shear_modulus': {'default': 80e9, 'range': [10e9, 500e9], 'unit': 'Pa'},
        'burgers_vector': {'default': 2.5e-10, 'range': [1e-10, 1e-9], 'unit': 'm'},
        'domain_size': {'default': 1e-5, 'range': [1e-6, 1e-4], 'unit': 'm'},
        'applied_strain_rate': {'default': 1e-3, 'range': [1e-4, 1e-2], 'unit': '1/s'}
    },
    'generalization_diffusion_solids': {
        'diffusion_coefficient': {'default': 1e-15, 'range': [1e-16, 1e-14], 'unit': 'm²/s'},
        'activation_energy': {'default': 1e5, 'range': [1e4, 1e6], 'unit': 'J/mol'},
        'temperature': {'default': 1000.0, 'range': [300.0, 2000.0], 'unit': 'K'},
        'domain_size': {'default': 1e-3, 'range': [1e-4, 1e-2], 'unit': 'm'},
        'time_duration': {'default': 3600.0, 'range': [100.0, 10000.0], 'unit': 's'}
    },
    'generalization_precipitation_nucleation': {
        'nucleation_rate': {'default': 1e12, 'range': [1e11, 1e13], 'unit': '1/(m³·s)'},
        'critical_radius': {'default': 1e-9, 'range': [1e-10, 1e-8], 'unit': 'm'},
        'interfacial_energy': {'default': 0.1, 'range': [0.01, 1.0], 'unit': 'J/m²'},
        'domain_size': {'default': 1e-6, 'range': [1e-7, 1e-5], 'unit': 'm'},
        'time_duration': {'default': 3600.0, 'range': [100.0, 10000.0], 'unit': 's'}
    },
    'generalization_residual_stress': {
        'thermal_expansion': {'default': 2.3e-5, 'range': [1e-6, 1e-4], 'unit': '1/K'},
        'elastic_modulus': {'default': 200e9, 'range': [1e9, 1000e9], 'unit': 'Pa'},
        'temperature_gradient': {'default': 100.0, 'range': [10.0, 1000.0], 'unit': 'K/m'},
        'domain_size': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'm'},
        'cooling_rate': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'K/s'}
    },
    'generalization_microstructure_evolution': {
        'phase_field_mobility': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm²/(J·s)'},
        'interface_energy': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'J/m²'},
        'domain_size': {'default': 1e-5, 'range': [1e-6, 1e-4], 'unit': 'm'},
        'time_duration': {'default': 3600.0, 'range': [100.0, 10000.0], 'unit': 's'},
        'temperature': {'default': 1000.0, 'range': [300.0, 2000.0], 'unit': 'K'}
    },
    'generalization_additive_manufacturing': {
        'laser_power': {'default': 1000.0, 'range': [100.0, 10000.0], 'unit': 'W'},
        'scan_speed': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'm/s'},
        'layer_thickness': {'default': 0.0001, 'range': [1e-5, 1e-3], 'unit': 'm'},
        'domain_size': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'm'},
        'time_duration': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 's'}
    },
    'generalization_material_processing': {
        'heating_rate': {'default': 10.0, 'range': [1.0, 100.0], 'unit': 'K/s'},
        'cooling_rate': {'default': 5.0, 'range': [0.5, 50.0], 'unit': 'K/s'},
        'processing_temperature': {'default': 1000.0, 'range': [300.0, 2000.0], 'unit': 'K'},
        'domain_size': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'm'},
        'time_duration': {'default': 3600.0, 'range': [100.0, 10000.0], 'unit': 's'}
    }
} 