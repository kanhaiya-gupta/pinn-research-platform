"""
Uncertainty Quantification Parameters
Parameters for quantifying and propagating uncertainty in physical systems.
"""

UNCERTAINTY_PARAMETERS_DICT = {
    # Uncertainty Sources
    'parameter_uncertainty': {
        'name': 'Parameter Uncertainty',
        'description': 'Uncertainty in physical parameters',
        'unit': 'dimensionless',
        'default': 0.1,
        'range': [0.0, 1.0],
        'category': 'uncertainty_sources',
        'propagation_method': 'monte_carlo'
    },
    'model_uncertainty': {
        'name': 'Model Uncertainty',
        'description': 'Uncertainty in mathematical model',
        'unit': 'dimensionless',
        'default': 0.05,
        'range': [0.0, 1.0],
        'category': 'uncertainty_sources',
        'propagation_method': 'bayesian'
    },
    'measurement_uncertainty': {
        'name': 'Measurement Uncertainty',
        'description': 'Uncertainty in experimental measurements',
        'unit': 'dimensionless',
        'default': 0.02,
        'range': [0.0, 1.0],
        'category': 'uncertainty_sources',
        'propagation_method': 'statistical'
    },
    'numerical_uncertainty': {
        'name': 'Numerical Uncertainty',
        'description': 'Uncertainty due to numerical discretization',
        'unit': 'dimensionless',
        'default': 0.01,
        'range': [0.0, 1.0],
        'category': 'uncertainty_sources',
        'propagation_method': 'convergence_study'
    },
    
    # Distribution Parameters
    'uncertainty_distribution': {
        'name': 'Uncertainty Distribution',
        'description': 'Probability distribution for uncertainty',
        'unit': 'dimensionless',
        'default': 'normal',
        'range': ['normal', 'uniform', 'lognormal', 'weibull'],
        'category': 'distribution_parameters',
        'propagation_method': 'distribution_based'
    },
    'standard_deviation': {
        'name': 'Standard Deviation',
        'description': 'Standard deviation of uncertainty',
        'unit': 'dimensionless',
        'default': 0.1,
        'range': [0.0, 1.0],
        'category': 'distribution_parameters',
        'propagation_method': 'statistical'
    },
    'coefficient_of_variation': {
        'name': 'Coefficient of Variation',
        'description': 'Coefficient of variation for uncertainty',
        'unit': 'dimensionless',
        'default': 0.1,
        'range': [0.0, 1.0],
        'category': 'distribution_parameters',
        'propagation_method': 'statistical'
    },
    'confidence_interval': {
        'name': 'Confidence Interval',
        'description': 'Confidence interval for uncertainty quantification',
        'unit': 'dimensionless',
        'default': 0.95,
        'range': [0.5, 0.99],
        'category': 'distribution_parameters',
        'propagation_method': 'statistical'
    },
    
    # Monte Carlo Parameters
    'monte_carlo_samples': {
        'name': 'Monte Carlo Samples',
        'description': 'Number of Monte Carlo samples',
        'unit': 'dimensionless',
        'default': 1000,
        'range': [100, 100000],
        'category': 'monte_carlo_parameters',
        'propagation_method': 'monte_carlo'
    },
    'latin_hypercube': {
        'name': 'Latin Hypercube Sampling',
        'description': 'Whether to use Latin hypercube sampling',
        'unit': 'dimensionless',
        'default': True,
        'range': [True, False],
        'category': 'monte_carlo_parameters',
        'propagation_method': 'monte_carlo'
    },
    'sobol_sequences': {
        'name': 'Sobol Sequences',
        'description': 'Whether to use Sobol sequences for sampling',
        'unit': 'dimensionless',
        'default': False,
        'range': [True, False],
        'category': 'monte_carlo_parameters',
        'propagation_method': 'monte_carlo'
    },
    
    # Sensitivity Analysis Parameters
    'sensitivity_method': {
        'name': 'Sensitivity Method',
        'description': 'Method for sensitivity analysis',
        'unit': 'dimensionless',
        'default': 'sobol',
        'range': ['sobol', 'morris', 'fast', 'local'],
        'category': 'sensitivity_parameters',
        'propagation_method': 'sensitivity_analysis'
    },
    'sensitivity_samples': {
        'name': 'Sensitivity Samples',
        'description': 'Number of samples for sensitivity analysis',
        'unit': 'dimensionless',
        'default': 1000,
        'range': [100, 10000],
        'category': 'sensitivity_parameters',
        'propagation_method': 'sensitivity_analysis'
    },
    'total_effect_index': {
        'name': 'Total Effect Index',
        'description': 'Threshold for total effect index',
        'unit': 'dimensionless',
        'default': 0.1,
        'range': [0.0, 1.0],
        'category': 'sensitivity_parameters',
        'propagation_method': 'sensitivity_analysis'
    },
    
    # Bayesian Parameters
    'prior_distribution': {
        'name': 'Prior Distribution',
        'description': 'Prior distribution for Bayesian inference',
        'unit': 'dimensionless',
        'default': 'uniform',
        'range': ['uniform', 'normal', 'lognormal', 'informative'],
        'category': 'bayesian_parameters',
        'propagation_method': 'bayesian'
    },
    'mcmc_samples': {
        'name': 'MCMC Samples',
        'description': 'Number of MCMC samples',
        'unit': 'dimensionless',
        'default': 10000,
        'range': [1000, 100000],
        'category': 'bayesian_parameters',
        'propagation_method': 'bayesian'
    },
    'burn_in_samples': {
        'name': 'Burn-in Samples',
        'description': 'Number of burn-in samples for MCMC',
        'unit': 'dimensionless',
        'default': 1000,
        'range': [100, 10000],
        'category': 'bayesian_parameters',
        'propagation_method': 'bayesian'
    },
    'proposal_variance': {
        'name': 'Proposal Variance',
        'description': 'Variance of proposal distribution for MCMC',
        'unit': 'dimensionless',
        'default': 0.1,
        'range': [0.01, 1.0],
        'category': 'bayesian_parameters',
        'propagation_method': 'bayesian'
    },
    
    # Polynomial Chaos Parameters
    'polynomial_order': {
        'name': 'Polynomial Order',
        'description': 'Order of polynomial chaos expansion',
        'unit': 'dimensionless',
        'default': 3,
        'range': [1, 10],
        'category': 'polynomial_chaos_parameters',
        'propagation_method': 'polynomial_chaos'
    },
    'quadrature_points': {
        'name': 'Quadrature Points',
        'description': 'Number of quadrature points',
        'unit': 'dimensionless',
        'default': 100,
        'range': [10, 1000],
        'category': 'polynomial_chaos_parameters',
        'propagation_method': 'polynomial_chaos'
    },
    'sparse_grid': {
        'name': 'Sparse Grid',
        'description': 'Whether to use sparse grid quadrature',
        'unit': 'dimensionless',
        'default': True,
        'range': [True, False],
        'category': 'polynomial_chaos_parameters',
        'propagation_method': 'polynomial_chaos'
    },
    
    # Reliability Analysis Parameters
    'reliability_method': {
        'name': 'Reliability Method',
        'description': 'Method for reliability analysis',
        'unit': 'dimensionless',
        'default': 'first_order',
        'range': ['first_order', 'second_order', 'monte_carlo'],
        'category': 'reliability_parameters',
        'propagation_method': 'reliability_analysis'
    },
    'failure_probability': {
        'name': 'Failure Probability',
        'description': 'Target failure probability',
        'unit': 'dimensionless',
        'default': 1e-6,
        'range': [1e-12, 1e-3],
        'category': 'reliability_parameters',
        'propagation_method': 'reliability_analysis'
    },
    'safety_factor': {
        'name': 'Safety Factor',
        'description': 'Safety factor for design',
        'unit': 'dimensionless',
        'default': 2.0,
        'range': [1.0, 10.0],
        'category': 'reliability_parameters',
        'propagation_method': 'reliability_analysis'
    },
    
    # Robust Optimization Parameters
    'robustness_weight': {
        'name': 'Robustness Weight',
        'description': 'Weight for robustness in optimization',
        'unit': 'dimensionless',
        'default': 0.5,
        'range': [0.0, 1.0],
        'category': 'robust_optimization_parameters',
        'propagation_method': 'robust_optimization'
    },
    'worst_case_scenario': {
        'name': 'Worst Case Scenario',
        'description': 'Whether to consider worst case scenario',
        'unit': 'dimensionless',
        'default': True,
        'range': [True, False],
        'category': 'robust_optimization_parameters',
        'propagation_method': 'robust_optimization'
    },
    'uncertainty_set': {
        'name': 'Uncertainty Set',
        'description': 'Type of uncertainty set',
        'unit': 'dimensionless',
        'default': 'ellipsoidal',
        'range': ['box', 'ellipsoidal', 'polyhedral'],
        'category': 'robust_optimization_parameters',
        'propagation_method': 'robust_optimization'
    },
    
    # Validation Parameters
    'validation_uncertainty': {
        'name': 'Validation Uncertainty',
        'description': 'Uncertainty in validation data',
        'unit': 'dimensionless',
        'default': 0.05,
        'range': [0.0, 1.0],
        'category': 'validation_parameters',
        'propagation_method': 'validation'
    },
    'calibration_uncertainty': {
        'name': 'Calibration Uncertainty',
        'description': 'Uncertainty in model calibration',
        'unit': 'dimensionless',
        'default': 0.1,
        'range': [0.0, 1.0],
        'category': 'validation_parameters',
        'propagation_method': 'validation'
    },
    
    # Output Parameters
    'uncertainty_visualization': {
        'name': 'Uncertainty Visualization',
        'description': 'Method for uncertainty visualization',
        'unit': 'dimensionless',
        'default': 'confidence_intervals',
        'range': ['confidence_intervals', 'probability_density', 'contour_plots'],
        'category': 'output_parameters',
        'propagation_method': 'visualization'
    },
    'uncertainty_quantiles': {
        'name': 'Uncertainty Quantiles',
        'description': 'Quantiles for uncertainty reporting',
        'unit': 'dimensionless',
        'default': [0.05, 0.5, 0.95],
        'range': [0.0, 1.0],
        'category': 'output_parameters',
        'propagation_method': 'statistical'
    }
}

