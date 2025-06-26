"""
Sparse Data Parameters
Parameters for learning from limited or sparse observational data.
"""

SPARSE_DATA_PARAMETERS_DICT = {
    # Sparse Data Parameters
    'sparse_data_ratio': {
        'name': 'Sparse Data Ratio',
        'description': 'Ratio of available data to total possible measurements',
        'unit': 'dimensionless',
        'default': 0.1,
        'range': [0.01, 1.0],
        'category': 'sparse_data_parameters',
        'data_availability': 'limited'
    },
    'measurement_density': {
        'name': 'Measurement Density',
        'description': 'Density of measurements in space and time',
        'unit': '1/(m³·s)',
        'default': 1.0,
        'range': [0.01, 100.0],
        'category': 'sparse_data_parameters',
        'data_availability': 'limited'
    },
    'sensor_coverage': {
        'name': 'Sensor Coverage',
        'description': 'Fraction of domain covered by sensors',
        'unit': 'dimensionless',
        'default': 0.1,
        'range': [0.01, 1.0],
        'category': 'sparse_data_parameters',
        'data_availability': 'limited'
    },
    
    # Sensor Placement Parameters
    'sensor_locations': {
        'name': 'Sensor Locations',
        'description': 'Spatial locations of available sensors',
        'unit': 'm',
        'default': [0.0, 0.5, 1.0],
        'range': [0.0, 10.0],
        'category': 'sensor_placement',
        'data_availability': 'limited'
    },
    'sensor_spacing': {
        'name': 'Sensor Spacing',
        'description': 'Distance between adjacent sensors',
        'unit': 'm',
        'default': 0.5,
        'range': [0.01, 10.0],
        'category': 'sensor_placement',
        'data_availability': 'limited'
    },
    'optimal_sensor_placement': {
        'name': 'Optimal Sensor Placement',
        'description': 'Optimal placement strategy for sensors',
        'unit': 'dimensionless',
        'default': 'uniform',
        'range': ['uniform', 'adaptive', 'optimal'],
        'category': 'sensor_placement',
        'data_availability': 'limited'
    },
    
    # Temporal Sampling Parameters
    'sampling_frequency': {
        'name': 'Sampling Frequency',
        'description': 'Frequency of data sampling',
        'unit': 'Hz',
        'default': 1.0,
        'range': [0.01, 100.0],
        'category': 'temporal_sampling',
        'data_availability': 'limited'
    },
    'sampling_interval': {
        'name': 'Sampling Interval',
        'description': 'Time interval between samples',
        'unit': 's',
        'default': 1.0,
        'range': [0.01, 100.0],
        'category': 'temporal_sampling',
        'data_availability': 'limited'
    },
    'irregular_sampling': {
        'name': 'Irregular Sampling',
        'description': 'Whether sampling is irregular in time',
        'unit': 'dimensionless',
        'default': False,
        'range': [True, False],
        'category': 'temporal_sampling',
        'data_availability': 'limited'
    },
    
    # Data Quality Parameters
    'measurement_noise': {
        'name': 'Measurement Noise',
        'description': 'Noise level in sparse measurements',
        'unit': 'dimensionless',
        'default': 0.01,
        'range': [0.0, 0.1],
        'category': 'data_quality',
        'data_availability': 'limited'
    },
    'measurement_uncertainty': {
        'name': 'Measurement Uncertainty',
        'description': 'Uncertainty in sparse measurements',
        'unit': 'dimensionless',
        'default': 0.05,
        'range': [0.0, 0.5],
        'category': 'data_quality',
        'data_availability': 'limited'
    },
    'missing_data_pattern': {
        'name': 'Missing Data Pattern',
        'description': 'Pattern of missing data',
        'unit': 'dimensionless',
        'default': 'random',
        'range': ['random', 'systematic', 'structured'],
        'category': 'data_quality',
        'data_availability': 'limited'
    },
    
    # Reconstruction Parameters
    'reconstruction_method': {
        'name': 'Reconstruction Method',
        'description': 'Method for field reconstruction from sparse data',
        'unit': 'dimensionless',
        'default': 'pinn',
        'range': ['pinn', 'interpolation', 'regression', 'neural_network'],
        'category': 'reconstruction_parameters',
        'data_availability': 'limited'
    },
    'interpolation_order': {
        'name': 'Interpolation Order',
        'description': 'Order of interpolation for field reconstruction',
        'unit': 'dimensionless',
        'default': 2,
        'range': [1, 5],
        'category': 'reconstruction_parameters',
        'data_availability': 'limited'
    },
    'smoothing_parameter': {
        'name': 'Smoothing Parameter',
        'description': 'Smoothing parameter for field reconstruction',
        'unit': 'dimensionless',
        'default': 0.1,
        'range': [0.0, 1.0],
        'category': 'reconstruction_parameters',
        'data_availability': 'limited'
    },
    
    # Regularization Parameters
    'regularization_strength': {
        'name': 'Regularization Strength',
        'description': 'Strength of regularization for sparse data',
        'unit': 'dimensionless',
        'default': 0.01,
        'range': [0.0, 1.0],
        'category': 'regularization_parameters',
        'data_availability': 'limited'
    },
    'physics_regularization': {
        'name': 'Physics Regularization',
        'description': 'Weight for physics-based regularization',
        'unit': 'dimensionless',
        'default': 1.0,
        'range': [0.0, 10.0],
        'category': 'regularization_parameters',
        'data_availability': 'limited'
    },
    'smoothness_regularization': {
        'name': 'Smoothness Regularization',
        'description': 'Weight for smoothness regularization',
        'unit': 'dimensionless',
        'default': 0.1,
        'range': [0.0, 1.0],
        'category': 'regularization_parameters',
        'data_availability': 'limited'
    },
    
    # Learning Parameters
    'learning_rate_sparse': {
        'name': 'Learning Rate (Sparse)',
        'description': 'Learning rate for sparse data learning',
        'unit': 'dimensionless',
        'default': 0.001,
        'range': [1e-6, 1e-1],
        'category': 'learning_parameters',
        'data_availability': 'limited'
    },
    'batch_size_sparse': {
        'name': 'Batch Size (Sparse)',
        'description': 'Batch size for sparse data training',
        'unit': 'dimensionless',
        'default': 32,
        'range': [1, 1000],
        'category': 'learning_parameters',
        'data_availability': 'limited'
    },
    'epochs_sparse': {
        'name': 'Training Epochs (Sparse)',
        'description': 'Number of training epochs for sparse data',
        'unit': 'dimensionless',
        'default': 1000,
        'range': [100, 10000],
        'category': 'learning_parameters',
        'data_availability': 'limited'
    },
    
    # Validation Parameters
    'validation_ratio': {
        'name': 'Validation Ratio',
        'description': 'Ratio of data used for validation',
        'unit': 'dimensionless',
        'default': 0.2,
        'range': [0.0, 0.5],
        'category': 'validation_parameters',
        'data_availability': 'limited'
    },
    'cross_validation_folds': {
        'name': 'Cross Validation Folds',
        'description': 'Number of folds for cross validation',
        'unit': 'dimensionless',
        'default': 5,
        'range': [2, 10],
        'category': 'validation_parameters',
        'data_availability': 'limited'
    },
    
    # Uncertainty Quantification
    'uncertainty_estimation': {
        'name': 'Uncertainty Estimation',
        'description': 'Method for uncertainty estimation with sparse data',
        'unit': 'dimensionless',
        'default': 'ensemble',
        'range': ['ensemble', 'bayesian', 'monte_carlo'],
        'category': 'uncertainty_parameters',
        'data_availability': 'limited'
    },
    'confidence_level': {
        'name': 'Confidence Level',
        'description': 'Confidence level for uncertainty quantification',
        'unit': 'dimensionless',
        'default': 0.95,
        'range': [0.5, 0.99],
        'category': 'uncertainty_parameters',
        'data_availability': 'limited'
    },
    
    # Adaptive Sampling Parameters
    'adaptive_sampling': {
        'name': 'Adaptive Sampling',
        'description': 'Whether to use adaptive sampling strategies',
        'unit': 'dimensionless',
        'default': False,
        'range': [True, False],
        'category': 'adaptive_sampling',
        'data_availability': 'limited'
    },
    'information_gain_threshold': {
        'name': 'Information Gain Threshold',
        'description': 'Threshold for information gain in adaptive sampling',
        'unit': 'dimensionless',
        'default': 0.1,
        'range': [0.0, 1.0],
        'category': 'adaptive_sampling',
        'data_availability': 'limited'
    },
    
    # Performance Metrics
    'reconstruction_error_threshold': {
        'name': 'Reconstruction Error Threshold',
        'description': 'Threshold for acceptable reconstruction error',
        'unit': 'dimensionless',
        'default': 0.1,
        'range': [0.01, 1.0],
        'category': 'performance_metrics',
        'data_availability': 'limited'
    },
    'convergence_criteria': {
        'name': 'Convergence Criteria',
        'description': 'Criteria for convergence in sparse data learning',
        'unit': 'dimensionless',
        'default': 1e-6,
        'range': [1e-12, 1e-3],
        'category': 'performance_metrics',
        'data_availability': 'limited'
    }
}

