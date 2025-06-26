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

# Equation-specific parameter mappings
CONTROL_OPTIMIZATION_EQUATION_PARAMETERS = {
    'control_heat': {
        'thermal_diffusivity': {
            'name': 'Thermal Diffusivity (α)',
            'description': 'Thermal diffusivity coefficient',
            'unit': 'm²/s',
            'default': 1e-5,
            'range': [1e-8, 1e-3],
            'category': 'thermal_properties'
        },
        'heat_source_control': {
            'name': 'Heat Source Control',
            'description': 'Control input for heat source',
            'unit': 'W/m³',
            'default': 0.0,
            'range': [-1e6, 1e6],
            'category': 'control_variables'
        },
        'state_tracking_weight': {
            'name': 'State Tracking Weight',
            'description': 'Weight for temperature tracking',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'control_effort_weight': {
            'name': 'Control Effort Weight',
            'description': 'Weight for control effort',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
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
    
    'control_burgers': {
        'viscosity': {
            'name': 'Viscosity (ν)',
            'description': 'Dynamic viscosity coefficient',
            'unit': 'Pa·s',
            'default': 0.01,
            'range': [1e-6, 1e-1],
            'category': 'fluid_properties'
        },
        'velocity_control': {
            'name': 'Velocity Control',
            'description': 'Control input for velocity field',
            'unit': 'm/s',
            'default': 0.0,
            'range': [-100.0, 100.0],
            'category': 'control_variables'
        },
        'state_tracking_weight': {
            'name': 'State Tracking Weight',
            'description': 'Weight for velocity tracking',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'control_effort_weight': {
            'name': 'Control Effort Weight',
            'description': 'Weight for control effort',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
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
    
    'control_navier_stokes': {
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
        'velocity_control': {
            'name': 'Velocity Control',
            'description': 'Control input for velocity field',
            'unit': 'm/s',
            'default': 0.0,
            'range': [-100.0, 100.0],
            'category': 'control_variables'
        },
        'pressure_control': {
            'name': 'Pressure Control',
            'description': 'Control input for pressure field',
            'unit': 'Pa',
            'default': 0.0,
            'range': [-1e6, 1e6],
            'category': 'control_variables'
        },
        'state_tracking_weight': {
            'name': 'State Tracking Weight',
            'description': 'Weight for flow tracking',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'control_effort_weight': {
            'name': 'Control Effort Weight',
            'description': 'Weight for control effort',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
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
    
    'control_reaction_diffusion': {
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
        'concentration_control': {
            'name': 'Concentration Control',
            'description': 'Control input for concentration field',
            'unit': 'mol/m³',
            'default': 0.0,
            'range': [0.0, 1000.0],
            'category': 'control_variables'
        },
        'state_tracking_weight': {
            'name': 'State Tracking Weight',
            'description': 'Weight for concentration tracking',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'control_effort_weight': {
            'name': 'Control Effort Weight',
            'description': 'Weight for control effort',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
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
    
    'control_elastic': {
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
        'displacement_control': {
            'name': 'Displacement Control',
            'description': 'Control input for displacement field',
            'unit': 'm',
            'default': 0.0,
            'range': [-1.0, 1.0],
            'category': 'control_variables'
        },
        'state_tracking_weight': {
            'name': 'State Tracking Weight',
            'description': 'Weight for displacement tracking',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'control_effort_weight': {
            'name': 'Control Effort Weight',
            'description': 'Weight for control effort',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
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
    
    'control_wave': {
        'wave_speed': {
            'name': 'Wave Speed (c)',
            'description': 'Wave propagation speed',
            'unit': 'm/s',
            'default': 340.0,
            'range': [1.0, 10000.0],
            'category': 'wave_properties'
        },
        'control_input': {
            'name': 'Control Input',
            'description': 'General control input variable',
            'unit': 'dimensionless',
            'default': 0.0,
            'range': [-10.0, 10.0],
            'category': 'control_variables'
        },
        'state_tracking_weight': {
            'name': 'State Tracking Weight',
            'description': 'Weight for wave amplitude tracking',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'control_effort_weight': {
            'name': 'Control Effort Weight',
            'description': 'Weight for control effort',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
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
    
    'control_schrodinger': {
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
        'control_input': {
            'name': 'Control Input',
            'description': 'General control input variable',
            'unit': 'dimensionless',
            'default': 0.0,
            'range': [-10.0, 10.0],
            'category': 'control_variables'
        },
        'state_tracking_weight': {
            'name': 'State Tracking Weight',
            'description': 'Weight for wave function tracking',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'control_effort_weight': {
            'name': 'Control Effort Weight',
            'description': 'Weight for control effort',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
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
    
    'control_phase_field': {
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
        'control_input': {
            'name': 'Control Input',
            'description': 'General control input variable',
            'unit': 'dimensionless',
            'default': 0.0,
            'range': [-10.0, 10.0],
            'category': 'control_variables'
        },
        'state_tracking_weight': {
            'name': 'State Tracking Weight',
            'description': 'Weight for phase field tracking',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'control_effort_weight': {
            'name': 'Control Effort Weight',
            'description': 'Weight for control effort',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
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
    
    'control_poroelasticity': {
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
        'pressure_control': {
            'name': 'Pressure Control',
            'description': 'Control input for pressure field',
            'unit': 'Pa',
            'default': 0.0,
            'range': [-1e6, 1e6],
            'category': 'control_variables'
        },
        'state_tracking_weight': {
            'name': 'State Tracking Weight',
            'description': 'Weight for poroelastic tracking',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'control_effort_weight': {
            'name': 'Control Effort Weight',
            'description': 'Weight for control effort',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
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
    
    'control_viscoelasticity': {
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
        'control_input': {
            'name': 'Control Input',
            'description': 'General control input variable',
            'unit': 'dimensionless',
            'default': 0.0,
            'range': [-10.0, 10.0],
            'category': 'control_variables'
        },
        'state_tracking_weight': {
            'name': 'State Tracking Weight',
            'description': 'Weight for viscoelastic tracking',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'control_effort_weight': {
            'name': 'Control Effort Weight',
            'description': 'Weight for control effort',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
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
    
    'control_radiative_transfer': {
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
        'control_input': {
            'name': 'Control Input',
            'description': 'General control input variable',
            'unit': 'dimensionless',
            'default': 0.0,
            'range': [-10.0, 10.0],
            'category': 'control_variables'
        },
        'state_tracking_weight': {
            'name': 'State Tracking Weight',
            'description': 'Weight for radiative tracking',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'control_effort_weight': {
            'name': 'Control Effort Weight',
            'description': 'Weight for control effort',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
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
    
    'control_shallow_water': {
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
        'control_input': {
            'name': 'Control Input',
            'description': 'General control input variable',
            'unit': 'dimensionless',
            'default': 0.0,
            'range': [-10.0, 10.0],
            'category': 'control_variables'
        },
        'state_tracking_weight': {
            'name': 'State Tracking Weight',
            'description': 'Weight for shallow water tracking',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'control_effort_weight': {
            'name': 'Control Effort Weight',
            'description': 'Weight for control effort',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
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
    
    'control_maxwell': {
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
        'control_input': {
            'name': 'Control Input',
            'description': 'General control input variable',
            'unit': 'dimensionless',
            'default': 0.0,
            'range': [-10.0, 10.0],
            'category': 'control_variables'
        },
        'state_tracking_weight': {
            'name': 'State Tracking Weight',
            'description': 'Weight for electromagnetic tracking',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'control_effort_weight': {
            'name': 'Control Effort Weight',
            'description': 'Weight for control effort',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
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
    
    'control_helmholtz': {
        'wavenumber': {
            'name': 'Wavenumber (k)',
            'description': 'Wavenumber in Helmholtz equation',
            'unit': '1/m',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'wave_properties'
        },
        'control_input': {
            'name': 'Control Input',
            'description': 'General control input variable',
            'unit': 'dimensionless',
            'default': 0.0,
            'range': [-10.0, 10.0],
            'category': 'control_variables'
        },
        'state_tracking_weight': {
            'name': 'State Tracking Weight',
            'description': 'Weight for Helmholtz tracking',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'control_effort_weight': {
            'name': 'Control Effort Weight',
            'description': 'Weight for control effort',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
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
    
    'control_shm': {
        'natural_frequency': {
            'name': 'Natural Frequency (ω)',
            'description': 'Natural frequency of oscillation',
            'unit': 'rad/s',
            'default': 1.0,
            'range': [0.1, 100.0],
            'category': 'mechanical_properties'
        },
        'control_input': {
            'name': 'Control Input',
            'description': 'General control input variable',
            'unit': 'dimensionless',
            'default': 0.0,
            'range': [-10.0, 10.0],
            'category': 'control_variables'
        },
        'state_tracking_weight': {
            'name': 'State Tracking Weight',
            'description': 'Weight for SHM tracking',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'control_effort_weight': {
            'name': 'Control Effort Weight',
            'description': 'Weight for control effort',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
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
    
    'control_advection_diffusion': {
        'advection_velocity': {
            'name': 'Advection Velocity (v)',
            'description': 'Advection velocity vector',
            'unit': 'm/s',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'transport_properties'
        },
        'diffusion_coefficient': {
            'name': 'Diffusion Coefficient (D)',
            'description': 'Diffusion coefficient',
            'unit': 'm²/s',
            'default': 1e-5,
            'range': [1e-8, 1e-3],
            'category': 'transport_properties'
        },
        'concentration_control': {
            'name': 'Concentration Control',
            'description': 'Control input for concentration field',
            'unit': 'mol/m³',
            'default': 0.0,
            'range': [0.0, 1000.0],
            'category': 'control_variables'
        },
        'state_tracking_weight': {
            'name': 'State Tracking Weight',
            'description': 'Weight for concentration tracking',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'control_effort_weight': {
            'name': 'Control Effort Weight',
            'description': 'Weight for control effort',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
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
    
    'control_atmospheric_oceanic': {
        'coriolis_parameter': {
            'name': 'Coriolis Parameter (f)',
            'description': 'Coriolis parameter for atmospheric/oceanic flows',
            'unit': '1/s',
            'default': 1e-4,
            'range': [1e-5, 1e-3],
            'category': 'geophysical_properties'
        },
        'buoyancy_frequency': {
            'name': 'Buoyancy Frequency (N)',
            'description': 'Brunt-Väisälä frequency',
            'unit': '1/s',
            'default': 1e-3,
            'range': [1e-4, 1e-2],
            'category': 'geophysical_properties'
        },
        'control_input': {
            'name': 'Control Input',
            'description': 'General control input variable',
            'unit': 'dimensionless',
            'default': 0.0,
            'range': [-10.0, 10.0],
            'category': 'control_variables'
        },
        'state_tracking_weight': {
            'name': 'State Tracking Weight',
            'description': 'Weight for atmospheric/oceanic tracking',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'control_effort_weight': {
            'name': 'Control Effort Weight',
            'description': 'Weight for control effort',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
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
    
    'control_biomechanical_transport': {
        'permeability': {
            'name': 'Permeability (κ)',
            'description': 'Tissue permeability',
            'unit': 'm²',
            'default': 1e-12,
            'range': [1e-16, 1e-8],
            'category': 'biomechanical_properties'
        },
        'diffusion_coefficient': {
            'name': 'Diffusion Coefficient (D)',
            'description': 'Molecular diffusion coefficient',
            'unit': 'm²/s',
            'default': 1e-9,
            'range': [1e-12, 1e-6],
            'category': 'transport_properties'
        },
        'control_input': {
            'name': 'Control Input',
            'description': 'General control input variable',
            'unit': 'dimensionless',
            'default': 0.0,
            'range': [-10.0, 10.0],
            'category': 'control_variables'
        },
        'state_tracking_weight': {
            'name': 'State Tracking Weight',
            'description': 'Weight for biomechanical tracking',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'control_effort_weight': {
            'name': 'Control Effort Weight',
            'description': 'Weight for control effort',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
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
    
    'control_crystal_plasticity': {
        'shear_modulus': {
            'name': 'Shear Modulus (G)',
            'description': 'Shear modulus for crystal plasticity',
            'unit': 'GPa',
            'default': 80.0,
            'range': [10.0, 500.0],
            'category': 'mechanical_properties'
        },
        'critical_resolved_shear_stress': {
            'name': 'Critical Resolved Shear Stress (τ_c)',
            'description': 'Critical resolved shear stress',
            'unit': 'MPa',
            'default': 100.0,
            'range': [1.0, 1000.0],
            'category': 'mechanical_properties'
        },
        'control_input': {
            'name': 'Control Input',
            'description': 'General control input variable',
            'unit': 'dimensionless',
            'default': 0.0,
            'range': [-10.0, 10.0],
            'category': 'control_variables'
        },
        'state_tracking_weight': {
            'name': 'State Tracking Weight',
            'description': 'Weight for crystal plasticity tracking',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'control_effort_weight': {
            'name': 'Control Effort Weight',
            'description': 'Weight for control effort',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1e-6,
            'range': [1e-9, 1e-3],
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
    
    'control_diffusion_solids': {
        'diffusion_coefficient': {
            'name': 'Diffusion Coefficient (D)',
            'description': 'Diffusion coefficient in solids',
            'unit': 'm²/s',
            'default': 1e-12,
            'range': [1e-20, 1e-8],
            'category': 'transport_properties'
        },
        'activation_energy': {
            'name': 'Activation Energy (E_a)',
            'description': 'Activation energy for diffusion',
            'unit': 'J/mol',
            'default': 100000.0,
            'range': [10000.0, 500000.0],
            'category': 'thermal_properties'
        },
        'concentration_control': {
            'name': 'Concentration Control',
            'description': 'Control input for concentration field',
            'unit': 'mol/m³',
            'default': 0.0,
            'range': [0.0, 1000.0],
            'category': 'control_variables'
        },
        'state_tracking_weight': {
            'name': 'State Tracking Weight',
            'description': 'Weight for diffusion tracking',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'control_effort_weight': {
            'name': 'Control Effort Weight',
            'description': 'Weight for control effort',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1e-6,
            'range': [1e-9, 1e-3],
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
    
    'control_elastic_wave': {
        'wave_speed_p': {
            'name': 'P-Wave Speed (c_p)',
            'description': 'Primary wave speed',
            'unit': 'm/s',
            'default': 5000.0,
            'range': [1000.0, 10000.0],
            'category': 'wave_properties'
        },
        'wave_speed_s': {
            'name': 'S-Wave Speed (c_s)',
            'description': 'Secondary wave speed',
            'unit': 'm/s',
            'default': 3000.0,
            'range': [500.0, 6000.0],
            'category': 'wave_properties'
        },
        'control_input': {
            'name': 'Control Input',
            'description': 'General control input variable',
            'unit': 'dimensionless',
            'default': 0.0,
            'range': [-10.0, 10.0],
            'category': 'control_variables'
        },
        'state_tracking_weight': {
            'name': 'State Tracking Weight',
            'description': 'Weight for elastic wave tracking',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'control_effort_weight': {
            'name': 'Control Effort Weight',
            'description': 'Weight for control effort',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 100.0,
            'range': [10.0, 1000.0],
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
    
    'control_electromagnetic_thermal': {
        'electrical_conductivity': {
            'name': 'Electrical Conductivity (σ)',
            'description': 'Electrical conductivity',
            'unit': 'S/m',
            'default': 1e6,
            'range': [1e-6, 1e8],
            'category': 'electrical_properties'
        },
        'thermal_conductivity': {
            'name': 'Thermal Conductivity (k)',
            'description': 'Thermal conductivity',
            'unit': 'W/(m·K)',
            'default': 50.0,
            'range': [0.1, 1000.0],
            'category': 'thermal_properties'
        },
        'control_input': {
            'name': 'Control Input',
            'description': 'General control input variable',
            'unit': 'dimensionless',
            'default': 0.0,
            'range': [-10.0, 10.0],
            'category': 'control_variables'
        },
        'state_tracking_weight': {
            'name': 'State Tracking Weight',
            'description': 'Weight for EM-thermal tracking',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'control_effort_weight': {
            'name': 'Control Effort Weight',
            'description': 'Weight for control effort',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
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
    
    'control_fluid_structure_interaction': {
        'fluid_density': {
            'name': 'Fluid Density (ρ_f)',
            'description': 'Fluid density',
            'unit': 'kg/m³',
            'default': 1000.0,
            'range': [1.0, 20000.0],
            'category': 'fluid_properties'
        },
        'fluid_viscosity': {
            'name': 'Fluid Viscosity (μ_f)',
            'description': 'Fluid dynamic viscosity',
            'unit': 'Pa·s',
            'default': 0.001,
            'range': [1e-6, 1e-1],
            'category': 'fluid_properties'
        },
        'structure_modulus': {
            'name': 'Structure Modulus (E_s)',
            'description': 'Young\'s modulus of structure',
            'unit': 'GPa',
            'default': 200.0,
            'range': [1.0, 1000.0],
            'category': 'mechanical_properties'
        },
        'control_input': {
            'name': 'Control Input',
            'description': 'General control input variable',
            'unit': 'dimensionless',
            'default': 0.0,
            'range': [-10.0, 10.0],
            'category': 'control_variables'
        },
        'state_tracking_weight': {
            'name': 'State Tracking Weight',
            'description': 'Weight for FSI tracking',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'control_effort_weight': {
            'name': 'Control Effort Weight',
            'description': 'Weight for control effort',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
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
    
    'control_geophysical_flow': {
        'coriolis_parameter': {
            'name': 'Coriolis Parameter (f)',
            'description': 'Coriolis parameter for geophysical flows',
            'unit': '1/s',
            'default': 1e-4,
            'range': [1e-5, 1e-3],
            'category': 'geophysical_properties'
        },
        'stratification_parameter': {
            'name': 'Stratification Parameter (N)',
            'description': 'Stratification parameter',
            'unit': '1/s',
            'default': 1e-3,
            'range': [1e-4, 1e-2],
            'category': 'geophysical_properties'
        },
        'control_input': {
            'name': 'Control Input',
            'description': 'General control input variable',
            'unit': 'dimensionless',
            'default': 0.0,
            'range': [-10.0, 10.0],
            'category': 'control_variables'
        },
        'state_tracking_weight': {
            'name': 'State Tracking Weight',
            'description': 'Weight for geophysical flow tracking',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'control_effort_weight': {
            'name': 'Control Effort Weight',
            'description': 'Weight for control effort',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
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
    
    'control_grain_growth': {
        'mobility': {
            'name': 'Grain Boundary Mobility (M)',
            'description': 'Grain boundary mobility',
            'unit': 'm²/(J·s)',
            'default': 1e-6,
            'range': [1e-12, 1e-3],
            'category': 'microstructure_properties'
        },
        'grain_boundary_energy': {
            'name': 'Grain Boundary Energy (γ)',
            'description': 'Grain boundary energy',
            'unit': 'J/m²',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'microstructure_properties'
        },
        'control_input': {
            'name': 'Control Input',
            'description': 'General control input variable',
            'unit': 'dimensionless',
            'default': 0.0,
            'range': [-10.0, 10.0],
            'category': 'control_variables'
        },
        'state_tracking_weight': {
            'name': 'State Tracking Weight',
            'description': 'Weight for grain growth tracking',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'control_effort_weight': {
            'name': 'Control Effort Weight',
            'description': 'Weight for control effort',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1e-6,
            'range': [1e-9, 1e-3],
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
    
    'control_heat_transfer': {
        'thermal_conductivity': {
            'name': 'Thermal Conductivity (k)',
            'description': 'Thermal conductivity coefficient',
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
        'heat_source_control': {
            'name': 'Heat Source Control',
            'description': 'Control input for heat source',
            'unit': 'W/m³',
            'default': 0.0,
            'range': [-1e6, 1e6],
            'category': 'control_variables'
        },
        'state_tracking_weight': {
            'name': 'State Tracking Weight',
            'description': 'Weight for temperature tracking',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'control_effort_weight': {
            'name': 'Control Effort Weight',
            'description': 'Weight for control effort',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
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
    
    'control_laser_heat_source': {
        'laser_power_control': {
            'name': 'Laser Power Control',
            'description': 'Control input for laser power',
            'unit': 'W',
            'default': 1000.0,
            'range': [1.0, 10000.0],
            'category': 'laser_control'
        },
        'laser_scan_speed_control': {
            'name': 'Laser Scan Speed Control',
            'description': 'Control input for laser scan speed',
            'unit': 'm/s',
            'default': 1.0,
            'range': [0.01, 10.0],
            'category': 'laser_control'
        },
        'laser_spot_size_control': {
            'name': 'Laser Spot Size Control',
            'description': 'Control input for laser spot size',
            'unit': 'm',
            'default': 1e-3,
            'range': [1e-5, 1e-2],
            'category': 'laser_control'
        },
        'absorption_coefficient': {
            'name': 'Absorption Coefficient (α)',
            'description': 'Material absorption coefficient',
            'unit': '1/m',
            'default': 1e6,
            'range': [1e3, 1e8],
            'category': 'optical_properties'
        },
        'state_tracking_weight': {
            'name': 'State Tracking Weight',
            'description': 'Weight for laser heat tracking',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'control_effort_weight': {
            'name': 'Control Effort Weight',
            'description': 'Weight for control effort',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
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
    
    'control_magnetohydrodynamics': {
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
        'fluid_viscosity': {
            'name': 'Fluid Viscosity (μ_f)',
            'description': 'Fluid dynamic viscosity',
            'unit': 'Pa·s',
            'default': 0.001,
            'range': [1e-6, 1e-1],
            'category': 'fluid_properties'
        },
        'control_input': {
            'name': 'Control Input',
            'description': 'General control input variable',
            'unit': 'dimensionless',
            'default': 0.0,
            'range': [-10.0, 10.0],
            'category': 'control_variables'
        },
        'state_tracking_weight': {
            'name': 'State Tracking Weight',
            'description': 'Weight for MHD tracking',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'control_effort_weight': {
            'name': 'Control Effort Weight',
            'description': 'Weight for control effort',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
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
    
    'control_melt_pool_dynamics': {
        'surface_tension': {
            'name': 'Surface Tension (γ)',
            'description': 'Liquid surface tension',
            'unit': 'N/m',
            'default': 1.0,
            'range': [0.01, 10.0],
            'category': 'surface_properties'
        },
        'thermal_conductivity': {
            'name': 'Thermal Conductivity (k)',
            'description': 'Thermal conductivity',
            'unit': 'W/(m·K)',
            'default': 50.0,
            'range': [0.1, 1000.0],
            'category': 'thermal_properties'
        },
        'latent_heat': {
            'name': 'Latent Heat (L)',
            'description': 'Latent heat of fusion',
            'unit': 'J/kg',
            'default': 3e5,
            'range': [1e4, 1e6],
            'category': 'thermal_properties'
        },
        'control_input': {
            'name': 'Control Input',
            'description': 'General control input variable',
            'unit': 'dimensionless',
            'default': 0.0,
            'range': [-10.0, 10.0],
            'category': 'control_variables'
        },
        'state_tracking_weight': {
            'name': 'State Tracking Weight',
            'description': 'Weight for melt pool tracking',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'control_effort_weight': {
            'name': 'Control Effort Weight',
            'description': 'Weight for control effort',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
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
    
    'control_microstructure_evolution': {
        'diffusion_coefficient': {
            'name': 'Diffusion Coefficient (D)',
            'description': 'Atomic diffusion coefficient',
            'unit': 'm²/s',
            'default': 1e-12,
            'range': [1e-20, 1e-8],
            'category': 'transport_properties'
        },
        'interface_energy': {
            'name': 'Interface Energy (γ)',
            'description': 'Grain boundary energy',
            'unit': 'J/m²',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'microstructure_properties'
        },
        'mobility_coefficient': {
            'name': 'Mobility Coefficient (M)',
            'description': 'Interface mobility coefficient',
            'unit': 'm²/(J·s)',
            'default': 1e-6,
            'range': [1e-12, 1e-3],
            'category': 'microstructure_properties'
        },
        'control_input': {
            'name': 'Control Input',
            'description': 'General control input variable',
            'unit': 'dimensionless',
            'default': 0.0,
            'range': [-10.0, 10.0],
            'category': 'control_variables'
        },
        'state_tracking_weight': {
            'name': 'State Tracking Weight',
            'description': 'Weight for microstructure tracking',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'control_effort_weight': {
            'name': 'Control Effort Weight',
            'description': 'Weight for control effort',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1e-6,
            'range': [1e-9, 1e-3],
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
    
    'control_nuclear_thermal': {
        'fission_cross_section': {
            'name': 'Fission Cross Section (σ_f)',
            'description': 'Nuclear fission cross section',
            'unit': 'barn',
            'default': 1e-24,
            'range': [1e-28, 1e-20],
            'category': 'nuclear_properties'
        },
        'neutron_flux': {
            'name': 'Neutron Flux (φ)',
            'description': 'Neutron flux density',
            'unit': 'n/(cm²·s)',
            'default': 1e14,
            'range': [1e10, 1e18],
            'category': 'nuclear_properties'
        },
        'thermal_conductivity': {
            'name': 'Thermal Conductivity (k)',
            'description': 'Thermal conductivity',
            'unit': 'W/(m·K)',
            'default': 50.0,
            'range': [0.1, 1000.0],
            'category': 'thermal_properties'
        },
        'control_input': {
            'name': 'Control Input',
            'description': 'General control input variable',
            'unit': 'dimensionless',
            'default': 0.0,
            'range': [-10.0, 10.0],
            'category': 'control_variables'
        },
        'state_tracking_weight': {
            'name': 'State Tracking Weight',
            'description': 'Weight for nuclear thermal tracking',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'control_effort_weight': {
            'name': 'Control Effort Weight',
            'description': 'Weight for control effort',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
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
    
    'control_quantum_mechanical': {
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
            'name': 'Potential Strength (V_0)',
            'description': 'Potential well strength',
            'unit': 'J',
            'default': 1e-19,
            'range': [1e-21, 1e-17],
            'category': 'quantum_properties'
        },
        'control_input': {
            'name': 'Control Input',
            'description': 'General control input variable',
            'unit': 'dimensionless',
            'default': 0.0,
            'range': [-10.0, 10.0],
            'category': 'control_variables'
        },
        'state_tracking_weight': {
            'name': 'State Tracking Weight',
            'description': 'Weight for quantum mechanical tracking',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'control_effort_weight': {
            'name': 'Control Effort Weight',
            'description': 'Weight for control effort',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
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
    
    'control_phase_field_allen_cahn': {
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
        'double_well_height': {
            'name': 'Double Well Height (W)',
            'description': 'Double well potential height',
            'unit': 'J/m³',
            'default': 1e6,
            'range': [1e4, 1e8],
            'category': 'phase_field'
        },
        'control_input': {
            'name': 'Control Input',
            'description': 'General control input variable',
            'unit': 'dimensionless',
            'default': 0.0,
            'range': [-10.0, 10.0],
            'category': 'control_variables'
        },
        'state_tracking_weight': {
            'name': 'State Tracking Weight',
            'description': 'Weight for Allen-Cahn tracking',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'control_effort_weight': {
            'name': 'Control Effort Weight',
            'description': 'Weight for control effort',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
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
    
    'control_phase_field_cahn_hilliard': {
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
        'free_energy_parameter': {
            'name': 'Free Energy Parameter (a)',
            'description': 'Free energy parameter',
            'unit': 'J/m³',
            'default': 1e6,
            'range': [1e4, 1e8],
            'category': 'phase_field'
        },
        'control_input': {
            'name': 'Control Input',
            'description': 'General control input variable',
            'unit': 'dimensionless',
            'default': 0.0,
            'range': [-10.0, 10.0],
            'category': 'control_variables'
        },
        'state_tracking_weight': {
            'name': 'State Tracking Weight',
            'description': 'Weight for Cahn-Hilliard tracking',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'control_effort_weight': {
            'name': 'Control Effort Weight',
            'description': 'Weight for control effort',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
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
    
    'control_precipitation_nucleation': {
        'nucleation_rate': {
            'name': 'Nucleation Rate (J)',
            'description': 'Nucleation rate constant',
            'unit': '1/(m³·s)',
            'default': 1e12,
            'range': [1e6, 1e18],
            'category': 'nucleation_properties'
        },
        'critical_radius': {
            'name': 'Critical Radius (r_c)',
            'description': 'Critical nucleation radius',
            'unit': 'm',
            'default': 1e-9,
            'range': [1e-12, 1e-6],
            'category': 'nucleation_properties'
        },
        'interfacial_energy': {
            'name': 'Interfacial Energy (γ)',
            'description': 'Particle-matrix interfacial energy',
            'unit': 'J/m²',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'nucleation_properties'
        },
        'control_input': {
            'name': 'Control Input',
            'description': 'General control input variable',
            'unit': 'dimensionless',
            'default': 0.0,
            'range': [-10.0, 10.0],
            'category': 'control_variables'
        },
        'state_tracking_weight': {
            'name': 'State Tracking Weight',
            'description': 'Weight for precipitation tracking',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'control_effort_weight': {
            'name': 'Control Effort Weight',
            'description': 'Weight for control effort',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1e-6,
            'range': [1e-9, 1e-3],
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
    
    'control_residual_stress': {
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
        'control_input': {
            'name': 'Control Input',
            'description': 'General control input variable',
            'unit': 'dimensionless',
            'default': 0.0,
            'range': [-10.0, 10.0],
            'category': 'control_variables'
        },
        'state_tracking_weight': {
            'name': 'State Tracking Weight',
            'description': 'Weight for residual stress tracking',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'control_effort_weight': {
            'name': 'Control Effort Weight',
            'description': 'Weight for control effort',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
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
    
    'control_sintering': {
        'sintering_temperature': {
            'name': 'Sintering Temperature (T_s)',
            'description': 'Sintering temperature',
            'unit': 'K',
            'default': 1500.0,
            'range': [500.0, 3000.0],
            'category': 'thermal_properties'
        },
        'activation_energy': {
            'name': 'Activation Energy (E_a)',
            'description': 'Sintering activation energy',
            'unit': 'J/mol',
            'default': 100000.0,
            'range': [10000.0, 500000.0],
            'category': 'thermal_properties'
        },
        'particle_size': {
            'name': 'Particle Size (d)',
            'description': 'Initial particle size',
            'unit': 'm',
            'default': 1e-6,
            'range': [1e-9, 1e-3],
            'category': 'microstructure_properties'
        },
        'control_input': {
            'name': 'Control Input',
            'description': 'General control input variable',
            'unit': 'dimensionless',
            'default': 0.0,
            'range': [-10.0, 10.0],
            'category': 'control_variables'
        },
        'state_tracking_weight': {
            'name': 'State Tracking Weight',
            'description': 'Weight for sintering tracking',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'control_effort_weight': {
            'name': 'Control Effort Weight',
            'description': 'Weight for control effort',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
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
            'default': 3600.0,
            'range': [100.0, 86400.0],
            'category': 'temporal_properties'
        }
    },
    
    'control_solidification_stefan': {
        'latent_heat': {
            'name': 'Latent Heat (L)',
            'description': 'Latent heat of fusion',
            'unit': 'J/kg',
            'default': 3e5,
            'range': [1e4, 1e6],
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
        'melting_temperature': {
            'name': 'Melting Temperature (T_m)',
            'description': 'Melting temperature',
            'unit': 'K',
            'default': 1800.0,
            'range': [300.0, 4000.0],
            'category': 'thermal_properties'
        },
        'heat_source_control': {
            'name': 'Heat Source Control',
            'description': 'Control input for heat source',
            'unit': 'W/m³',
            'default': 0.0,
            'range': [-1e6, 1e6],
            'category': 'control_variables'
        },
        'state_tracking_weight': {
            'name': 'State Tracking Weight',
            'description': 'Weight for Stefan problem tracking',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'control_effort_weight': {
            'name': 'Control Effort Weight',
            'description': 'Weight for control effort',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
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
    
    'control_thermoelasticity': {
        'elastic_modulus': {
            'name': 'Elastic Modulus (E)',
            'description': 'Young\'s modulus',
            'unit': 'GPa',
            'default': 200.0,
            'range': [1.0, 1000.0],
            'category': 'mechanical_properties'
        },
        'thermal_conductivity': {
            'name': 'Thermal Conductivity (k)',
            'description': 'Thermal conductivity',
            'unit': 'W/(m·K)',
            'default': 50.0,
            'range': [0.1, 1000.0],
            'category': 'thermal_properties'
        },
        'thermal_expansion': {
            'name': 'Thermal Expansion (α)',
            'description': 'Thermal expansion coefficient',
            'unit': '1/K',
            'default': 1e-5,
            'range': [1e-7, 1e-3],
            'category': 'thermal_properties'
        },
        'control_input': {
            'name': 'Control Input',
            'description': 'General control input variable',
            'unit': 'dimensionless',
            'default': 0.0,
            'range': [-10.0, 10.0],
            'category': 'control_variables'
        },
        'state_tracking_weight': {
            'name': 'State Tracking Weight',
            'description': 'Weight for thermoelastic tracking',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
        },
        'control_effort_weight': {
            'name': 'Control Effort Weight',
            'description': 'Weight for control effort',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 10.0],
            'category': 'objective_weights'
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
    }
} 