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