# Equation-specific parameter mappings
SPARSE_DATA_EQUATION_PARAMETERS = {
    'sparse_heat': {
        'thermal_diffusivity': {
            'name': 'Thermal Diffusivity (α)',
            'description': 'Thermal diffusivity coefficient',
            'unit': 'm²/s',
            'default': 1e-5,
            'range': [1e-8, 1e-3],
            'category': 'thermal_properties'
        },
        'sparse_data_ratio': {
            'name': 'Sparse Data Ratio',
            'description': 'Ratio of available temperature data',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.01, 1.0],
            'category': 'sparse_data_parameters'
        },
        'measurement_noise': {
            'name': 'Measurement Noise',
            'description': 'Noise level in temperature measurements',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.0, 0.1],
            'category': 'data_quality'
        },
        'reconstruction_method': {
            'name': 'Reconstruction Method',
            'description': 'Method for temperature field reconstruction',
            'unit': 'dimensionless',
            'default': 'pinn',
            'range': ['pinn', 'interpolation', 'regression', 'neural_network'],
            'category': 'reconstruction_parameters'
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
    
    'sparse_burgers': {
        'viscosity': {
            'name': 'Viscosity (ν)',
            'description': 'Dynamic viscosity coefficient',
            'unit': 'Pa·s',
            'default': 0.01,
            'range': [1e-6, 1e-1],
            'category': 'fluid_properties'
        },
        'sparse_data_ratio': {
            'name': 'Sparse Data Ratio',
            'description': 'Ratio of available velocity data',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.01, 1.0],
            'category': 'sparse_data_parameters'
        },
        'measurement_noise': {
            'name': 'Measurement Noise',
            'description': 'Noise level in velocity measurements',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.0, 0.1],
            'category': 'data_quality'
        },
        'reconstruction_method': {
            'name': 'Reconstruction Method',
            'description': 'Method for velocity field reconstruction',
            'unit': 'dimensionless',
            'default': 'pinn',
            'range': ['pinn', 'interpolation', 'regression', 'neural_network'],
            'category': 'reconstruction_parameters'
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
    
    'sparse_navier_stokes': {
        'viscosity': {
            'name': 'Viscosity (μ)',
            'description': 'Dynamic viscosity',
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
        'sparse_data_ratio': {
            'name': 'Sparse Data Ratio',
            'description': 'Ratio of available flow data',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.01, 1.0],
            'category': 'sparse_data_parameters'
        },
        'measurement_noise': {
            'name': 'Measurement Noise',
            'description': 'Noise level in flow measurements',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.0, 0.1],
            'category': 'data_quality'
        },
        'reconstruction_method': {
            'name': 'Reconstruction Method',
            'description': 'Method for flow field reconstruction',
            'unit': 'dimensionless',
            'default': 'pinn',
            'range': ['pinn', 'interpolation', 'regression', 'neural_network'],
            'category': 'reconstruction_parameters'
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
    
    'sparse_reaction_diffusion': {
        'diffusion_coefficient': {
            'name': 'Diffusion Coefficient (D)',
            'description': 'Diffusion coefficient',
            'unit': 'm²/s',
            'default': 1e-9,
            'range': [1e-12, 1e-6],
            'category': 'transport_properties'
        },
        'reaction_rate': {
            'name': 'Reaction Rate (k)',
            'description': 'Chemical reaction rate',
            'unit': '1/s',
            'default': 1e-3,
            'range': [1e-6, 1e0],
            'category': 'chemical_properties'
        },
        'sparse_data_ratio': {
            'name': 'Sparse Data Ratio',
            'description': 'Ratio of available concentration data',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.01, 1.0],
            'category': 'sparse_data_parameters'
        },
        'measurement_noise': {
            'name': 'Measurement Noise',
            'description': 'Noise level in concentration measurements',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.0, 0.1],
            'category': 'data_quality'
        },
        'reconstruction_method': {
            'name': 'Reconstruction Method',
            'description': 'Method for concentration field reconstruction',
            'unit': 'dimensionless',
            'default': 'pinn',
            'range': ['pinn', 'interpolation', 'regression', 'neural_network'],
            'category': 'reconstruction_parameters'
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
    
    'sparse_elastic': {
        'elastic_modulus': {
            'name': 'Elastic Modulus (E)',
            'description': 'Young\'s modulus',
            'unit': 'GPa',
            'default': 200.0,
            'range': [1.0, 1000.0],
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
        'sparse_data_ratio': {
            'name': 'Sparse Data Ratio',
            'description': 'Ratio of available displacement data',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.01, 1.0],
            'category': 'sparse_data_parameters'
        },
        'measurement_noise': {
            'name': 'Measurement Noise',
            'description': 'Noise level in displacement measurements',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.0, 0.1],
            'category': 'data_quality'
        },
        'reconstruction_method': {
            'name': 'Reconstruction Method',
            'description': 'Method for displacement field reconstruction',
            'unit': 'dimensionless',
            'default': 'pinn',
            'range': ['pinn', 'interpolation', 'regression', 'neural_network'],
            'category': 'reconstruction_parameters'
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
    
    'sparse_wave': {
        'wave_speed': {
            'name': 'Wave Speed (c)',
            'description': 'Wave propagation speed',
            'unit': 'm/s',
            'default': 340.0,
            'range': [1.0, 10000.0],
            'category': 'wave_properties'
        },
        'sparse_data_ratio': {
            'name': 'Sparse Data Ratio',
            'description': 'Ratio of available wave amplitude data',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.01, 1.0],
            'category': 'sparse_data_parameters'
        },
        'measurement_noise': {
            'name': 'Measurement Noise',
            'description': 'Noise level in wave measurements',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.0, 0.1],
            'category': 'data_quality'
        },
        'reconstruction_method': {
            'name': 'Reconstruction Method',
            'description': 'Method for wave field reconstruction',
            'unit': 'dimensionless',
            'default': 'pinn',
            'range': ['pinn', 'interpolation', 'regression', 'neural_network'],
            'category': 'reconstruction_parameters'
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
            'default': 2.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties'
        }
    },
    
    'sparse_schrodinger': {
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
        'sparse_data_ratio': {
            'name': 'Sparse Data Ratio',
            'description': 'Ratio of available wave function data',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.01, 1.0],
            'category': 'sparse_data_parameters'
        },
        'measurement_noise': {
            'name': 'Measurement Noise',
            'description': 'Noise level in quantum measurements',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.0, 0.1],
            'category': 'data_quality'
        },
        'reconstruction_method': {
            'name': 'Reconstruction Method',
            'description': 'Method for wave function reconstruction',
            'unit': 'dimensionless',
            'default': 'pinn',
            'range': ['pinn', 'interpolation', 'regression', 'neural_network'],
            'category': 'reconstruction_parameters'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1e-9,
            'range': [1e-12, 1e-6],
            'category': 'domain_properties'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration',
            'unit': 's',
            'default': 1e-12,
            'range': [1e-15, 1e-9],
            'category': 'temporal_properties'
        }
    },
    
    'sparse_phase_field': {
        'mobility': {
            'name': 'Mobility (M)',
            'description': 'Phase field mobility',
            'unit': 'm²/(J·s)',
            'default': 1e-3,
            'range': [1e-6, 1e-1],
            'category': 'phase_field'
        },
        'interface_thickness': {
            'name': 'Interface Thickness (ε)',
            'description': 'Phase field interface thickness',
            'unit': 'm',
            'default': 1e-6,
            'range': [1e-9, 1e-3],
            'category': 'phase_field'
        },
        'sparse_data_ratio': {
            'name': 'Sparse Data Ratio',
            'description': 'Ratio of available phase field data',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.01, 1.0],
            'category': 'sparse_data_parameters'
        },
        'measurement_noise': {
            'name': 'Measurement Noise',
            'description': 'Noise level in phase field measurements',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.0, 0.1],
            'category': 'data_quality'
        },
        'reconstruction_method': {
            'name': 'Reconstruction Method',
            'description': 'Method for phase field reconstruction',
            'unit': 'dimensionless',
            'default': 'pinn',
            'range': ['pinn', 'interpolation', 'regression', 'neural_network'],
            'category': 'reconstruction_parameters'
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
    
    'sparse_poroelasticity': {
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
            'description': 'Biot coefficient',
            'unit': 'dimensionless',
            'default': 0.8,
            'range': [0.0, 1.0],
            'category': 'poroelastic_properties'
        },
        'elastic_modulus': {
            'name': 'Elastic Modulus (E)',
            'description': 'Young\'s modulus',
            'unit': 'GPa',
            'default': 200.0,
            'range': [1.0, 1000.0],
            'category': 'mechanical_properties'
        },
        'sparse_data_ratio': {
            'name': 'Sparse Data Ratio',
            'description': 'Ratio of available poroelastic data',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.01, 1.0],
            'category': 'sparse_data_parameters'
        },
        'measurement_noise': {
            'name': 'Measurement Noise',
            'description': 'Noise level in poroelastic measurements',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.0, 0.1],
            'category': 'data_quality'
        },
        'reconstruction_method': {
            'name': 'Reconstruction Method',
            'description': 'Method for poroelastic field reconstruction',
            'unit': 'dimensionless',
            'default': 'pinn',
            'range': ['pinn', 'interpolation', 'regression', 'neural_network'],
            'category': 'reconstruction_parameters'
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
    
    'sparse_viscoelasticity': {
        'relaxation_time': {
            'name': 'Relaxation Time (τ)',
            'description': 'Viscoelastic relaxation time',
            'unit': 's',
            'default': 1.0,
            'range': [1e-3, 1e3],
            'category': 'viscoelastic_properties'
        },
        'elastic_modulus': {
            'name': 'Elastic Modulus (E)',
            'description': 'Young\'s modulus',
            'unit': 'GPa',
            'default': 200.0,
            'range': [1.0, 1000.0],
            'category': 'mechanical_properties'
        },
        'sparse_data_ratio': {
            'name': 'Sparse Data Ratio',
            'description': 'Ratio of available viscoelastic data',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.01, 1.0],
            'category': 'sparse_data_parameters'
        },
        'measurement_noise': {
            'name': 'Measurement Noise',
            'description': 'Noise level in viscoelastic measurements',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.0, 0.1],
            'category': 'data_quality'
        },
        'reconstruction_method': {
            'name': 'Reconstruction Method',
            'description': 'Method for viscoelastic field reconstruction',
            'unit': 'dimensionless',
            'default': 'pinn',
            'range': ['pinn', 'interpolation', 'regression', 'neural_network'],
            'category': 'reconstruction_parameters'
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
    
    'sparse_radiative_transfer': {
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
        'sparse_data_ratio': {
            'name': 'Sparse Data Ratio',
            'description': 'Ratio of available radiative data',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.01, 1.0],
            'category': 'sparse_data_parameters'
        },
        'measurement_noise': {
            'name': 'Measurement Noise',
            'description': 'Noise level in radiative measurements',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.0, 0.1],
            'category': 'data_quality'
        },
        'reconstruction_method': {
            'name': 'Reconstruction Method',
            'description': 'Method for radiative field reconstruction',
            'unit': 'dimensionless',
            'default': 'pinn',
            'range': ['pinn', 'interpolation', 'regression', 'neural_network'],
            'category': 'reconstruction_parameters'
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
    
    'sparse_shallow_water': {
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
            'description': 'Coriolis parameter',
            'unit': '1/s',
            'default': 1e-4,
            'range': [1e-5, 1e-3],
            'category': 'geophysical_properties'
        },
        'sparse_data_ratio': {
            'name': 'Sparse Data Ratio',
            'description': 'Ratio of available shallow water data',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.01, 1.0],
            'category': 'sparse_data_parameters'
        },
        'measurement_noise': {
            'name': 'Measurement Noise',
            'description': 'Noise level in shallow water measurements',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.0, 0.1],
            'category': 'data_quality'
        },
        'reconstruction_method': {
            'name': 'Reconstruction Method',
            'description': 'Method for shallow water field reconstruction',
            'unit': 'dimensionless',
            'default': 'pinn',
            'range': ['pinn', 'interpolation', 'regression', 'neural_network'],
            'category': 'reconstruction_parameters'
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
    },
    
    'sparse_maxwell': {
        'electrical_conductivity': {
            'name': 'Electrical Conductivity (σ)',
            'description': 'Electrical conductivity',
            'unit': 'S/m',
            'default': 1e6,
            'range': [1e-6, 1e8],
            'category': 'electrical_properties'
        },
        'magnetic_permeability': {
            'name': 'Magnetic Permeability (μ)',
            'description': 'Magnetic permeability',
            'unit': 'H/m',
            'default': 1.257e-6,
            'range': [1e-7, 1e-5],
            'category': 'magnetic_properties'
        },
        'sparse_data_ratio': {
            'name': 'Sparse Data Ratio',
            'description': 'Ratio of available electromagnetic data',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.01, 1.0],
            'category': 'sparse_data_parameters'
        },
        'measurement_noise': {
            'name': 'Measurement Noise',
            'description': 'Noise level in electromagnetic measurements',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.0, 0.1],
            'category': 'data_quality'
        },
        'reconstruction_method': {
            'name': 'Reconstruction Method',
            'description': 'Method for electromagnetic field reconstruction',
            'unit': 'dimensionless',
            'default': 'pinn',
            'range': ['pinn', 'interpolation', 'regression', 'neural_network'],
            'category': 'reconstruction_parameters'
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
    
    'sparse_helmholtz': {
        'wavenumber': {
            'name': 'Wavenumber (k)',
            'description': 'Wavenumber in Helmholtz equation',
            'unit': '1/m',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'wave_properties'
        },
        'sparse_data_ratio': {
            'name': 'Sparse Data Ratio',
            'description': 'Ratio of available Helmholtz data',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.01, 1.0],
            'category': 'sparse_data_parameters'
        },
        'measurement_noise': {
            'name': 'Measurement Noise',
            'description': 'Noise level in Helmholtz measurements',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.0, 0.1],
            'category': 'data_quality'
        },
        'reconstruction_method': {
            'name': 'Reconstruction Method',
            'description': 'Method for Helmholtz field reconstruction',
            'unit': 'dimensionless',
            'default': 'pinn',
            'range': ['pinn', 'interpolation', 'regression', 'neural_network'],
            'category': 'reconstruction_parameters'
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
    
    'sparse_shm': {
        'natural_frequency': {
            'name': 'Natural Frequency (ω)',
            'description': 'Natural frequency of oscillation',
            'unit': 'rad/s',
            'default': 1.0,
            'range': [0.1, 100.0],
            'category': 'mechanical_properties'
        },
        'sparse_data_ratio': {
            'name': 'Sparse Data Ratio',
            'description': 'Ratio of available SHM data',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.01, 1.0],
            'category': 'sparse_data_parameters'
        },
        'measurement_noise': {
            'name': 'Measurement Noise',
            'description': 'Noise level in SHM measurements',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.0, 0.1],
            'category': 'data_quality'
        },
        'reconstruction_method': {
            'name': 'Reconstruction Method',
            'description': 'Method for SHM field reconstruction',
            'unit': 'dimensionless',
            'default': 'pinn',
            'range': ['pinn', 'interpolation', 'regression', 'neural_network'],
            'category': 'reconstruction_parameters'
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
    
    'sparse_advection_diffusion': {
        'diffusion_coefficient': {
            'name': 'Diffusion Coefficient (D)',
            'description': 'Diffusion coefficient',
            'unit': 'm²/s',
            'default': 1e-9,
            'range': [1e-12, 1e-6],
            'category': 'transport_properties'
        },
        'advection_velocity': {
            'name': 'Advection Velocity (v)',
            'description': 'Advection velocity vector',
            'unit': 'm/s',
            'default': 1e-3,
            'range': [1e-6, 1e0],
            'category': 'transport_properties'
        },
        'sparse_data_ratio': {
            'name': 'Sparse Data Ratio',
            'description': 'Ratio of available concentration data',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.01, 1.0],
            'category': 'sparse_data_parameters'
        },
        'measurement_noise': {
            'name': 'Measurement Noise',
            'description': 'Noise level in concentration measurements',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.0, 0.1],
            'category': 'data_quality'
        },
        'reconstruction_method': {
            'name': 'Reconstruction Method',
            'description': 'Method for concentration field reconstruction',
            'unit': 'dimensionless',
            'default': 'pinn',
            'range': ['pinn', 'interpolation', 'regression', 'neural_network'],
            'category': 'reconstruction_parameters'
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
    
    'sparse_heat_transfer': {
        'thermal_conductivity': {
            'name': 'Thermal Conductivity (k)',
            'description': 'Thermal conductivity',
            'unit': 'W/(m·K)',
            'default': 50.0,
            'range': [0.1, 1000.0],
            'category': 'thermal_properties'
        },
        'heat_capacity': {
            'name': 'Heat Capacity (c_p)',
            'description': 'Specific heat capacity',
            'unit': 'J/(kg·K)',
            'default': 500.0,
            'range': [100.0, 5000.0],
            'category': 'thermal_properties'
        },
        'density': {
            'name': 'Density (ρ)',
            'description': 'Material density',
            'unit': 'kg/m³',
            'default': 8000.0,
            'range': [100.0, 20000.0],
            'category': 'material_properties'
        },
        'sparse_data_ratio': {
            'name': 'Sparse Data Ratio',
            'description': 'Ratio of available thermal data',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.01, 1.0],
            'category': 'sparse_data_parameters'
        },
        'measurement_noise': {
            'name': 'Measurement Noise',
            'description': 'Noise level in thermal measurements',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.0, 0.1],
            'category': 'data_quality'
        },
        'reconstruction_method': {
            'name': 'Reconstruction Method',
            'description': 'Method for thermal field reconstruction',
            'unit': 'dimensionless',
            'default': 'pinn',
            'range': ['pinn', 'interpolation', 'regression', 'neural_network'],
            'category': 'reconstruction_parameters'
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
    
    'sparse_magnetohydrodynamics': {
        'magnetic_permeability': {
            'name': 'Magnetic Permeability (μ)',
            'description': 'Magnetic permeability',
            'unit': 'H/m',
            'default': 1.257e-6,
            'range': [1e-7, 1e-5],
            'category': 'magnetic_properties'
        },
        'electrical_conductivity': {
            'name': 'Electrical Conductivity (σ)',
            'description': 'Electrical conductivity',
            'unit': 'S/m',
            'default': 1e6,
            'range': [1e-6, 1e8],
            'category': 'electrical_properties'
        },
        'viscosity': {
            'name': 'Viscosity (μ)',
            'description': 'Dynamic viscosity',
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
        'sparse_data_ratio': {
            'name': 'Sparse Data Ratio',
            'description': 'Ratio of available MHD data',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.01, 1.0],
            'category': 'sparse_data_parameters'
        },
        'measurement_noise': {
            'name': 'Measurement Noise',
            'description': 'Noise level in MHD measurements',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.0, 0.1],
            'category': 'data_quality'
        },
        'reconstruction_method': {
            'name': 'Reconstruction Method',
            'description': 'Method for MHD field reconstruction',
            'unit': 'dimensionless',
            'default': 'pinn',
            'range': ['pinn', 'interpolation', 'regression', 'neural_network'],
            'category': 'reconstruction_parameters'
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
    
    'sparse_thermoelasticity': {
        'elastic_modulus': {
            'name': 'Elastic Modulus (E)',
            'description': 'Young\'s modulus',
            'unit': 'GPa',
            'default': 200.0,
            'range': [1.0, 1000.0],
            'category': 'mechanical_properties'
        },
        'thermal_expansion': {
            'name': 'Thermal Expansion (α)',
            'description': 'Thermal expansion coefficient',
            'unit': '1/K',
            'default': 1e-5,
            'range': [1e-7, 1e-3],
            'category': 'thermal_properties'
        },
        'thermal_conductivity': {
            'name': 'Thermal Conductivity (k)',
            'description': 'Thermal conductivity',
            'unit': 'W/(m·K)',
            'default': 50.0,
            'range': [0.1, 1000.0],
            'category': 'thermal_properties'
        },
        'sparse_data_ratio': {
            'name': 'Sparse Data Ratio',
            'description': 'Ratio of available thermoelastic data',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.01, 1.0],
            'category': 'sparse_data_parameters'
        },
        'measurement_noise': {
            'name': 'Measurement Noise',
            'description': 'Noise level in thermoelastic measurements',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.0, 0.1],
            'category': 'data_quality'
        },
        'reconstruction_method': {
            'name': 'Reconstruction Method',
            'description': 'Method for thermoelastic field reconstruction',
            'unit': 'dimensionless',
            'default': 'pinn',
            'range': ['pinn', 'interpolation', 'regression', 'neural_network'],
            'category': 'reconstruction_parameters'
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
    
    'sparse_elastic_wave': {
        'elastic_modulus': {
            'name': 'Elastic Modulus (E)',
            'description': 'Young\'s modulus',
            'unit': 'GPa',
            'default': 200.0,
            'range': [1.0, 1000.0],
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
            'default': 8000.0,
            'range': [100.0, 20000.0],
            'category': 'material_properties'
        },
        'sparse_data_ratio': {
            'name': 'Sparse Data Ratio',
            'description': 'Ratio of available elastic wave data',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.01, 1.0],
            'category': 'sparse_data_parameters'
        },
        'measurement_noise': {
            'name': 'Measurement Noise',
            'description': 'Noise level in elastic wave measurements',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.0, 0.1],
            'category': 'data_quality'
        },
        'reconstruction_method': {
            'name': 'Reconstruction Method',
            'description': 'Method for elastic wave field reconstruction',
            'unit': 'dimensionless',
            'default': 'pinn',
            'range': ['pinn', 'interpolation', 'regression', 'neural_network'],
            'category': 'reconstruction_parameters'
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
    
    'sparse_nuclear_thermal': {
        'thermal_conductivity': {
            'name': 'Thermal Conductivity (k)',
            'description': 'Thermal conductivity',
            'unit': 'W/(m·K)',
            'default': 50.0,
            'range': [0.1, 1000.0],
            'category': 'thermal_properties'
        },
        'nuclear_source_strength': {
            'name': 'Nuclear Source Strength (S)',
            'description': 'Nuclear heat source strength',
            'unit': 'W/m³',
            'default': 1e6,
            'range': [1e3, 1e9],
            'category': 'nuclear_properties'
        },
        'sparse_data_ratio': {
            'name': 'Sparse Data Ratio',
            'description': 'Ratio of available nuclear thermal data',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.01, 1.0],
            'category': 'sparse_data_parameters'
        },
        'measurement_noise': {
            'name': 'Measurement Noise',
            'description': 'Noise level in nuclear thermal measurements',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.0, 0.1],
            'category': 'data_quality'
        },
        'reconstruction_method': {
            'name': 'Reconstruction Method',
            'description': 'Method for nuclear thermal field reconstruction',
            'unit': 'dimensionless',
            'default': 'pinn',
            'range': ['pinn', 'interpolation', 'regression', 'neural_network'],
            'category': 'reconstruction_parameters'
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
    
    'sparse_quantum_mechanical': {
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
            'name': 'Potential Strength (V₀)',
            'description': 'Potential well strength',
            'unit': 'J',
            'default': 1e-20,
            'range': [1e-25, 1e-15],
            'category': 'quantum_properties'
        },
        'sparse_data_ratio': {
            'name': 'Sparse Data Ratio',
            'description': 'Ratio of available quantum data',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.01, 1.0],
            'category': 'sparse_data_parameters'
        },
        'measurement_noise': {
            'name': 'Measurement Noise',
            'description': 'Noise level in quantum measurements',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.0, 0.1],
            'category': 'data_quality'
        },
        'reconstruction_method': {
            'name': 'Reconstruction Method',
            'description': 'Method for quantum field reconstruction',
            'unit': 'dimensionless',
            'default': 'pinn',
            'range': ['pinn', 'interpolation', 'regression', 'neural_network'],
            'category': 'reconstruction_parameters'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1e-9,
            'range': [1e-12, 1e-6],
            'category': 'domain_properties'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration',
            'unit': 's',
            'default': 1e-12,
            'range': [1e-15, 1e-9],
            'category': 'temporal_properties'
        }
    },
    
    'sparse_phase_field_allen_cahn': {
        'mobility': {
            'name': 'Mobility (M)',
            'description': 'Phase field mobility',
            'unit': 'm²/(J·s)',
            'default': 1e-3,
            'range': [1e-6, 1e-1],
            'category': 'phase_field'
        },
        'interface_thickness': {
            'name': 'Interface Thickness (ε)',
            'description': 'Phase field interface thickness',
            'unit': 'm',
            'default': 1e-6,
            'range': [1e-9, 1e-3],
            'category': 'phase_field'
        },
        'double_well_parameter': {
            'name': 'Double Well Parameter (a)',
            'description': 'Double well potential parameter',
            'unit': 'J/m³',
            'default': 1e6,
            'range': [1e3, 1e9],
            'category': 'phase_field'
        },
        'sparse_data_ratio': {
            'name': 'Sparse Data Ratio',
            'description': 'Ratio of available Allen-Cahn data',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.01, 1.0],
            'category': 'sparse_data_parameters'
        },
        'measurement_noise': {
            'name': 'Measurement Noise',
            'description': 'Noise level in Allen-Cahn measurements',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.0, 0.1],
            'category': 'data_quality'
        },
        'reconstruction_method': {
            'name': 'Reconstruction Method',
            'description': 'Method for Allen-Cahn field reconstruction',
            'unit': 'dimensionless',
            'default': 'pinn',
            'range': ['pinn', 'interpolation', 'regression', 'neural_network'],
            'category': 'reconstruction_parameters'
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
    
    'sparse_phase_field_cahn_hilliard': {
        'mobility': {
            'name': 'Mobility (M)',
            'description': 'Phase field mobility',
            'unit': 'm²/(J·s)',
            'default': 1e-3,
            'range': [1e-6, 1e-1],
            'category': 'phase_field'
        },
        'interface_thickness': {
            'name': 'Interface Thickness (ε)',
            'description': 'Phase field interface thickness',
            'unit': 'm',
            'default': 1e-6,
            'range': [1e-9, 1e-3],
            'category': 'phase_field'
        },
        'chemical_potential_parameter': {
            'name': 'Chemical Potential Parameter (μ₀)',
            'description': 'Chemical potential parameter',
            'unit': 'J/m³',
            'default': 1e6,
            'range': [1e3, 1e9],
            'category': 'phase_field'
        },
        'sparse_data_ratio': {
            'name': 'Sparse Data Ratio',
            'description': 'Ratio of available Cahn-Hilliard data',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.01, 1.0],
            'category': 'sparse_data_parameters'
        },
        'measurement_noise': {
            'name': 'Measurement Noise',
            'description': 'Noise level in Cahn-Hilliard measurements',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.0, 0.1],
            'category': 'data_quality'
        },
        'reconstruction_method': {
            'name': 'Reconstruction Method',
            'description': 'Method for Cahn-Hilliard field reconstruction',
            'unit': 'dimensionless',
            'default': 'pinn',
            'range': ['pinn', 'interpolation', 'regression', 'neural_network'],
            'category': 'reconstruction_parameters'
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
            'default': 86400.0,
            'range': [3600.0, 31536000.0],
            'category': 'temporal_properties'
        }
    },
    
    'sparse_atmospheric_oceanic': {
        'atmospheric_viscosity': {'name': 'Atmospheric Viscosity (μ_a)', 'description': 'Atmospheric dynamic viscosity', 'unit': 'Pa·s', 'default': 1.8e-5, 'range': [1e-6, 1e-4], 'category': 'atmospheric_properties'},
        'oceanic_viscosity': {'name': 'Oceanic Viscosity (μ_o)', 'description': 'Oceanic dynamic viscosity', 'unit': 'Pa·s', 'default': 0.001, 'range': [1e-4, 1e-2], 'category': 'oceanic_properties'},
        'atmospheric_density': {'name': 'Atmospheric Density (ρ_a)', 'description': 'Atmospheric density', 'unit': 'kg/m³', 'default': 1.2, 'range': [0.1, 10.0], 'category': 'atmospheric_properties'},
        'oceanic_density': {'name': 'Oceanic Density (ρ_o)', 'description': 'Oceanic density', 'unit': 'kg/m³', 'default': 1025.0, 'range': [1000.0, 1100.0], 'category': 'oceanic_properties'},
        'sparse_data_ratio': {'name': 'Sparse Data Ratio', 'description': 'Ratio of available atmospheric-oceanic data', 'unit': 'dimensionless', 'default': 0.1, 'range': [0.01, 1.0], 'category': 'sparse_data_parameters'},
        'measurement_noise': {'name': 'Measurement Noise', 'description': 'Noise level in atmospheric-oceanic measurements', 'unit': 'dimensionless', 'default': 0.01, 'range': [0.0, 0.1], 'category': 'data_quality'},
        'reconstruction_method': {'name': 'Reconstruction Method', 'description': 'Method for atmospheric-oceanic field reconstruction', 'unit': 'dimensionless', 'default': 'pinn', 'range': ['pinn', 'interpolation', 'regression', 'neural_network'], 'category': 'reconstruction_parameters'},
        'domain_size': {'name': 'Domain Size', 'description': 'Spatial domain dimensions', 'unit': 'm', 'default': 1000.0, 'range': [100.0, 10000.0], 'category': 'domain_properties'},
        'time_duration': {'name': 'Time Duration', 'description': 'Simulation time duration', 'unit': 's', 'default': 86400.0, 'range': [3600.0, 31536000.0], 'category': 'temporal_properties'}
    },
    
    'sparse_biomechanical_transport': {
        'elastic_modulus': {'name': 'Elastic Modulus (E)', 'description': 'Tissue elastic modulus', 'unit': 'kPa', 'default': 10.0, 'range': [0.1, 1000.0], 'category': 'mechanical_properties'},
        'diffusion_coefficient': {'name': 'Diffusion Coefficient (D)', 'description': 'Transport diffusion coefficient', 'unit': 'm²/s', 'default': 1e-9, 'range': [1e-12, 1e-6], 'category': 'transport_properties'},
        'permeability': {'name': 'Permeability (κ)', 'description': 'Tissue permeability', 'unit': 'm²', 'default': 1e-12, 'range': [1e-20, 1e-8], 'category': 'transport_properties'},
        'sparse_data_ratio': {'name': 'Sparse Data Ratio', 'description': 'Ratio of available biomechanical data', 'unit': 'dimensionless', 'default': 0.1, 'range': [0.01, 1.0], 'category': 'sparse_data_parameters'},
        'measurement_noise': {'name': 'Measurement Noise', 'description': 'Noise level in biomechanical measurements', 'unit': 'dimensionless', 'default': 0.01, 'range': [0.0, 0.1], 'category': 'data_quality'},
        'reconstruction_method': {'name': 'Reconstruction Method', 'description': 'Method for biomechanical field reconstruction', 'unit': 'dimensionless', 'default': 'pinn', 'range': ['pinn', 'interpolation', 'regression', 'neural_network'], 'category': 'reconstruction_parameters'},
        'domain_size': {'name': 'Domain Size', 'description': 'Spatial domain dimensions', 'unit': 'm', 'default': 0.01, 'range': [0.001, 0.1], 'category': 'domain_properties'},
        'time_duration': {'name': 'Time Duration', 'description': 'Simulation time duration', 'unit': 's', 'default': 1.0, 'range': [0.1, 10.0], 'category': 'temporal_properties'}
    },
    
    'sparse_crystal_plasticity': {
        'shear_modulus': {'name': 'Shear Modulus (μ)', 'description': 'Shear modulus', 'unit': 'GPa', 'default': 80.0, 'range': [1.0, 500.0], 'category': 'mechanical_properties'},
        'burgers_vector': {'name': 'Burgers Vector (b)', 'description': 'Burgers vector magnitude', 'unit': 'm', 'default': 2.5e-10, 'range': [1e-11, 1e-9], 'category': 'crystal_properties'},
        'initial_dislocation_density': {'name': 'Initial Dislocation Density (ρ₀)', 'description': 'Initial dislocation density', 'unit': '1/m²', 'default': 1e12, 'range': [1e10, 1e15], 'category': 'crystal_properties'},
        'sparse_data_ratio': {'name': 'Sparse Data Ratio', 'description': 'Ratio of available crystal plasticity data', 'unit': 'dimensionless', 'default': 0.1, 'range': [0.01, 1.0], 'category': 'sparse_data_parameters'},
        'measurement_noise': {'name': 'Measurement Noise', 'description': 'Noise level in crystal plasticity measurements', 'unit': 'dimensionless', 'default': 0.01, 'range': [0.0, 0.1], 'category': 'data_quality'},
        'reconstruction_method': {'name': 'Reconstruction Method', 'description': 'Method for crystal plasticity field reconstruction', 'unit': 'dimensionless', 'default': 'pinn', 'range': ['pinn', 'interpolation', 'regression', 'neural_network'], 'category': 'reconstruction_parameters'},
        'domain_size': {'name': 'Domain Size', 'description': 'Spatial domain dimensions', 'unit': 'm', 'default': 1e-3, 'range': [1e-6, 1e-1], 'category': 'domain_properties'},
        'time_duration': {'name': 'Time Duration', 'description': 'Simulation time duration', 'unit': 's', 'default': 1.0, 'range': [0.1, 10.0], 'category': 'temporal_properties'}
    },
    
    'sparse_diffusion_solids': {
        'diffusion_coefficient': {'name': 'Diffusion Coefficient (D)', 'description': 'Diffusion coefficient in solids', 'unit': 'm²/s', 'default': 1e-12, 'range': [1e-15, 1e-9], 'category': 'diffusion_properties'},
        'activation_energy': {'name': 'Activation Energy (E_a)', 'description': 'Diffusion activation energy', 'unit': 'J/mol', 'default': 1e5, 'range': [1e4, 1e6], 'category': 'diffusion_properties'},
        'pre_exponential_factor': {'name': 'Pre-exponential Factor (D₀)', 'description': 'Pre-exponential diffusion factor', 'unit': 'm²/s', 'default': 1e-6, 'range': [1e-9, 1e-3], 'category': 'diffusion_properties'},
        'sparse_data_ratio': {'name': 'Sparse Data Ratio', 'description': 'Ratio of available diffusion data', 'unit': 'dimensionless', 'default': 0.1, 'range': [0.01, 1.0], 'category': 'sparse_data_parameters'},
        'measurement_noise': {'name': 'Measurement Noise', 'description': 'Noise level in diffusion measurements', 'unit': 'dimensionless', 'default': 0.01, 'range': [0.0, 0.1], 'category': 'data_quality'},
        'reconstruction_method': {'name': 'Reconstruction Method', 'description': 'Method for diffusion field reconstruction', 'unit': 'dimensionless', 'default': 'pinn', 'range': ['pinn', 'interpolation', 'regression', 'neural_network'], 'category': 'reconstruction_parameters'},
        'domain_size': {'name': 'Domain Size', 'description': 'Spatial domain dimensions', 'unit': 'm', 'default': 1e-3, 'range': [1e-6, 1e-1], 'category': 'domain_properties'},
        'time_duration': {'name': 'Time Duration', 'description': 'Simulation time duration', 'unit': 's', 'default': 1.0, 'range': [0.1, 10.0], 'category': 'temporal_properties'}
    },
    
    'sparse_electromagnetic_thermal': {
        'electrical_conductivity': {'name': 'Electrical Conductivity (σ)', 'description': 'Electrical conductivity', 'unit': 'S/m', 'default': 1e6, 'range': [1e-6, 1e8], 'category': 'electrical_properties'},
        'thermal_conductivity': {'name': 'Thermal Conductivity (k)', 'description': 'Thermal conductivity', 'unit': 'W/(m·K)', 'default': 50.0, 'range': [0.1, 1000.0], 'category': 'thermal_properties'},
        'heat_capacity': {'name': 'Heat Capacity (c_p)', 'description': 'Specific heat capacity', 'unit': 'J/(kg·K)', 'default': 500.0, 'range': [100.0, 5000.0], 'category': 'thermal_properties'},
        'density': {'name': 'Density (ρ)', 'description': 'Material density', 'unit': 'kg/m³', 'default': 8000.0, 'range': [100.0, 20000.0], 'category': 'material_properties'},
        'sparse_data_ratio': {'name': 'Sparse Data Ratio', 'description': 'Ratio of available EM-thermal data', 'unit': 'dimensionless', 'default': 0.1, 'range': [0.01, 1.0], 'category': 'sparse_data_parameters'},
        'measurement_noise': {'name': 'Measurement Noise', 'description': 'Noise level in EM-thermal measurements', 'unit': 'dimensionless', 'default': 0.01, 'range': [0.0, 0.1], 'category': 'data_quality'},
        'reconstruction_method': {'name': 'Reconstruction Method', 'description': 'Method for EM-thermal field reconstruction', 'unit': 'dimensionless', 'default': 'pinn', 'range': ['pinn', 'interpolation', 'regression', 'neural_network'], 'category': 'reconstruction_parameters'},
        'domain_size': {'name': 'Domain Size', 'description': 'Spatial domain dimensions', 'unit': 'm', 'default': 1.0, 'range': [0.1, 10.0], 'category': 'domain_properties'},
        'time_duration': {'name': 'Time Duration', 'description': 'Simulation time duration', 'unit': 's', 'default': 1.0, 'range': [0.1, 10.0], 'category': 'temporal_properties'}
    },
    
    'sparse_fluid_structure_interaction': {
        'fluid_viscosity': {'name': 'Fluid Viscosity (μ_f)', 'description': 'Fluid dynamic viscosity', 'unit': 'Pa·s', 'default': 0.001, 'range': [1e-6, 1e-1], 'category': 'fluid_properties'},
        'fluid_density': {'name': 'Fluid Density (ρ_f)', 'description': 'Fluid density', 'unit': 'kg/m³', 'default': 1000.0, 'range': [1.0, 20000.0], 'category': 'fluid_properties'},
        'solid_elastic_modulus': {'name': 'Solid Elastic Modulus (E_s)', 'description': 'Solid Young\'s modulus', 'unit': 'GPa', 'default': 200.0, 'range': [1.0, 1000.0], 'category': 'mechanical_properties'},
        'solid_density': {'name': 'Solid Density (ρ_s)', 'description': 'Solid density', 'unit': 'kg/m³', 'default': 8000.0, 'range': [100.0, 20000.0], 'category': 'material_properties'},
        'sparse_data_ratio': {'name': 'Sparse Data Ratio', 'description': 'Ratio of available FSI data', 'unit': 'dimensionless', 'default': 0.1, 'range': [0.01, 1.0], 'category': 'sparse_data_parameters'},
        'measurement_noise': {'name': 'Measurement Noise', 'description': 'Noise level in FSI measurements', 'unit': 'dimensionless', 'default': 0.01, 'range': [0.0, 0.1], 'category': 'data_quality'},
        'reconstruction_method': {'name': 'Reconstruction Method', 'description': 'Method for FSI field reconstruction', 'unit': 'dimensionless', 'default': 'pinn', 'range': ['pinn', 'interpolation', 'regression', 'neural_network'], 'category': 'reconstruction_parameters'},
        'domain_size': {'name': 'Domain Size', 'description': 'Spatial domain dimensions', 'unit': 'm', 'default': 1.0, 'range': [0.1, 10.0], 'category': 'domain_properties'},
        'time_duration': {'name': 'Time Duration', 'description': 'Simulation time duration', 'unit': 's', 'default': 1.0, 'range': [0.1, 10.0], 'category': 'temporal_properties'}
    },
    
    'sparse_geophysical_flow': {
        'gravity': {'name': 'Gravity (g)', 'description': 'Acceleration due to gravity', 'unit': 'm/s²', 'default': 9.81, 'range': [1.0, 20.0], 'category': 'geophysical_properties'},
        'coriolis_parameter': {'name': 'Coriolis Parameter (f)', 'description': 'Coriolis parameter', 'unit': '1/s', 'default': 1e-4, 'range': [1e-5, 1e-3], 'category': 'geophysical_properties'},
        'viscosity': {'name': 'Viscosity (μ)', 'description': 'Dynamic viscosity', 'unit': 'Pa·s', 'default': 0.001, 'range': [1e-6, 1e-1], 'category': 'fluid_properties'},
        'density': {'name': 'Density (ρ)', 'description': 'Fluid density', 'unit': 'kg/m³', 'default': 1000.0, 'range': [1.0, 20000.0], 'category': 'fluid_properties'},
        'sparse_data_ratio': {'name': 'Sparse Data Ratio', 'description': 'Ratio of available geophysical data', 'unit': 'dimensionless', 'default': 0.1, 'range': [0.01, 1.0], 'category': 'sparse_data_parameters'},
        'measurement_noise': {'name': 'Measurement Noise', 'description': 'Noise level in geophysical measurements', 'unit': 'dimensionless', 'default': 0.01, 'range': [0.0, 0.1], 'category': 'data_quality'},
        'reconstruction_method': {'name': 'Reconstruction Method', 'description': 'Method for geophysical field reconstruction', 'unit': 'dimensionless', 'default': 'pinn', 'range': ['pinn', 'interpolation', 'regression', 'neural_network'], 'category': 'reconstruction_parameters'},
        'domain_size': {'name': 'Domain Size', 'description': 'Spatial domain dimensions', 'unit': 'm', 'default': 1000.0, 'range': [100.0, 10000.0], 'category': 'domain_properties'},
        'time_duration': {'name': 'Time Duration', 'description': 'Simulation time duration', 'unit': 's', 'default': 3600.0, 'range': [100.0, 86400.0], 'category': 'temporal_properties'}
    },
    
    'sparse_grain_growth': {
        'mobility': {'name': 'Mobility (M)', 'description': 'Grain boundary mobility', 'unit': 'm²/(J·s)', 'default': 1e-3, 'range': [1e-6, 1e-1], 'category': 'grain_growth'},
        'surface_energy': {'name': 'Surface Energy (γ)', 'description': 'Grain boundary surface energy', 'unit': 'J/m²', 'default': 1.0, 'range': [0.1, 10.0], 'category': 'grain_growth'},
        'initial_grain_size': {'name': 'Initial Grain Size (R₀)', 'description': 'Initial average grain radius', 'unit': 'm', 'default': 1e-6, 'range': [1e-9, 1e-3], 'category': 'grain_growth'},
        'sparse_data_ratio': {'name': 'Sparse Data Ratio', 'description': 'Ratio of available grain growth data', 'unit': 'dimensionless', 'default': 0.1, 'range': [0.01, 1.0], 'category': 'sparse_data_parameters'},
        'measurement_noise': {'name': 'Measurement Noise', 'description': 'Noise level in grain growth measurements', 'unit': 'dimensionless', 'default': 0.01, 'range': [0.0, 0.1], 'category': 'data_quality'},
        'reconstruction_method': {'name': 'Reconstruction Method', 'description': 'Method for grain growth field reconstruction', 'unit': 'dimensionless', 'default': 'pinn', 'range': ['pinn', 'interpolation', 'regression', 'neural_network'], 'category': 'reconstruction_parameters'},
        'domain_size': {'name': 'Domain Size', 'description': 'Spatial domain dimensions', 'unit': 'm', 'default': 1e-3, 'range': [1e-6, 1e-1], 'category': 'domain_properties'},
        'time_duration': {'name': 'Time Duration', 'description': 'Simulation time duration', 'unit': 's', 'default': 1.0, 'range': [0.1, 10.0], 'category': 'temporal_properties'}
    },
    
    'sparse_laser_heat_source': {
        'laser_power': {'name': 'Laser Power (P)', 'description': 'Laser beam power', 'unit': 'W', 'default': 1000.0, 'range': [1.0, 10000.0], 'category': 'laser_properties'},
        'beam_radius': {'name': 'Beam Radius (σ)', 'description': 'Laser beam radius', 'unit': 'm', 'default': 1e-3, 'range': [1e-6, 1e-2], 'category': 'laser_properties'},
        'absorption_coefficient': {'name': 'Absorption Coefficient (α)', 'description': 'Material absorption coefficient', 'unit': '1/m', 'default': 1e6, 'range': [1e3, 1e8], 'category': 'laser_properties'},
        'sparse_data_ratio': {'name': 'Sparse Data Ratio', 'description': 'Ratio of available laser heat source data', 'unit': 'dimensionless', 'default': 0.1, 'range': [0.01, 1.0], 'category': 'sparse_data_parameters'},
        'measurement_noise': {'name': 'Measurement Noise', 'description': 'Noise level in laser heat source measurements', 'unit': 'dimensionless', 'default': 0.01, 'range': [0.0, 0.1], 'category': 'data_quality'},
        'reconstruction_method': {'name': 'Reconstruction Method', 'description': 'Method for laser heat source field reconstruction', 'unit': 'dimensionless', 'default': 'pinn', 'range': ['pinn', 'interpolation', 'regression', 'neural_network'], 'category': 'reconstruction_parameters'},
        'domain_size': {'name': 'Domain Size', 'description': 'Spatial domain dimensions', 'unit': 'm', 'default': 1e-2, 'range': [1e-4, 1e-1], 'category': 'domain_properties'},
        'time_duration': {'name': 'Time Duration', 'description': 'Simulation time duration', 'unit': 's', 'default': 1.0, 'range': [0.1, 10.0], 'category': 'temporal_properties'}
    },
    
    'sparse_melt_pool_dynamics': {
        'surface_tension': {'name': 'Surface Tension (γ)', 'description': 'Liquid surface tension', 'unit': 'N/m', 'default': 1.0, 'range': [0.01, 10.0], 'category': 'fluid_properties'},
        'viscosity': {'name': 'Viscosity (μ)', 'description': 'Dynamic viscosity', 'unit': 'Pa·s', 'default': 0.001, 'range': [1e-6, 1e-1], 'category': 'fluid_properties'},
        'density': {'name': 'Density (ρ)', 'description': 'Fluid density', 'unit': 'kg/m³', 'default': 7000.0, 'range': [1000.0, 20000.0], 'category': 'fluid_properties'},
        'sparse_data_ratio': {'name': 'Sparse Data Ratio', 'description': 'Ratio of available melt pool data', 'unit': 'dimensionless', 'default': 0.1, 'range': [0.01, 1.0], 'category': 'sparse_data_parameters'},
        'measurement_noise': {'name': 'Measurement Noise', 'description': 'Noise level in melt pool measurements', 'unit': 'dimensionless', 'default': 0.01, 'range': [0.0, 0.1], 'category': 'data_quality'},
        'reconstruction_method': {'name': 'Reconstruction Method', 'description': 'Method for melt pool field reconstruction', 'unit': 'dimensionless', 'default': 'pinn', 'range': ['pinn', 'interpolation', 'regression', 'neural_network'], 'category': 'reconstruction_parameters'},
        'domain_size': {'name': 'Domain Size', 'description': 'Spatial domain dimensions', 'unit': 'm', 'default': 1e-3, 'range': [1e-6, 1e-2], 'category': 'domain_properties'},
        'time_duration': {'name': 'Time Duration', 'description': 'Simulation time duration', 'unit': 's', 'default': 1.0, 'range': [0.1, 10.0], 'category': 'temporal_properties'}
    },
    
    'sparse_microstructure_evolution': {
        'phase_field_mobility': {'name': 'Phase Field Mobility (M)', 'description': 'Phase field mobility', 'unit': 'm²/(J·s)', 'default': 1e-3, 'range': [1e-6, 1e-1], 'category': 'phase_field'},
        'interface_energy': {'name': 'Interface Energy (γ)', 'description': 'Interface energy', 'unit': 'J/m²', 'default': 1.0, 'range': [0.1, 10.0], 'category': 'phase_field'},
        'transformation_rate': {'name': 'Transformation Rate (k)', 'description': 'Phase transformation rate', 'unit': '1/s', 'default': 1e-3, 'range': [1e-6, 1e0], 'category': 'transformation_properties'},
        'sparse_data_ratio': {'name': 'Sparse Data Ratio', 'description': 'Ratio of available microstructure evolution data', 'unit': 'dimensionless', 'default': 0.1, 'range': [0.01, 1.0], 'category': 'sparse_data_parameters'},
        'measurement_noise': {'name': 'Measurement Noise', 'description': 'Noise level in microstructure evolution measurements', 'unit': 'dimensionless', 'default': 0.01, 'range': [0.0, 0.1], 'category': 'data_quality'},
        'reconstruction_method': {'name': 'Reconstruction Method', 'description': 'Method for microstructure evolution field reconstruction', 'unit': 'dimensionless', 'default': 'pinn', 'range': ['pinn', 'interpolation', 'regression', 'neural_network'], 'category': 'reconstruction_parameters'},
        'domain_size': {'name': 'Domain Size', 'description': 'Spatial domain dimensions', 'unit': 'm', 'default': 1e-3, 'range': [1e-6, 1e-1], 'category': 'domain_properties'},
        'time_duration': {'name': 'Time Duration', 'description': 'Simulation time duration', 'unit': 's', 'default': 1.0, 'range': [0.1, 10.0], 'category': 'temporal_properties'}
    },
    
    'sparse_precipitation_nucleation': {
        'nucleation_rate': {'name': 'Nucleation Rate (J₀)', 'description': 'Pre-exponential nucleation rate', 'unit': '1/(m³·s)', 'default': 1e20, 'range': [1e15, 1e25], 'category': 'nucleation_properties'},
        'critical_free_energy': {'name': 'Critical Free Energy (ΔG*)', 'description': 'Critical free energy barrier', 'unit': 'J', 'default': 1e-20, 'range': [1e-25, 1e-15], 'category': 'nucleation_properties'},
        'temperature': {'name': 'Temperature (T)', 'description': 'System temperature', 'unit': 'K', 'default': 300.0, 'range': [100.0, 2000.0], 'category': 'thermal_properties'},
        'sparse_data_ratio': {'name': 'Sparse Data Ratio', 'description': 'Ratio of available nucleation data', 'unit': 'dimensionless', 'default': 0.1, 'range': [0.01, 1.0], 'category': 'sparse_data_parameters'},
        'measurement_noise': {'name': 'Measurement Noise', 'description': 'Noise level in nucleation measurements', 'unit': 'dimensionless', 'default': 0.01, 'range': [0.0, 0.1], 'category': 'data_quality'},
        'reconstruction_method': {'name': 'Reconstruction Method', 'description': 'Method for nucleation field reconstruction', 'unit': 'dimensionless', 'default': 'pinn', 'range': ['pinn', 'interpolation', 'regression', 'neural_network'], 'category': 'reconstruction_parameters'},
        'domain_size': {'name': 'Domain Size', 'description': 'Spatial domain dimensions', 'unit': 'm', 'default': 1e-3, 'range': [1e-6, 1e-1], 'category': 'domain_properties'},
        'time_duration': {'name': 'Time Duration', 'description': 'Simulation time duration', 'unit': 's', 'default': 1.0, 'range': [0.1, 10.0], 'category': 'temporal_properties'}
    },
    
    'sparse_residual_stress': {
        'elastic_modulus': {'name': 'Elastic Modulus (E)', 'description': 'Young\'s modulus', 'unit': 'GPa', 'default': 200.0, 'range': [1.0, 1000.0], 'category': 'mechanical_properties'},
        'thermal_expansion': {'name': 'Thermal Expansion (α)', 'description': 'Thermal expansion coefficient', 'unit': '1/K', 'default': 1e-5, 'range': [1e-7, 1e-3], 'category': 'thermal_properties'},
        'thermal_strain': {'name': 'Thermal Strain (εᵗ)', 'description': 'Thermal strain contribution', 'unit': 'dimensionless', 'default': 1e-3, 'range': [1e-6, 1e-1], 'category': 'thermal_properties'},
        'sparse_data_ratio': {'name': 'Sparse Data Ratio', 'description': 'Ratio of available residual stress data', 'unit': 'dimensionless', 'default': 0.1, 'range': [0.01, 1.0], 'category': 'sparse_data_parameters'},
        'measurement_noise': {'name': 'Measurement Noise', 'description': 'Noise level in residual stress measurements', 'unit': 'dimensionless', 'default': 0.01, 'range': [0.0, 0.1], 'category': 'data_quality'},
        'reconstruction_method': {'name': 'Reconstruction Method', 'description': 'Method for residual stress field reconstruction', 'unit': 'dimensionless', 'default': 'pinn', 'range': ['pinn', 'interpolation', 'regression', 'neural_network'], 'category': 'reconstruction_parameters'},
        'domain_size': {'name': 'Domain Size', 'description': 'Spatial domain dimensions', 'unit': 'm', 'default': 1.0, 'range': [0.1, 10.0], 'category': 'domain_properties'},
        'time_duration': {'name': 'Time Duration', 'description': 'Simulation time duration', 'unit': 's', 'default': 1.0, 'range': [0.1, 10.0], 'category': 'temporal_properties'}
    },
    
    'sparse_sintering': {
        'diffusion_coefficient': {'name': 'Diffusion Coefficient (D)', 'description': 'Sintering diffusion coefficient', 'unit': 'm²/s', 'default': 1e-12, 'range': [1e-15, 1e-9], 'category': 'sintering_properties'},
        'initial_density': {'name': 'Initial Density (ρ₀)', 'description': 'Initial material density', 'unit': 'kg/m³', 'default': 4000.0, 'range': [1000.0, 8000.0], 'category': 'sintering_properties'},
        'final_density': {'name': 'Final Density (ρ_f)', 'description': 'Final material density', 'unit': 'kg/m³', 'default': 8000.0, 'range': [4000.0, 20000.0], 'category': 'sintering_properties'},
        'sparse_data_ratio': {'name': 'Sparse Data Ratio', 'description': 'Ratio of available sintering data', 'unit': 'dimensionless', 'default': 0.1, 'range': [0.01, 1.0], 'category': 'sparse_data_parameters'},
        'measurement_noise': {'name': 'Measurement Noise', 'description': 'Noise level in sintering measurements', 'unit': 'dimensionless', 'default': 0.01, 'range': [0.0, 0.1], 'category': 'data_quality'},
        'reconstruction_method': {'name': 'Reconstruction Method', 'description': 'Method for sintering field reconstruction', 'unit': 'dimensionless', 'default': 'pinn', 'range': ['pinn', 'interpolation', 'regression', 'neural_network'], 'category': 'reconstruction_parameters'},
        'domain_size': {'name': 'Domain Size', 'description': 'Spatial domain dimensions', 'unit': 'm', 'default': 1e-3, 'range': [1e-6, 1e-1], 'category': 'domain_properties'},
        'time_duration': {'name': 'Time Duration', 'description': 'Simulation time duration', 'unit': 's', 'default': 1.0, 'range': [0.1, 10.0], 'category': 'temporal_properties'}
    },
    
    'sparse_solidification_stefan': {
        'thermal_diffusivity': {'name': 'Thermal Diffusivity (α)', 'description': 'Thermal diffusivity coefficient', 'unit': 'm²/s', 'default': 1e-5, 'range': [1e-8, 1e-3], 'category': 'thermal_properties'},
        'latent_heat': {'name': 'Latent Heat (L)', 'description': 'Latent heat of fusion', 'unit': 'J/kg', 'default': 3.34e5, 'range': [1e4, 1e6], 'category': 'thermal_properties'},
        'melting_temperature': {'name': 'Melting Temperature (T_m)', 'description': 'Melting temperature', 'unit': 'K', 'default': 273.15, 'range': [100.0, 2000.0], 'category': 'thermal_properties'},
        'sparse_data_ratio': {'name': 'Sparse Data Ratio', 'description': 'Ratio of available Stefan problem data', 'unit': 'dimensionless', 'default': 0.1, 'range': [0.01, 1.0], 'category': 'sparse_data_parameters'},
        'measurement_noise': {'name': 'Measurement Noise', 'description': 'Noise level in Stefan problem measurements', 'unit': 'dimensionless', 'default': 0.01, 'range': [0.0, 0.1], 'category': 'data_quality'},
        'reconstruction_method': {'name': 'Reconstruction Method', 'description': 'Method for Stefan problem field reconstruction', 'unit': 'dimensionless', 'default': 'pinn', 'range': ['pinn', 'interpolation', 'regression', 'neural_network'], 'category': 'reconstruction_parameters'},
        'domain_size': {'name': 'Domain Size', 'description': 'Spatial domain dimensions', 'unit': 'm', 'default': 1.0, 'range': [0.1, 10.0], 'category': 'domain_properties'},
        'time_duration': {'name': 'Time Duration', 'description': 'Simulation time duration', 'unit': 's', 'default': 1.0, 'range': [0.1, 10.0], 'category': 'temporal_properties'}
    }
} 