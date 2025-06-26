"""
Control Optimization Parameters
Parameters for optimal control and parameter optimization problems.
"""

CONTROL_OPTIMIZATION_PARAMETERS_DICT = {
    # Control Variables
    'control_input': {
        'name': 'Control Input',
        'description': 'General control input variable',
        'unit': 'dimensionless',
        'default': 0.0,
        'range': [-10.0, 10.0],
        'category': 'control_variables',
        'optimization_method': 'gradient_descent'
    },
    'heat_source_control': {
        'name': 'Heat Source Control',
        'description': 'Control input for heat source',
        'unit': 'W/m³',
        'default': 0.0,
        'range': [-1e6, 1e6],
        'category': 'control_variables',
        'optimization_method': 'optimal_control'
    },
    'velocity_control': {
        'name': 'Velocity Control',
        'description': 'Control input for velocity field',
        'unit': 'm/s',
        'default': 0.0,
        'range': [-100.0, 100.0],
        'category': 'control_variables',
        'optimization_method': 'optimal_control'
    },
    'pressure_control': {
        'name': 'Pressure Control',
        'description': 'Control input for pressure field',
        'unit': 'Pa',
        'default': 0.0,
        'range': [-1e6, 1e6],
        'category': 'control_variables',
        'optimization_method': 'optimal_control'
    },
    'temperature_control': {
        'name': 'Temperature Control',
        'description': 'Control input for temperature field',
        'unit': 'K',
        'default': 300.0,
        'range': [100.0, 2000.0],
        'category': 'control_variables',
        'optimization_method': 'optimal_control'
    },
    'concentration_control': {
        'name': 'Concentration Control',
        'description': 'Control input for concentration field',
        'unit': 'mol/m³',
        'default': 0.0,
        'range': [0.0, 1000.0],
        'category': 'control_variables',
        'optimization_method': 'optimal_control'
    },
    'displacement_control': {
        'name': 'Displacement Control',
        'description': 'Control input for displacement field',
        'unit': 'm',
        'default': 0.0,
        'range': [-1.0, 1.0],
        'category': 'control_variables',
        'optimization_method': 'optimal_control'
    },
    
    # Laser Control Parameters
    'laser_power_control': {
        'name': 'Laser Power Control',
        'description': 'Control input for laser power',
        'unit': 'W',
        'default': 1000.0,
        'range': [1.0, 10000.0],
        'category': 'laser_control',
        'optimization_method': 'optimal_control'
    },
    'laser_scan_speed_control': {
        'name': 'Laser Scan Speed Control',
        'description': 'Control input for laser scan speed',
        'unit': 'm/s',
        'default': 1.0,
        'range': [0.01, 10.0],
        'category': 'laser_control',
        'optimization_method': 'optimal_control'
    },
    'laser_spot_size_control': {
        'name': 'Laser Spot Size Control',
        'description': 'Control input for laser spot size',
        'unit': 'm',
        'default': 1e-3,
        'range': [1e-5, 1e-2],
        'category': 'laser_control',
        'optimization_method': 'optimal_control'
    },
    'laser_trajectory_control': {
        'name': 'Laser Trajectory Control',
        'description': 'Control input for laser trajectory',
        'unit': 'm',
        'default': [0.0, 0.0],
        'range': [0.0, 1.0],
        'category': 'laser_control',
        'optimization_method': 'trajectory_optimization'
    },
    
    # Boundary Control Parameters
    'boundary_temperature_control': {
        'name': 'Boundary Temperature Control',
        'description': 'Control input for boundary temperature',
        'unit': 'K',
        'default': 300.0,
        'range': [100.0, 2000.0],
        'category': 'boundary_control',
        'optimization_method': 'boundary_control'
    },
    'boundary_heat_flux_control': {
        'name': 'Boundary Heat Flux Control',
        'description': 'Control input for boundary heat flux',
        'unit': 'W/m²',
        'default': 0.0,
        'range': [-1e6, 1e6],
        'category': 'boundary_control',
        'optimization_method': 'boundary_control'
    },
    'boundary_pressure_control': {
        'name': 'Boundary Pressure Control',
        'description': 'Control input for boundary pressure',
        'unit': 'Pa',
        'default': 101325.0,
        'range': [1e3, 1e8],
        'category': 'boundary_control',
        'optimization_method': 'boundary_control'
    },
    'boundary_velocity_control': {
        'name': 'Boundary Velocity Control',
        'description': 'Control input for boundary velocity',
        'unit': 'm/s',
        'default': 0.0,
        'range': [-100.0, 100.0],
        'category': 'boundary_control',
        'optimization_method': 'boundary_control'
    },
    
    # Objective Function Weights
    'state_tracking_weight': {
        'name': 'State Tracking Weight',
        'description': 'Weight for state tracking in objective function',
        'unit': 'dimensionless',
        'default': 1.0,
        'range': [0.0, 10.0],
        'category': 'objective_weights',
        'optimization_method': 'weight_optimization'
    },
    'control_effort_weight': {
        'name': 'Control Effort Weight',
        'description': 'Weight for control effort in objective function',
        'unit': 'dimensionless',
        'default': 0.1,
        'range': [0.0, 10.0],
        'category': 'objective_weights',
        'optimization_method': 'weight_optimization'
    },
    'terminal_state_weight': {
        'name': 'Terminal State Weight',
        'description': 'Weight for terminal state in objective function',
        'unit': 'dimensionless',
        'default': 1.0,
        'range': [0.0, 10.0],
        'category': 'objective_weights',
        'optimization_method': 'weight_optimization'
    },
    'constraint_violation_weight': {
        'name': 'Constraint Violation Weight',
        'description': 'Weight for constraint violation penalty',
        'unit': 'dimensionless',
        'default': 100.0,
        'range': [1.0, 1000.0],
        'category': 'objective_weights',
        'optimization_method': 'weight_optimization'
    },
    
    # Optimization Algorithm Parameters
    'learning_rate': {
        'name': 'Learning Rate',
        'description': 'Learning rate for optimization algorithm',
        'unit': 'dimensionless',
        'default': 0.01,
        'range': [1e-6, 1.0],
        'category': 'optimization_parameters',
        'optimization_method': 'gradient_descent'
    },
    'momentum': {
        'name': 'Momentum',
        'description': 'Momentum parameter for optimization',
        'unit': 'dimensionless',
        'default': 0.9,
        'range': [0.0, 1.0],
        'category': 'optimization_parameters',
        'optimization_method': 'momentum_gradient'
    },
    'adam_beta1': {
        'name': 'Adam Beta1',
        'description': 'Beta1 parameter for Adam optimizer',
        'unit': 'dimensionless',
        'default': 0.9,
        'range': [0.0, 1.0],
        'category': 'optimization_parameters',
        'optimization_method': 'adam'
    },
    'adam_beta2': {
        'name': 'Adam Beta2',
        'description': 'Beta2 parameter for Adam optimizer',
        'unit': 'dimensionless',
        'default': 0.999,
        'range': [0.0, 1.0],
        'category': 'optimization_parameters',
        'optimization_method': 'adam'
    },
    
    # Constraint Parameters
    'control_bounds_lower': {
        'name': 'Control Bounds Lower',
        'description': 'Lower bounds for control variables',
        'unit': 'dimensionless',
        'default': -10.0,
        'range': [-100.0, 0.0],
        'category': 'constraint_parameters',
        'optimization_method': 'constrained_optimization'
    },
    'control_bounds_upper': {
        'name': 'Control Bounds Upper',
        'description': 'Upper bounds for control variables',
        'unit': 'dimensionless',
        'default': 10.0,
        'range': [0.0, 100.0],
        'category': 'constraint_parameters',
        'optimization_method': 'constrained_optimization'
    },
    'state_bounds_lower': {
        'name': 'State Bounds Lower',
        'description': 'Lower bounds for state variables',
        'unit': 'dimensionless',
        'default': -100.0,
        'range': [-1000.0, 0.0],
        'category': 'constraint_parameters',
        'optimization_method': 'constrained_optimization'
    },
    'state_bounds_upper': {
        'name': 'State Bounds Upper',
        'description': 'Upper bounds for state variables',
        'unit': 'dimensionless',
        'default': 100.0,
        'range': [0.0, 1000.0],
        'category': 'constraint_parameters',
        'optimization_method': 'constrained_optimization'
    },
    
    # Time Horizon Parameters
    'control_horizon': {
        'name': 'Control Horizon',
        'description': 'Time horizon for control optimization',
        'unit': 's',
        'default': 10.0,
        'range': [0.1, 1000.0],
        'category': 'time_horizon_parameters',
        'optimization_method': 'receding_horizon'
    },
    'prediction_horizon': {
        'name': 'Prediction Horizon',
        'description': 'Time horizon for prediction',
        'unit': 's',
        'default': 20.0,
        'range': [0.1, 1000.0],
        'category': 'time_horizon_parameters',
        'optimization_method': 'receding_horizon'
    },
    'control_interval': {
        'name': 'Control Interval',
        'description': 'Time interval between control updates',
        'unit': 's',
        'default': 0.1,
        'range': [0.01, 10.0],
        'category': 'time_horizon_parameters',
        'optimization_method': 'receding_horizon'
    },
    
    # Convergence Parameters
    'optimization_tolerance': {
        'name': 'Optimization Tolerance',
        'description': 'Tolerance for optimization convergence',
        'unit': 'dimensionless',
        'default': 1e-6,
        'range': [1e-12, 1e-3],
        'category': 'convergence_parameters',
        'optimization_method': 'convergence_criteria'
    },
    'max_optimization_iterations': {
        'name': 'Maximum Optimization Iterations',
        'description': 'Maximum iterations for optimization',
        'unit': 'dimensionless',
        'default': 1000,
        'range': [100, 10000],
        'category': 'convergence_parameters',
        'optimization_method': 'convergence_criteria'
    },
    
    # Robustness Parameters
    'uncertainty_robustness': {
        'name': 'Uncertainty Robustness',
        'description': 'Robustness parameter for uncertainty',
        'unit': 'dimensionless',
        'default': 0.1,
        'range': [0.0, 1.0],
        'category': 'robustness_parameters',
        'optimization_method': 'robust_optimization'
    },
    'disturbance_rejection': {
        'name': 'Disturbance Rejection',
        'description': 'Disturbance rejection parameter',
        'unit': 'dimensionless',
        'default': 1.0,
        'range': [0.0, 10.0],
        'category': 'robustness_parameters',
        'optimization_method': 'robust_optimization'
    }
} 