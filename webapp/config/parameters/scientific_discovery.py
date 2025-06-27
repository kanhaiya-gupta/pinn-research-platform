"""
Scientific Discovery Parameters
Parameters for discovering new physical laws and relationships.
"""

SCIENTIFIC_DISCOVERY_PARAMETERS_DICT = {
    # Discovery Parameters
    'discovery_method': {
        'name': 'Discovery Method',
        'description': 'Method for scientific discovery',
        'unit': 'dimensionless',
        'default': 'symbolic_regression',
        'range': ['symbolic_regression', 'genetic_programming', 'sparse_regression', 'neural_ode'],
        'category': 'discovery_parameters',
        'discovery_type': 'equation_discovery'
    },
    'complexity_penalty': {
        'name': 'Complexity Penalty',
        'description': 'Penalty for model complexity',
        'unit': 'dimensionless',
        'default': 0.1,
        'range': [0.0, 1.0],
        'category': 'discovery_parameters',
        'discovery_type': 'equation_discovery'
    },
    'sparsity_weight': {
        'name': 'Sparsity Weight',
        'description': 'Weight for sparsity in discovery',
        'unit': 'dimensionless',
        'default': 1.0,
        'range': [0.0, 10.0],
        'category': 'discovery_parameters',
        'discovery_type': 'equation_discovery'
    },
    
    # Symbolic Regression Parameters
    'symbolic_operators': {
        'name': 'Symbolic Operators',
        'description': 'Mathematical operators for symbolic regression',
        'unit': 'dimensionless',
        'default': ['+', '-', '*', '/', 'sin', 'cos', 'exp', 'log'],
        'range': ['operators'],
        'category': 'symbolic_regression_parameters',
        'discovery_type': 'symbolic_regression'
    },
    'max_expression_depth': {
        'name': 'Maximum Expression Depth',
        'description': 'Maximum depth of symbolic expressions',
        'unit': 'dimensionless',
        'default': 5,
        'range': [1, 20],
        'category': 'symbolic_regression_parameters',
        'discovery_type': 'symbolic_regression'
    },
    'population_size': {
        'name': 'Population Size',
        'description': 'Population size for genetic programming',
        'unit': 'dimensionless',
        'default': 1000,
        'range': [100, 10000],
        'category': 'symbolic_regression_parameters',
        'discovery_type': 'symbolic_regression'
    },
    'generations': {
        'name': 'Number of Generations',
        'description': 'Number of generations for evolution',
        'unit': 'dimensionless',
        'default': 100,
        'range': [10, 1000],
        'category': 'symbolic_regression_parameters',
        'discovery_type': 'symbolic_regression'
    },
    
    # Sparse Regression Parameters
    'sparse_regression_method': {
        'name': 'Sparse Regression Method',
        'description': 'Method for sparse regression',
        'unit': 'dimensionless',
        'default': 'lasso',
        'range': ['lasso', 'ridge', 'elastic_net', 'group_lasso'],
        'category': 'sparse_regression_parameters',
        'discovery_type': 'sparse_regression'
    },
    'regularization_strength': {
        'name': 'Regularization Strength',
        'description': 'Strength of regularization for sparse regression',
        'unit': 'dimensionless',
        'default': 0.01,
        'range': [0.0, 1.0],
        'category': 'sparse_regression_parameters',
        'discovery_type': 'sparse_regression'
    },
    'feature_library': {
        'name': 'Feature Library',
        'description': 'Library of candidate features',
        'unit': 'dimensionless',
        'default': 'polynomial',
        'range': ['polynomial', 'trigonometric', 'exponential', 'custom'],
        'category': 'sparse_regression_parameters',
        'discovery_type': 'sparse_regression'
    },
    'max_degree': {
        'name': 'Maximum Polynomial Degree',
        'description': 'Maximum degree for polynomial features',
        'unit': 'dimensionless',
        'default': 3,
        'range': [1, 10],
        'category': 'sparse_regression_parameters',
        'discovery_type': 'sparse_regression'
    },
    
    # Neural ODE Parameters
    'neural_ode_depth': {
        'name': 'Neural ODE Depth',
        'description': 'Depth of neural ODE network',
        'unit': 'dimensionless',
        'default': 3,
        'range': [1, 10],
        'category': 'neural_ode_parameters',
        'discovery_type': 'neural_ode'
    },
    'neural_ode_width': {
        'name': 'Neural ODE Width',
        'description': 'Width of neural ODE network',
        'unit': 'dimensionless',
        'default': 50,
        'range': [10, 200],
        'category': 'neural_ode_parameters',
        'discovery_type': 'neural_ode'
    },
    'ode_solver': {
        'name': 'ODE Solver',
        'description': 'Solver for neural ODEs',
        'unit': 'dimensionless',
        'default': 'rk4',
        'range': ['euler', 'rk4', 'dopri5', 'adaptive'],
        'category': 'neural_ode_parameters',
        'discovery_type': 'neural_ode'
    },
    
    # Conservation Law Discovery
    'conservation_law_discovery': {
        'name': 'Conservation Law Discovery',
        'description': 'Whether to discover conservation laws',
        'unit': 'dimensionless',
        'default': True,
        'range': [True, False],
        'category': 'conservation_parameters',
        'discovery_type': 'conservation_laws'
    },
    'symmetry_detection': {
        'name': 'Symmetry Detection',
        'description': 'Whether to detect symmetries',
        'unit': 'dimensionless',
        'default': True,
        'range': [True, False],
        'category': 'conservation_parameters',
        'discovery_type': 'conservation_laws'
    },
    'invariant_quantities': {
        'name': 'Invariant Quantities',
        'description': 'Quantities that should be invariant',
        'unit': 'dimensionless',
        'default': ['energy', 'momentum'],
        'range': ['energy', 'momentum', 'angular_momentum', 'mass'],
        'category': 'conservation_parameters',
        'discovery_type': 'conservation_laws'
    },
    
    # Causal Discovery Parameters
    'causal_discovery': {
        'name': 'Causal Discovery',
        'description': 'Whether to perform causal discovery',
        'unit': 'dimensionless',
        'default': False,
        'range': [True, False],
        'category': 'causal_parameters',
        'discovery_type': 'causal_discovery'
    },
    'causal_method': {
        'name': 'Causal Discovery Method',
        'description': 'Method for causal discovery',
        'unit': 'dimensionless',
        'default': 'pcmci',
        'range': ['pcmci', 'granger', 'transfer_entropy', 'structural'],
        'category': 'causal_parameters',
        'discovery_type': 'causal_discovery'
    },
    'causal_threshold': {
        'name': 'Causal Threshold',
        'description': 'Threshold for causal relationships',
        'unit': 'dimensionless',
        'default': 0.05,
        'range': [0.0, 1.0],
        'category': 'causal_parameters',
        'discovery_type': 'causal_discovery'
    },
    
    # Dimensional Analysis Parameters
    'dimensional_analysis': {
        'name': 'Dimensional Analysis',
        'description': 'Whether to use dimensional analysis',
        'unit': 'dimensionless',
        'default': True,
        'range': [True, False],
        'category': 'dimensional_parameters',
        'discovery_type': 'dimensional_analysis'
    },
    'buckingham_pi': {
        'name': 'Buckingham Pi Theorem',
        'description': 'Whether to apply Buckingham Pi theorem',
        'unit': 'dimensionless',
        'default': True,
        'range': [True, False],
        'category': 'dimensional_parameters',
        'discovery_type': 'dimensional_analysis'
    },
    'dimensionless_groups': {
        'name': 'Dimensionless Groups',
        'description': 'Known dimensionless groups',
        'unit': 'dimensionless',
        'default': ['reynolds', 'prandtl', 'nusselt'],
        'range': ['reynolds', 'prandtl', 'nusselt', 'fourier', 'peclet'],
        'category': 'dimensional_parameters',
        'discovery_type': 'dimensional_analysis'
    },
    
    # Pattern Recognition Parameters
    'pattern_recognition': {
        'name': 'Pattern Recognition',
        'description': 'Whether to perform pattern recognition',
        'unit': 'dimensionless',
        'default': True,
        'range': [True, False],
        'category': 'pattern_parameters',
        'discovery_type': 'pattern_recognition'
    },
    'clustering_method': {
        'name': 'Clustering Method',
        'description': 'Method for clustering patterns',
        'unit': 'dimensionless',
        'default': 'kmeans',
        'range': ['kmeans', 'dbscan', 'hierarchical', 'spectral'],
        'category': 'pattern_parameters',
        'discovery_type': 'pattern_recognition'
    },
    'similarity_metric': {
        'name': 'Similarity Metric',
        'description': 'Metric for measuring similarity',
        'unit': 'dimensionless',
        'default': 'euclidean',
        'range': ['euclidean', 'cosine', 'manhattan', 'correlation'],
        'category': 'pattern_parameters',
        'discovery_type': 'pattern_recognition'
    },
    
    # Hypothesis Testing Parameters
    'hypothesis_testing': {
        'name': 'Hypothesis Testing',
        'description': 'Whether to perform hypothesis testing',
        'unit': 'dimensionless',
        'default': True,
        'range': [True, False],
        'category': 'hypothesis_parameters',
        'discovery_type': 'hypothesis_testing'
    },
    'significance_level': {
        'name': 'Significance Level',
        'description': 'Significance level for hypothesis tests',
        'unit': 'dimensionless',
        'default': 0.05,
        'range': [0.0, 1.0],
        'category': 'hypothesis_parameters',
        'discovery_type': 'hypothesis_testing'
    },
    'multiple_testing_correction': {
        'name': 'Multiple Testing Correction',
        'description': 'Method for multiple testing correction',
        'unit': 'dimensionless',
        'default': 'bonferroni',
        'range': ['bonferroni', 'holm', 'fdr', 'none'],
        'category': 'hypothesis_parameters',
        'discovery_type': 'hypothesis_testing'
    },
    
    # Validation Parameters
    'cross_validation_discovery': {
        'name': 'Cross Validation (Discovery)',
        'description': 'Whether to use cross validation for discovery',
        'unit': 'dimensionless',
        'default': True,
        'range': [True, False],
        'category': 'validation_parameters',
        'discovery_type': 'validation'
    },
    'out_of_sample_testing': {
        'name': 'Out-of-Sample Testing',
        'description': 'Whether to test on out-of-sample data',
        'unit': 'dimensionless',
        'default': True,
        'range': [True, False],
        'category': 'validation_parameters',
        'discovery_type': 'validation'
    },
    'robustness_testing': {
        'name': 'Robustness Testing',
        'description': 'Whether to test robustness of discoveries',
        'unit': 'dimensionless',
        'default': True,
        'range': [True, False],
        'category': 'validation_parameters',
        'discovery_type': 'validation'
    },
    
    # Interpretability Parameters
    'interpretability_score': {
        'name': 'Interpretability Score',
        'description': 'Weight for interpretability in discovery',
        'unit': 'dimensionless',
        'default': 1.0,
        'range': [0.0, 10.0],
        'category': 'interpretability_parameters',
        'discovery_type': 'interpretability'
    },
    'simplicity_preference': {
        'name': 'Simplicity Preference',
        'description': 'Preference for simple models',
        'unit': 'dimensionless',
        'default': 1.0,
        'range': [0.0, 10.0],
        'category': 'interpretability_parameters',
        'discovery_type': 'interpretability'
    },
    'physical_constraints': {
        'name': 'Physical Constraints',
        'description': 'Whether to enforce physical constraints',
        'unit': 'dimensionless',
        'default': True,
        'range': [True, False],
        'category': 'interpretability_parameters',
        'discovery_type': 'interpretability'
    }
}

