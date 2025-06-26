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

# Equation-specific parameters for uncertainty quantification
UNCERTAINTY_EQUATION_PARAMETERS = {
    'uncertainty_burgers': {
        'viscosity_uncertainty': {'default': 0.1, 'range': [0.0, 0.5]},
        'initial_condition_uncertainty': {'default': 0.05, 'range': [0.0, 0.3]},
        'boundary_condition_uncertainty': {'default': 0.02, 'range': [0.0, 0.2]},
        'monte_carlo_samples': {'default': 1000, 'range': [100, 10000]},
        'uncertainty_distribution': {'default': 'normal', 'range': ['normal', 'uniform', 'lognormal']}
    },
    'uncertainty_heat': {
        'thermal_diffusivity_uncertainty': {'default': 0.15, 'range': [0.0, 0.5]},
        'boundary_condition_uncertainty': {'default': 0.03, 'range': [0.0, 0.2]},
        'initial_temperature_uncertainty': {'default': 0.05, 'range': [0.0, 0.3]},
        'monte_carlo_samples': {'default': 1000, 'range': [100, 10000]},
        'uncertainty_distribution': {'default': 'normal', 'range': ['normal', 'uniform', 'lognormal']}
    },
    'uncertainty_wave': {
        'wave_speed_uncertainty': {'default': 0.1, 'range': [0.0, 0.4]},
        'initial_condition_uncertainty': {'default': 0.05, 'range': [0.0, 0.3]},
        'boundary_condition_uncertainty': {'default': 0.02, 'range': [0.0, 0.2]},
        'monte_carlo_samples': {'default': 1000, 'range': [100, 10000]},
        'uncertainty_distribution': {'default': 'normal', 'range': ['normal', 'uniform', 'lognormal']}
    },
    'uncertainty_shm': {
        'frequency_uncertainty': {'default': 0.08, 'range': [0.0, 0.3]},
        'damping_uncertainty': {'default': 0.12, 'range': [0.0, 0.4]},
        'initial_amplitude_uncertainty': {'default': 0.05, 'range': [0.0, 0.3]},
        'monte_carlo_samples': {'default': 1000, 'range': [100, 10000]},
        'uncertainty_distribution': {'default': 'normal', 'range': ['normal', 'uniform', 'lognormal']}
    },
    'uncertainty_helmholtz': {
        'wavenumber_uncertainty': {'default': 0.1, 'range': [0.0, 0.4]},
        'boundary_condition_uncertainty': {'default': 0.03, 'range': [0.0, 0.2]},
        'medium_property_uncertainty': {'default': 0.08, 'range': [0.0, 0.3]},
        'monte_carlo_samples': {'default': 1000, 'range': [100, 10000]},
        'uncertainty_distribution': {'default': 'normal', 'range': ['normal', 'uniform', 'lognormal']}
    },
    'uncertainty_navier_stokes': {
        'viscosity_uncertainty': {'default': 0.15, 'range': [0.0, 0.5]},
        'density_uncertainty': {'default': 0.05, 'range': [0.0, 0.2]},
        'boundary_condition_uncertainty': {'default': 0.03, 'range': [0.0, 0.2]},
        'monte_carlo_samples': {'default': 2000, 'range': [500, 20000]},
        'uncertainty_distribution': {'default': 'normal', 'range': ['normal', 'uniform', 'lognormal']}
    },
    'uncertainty_schrodinger': {
        'potential_uncertainty': {'default': 0.1, 'range': [0.0, 0.4]},
        'initial_state_uncertainty': {'default': 0.05, 'range': [0.0, 0.3]},
        'hamiltonian_uncertainty': {'default': 0.08, 'range': [0.0, 0.3]},
        'monte_carlo_samples': {'default': 1000, 'range': [100, 10000]},
        'uncertainty_distribution': {'default': 'normal', 'range': ['normal', 'uniform', 'lognormal']}
    },
    'uncertainty_maxwell': {
        'permittivity_uncertainty': {'default': 0.1, 'range': [0.0, 0.4]},
        'permeability_uncertainty': {'default': 0.08, 'range': [0.0, 0.3]},
        'boundary_condition_uncertainty': {'default': 0.03, 'range': [0.0, 0.2]},
        'monte_carlo_samples': {'default': 1000, 'range': [100, 10000]},
        'uncertainty_distribution': {'default': 'normal', 'range': ['normal', 'uniform', 'lognormal']}
    },
    'uncertainty_heat_transfer': {
        'thermal_conductivity_uncertainty': {'default': 0.12, 'range': [0.0, 0.4]},
        'heat_capacity_uncertainty': {'default': 0.08, 'range': [0.0, 0.3]},
        'heat_source_uncertainty': {'default': 0.05, 'range': [0.0, 0.2]},
        'monte_carlo_samples': {'default': 1000, 'range': [100, 10000]},
        'uncertainty_distribution': {'default': 'normal', 'range': ['normal', 'uniform', 'lognormal']}
    },
    'uncertainty_elastic': {
        'elastic_modulus_uncertainty': {'default': 0.15, 'range': [0.0, 0.5]},
        'poisson_ratio_uncertainty': {'default': 0.1, 'range': [0.0, 0.3]},
        'boundary_condition_uncertainty': {'default': 0.03, 'range': [0.0, 0.2]},
        'monte_carlo_samples': {'default': 1000, 'range': [100, 10000]},
        'uncertainty_distribution': {'default': 'normal', 'range': ['normal', 'uniform', 'lognormal']}
    },
    'uncertainty_phase_field': {
        'mobility_uncertainty': {'default': 0.1, 'range': [0.0, 0.4]},
        'free_energy_uncertainty': {'default': 0.08, 'range': [0.0, 0.3]},
        'interface_thickness_uncertainty': {'default': 0.05, 'range': [0.0, 0.2]},
        'monte_carlo_samples': {'default': 1000, 'range': [100, 10000]},
        'uncertainty_distribution': {'default': 'normal', 'range': ['normal', 'uniform', 'lognormal']}
    },
    'uncertainty_reaction_diffusion': {
        'diffusion_coefficient_uncertainty': {'default': 0.12, 'range': [0.0, 0.4]},
        'reaction_rate_uncertainty': {'default': 0.15, 'range': [0.0, 0.5]},
        'initial_concentration_uncertainty': {'default': 0.05, 'range': [0.0, 0.3]},
        'monte_carlo_samples': {'default': 1000, 'range': [100, 10000]},
        'uncertainty_distribution': {'default': 'normal', 'range': ['normal', 'uniform', 'lognormal']}
    },
    'uncertainty_poroelasticity': {
        'permeability_uncertainty': {'default': 0.2, 'range': [0.0, 0.6]},
        'elastic_modulus_uncertainty': {'default': 0.15, 'range': [0.0, 0.5]},
        'fluid_viscosity_uncertainty': {'default': 0.1, 'range': [0.0, 0.4]},
        'monte_carlo_samples': {'default': 1500, 'range': [500, 15000]},
        'uncertainty_distribution': {'default': 'normal', 'range': ['normal', 'uniform', 'lognormal']}
    },
    'uncertainty_viscoelasticity': {
        'elastic_modulus_uncertainty': {'default': 0.15, 'range': [0.0, 0.5]},
        'relaxation_time_uncertainty': {'default': 0.2, 'range': [0.0, 0.6]},
        'viscosity_uncertainty': {'default': 0.12, 'range': [0.0, 0.4]},
        'monte_carlo_samples': {'default': 1000, 'range': [100, 10000]},
        'uncertainty_distribution': {'default': 'normal', 'range': ['normal', 'uniform', 'lognormal']}
    },
    'uncertainty_radiative_transfer': {
        'absorption_coefficient_uncertainty': {'default': 0.15, 'range': [0.0, 0.5]},
        'scattering_coefficient_uncertainty': {'default': 0.12, 'range': [0.0, 0.4]},
        'phase_function_uncertainty': {'default': 0.08, 'range': [0.0, 0.3]},
        'monte_carlo_samples': {'default': 2000, 'range': [500, 20000]},
        'uncertainty_distribution': {'default': 'normal', 'range': ['normal', 'uniform', 'lognormal']}
    },
    'uncertainty_shallow_water': {
        'bathymetry_uncertainty': {'default': 0.1, 'range': [0.0, 0.4]},
        'friction_coefficient_uncertainty': {'default': 0.15, 'range': [0.0, 0.5]},
        'initial_condition_uncertainty': {'default': 0.05, 'range': [0.0, 0.3]},
        'monte_carlo_samples': {'default': 1500, 'range': [500, 15000]},
        'uncertainty_distribution': {'default': 'normal', 'range': ['normal', 'uniform', 'lognormal']}
    },
    'uncertainty_magnetohydrodynamics': {
        'plasma_density_uncertainty': {'default': 0.15, 'range': [0.0, 0.5]},
        'magnetic_field_uncertainty': {'default': 0.1, 'range': [0.0, 0.4]},
        'temperature_uncertainty': {'default': 0.12, 'range': [0.0, 0.4]},
        'monte_carlo_samples': {'default': 2000, 'range': [500, 20000]},
        'uncertainty_distribution': {'default': 'normal', 'range': ['normal', 'uniform', 'lognormal']}
    },
    'uncertainty_thermoelasticity': {
        'thermal_expansion_uncertainty': {'default': 0.15, 'range': [0.0, 0.5]},
        'elastic_modulus_uncertainty': {'default': 0.12, 'range': [0.0, 0.4]},
        'thermal_conductivity_uncertainty': {'default': 0.1, 'range': [0.0, 0.4]},
        'monte_carlo_samples': {'default': 1500, 'range': [500, 15000]},
        'uncertainty_distribution': {'default': 'normal', 'range': ['normal', 'uniform', 'lognormal']}
    },
    'uncertainty_advection_diffusion': {
        'velocity_uncertainty': {'default': 0.12, 'range': [0.0, 0.4]},
        'diffusion_coefficient_uncertainty': {'default': 0.1, 'range': [0.0, 0.4]},
        'initial_concentration_uncertainty': {'default': 0.05, 'range': [0.0, 0.3]},
        'monte_carlo_samples': {'default': 1000, 'range': [100, 10000]},
        'uncertainty_distribution': {'default': 'normal', 'range': ['normal', 'uniform', 'lognormal']}
    },
    'uncertainty_elastic_wave': {
        'elastic_modulus_uncertainty': {'default': 0.15, 'range': [0.0, 0.5]},
        'density_uncertainty': {'default': 0.08, 'range': [0.0, 0.3]},
        'damping_uncertainty': {'default': 0.1, 'range': [0.0, 0.4]},
        'monte_carlo_samples': {'default': 1000, 'range': [100, 10000]},
        'uncertainty_distribution': {'default': 'normal', 'range': ['normal', 'uniform', 'lognormal']}
    },
    'uncertainty_fluid_structure_interaction': {
        'fluid_viscosity_uncertainty': {'default': 0.15, 'range': [0.0, 0.5]},
        'elastic_modulus_uncertainty': {'default': 0.12, 'range': [0.0, 0.4]},
        'coupling_parameter_uncertainty': {'default': 0.1, 'range': [0.0, 0.4]},
        'monte_carlo_samples': {'default': 2000, 'range': [500, 20000]},
        'uncertainty_distribution': {'default': 'normal', 'range': ['normal', 'uniform', 'lognormal']}
    },
    'uncertainty_electromagnetic_thermal': {
        'electromagnetic_property_uncertainty': {'default': 0.1, 'range': [0.0, 0.4]},
        'thermal_property_uncertainty': {'default': 0.12, 'range': [0.0, 0.4]},
        'coupling_coefficient_uncertainty': {'default': 0.08, 'range': [0.0, 0.3]},
        'monte_carlo_samples': {'default': 1500, 'range': [500, 15000]},
        'uncertainty_distribution': {'default': 'normal', 'range': ['normal', 'uniform', 'lognormal']}
    },
    'uncertainty_biomechanical_transport': {
        'elastic_modulus_uncertainty': {'default': 0.2, 'range': [0.0, 0.6]},
        'diffusion_coefficient_uncertainty': {'default': 0.15, 'range': [0.0, 0.5]},
        'biological_parameter_uncertainty': {'default': 0.25, 'range': [0.0, 0.7]},
        'monte_carlo_samples': {'default': 1500, 'range': [500, 15000]},
        'uncertainty_distribution': {'default': 'normal', 'range': ['normal', 'uniform', 'lognormal']}
    },
    'uncertainty_geophysical_flow': {
        'coriolis_parameter_uncertainty': {'default': 0.05, 'range': [0.0, 0.2]},
        'friction_parameter_uncertainty': {'default': 0.15, 'range': [0.0, 0.5]},
        'topography_uncertainty': {'default': 0.1, 'range': [0.0, 0.4]},
        'monte_carlo_samples': {'default': 2000, 'range': [500, 20000]},
        'uncertainty_distribution': {'default': 'normal', 'range': ['normal', 'uniform', 'lognormal']}
    },
    'uncertainty_atmospheric_oceanic': {
        'atmospheric_parameter_uncertainty': {'default': 0.15, 'range': [0.0, 0.5]},
        'oceanic_parameter_uncertainty': {'default': 0.12, 'range': [0.0, 0.4]},
        'coupling_parameter_uncertainty': {'default': 0.1, 'range': [0.0, 0.4]},
        'monte_carlo_samples': {'default': 3000, 'range': [1000, 30000]},
        'uncertainty_distribution': {'default': 'normal', 'range': ['normal', 'uniform', 'lognormal']}
    },
    'uncertainty_nuclear_thermal': {
        'nuclear_cross_section_uncertainty': {'default': 0.2, 'range': [0.0, 0.6]},
        'thermal_property_uncertainty': {'default': 0.12, 'range': [0.0, 0.4]},
        'neutron_flux_uncertainty': {'default': 0.15, 'range': [0.0, 0.5]},
        'monte_carlo_samples': {'default': 2000, 'range': [500, 20000]},
        'uncertainty_distribution': {'default': 'normal', 'range': ['normal', 'uniform', 'lognormal']}
    },
    'uncertainty_quantum_mechanical': {
        'potential_energy_uncertainty': {'default': 0.1, 'range': [0.0, 0.4]},
        'wave_function_uncertainty': {'default': 0.08, 'range': [0.0, 0.3]},
        'quantum_number_uncertainty': {'default': 0.05, 'range': [0.0, 0.2]},
        'monte_carlo_samples': {'default': 1000, 'range': [100, 10000]},
        'uncertainty_distribution': {'default': 'normal', 'range': ['normal', 'uniform', 'lognormal']}
    },
    'uncertainty_phase_field_allen_cahn': {
        'mobility_uncertainty': {'default': 0.12, 'range': [0.0, 0.4]},
        'free_energy_uncertainty': {'default': 0.1, 'range': [0.0, 0.4]},
        'interface_energy_uncertainty': {'default': 0.08, 'range': [0.0, 0.3]},
        'monte_carlo_samples': {'default': 1000, 'range': [100, 10000]},
        'uncertainty_distribution': {'default': 'normal', 'range': ['normal', 'uniform', 'lognormal']}
    },
    'uncertainty_phase_field_cahn_hilliard': {
        'mobility_uncertainty': {'default': 0.12, 'range': [0.0, 0.4]},
        'free_energy_uncertainty': {'default': 0.1, 'range': [0.0, 0.4]},
        'gradient_energy_uncertainty': {'default': 0.08, 'range': [0.0, 0.3]},
        'monte_carlo_samples': {'default': 1000, 'range': [100, 10000]},
        'uncertainty_distribution': {'default': 'normal', 'range': ['normal', 'uniform', 'lognormal']}
    },
    'uncertainty_solidification_stefan': {
        'thermal_diffusivity_uncertainty': {'default': 0.15, 'range': [0.0, 0.5]},
        'latent_heat_uncertainty': {'default': 0.1, 'range': [0.0, 0.4]},
        'phase_change_temperature_uncertainty': {'default': 0.05, 'range': [0.0, 0.2]},
        'monte_carlo_samples': {'default': 1000, 'range': [100, 10000]},
        'uncertainty_distribution': {'default': 'normal', 'range': ['normal', 'uniform', 'lognormal']}
    },
    'uncertainty_grain_growth': {
        'mobility_uncertainty': {'default': 0.15, 'range': [0.0, 0.5]},
        'grain_boundary_energy_uncertainty': {'default': 0.12, 'range': [0.0, 0.4]},
        'initial_grain_size_uncertainty': {'default': 0.08, 'range': [0.0, 0.3]},
        'monte_carlo_samples': {'default': 1000, 'range': [100, 10000]},
        'uncertainty_distribution': {'default': 'normal', 'range': ['normal', 'uniform', 'lognormal']}
    },
    'uncertainty_sintering': {
        'diffusion_coefficient_uncertainty': {'default': 0.2, 'range': [0.0, 0.6]},
        'sintering_mechanism_uncertainty': {'default': 0.15, 'range': [0.0, 0.5]},
        'powder_property_uncertainty': {'default': 0.12, 'range': [0.0, 0.4]},
        'monte_carlo_samples': {'default': 1000, 'range': [100, 10000]},
        'uncertainty_distribution': {'default': 'normal', 'range': ['normal', 'uniform', 'lognormal']}
    },
    'uncertainty_laser_heat_source': {
        'laser_power_uncertainty': {'default': 0.1, 'range': [0.0, 0.4]},
        'beam_radius_uncertainty': {'default': 0.08, 'range': [0.0, 0.3]},
        'absorption_coefficient_uncertainty': {'default': 0.12, 'range': [0.0, 0.4]},
        'monte_carlo_samples': {'default': 1000, 'range': [100, 10000]},
        'uncertainty_distribution': {'default': 'normal', 'range': ['normal', 'uniform', 'lognormal']}
    },
    'uncertainty_melt_pool_dynamics': {
        'fluid_viscosity_uncertainty': {'default': 0.15, 'range': [0.0, 0.5]},
        'surface_tension_uncertainty': {'default': 0.1, 'range': [0.0, 0.4]},
        'thermal_property_uncertainty': {'default': 0.12, 'range': [0.0, 0.4]},
        'monte_carlo_samples': {'default': 2000, 'range': [500, 20000]},
        'uncertainty_distribution': {'default': 'normal', 'range': ['normal', 'uniform', 'lognormal']}
    },
    'uncertainty_crystal_plasticity': {
        'critical_resolved_shear_stress_uncertainty': {'default': 0.15, 'range': [0.0, 0.5]},
        'hardening_parameter_uncertainty': {'default': 0.12, 'range': [0.0, 0.4]},
        'dislocation_density_uncertainty': {'default': 0.1, 'range': [0.0, 0.4]},
        'monte_carlo_samples': {'default': 1000, 'range': [100, 10000]},
        'uncertainty_distribution': {'default': 'normal', 'range': ['normal', 'uniform', 'lognormal']}
    },
    'uncertainty_diffusion_solids': {
        'diffusion_coefficient_uncertainty': {'default': 0.2, 'range': [0.0, 0.6]},
        'activation_energy_uncertainty': {'default': 0.15, 'range': [0.0, 0.5]},
        'temperature_uncertainty': {'default': 0.05, 'range': [0.0, 0.2]},
        'monte_carlo_samples': {'default': 1000, 'range': [100, 10000]},
        'uncertainty_distribution': {'default': 'normal', 'range': ['normal', 'uniform', 'lognormal']}
    },
    'uncertainty_precipitation_nucleation': {
        'nucleation_rate_uncertainty': {'default': 0.25, 'range': [0.0, 0.7]},
        'activation_energy_uncertainty': {'default': 0.2, 'range': [0.0, 0.6]},
        'supersaturation_uncertainty': {'default': 0.15, 'range': [0.0, 0.5]},
        'monte_carlo_samples': {'default': 1000, 'range': [100, 10000]},
        'uncertainty_distribution': {'default': 'normal', 'range': ['normal', 'uniform', 'lognormal']}
    },
    'uncertainty_residual_stress': {
        'elastic_modulus_uncertainty': {'default': 0.15, 'range': [0.0, 0.5]},
        'thermal_expansion_uncertainty': {'default': 0.12, 'range': [0.0, 0.4]},
        'temperature_gradient_uncertainty': {'default': 0.1, 'range': [0.0, 0.4]},
        'monte_carlo_samples': {'default': 1000, 'range': [100, 10000]},
        'uncertainty_distribution': {'default': 'normal', 'range': ['normal', 'uniform', 'lognormal']}
    },
    'uncertainty_microstructure_evolution': {
        'evolution_parameter_uncertainty': {'default': 0.2, 'range': [0.0, 0.6]},
        'phase_field_parameter_uncertainty': {'default': 0.15, 'range': [0.0, 0.5]},
        'initial_microstructure_uncertainty': {'default': 0.1, 'range': [0.0, 0.4]},
        'monte_carlo_samples': {'default': 2000, 'range': [500, 20000]},
        'uncertainty_distribution': {'default': 'normal', 'range': ['normal', 'uniform', 'lognormal']}
    }
} 