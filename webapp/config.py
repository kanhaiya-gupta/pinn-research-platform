import os
from pathlib import Path

class Config:
    """Configuration class for PINN Frontend"""
    
    # API Configuration
    API_BASE_URL = os.environ.get('API_BASE_URL') or 'http://localhost:8000'
    
    # PINN Purposes and Applications
    PINN_PURPOSES = {
        'forward_problems': {
            'name': 'Forward Problems',
            'description': 'Simulate physical systems by solving known PDEs with given initial and boundary conditions',
            'icon': 'fas fa-arrow-right',
            'color': '#3498db',
            'examples': ['Heat conduction', 'Wave propagation', 'Fluid dynamics'],
            'route': 'forward-problems',
            'folder': 'forward_problems'
        },
        'inverse_problems': {
            'name': 'Inverse Problems',
            'description': 'Infer unknown parameters, source terms, or boundary conditions from observed data',
            'icon': 'fas fa-search',
            'color': '#e74c3c',
            'examples': ['Parameter identification', 'Source reconstruction', 'Boundary condition estimation'],
            'route': 'inverse-problems',
            'folder': 'inverse_problems'
        },
        'efficiency': {
            'name': 'Simulation Efficiency',
            'description': 'Provide faster, differentiable, and real-time alternatives to traditional numerical solvers',
            'icon': 'fas fa-tachometer-alt',
            'color': '#27ae60',
            'examples': ['Real-time simulation', 'Differentiable physics', 'Fast surrogate models'],
            'route': 'simulation-efficiency',
            'folder': 'efficiency'
        },
        'sparse_data': {
            'name': 'Sparse/Noisy Data Learning',
            'description': 'Use physical laws to guide learning, reducing dependence on large labeled datasets',
            'icon': 'fas fa-database',
            'color': '#f39c12',
            'examples': ['Limited data scenarios', 'Noisy measurements', 'Data augmentation'],
            'route': 'sparse-data-learning',
            'folder': 'sparse_data'
        },
        'data_assimilation': {
            'name': 'Data Assimilation',
            'description': 'Combine observational data with governing physics to improve state estimation',
            'icon': 'fas fa-sync',
            'color': '#9b59b6',
            'examples': ['Weather forecasting', 'Ocean modeling', 'Climate prediction'],
            'route': 'data-assimilation',
            'folder': 'data_assimilation'
        },
        'multiphysics': {
            'name': 'Multiphysics Systems',
            'description': 'Handle systems involving multiple interacting physical phenomena or scales',
            'icon': 'fas fa-cogs',
            'color': '#1abc9c',
            'examples': ['Fluid-structure interaction', 'Thermo-mechanical coupling', 'Electromagnetic-thermal'],
            'route': 'multiphysics-systems',
            'folder': 'multiphysics'
        },
        'scientific_discovery': {
            'name': 'Scientific Discovery',
            'description': 'Discover or validate new physical laws, constitutive relations, or hidden dynamics',
            'icon': 'fas fa-microscope',
            'color': '#34495e',
            'examples': ['New constitutive laws', 'Hidden dynamics', 'Physical validation'],
            'route': 'scientific-discovery',
            'folder': 'scientific_discovery'
        },
        'uncertainty': {
            'name': 'Uncertainty Quantification',
            'description': 'Extend PINNs to probabilistic frameworks to model and quantify uncertainties',
            'icon': 'fas fa-chart-area',
            'color': '#e67e22',
            'examples': ['Probabilistic predictions', 'Confidence intervals', 'Risk assessment'],
            'route': 'uncertainty-quantification',
            'folder': 'uncertainty'
        },
        'generalization': {
            'name': 'Generalization & Robustness',
            'description': 'Physics constraints act as regularizers, leading to better generalization',
            'icon': 'fas fa-shield-alt',
            'color': '#16a085',
            'examples': ['Out-of-distribution', 'Domain adaptation', 'Robust predictions'],
            'route': 'generalization-robustness',
            'folder': 'generalization'
        },
        'control_optimization': {
            'name': 'Control & Optimization',
            'description': 'Use PINNs in design, control, or optimization tasks with physics constraints',
            'icon': 'fas fa-sliders-h',
            'color': '#8e44ad',
            'examples': ['Optimal control', 'Design optimization', 'Parameter tuning'],
            'route': 'control-optimization',
            'folder': 'control_optimization'
        }
    }
    
    # Supported Equations with expanded scope
    SUPPORTED_EQUATIONS = {
        'burgers': {
            'name': 'Burgers Equation',
            'description': 'Nonlinear partial differential equation modeling fluid dynamics and shock waves',
            'icon': 'fas fa-water',
            'color': '#3498db',
            'formula': '∂u/∂t + u∂u/∂x = ν∂²u/∂x²',
            'purposes': ['forward_problems', 'inverse_problems', 'efficiency'],
            'applications': ['Shock wave propagation', 'Traffic flow modeling', 'Gas dynamics']
        },
        'heat': {
            'name': 'Heat Equation',
            'description': 'Parabolic partial differential equation for heat conduction and diffusion',
            'icon': 'fas fa-fire',
            'color': '#e74c3c',
            'formula': '∂u/∂t = α∂²u/∂x²',
            'purposes': ['forward_problems', 'inverse_problems', 'efficiency', 'sparse_data'],
            'applications': ['Thermal analysis', 'Material processing', 'Climate modeling']
        },
        'wave': {
            'name': 'Wave Equation',
            'description': 'Hyperbolic partial differential equation for wave propagation phenomena',
            'icon': 'fas fa-wave-square',
            'color': '#9b59b6',
            'formula': '∂²u/∂t² = c²∂²u/∂x²',
            'purposes': ['forward_problems', 'inverse_problems', 'efficiency', 'multiphysics'],
            'applications': ['Acoustic waves', 'Electromagnetic waves', 'Seismic waves']
        },
        'shm': {
            'name': 'Simple Harmonic Motion',
            'description': 'Ordinary differential equation for oscillatory motion and vibrations',
            'icon': 'fas fa-sync',
            'color': '#f39c12',
            'formula': 'd²x/dt² + ω²x = 0',
            'purposes': ['forward_problems', 'control_optimization', 'generalization'],
            'applications': ['Mechanical vibrations', 'Electrical circuits', 'Molecular dynamics']
        },
        'helmholtz': {
            'name': 'Helmholtz Equation',
            'description': 'Elliptic partial differential equation for wave phenomena in steady state',
            'icon': 'fas fa-atom',
            'color': '#1abc9c',
            'formula': '∇²u + k²u = 0',
            'purposes': ['forward_problems', 'inverse_problems', 'multiphysics'],
            'applications': ['Acoustic scattering', 'Electromagnetic fields', 'Quantum mechanics']
        },
        'navier_stokes': {
            'name': 'Navier-Stokes Equations',
            'description': 'System of PDEs describing fluid motion and turbulence',
            'icon': 'fas fa-wind',
            'color': '#34495e',
            'formula': 'ρ(∂v/∂t + v·∇v) = -∇p + μ∇²v + f',
            'purposes': ['forward_problems', 'inverse_problems', 'multiphysics', 'efficiency'],
            'applications': ['Aerodynamics', 'Oceanography', 'Blood flow modeling']
        },
        'schrodinger': {
            'name': 'Schrödinger Equation',
            'description': 'Quantum mechanical equation for particle wave functions',
            'icon': 'fas fa-quantum',
            'color': '#8e44ad',
            'formula': 'iℏ∂ψ/∂t = Ĥψ',
            'purposes': ['forward_problems', 'scientific_discovery', 'uncertainty'],
            'applications': ['Quantum chemistry', 'Material properties', 'Quantum computing']
        },
        'maxwell': {
            'name': 'Maxwell Equations',
            'description': 'System of PDEs describing electromagnetic fields',
            'icon': 'fas fa-bolt',
            'color': '#e67e22',
            'formula': '∇·E = ρ/ε₀, ∇×E = -∂B/∂t, ∇·B = 0, ∇×B = μ₀J + μ₀ε₀∂E/∂t',
            'purposes': ['forward_problems', 'multiphysics', 'efficiency'],
            'applications': ['Antenna design', 'Optical systems', 'Electromagnetic compatibility']
        }
    }
    
    # Default Parameters for each equation
    DEFAULT_PARAMETERS = {
        'burgers': {
            'nu': 0.01,
            'nx': 256,
            'nt': 100,
            'x_min': 0.0,
            'x_max': 1.0,
            't_min': 0.0,
            't_max': 1.0
        },
        'heat': {
            'alpha': 0.1,
            'nx': 256,
            'nt': 100,
            'x_min': 0.0,
            'x_max': 1.0,
            't_min': 0.0,
            't_max': 1.0
        },
        'wave': {
            'c': 1.0,
            'nx': 256,
            'nt': 100,
            'x_min': 0.0,
            'x_max': 1.0,
            't_min': 0.0,
            't_max': 1.0
        },
        'shm': {
            'omega': 1.0,
            'nt': 1000,
            't_min': 0.0,
            't_max': 10.0
        },
        'helmholtz': {
            'k': 1.0,
            'nx': 100,
            'ny': 100,
            'x_min': 0.0,
            'x_max': 1.0,
            'y_min': 0.0,
            'y_max': 1.0
        },
        'navier_stokes': {
            'reynolds': 100.0,
            'nx': 128,
            'ny': 128,
            'nt': 50,
            'x_min': 0.0,
            'x_max': 1.0,
            'y_min': 0.0,
            'y_max': 1.0,
            't_min': 0.0,
            't_max': 1.0
        },
        'schrodinger': {
            'hbar': 1.0,
            'mass': 1.0,
            'nx': 256,
            'nt': 100,
            'x_min': -5.0,
            'x_max': 5.0,
            't_min': 0.0,
            't_max': 1.0
        },
        'maxwell': {
            'epsilon': 1.0,
            'mu': 1.0,
            'nx': 128,
            'ny': 128,
            'nt': 50,
            'x_min': 0.0,
            'x_max': 1.0,
            'y_min': 0.0,
            'y_max': 1.0,
            't_min': 0.0,
            't_max': 1.0
        }
    }
    
    # Parameter descriptions for UI
    PARAMETER_DESCRIPTIONS = {
        'nu': 'Viscosity coefficient',
        'alpha': 'Thermal diffusivity',
        'c': 'Wave speed',
        'omega': 'Angular frequency',
        'k': 'Wavenumber',
        'reynolds': 'Reynolds number',
        'hbar': 'Reduced Planck constant',
        'mass': 'Particle mass',
        'epsilon': 'Permittivity',
        'mu': 'Permeability'
    }
    
    # Activation Functions Configuration
    ACTIVATION_FUNCTIONS = {
        'hidden_activations': {
            'tanh': {
                'name': 'Hyperbolic Tangent (tanh)',
                'description': 'Smooth, differentiable - ideal for PDEs',
                'suitability': 'Very common in PINNs',
                'notes': 'Smooth, differentiable — ideal for PDEs',
                'recommended_for': ['forward_problems', 'inverse_problems', 'data_assimilation']
            },
            'sin': {
                'name': 'Sine Function (sin)',
                'description': 'Captures high-frequency patterns and oscillatory behavior',
                'suitability': 'High-frequency problems (e.g., Fourier PINNs)',
                'notes': 'Captures fine details and oscillatory behavior',
                'recommended_for': ['scientific_discovery', 'multiphysics', 'high_frequency']
            },
            'softplus': {
                'name': 'Softplus Function',
                'description': 'Smooth ReLU alternative - smooth and differentiable',
                'suitability': 'Sometimes used as ReLU alternative',
                'notes': 'Smooth ReLU alternative, good for bounded outputs',
                'recommended_for': ['bounded_outputs', 'positive_values']
            },
            'relu': {
                'name': 'Rectified Linear Unit (ReLU)',
                'description': 'Not recommended for PINNs due to lack of smoothness',
                'suitability': 'Generally avoided in PINNs',
                'notes': 'Not smooth — poor for higher-order PDEs',
                'recommended_for': ['avoid_in_pinns']
            },
            'sigmoid': {
                'name': 'Sigmoid Function',
                'description': 'For bounded outputs between 0 and 1',
                'suitability': 'When output needs bounding',
                'notes': 'Useful when solution values need to be bounded',
                'recommended_for': ['bounded_outputs', 'probability_outputs']
            }
        },
        'output_activations': {
            'linear': {
                'name': 'Linear (No Activation)',
                'description': 'No transformation - standard for most PINN outputs',
                'suitability': 'Most common for PINN outputs',
                'notes': 'No transformation applied - raw network output',
                'recommended_for': ['most_pinn_applications', 'unbounded_outputs']
            },
            'tanh': {
                'name': 'Hyperbolic Tangent (tanh)',
                'description': 'Bounded output between -1 and 1',
                'suitability': 'When solution is bounded',
                'notes': 'Useful for normalized or bounded physical variables',
                'recommended_for': ['bounded_solutions', 'normalized_outputs']
            },
            'sigmoid': {
                'name': 'Sigmoid Function',
                'description': 'Bounded output between 0 and 1',
                'suitability': 'Probability or positive bounded outputs',
                'notes': 'Useful for probabilities or positive bounded variables',
                'recommended_for': ['probabilities', 'positive_bounded']
            },
            'softplus': {
                'name': 'Softplus Function',
                'description': 'Positive output (≥ 0)',
                'suitability': 'When solution must be positive',
                'notes': 'Smooth alternative to ReLU for positive outputs',
                'recommended_for': ['positive_outputs', 'concentrations', 'temperatures']
            }
        }
    }
    
    # Optimizers Configuration
    OPTIMIZERS = {
        'adam': {
            'name': 'Adam Optimizer',
            'description': 'Adaptive learning rate optimizer',
            'suitability': 'Pre-training or early phases',
            'notes': 'Fast and adaptive, good for initial convergence',
            'recommended_for': ['initial_training', 'adaptive_learning']
        },
        'lbfgs': {
            'name': 'L-BFGS Optimizer',
            'description': 'Second-order optimization method',
            'suitability': 'Final convergence',
            'notes': 'Full-batch, second-order, excellent for PDEs',
            'recommended_for': ['final_convergence', 'high_precision']
        },
        'adam_lbfgs': {
            'name': 'Adam → L-BFGS Hybrid',
            'description': 'Best practice combination for PINNs',
            'suitability': 'Best practice combination',
            'notes': 'Combines speed of Adam with precision of L-BFGS',
            'recommended_for': ['best_practice', 'production_use']
        },
        'sgd': {
            'name': 'Stochastic Gradient Descent',
            'description': 'Basic gradient descent optimizer',
            'suitability': 'Rare in PINNs',
            'notes': 'Too noisy, unstable for PINN training',
            'recommended_for': ['avoid_in_pinns']
        }
    }
    
    # Architecture Recommendations by Purpose
    ARCHITECTURE_RECOMMENDATIONS = {
        'forward_problems': {
            'hidden_activation': 'tanh',
            'output_activation': 'linear',
            'optimizer': 'adam_lbfgs',
            'notes': 'Smooth hidden activations + linear output + L-BFGS for PDE solving'
        },
        'inverse_problems': {
            'hidden_activation': 'tanh',
            'output_activation': 'linear',
            'optimizer': 'adam_lbfgs',
            'notes': 'Sensitive to optimizer tuning, Adam + L-BFGS ideal'
        },
        'sparse_data': {
            'hidden_activation': 'tanh',
            'output_activation': 'linear',
            'optimizer': 'adam',
            'notes': 'Physics loss helps regularize; tanh preferred'
        },
        'data_assimilation': {
            'hidden_activation': 'tanh',
            'output_activation': 'linear',
            'optimizer': 'adam_lbfgs',
            'notes': 'Requires loss weighting + smooth activations'
        },
        'multiphysics': {
            'hidden_activation': 'tanh',
            'output_activation': 'linear',
            'optimizer': 'adam',
            'notes': 'May need custom activations or domain decomposition'
        },
        'scientific_discovery': {
            'hidden_activation': 'sin',
            'output_activation': 'linear',
            'optimizer': 'adam_lbfgs',
            'notes': 'sin/tanh + robust optimizer; may use symbolic loss'
        },
        'uncertainty': {
            'hidden_activation': 'tanh',
            'output_activation': 'linear',
            'optimizer': 'adam',
            'notes': 'Extended with probabilistic layers or ensembles'
        },
        'control_optimization': {
            'hidden_activation': 'tanh',
            'output_activation': 'linear',
            'optimizer': 'adam_lbfgs',
            'notes': 'Differentiable models needed → smooth activations'
        }
    }

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
} 