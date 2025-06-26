"""
Efficiency Parameters
Parameters for optimizing computational efficiency and performance.
"""

EFFICIENCY_PARAMETERS_DICT = {
    # Computational Parameters
    'time_step': {
        'name': 'Time Step',
        'description': 'Time step for numerical integration',
        'unit': 's',
        'default': 1e-3,
        'range': [1e-6, 1e-1],
        'category': 'computational_parameters',
        'optimization_target': 'accuracy'
    },
    'spatial_discretization': {
        'name': 'Spatial Discretization',
        'description': 'Spatial discretization parameter',
        'unit': 'm',
        'default': 1e-2,
        'range': [1e-4, 1e-1],
        'category': 'computational_parameters',
        'optimization_target': 'accuracy'
    },
    'tolerance': {
        'name': 'Solver Tolerance',
        'description': 'Tolerance for iterative solvers',
        'unit': 'dimensionless',
        'default': 1e-6,
        'range': [1e-12, 1e-3],
        'category': 'computational_parameters',
        'optimization_target': 'convergence'
    },
    'max_iterations': {
        'name': 'Maximum Iterations',
        'description': 'Maximum iterations for solvers',
        'unit': 'dimensionless',
        'default': 1000,
        'range': [100, 10000],
        'category': 'computational_parameters',
        'optimization_target': 'convergence'
    },
    
    # Neural Network Parameters
    'network_depth': {
        'name': 'Network Depth',
        'description': 'Number of hidden layers',
        'unit': 'dimensionless',
        'default': 4,
        'range': [1, 20],
        'category': 'neural_network_parameters',
        'optimization_target': 'expressiveness'
    },
    'network_width': {
        'name': 'Network Width',
        'description': 'Number of neurons per layer',
        'unit': 'dimensionless',
        'default': 50,
        'range': [10, 500],
        'category': 'neural_network_parameters',
        'optimization_target': 'expressiveness'
    },
    'learning_rate': {
        'name': 'Learning Rate',
        'description': 'Learning rate for training',
        'unit': 'dimensionless',
        'default': 0.001,
        'range': [1e-6, 1e-1],
        'category': 'neural_network_parameters',
        'optimization_target': 'convergence'
    },
    'batch_size': {
        'name': 'Batch Size',
        'description': 'Batch size for training',
        'unit': 'dimensionless',
        'default': 32,
        'range': [1, 1000],
        'category': 'neural_network_parameters',
        'optimization_target': 'memory'
    },
    
    # Training Parameters
    'epochs': {
        'name': 'Training Epochs',
        'description': 'Number of training epochs',
        'unit': 'dimensionless',
        'default': 1000,
        'range': [100, 10000],
        'category': 'training_parameters',
        'optimization_target': 'accuracy'
    },
    'early_stopping_patience': {
        'name': 'Early Stopping Patience',
        'description': 'Patience for early stopping',
        'unit': 'dimensionless',
        'default': 100,
        'range': [10, 1000],
        'category': 'training_parameters',
        'optimization_target': 'efficiency'
    },
    'validation_split': {
        'name': 'Validation Split',
        'description': 'Fraction of data for validation',
        'unit': 'dimensionless',
        'default': 0.2,
        'range': [0.1, 0.5],
        'category': 'training_parameters',
        'optimization_target': 'generalization'
    },
    
    # Sampling Parameters
    'collocation_points': {
        'name': 'Collocation Points',
        'description': 'Number of collocation points',
        'unit': 'dimensionless',
        'default': 1000,
        'range': [100, 100000],
        'category': 'sampling_parameters',
        'optimization_target': 'accuracy'
    },
    'boundary_points': {
        'name': 'Boundary Points',
        'description': 'Number of boundary points',
        'unit': 'dimensionless',
        'default': 100,
        'range': [10, 10000],
        'category': 'sampling_parameters',
        'optimization_target': 'accuracy'
    },
    'initial_points': {
        'name': 'Initial Points',
        'description': 'Number of initial condition points',
        'unit': 'dimensionless',
        'default': 100,
        'range': [10, 10000],
        'category': 'sampling_parameters',
        'optimization_target': 'accuracy'
    },
    'data_points': {
        'name': 'Data Points',
        'description': 'Number of observational data points',
        'unit': 'dimensionless',
        'default': 100,
        'range': [10, 10000],
        'category': 'sampling_parameters',
        'optimization_target': 'accuracy'
    },
    
    # Adaptive Parameters
    'adaptive_sampling': {
        'name': 'Adaptive Sampling',
        'description': 'Whether to use adaptive sampling',
        'unit': 'dimensionless',
        'default': True,
        'range': [True, False],
        'category': 'adaptive_parameters',
        'optimization_target': 'efficiency'
    },
    'error_threshold': {
        'name': 'Error Threshold',
        'description': 'Threshold for adaptive sampling',
        'unit': 'dimensionless',
        'default': 0.01,
        'range': [1e-6, 1e-1],
        'category': 'adaptive_parameters',
        'optimization_target': 'accuracy'
    },
    'refinement_factor': {
        'name': 'Refinement Factor',
        'description': 'Factor for mesh refinement',
        'unit': 'dimensionless',
        'default': 2.0,
        'range': [1.1, 10.0],
        'category': 'adaptive_parameters',
        'optimization_target': 'efficiency'
    },
    
    # Parallel Computing Parameters
    'num_processes': {
        'name': 'Number of Processes',
        'description': 'Number of parallel processes',
        'unit': 'dimensionless',
        'default': 1,
        'range': [1, 100],
        'category': 'parallel_parameters',
        'optimization_target': 'speed'
    },
    'chunk_size': {
        'name': 'Chunk Size',
        'description': 'Size of data chunks for parallel processing',
        'unit': 'dimensionless',
        'default': 1000,
        'range': [100, 100000],
        'category': 'parallel_parameters',
        'optimization_target': 'memory'
    },
    'load_balancing': {
        'name': 'Load Balancing',
        'description': 'Load balancing strategy',
        'unit': 'dimensionless',
        'default': 'dynamic',
        'range': ['static', 'dynamic', 'adaptive'],
        'category': 'parallel_parameters',
        'optimization_target': 'speed'
    },
    
    # Memory Management Parameters
    'memory_limit': {
        'name': 'Memory Limit',
        'description': 'Memory limit for computations',
        'unit': 'GB',
        'default': 8.0,
        'range': [1.0, 100.0],
        'category': 'memory_parameters',
        'optimization_target': 'memory'
    },
    'cache_size': {
        'name': 'Cache Size',
        'description': 'Size of computation cache',
        'unit': 'MB',
        'default': 1000,
        'range': [100, 10000],
        'category': 'memory_parameters',
        'optimization_target': 'speed'
    },
    'garbage_collection': {
        'name': 'Garbage Collection',
        'description': 'Garbage collection frequency',
        'unit': 'dimensionless',
        'default': 1000,
        'range': [100, 10000],
        'category': 'memory_parameters',
        'optimization_target': 'memory'
    },
    
    # Algorithm Parameters
    'optimization_algorithm': {
        'name': 'Optimization Algorithm',
        'description': 'Optimization algorithm for training',
        'unit': 'dimensionless',
        'default': 'adam',
        'range': ['sgd', 'adam', 'lbfgs', 'rmsprop'],
        'category': 'algorithm_parameters',
        'optimization_target': 'convergence'
    },
    'line_search': {
        'name': 'Line Search',
        'description': 'Whether to use line search',
        'unit': 'dimensionless',
        'default': True,
        'range': [True, False],
        'category': 'algorithm_parameters',
        'optimization_target': 'convergence'
    },
    'momentum': {
        'name': 'Momentum',
        'description': 'Momentum parameter for optimization',
        'unit': 'dimensionless',
        'default': 0.9,
        'range': [0.0, 1.0],
        'category': 'algorithm_parameters',
        'optimization_target': 'convergence'
    },
    
    # Preconditioning Parameters
    'preconditioner': {
        'name': 'Preconditioner',
        'description': 'Type of preconditioner for linear solvers',
        'unit': 'dimensionless',
        'default': 'ilu',
        'range': ['none', 'ilu', 'amg', 'jacobi'],
        'category': 'preconditioning_parameters',
        'optimization_target': 'convergence'
    },
    'preconditioner_tolerance': {
        'name': 'Preconditioner Tolerance',
        'description': 'Tolerance for preconditioner',
        'unit': 'dimensionless',
        'default': 1e-3,
        'range': [1e-6, 1e-1],
        'category': 'preconditioning_parameters',
        'optimization_target': 'convergence'
    },
    
    # Performance Monitoring
    'performance_monitoring': {
        'name': 'Performance Monitoring',
        'description': 'Whether to monitor performance',
        'unit': 'dimensionless',
        'default': True,
        'range': [True, False],
        'category': 'monitoring_parameters',
        'optimization_target': 'efficiency'
    },
    'profiling_level': {
        'name': 'Profiling Level',
        'description': 'Level of performance profiling',
        'unit': 'dimensionless',
        'default': 'basic',
        'range': ['none', 'basic', 'detailed', 'full'],
        'category': 'monitoring_parameters',
        'optimization_target': 'efficiency'
    },
    'timing_precision': {
        'name': 'Timing Precision',
        'description': 'Precision for timing measurements',
        'unit': 's',
        'default': 1e-6,
        'range': [1e-9, 1e-3],
        'category': 'monitoring_parameters',
        'optimization_target': 'efficiency'
    }
} 