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
        'viscosity': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'm²/s'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'time_duration': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 's'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'},
        'data_points': {'default': 1000, 'range': [100, 10000], 'unit': 'dimensionless'}
    },
    'discovery_heat': {
        'thermal_diffusivity': {'default': 1e-5, 'range': [1e-6, 1e-4], 'unit': 'm²/s'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'time_duration': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 's'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'},
        'data_points': {'default': 1000, 'range': [100, 10000], 'unit': 'dimensionless'}
    },
    'discovery_wave': {
        'wave_speed': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm/s'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'time_duration': {'default': 2.0, 'range': [0.5, 10.0], 'unit': 's'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'},
        'data_points': {'default': 1000, 'range': [100, 10000], 'unit': 'dimensionless'}
    },
    'discovery_shm': {
        'natural_frequency': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'rad/s'},
        'damping_ratio': {'default': 0.1, 'range': [0.0, 1.0], 'unit': 'dimensionless'},
        'time_duration': {'default': 10.0, 'range': [1.0, 100.0], 'unit': 's'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'},
        'data_points': {'default': 1000, 'range': [100, 10000], 'unit': 'dimensionless'}
    },
    'discovery_helmholtz': {
        'wavenumber': {'default': 1.0, 'range': [0.1, 10.0], 'unit': '1/m'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'},
        'data_points': {'default': 1000, 'range': [100, 10000], 'unit': 'dimensionless'},
        'source_strength': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'dimensionless'}
    },
    'discovery_navier_stokes': {
        'reynolds_number': {'default': 100.0, 'range': [1.0, 1000.0], 'unit': 'dimensionless'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'time_duration': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 's'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'},
        'data_points': {'default': 1000, 'range': [100, 10000], 'unit': 'dimensionless'}
    },
    'discovery_schrodinger': {
        'planck_constant': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'J·s'},
        'mass': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'kg'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'time_duration': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 's'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'}
    },
    'discovery_maxwell': {
        'permittivity': {'default': 8.85e-12, 'range': [1e-12, 1e-10], 'unit': 'F/m'},
        'permeability': {'default': 1.26e-6, 'range': [1e-7, 1e-5], 'unit': 'H/m'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'time_duration': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 's'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'}
    },
    'discovery_heat_transfer': {
        'thermal_conductivity': {'default': 50.0, 'range': [1.0, 500.0], 'unit': 'W/(m·K)'},
        'density': {'default': 2700.0, 'range': [100.0, 10000.0], 'unit': 'kg/m³'},
        'specific_heat': {'default': 900.0, 'range': [100.0, 5000.0], 'unit': 'J/(kg·K)'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'}
    },
    'discovery_elastic': {
        'young_modulus': {'default': 200e9, 'range': [1e9, 1000e9], 'unit': 'Pa'},
        'poisson_ratio': {'default': 0.3, 'range': [0.0, 0.5], 'unit': 'dimensionless'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'},
        'applied_force': {'default': 1000.0, 'range': [100.0, 10000.0], 'unit': 'N'}
    },
    'discovery_phase_field': {
        'mobility': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm²/(J·s)'},
        'interface_thickness': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'm'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'time_duration': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 's'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'}
    },
    'discovery_reaction_diffusion': {
        'diffusion_coefficient': {'default': 1e-9, 'range': [1e-10, 1e-8], 'unit': 'm²/s'},
        'reaction_rate': {'default': 1.0, 'range': [0.1, 10.0], 'unit': '1/s'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'time_duration': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 's'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'}
    },
    'discovery_poroelasticity': {
        'permeability': {'default': 1e-12, 'range': [1e-15, 1e-9], 'unit': 'm²'},
        'porosity': {'default': 0.2, 'range': [0.01, 0.5], 'unit': 'dimensionless'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'time_duration': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 's'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'}
    },
    'discovery_viscoelasticity': {
        'elastic_modulus': {'default': 1e9, 'range': [1e8, 1e10], 'unit': 'Pa'},
        'viscosity': {'default': 1e6, 'range': [1e5, 1e7], 'unit': 'Pa·s'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'},
        'relaxation_time': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 's'}
    },
    'discovery_radiative_transfer': {
        'absorption_coefficient': {'default': 1.0, 'range': [0.1, 10.0], 'unit': '1/m'},
        'scattering_coefficient': {'default': 0.1, 'range': [0.01, 1.0], 'unit': '1/m'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'},
        'source_intensity': {'default': 1000.0, 'range': [100.0, 10000.0], 'unit': 'W/m²'}
    },
    'discovery_shallow_water': {
        'gravity': {'default': 9.81, 'range': [1.0, 20.0], 'unit': 'm/s²'},
        'water_depth': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'domain_size': {'default': 100.0, 'range': [10.0, 1000.0], 'unit': 'm'},
        'time_duration': {'default': 10.0, 'range': [1.0, 100.0], 'unit': 's'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'}
    },
    'discovery_magnetohydrodynamics': {
        'magnetic_field': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'T'},
        'plasma_density': {'default': 1e19, 'range': [1e18, 1e20], 'unit': '1/m³'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'time_duration': {'default': 1e-6, 'range': [1e-7, 1e-5], 'unit': 's'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'}
    },
    'discovery_thermoelasticity': {
        'thermal_expansion': {'default': 2.3e-5, 'range': [1e-6, 1e-4], 'unit': '1/K'},
        'thermal_conductivity': {'default': 50.0, 'range': [1.0, 500.0], 'unit': 'W/(m·K)'},
        'elastic_modulus': {'default': 200e9, 'range': [1e9, 1000e9], 'unit': 'Pa'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'}
    },
    'discovery_advection_diffusion': {
        'velocity': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm/s'},
        'diffusion_coefficient': {'default': 1e-9, 'range': [1e-10, 1e-8], 'unit': 'm²/s'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'time_duration': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 's'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'}
    },
    'discovery_elastic_wave': {
        'p_wave_speed': {'default': 5000.0, 'range': [1000.0, 10000.0], 'unit': 'm/s'},
        's_wave_speed': {'default': 3000.0, 'range': [500.0, 6000.0], 'unit': 'm/s'},
        'domain_size': {'default': 1000.0, 'range': [100.0, 10000.0], 'unit': 'm'},
        'time_duration': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 's'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'}
    },
    'discovery_fluid_structure_interaction': {
        'fluid_density': {'default': 1000.0, 'range': [100.0, 2000.0], 'unit': 'kg/m³'},
        'fluid_viscosity': {'default': 1e-3, 'range': [1e-4, 1e-2], 'unit': 'Pa·s'},
        'structure_modulus': {'default': 200e9, 'range': [1e9, 1000e9], 'unit': 'Pa'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'}
    },
    'discovery_electromagnetic_thermal': {
        'electrical_conductivity': {'default': 1e7, 'range': [1e6, 1e8], 'unit': 'S/m'},
        'thermal_conductivity': {'default': 50.0, 'range': [1.0, 500.0], 'unit': 'W/(m·K)'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'},
        'applied_current': {'default': 100.0, 'range': [10.0, 1000.0], 'unit': 'A'}
    },
    'discovery_biomechanical_transport': {
        'tissue_modulus': {'default': 1e6, 'range': [1e5, 1e7], 'unit': 'Pa'},
        'diffusion_coefficient': {'default': 1e-9, 'range': [1e-10, 1e-8], 'unit': 'm²/s'},
        'domain_size': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'm'},
        'time_duration': {'default': 3600.0, 'range': [100.0, 10000.0], 'unit': 's'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'}
    },
    'discovery_geophysical_flow': {
        'coriolis_parameter': {'default': 1e-4, 'range': [1e-5, 1e-3], 'unit': '1/s'},
        'gravity': {'default': 9.81, 'range': [1.0, 20.0], 'unit': 'm/s²'},
        'domain_size': {'default': 1000000.0, 'range': [100000.0, 10000000.0], 'unit': 'm'},
        'time_duration': {'default': 86400.0, 'range': [3600.0, 604800.0], 'unit': 's'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'}
    },
    'discovery_atmospheric_oceanic': {
        'atmospheric_pressure': {'default': 101325.0, 'range': [50000.0, 200000.0], 'unit': 'Pa'},
        'ocean_depth': {'default': 1000.0, 'range': [100.0, 10000.0], 'unit': 'm'},
        'domain_size': {'default': 1000000.0, 'range': [100000.0, 10000000.0], 'unit': 'm'},
        'time_duration': {'default': 86400.0, 'range': [3600.0, 604800.0], 'unit': 's'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'}
    },
    'discovery_nuclear_thermal': {
        'fission_rate': {'default': 1e18, 'range': [1e17, 1e19], 'unit': '1/(m³·s)'},
        'thermal_conductivity': {'default': 50.0, 'range': [1.0, 500.0], 'unit': 'W/(m·K)'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'time_duration': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 's'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'}
    },
    'discovery_quantum_mechanical': {
        'planck_constant': {'default': 1.055e-34, 'range': [1e-35, 1e-33], 'unit': 'J·s'},
        'mass': {'default': 9.11e-31, 'range': [1e-32, 1e-29], 'unit': 'kg'},
        'domain_size': {'default': 1e-9, 'range': [1e-10, 1e-8], 'unit': 'm'},
        'time_duration': {'default': 1e-12, 'range': [1e-13, 1e-11], 'unit': 's'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'}
    },
    'discovery_phase_field_allen_cahn': {
        'mobility': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm²/(J·s)'},
        'interface_thickness': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'm'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'time_duration': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 's'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'}
    },
    'discovery_phase_field_cahn_hilliard': {
        'mobility': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm²/(J·s)'},
        'interface_thickness': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'm'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'time_duration': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 's'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'}
    },
    'discovery_solidification_stefan': {
        'thermal_diffusivity': {'default': 1e-5, 'range': [1e-6, 1e-4], 'unit': 'm²/s'},
        'latent_heat': {'default': 3.34e5, 'range': [1e5, 1e6], 'unit': 'J/kg'},
        'domain_size': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm'},
        'time_duration': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 's'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'}
    },
    'discovery_grain_growth': {
        'mobility': {'default': 1e-12, 'range': [1e-13, 1e-11], 'unit': 'm²/(J·s)'},
        'grain_boundary_energy': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'J/m²'},
        'domain_size': {'default': 1e-3, 'range': [1e-4, 1e-2], 'unit': 'm'},
        'time_duration': {'default': 3600.0, 'range': [100.0, 10000.0], 'unit': 's'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'}
    },
    'discovery_sintering': {
        'diffusion_coefficient': {'default': 1e-15, 'range': [1e-16, 1e-14], 'unit': 'm²/s'},
        'surface_energy': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'J/m²'},
        'domain_size': {'default': 1e-3, 'range': [1e-4, 1e-2], 'unit': 'm'},
        'time_duration': {'default': 3600.0, 'range': [100.0, 10000.0], 'unit': 's'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'}
    },
    'discovery_laser_heat_source': {
        'laser_power': {'default': 1000.0, 'range': [100.0, 10000.0], 'unit': 'W'},
        'beam_radius': {'default': 0.001, 'range': [1e-4, 1e-2], 'unit': 'm'},
        'absorption_coefficient': {'default': 0.8, 'range': [0.1, 1.0], 'unit': 'dimensionless'},
        'domain_size': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'm'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'}
    },
    'discovery_melt_pool_dynamics': {
        'surface_tension': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'N/m'},
        'viscosity': {'default': 1e-3, 'range': [1e-4, 1e-2], 'unit': 'Pa·s'},
        'domain_size': {'default': 0.001, 'range': [1e-4, 1e-2], 'unit': 'm'},
        'time_duration': {'default': 0.001, 'range': [1e-4, 1e-2], 'unit': 's'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'}
    },
    'discovery_crystal_plasticity': {
        'critical_resolved_shear_stress': {'default': 1e6, 'range': [1e5, 1e7], 'unit': 'Pa'},
        'shear_modulus': {'default': 80e9, 'range': [10e9, 500e9], 'unit': 'Pa'},
        'domain_size': {'default': 1e-5, 'range': [1e-6, 1e-4], 'unit': 'm'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'},
        'applied_strain_rate': {'default': 1e-3, 'range': [1e-4, 1e-2], 'unit': '1/s'}
    },
    'discovery_diffusion_solids': {
        'diffusion_coefficient': {'default': 1e-15, 'range': [1e-16, 1e-14], 'unit': 'm²/s'},
        'activation_energy': {'default': 1e5, 'range': [1e4, 1e6], 'unit': 'J/mol'},
        'domain_size': {'default': 1e-3, 'range': [1e-4, 1e-2], 'unit': 'm'},
        'time_duration': {'default': 3600.0, 'range': [100.0, 10000.0], 'unit': 's'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'}
    },
    'discovery_precipitation_nucleation': {
        'nucleation_rate': {'default': 1e12, 'range': [1e11, 1e13], 'unit': '1/(m³·s)'},
        'critical_radius': {'default': 1e-9, 'range': [1e-10, 1e-8], 'unit': 'm'},
        'domain_size': {'default': 1e-6, 'range': [1e-7, 1e-5], 'unit': 'm'},
        'time_duration': {'default': 3600.0, 'range': [100.0, 10000.0], 'unit': 's'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'}
    },
    'discovery_residual_stress': {
        'thermal_expansion': {'default': 2.3e-5, 'range': [1e-6, 1e-4], 'unit': '1/K'},
        'elastic_modulus': {'default': 200e9, 'range': [1e9, 1000e9], 'unit': 'Pa'},
        'domain_size': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'm'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'},
        'temperature_gradient': {'default': 100.0, 'range': [10.0, 1000.0], 'unit': 'K/m'}
    },
    'discovery_microstructure_evolution': {
        'phase_field_mobility': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'm²/(J·s)'},
        'interface_energy': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 'J/m²'},
        'domain_size': {'default': 1e-5, 'range': [1e-6, 1e-4], 'unit': 'm'},
        'time_duration': {'default': 3600.0, 'range': [100.0, 10000.0], 'unit': 's'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'}
    },
    'discovery_additive_manufacturing': {
        'laser_power': {'default': 1000.0, 'range': [100.0, 10000.0], 'unit': 'W'},
        'scan_speed': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'm/s'},
        'domain_size': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'm'},
        'time_duration': {'default': 1.0, 'range': [0.1, 10.0], 'unit': 's'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'}
    },
    'discovery_material_processing': {
        'heating_rate': {'default': 10.0, 'range': [1.0, 100.0], 'unit': 'K/s'},
        'cooling_rate': {'default': 5.0, 'range': [0.5, 50.0], 'unit': 'K/s'},
        'domain_size': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'm'},
        'time_duration': {'default': 3600.0, 'range': [100.0, 10000.0], 'unit': 's'},
        'noise_level': {'default': 0.01, 'range': [0.001, 0.1], 'unit': 'dimensionless'}
    }
} 