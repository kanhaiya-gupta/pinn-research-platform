"""
Data Assimilation Parameters
Parameters for assimilating observational data into physical models.
"""

DATA_ASSIMILATION_PARAMETERS_DICT = {
    # Assimilation Coefficients
    'assimilation_strength': {
        'name': 'Assimilation Strength',
        'description': 'Strength of data assimilation term',
        'unit': 'dimensionless',
        'default': 1.0,
        'range': [0.0, 10.0],
        'category': 'assimilation_parameters',
        'adaptive': True
    },
    'temperature_assimilation_coefficient': {
        'name': 'Temperature Assimilation Coefficient',
        'description': 'Assimilation coefficient for temperature data',
        'unit': '1/s',
        'default': 1.0,
        'range': [0.0, 10.0],
        'category': 'assimilation_parameters',
        'adaptive': True
    },
    'velocity_assimilation_coefficient': {
        'name': 'Velocity Assimilation Coefficient',
        'description': 'Assimilation coefficient for velocity data',
        'unit': '1/s',
        'default': 1.0,
        'range': [0.0, 10.0],
        'category': 'assimilation_parameters',
        'adaptive': True
    },
    'concentration_assimilation_coefficient': {
        'name': 'Concentration Assimilation Coefficient',
        'description': 'Assimilation coefficient for concentration data',
        'unit': '1/s',
        'default': 1.0,
        'range': [0.0, 10.0],
        'category': 'assimilation_parameters',
        'adaptive': True
    },
    'pressure_assimilation_coefficient': {
        'name': 'Pressure Assimilation Coefficient',
        'description': 'Assimilation coefficient for pressure data',
        'unit': '1/s',
        'default': 1.0,
        'range': [0.0, 10.0],
        'category': 'assimilation_parameters',
        'adaptive': True
    },
    'displacement_assimilation_coefficient': {
        'name': 'Displacement Assimilation Coefficient',
        'description': 'Assimilation coefficient for displacement data',
        'unit': '1/s',
        'default': 1.0,
        'range': [0.0, 10.0],
        'category': 'assimilation_parameters',
        'adaptive': True
    },
    
    # Observation Parameters
    'observation_frequency': {
        'name': 'Observation Frequency',
        'description': 'Frequency of observational data updates',
        'unit': 'Hz',
        'default': 1.0,
        'range': [0.01, 100.0],
        'category': 'observation_parameters',
        'adaptive': False
    },
    'observation_noise': {
        'name': 'Observation Noise',
        'description': 'Standard deviation of observation noise',
        'unit': 'dimensionless',
        'default': 0.01,
        'range': [0.0, 0.1],
        'category': 'observation_parameters',
        'adaptive': False
    },
    'observation_uncertainty': {
        'name': 'Observation Uncertainty',
        'description': 'Uncertainty in observational measurements',
        'unit': 'dimensionless',
        'default': 0.05,
        'range': [0.0, 0.5],
        'category': 'observation_parameters',
        'adaptive': False
    },
    'observation_weight': {
        'name': 'Observation Weight',
        'description': 'Weight given to observational data',
        'unit': 'dimensionless',
        'default': 1.0,
        'range': [0.0, 10.0],
        'category': 'observation_parameters',
        'adaptive': True
    },
    
    # Kalman Filter Parameters
    'kalman_gain': {
        'name': 'Kalman Gain',
        'description': 'Kalman filter gain matrix',
        'unit': 'dimensionless',
        'default': 1.0,
        'range': [0.0, 10.0],
        'category': 'kalman_filter_parameters',
        'adaptive': True
    },
    'process_noise': {
        'name': 'Process Noise',
        'description': 'Process noise covariance',
        'unit': 'dimensionless',
        'default': 0.01,
        'range': [0.0, 1.0],
        'category': 'kalman_filter_parameters',
        'adaptive': True
    },
    'measurement_noise': {
        'name': 'Measurement Noise',
        'description': 'Measurement noise covariance',
        'unit': 'dimensionless',
        'default': 0.01,
        'range': [0.0, 1.0],
        'category': 'kalman_filter_parameters',
        'adaptive': True
    },
    
    # Ensemble Parameters
    'ensemble_size': {
        'name': 'Ensemble Size',
        'description': 'Number of ensemble members',
        'unit': 'dimensionless',
        'default': 100,
        'range': [10, 1000],
        'category': 'ensemble_parameters',
        'adaptive': False
    },
    'ensemble_inflation': {
        'name': 'Ensemble Inflation',
        'description': 'Ensemble inflation factor',
        'unit': 'dimensionless',
        'default': 1.1,
        'range': [1.0, 2.0],
        'category': 'ensemble_parameters',
        'adaptive': True
    },
    'localization_radius': {
        'name': 'Localization Radius',
        'description': 'Localization radius for ensemble methods',
        'unit': 'm',
        'default': 1.0,
        'range': [0.1, 10.0],
        'category': 'ensemble_parameters',
        'adaptive': True
    },
    
    # Variational Parameters
    'cost_function_weight': {
        'name': 'Cost Function Weight',
        'description': 'Weight in variational cost function',
        'unit': 'dimensionless',
        'default': 1.0,
        'range': [0.0, 10.0],
        'category': 'variational_parameters',
        'adaptive': True
    },
    'background_weight': {
        'name': 'Background Weight',
        'description': 'Weight for background state',
        'unit': 'dimensionless',
        'default': 1.0,
        'range': [0.0, 10.0],
        'category': 'variational_parameters',
        'adaptive': True
    },
    'observation_weight_variational': {
        'name': 'Observation Weight (Variational)',
        'description': 'Weight for observations in variational method',
        'unit': 'dimensionless',
        'default': 1.0,
        'range': [0.0, 10.0],
        'category': 'variational_parameters',
        'adaptive': True
    },
    
    # Time Window Parameters
    'assimilation_window': {
        'name': 'Assimilation Window',
        'description': 'Time window for data assimilation',
        'unit': 's',
        'default': 1.0,
        'range': [0.1, 100.0],
        'category': 'time_window_parameters',
        'adaptive': False
    },
    'forecast_horizon': {
        'name': 'Forecast Horizon',
        'description': 'Forecast time horizon',
        'unit': 's',
        'default': 10.0,
        'range': [1.0, 1000.0],
        'category': 'time_window_parameters',
        'adaptive': False
    },
    'update_interval': {
        'name': 'Update Interval',
        'description': 'Time interval between updates',
        'unit': 's',
        'default': 0.1,
        'range': [0.01, 10.0],
        'category': 'time_window_parameters',
        'adaptive': False
    },
    
    # Spatial Parameters
    'spatial_correlation_length': {
        'name': 'Spatial Correlation Length',
        'description': 'Spatial correlation length for observations',
        'unit': 'm',
        'default': 1.0,
        'range': [0.1, 10.0],
        'category': 'spatial_parameters',
        'adaptive': True
    },
    'temporal_correlation_time': {
        'name': 'Temporal Correlation Time',
        'description': 'Temporal correlation time for observations',
        'unit': 's',
        'default': 1.0,
        'range': [0.1, 100.0],
        'category': 'spatial_parameters',
        'adaptive': True
    },
    
    # Quality Control Parameters
    'quality_threshold': {
        'name': 'Quality Threshold',
        'description': 'Threshold for observation quality control',
        'unit': 'dimensionless',
        'default': 3.0,
        'range': [1.0, 10.0],
        'category': 'quality_control_parameters',
        'adaptive': False
    },
    'outlier_threshold': {
        'name': 'Outlier Threshold',
        'description': 'Threshold for outlier detection',
        'unit': 'dimensionless',
        'default': 5.0,
        'range': [1.0, 20.0],
        'category': 'quality_control_parameters',
        'adaptive': False
    },
    
    # Convergence Parameters
    'convergence_tolerance': {
        'name': 'Convergence Tolerance',
        'description': 'Tolerance for assimilation convergence',
        'unit': 'dimensionless',
        'default': 1e-6,
        'range': [1e-12, 1e-3],
        'category': 'convergence_parameters',
        'adaptive': False
    },
    'max_assimilation_iterations': {
        'name': 'Maximum Assimilation Iterations',
        'description': 'Maximum iterations for assimilation',
        'unit': 'dimensionless',
        'default': 100,
        'range': [10, 1000],
        'category': 'convergence_parameters',
        'adaptive': False
    },
    
    # Adaptive Parameters
    'adaptive_learning_rate': {
        'name': 'Adaptive Learning Rate',
        'description': 'Learning rate for adaptive assimilation',
        'unit': 'dimensionless',
        'default': 0.01,
        'range': [0.001, 0.1],
        'category': 'adaptive_parameters',
        'adaptive': True
    },
    'forgetting_factor': {
        'name': 'Forgetting Factor',
        'description': 'Forgetting factor for adaptive methods',
        'unit': 'dimensionless',
        'default': 0.95,
        'range': [0.5, 1.0],
        'category': 'adaptive_parameters',
        'adaptive': True
    }
} 