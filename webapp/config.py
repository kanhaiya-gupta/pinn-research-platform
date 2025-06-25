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
            'purposes': ['forward_problems', 'inverse_problems', 'efficiency', 'sparse_data', 'data_assimilation', 'generalization'],
            'applications': ['Shock wave propagation', 'Traffic flow modeling', 'Gas dynamics']
        },
        'heat': {
            'name': 'Heat Equation',
            'description': 'Parabolic partial differential equation for heat conduction and diffusion',
            'icon': 'fas fa-fire',
            'color': '#e74c3c',
            'formula': '∂u/∂t = α∂²u/∂x²',
            'purposes': ['forward_problems', 'inverse_problems', 'efficiency', 'sparse_data', 'data_assimilation', 'generalization', 'uncertainty'],
            'applications': ['Thermal analysis', 'Material processing', 'Climate modeling']
        },
        'wave': {
            'name': 'Wave Equation',
            'description': 'Hyperbolic partial differential equation for wave propagation phenomena',
            'icon': 'fas fa-wave-square',
            'color': '#9b59b6',
            'formula': '∂²u/∂t² = c²∂²u/∂x²',
            'purposes': ['forward_problems', 'inverse_problems', 'efficiency', 'multiphysics', 'sparse_data', 'data_assimilation', 'generalization'],
            'applications': ['Acoustic waves', 'Electromagnetic waves', 'Seismic waves']
        },
        'shm': {
            'name': 'Simple Harmonic Motion',
            'description': 'Ordinary differential equation for oscillatory motion and vibrations',
            'icon': 'fas fa-sync',
            'color': '#f39c12',
            'formula': 'd²x/dt² + ω²x = 0',
            'purposes': ['forward_problems', 'control_optimization', 'generalization', 'efficiency', 'sparse_data', 'uncertainty'],
            'applications': ['Mechanical vibrations', 'Electrical circuits', 'Molecular dynamics']
        },
        'helmholtz': {
            'name': 'Helmholtz Equation',
            'description': 'Elliptic partial differential equation for wave phenomena in steady state',
            'icon': 'fas fa-atom',
            'color': '#1abc9c',
            'formula': '∇²u + k²u = 0',
            'purposes': ['forward_problems', 'inverse_problems', 'multiphysics', 'efficiency', 'sparse_data', 'scientific_discovery'],
            'applications': ['Acoustic scattering', 'Electromagnetic fields', 'Quantum mechanics']
        },
        'navier_stokes': {
            'name': 'Navier-Stokes Equations',
            'description': 'System of PDEs describing fluid motion and turbulence',
            'icon': 'fas fa-wind',
            'color': '#34495e',
            'formula': 'ρ(∂v/∂t + v·∇v) = -∇p + μ∇²v + f',
            'purposes': ['forward_problems', 'inverse_problems', 'multiphysics', 'efficiency', 'data_assimilation', 'scientific_discovery', 'uncertainty'],
            'applications': ['Aerodynamics', 'Oceanography', 'Blood flow modeling']
        },
        'schrodinger': {
            'name': 'Schrödinger Equation',
            'description': 'Quantum mechanical equation for particle wave functions',
            'icon': 'fas fa-quantum',
            'color': '#8e44ad',
            'formula': 'iℏ∂ψ/∂t = Ĥψ',
            'purposes': ['forward_problems', 'scientific_discovery', 'uncertainty', 'efficiency', 'sparse_data', 'generalization'],
            'applications': ['Quantum chemistry', 'Material properties', 'Quantum computing']
        },
        'maxwell': {
            'name': 'Maxwell Equations',
            'description': 'System of PDEs describing electromagnetic fields',
            'icon': 'fas fa-bolt',
            'color': '#e67e22',
            'formula': '∇·E = ρ/ε₀, ∇×E = -∂B/∂t, ∇·B = 0, ∇×B = μ₀J + μ₀ε₀∂E/∂t',
            'purposes': ['forward_problems', 'multiphysics', 'efficiency', 'scientific_discovery', 'uncertainty'],
            'applications': ['Antenna design', 'Optical systems', 'Electromagnetic compatibility']
        },
        'linear_dynamics': {
            'name': 'Linear Dynamical Systems',
            'description': 'Linear state-space models for control and optimization',
            'icon': 'fas fa-cogs',
            'color': '#3498db',
            'formula': 'dx/dt = Ax + Bu',
            'purposes': ['control_optimization', 'forward_problems', 'inverse_problems', 'efficiency'],
            'applications': ['Robotics', 'Aerospace', 'Process control', 'Satellite attitude control']
        },
        'nonlinear_dynamics': {
            'name': 'Nonlinear Dynamical Systems',
            'description': 'Nonlinear state-space models for complex control problems',
            'icon': 'fas fa-project-diagram',
            'color': '#e74c3c',
            'formula': 'dx/dt = f(x, u, t)',
            'purposes': ['control_optimization', 'forward_problems', 'inverse_problems', 'efficiency'],
            'applications': ['Autonomous vehicles', 'Biological systems', 'Fluid dynamics', 'Neural control']
        },
        'optimal_control_shm': {
            'name': 'Optimal Control - Simple Harmonic Motion',
            'description': 'Controlled harmonic oscillator with optimal control input',
            'icon': 'fas fa-wave-square',
            'color': '#9b59b6',
            'formula': 'd²x/dt² + ω²x = u(t)',
            'purposes': ['control_optimization', 'forward_problems', 'efficiency', 'generalization'],
            'applications': ['Vibration suppression', 'Suspension systems', 'LC oscillators', 'Molecular dynamics']
        },
        'fluid_control': {
            'name': 'Fluid Dynamics Control',
            'description': 'Navier-Stokes equations with control forces for flow optimization',
            'icon': 'fas fa-wind',
            'color': '#1abc9c',
            'formula': '∂u/∂t + (u·∇)u = -∇p/ρ + ν∇²u + f(u,t)',
            'purposes': ['control_optimization', 'multiphysics', 'efficiency', 'data_assimilation'],
            'applications': ['Aerodynamic optimization', 'Flow control', 'HVAC systems', 'Pipeline optimization']
        },
        'thermal_control': {
            'name': 'Thermal Control Systems',
            'description': 'Heat transfer equation with control heat sources',
            'icon': 'fas fa-thermometer-half',
            'color': '#f39c12',
            'formula': 'ρc_p ∂T/∂t = ∇·(k∇T) + u',
            'purposes': ['control_optimization', 'additive_manufacturing', 'efficiency', 'data_assimilation'],
            'applications': ['Additive manufacturing', 'Electronics cooling', 'Heat treatment', 'Laser processing']
        },
        'wave_control': {
            'name': 'Wave Control Systems',
            'description': 'Wave equation with control forces for vibration and acoustic control',
            'icon': 'fas fa-broadcast-tower',
            'color': '#34495e',
            'formula': '∂²u/∂t² = c²∇²u + f',
            'purposes': ['control_optimization', 'forward_problems', 'efficiency', 'generalization'],
            'applications': ['Structural engineering', 'Noise cancellation', 'Laser stabilization', 'Earthquake resistance']
        },
        'additive_manufacturing_control': {
            'name': 'Additive Manufacturing Control',
            'description': 'Heat transfer with phase change and laser control for 3D printing',
            'icon': 'fas fa-print',
            'color': '#8e44ad',
            'formula': 'ρc_p ∂T/∂t = ∇·(k∇T) + Q_laser - L ∂f_s/∂t',
            'purposes': ['control_optimization', 'additive_manufacturing', 'multiphysics', 'efficiency'],
            'applications': ['Laser powder bed fusion', 'Melt pool control', 'Defect minimization', 'Stress reduction']
        },
        'material_control': {
            'name': 'Material Science Control',
            'description': 'Phase-field equation with external control for microstructure optimization',
            'icon': 'fas fa-atom',
            'color': '#16a085',
            'formula': '∂φ/∂t = -M δF/δφ + u',
            'purposes': ['control_optimization', 'material_science', 'scientific_discovery', 'efficiency'],
            'applications': ['Grain growth control', 'Phase transformation', 'Thin film deposition', 'Alloy optimization']
        },
        'hjb_equation': {
            'name': 'Hamilton-Jacobi-Bellman Equation',
            'description': 'Optimal control theory for finding optimal control policies',
            'icon': 'fas fa-chess',
            'color': '#e67e22',
            'formula': '∂V/∂t + min_u[L(x,u,t) + ∇V·f(x,u,t)] = 0',
            'purposes': ['control_optimization', 'scientific_discovery', 'efficiency', 'generalization'],
            'applications': ['Robotics path planning', 'Power grid optimization', 'Portfolio optimization', 'Energy systems']
        },
        'multi_objective_control': {
            'name': 'Multi-Objective Control',
            'description': 'Control systems with multiple competing objectives',
            'icon': 'fas fa-balance-scale',
            'color': '#27ae60',
            'formula': 'J = Σ w_i J_i where J_i are individual objectives',
            'purposes': ['control_optimization', 'efficiency', 'generalization', 'uncertainty'],
            'applications': ['Autonomous systems', 'Smart cities', 'Healthcare', 'Environmental control']
        },
        'heat_transfer_phase_change': {
            'name': 'Heat Transfer with Phase Change',
            'description': 'PDE for thermal processes with melting/solidification in additive manufacturing',
            'icon': 'fas fa-thermometer-half',
            'color': '#e74c3c',
            'formula': 'ρc_p ∂T/∂t = ∇·(k∇T) + Q - L ∂f_s/∂t',
            'purposes': ['forward_problems', 'additive_manufacturing', 'multiphysics', 'efficiency'],
            'applications': ['Melt pool dynamics', 'Thermal history prediction', 'Solidification modeling']
        },
        'stefan_condition': {
            'name': 'Stefan Condition',
            'description': 'Boundary condition for moving phase interfaces',
            'icon': 'fas fa-arrows-alt-h',
            'color': '#9b59b6',
            'formula': 'k_s ∇T_s·n - k_l ∇T_l·n = ρL v_n',
            'purposes': ['forward_problems', 'additive_manufacturing', 'multiphysics'],
            'applications': ['Melt pool boundaries', 'Solidification front modeling']
        },
        'navier_stokes_free_surface': {
            'name': 'Navier-Stokes with Free Surface',
            'description': 'PDEs for fluid flow in melt pools with surface tension effects',
            'icon': 'fas fa-water',
            'color': '#3498db',
            'formula': 'ρ(∂v/∂t + v·∇v) = -∇p + μ∇²v + f_surface, ∇·v = 0',
            'purposes': ['forward_problems', 'additive_manufacturing', 'multiphysics', 'efficiency'],
            'applications': ['Melt pool dynamics', 'Keyhole formation', 'Surface tension effects']
        },
        'thermal_stress': {
            'name': 'Thermal Stress Equation',
            'description': 'PDE for residual stresses due to thermal gradients',
            'icon': 'fas fa-compress-arrows-alt',
            'color': '#f39c12',
            'formula': '∇·σ = 0, σ = C:(ε - ε_th)',
            'purposes': ['forward_problems', 'additive_manufacturing', 'multiphysics'],
            'applications': ['Residual stress prediction', 'Warping analysis', 'Cracking analysis']
        },
        'phase_field': {
            'name': 'Phase-Field Equation',
            'description': 'PDE for microstructure evolution in materials',
            'icon': 'fas fa-atom',
            'color': '#1abc9c',
            'formula': '∂φ/∂t = -M δF/δφ',
            'purposes': ['forward_problems', 'material_science', 'multiphysics', 'scientific_discovery'],
            'applications': ['Grain growth', 'Phase transformations', 'Solidification']
        },
        'cahn_hilliard': {
            'name': 'Cahn-Hilliard Equation',
            'description': 'PDE for phase separation and diffusion in materials',
            'icon': 'fas fa-layer-group',
            'color': '#34495e',
            'formula': '∂c/∂t = ∇·(M∇μ), μ = δF/δc',
            'purposes': ['forward_problems', 'material_science', 'multiphysics'],
            'applications': ['Spinodal decomposition', 'Thin film growth', 'Battery materials']
        },
        'fick_second_law': {
            'name': 'Fick\'s Second Law',
            'description': 'PDE for diffusion processes in materials',
            'icon': 'fas fa-exchange-alt',
            'color': '#27ae60',
            'formula': '∂c/∂t = ∇·(D∇c)',
            'purposes': ['forward_problems', 'material_science', 'efficiency'],
            'applications': ['Dopant diffusion', 'Hydrogen diffusion', 'Drug diffusion']
        },
        'crystal_plasticity': {
            'name': 'Crystal Plasticity Equations',
            'description': 'ODEs/PDEs for plastic deformation in crystalline materials',
            'icon': 'fas fa-cube',
            'color': '#8e44ad',
            'formula': 'ε̇^p = Σ_α γ̇^α m^α, γ̇^α = f(τ^α, s^α)',
            'purposes': ['forward_problems', 'material_science', 'multiphysics'],
            'applications': ['Deformation modeling', 'Fatigue analysis', 'Part integrity']
        },
        'advection_diffusion': {
            'name': 'Advection-Diffusion Equation',
            'description': 'PDE for transport phenomena with convection and diffusion',
            'icon': 'fas fa-wind',
            'color': '#16a085',
            'formula': '∂c/∂t + v·∇c = ∇·(D∇c)',
            'purposes': ['forward_problems', 'data_assimilation', 'multiphysics', 'efficiency'],
            'applications': ['Atmospheric transport', 'Ocean currents', 'Pollutant dispersion']
        },
        'shallow_water': {
            'name': 'Shallow Water Equations',
            'description': 'PDEs for fluid flow in shallow layers',
            'icon': 'fas fa-water',
            'color': '#2980b9',
            'formula': '∂h/∂t + ∇·(hv) = 0, ∂v/∂t + v·∇v = -g∇h',
            'purposes': ['forward_problems', 'data_assimilation', 'multiphysics'],
            'applications': ['Ocean modeling', 'Tsunami simulation', 'River flow']
        },
        'poroelasticity': {
            'name': 'Poroelasticity Equations',
            'description': 'PDEs for fluid-saturated porous media',
            'icon': 'fas fa-filter',
            'color': '#d35400',
            'formula': '∇·σ = 0, ∂ζ/∂t + ∇·q = 0',
            'purposes': ['forward_problems', 'biomechanics', 'geophysics', 'multiphysics'],
            'applications': ['Bone mechanics', 'Groundwater flow', 'Tissue modeling']
        },
        'radiative_transfer': {
            'name': 'Radiative Transfer Equation',
            'description': 'PDE for radiation transport in participating media',
            'icon': 'fas fa-sun',
            'color': '#f1c40f',
            'formula': 'Ω·∇I + κI = κI_b + σ/(4π)∫I(Ω′)Φ(Ω,Ω′)dΩ′',
            'purposes': ['forward_problems', 'remote_sensing', 'multiphysics'],
            'applications': ['Atmospheric radiation', 'Optical systems', 'Climate modeling']
        },
        'reaction_diffusion': {
            'name': 'Reaction-Diffusion Equations',
            'description': 'PDEs for chemical reactions with diffusion',
            'icon': 'fas fa-flask',
            'color': '#e67e22',
            'formula': '∂u/∂t = D∇²u + f(u,v), ∂v/∂t = D∇²v + g(u,v)',
            'purposes': ['forward_problems', 'scientific_discovery', 'multiphysics'],
            'applications': ['Chemical kinetics', 'Pattern formation', 'Biological systems']
        },
        'elastic_wave': {
            'name': 'Elastic Wave Equation',
            'description': 'PDE for wave propagation in elastic media',
            'icon': 'fas fa-wave-square',
            'color': '#9b59b6',
            'formula': 'ρ∂²u/∂t² = ∇·(C:∇u)',
            'purposes': ['forward_problems', 'geophysics', 'multiphysics'],
            'applications': ['Seismic waves', 'Ultrasound', 'Structural dynamics']
        },
        'magnetohydrodynamics': {
            'name': 'Magnetohydrodynamics (MHD)',
            'description': 'PDEs for electrically conducting fluids in magnetic fields',
            'icon': 'fas fa-magnet',
            'color': '#8e44ad',
            'formula': 'ρ(∂v/∂t + v·∇v) = -∇p + μ∇²v + J×B, ∂B/∂t = ∇×(v×B) + η∇²B',
            'purposes': ['forward_problems', 'fusion_energy', 'multiphysics'],
            'applications': ['Plasma physics', 'Fusion reactors', 'Space physics']
        },
        'viscoelasticity': {
            'name': 'Viscoelasticity Equations',
            'description': 'PDEs for materials with both viscous and elastic properties',
            'icon': 'fas fa-tint',
            'color': '#3498db',
            'formula': 'σ + τ∂σ/∂t = E(ε + τ_ε∂ε/∂t)',
            'purposes': ['forward_problems', 'material_science', 'biomechanics'],
            'applications': ['Polymer mechanics', 'Biological tissues', 'Rheology']
        },
        'thermoelasticity': {
            'name': 'Thermoelasticity Equations',
            'description': 'PDEs coupling thermal and mechanical effects',
            'icon': 'fas fa-thermometer-half',
            'color': '#e74c3c',
            'formula': '∇·σ = 0, ρc_p∂T/∂t = ∇·(k∇T) - T_0α∇·∂u/∂t',
            'purposes': ['forward_problems', 'additive_manufacturing', 'multiphysics'],
            'applications': ['Thermal stress', 'Heat exchangers', 'Electronic packaging']
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
        'efficiency': {
            'hidden_activation': 'tanh',
            'output_activation': 'linear',
            'optimizer': 'adam_lbfgs',
            'notes': 'Fast convergence + smooth activations for real-time applications'
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
        'generalization': {
            'hidden_activation': 'tanh',
            'output_activation': 'linear',
            'optimizer': 'adam_lbfgs',
            'notes': 'Physics constraints act as regularizers for better generalization'
        },
        'control_optimization': {
            'hidden_activation': 'tanh',
            'output_activation': 'linear',
            'optimizer': 'adam_lbfgs',
            'notes': 'Differentiable models needed → smooth activations'
        }
    }

    # Training Parameters Configuration
    TRAINING_PARAMETERS = {
        'learning_rate_schedulers': {
            'constant': {
                'name': 'Constant Learning Rate',
                'description': 'Fixed learning rate throughout training',
                'suitability': 'Simple problems, stable training',
                'notes': 'Most common for PINNs'
            },
            'step': {
                'name': 'Step Decay',
                'description': 'Reduces LR by factor every N epochs',
                'suitability': 'When convergence plateaus',
                'notes': 'Good for fine-tuning'
            },
            'cosine': {
                'name': 'Cosine Annealing',
                'description': 'Smooth learning rate reduction',
                'suitability': 'Better convergence, less sensitive',
                'notes': 'Popular in modern deep learning'
            },
            'exponential': {
                'name': 'Exponential Decay',
                'description': 'Continuous LR reduction',
                'suitability': 'Stiff problems, careful tuning needed',
                'notes': 'Can be too aggressive'
            }
        },
        'weight_initializations': {
            'xavier': {
                'name': 'Xavier/Glorot',
                'description': 'Optimal for tanh/sigmoid activations',
                'suitability': 'Most common, good for PINNs',
                'notes': 'Default choice for most networks'
            },
            'he': {
                'name': 'He Initialization',
                'description': 'Good for ReLU-like activations',
                'suitability': 'Not recommended for PINNs',
                'notes': 'Designed for ReLU, not smooth activations'
            },
            'normal': {
                'name': 'Normal Distribution',
                'description': 'Simple normal distribution',
                'suitability': 'Simple, but may need tuning',
                'notes': 'Standard deviation matters'
            },
            'uniform': {
                'name': 'Uniform Distribution',
                'description': 'Bounded weight initialization',
                'suitability': 'Simple, bounded weights',
                'notes': 'Range selection is important'
            }
        },
        'batch_strategies': {
            'full_batch': {
                'name': 'Full Batch',
                'description': 'Use all points in each iteration',
                'suitability': 'Most common in PINNs',
                'notes': 'Stable gradients, memory intensive'
            },
            'mini_batch': {
                'name': 'Mini Batch',
                'description': 'Use subset of points per iteration',
                'suitability': 'Large datasets, memory constraints',
                'notes': 'May need more epochs'
            }
        }
    }
    
    # Training Recommendations by Purpose
    TRAINING_RECOMMENDATIONS = {
        'forward_problems': {
            'learning_rate': 0.001,
            'optimizer': 'adam_lbfgs',
            'scheduler': 'constant',
            'batch_size': 'full_batch',
            'loss_weights': {'physics': 1.0, 'boundary': 1.0, 'initial': 1.0},
            'sampling': {'interior': 1000, 'boundary': 200, 'initial': 200},
            'notes': 'Standard PINN setup with balanced loss weights'
        },
        'inverse_problems': {
            'learning_rate': 0.001,
            'optimizer': 'adam_lbfgs',
            'scheduler': 'step',
            'batch_size': 'full_batch',
            'loss_weights': {'physics': 1.0, 'data': 10.0, 'boundary': 1.0},
            'sampling': {'interior': 1000, 'boundary': 200, 'data': 100},
            'notes': 'Higher data weight, step scheduler for fine-tuning'
        },
        'data_assimilation': {
            'learning_rate': 0.001,
            'optimizer': 'adam',
            'scheduler': 'cosine',
            'batch_size': 'full_batch',
            'loss_weights': {'physics': 1.0, 'data': 5.0, 'boundary': 1.0},
            'sampling': {'interior': 1000, 'boundary': 200, 'data': 200},
            'notes': 'Balanced physics and data, cosine scheduler'
        },
        'scientific_discovery': {
            'learning_rate': 0.0005,
            'optimizer': 'adam_lbfgs',
            'scheduler': 'constant',
            'batch_size': 'full_batch',
            'loss_weights': {'physics': 1.0, 'boundary': 1.0, 'initial': 1.0},
            'sampling': {'interior': 2000, 'boundary': 400, 'initial': 400},
            'notes': 'Lower LR, more points for discovery tasks'
        },
        'multiphysics': {
            'learning_rate': 0.001,
            'optimizer': 'adam',
            'scheduler': 'step',
            'batch_size': 'full_batch',
            'loss_weights': {'physics': 1.0, 'boundary': 1.0, 'coupling': 1.0},
            'sampling': {'interior': 1500, 'boundary': 300, 'initial': 300},
            'notes': 'Step scheduler for complex coupled systems'
        },
        'sparse_data': {
            'learning_rate': 0.001,
            'optimizer': 'adam',
            'scheduler': 'constant',
            'batch_size': 'full_batch',
            'loss_weights': {'physics': 1.0, 'boundary': 1.0, 'data': 2.0},
            'sampling': {'interior': 1000, 'boundary': 200, 'data': 50},
            'notes': 'Physics loss helps regularize sparse data'
        },
        'efficiency': {
            'learning_rate': 0.001,
            'optimizer': 'adam',
            'scheduler': 'constant',
            'batch_size': 'full_batch',
            'loss_weights': {'physics': 1.0, 'boundary': 1.0, 'initial': 1.0},
            'sampling': {'interior': 800, 'boundary': 150, 'initial': 150},
            'notes': 'Optimized for speed while maintaining accuracy'
        },
        'uncertainty': {
            'learning_rate': 0.001,
            'optimizer': 'adam',
            'scheduler': 'cosine',
            'batch_size': 'full_batch',
            'loss_weights': {'physics': 1.0, 'boundary': 1.0, 'initial': 1.0},
            'sampling': {'interior': 1000, 'boundary': 200, 'initial': 200},
            'notes': 'Cosine scheduler for stable uncertainty estimation'
        },
        'control_optimization': {
            'learning_rate': 0.001,
            'optimizer': 'adam_lbfgs',
            'scheduler': 'step',
            'batch_size': 'full_batch',
            'loss_weights': {'physics': 1.0, 'boundary': 1.0, 'control': 1.0},
            'sampling': {'interior': 1000, 'boundary': 200, 'initial': 200},
            'notes': 'Step scheduler for control optimization convergence'
        },
        'generalization': {
            'learning_rate': 0.001,
            'optimizer': 'adam',
            'scheduler': 'cosine',
            'batch_size': 'full_batch',
            'loss_weights': {'physics': 1.0, 'boundary': 1.0, 'initial': 1.0},
            'sampling': {'interior': 1200, 'boundary': 250, 'initial': 250},
            'notes': 'Cosine scheduler for better generalization'
        }
    }

    # Enhanced Data Assimilation Applications
    DATA_ASSIMILATION_APPLICATIONS = {
        'weather_forecasting': {
            'name': 'Weather Forecasting',
            'description': 'Atmospheric data assimilation for weather prediction',
            'equations': ['advection_diffusion', 'navier_stokes', 'shallow_water'],
            'data_sources': ['Satellite observations', 'Radar data', 'Weather stations'],
            'challenges': ['High-dimensional state space', 'Nonlinear dynamics', 'Sparse observations']
        },
        'ocean_modeling': {
            'name': 'Ocean Modeling',
            'description': 'Ocean circulation and wave prediction',
            'equations': ['shallow_water', 'advection_diffusion', 'navier_stokes'],
            'data_sources': ['Satellite altimetry', 'Buoy measurements', 'Ship observations'],
            'challenges': ['Multi-scale dynamics', 'Boundary conditions', 'Data sparsity']
        },
        'additive_manufacturing': {
            'name': 'Additive Manufacturing',
            'description': 'Real-time process monitoring and control',
            'equations': ['thermal_stress', 'stefan_condition', 'phase_field'],
            'data_sources': ['Thermal imaging', 'Strain gauges', 'Optical sensors'],
            'challenges': ['Multi-physics coupling', 'Moving boundaries', 'Real-time requirements']
        },
        'material_science': {
            'name': 'Material Science',
            'description': 'Microstructure evolution and property prediction',
            'equations': ['phase_field', 'cahn_hilliard', 'thermal_stress'],
            'data_sources': ['X-ray diffraction', 'Microscopy', 'Mechanical testing'],
            'challenges': ['Multi-scale modeling', 'Phase transitions', 'Experimental validation']
        },
        'remote_sensing': {
            'name': 'Remote Sensing',
            'description': 'Satellite data assimilation and environmental monitoring',
            'equations': ['radiative_transfer', 'advection_diffusion', 'heat'],
            'data_sources': ['Satellite imagery', 'Ground sensors', 'Aircraft measurements'],
            'challenges': ['Atmospheric correction', 'Spatial resolution', 'Temporal coverage']
        },
        'biomechanics': {
            'name': 'Biomechanics',
            'description': 'Biological tissue modeling and medical applications',
            'equations': ['poroelasticity', 'navier_stokes', 'advection_diffusion'],
            'data_sources': ['MRI', 'CT scans', 'Biomechanical testing'],
            'challenges': ['Patient-specific modeling', 'Multi-scale physics', 'Validation data']
        },
        'geophysics': {
            'name': 'Geophysics',
            'description': 'Subsurface imaging and natural hazard prediction',
            'equations': ['wave', 'poroelasticity', 'advection_diffusion'],
            'data_sources': ['Seismic data', 'Gravity measurements', 'Well logs'],
            'challenges': ['Inverse problems', 'Nonlinear relationships', 'Sparse data']
        }
    }
    
    # Data Assimilation Loss Function Components
    DATA_ASSIMILATION_LOSS_COMPONENTS = {
        'data_mismatch': {
            'name': 'Data Mismatch Loss',
            'formula': 'L_data = (1/N_d) Σ|u(x_i,t_i) - u_obs(x_i,t_i)|²',
            'description': 'Ensures neural network fits observed data points',
            'weight_range': [0.1, 100.0],
            'default_weight': 10.0
        },
        'physics_residual': {
            'name': 'Physics Residual Loss',
            'formula': 'L_physics = (1/N_r) Σ|N[u](x_j,t_j)|²',
            'description': 'Enforces governing physical equations at collocation points',
            'weight_range': [0.1, 10.0],
            'default_weight': 1.0
        },
        'boundary_conditions': {
            'name': 'Boundary Condition Loss',
            'formula': 'L_bc = (1/N_bc) Σ|u(x_bc,t) - u_bc|²',
            'description': 'Ensures solution satisfies boundary conditions',
            'weight_range': [0.1, 10.0],
            'default_weight': 1.0
        },
        'initial_conditions': {
            'name': 'Initial Condition Loss',
            'formula': 'L_ic = (1/N_ic) Σ|u(x,t=0) - u_ic(x)|²',
            'description': 'Ensures solution satisfies initial conditions',
            'weight_range': [0.1, 10.0],
            'default_weight': 1.0
        },
        'regularization': {
            'name': 'Regularization Loss',
            'formula': 'L_reg = λ||∇u||²',
            'description': 'Prevents overfitting and ensures smooth solutions',
            'weight_range': [0.001, 1.0],
            'default_weight': 0.01
        }
    }

    # Enhanced Control & Optimization Applications
    CONTROL_OPTIMIZATION_APPLICATIONS = {
        'mechanical_systems': {
            'name': 'Mechanical Systems',
            'description': 'Vibration control and optimal actuator placement',
            'equations': ['optimal_control_shm', 'wave_control', 'linear_dynamics'],
            'control_objectives': ['Vibration suppression', 'Trajectory tracking', 'Energy minimization'],
            'challenges': ['Nonlinear dynamics', 'Real-time constraints', 'Multi-body interactions']
        },
        'aerospace': {
            'name': 'Aerospace',
            'description': 'Aircraft optimization and satellite control',
            'equations': ['fluid_control', 'linear_dynamics', 'thermal_control'],
            'control_objectives': ['Drag reduction', 'Attitude control', 'Thermal management'],
            'challenges': ['High-dimensional dynamics', 'Safety constraints', 'Environmental factors']
        },
        'additive_manufacturing': {
            'name': 'Additive Manufacturing',
            'description': '3D printing process optimization and control',
            'equations': ['additive_manufacturing_control', 'thermal_control', 'material_control'],
            'control_objectives': ['Defect minimization', 'Stress reduction', 'Quality optimization'],
            'challenges': ['Multi-physics coupling', 'Real-time control', 'Process variability']
        },
        'material_science': {
            'name': 'Material Science',
            'description': 'Microstructure control and material property optimization',
            'equations': ['material_control', 'phase_field', 'cahn_hilliard'],
            'control_objectives': ['Grain size control', 'Phase transformation', 'Property optimization'],
            'challenges': ['Multi-scale modeling', 'Experimental validation', 'Processing constraints']
        },
        'energy_systems': {
            'name': 'Energy Systems',
            'description': 'Power grid optimization and renewable energy control',
            'equations': ['hjb_equation', 'linear_dynamics', 'thermal_control'],
            'control_objectives': ['Grid stability', 'Efficiency maximization', 'Cost minimization'],
            'challenges': ['Large-scale systems', 'Uncertainty', 'Real-time operation']
        },
        'healthcare': {
            'name': 'Healthcare',
            'description': 'Medical device control and therapeutic optimization',
            'equations': ['linear_dynamics', 'advection_diffusion', 'fluid_control'],
            'control_objectives': ['Drug delivery', 'Blood flow control', 'Device optimization'],
            'challenges': ['Patient-specific modeling', 'Safety constraints', 'Clinical validation']
        },
        'autonomous_systems': {
            'name': 'Autonomous Systems',
            'description': 'Robotics, autonomous vehicles, and smart systems',
            'equations': ['nonlinear_dynamics', 'hjb_equation', 'multi_objective_control'],
            'control_objectives': ['Path planning', 'Obstacle avoidance', 'Multi-agent coordination'],
            'challenges': ['Complex environments', 'Real-time decision making', 'Safety assurance']
        }
    }
    
    # Control & Optimization Loss Function Components
    CONTROL_OPTIMIZATION_LOSS_COMPONENTS = {
        'data_fidelity': {
            'name': 'Data Fidelity Loss',
            'formula': 'L_data = (1/N_d) Σ|u(x_i,t_i) - u_obs(x_i,t_i)|²',
            'description': 'Ensures neural network fits observed data points',
            'weight_range': [0.1, 100.0],
            'default_weight': 1.0
        },
        'physics_constraint': {
            'name': 'Physics Constraint Loss',
            'formula': 'L_physics = (1/N_r) Σ|N[u](x_j,t_j)|²',
            'description': 'Enforces governing physical equations',
            'weight_range': [0.1, 10.0],
            'default_weight': 1.0
        },
        'control_objective': {
            'name': 'Control Objective Loss',
            'formula': 'L_control = ∫[L(x,u,t) + Φ(x(T))]dt',
            'description': 'Minimizes control/optimization cost functional',
            'weight_range': [0.1, 50.0],
            'default_weight': 10.0
        },
        'boundary_conditions': {
            'name': 'Boundary Condition Loss',
            'formula': 'L_bc = (1/N_bc) Σ|u(x_bc,t) - u_bc|²',
            'description': 'Ensures solution satisfies boundary conditions',
            'weight_range': [0.1, 10.0],
            'default_weight': 1.0
        },
        'initial_conditions': {
            'name': 'Initial Condition Loss',
            'formula': 'L_ic = (1/N_ic) Σ|u(x,t=0) - u_ic(x)|²',
            'description': 'Ensures solution satisfies initial conditions',
            'weight_range': [0.1, 10.0],
            'default_weight': 1.0
        },
        'regularization': {
            'name': 'Regularization Loss',
            'formula': 'L_reg = λ||∇u||² + μ||u||²',
            'description': 'Prevents overfitting and ensures smooth solutions',
            'weight_range': [0.001, 1.0],
            'default_weight': 0.01
        },
        'constraint_penalty': {
            'name': 'Constraint Penalty Loss',
            'formula': 'L_constraint = Σ max(0, g_i(x,u))²',
            'description': 'Penalizes constraint violations',
            'weight_range': [0.1, 100.0],
            'default_weight': 10.0
        }
    }
    
    # Optimal Control Problem Types
    OPTIMAL_CONTROL_TYPES = {
        'linear_quadratic': {
            'name': 'Linear Quadratic (LQ) Control',
            'description': 'Linear dynamics with quadratic cost function',
            'formula': 'J = ∫(x^T Q x + u^T R u)dt',
            'applications': ['Robotics', 'Aerospace', 'Process control'],
            'advantages': ['Analytical solutions', 'Stability guarantees', 'Computational efficiency']
        },
        'nonlinear_optimal': {
            'name': 'Nonlinear Optimal Control',
            'description': 'Nonlinear dynamics with general cost function',
            'formula': 'J = ∫L(x,u,t)dt + Φ(x(T))',
            'applications': ['Autonomous vehicles', 'Biological systems', 'Complex dynamics'],
            'advantages': ['Handles nonlinearities', 'General cost functions', 'Real-world applicability']
        },
        'model_predictive': {
            'name': 'Model Predictive Control (MPC)',
            'description': 'Receding horizon optimization with constraints',
            'formula': 'min_u ∫[t,t+H] L(x,u)dt subject to constraints',
            'applications': ['Chemical processes', 'Autonomous systems', 'Energy management'],
            'advantages': ['Constraint handling', 'Robustness', 'Real-time adaptation']
        },
        'robust_control': {
            'name': 'Robust Control',
            'description': 'Control under uncertainty and disturbances',
            'formula': 'min_u max_w J(x,u,w)',
            'applications': ['Aerospace', 'Manufacturing', 'Healthcare'],
            'advantages': ['Uncertainty handling', 'Disturbance rejection', 'Safety guarantees']
        },
        'adaptive_control': {
            'name': 'Adaptive Control',
            'description': 'Online parameter estimation and control',
            'formula': 'u = K(θ̂)x where θ̂ is estimated parameter',
            'applications': ['Robotics', 'Aerospace', 'Biomedical systems'],
            'advantages': ['Parameter adaptation', 'Online learning', 'Performance improvement']
        }
    }

    # Forward Problems Research Applications
    FORWARD_PROBLEMS_APPLICATIONS = {
        "additive_manufacturing": {
            "name": "Additive Manufacturing",
            "description": "3D printing process simulation and optimization",
            "equations": [
                "heat_transfer_phase_change",
                "stefan_condition",
                "navier_stokes_free_surface",
                "thermal_stress"
            ],
            "challenges": [
                "Multi-physics coupling",
                "Moving boundaries",
                "Real-time control"
            ],
            "benefits": [
                "Process optimization",
                "Defect prevention",
                "Quality improvement"
            ]
        },
        "material_science": {
            "name": "Material Science",
            "description": "Microstructure evolution and material property prediction",
            "equations": [
                "phase_field",
                "cahn_hilliard",
                "fick_second_law",
                "crystal_plasticity"
            ],
            "challenges": [
                "Multi-scale modeling",
                "Phase transitions",
                "Experimental validation"
            ],
            "benefits": [
                "Accelerated design",
                "Property optimization",
                "Process understanding"
            ]
        },
        "battery_systems": {
            "name": "Battery and Energy Systems",
            "description": "Electrochemical transport and thermal management",
            "equations": [
                "advection_diffusion",
                "heat_transfer_phase_change",
                "thermal_stress"
            ],
            "challenges": [
                "Multi-physics coupling",
                "Safety constraints",
                "Performance optimization"
            ],
            "benefits": [
                "Enhanced safety",
                "Improved performance",
                "Extended lifetime"
            ]
        },
        "biomechanics": {
            "name": "Biomechanics",
            "description": "Biological tissue modeling and medical applications",
            "equations": [
                "poroelasticity",
                "viscoelasticity",
                "advection_diffusion"
            ],
            "challenges": [
                "Patient-specific modeling",
                "Multi-scale physics",
                "Validation data"
            ],
            "benefits": [
                "Personalized medicine",
                "Reduced experimental costs",
                "Better treatments"
            ]
        },
        "geophysics": {
            "name": "Geophysics",
            "description": "Subsurface imaging and natural hazard prediction",
            "equations": [
                "elastic_wave",
                "poroelasticity",
                "advection_diffusion"
            ],
            "challenges": [
                "Inverse problems",
                "Nonlinear relationships",
                "Sparse data"
            ],
            "benefits": [
                "Resource exploration",
                "Hazard prediction",
                "Environmental monitoring"
            ]
        },
        "fusion_energy": {
            "name": "Fusion Energy",
            "description": "Plasma dynamics and reactor design",
            "equations": [
                "magnetohydrodynamics",
                "heat_transfer_phase_change",
                "thermal_stress"
            ],
            "challenges": [
                "High-dimensional systems",
                "Complex physics",
                "Safety requirements"
            ],
            "benefits": [
                "Clean energy",
                "Advanced physics",
                "Technology development"
            ]
        },
        "climate_modeling": {
            "name": "Climate Modeling",
            "description": "Atmospheric and oceanic circulation modeling",
            "equations": [
                "advection_diffusion",
                "shallow_water",
                "radiative_transfer"
            ],
            "challenges": [
                "Multi-scale dynamics",
                "Uncertainty quantification",
                "Computational cost"
            ],
            "benefits": [
                "Climate prediction",
                "Policy support",
                "Risk assessment"
            ]
        },
        "nanotechnology": {
            "name": "Nanotechnology",
            "description": "Nanoscale phenomena and device modeling",
            "equations": [
                "phase_field",
                "cahn_hilliard",
                "reaction_diffusion"
            ],
            "challenges": [
                "Quantum effects",
                "Surface phenomena",
                "Fabrication constraints"
            ],
            "benefits": [
                "Device optimization",
                "Material design",
                "Process control"
            ]
        },
        "aerospace": {
            "name": "Aerospace Engineering",
            "description": "Aircraft and spacecraft design optimization",
            "equations": [
                "navier_stokes_free_surface",
                "thermoelasticity",
                "elastic_wave"
            ],
            "challenges": [
                "High-speed flows",
                "Thermal management",
                "Structural integrity"
            ],
            "benefits": [
                "Performance improvement",
                "Safety enhancement",
                "Cost reduction"
            ]
        },
        "biomedical": {
            "name": "Biomedical Engineering",
            "description": "Medical device design and therapeutic optimization",
            "equations": [
                "poroelasticity",
                "advection_diffusion",
                "viscoelasticity"
            ],
            "challenges": [
                "Patient variability",
                "Safety requirements",
                "Clinical validation"
            ],
            "benefits": [
                "Better treatments",
                "Reduced side effects",
                "Personalized care"
            ]
        },
        "renewable_energy": {
            "name": "Renewable Energy",
            "description": "Solar, wind, and other renewable energy systems",
            "equations": [
                "radiative_transfer",
                "navier_stokes_free_surface",
                "thermoelasticity"
            ],
            "challenges": [
                "Intermittency",
                "Storage requirements",
                "Grid integration"
            ],
            "benefits": [
                "Efficiency improvement",
                "Cost reduction",
                "Sustainability"
            ]
        }
    }

    # Forward Problems Loss Function Components
    FORWARD_PROBLEMS_LOSS_COMPONENTS = {
        "physics_residual": {
            "name": "Physics Residual Loss",
            "formula": "L_physics = (1/N_r) \u03a3|N[u](x_i,t_i)|\u00b2",
            "description": "Enforces governing physical equations at collocation points",
            "weight_range": [
                0.1,
                10.0
            ],
            "default_weight": 1.0
        },
        "boundary_conditions": {
            "name": "Boundary Condition Loss",
            "formula": "L_bc = (1/N_bc) \u03a3|u(x_bc,t) - u_bc|\u00b2",
            "description": "Ensures solution satisfies boundary conditions",
            "weight_range": [
                0.1,
                10.0
            ],
            "default_weight": 1.0
        },
        "initial_conditions": {
            "name": "Initial Condition Loss",
            "formula": "L_ic = (1/N_ic) \u03a3|u(x,t=0) - u_ic(x)|\u00b2",
            "description": "Ensures solution satisfies initial conditions",
            "weight_range": [
                0.1,
                10.0
            ],
            "default_weight": 1.0
        },
        "interface_conditions": {
            "name": "Interface Condition Loss",
            "formula": "L_interface = (1/N_i) \u03a3|f_interface(u_s,u_l)|\u00b2",
            "description": "Enforces conditions at phase interfaces or domain boundaries",
            "weight_range": [
                0.1,
                10.0
            ],
            "default_weight": 1.0
        },
        "conservation_laws": {
            "name": "Conservation Law Loss",
            "formula": "L_conservation = (1/N_c) \u03a3|\u2207\u00b7J + \u2202\u03c1/\u2202t|\u00b2",
            "description": "Enforces mass, momentum, or energy conservation",
            "weight_range": [
                0.1,
                10.0
            ],
            "default_weight": 1.0
        },
        "regularization": {
            "name": "Regularization Loss",
            "formula": "L_reg = \u03bb||\u2207u||\u00b2 + \u03bc||u||\u00b2",
            "description": "Prevents overfitting and ensures smooth solutions",
            "weight_range": [
                0.001,
                1.0
            ],
            "default_weight": 0.01
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