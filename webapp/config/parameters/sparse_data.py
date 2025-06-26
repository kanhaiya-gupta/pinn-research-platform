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