# Equation-specific parameter mappings for uncertainty quantification
UNCERTAINTY_EQUATION_PARAMETERS = {
    'uncertainty_burgers': {
        'parameter_uncertainty': {
            'name': 'Parameter Uncertainty',
            'description': 'Uncertainty in viscosity and initial conditions',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'uncertainty_sources',
            'propagation_method': 'monte_carlo'
        },
        'viscosity_uncertainty': {
            'name': 'Viscosity Uncertainty',
            'description': 'Uncertainty in dynamic viscosity',
            'unit': 'dimensionless',
            'default': 0.15,
            'range': [0.0, 1.0],
            'category': 'fluid_properties',
            'propagation_method': 'statistical'
        },
        'initial_condition_uncertainty': {
            'name': 'Initial Condition Uncertainty',
            'description': 'Uncertainty in initial velocity field',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'initial_conditions',
            'propagation_method': 'bayesian'
        },
        'monte_carlo_samples': {
            'name': 'Monte Carlo Samples',
            'description': 'Number of Monte Carlo samples',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 100000],
            'category': 'monte_carlo_parameters',
            'propagation_method': 'monte_carlo'
        }
    },
    
    'uncertainty_heat': {
        'thermal_diffusivity_uncertainty': {
            'name': 'Thermal Diffusivity Uncertainty',
            'description': 'Uncertainty in thermal diffusivity',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'thermal_properties',
            'propagation_method': 'statistical'
        },
        'boundary_condition_uncertainty': {
            'name': 'Boundary Condition Uncertainty',
            'description': 'Uncertainty in boundary conditions',
            'unit': 'dimensionless',
            'default': 0.05,
            'range': [0.0, 1.0],
            'category': 'boundary_conditions',
            'propagation_method': 'bayesian'
        },
        'monte_carlo_samples': {
            'name': 'Monte Carlo Samples',
            'description': 'Number of Monte Carlo samples',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 100000],
            'category': 'monte_carlo_parameters',
            'propagation_method': 'monte_carlo'
        }
    },
    
    'uncertainty_wave': {
        'wave_speed_uncertainty': {
            'name': 'Wave Speed Uncertainty',
            'description': 'Uncertainty in wave speed',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'wave_properties',
            'propagation_method': 'statistical'
        },
        'initial_condition_uncertainty': {
            'name': 'Initial Condition Uncertainty',
            'description': 'Uncertainty in initial wave field',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'initial_conditions',
            'propagation_method': 'bayesian'
        },
        'monte_carlo_samples': {
            'name': 'Monte Carlo Samples',
            'description': 'Number of Monte Carlo samples',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 100000],
            'category': 'monte_carlo_parameters',
            'propagation_method': 'monte_carlo'
        }
    },
    
    'uncertainty_shm': {
        'frequency_uncertainty': {
            'name': 'Frequency Uncertainty',
            'description': 'Uncertainty in natural frequency',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'mechanical_properties',
            'propagation_method': 'statistical'
        },
        'damping_uncertainty': {
            'name': 'Damping Uncertainty',
            'description': 'Uncertainty in damping ratio',
            'unit': 'dimensionless',
            'default': 0.15,
            'range': [0.0, 1.0],
            'category': 'mechanical_properties',
            'propagation_method': 'statistical'
        },
        'monte_carlo_samples': {
            'name': 'Monte Carlo Samples',
            'description': 'Number of Monte Carlo samples',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 100000],
            'category': 'monte_carlo_parameters',
            'propagation_method': 'monte_carlo'
        }
    },
    
    'uncertainty_helmholtz': {
        'wavenumber_uncertainty': {
            'name': 'Wavenumber Uncertainty',
            'description': 'Uncertainty in wavenumber',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'wave_properties',
            'propagation_method': 'statistical'
        },
        'boundary_condition_uncertainty': {
            'name': 'Boundary Condition Uncertainty',
            'description': 'Uncertainty in boundary conditions',
            'unit': 'dimensionless',
            'default': 0.05,
            'range': [0.0, 1.0],
            'category': 'boundary_conditions',
            'propagation_method': 'bayesian'
        },
        'monte_carlo_samples': {
            'name': 'Monte Carlo Samples',
            'description': 'Number of Monte Carlo samples',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 100000],
            'category': 'monte_carlo_parameters',
            'propagation_method': 'monte_carlo'
        }
    },
    
    'uncertainty_navier_stokes': {
        'viscosity_uncertainty': {
            'name': 'Viscosity Uncertainty',
            'description': 'Uncertainty in dynamic viscosity',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'fluid_properties',
            'propagation_method': 'statistical'
        },
        'boundary_condition_uncertainty': {
            'name': 'Boundary Condition Uncertainty',
            'description': 'Uncertainty in boundary conditions',
            'unit': 'dimensionless',
            'default': 0.05,
            'range': [0.0, 1.0],
            'category': 'boundary_conditions',
            'propagation_method': 'bayesian'
        },
        'monte_carlo_samples': {
            'name': 'Monte Carlo Samples',
            'description': 'Number of Monte Carlo samples',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 100000],
            'category': 'monte_carlo_parameters',
            'propagation_method': 'monte_carlo'
        }
    },
    
    'uncertainty_schrodinger': {
        'potential_uncertainty': {
            'name': 'Potential Uncertainty',
            'description': 'Uncertainty in potential energy',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'quantum_properties',
            'propagation_method': 'statistical'
        },
        'initial_state_uncertainty': {
            'name': 'Initial State Uncertainty',
            'description': 'Uncertainty in initial wave function',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'quantum_properties',
            'propagation_method': 'bayesian'
        },
        'monte_carlo_samples': {
            'name': 'Monte Carlo Samples',
            'description': 'Number of Monte Carlo samples',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 100000],
            'category': 'monte_carlo_parameters',
            'propagation_method': 'monte_carlo'
        }
    },
    
    'uncertainty_maxwell': {
        'electromagnetic_uncertainty': {
            'name': 'Electromagnetic Uncertainty',
            'description': 'Uncertainty in electromagnetic properties',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'electromagnetic_properties',
            'propagation_method': 'statistical'
        },
        'monte_carlo_samples': {
            'name': 'Monte Carlo Samples',
            'description': 'Number of Monte Carlo samples',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 100000],
            'category': 'monte_carlo_parameters',
            'propagation_method': 'monte_carlo'
        }
    },
    
    'uncertainty_heat_transfer': {
        'thermal_property_uncertainty': {
            'name': 'Thermal Property Uncertainty',
            'description': 'Uncertainty in thermal conductivity and heat capacity',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'thermal_properties',
            'propagation_method': 'statistical'
        },
        'monte_carlo_samples': {
            'name': 'Monte Carlo Samples',
            'description': 'Number of Monte Carlo samples',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 100000],
            'category': 'monte_carlo_parameters',
            'propagation_method': 'monte_carlo'
        }
    },
    
    'uncertainty_elastic': {
        'elastic_modulus_uncertainty': {
            'name': 'Elastic Modulus Uncertainty',
            'description': 'Uncertainty in elastic moduli',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'mechanical_properties',
            'propagation_method': 'statistical'
        },
        'monte_carlo_samples': {
            'name': 'Monte Carlo Samples',
            'description': 'Number of Monte Carlo samples',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 100000],
            'category': 'monte_carlo_parameters',
            'propagation_method': 'monte_carlo'
        }
    },
    
    'uncertainty_phase_field': {
        'mobility_uncertainty': {
            'name': 'Mobility Uncertainty',
            'description': 'Uncertainty in phase field mobility',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'phase_field_properties',
            'propagation_method': 'statistical'
        },
        'free_energy_uncertainty': {
            'name': 'Free Energy Uncertainty',
            'description': 'Uncertainty in free energy functional',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'phase_field_properties',
            'propagation_method': 'statistical'
        },
        'monte_carlo_samples': {
            'name': 'Monte Carlo Samples',
            'description': 'Number of Monte Carlo samples',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 100000],
            'category': 'monte_carlo_parameters',
            'propagation_method': 'monte_carlo'
        }
    },
    
    'uncertainty_reaction_diffusion': {
        'diffusion_uncertainty': {
            'name': 'Diffusion Uncertainty',
            'description': 'Uncertainty in diffusion coefficient',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'transport_properties',
            'propagation_method': 'statistical'
        },
        'reaction_uncertainty': {
            'name': 'Reaction Uncertainty',
            'description': 'Uncertainty in reaction function',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'chemical_properties',
            'propagation_method': 'statistical'
        },
        'monte_carlo_samples': {
            'name': 'Monte Carlo Samples',
            'description': 'Number of Monte Carlo samples',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 100000],
            'category': 'monte_carlo_parameters',
            'propagation_method': 'monte_carlo'
        }
    },
    
    'uncertainty_poroelasticity': {
        'permeability_uncertainty': {
            'name': 'Permeability Uncertainty',
            'description': 'Uncertainty in permeability',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'poroelastic_properties',
            'propagation_method': 'statistical'
        },
        'elastic_modulus_uncertainty': {
            'name': 'Elastic Modulus Uncertainty',
            'description': 'Uncertainty in elastic moduli',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'mechanical_properties',
            'propagation_method': 'statistical'
        },
        'monte_carlo_samples': {
            'name': 'Monte Carlo Samples',
            'description': 'Number of Monte Carlo samples',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 100000],
            'category': 'monte_carlo_parameters',
            'propagation_method': 'monte_carlo'
        }
    },
    
    'uncertainty_viscoelasticity': {
        'elastic_modulus_uncertainty': {
            'name': 'Elastic Modulus Uncertainty',
            'description': 'Uncertainty in elastic modulus',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'mechanical_properties',
            'propagation_method': 'statistical'
        },
        'relaxation_time_uncertainty': {
            'name': 'Relaxation Time Uncertainty',
            'description': 'Uncertainty in relaxation time',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'viscoelastic_properties',
            'propagation_method': 'statistical'
        },
        'monte_carlo_samples': {
            'name': 'Monte Carlo Samples',
            'description': 'Number of Monte Carlo samples',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 100000],
            'category': 'monte_carlo_parameters',
            'propagation_method': 'monte_carlo'
        }
    },
    
    'uncertainty_radiative_transfer': {
        'optical_property_uncertainty': {
            'name': 'Optical Property Uncertainty',
            'description': 'Uncertainty in absorption and scattering coefficients',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'radiation_properties',
            'propagation_method': 'statistical'
        },
        'monte_carlo_samples': {
            'name': 'Monte Carlo Samples',
            'description': 'Number of Monte Carlo samples',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 100000],
            'category': 'monte_carlo_parameters',
            'propagation_method': 'monte_carlo'
        }
    },
    
    'uncertainty_shallow_water': {
        'bathymetry_uncertainty': {
            'name': 'Bathymetry Uncertainty',
            'description': 'Uncertainty in bottom topography',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'geometric_parameters',
            'propagation_method': 'statistical'
        },
        'friction_uncertainty': {
            'name': 'Friction Uncertainty',
            'description': 'Uncertainty in friction coefficient',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'geophysical_properties',
            'propagation_method': 'statistical'
        },
        'monte_carlo_samples': {
            'name': 'Monte Carlo Samples',
            'description': 'Number of Monte Carlo samples',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 100000],
            'category': 'monte_carlo_parameters',
            'propagation_method': 'monte_carlo'
        }
    },
    
    'uncertainty_magnetohydrodynamics': {
        'plasma_parameter_uncertainty': {
            'name': 'Plasma Parameter Uncertainty',
            'description': 'Uncertainty in plasma parameters',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'plasma_properties',
            'propagation_method': 'statistical'
        },
        'monte_carlo_samples': {
            'name': 'Monte Carlo Samples',
            'description': 'Number of Monte Carlo samples',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 100000],
            'category': 'monte_carlo_parameters',
            'propagation_method': 'monte_carlo'
        }
    },
    
    'uncertainty_thermoelasticity': {
        'coupled_parameter_uncertainty': {
            'name': 'Coupled Parameter Uncertainty',
            'description': 'Uncertainty in thermoelastic coupling parameters',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'thermoelastic_properties',
            'propagation_method': 'statistical'
        },
        'monte_carlo_samples': {
            'name': 'Monte Carlo Samples',
            'description': 'Number of Monte Carlo samples',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 100000],
            'category': 'monte_carlo_parameters',
            'propagation_method': 'monte_carlo'
        }
    },
    
    'uncertainty_advection_diffusion': {
        'velocity_uncertainty': {
            'name': 'Velocity Uncertainty',
            'description': 'Uncertainty in velocity field',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'transport_properties',
            'propagation_method': 'statistical'
        },
        'diffusivity_uncertainty': {
            'name': 'Diffusivity Uncertainty',
            'description': 'Uncertainty in diffusion coefficient',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'transport_properties',
            'propagation_method': 'statistical'
        },
        'monte_carlo_samples': {
            'name': 'Monte Carlo Samples',
            'description': 'Number of Monte Carlo samples',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 100000],
            'category': 'monte_carlo_parameters',
            'propagation_method': 'monte_carlo'
        }
    },
    
    'uncertainty_elastic_wave': {
        'elastic_modulus_uncertainty': {
            'name': 'Elastic Modulus Uncertainty',
            'description': 'Uncertainty in elastic moduli',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'mechanical_properties',
            'propagation_method': 'statistical'
        },
        'monte_carlo_samples': {
            'name': 'Monte Carlo Samples',
            'description': 'Number of Monte Carlo samples',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 100000],
            'category': 'monte_carlo_parameters',
            'propagation_method': 'monte_carlo'
        }
    },
    
    'uncertainty_fluid_structure_interaction': {
        'fsi_parameter_uncertainty': {
            'name': 'FSI Parameter Uncertainty',
            'description': 'Uncertainty in fluid-structure interaction parameters',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'coupling_parameters',
            'propagation_method': 'statistical'
        },
        'monte_carlo_samples': {
            'name': 'Monte Carlo Samples',
            'description': 'Number of Monte Carlo samples',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 100000],
            'category': 'monte_carlo_parameters',
            'propagation_method': 'monte_carlo'
        }
    },
    
    'uncertainty_electromagnetic_thermal': {
        'em_thermal_parameter_uncertainty': {
            'name': 'EM-Thermal Parameter Uncertainty',
            'description': 'Uncertainty in electromagnetic-thermal coupling parameters',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'coupling_parameters',
            'propagation_method': 'statistical'
        },
        'monte_carlo_samples': {
            'name': 'Monte Carlo Samples',
            'description': 'Number of Monte Carlo samples',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 100000],
            'category': 'monte_carlo_parameters',
            'propagation_method': 'monte_carlo'
        }
    },
    
    'uncertainty_biomechanical_transport': {
        'biological_parameter_uncertainty': {
            'name': 'Biological Parameter Uncertainty',
            'description': 'Uncertainty in biological parameters',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'biological_properties',
            'propagation_method': 'statistical'
        },
        'monte_carlo_samples': {
            'name': 'Monte Carlo Samples',
            'description': 'Number of Monte Carlo samples',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 100000],
            'category': 'monte_carlo_parameters',
            'propagation_method': 'monte_carlo'
        }
    },
    
    'uncertainty_geophysical_flow': {
        'geophysical_parameter_uncertainty': {
            'name': 'Geophysical Parameter Uncertainty',
            'description': 'Uncertainty in geophysical parameters',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'geophysical_properties',
            'propagation_method': 'statistical'
        },
        'monte_carlo_samples': {
            'name': 'Monte Carlo Samples',
            'description': 'Number of Monte Carlo samples',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 100000],
            'category': 'monte_carlo_parameters',
            'propagation_method': 'monte_carlo'
        }
    },
    
    'uncertainty_atmospheric_oceanic': {
        'atmospheric_oceanic_parameter_uncertainty': {
            'name': 'Atmospheric-Oceanic Parameter Uncertainty',
            'description': 'Uncertainty in atmospheric-oceanic coupling parameters',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'coupling_parameters',
            'propagation_method': 'statistical'
        },
        'monte_carlo_samples': {
            'name': 'Monte Carlo Samples',
            'description': 'Number of Monte Carlo samples',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 100000],
            'category': 'monte_carlo_parameters',
            'propagation_method': 'monte_carlo'
        }
    },
    
    'uncertainty_nuclear_thermal': {
        'nuclear_parameter_uncertainty': {
            'name': 'Nuclear Parameter Uncertainty',
            'description': 'Uncertainty in nuclear parameters',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'nuclear_properties',
            'propagation_method': 'statistical'
        },
        'monte_carlo_samples': {
            'name': 'Monte Carlo Samples',
            'description': 'Number of Monte Carlo samples',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 100000],
            'category': 'monte_carlo_parameters',
            'propagation_method': 'monte_carlo'
        }
    },
    
    'uncertainty_quantum_mechanical': {
        'quantum_parameter_uncertainty': {
            'name': 'Quantum Parameter Uncertainty',
            'description': 'Uncertainty in quantum mechanical parameters',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'quantum_properties',
            'propagation_method': 'statistical'
        },
        'monte_carlo_samples': {
            'name': 'Monte Carlo Samples',
            'description': 'Number of Monte Carlo samples',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 100000],
            'category': 'monte_carlo_parameters',
            'propagation_method': 'monte_carlo'
        }
    },
    
    'uncertainty_phase_field_allen_cahn': {
        'allen_cahn_parameter_uncertainty': {
            'name': 'Allen-Cahn Parameter Uncertainty',
            'description': 'Uncertainty in Allen-Cahn equation parameters',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'phase_field_properties',
            'propagation_method': 'statistical'
        },
        'monte_carlo_samples': {
            'name': 'Monte Carlo Samples',
            'description': 'Number of Monte Carlo samples',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 100000],
            'category': 'monte_carlo_parameters',
            'propagation_method': 'monte_carlo'
        }
    },
    
    'uncertainty_phase_field_cahn_hilliard': {
        'cahn_hilliard_parameter_uncertainty': {
            'name': 'Cahn-Hilliard Parameter Uncertainty',
            'description': 'Uncertainty in Cahn-Hilliard equation parameters',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'phase_field_properties',
            'propagation_method': 'statistical'
        },
        'monte_carlo_samples': {
            'name': 'Monte Carlo Samples',
            'description': 'Number of Monte Carlo samples',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 100000],
            'category': 'monte_carlo_parameters',
            'propagation_method': 'monte_carlo'
        }
    },
    
    'uncertainty_solidification_stefan': {
        'stefan_parameter_uncertainty': {
            'name': 'Stefan Parameter Uncertainty',
            'description': 'Uncertainty in Stefan solidification parameters',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'thermal_properties',
            'propagation_method': 'statistical'
        },
        'monte_carlo_samples': {
            'name': 'Monte Carlo Samples',
            'description': 'Number of Monte Carlo samples',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 100000],
            'category': 'monte_carlo_parameters',
            'propagation_method': 'monte_carlo'
        }
    },
    
    'uncertainty_grain_growth': {
        'grain_growth_parameter_uncertainty': {
            'name': 'Grain Growth Parameter Uncertainty',
            'description': 'Uncertainty in grain growth parameters',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'material_properties',
            'propagation_method': 'statistical'
        },
        'monte_carlo_samples': {
            'name': 'Monte Carlo Samples',
            'description': 'Number of Monte Carlo samples',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 100000],
            'category': 'monte_carlo_parameters',
            'propagation_method': 'monte_carlo'
        }
    },
    
    'uncertainty_sintering': {
        'sintering_parameter_uncertainty': {
            'name': 'Sintering Parameter Uncertainty',
            'description': 'Uncertainty in sintering parameters',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'material_properties',
            'propagation_method': 'statistical'
        },
        'monte_carlo_samples': {
            'name': 'Monte Carlo Samples',
            'description': 'Number of Monte Carlo samples',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 100000],
            'category': 'monte_carlo_parameters',
            'propagation_method': 'monte_carlo'
        }
    },
    
    'uncertainty_laser_heat_source': {
        'laser_parameter_uncertainty': {
            'name': 'Laser Parameter Uncertainty',
            'description': 'Uncertainty in laser heat source parameters',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'am_properties',
            'propagation_method': 'statistical'
        },
        'monte_carlo_samples': {
            'name': 'Monte Carlo Samples',
            'description': 'Number of Monte Carlo samples',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 100000],
            'category': 'monte_carlo_parameters',
            'propagation_method': 'monte_carlo'
        }
    },
    
    'uncertainty_melt_pool_dynamics': {
        'melt_pool_parameter_uncertainty': {
            'name': 'Melt Pool Parameter Uncertainty',
            'description': 'Uncertainty in melt pool dynamics parameters',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'am_properties',
            'propagation_method': 'statistical'
        },
        'monte_carlo_samples': {
            'name': 'Monte Carlo Samples',
            'description': 'Number of Monte Carlo samples',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 100000],
            'category': 'monte_carlo_parameters',
            'propagation_method': 'monte_carlo'
        }
    },
    
    'uncertainty_crystal_plasticity': {
        'plasticity_parameter_uncertainty': {
            'name': 'Plasticity Parameter Uncertainty',
            'description': 'Uncertainty in crystal plasticity parameters',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'mechanical_properties',
            'propagation_method': 'statistical'
        },
        'monte_carlo_samples': {
            'name': 'Monte Carlo Samples',
            'description': 'Number of Monte Carlo samples',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 100000],
            'category': 'monte_carlo_parameters',
            'propagation_method': 'monte_carlo'
        }
    },
    
    'uncertainty_diffusion_solids': {
        'solid_diffusion_parameter_uncertainty': {
            'name': 'Solid Diffusion Parameter Uncertainty',
            'description': 'Uncertainty in solid diffusion parameters',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'transport_properties',
            'propagation_method': 'statistical'
        },
        'monte_carlo_samples': {
            'name': 'Monte Carlo Samples',
            'description': 'Number of Monte Carlo samples',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 100000],
            'category': 'monte_carlo_parameters',
            'propagation_method': 'monte_carlo'
        }
    },
    
    'uncertainty_precipitation_nucleation': {
        'precipitation_parameter_uncertainty': {
            'name': 'Precipitation Parameter Uncertainty',
            'description': 'Uncertainty in precipitation nucleation parameters',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'kinetic_properties',
            'propagation_method': 'statistical'
        },
        'monte_carlo_samples': {
            'name': 'Monte Carlo Samples',
            'description': 'Number of Monte Carlo samples',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 100000],
            'category': 'monte_carlo_parameters',
            'propagation_method': 'monte_carlo'
        }
    },
    
    'uncertainty_residual_stress': {
        'residual_stress_parameter_uncertainty': {
            'name': 'Residual Stress Parameter Uncertainty',
            'description': 'Uncertainty in residual stress parameters',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'mechanical_properties',
            'propagation_method': 'statistical'
        },
        'monte_carlo_samples': {
            'name': 'Monte Carlo Samples',
            'description': 'Number of Monte Carlo samples',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 100000],
            'category': 'monte_carlo_parameters',
            'propagation_method': 'monte_carlo'
        }
    },
    
    'uncertainty_microstructure_evolution': {
        'microstructure_parameter_uncertainty': {
            'name': 'Microstructure Parameter Uncertainty',
            'description': 'Uncertainty in microstructure evolution parameters',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'kinetic_properties',
            'propagation_method': 'statistical'
        },
        'monte_carlo_samples': {
            'name': 'Monte Carlo Samples',
            'description': 'Number of Monte Carlo samples',
            'unit': 'dimensionless',
            'default': 1000,
            'range': [100, 100000],
            'category': 'monte_carlo_parameters',
            'propagation_method': 'monte_carlo'
        }
    }
}