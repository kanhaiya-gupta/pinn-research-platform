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

# Equation-specific parameter mappings
DATA_ASSIMILATION_EQUATION_PARAMETERS = {
    'assimilation_heat': {
        'thermal_diffusivity': {
            'name': 'Thermal Diffusivity (α)',
            'description': 'Thermal diffusivity coefficient',
            'unit': 'm²/s',
            'default': 1e-5,
            'range': [1e-8, 1e-3],
            'category': 'thermal_properties'
        },
        'assimilation_strength': {
            'name': 'Assimilation Strength',
            'description': 'Strength of temperature data assimilation',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'assimilation_parameters'
        },
        'observation_frequency': {
            'name': 'Observation Frequency',
            'description': 'Frequency of temperature observations',
            'unit': 'Hz',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'observation_parameters'
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
    
    'assimilation_burgers': {
        'viscosity': {
            'name': 'Viscosity (ν)',
            'description': 'Dynamic viscosity coefficient',
            'unit': 'Pa·s',
            'default': 0.01,
            'range': [1e-6, 1e-1],
            'category': 'fluid_properties'
        },
        'assimilation_strength': {
            'name': 'Assimilation Strength',
            'description': 'Strength of velocity data assimilation',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'assimilation_parameters'
        },
        'observation_frequency': {
            'name': 'Observation Frequency',
            'description': 'Frequency of velocity observations',
            'unit': 'Hz',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'observation_parameters'
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
    
    'assimilation_navier_stokes': {
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
        'assimilation_strength': {
            'name': 'Assimilation Strength',
            'description': 'Strength of velocity/pressure data assimilation',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'assimilation_parameters'
        },
        'observation_frequency': {
            'name': 'Observation Frequency',
            'description': 'Frequency of flow observations',
            'unit': 'Hz',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'observation_parameters'
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
    
    'assimilation_reaction_diffusion': {
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
        'assimilation_strength': {
            'name': 'Assimilation Strength',
            'description': 'Strength of concentration data assimilation',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'assimilation_parameters'
        },
        'observation_frequency': {
            'name': 'Observation Frequency',
            'description': 'Frequency of concentration observations',
            'unit': 'Hz',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'observation_parameters'
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
    
    'assimilation_elastic': {
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
        'assimilation_strength': {
            'name': 'Assimilation Strength',
            'description': 'Strength of displacement data assimilation',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'assimilation_parameters'
        },
        'observation_frequency': {
            'name': 'Observation Frequency',
            'description': 'Frequency of displacement observations',
            'unit': 'Hz',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'observation_parameters'
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
    
    'assimilation_wave': {
        'wave_speed': {
            'name': 'Wave Speed (c)',
            'description': 'Wave propagation speed',
            'unit': 'm/s',
            'default': 340.0,
            'range': [1.0, 10000.0],
            'category': 'wave_properties'
        },
        'assimilation_strength': {
            'name': 'Assimilation Strength',
            'description': 'Strength of wave amplitude data assimilation',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'assimilation_parameters'
        },
        'observation_frequency': {
            'name': 'Observation Frequency',
            'description': 'Frequency of wave observations',
            'unit': 'Hz',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'observation_parameters'
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
    
    'assimilation_schrodinger': {
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
        'assimilation_strength': {
            'name': 'Assimilation Strength',
            'description': 'Strength of wave function data assimilation',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'assimilation_parameters'
        },
        'observation_frequency': {
            'name': 'Observation Frequency',
            'description': 'Frequency of quantum observations',
            'unit': 'Hz',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'observation_parameters'
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
    
    'assimilation_phase_field': {
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
        'assimilation_strength': {
            'name': 'Assimilation Strength',
            'description': 'Strength of phase field data assimilation',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'assimilation_parameters'
        },
        'observation_frequency': {
            'name': 'Observation Frequency',
            'description': 'Frequency of phase field observations',
            'unit': 'Hz',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'observation_parameters'
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
    
    'assimilation_poroelasticity': {
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
        'assimilation_strength': {
            'name': 'Assimilation Strength',
            'description': 'Strength of poroelastic data assimilation',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'assimilation_parameters'
        },
        'observation_frequency': {
            'name': 'Observation Frequency',
            'description': 'Frequency of poroelastic observations',
            'unit': 'Hz',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'observation_parameters'
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
    
    'assimilation_viscoelasticity': {
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
        'assimilation_strength': {
            'name': 'Assimilation Strength',
            'description': 'Strength of viscoelastic data assimilation',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'assimilation_parameters'
        },
        'observation_frequency': {
            'name': 'Observation Frequency',
            'description': 'Frequency of viscoelastic observations',
            'unit': 'Hz',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'observation_parameters'
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
    
    'assimilation_radiative_transfer': {
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
        'assimilation_strength': {
            'name': 'Assimilation Strength',
            'description': 'Strength of radiative data assimilation',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'assimilation_parameters'
        },
        'observation_frequency': {
            'name': 'Observation Frequency',
            'description': 'Frequency of radiative observations',
            'unit': 'Hz',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'observation_parameters'
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
    
    'assimilation_shallow_water': {
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
        'assimilation_strength': {
            'name': 'Assimilation Strength',
            'description': 'Strength of shallow water data assimilation',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'assimilation_parameters'
        },
        'observation_frequency': {
            'name': 'Observation Frequency',
            'description': 'Frequency of shallow water observations',
            'unit': 'Hz',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'observation_parameters'
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
    
    'assimilation_maxwell': {
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
        'assimilation_strength': {
            'name': 'Assimilation Strength',
            'description': 'Strength of electromagnetic data assimilation',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'assimilation_parameters'
        },
        'observation_frequency': {
            'name': 'Observation Frequency',
            'description': 'Frequency of electromagnetic observations',
            'unit': 'Hz',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'observation_parameters'
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
    
    'assimilation_helmholtz': {
        'wavenumber': {
            'name': 'Wavenumber (k)',
            'description': 'Wavenumber in Helmholtz equation',
            'unit': '1/m',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'wave_properties'
        },
        'assimilation_strength': {
            'name': 'Assimilation Strength',
            'description': 'Strength of Helmholtz data assimilation',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'assimilation_parameters'
        },
        'observation_frequency': {
            'name': 'Observation Frequency',
            'description': 'Frequency of Helmholtz observations',
            'unit': 'Hz',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'observation_parameters'
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
    
    'assimilation_shm': {
        'natural_frequency': {
            'name': 'Natural Frequency (ω)',
            'description': 'Natural frequency of oscillation',
            'unit': 'rad/s',
            'default': 1.0,
            'range': [0.1, 100.0],
            'category': 'mechanical_properties'
        },
        'assimilation_strength': {
            'name': 'Assimilation Strength',
            'description': 'Strength of SHM data assimilation',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'assimilation_parameters'
        },
        'observation_frequency': {
            'name': 'Observation Frequency',
            'description': 'Frequency of SHM observations',
            'unit': 'Hz',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'observation_parameters'
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
    
    'assimilation_advection_diffusion': {
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
        'assimilation_strength': {
            'name': 'Assimilation Strength',
            'description': 'Strength of advection-diffusion data assimilation',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'assimilation_parameters'
        },
        'observation_frequency': {
            'name': 'Observation Frequency',
            'description': 'Frequency of concentration observations',
            'unit': 'Hz',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'observation_parameters'
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
    
    'assimilation_atmospheric_oceanic': {
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
        'assimilation_strength': {
            'name': 'Assimilation Strength',
            'description': 'Strength of atmospheric/oceanic data assimilation',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'assimilation_parameters'
        },
        'observation_frequency': {
            'name': 'Observation Frequency',
            'description': 'Frequency of atmospheric/oceanic observations',
            'unit': 'Hz',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'observation_parameters'
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
    
    'assimilation_biomechanical_transport': {
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
        'assimilation_strength': {
            'name': 'Assimilation Strength',
            'description': 'Strength of biomechanical transport data assimilation',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'assimilation_parameters'
        },
        'observation_frequency': {
            'name': 'Observation Frequency',
            'description': 'Frequency of biomechanical observations',
            'unit': 'Hz',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'observation_parameters'
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
    
    'assimilation_crystal_plasticity': {
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
        'assimilation_strength': {
            'name': 'Assimilation Strength',
            'description': 'Strength of crystal plasticity data assimilation',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'assimilation_parameters'
        },
        'observation_frequency': {
            'name': 'Observation Frequency',
            'description': 'Frequency of crystal plasticity observations',
            'unit': 'Hz',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'observation_parameters'
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
    
    'assimilation_diffusion_solids': {
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
        'assimilation_strength': {
            'name': 'Assimilation Strength',
            'description': 'Strength of solid diffusion data assimilation',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'assimilation_parameters'
        },
        'observation_frequency': {
            'name': 'Observation Frequency',
            'description': 'Frequency of diffusion observations',
            'unit': 'Hz',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'observation_parameters'
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
    
    'assimilation_elastic_wave': {
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
        'assimilation_strength': {
            'name': 'Assimilation Strength',
            'description': 'Strength of elastic wave data assimilation',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'assimilation_parameters'
        },
        'observation_frequency': {
            'name': 'Observation Frequency',
            'description': 'Frequency of elastic wave observations',
            'unit': 'Hz',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'observation_parameters'
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
    
    'assimilation_electromagnetic_thermal': {
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
        'assimilation_strength': {
            'name': 'Assimilation Strength',
            'description': 'Strength of electromagnetic-thermal data assimilation',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'assimilation_parameters'
        },
        'observation_frequency': {
            'name': 'Observation Frequency',
            'description': 'Frequency of electromagnetic-thermal observations',
            'unit': 'Hz',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'observation_parameters'
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
    
    'assimilation_fluid_structure_interaction': {
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
        'assimilation_strength': {
            'name': 'Assimilation Strength',
            'description': 'Strength of FSI data assimilation',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'assimilation_parameters'
        },
        'observation_frequency': {
            'name': 'Observation Frequency',
            'description': 'Frequency of FSI observations',
            'unit': 'Hz',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'observation_parameters'
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
    
    'assimilation_geophysical_flow': {
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
        'assimilation_strength': {
            'name': 'Assimilation Strength',
            'description': 'Strength of geophysical flow data assimilation',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'assimilation_parameters'
        },
        'observation_frequency': {
            'name': 'Observation Frequency',
            'description': 'Frequency of geophysical flow observations',
            'unit': 'Hz',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'observation_parameters'
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
    
    'assimilation_grain_growth': {
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
        'assimilation_strength': {
            'name': 'Assimilation Strength',
            'description': 'Strength of grain growth data assimilation',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'assimilation_parameters'
        },
        'observation_frequency': {
            'name': 'Observation Frequency',
            'description': 'Frequency of grain growth observations',
            'unit': 'Hz',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'observation_parameters'
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
    
    'assimilation_heat_transfer': {
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
        'assimilation_strength': {
            'name': 'Assimilation Strength',
            'description': 'Strength of heat transfer data assimilation',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'assimilation_parameters'
        },
        'observation_frequency': {
            'name': 'Observation Frequency',
            'description': 'Frequency of temperature observations',
            'unit': 'Hz',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'observation_parameters'
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
    
    'assimilation_laser_heat_source': {
        'laser_power': {
            'name': 'Laser Power (P)',
            'description': 'Laser beam power',
            'unit': 'W',
            'default': 1000.0,
            'range': [1.0, 10000.0],
            'category': 'laser_properties'
        },
        'beam_radius': {
            'name': 'Beam Radius (r)',
            'description': 'Laser beam radius',
            'unit': 'm',
            'default': 1e-3,
            'range': [1e-6, 1e-1],
            'category': 'laser_properties'
        },
        'absorption_coefficient': {
            'name': 'Absorption Coefficient (α)',
            'description': 'Material absorption coefficient',
            'unit': '1/m',
            'default': 1e6,
            'range': [1e3, 1e8],
            'category': 'optical_properties'
        },
        'assimilation_strength': {
            'name': 'Assimilation Strength',
            'description': 'Strength of laser heat source data assimilation',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'assimilation_parameters'
        },
        'observation_frequency': {
            'name': 'Observation Frequency',
            'description': 'Frequency of laser heat observations',
            'unit': 'Hz',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'observation_parameters'
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
    
    'assimilation_magnetohydrodynamics': {
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
        'assimilation_strength': {
            'name': 'Assimilation Strength',
            'description': 'Strength of MHD data assimilation',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'assimilation_parameters'
        },
        'observation_frequency': {
            'name': 'Observation Frequency',
            'description': 'Frequency of MHD observations',
            'unit': 'Hz',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'observation_parameters'
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
    
    'assimilation_melt_pool_dynamics': {
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
        'assimilation_strength': {
            'name': 'Assimilation Strength',
            'description': 'Strength of melt pool data assimilation',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'assimilation_parameters'
        },
        'observation_frequency': {
            'name': 'Observation Frequency',
            'description': 'Frequency of melt pool observations',
            'unit': 'Hz',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'observation_parameters'
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
    
    'assimilation_microstructure_evolution': {
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
        'assimilation_strength': {
            'name': 'Assimilation Strength',
            'description': 'Strength of microstructure data assimilation',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'assimilation_parameters'
        },
        'observation_frequency': {
            'name': 'Observation Frequency',
            'description': 'Frequency of microstructure observations',
            'unit': 'Hz',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'observation_parameters'
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
    
    'assimilation_nuclear_thermal': {
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
        'assimilation_strength': {
            'name': 'Assimilation Strength',
            'description': 'Strength of nuclear thermal data assimilation',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'assimilation_parameters'
        },
        'observation_frequency': {
            'name': 'Observation Frequency',
            'description': 'Frequency of nuclear thermal observations',
            'unit': 'Hz',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'observation_parameters'
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
    
    'assimilation_phase_field_allen_cahn': {
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
        'assimilation_strength': {
            'name': 'Assimilation Strength',
            'description': 'Strength of Allen-Cahn data assimilation',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'assimilation_parameters'
        },
        'observation_frequency': {
            'name': 'Observation Frequency',
            'description': 'Frequency of Allen-Cahn observations',
            'unit': 'Hz',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'observation_parameters'
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
    
    'assimilation_phase_field_cahn_hilliard': {
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
        'assimilation_strength': {
            'name': 'Assimilation Strength',
            'description': 'Strength of Cahn-Hilliard data assimilation',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'assimilation_parameters'
        },
        'observation_frequency': {
            'name': 'Observation Frequency',
            'description': 'Frequency of Cahn-Hilliard observations',
            'unit': 'Hz',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'observation_parameters'
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
    
    'assimilation_precipitation_nucleation': {
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
        'assimilation_strength': {
            'name': 'Assimilation Strength',
            'description': 'Strength of precipitation nucleation data assimilation',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'assimilation_parameters'
        },
        'observation_frequency': {
            'name': 'Observation Frequency',
            'description': 'Frequency of nucleation observations',
            'unit': 'Hz',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'observation_parameters'
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
    
    'assimilation_quantum_mechanical': {
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
        'assimilation_strength': {
            'name': 'Assimilation Strength',
            'description': 'Strength of quantum mechanical data assimilation',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'assimilation_parameters'
        },
        'observation_frequency': {
            'name': 'Observation Frequency',
            'description': 'Frequency of quantum observations',
            'unit': 'Hz',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'observation_parameters'
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
    
    'assimilation_residual_stress': {
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
        'thermal_expansion': {
            'name': 'Thermal Expansion (α)',
            'description': 'Thermal expansion coefficient',
            'unit': '1/K',
            'default': 1e-5,
            'range': [1e-7, 1e-3],
            'category': 'thermal_properties'
        },
        'assimilation_strength': {
            'name': 'Assimilation Strength',
            'description': 'Strength of residual stress data assimilation',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'assimilation_parameters'
        },
        'observation_frequency': {
            'name': 'Observation Frequency',
            'description': 'Frequency of residual stress observations',
            'unit': 'Hz',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'observation_parameters'
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
    
    'assimilation_sintering': {
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
        'assimilation_strength': {
            'name': 'Assimilation Strength',
            'description': 'Strength of sintering data assimilation',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'assimilation_parameters'
        },
        'observation_frequency': {
            'name': 'Observation Frequency',
            'description': 'Frequency of sintering observations',
            'unit': 'Hz',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'observation_parameters'
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
    
    'assimilation_solidification_stefan': {
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
        'assimilation_strength': {
            'name': 'Assimilation Strength',
            'description': 'Strength of Stefan problem data assimilation',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'assimilation_parameters'
        },
        'observation_frequency': {
            'name': 'Observation Frequency',
            'description': 'Frequency of solidification observations',
            'unit': 'Hz',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'observation_parameters'
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
    
    'assimilation_thermoelasticity': {
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
        'assimilation_strength': {
            'name': 'Assimilation Strength',
            'description': 'Strength of thermoelastic data assimilation',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'assimilation_parameters'
        },
        'observation_frequency': {
            'name': 'Observation Frequency',
            'description': 'Frequency of thermoelastic observations',
            'unit': 'Hz',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'observation_parameters'
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