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