# Equation-specific parameters for scientific discovery equations
SCIENTIFIC_DISCOVERY_EQUATION_PARAMETERS = {
    'discovery_burgers': {
        'viscosity': {
            'name': 'Viscosity (ν)',
            'description': 'Kinematic viscosity for Burgers equation discovery',
            'unit': 'm²/s',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'fluid_properties',
            'discovery_type': 'parameter_identification'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for Burgers equation discovery',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'discovery_type': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for Burgers equation discovery',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties',
            'discovery_type': 'temporal_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for Burgers equation discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        },
        'data_points': {
            'name': 'Data Points',
            'description': 'Number of data points for Burgers equation discovery',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 10000],
            'category': 'sampling_parameters',
            'discovery_type': 'data_requirements'
        }
    },
    'discovery_heat': {
        'thermal_diffusivity': {
            'name': 'Thermal Diffusivity (α)',
            'description': 'Thermal diffusivity for heat equation discovery',
            'unit': 'm²/s',
            'default': 1e-5,
            'range': [1e-6, 1e-4],
            'category': 'thermal_properties',
            'discovery_type': 'parameter_identification'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for heat equation discovery',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'discovery_type': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for heat equation discovery',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties',
            'discovery_type': 'temporal_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for heat equation discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        },
        'data_points': {
            'name': 'Data Points',
            'description': 'Number of data points for heat equation discovery',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 10000],
            'category': 'sampling_parameters',
            'discovery_type': 'data_requirements'
        }
    },
    'discovery_wave': {
        'wave_speed': {
            'name': 'Wave Speed (c)',
            'description': 'Wave propagation speed for wave equation discovery',
            'unit': 'm/s',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'wave_properties',
            'discovery_type': 'parameter_identification'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for wave equation discovery',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'discovery_type': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for wave equation discovery',
            'unit': 's',
            'default': 2.0,
            'range': [0.5, 10.0],
            'category': 'temporal_properties',
            'discovery_type': 'temporal_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for wave equation discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        },
        'data_points': {
            'name': 'Data Points',
            'description': 'Number of data points for wave equation discovery',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 10000],
            'category': 'sampling_parameters',
            'discovery_type': 'data_requirements'
        }
    },
    'discovery_shm': {
        'natural_frequency': {
            'name': 'Natural Frequency (ω₀)',
            'description': 'Natural frequency for simple harmonic motion discovery',
            'unit': 'rad/s',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'oscillatory_properties',
            'discovery_type': 'parameter_identification'
        },
        'damping_ratio': {
            'name': 'Damping Ratio (ζ)',
            'description': 'Damping ratio for simple harmonic motion discovery',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'oscillatory_properties',
            'discovery_type': 'parameter_identification'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for simple harmonic motion discovery',
            'unit': 's',
            'default': 10.0,
            'range': [1.0, 100.0],
            'category': 'temporal_properties',
            'discovery_type': 'temporal_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for simple harmonic motion discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        },
        'data_points': {
            'name': 'Data Points',
            'description': 'Number of data points for simple harmonic motion discovery',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 10000],
            'category': 'sampling_parameters',
            'discovery_type': 'data_requirements'
        }
    },
    'discovery_helmholtz': {
        'wavenumber': {
            'name': 'Wavenumber (k)',
            'description': 'Wavenumber for Helmholtz equation discovery',
            'unit': '1/m',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'wave_properties',
            'discovery_type': 'parameter_identification'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for Helmholtz equation discovery',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'discovery_type': 'spatial_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for Helmholtz equation discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        },
        'data_points': {
            'name': 'Data Points',
            'description': 'Number of data points for Helmholtz equation discovery',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 10000],
            'category': 'sampling_parameters',
            'discovery_type': 'data_requirements'
        },
        'source_strength': {
            'name': 'Source Strength',
            'description': 'Strength of source term for Helmholtz equation discovery',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'source_terms',
            'discovery_type': 'parameter_identification'
        }
    },
    'discovery_navier_stokes': {
        'reynolds_number': {
            'name': 'Reynolds Number (Re)',
            'description': 'Reynolds number for Navier-Stokes equation discovery',
            'unit': 'dimensionless',
            'default': 100.0,
            'range': [1.0, 1000.0],
            'category': 'flow_properties',
            'discovery_type': 'parameter_identification'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for Navier-Stokes equation discovery',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'discovery_type': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for Navier-Stokes equation discovery',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties',
            'discovery_type': 'temporal_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for Navier-Stokes equation discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        },
        'data_points': {
            'name': 'Data Points',
            'description': 'Number of data points for Navier-Stokes equation discovery',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 10000],
            'category': 'sampling_parameters',
            'discovery_type': 'data_requirements'
        }
    },
    'discovery_schrodinger': {
        'planck_constant': {
            'name': 'Planck Constant (ℏ)',
            'description': 'Reduced Planck constant for Schrödinger equation discovery',
            'unit': 'J·s',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'quantum_properties',
            'discovery_type': 'parameter_identification'
        },
        'mass': {
            'name': 'Particle Mass (m)',
            'description': 'Mass of particle for Schrödinger equation discovery',
            'unit': 'kg',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'quantum_properties',
            'discovery_type': 'parameter_identification'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for Schrödinger equation discovery',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'discovery_type': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for Schrödinger equation discovery',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties',
            'discovery_type': 'temporal_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for Schrödinger equation discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        }
    },
    'discovery_maxwell': {
        'permittivity': {
            'name': 'Permittivity (ε)',
            'description': 'Electric permittivity for Maxwell equations discovery',
            'unit': 'F/m',
            'default': 8.85e-12,
            'range': [1e-12, 1e-10],
            'category': 'electromagnetic_properties',
            'discovery_type': 'parameter_identification'
        },
        'permeability': {
            'name': 'Permeability (μ)',
            'description': 'Magnetic permeability for Maxwell equations discovery',
            'unit': 'H/m',
            'default': 1.26e-6,
            'range': [1e-7, 1e-5],
            'category': 'electromagnetic_properties',
            'discovery_type': 'parameter_identification'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for Maxwell equations discovery',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'discovery_type': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for Maxwell equations discovery',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties',
            'discovery_type': 'temporal_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for Maxwell equations discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        }
    },
    'discovery_heat_transfer': {
        'thermal_conductivity': {
            'name': 'Thermal Conductivity (k)',
            'description': 'Thermal conductivity for heat transfer equation discovery',
            'unit': 'W/(m·K)',
            'default': 50.0,
            'range': [1.0, 500.0],
            'category': 'thermal_properties',
            'discovery_type': 'parameter_identification'
        },
        'density': {
            'name': 'Material Density (ρ)',
            'description': 'Material density for heat transfer equation discovery',
            'unit': 'kg/m³',
            'default': 2700.0,
            'range': [100.0, 10000.0],
            'category': 'material_properties',
            'discovery_type': 'parameter_identification'
        },
        'specific_heat': {
            'name': 'Specific Heat (c)',
            'description': 'Specific heat capacity for heat transfer equation discovery',
            'unit': 'J/(kg·K)',
            'default': 900.0,
            'range': [100.0, 5000.0],
            'category': 'thermal_properties',
            'discovery_type': 'parameter_identification'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for heat transfer equation discovery',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'discovery_type': 'spatial_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for heat transfer equation discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        }
    },
    'discovery_elastic': {
        'young_modulus': {
            'name': "Young's Modulus (E)",
            'description': "Young's modulus for elastic equation discovery",
            'unit': 'Pa',
            'default': 200e9,
            'range': [1e9, 1000e9],
            'category': 'material_properties',
            'discovery_type': 'parameter_identification'
        },
        'poisson_ratio': {
            'name': 'Poisson Ratio (ν)',
            'description': 'Poisson ratio for elastic equation discovery',
            'unit': 'dimensionless',
            'default': 0.3,
            'range': [0.0, 0.5],
            'category': 'material_properties',
            'discovery_type': 'parameter_identification'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for elastic equation discovery',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'discovery_type': 'spatial_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for elastic equation discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        },
        'applied_force': {
            'name': 'Applied Force',
            'description': 'Applied force for elastic equation discovery',
            'unit': 'N',
            'default': 1000.0,
            'range': [100.0, 10000.0],
            'category': 'boundary_conditions',
            'discovery_type': 'parameter_identification'
        }
    },
    'discovery_phase_field': {
        'mobility': {
            'name': 'Phase Field Mobility (M)',
            'description': 'Mobility parameter for phase field equation discovery',
            'unit': 'm²/(J·s)',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'material_properties',
            'discovery_type': 'parameter_identification'
        },
        'interface_thickness': {
            'name': 'Interface Thickness (ε)',
            'description': 'Interface thickness parameter for phase field equation discovery',
            'unit': 'm',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'material_properties',
            'discovery_type': 'parameter_identification'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for phase field equation discovery',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'discovery_type': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for phase field equation discovery',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties',
            'discovery_type': 'temporal_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for phase field equation discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        }
    },
    'discovery_reaction_diffusion': {
        'diffusion_coefficient': {
            'name': 'Diffusion Coefficient (D)',
            'description': 'Diffusion coefficient for reaction-diffusion equation discovery',
            'unit': 'm²/s',
            'default': 1e-9,
            'range': [1e-10, 1e-8],
            'category': 'transport_properties',
            'discovery_type': 'parameter_identification'
        },
        'reaction_rate': {
            'name': 'Reaction Rate (k)',
            'description': 'Reaction rate constant for reaction-diffusion equation discovery',
            'unit': '1/s',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'reaction_properties',
            'discovery_type': 'parameter_identification'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for reaction-diffusion equation discovery',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'discovery_type': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for reaction-diffusion equation discovery',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties',
            'discovery_type': 'temporal_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for reaction-diffusion equation discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        }
    },
    'discovery_poroelasticity': {
        'permeability': {
            'name': 'Permeability (k)',
            'description': 'Permeability for poroelasticity equation discovery',
            'unit': 'm²',
            'default': 1e-12,
            'range': [1e-15, 1e-9],
            'category': 'porous_media_properties',
            'discovery_type': 'parameter_identification'
        },
        'porosity': {
            'name': 'Porosity (φ)',
            'description': 'Porosity for poroelasticity equation discovery',
            'unit': 'dimensionless',
            'default': 0.2,
            'range': [0.01, 0.5],
            'category': 'porous_media_properties',
            'discovery_type': 'parameter_identification'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for poroelasticity equation discovery',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'discovery_type': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for poroelasticity equation discovery',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties',
            'discovery_type': 'temporal_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for poroelasticity equation discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        }
    },
    'discovery_viscoelasticity': {
        'elastic_modulus': {
            'name': 'Elastic Modulus (E)',
            'description': 'Elastic modulus for viscoelasticity equation discovery',
            'unit': 'Pa',
            'default': 1e9,
            'range': [1e8, 1e10],
            'category': 'material_properties',
            'discovery_type': 'parameter_identification'
        },
        'viscosity': {
            'name': 'Viscosity (η)',
            'description': 'Viscosity for viscoelasticity equation discovery',
            'unit': 'Pa·s',
            'default': 1e6,
            'range': [1e5, 1e7],
            'category': 'material_properties',
            'discovery_type': 'parameter_identification'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for viscoelasticity equation discovery',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'discovery_type': 'spatial_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for viscoelasticity equation discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        },
        'relaxation_time': {
            'name': 'Relaxation Time (τ)',
            'description': 'Relaxation time for viscoelasticity equation discovery',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'material_properties',
            'discovery_type': 'parameter_identification'
        }
    },
    'discovery_radiative_transfer': {
        'absorption_coefficient': {
            'name': 'Absorption Coefficient (μa)',
            'description': 'Absorption coefficient for radiative transfer equation discovery',
            'unit': '1/m',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'optical_properties',
            'discovery_type': 'parameter_identification'
        },
        'scattering_coefficient': {
            'name': 'Scattering Coefficient (μs)',
            'description': 'Scattering coefficient for radiative transfer equation discovery',
            'unit': '1/m',
            'default': 0.1,
            'range': [0.01, 1.0],
            'category': 'optical_properties',
            'discovery_type': 'parameter_identification'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for radiative transfer equation discovery',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'discovery_type': 'spatial_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for radiative transfer equation discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        },
        'source_intensity': {
            'name': 'Source Intensity (I₀)',
            'description': 'Source intensity for radiative transfer equation discovery',
            'unit': 'W/m²',
            'default': 1000.0,
            'range': [100.0, 10000.0],
            'category': 'source_terms',
            'discovery_type': 'parameter_identification'
        }
    },
    'discovery_shallow_water': {
        'gravity': {
            'name': 'Gravitational Acceleration (g)',
            'description': 'Gravitational acceleration for shallow water equation discovery',
            'unit': 'm/s²',
            'default': 9.81,
            'range': [1.0, 20.0],
            'category': 'gravitational_properties',
            'discovery_type': 'parameter_identification'
        },
        'water_depth': {
            'name': 'Water Depth (h)',
            'description': 'Water depth for shallow water equation discovery',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'flow_properties',
            'discovery_type': 'parameter_identification'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for shallow water equation discovery',
            'unit': 'm',
            'default': 100.0,
            'range': [10.0, 1000.0],
            'category': 'domain_properties',
            'discovery_type': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for shallow water equation discovery',
            'unit': 's',
            'default': 10.0,
            'range': [1.0, 100.0],
            'category': 'temporal_properties',
            'discovery_type': 'temporal_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for shallow water equation discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        }
    },
    'discovery_magnetohydrodynamics': {
        'magnetic_field': {
            'name': 'Magnetic Field (B)',
            'description': 'Magnetic field strength for magnetohydrodynamics equation discovery',
            'unit': 'T',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'electromagnetic_properties',
            'discovery_type': 'parameter_identification'
        },
        'plasma_density': {
            'name': 'Plasma Density (ρ)',
            'description': 'Plasma density for magnetohydrodynamics equation discovery',
            'unit': '1/m³',
            'default': 1e19,
            'range': [1e18, 1e20],
            'category': 'plasma_properties',
            'discovery_type': 'parameter_identification'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for magnetohydrodynamics equation discovery',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'discovery_type': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for magnetohydrodynamics equation discovery',
            'unit': 's',
            'default': 1e-6,
            'range': [1e-7, 1e-5],
            'category': 'temporal_properties',
            'discovery_type': 'temporal_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for magnetohydrodynamics equation discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        }
    },
    'discovery_thermoelasticity': {
        'thermal_expansion': {
            'name': 'Thermal Expansion (α)',
            'description': 'Thermal expansion coefficient for thermoelasticity equation discovery',
            'unit': '1/K',
            'default': 2.3e-5,
            'range': [1e-6, 1e-4],
            'category': 'thermal_properties',
            'discovery_type': 'parameter_identification'
        },
        'thermal_conductivity': {
            'name': 'Thermal Conductivity (k)',
            'description': 'Thermal conductivity for thermoelasticity equation discovery',
            'unit': 'W/(m·K)',
            'default': 50.0,
            'range': [1.0, 500.0],
            'category': 'thermal_properties',
            'discovery_type': 'parameter_identification'
        },
        'elastic_modulus': {
            'name': 'Elastic Modulus (E)',
            'description': 'Elastic modulus for thermoelasticity equation discovery',
            'unit': 'Pa',
            'default': 200e9,
            'range': [1e9, 1000e9],
            'category': 'material_properties',
            'discovery_type': 'parameter_identification'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for thermoelasticity equation discovery',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'discovery_type': 'spatial_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for thermoelasticity equation discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        }
    },
    'discovery_advection_diffusion': {
        'velocity': {
            'name': 'Flow Velocity (v)',
            'description': 'Flow velocity for advection-diffusion equation discovery',
            'unit': 'm/s',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'flow_properties',
            'discovery_type': 'parameter_identification'
        },
        'diffusion_coefficient': {
            'name': 'Diffusion Coefficient (D)',
            'description': 'Diffusion coefficient for advection-diffusion equation discovery',
            'unit': 'm²/s',
            'default': 1e-9,
            'range': [1e-10, 1e-8],
            'category': 'transport_properties',
            'discovery_type': 'parameter_identification'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for advection-diffusion equation discovery',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'discovery_type': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for advection-diffusion equation discovery',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties',
            'discovery_type': 'temporal_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for advection-diffusion equation discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        }
    },
    'discovery_elastic_wave': {
        'p_wave_speed': {
            'name': 'P-Wave Speed (cp)',
            'description': 'P-wave speed for elastic wave equation discovery',
            'unit': 'm/s',
            'default': 5000.0,
            'range': [1000.0, 10000.0],
            'category': 'wave_properties',
            'discovery_type': 'parameter_identification'
        },
        's_wave_speed': {
            'name': 'S-Wave Speed (cs)',
            'description': 'S-wave speed for elastic wave equation discovery',
            'unit': 'm/s',
            'default': 3000.0,
            'range': [500.0, 6000.0],
            'category': 'wave_properties',
            'discovery_type': 'parameter_identification'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for elastic wave equation discovery',
            'unit': 'm',
            'default': 1000.0,
            'range': [100.0, 10000.0],
            'category': 'domain_properties',
            'discovery_type': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for elastic wave equation discovery',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties',
            'discovery_type': 'temporal_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for elastic wave equation discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        }
    },
    'discovery_fluid_structure_interaction': {
        'fluid_density': {
            'name': 'Fluid Density (ρf)',
            'description': 'Fluid density for fluid-structure interaction equation discovery',
            'unit': 'kg/m³',
            'default': 1000.0,
            'range': [100.0, 2000.0],
            'category': 'fluid_properties',
            'discovery_type': 'parameter_identification'
        },
        'fluid_viscosity': {
            'name': 'Fluid Viscosity (μf)',
            'description': 'Fluid viscosity for fluid-structure interaction equation discovery',
            'unit': 'Pa·s',
            'default': 1e-3,
            'range': [1e-4, 1e-2],
            'category': 'fluid_properties',
            'discovery_type': 'parameter_identification'
        },
        'structure_modulus': {
            'name': 'Structure Modulus (Es)',
            'description': 'Structure elastic modulus for fluid-structure interaction equation discovery',
            'unit': 'Pa',
            'default': 200e9,
            'range': [1e9, 1000e9],
            'category': 'material_properties',
            'discovery_type': 'parameter_identification'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for fluid-structure interaction equation discovery',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'discovery_type': 'spatial_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for fluid-structure interaction equation discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        }
    },
    'discovery_electromagnetic_thermal': {
        'electrical_conductivity': {
            'name': 'Electrical Conductivity (σ)',
            'description': 'Electrical conductivity for electromagnetic-thermal equation discovery',
            'unit': 'S/m',
            'default': 1e7,
            'range': [1e6, 1e8],
            'category': 'electrical_properties',
            'discovery_type': 'parameter_identification'
        },
        'thermal_conductivity': {
            'name': 'Thermal Conductivity (k)',
            'description': 'Thermal conductivity for electromagnetic-thermal equation discovery',
            'unit': 'W/(m·K)',
            'default': 50.0,
            'range': [1.0, 500.0],
            'category': 'thermal_properties',
            'discovery_type': 'parameter_identification'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for electromagnetic-thermal equation discovery',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'discovery_type': 'spatial_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for electromagnetic-thermal equation discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        },
        'applied_current': {
            'name': 'Applied Current (I)',
            'description': 'Applied current for electromagnetic-thermal equation discovery',
            'unit': 'A',
            'default': 100.0,
            'range': [10.0, 1000.0],
            'category': 'boundary_conditions',
            'discovery_type': 'parameter_identification'
        }
    },
    'discovery_biomechanical_transport': {
        'tissue_modulus': {
            'name': 'Tissue Modulus (Et)',
            'description': 'Tissue elastic modulus for biomechanical transport equation discovery',
            'unit': 'Pa',
            'default': 1e6,
            'range': [1e5, 1e7],
            'category': 'biological_properties',
            'discovery_type': 'parameter_identification'
        },
        'diffusion_coefficient': {
            'name': 'Diffusion Coefficient (D)',
            'description': 'Diffusion coefficient for biomechanical transport equation discovery',
            'unit': 'm²/s',
            'default': 1e-9,
            'range': [1e-10, 1e-8],
            'category': 'transport_properties',
            'discovery_type': 'parameter_identification'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for biomechanical transport equation discovery',
            'unit': 'm',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'domain_properties',
            'discovery_type': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for biomechanical transport equation discovery',
            'unit': 's',
            'default': 3600.0,
            'range': [100.0, 10000.0],
            'category': 'temporal_properties',
            'discovery_type': 'temporal_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for biomechanical transport equation discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        }
    },
    'discovery_geophysical_flow': {
        'coriolis_parameter': {
            'name': 'Coriolis Parameter (f)',
            'description': 'Coriolis parameter for geophysical flow equation discovery',
            'unit': '1/s',
            'default': 1e-4,
            'range': [1e-5, 1e-3],
            'category': 'geophysical_properties',
            'discovery_type': 'parameter_identification'
        },
        'gravity': {
            'name': 'Gravitational Acceleration (g)',
            'description': 'Gravitational acceleration for geophysical flow equation discovery',
            'unit': 'm/s²',
            'default': 9.81,
            'range': [1.0, 20.0],
            'category': 'gravitational_properties',
            'discovery_type': 'parameter_identification'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for geophysical flow equation discovery',
            'unit': 'm',
            'default': 1000000.0,
            'range': [100000.0, 10000000.0],
            'category': 'domain_properties',
            'discovery_type': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for geophysical flow equation discovery',
            'unit': 's',
            'default': 86400.0,
            'range': [3600.0, 604800.0],
            'category': 'temporal_properties',
            'discovery_type': 'temporal_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for geophysical flow equation discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        }
    },
    'discovery_atmospheric_oceanic': {
        'atmospheric_pressure': {
            'name': 'Atmospheric Pressure (P)',
            'description': 'Atmospheric pressure for atmospheric-oceanic equation discovery',
            'unit': 'Pa',
            'default': 101325.0,
            'range': [50000.0, 200000.0],
            'category': 'atmospheric_properties',
            'discovery_type': 'parameter_identification'
        },
        'ocean_depth': {
            'name': 'Ocean Depth (h)',
            'description': 'Ocean depth for atmospheric-oceanic equation discovery',
            'unit': 'm',
            'default': 1000.0,
            'range': [100.0, 10000.0],
            'category': 'oceanic_properties',
            'discovery_type': 'parameter_identification'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for atmospheric-oceanic equation discovery',
            'unit': 'm',
            'default': 1000000.0,
            'range': [100000.0, 10000000.0],
            'category': 'domain_properties',
            'discovery_type': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for atmospheric-oceanic equation discovery',
            'unit': 's',
            'default': 86400.0,
            'range': [3600.0, 604800.0],
            'category': 'temporal_properties',
            'discovery_type': 'temporal_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for atmospheric-oceanic equation discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        }
    },
    'discovery_nuclear_thermal': {
        'fission_rate': {
            'name': 'Fission Rate (Rf)',
            'description': 'Fission rate for nuclear-thermal equation discovery',
            'unit': '1/(m³·s)',
            'default': 1e18,
            'range': [1e17, 1e19],
            'category': 'nuclear_properties',
            'discovery_type': 'parameter_identification'
        },
        'thermal_conductivity': {
            'name': 'Thermal Conductivity (k)',
            'description': 'Thermal conductivity for nuclear-thermal equation discovery',
            'unit': 'W/(m·K)',
            'default': 50.0,
            'range': [1.0, 500.0],
            'category': 'thermal_properties',
            'discovery_type': 'parameter_identification'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for nuclear-thermal equation discovery',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'discovery_type': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for nuclear-thermal equation discovery',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties',
            'discovery_type': 'temporal_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for nuclear-thermal equation discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        }
    },
    'discovery_quantum_mechanical': {
        'planck_constant': {
            'name': 'Planck Constant (ℏ)',
            'description': 'Reduced Planck constant for quantum mechanical equation discovery',
            'unit': 'J·s',
            'default': 1.055e-34,
            'range': [1e-35, 1e-33],
            'category': 'quantum_properties',
            'discovery_type': 'parameter_identification'
        },
        'mass': {
            'name': 'Particle Mass (m)',
            'description': 'Particle mass for quantum mechanical equation discovery',
            'unit': 'kg',
            'default': 9.11e-31,
            'range': [1e-32, 1e-29],
            'category': 'quantum_properties',
            'discovery_type': 'parameter_identification'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for quantum mechanical equation discovery',
            'unit': 'm',
            'default': 1e-9,
            'range': [1e-10, 1e-8],
            'category': 'domain_properties',
            'discovery_type': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for quantum mechanical equation discovery',
            'unit': 's',
            'default': 1e-12,
            'range': [1e-13, 1e-11],
            'category': 'temporal_properties',
            'discovery_type': 'temporal_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for quantum mechanical equation discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        }
    },
    'discovery_phase_field_allen_cahn': {
        'mobility': {
            'name': 'Phase Field Mobility (M)',
            'description': 'Mobility parameter for Allen-Cahn equation discovery',
            'unit': 'm²/(J·s)',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'material_properties',
            'discovery_type': 'parameter_identification'
        },
        'interface_thickness': {
            'name': 'Interface Thickness (ε)',
            'description': 'Interface thickness parameter for Allen-Cahn equation discovery',
            'unit': 'm',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'material_properties',
            'discovery_type': 'parameter_identification'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for Allen-Cahn equation discovery',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'discovery_type': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for Allen-Cahn equation discovery',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties',
            'discovery_type': 'temporal_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for Allen-Cahn equation discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        }
    },
    'discovery_phase_field_cahn_hilliard': {
        'mobility': {
            'name': 'Phase Field Mobility (M)',
            'description': 'Mobility parameter for Cahn-Hilliard equation discovery',
            'unit': 'm²/(J·s)',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'material_properties',
            'discovery_type': 'parameter_identification'
        },
        'interface_thickness': {
            'name': 'Interface Thickness (ε)',
            'description': 'Interface thickness parameter for Cahn-Hilliard equation discovery',
            'unit': 'm',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'material_properties',
            'discovery_type': 'parameter_identification'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for Cahn-Hilliard equation discovery',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'discovery_type': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for Cahn-Hilliard equation discovery',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties',
            'discovery_type': 'temporal_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for Cahn-Hilliard equation discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        }
    },
    'discovery_solidification_stefan': {
        'thermal_diffusivity': {
            'name': 'Thermal Diffusivity (α)',
            'description': 'Thermal diffusivity for Stefan solidification equation discovery',
            'unit': 'm²/s',
            'default': 1e-5,
            'range': [1e-6, 1e-4],
            'category': 'thermal_properties',
            'discovery_type': 'parameter_identification'
        },
        'latent_heat': {
            'name': 'Latent Heat (L)',
            'description': 'Latent heat for Stefan solidification equation discovery',
            'unit': 'J/kg',
            'default': 3.34e5,
            'range': [1e5, 1e6],
            'category': 'thermal_properties',
            'discovery_type': 'parameter_identification'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for Stefan solidification equation discovery',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties',
            'discovery_type': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for Stefan solidification equation discovery',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties',
            'discovery_type': 'temporal_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for Stefan solidification equation discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        }
    },
    'discovery_grain_growth': {
        'mobility': {
            'name': 'Grain Growth Mobility (M)',
            'description': 'Mobility parameter for grain growth equation discovery',
            'unit': 'm²/(J·s)',
            'default': 1e-12,
            'range': [1e-13, 1e-11],
            'category': 'material_properties',
            'discovery_type': 'parameter_identification'
        },
        'grain_boundary_energy': {
            'name': 'Grain Boundary Energy (γ)',
            'description': 'Grain boundary energy for grain growth equation discovery',
            'unit': 'J/m²',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'material_properties',
            'discovery_type': 'parameter_identification'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for grain growth equation discovery',
            'unit': 'm',
            'default': 1e-3,
            'range': [1e-4, 1e-2],
            'category': 'domain_properties',
            'discovery_type': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for grain growth equation discovery',
            'unit': 's',
            'default': 3600.0,
            'range': [100.0, 10000.0],
            'category': 'temporal_properties',
            'discovery_type': 'temporal_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for grain growth equation discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        }
    },
    'discovery_sintering': {
        'diffusion_coefficient': {
            'name': 'Diffusion Coefficient (D)',
            'description': 'Diffusion coefficient for sintering equation discovery',
            'unit': 'm²/s',
            'default': 1e-15,
            'range': [1e-16, 1e-14],
            'category': 'transport_properties',
            'discovery_type': 'parameter_identification'
        },
        'surface_energy': {
            'name': 'Surface Energy (γ)',
            'description': 'Surface energy for sintering equation discovery',
            'unit': 'J/m²',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'material_properties',
            'discovery_type': 'parameter_identification'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for sintering equation discovery',
            'unit': 'm',
            'default': 1e-3,
            'range': [1e-4, 1e-2],
            'category': 'domain_properties',
            'discovery_type': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for sintering equation discovery',
            'unit': 's',
            'default': 3600.0,
            'range': [100.0, 10000.0],
            'category': 'temporal_properties',
            'discovery_type': 'temporal_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for sintering equation discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        }
    },
    'discovery_laser_heat_source': {
        'laser_power': {
            'name': 'Laser Power (P)',
            'description': 'Laser power for laser heat source equation discovery',
            'unit': 'W',
            'default': 1000.0,
            'range': [100.0, 10000.0],
            'category': 'source_terms',
            'discovery_type': 'parameter_identification'
        },
        'beam_radius': {
            'name': 'Beam Radius (r)',
            'description': 'Laser beam radius for laser heat source equation discovery',
            'unit': 'm',
            'default': 0.001,
            'range': [1e-4, 1e-2],
            'category': 'source_terms',
            'discovery_type': 'parameter_identification'
        },
        'absorption_coefficient': {
            'name': 'Absorption Coefficient (α)',
            'description': 'Absorption coefficient for laser heat source equation discovery',
            'unit': 'dimensionless',
            'default': 0.8,
            'range': [0.1, 1.0],
            'category': 'optical_properties',
            'discovery_type': 'parameter_identification'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for laser heat source equation discovery',
            'unit': 'm',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'domain_properties',
            'discovery_type': 'spatial_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for laser heat source equation discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        }
    },
    'discovery_melt_pool_dynamics': {
        'surface_tension': {
            'name': 'Surface Tension (σ)',
            'description': 'Surface tension for melt pool dynamics equation discovery',
            'unit': 'N/m',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'fluid_properties',
            'discovery_type': 'parameter_identification'
        },
        'viscosity': {
            'name': 'Viscosity (μ)',
            'description': 'Viscosity for melt pool dynamics equation discovery',
            'unit': 'Pa·s',
            'default': 1e-3,
            'range': [1e-4, 1e-2],
            'category': 'fluid_properties',
            'discovery_type': 'parameter_identification'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for melt pool dynamics equation discovery',
            'unit': 'm',
            'default': 0.001,
            'range': [1e-4, 1e-2],
            'category': 'domain_properties',
            'discovery_type': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for melt pool dynamics equation discovery',
            'unit': 's',
            'default': 0.001,
            'range': [1e-4, 1e-2],
            'category': 'temporal_properties',
            'discovery_type': 'temporal_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for melt pool dynamics equation discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        }
    },
    'discovery_crystal_plasticity': {
        'critical_resolved_shear_stress': {
            'name': 'Critical Resolved Shear Stress (τc)',
            'description': 'Critical resolved shear stress for crystal plasticity equation discovery',
            'unit': 'Pa',
            'default': 1e6,
            'range': [1e5, 1e7],
            'category': 'material_properties',
            'discovery_type': 'parameter_identification'
        },
        'shear_modulus': {
            'name': 'Shear Modulus (G)',
            'description': 'Shear modulus for crystal plasticity equation discovery',
            'unit': 'Pa',
            'default': 80e9,
            'range': [10e9, 500e9],
            'category': 'material_properties',
            'discovery_type': 'parameter_identification'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for crystal plasticity equation discovery',
            'unit': 'm',
            'default': 1e-5,
            'range': [1e-6, 1e-4],
            'category': 'domain_properties',
            'discovery_type': 'spatial_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for crystal plasticity equation discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        },
        'applied_strain_rate': {
            'name': 'Applied Strain Rate (ε̇)',
            'description': 'Applied strain rate for crystal plasticity equation discovery',
            'unit': '1/s',
            'default': 1e-3,
            'range': [1e-4, 1e-2],
            'category': 'boundary_conditions',
            'discovery_type': 'parameter_identification'
        }
    },
    'discovery_diffusion_solids': {
        'diffusion_coefficient': {
            'name': 'Diffusion Coefficient (D)',
            'description': 'Diffusion coefficient for solid diffusion equation discovery',
            'unit': 'm²/s',
            'default': 1e-15,
            'range': [1e-16, 1e-14],
            'category': 'transport_properties',
            'discovery_type': 'parameter_identification'
        },
        'activation_energy': {
            'name': 'Activation Energy (Ea)',
            'description': 'Activation energy for solid diffusion equation discovery',
            'unit': 'J/mol',
            'default': 1e5,
            'range': [1e4, 1e6],
            'category': 'material_properties',
            'discovery_type': 'parameter_identification'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for solid diffusion equation discovery',
            'unit': 'm',
            'default': 1e-3,
            'range': [1e-4, 1e-2],
            'category': 'domain_properties',
            'discovery_type': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for solid diffusion equation discovery',
            'unit': 's',
            'default': 3600.0,
            'range': [100.0, 10000.0],
            'category': 'temporal_properties',
            'discovery_type': 'temporal_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for solid diffusion equation discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        }
    },
    'discovery_precipitation_nucleation': {
        'nucleation_rate': {
            'name': 'Nucleation Rate (J)',
            'description': 'Nucleation rate for precipitation equation discovery',
            'unit': '1/(m³·s)',
            'default': 1e12,
            'range': [1e11, 1e13],
            'category': 'nucleation_properties',
            'discovery_type': 'parameter_identification'
        },
        'critical_radius': {
            'name': 'Critical Radius (rc)',
            'description': 'Critical radius for precipitation equation discovery',
            'unit': 'm',
            'default': 1e-9,
            'range': [1e-10, 1e-8],
            'category': 'nucleation_properties',
            'discovery_type': 'parameter_identification'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for precipitation equation discovery',
            'unit': 'm',
            'default': 1e-6,
            'range': [1e-7, 1e-5],
            'category': 'domain_properties',
            'discovery_type': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for precipitation equation discovery',
            'unit': 's',
            'default': 3600.0,
            'range': [100.0, 10000.0],
            'category': 'temporal_properties',
            'discovery_type': 'temporal_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for precipitation equation discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        }
    },
    'discovery_residual_stress': {
        'thermal_expansion': {
            'name': 'Thermal Expansion (α)',
            'description': 'Thermal expansion coefficient for residual stress equation discovery',
            'unit': '1/K',
            'default': 2.3e-5,
            'range': [1e-6, 1e-4],
            'category': 'thermal_properties',
            'discovery_type': 'parameter_identification'
        },
        'elastic_modulus': {
            'name': 'Elastic Modulus (E)',
            'description': 'Elastic modulus for residual stress equation discovery',
            'unit': 'Pa',
            'default': 200e9,
            'range': [1e9, 1000e9],
            'category': 'material_properties',
            'discovery_type': 'parameter_identification'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for residual stress equation discovery',
            'unit': 'm',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'domain_properties',
            'discovery_type': 'spatial_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for residual stress equation discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        },
        'temperature_gradient': {
            'name': 'Temperature Gradient (∇T)',
            'description': 'Temperature gradient for residual stress equation discovery',
            'unit': 'K/m',
            'default': 100.0,
            'range': [10.0, 1000.0],
            'category': 'thermal_properties',
            'discovery_type': 'parameter_identification'
        }
    },
    'discovery_microstructure_evolution': {
        'phase_field_mobility': {
            'name': 'Phase Field Mobility (M)',
            'description': 'Phase field mobility for microstructure evolution equation discovery',
            'unit': 'm²/(J·s)',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'material_properties',
            'discovery_type': 'parameter_identification'
        },
        'interface_energy': {
            'name': 'Interface Energy (γ)',
            'description': 'Interface energy for microstructure evolution equation discovery',
            'unit': 'J/m²',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'material_properties',
            'discovery_type': 'parameter_identification'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for microstructure evolution equation discovery',
            'unit': 'm',
            'default': 1e-5,
            'range': [1e-6, 1e-4],
            'category': 'domain_properties',
            'discovery_type': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for microstructure evolution equation discovery',
            'unit': 's',
            'default': 3600.0,
            'range': [100.0, 10000.0],
            'category': 'temporal_properties',
            'discovery_type': 'temporal_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for microstructure evolution equation discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        }
    },
    'discovery_additive_manufacturing': {
        'laser_power': {
            'name': 'Laser Power (P)',
            'description': 'Laser power for additive manufacturing equation discovery',
            'unit': 'W',
            'default': 1000.0,
            'range': [100.0, 10000.0],
            'category': 'source_terms',
            'discovery_type': 'parameter_identification'
        },
        'scan_speed': {
            'name': 'Scan Speed (v)',
            'description': 'Scan speed for additive manufacturing equation discovery',
            'unit': 'm/s',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'source_terms',
            'discovery_type': 'parameter_identification'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for additive manufacturing equation discovery',
            'unit': 'm',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'domain_properties',
            'discovery_type': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for additive manufacturing equation discovery',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties',
            'discovery_type': 'temporal_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for additive manufacturing equation discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        }
    },
    'discovery_material_processing': {
        'heating_rate': {
            'name': 'Heating Rate (Ṫ)',
            'description': 'Heating rate for material processing equation discovery',
            'unit': 'K/s',
            'default': 10.0,
            'range': [1.0, 100.0],
            'category': 'thermal_properties',
            'discovery_type': 'parameter_identification'
        },
        'cooling_rate': {
            'name': 'Cooling Rate (Ṫ)',
            'description': 'Cooling rate for material processing equation discovery',
            'unit': 'K/s',
            'default': 5.0,
            'range': [0.5, 50.0],
            'category': 'thermal_properties',
            'discovery_type': 'parameter_identification'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length for material processing equation discovery',
            'unit': 'm',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'domain_properties',
            'discovery_type': 'spatial_scaling'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration for material processing equation discovery',
            'unit': 's',
            'default': 3600.0,
            'range': [100.0, 10000.0],
            'category': 'temporal_properties',
            'discovery_type': 'temporal_scaling'
        },
        'noise_level': {
            'name': 'Noise Level',
            'description': 'Level of noise in data for material processing equation discovery',
            'unit': 'dimensionless',
            'default': 0.01,
            'range': [0.001, 0.1],
            'category': 'data_quality',
            'discovery_type': 'robustness_testing'
        }
    }
} 