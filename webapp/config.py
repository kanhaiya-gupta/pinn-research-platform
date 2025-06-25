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
    ,
        'heat_transfer_phase_change_inverse': {
            "name": "Heat Transfer with Phase Change (Inverse)",
            "description": "Inverse problem for thermal processes with melting/solidification in additive manufacturing",
            "icon": "fas fa-thermometer-half",
            "color": "#e74c3c",
            "formula": "\u03c1c_p \u2202T/\u2202t = \u2207\u00b7(k\u2207T) + Q - L \u2202f_s/\u2202t",
            "purposes": [
                        "inverse_problems",
                        "additive_manufacturing",
                        "multiphysics"
            ],
            "applications": [
                        "Material characterization",
                        "Heat source identification",
                        "Phase change modeling"
            ]
},
        'stefan_condition_inverse': {
            "name": "Stefan Condition (Inverse)",
            "description": "Inverse problem for moving phase interfaces",
            "icon": "fas fa-arrows-alt-h",
            "color": "#9b59b6",
            "formula": "k_s \u2207T_s\u00b7n - k_l \u2207T_l\u00b7n = \u03c1L v_n",
            "purposes": [
                        "inverse_problems",
                        "additive_manufacturing",
                        "multiphysics"
            ],
            "applications": [
                        "Melt pool boundary tracking",
                        "Solidification rate inference"
            ]
},
        'navier_stokes_free_surface_inverse': {
            "name": "Navier-Stokes with Free Surface (Inverse)",
            "description": "Inverse problem for fluid flow in melt pools with surface tension effects",
            "icon": "fas fa-water",
            "color": "#3498db",
            "formula": "\u03c1(\u2202v/\u2202t + v\u00b7\u2207v) = -\u2207p + \u03bc\u2207\u00b2v + f_surface, \u2207\u00b7v = 0",
            "purposes": [
                        "inverse_problems",
                        "additive_manufacturing",
                        "multiphysics"
            ],
            "applications": [
                        "Melt pool dynamics",
                        "Keyhole formation",
                        "Surface tension estimation"
            ]
},
        'thermal_stress_inverse': {
            "name": "Thermal Stress Equation (Inverse)",
            "description": "Inverse problem for residual stresses due to thermal gradients",
            "icon": "fas fa-compress-arrows-alt",
            "color": "#f39c12",
            "formula": "\u2207\u00b7\u03c3 = 0, \u03c3 = C:(\u03b5 - \u03b5_th)",
            "purposes": [
                        "inverse_problems",
                        "additive_manufacturing",
                        "multiphysics"
            ],
            "applications": [
                        "Material characterization",
                        "Residual stress analysis"
            ]
},
        'phase_field_inverse': {
            "name": "Phase-Field Equation (Inverse)",
            "description": "Inverse problem for microstructure evolution in materials",
            "icon": "fas fa-atom",
            "color": "#1abc9c",
            "formula": "\u2202\u03c6/\u2202t = -M \u03b4F/\u03b4\u03c6",
            "purposes": [
                        "inverse_problems",
                        "material_science",
                        "multiphysics"
            ],
            "applications": [
                        "Grain growth",
                        "Phase transformation",
                        "Free energy reconstruction"
            ]
},
        'cahn_hilliard_inverse': {
            "name": "Cahn-Hilliard Equation (Inverse)",
            "description": "Inverse problem for phase separation and diffusion in materials",
            "icon": "fas fa-layer-group",
            "color": "#34495e",
            "formula": "\u2202c/\u2202t = \u2207\u00b7(M\u2207\u03bc), \u03bc = \u03b4F/\u03b4c",
            "purposes": [
                        "inverse_problems",
                        "material_science",
                        "multiphysics"
            ],
            "applications": [
                        "Spinodal decomposition",
                        "Thin film growth",
                        "Diffusion coefficient estimation"
            ]
},
        'fick_second_law_inverse': {
            "name": "Fick's Second Law (Inverse)",
            "description": "Inverse problem for diffusion processes in materials",
            "icon": "fas fa-exchange-alt",
            "color": "#27ae60",
            "formula": "\u2202c/\u2202t = \u2207\u00b7(D\u2207c)",
            "purposes": [
                        "inverse_problems",
                        "material_science",
                        "efficiency"
            ],
            "applications": [
                        "Dopant diffusion",
                        "Hydrogen diffusion",
                        "Drug diffusion"
            ]
},
        'crystal_plasticity_inverse': {
            "name": "Crystal Plasticity Equations (Inverse)",
            "description": "Inverse problem for plastic deformation in crystalline materials",
            "icon": "fas fa-cube",
            "color": "#8e44ad",
            "formula": "\u03b5\u0307^p = \u03a3_\u03b1 \u03b3\u0307^\u03b1 m^\u03b1, \u03b3\u0307^\u03b1 = f(\u03c4^\u03b1, s^\u03b1)",
            "purposes": [
                        "inverse_problems",
                        "material_science",
                        "multiphysics"
            ],
            "applications": [
                        "Deformation modeling",
                        "Fatigue analysis",
                        "Slip resistance estimation"
            ]
},
        'nernst_planck_inverse': {
            "name": "Nernst-Planck Equation (Inverse)",
            "description": "Inverse problem for electrochemical transport in batteries",
            "icon": "fas fa-battery-three-quarters",
            "color": "#16a085",
            "formula": "\u2202c/\u2202t = \u2207\u00b7(D\u2207c + \u03bcc\u2207\u03c6)",
            "purposes": [
                        "inverse_problems",
                        "battery_systems",
                        "multiphysics"
            ],
            "applications": [
                        "Battery parameter estimation",
                        "Electrochemical property inference"
            ]
},
        'poroelasticity_inverse': {
            "name": "Poroelasticity Equations (Inverse)",
            "description": "Inverse problem for fluid-saturated porous media",
            "icon": "fas fa-filter",
            "color": "#d35400",
            "formula": "\u2207\u00b7\u03c3 = 0, \u2202\u03b6/\u2202t + \u2207\u00b7q = 0",
            "purposes": [
                        "inverse_problems",
                        "biomechanics",
                        "geophysics"
            ],
            "applications": [
                        "Tissue property estimation",
                        "Groundwater flow parameter estimation"
            ]
},
        'magnetohydrodynamics_inverse': {
            "name": "Magnetohydrodynamics (Inverse)",
            "description": "Inverse problem for electrically conducting fluids in magnetic fields",
            "icon": "fas fa-magnet",
            "color": "#8e44ad",
            "formula": "\u03c1(\u2202v/\u2202t + v\u00b7\u2207v) = -\u2207p + \u03bc\u2207\u00b2v + J\u00d7B, \u2202B/\u2202t = \u2207\u00d7(v\u00d7B) + \u03b7\u2207\u00b2B",
            "purposes": [
                        "inverse_problems",
                        "fusion_energy",
                        "multiphysics"
            ],
            "applications": [
                        "Plasma property inference",
                        "Magnetic field parameter estimation"
            ]
},
        'darcy_law_inverse': {
            "name": "Darcy's Law (Inverse)",
            "description": "Inverse problem for flow through porous media",
            "icon": "fas fa-tint",
            "color": "#2980b9",
            "formula": "q = -k/\u03bc \u2207p",
            "purposes": [
                        "inverse_problems",
                        "geophysics",
                        "biomechanics"
            ],
            "applications": [
                        "Permeability estimation",
                        "Groundwater flow analysis"
            ]
},
        'reaction_kinetics_inverse': {
            "name": "Reaction Kinetics (Inverse)",
            "description": "Inverse problem for chemical reaction rates and parameters",
            "icon": "fas fa-flask",
            "color": "#e67e22",
            "formula": "dc/dt = -k c^n",
            "purposes": [
                        "inverse_problems",
                        "battery_systems",
                        "material_science"
            ],
            "applications": [
                        "Reaction rate estimation",
                        "Catalyst parameter inference"
            ]
},
        'heat_transfer_phase_change_sparse': {
            "name": "Heat Transfer with Phase Change (Sparse Data)",
            "description": "Reconstruct temperature field or infer parameters from sparse/noisy thermal measurements in additive manufacturing",
            "icon": "fas fa-thermometer-half",
            "color": "#e74c3c",
            "formula": "\u03c1c_p \u2202T/\u2202t = \u2207\u00b7(k\u2207T) + Q - L \u2202f_s/\u2202t",
            "purposes": [
                        "sparse_data",
                        "additive_manufacturing",
                        "multiphysics"
            ],
            "applications": [
                        "Melt pool dynamics",
                        "Thermal history prediction",
                        "Solidification modeling"
            ]
},
        'stefan_condition_sparse': {
            "name": "Stefan Condition (Sparse Data)",
            "description": "Reconstruct interface position or infer parameters from sparse/noisy boundary data",
            "icon": "fas fa-arrows-alt-h",
            "color": "#9b59b6",
            "formula": "k_s \u2207T_s\u00b7n - k_l \u2207T_l\u00b7n = \u03c1L v_n",
            "purposes": [
                        "sparse_data",
                        "additive_manufacturing",
                        "multiphysics"
            ],
            "applications": [
                        "Melt pool boundary tracking",
                        "Solidification rate inference"
            ]
},
        'navier_stokes_free_surface_sparse': {
            "name": "Navier-Stokes with Free Surface (Sparse Data)",
            "description": "Reconstruct velocity field or infer parameters from sparse/noisy velocity measurements",
            "icon": "fas fa-water",
            "color": "#3498db",
            "formula": "\u03c1(\u2202v/\u2202t + v\u00b7\u2207v) = -\u2207p + \u03bc\u2207\u00b2v + f_surface, \u2207\u00b7v = 0",
            "purposes": [
                        "sparse_data",
                        "additive_manufacturing",
                        "multiphysics"
            ],
            "applications": [
                        "Melt pool dynamics",
                        "Keyhole formation",
                        "Surface tension effects"
            ]
},
        'thermal_stress_sparse': {
            "name": "Thermal Stress Equation (Sparse Data)",
            "description": "Reconstruct stress field or infer parameters from sparse/noisy stress or displacement data",
            "icon": "fas fa-compress-arrows-alt",
            "color": "#f39c12",
            "formula": "\u2207\u00b7\u03c3 = 0, \u03c3 = C:(\u03b5 - \u03b5_th)",
            "purposes": [
                        "sparse_data",
                        "additive_manufacturing",
                        "multiphysics"
            ],
            "applications": [
                        "Residual stress prediction",
                        "Warping analysis",
                        "Cracking analysis"
            ]
},
        'phase_field_sparse': {
            "name": "Phase-Field Equation (Sparse Data)",
            "description": "Reconstruct microstructure or infer parameters from sparse/noisy microscopy data",
            "icon": "fas fa-atom",
            "color": "#1abc9c",
            "formula": "\u2202\u03c6/\u2202t = -M \u03b4F/\u03b4\u03c6",
            "purposes": [
                        "sparse_data",
                        "material_science",
                        "multiphysics"
            ],
            "applications": [
                        "Grain growth",
                        "Phase transformation",
                        "Solidification"
            ]
},
        'cahn_hilliard_sparse': {
            "name": "Cahn-Hilliard Equation (Sparse Data)",
            "description": "Reconstruct concentration field or infer parameters from sparse/noisy concentration data",
            "icon": "fas fa-layer-group",
            "color": "#34495e",
            "formula": "\u2202c/\u2202t = \u2207\u00b7(M\u2207\u03bc), \u03bc = \u03b4F/\u03b4c",
            "purposes": [
                        "sparse_data",
                        "material_science",
                        "multiphysics"
            ],
            "applications": [
                        "Spinodal decomposition",
                        "Thin film growth",
                        "Battery materials"
            ]
},
        'fick_second_law_sparse': {
            "name": "Fick's Second Law (Sparse Data)",
            "description": "Reconstruct concentration or infer diffusivity from sparse/noisy measurements",
            "icon": "fas fa-exchange-alt",
            "color": "#27ae60",
            "formula": "\u2202c/\u2202t = \u2207\u00b7(D\u2207c)",
            "purposes": [
                        "sparse_data",
                        "material_science",
                        "efficiency"
            ],
            "applications": [
                        "Dopant diffusion",
                        "Hydrogen diffusion",
                        "Drug diffusion"
            ]
},
        'crystal_plasticity_sparse': {
            "name": "Crystal Plasticity Equations (Sparse Data)",
            "description": "Reconstruct strain field or infer slip parameters from sparse/noisy deformation data",
            "icon": "fas fa-cube",
            "color": "#8e44ad",
            "formula": "\u03b5\u0307^p = \u03a3_\u03b1 \u03b3\u0307^\u03b1 m^\u03b1, \u03b3\u0307^\u03b1 = f(\u03c4^\u03b1, s^\u03b1)",
            "purposes": [
                        "sparse_data",
                        "material_science",
                        "multiphysics"
            ],
            "applications": [
                        "Deformation modeling",
                        "Fatigue analysis",
                        "Part integrity"
            ]
},
        'nernst_planck_sparse': {
            "name": "Nernst-Planck Equation (Sparse Data)",
            "description": "Reconstruct concentration or infer parameters from sparse/noisy electrochemical data",
            "icon": "fas fa-battery-three-quarters",
            "color": "#16a085",
            "formula": "\u2202c/\u2202t = \u2207\u00b7(D\u2207c + \u03bcc\u2207\u03c6)",
            "purposes": [
                        "sparse_data",
                        "battery_systems",
                        "multiphysics"
            ],
            "applications": [
                        "Battery modeling",
                        "Fuel cell analysis",
                        "Electrochemical transport"
            ]
},
        'poroelasticity_sparse': {
            "name": "Poroelasticity Equations (Sparse Data)",
            "description": "Reconstruct stress or pressure fields from sparse/noisy biomechanical data",
            "icon": "fas fa-filter",
            "color": "#d35400",
            "formula": "\u2207\u00b7\u03c3 = -\u2207p_f, \u2202p_f/\u2202t + \u2207\u00b7(k\u2207p_f) = S",
            "purposes": [
                        "sparse_data",
                        "biomechanics",
                        "geophysics"
            ],
            "applications": [
                        "Tissue mechanics",
                        "Bone mechanics",
                        "Groundwater flow"
            ]
},
        'magnetohydrodynamics_sparse': {
            "name": "Magnetohydrodynamics (Sparse Data)",
            "description": "Reconstruct plasma flow or magnetic field from sparse/noisy diagnostic data",
            "icon": "fas fa-magnet",
            "color": "#8e44ad",
            "formula": "\u03c1(\u2202v/\u2202t + v\u00b7\u2207v) = -\u2207p + J\u00d7B + \u03bc\u2207\u00b2v, \u2202B/\u2202t = \u2207\u00d7(v\u00d7B - \u03b7\u2207\u00d7B)",
            "purposes": [
                        "sparse_data",
                        "fusion_energy",
                        "multiphysics"
            ],
            "applications": [
                        "Plasma dynamics",
                        "Fusion diagnostics",
                        "Space physics"
            ]
},
        'advection_diffusion_sparse': {
            "name": "Advection-Diffusion Equation (Sparse Data)",
            "description": "Reconstruct concentration fields from sparse/noisy transport data",
            "icon": "fas fa-wind",
            "color": "#16a085",
            "formula": "\u2202c/\u2202t + v\u00b7\u2207c = \u2207\u00b7(D\u2207c)",
            "purposes": [
                        "sparse_data",
                        "data_assimilation",
                        "multiphysics"
            ],
            "applications": [
                        "Atmospheric transport",
                        "Ocean currents",
                        "Pollutant dispersion"
            ]
},
        'reaction_diffusion_sparse': {
            "name": "Reaction-Diffusion Equations (Sparse Data)",
            "description": "Reconstruct chemical concentration fields from sparse/noisy reaction data",
            "icon": "fas fa-flask",
            "color": "#e67e22",
            "formula": "\u2202u/\u2202t = D\u2207\u00b2u + f(u,v), \u2202v/\u2202t = D\u2207\u00b2v + g(u,v)",
            "purposes": [
                        "sparse_data",
                        "scientific_discovery",
                        "multiphysics"
            ],
            "applications": [
                        "Chemical kinetics",
                        "Pattern formation",
                        "Biological systems"
            ]
},
        'elastic_wave_sparse': {
            "name": "Elastic Wave Equation (Sparse Data)",
            "description": "Reconstruct wave fields from sparse/noisy seismic data",
            "icon": "fas fa-wave-square",
            "color": "#9b59b6",
            "formula": "\u03c1\u2202\u00b2u/\u2202t\u00b2 = \u2207\u00b7(C:\u2207u)",
            "purposes": [
                        "sparse_data",
                        "geophysics",
                        "multiphysics"
            ],
            "applications": [
                        "Seismic waves",
                        "Ultrasound",
                        "Structural dynamics"
            ]
},
        'viscoelasticity_sparse': {
            "name": "Viscoelasticity Equations (Sparse Data)",
            "description": "Reconstruct deformation fields from sparse/noisy rheological data",
            "icon": "fas fa-tint",
            "color": "#3498db",
            "formula": "\u03c3 + \u03c4\u2202\u03c3/\u2202t = E(\u03b5 + \u03c4_\u03b5\u2202\u03b5/\u2202t)",
            "purposes": [
                        "sparse_data",
                        "material_science",
                        "biomechanics"
            ],
            "applications": [
                        "Polymer mechanics",
                        "Biological tissues",
                        "Rheology"
            ]
},
        'thermoelasticity_sparse': {
            "name": "Thermoelasticity Equations (Sparse Data)",
            "description": "Reconstruct coupled thermal-mechanical fields from sparse/noisy data",
            "icon": "fas fa-thermometer-half",
            "color": "#e74c3c",
            "formula": "\u2207\u00b7\u03c3 = 0, \u03c1c_p\u2202T/\u2202t = \u2207\u00b7(k\u2207T) - T_0\u03b1\u2207\u00b7\u2202u/\u2202t",
            "purposes": [
                        "sparse_data",
                        "additive_manufacturing",
                        "multiphysics"
            ],
            "applications": [
                        "Thermal stress",
                        "Heat exchangers",
                        "Electronic packaging"
            ]
},
        'heat_equation_uq': {
            "name": "Heat Equation (Uncertainty Quantification)",
            "description": "Quantify uncertainty in temperature fields and thermal diffusivity from noisy measurements",
            "icon": "fas fa-thermometer-half",
            "color": "#e74c3c",
            "formula": "\u2202u/\u2202t = \u03b1 \u2202\u00b2u/\u2202x\u00b2",
            "purposes": [
                        "uncertainty",
                        "forward_problems",
                        "multiphysics"
            ],
            "applications": [
                        "Thermal analysis",
                        "Material processing",
                        "Climate modeling"
            ],
            "uq_methods": [
                        "Bayesian PINNs",
                        "Monte Carlo Dropout",
                        "Deep Ensembles"
            ]
},
        'shm_uq': {
            "name": "Simple Harmonic Motion (Uncertainty Quantification)",
            "description": "Quantify uncertainty in displacement and natural frequency from noisy oscillation data",
            "icon": "fas fa-wave-square",
            "color": "#9b59b6",
            "formula": "d\u00b2x/dt\u00b2 + \u03c9\u00b2x = 0",
            "purposes": [
                        "uncertainty",
                        "control_optimization",
                        "multiphysics"
            ],
            "applications": [
                        "Mechanical vibrations",
                        "Electrical circuits",
                        "Molecular dynamics"
            ],
            "uq_methods": [
                        "Bayesian PINNs",
                        "Variational Inference",
                        "Ensemble Methods"
            ]
},
        'navier_stokes_uq': {
            "name": "Navier-Stokes Equations (Uncertainty Quantification)",
            "description": "Quantify uncertainty in velocity, pressure, and viscosity from noisy flow data",
            "icon": "fas fa-water",
            "color": "#3498db",
            "formula": "\u03c1(\u2202v/\u2202t + v\u00b7\u2207v) = -\u2207p + \u03bc\u2207\u00b2v + f, \u2207\u00b7v = 0",
            "purposes": [
                        "uncertainty",
                        "forward_problems",
                        "multiphysics"
            ],
            "applications": [
                        "Aerodynamics",
                        "Oceanography",
                        "Blood flow modeling"
            ],
            "uq_methods": [
                        "Bayesian PINNs",
                        "Monte Carlo Sampling",
                        "Gaussian Processes"
            ]
},
        'schrodinger_uq': {
            "name": "Schr\u00f6dinger Equation (Uncertainty Quantification)",
            "description": "Quantify uncertainty in wave functions and Hamiltonian parameters from noisy quantum data",
            "icon": "fas fa-atom",
            "color": "#1abc9c",
            "formula": "i\u210f \u2202\u03c8/\u2202t = \u0124\u03c8",
            "purposes": [
                        "uncertainty",
                        "scientific_discovery",
                        "multiphysics"
            ],
            "applications": [
                        "Quantum chemistry",
                        "Material properties",
                        "Quantum computing"
            ],
            "uq_methods": [
                        "Bayesian PINNs",
                        "Variational Quantum Eigensolver",
                        "Ensemble Methods"
            ]
},
        'maxwell_uq': {
            "name": "Maxwell Equations (Uncertainty Quantification)",
            "description": "Quantify uncertainty in electromagnetic fields and material properties from noisy field data",
            "icon": "fas fa-magnet",
            "color": "#8e44ad",
            "formula": "\u2207\u00b7E = \u03c1/\u03b5\u2080, \u2207\u00d7E = -\u2202B/\u2202t, \u2207\u00b7B = 0, \u2207\u00d7B = \u03bc\u2080J + \u03bc\u2080\u03b5\u2080\u2202E/\u2202t",
            "purposes": [
                        "uncertainty",
                        "forward_problems",
                        "multiphysics"
            ],
            "applications": [
                        "Antenna design",
                        "Optical systems",
                        "Electromagnetic compatibility"
            ],
            "uq_methods": [
                        "Bayesian PINNs",
                        "Monte Carlo Methods",
                        "Gaussian Processes"
            ]
},
        'multi_objective_control_uq': {
            "name": "Multi-Objective Control (Uncertainty Quantification)",
            "description": "Quantify uncertainty in control inputs and objectives from noisy optimization data",
            "icon": "fas fa-sliders-h",
            "color": "#f39c12",
            "formula": "J = \u03a3 w_i J_i",
            "purposes": [
                        "uncertainty",
                        "control_optimization",
                        "multiphysics"
            ],
            "applications": [
                        "Autonomous systems",
                        "Smart cities",
                        "Healthcare",
                        "Environmental control"
            ],
            "uq_methods": [
                        "Bayesian Optimization",
                        "Robust Control",
                        "Stochastic Programming"
            ]
},
        'heat_transfer_phase_change_uq': {
            "name": "Heat Transfer with Phase Change (Uncertainty Quantification)",
            "description": "Quantify uncertainty in temperature fields and phase change parameters from noisy thermal data",
            "icon": "fas fa-thermometer-half",
            "color": "#e74c3c",
            "formula": "\u03c1c_p \u2202T/\u2202t = \u2207\u00b7(k\u2207T) + Q - L \u2202f_s/\u2202t",
            "purposes": [
                        "uncertainty",
                        "additive_manufacturing",
                        "multiphysics"
            ],
            "applications": [
                        "Melt pool dynamics",
                        "Thermal history prediction",
                        "Solidification modeling"
            ],
            "uq_methods": [
                        "Bayesian PINNs",
                        "Monte Carlo Dropout",
                        "Variational Inference"
            ]
},
        'stefan_condition_uq': {
            "name": "Stefan Condition (Uncertainty Quantification)",
            "description": "Quantify uncertainty in thermal conductivities and latent heat from noisy boundary data",
            "icon": "fas fa-arrows-alt-h",
            "color": "#9b59b6",
            "formula": "k_s \u2207T_s\u00b7n - k_l \u2207T_l\u00b7n = \u03c1L v_n",
            "purposes": [
                        "uncertainty",
                        "additive_manufacturing",
                        "multiphysics"
            ],
            "applications": [
                        "Melt pool boundary tracking",
                        "Solidification rate inference"
            ],
            "uq_methods": [
                        "Bayesian PINNs",
                        "Gaussian Processes",
                        "Ensemble Methods"
            ]
},
        'navier_stokes_free_surface_uq': {
            "name": "Navier-Stokes with Free Surface (Uncertainty Quantification)",
            "description": "Quantify uncertainty in velocity fields and surface forces from noisy flow data",
            "icon": "fas fa-water",
            "color": "#3498db",
            "formula": "\u03c1(\u2202v/\u2202t + v\u00b7\u2207v) = -\u2207p + \u03bc\u2207\u00b2v + f_surface, \u2207\u00b7v = 0",
            "purposes": [
                        "uncertainty",
                        "additive_manufacturing",
                        "multiphysics"
            ],
            "applications": [
                        "Melt pool dynamics",
                        "Keyhole formation",
                        "Surface tension effects"
            ],
            "uq_methods": [
                        "Bayesian PINNs",
                        "Monte Carlo Sampling",
                        "Variational Inference"
            ]
},
        'thermal_stress_uq': {
            "name": "Thermal Stress Equation (Uncertainty Quantification)",
            "description": "Quantify uncertainty in stress fields and elastic properties from noisy mechanical data",
            "icon": "fas fa-compress-arrows-alt",
            "color": "#f39c12",
            "formula": "\u2207\u00b7\u03c3 = 0, \u03c3 = C:(\u03b5 - \u03b5_th)",
            "purposes": [
                        "uncertainty",
                        "additive_manufacturing",
                        "multiphysics"
            ],
            "applications": [
                        "Residual stress prediction",
                        "Warping analysis",
                        "Cracking analysis"
            ],
            "uq_methods": [
                        "Bayesian PINNs",
                        "Monte Carlo Methods",
                        "Ensemble Methods"
            ]
},
        'phase_field_uq': {
            "name": "Phase-Field Equation (Uncertainty Quantification)",
            "description": "Quantify uncertainty in microstructure evolution and mobility parameters from noisy microscopy data",
            "icon": "fas fa-atom",
            "color": "#1abc9c",
            "formula": "\u2202\u03c6/\u2202t = -M \u03b4F/\u03b4\u03c6",
            "purposes": [
                        "uncertainty",
                        "material_science",
                        "multiphysics"
            ],
            "applications": [
                        "Grain growth",
                        "Phase transformation",
                        "Solidification"
            ],
            "uq_methods": [
                        "Bayesian PINNs",
                        "Variational Inference",
                        "Gaussian Processes"
            ]
},
        'cahn_hilliard_uq': {
            "name": "Cahn-Hilliard Equation (Uncertainty Quantification)",
            "description": "Quantify uncertainty in concentration fields and diffusion parameters from noisy concentration data",
            "icon": "fas fa-layer-group",
            "color": "#34495e",
            "formula": "\u2202c/\u2202t = \u2207\u00b7(M\u2207\u03bc), \u03bc = \u03b4F/\u03b4c",
            "purposes": [
                        "uncertainty",
                        "material_science",
                        "multiphysics"
            ],
            "applications": [
                        "Spinodal decomposition",
                        "Thin film growth",
                        "Battery materials"
            ],
            "uq_methods": [
                        "Bayesian PINNs",
                        "Monte Carlo Methods",
                        "Variational Inference"
            ]
},
        'fick_second_law_uq': {
            "name": "Fick's Second Law (Uncertainty Quantification)",
            "description": "Quantify uncertainty in concentration fields and diffusivity from noisy diffusion data",
            "icon": "fas fa-exchange-alt",
            "color": "#27ae60",
            "formula": "\u2202c/\u2202t = \u2207\u00b7(D\u2207c)",
            "purposes": [
                        "uncertainty",
                        "material_science",
                        "efficiency"
            ],
            "applications": [
                        "Dopant diffusion",
                        "Hydrogen diffusion",
                        "Drug diffusion"
            ],
            "uq_methods": [
                        "Bayesian PINNs",
                        "Gaussian Processes",
                        "Ensemble Methods"
            ]
},
        'crystal_plasticity_uq': {
            "name": "Crystal Plasticity Equations (Uncertainty Quantification)",
            "description": "Quantify uncertainty in strain fields and slip parameters from noisy deformation data",
            "icon": "fas fa-cube",
            "color": "#8e44ad",
            "formula": "\u03b5\u0307^p = \u03a3_\u03b1 \u03b3\u0307^\u03b1 m^\u03b1, \u03b3\u0307^\u03b1 = f(\u03c4^\u03b1, s^\u03b1)",
            "purposes": [
                        "uncertainty",
                        "material_science",
                        "multiphysics"
            ],
            "applications": [
                        "Deformation modeling",
                        "Fatigue analysis",
                        "Part integrity"
            ],
            "uq_methods": [
                        "Bayesian PINNs",
                        "Monte Carlo Sampling",
                        "Variational Inference"
            ]
},
        'nernst_planck_uq': {
            "name": "Nernst-Planck Equation (Uncertainty Quantification)",
            "description": "Quantify uncertainty in ion concentration and transport parameters from noisy electrochemical data",
            "icon": "fas fa-battery-three-quarters",
            "color": "#16a085",
            "formula": "\u2202c/\u2202t = \u2207\u00b7(D\u2207c + zF/(RT) Dc\u2207\u03c6)",
            "purposes": [
                        "uncertainty",
                        "battery_systems",
                        "multiphysics"
            ],
            "applications": [
                        "Battery modeling",
                        "Fuel cell analysis",
                        "Electrochemical transport"
            ],
            "uq_methods": [
                        "Bayesian PINNs",
                        "Monte Carlo Methods",
                        "Gaussian Processes"
            ]
},
        'poroelasticity_uq': {
            "name": "Poroelasticity Equations (Uncertainty Quantification)",
            "description": "Quantify uncertainty in stress and permeability from noisy biomechanical data",
            "icon": "fas fa-filter",
            "color": "#d35400",
            "formula": "\u2207\u00b7\u03c3 = -\u2207p_f, \u2202p_f/\u2202t + \u2207\u00b7(k\u2207p_f) = S",
            "purposes": [
                        "uncertainty",
                        "biomechanics",
                        "geophysics"
            ],
            "applications": [
                        "Tissue mechanics",
                        "Bone mechanics",
                        "Groundwater flow"
            ],
            "uq_methods": [
                        "Bayesian PINNs",
                        "Variational Inference",
                        "Ensemble Methods"
            ]
},
        'magnetohydrodynamics_uq': {
            "name": "Magnetohydrodynamics (Uncertainty Quantification)",
            "description": "Quantify uncertainty in plasma fields and transport coefficients from noisy diagnostic data",
            "icon": "fas fa-magnet",
            "color": "#8e44ad",
            "formula": "\u03c1(\u2202v/\u2202t + v\u00b7\u2207v) = -\u2207p + J\u00d7B + \u03bc\u2207\u00b2v, \u2202B/\u2202t = \u2207\u00d7(v\u00d7B - \u03b7\u2207\u00d7B)",
            "purposes": [
                        "uncertainty",
                        "fusion_energy",
                        "multiphysics"
            ],
            "applications": [
                        "Plasma dynamics",
                        "Fusion diagnostics",
                        "Space physics"
            ],
            "uq_methods": [
                        "Bayesian PINNs",
                        "Monte Carlo Sampling",
                        "Gaussian Processes"
            ]
},
        'helmholtz_discovery': {
            "name": "Helmholtz Equation (Scientific Discovery)",
            "description": "Discover spatially varying wave number k(x) or unknown source terms from field measurements",
            "icon": "fas fa-wave-square",
            "color": "#9b59b6",
            "formula": "\u2207\u00b2u + k\u00b2u = 0",
            "purposes": [
                        "scientific_discovery",
                        "acoustics",
                        "electromagnetics"
            ],
            "applications": [
                        "Acoustic scattering",
                        "Electromagnetic fields",
                        "Quantum mechanics"
            ]
},
        'navier_stokes_discovery': {
            "name": "Navier-Stokes Equations (Scientific Discovery)",
            "description": "Discover unknown forcing terms, viscosity, or constitutive relations from velocity/pressure data",
            "icon": "fas fa-water",
            "color": "#3498db",
            "formula": "\u03c1(\u2202v/\u2202t + v\u00b7\u2207v) = -\u2207p + \u03bc\u2207\u00b2v + f, \u2207\u00b7v = 0",
            "purposes": [
                        "scientific_discovery",
                        "fluid_dynamics",
                        "multiphysics"
            ],
            "applications": [
                        "Aerodynamics",
                        "Oceanography",
                        "Blood flow modeling"
            ]
},
        'schrodinger_discovery': {
            "name": "Schr\u00f6dinger Equation (Scientific Discovery)",
            "description": "Discover Hamiltonian parameters or potential terms from wave function data",
            "icon": "fas fa-atom",
            "color": "#1abc9c",
            "formula": "i\u210f\u2202\u03c8/\u2202t = \u0124\u03c8",
            "purposes": [
                        "scientific_discovery",
                        "quantum_mechanics",
                        "chemistry"
            ],
            "applications": [
                        "Quantum chemistry",
                        "Material properties",
                        "Quantum computing"
            ]
},
        'maxwell_discovery': {
            "name": "Maxwell Equations (Scientific Discovery)",
            "description": "Discover material properties or source terms from field measurements",
            "icon": "fas fa-magnet",
            "color": "#8e44ad",
            "formula": "\u2207\u00b7E = \u03c1/\u03b5\u2080, \u2207\u00d7E = -\u2202B/\u2202t, \u2207\u00b7B = 0, \u2207\u00d7B = \u03bc\u2080J + \u03bc\u2080\u03b5\u2080\u2202E/\u2202t",
            "purposes": [
                        "scientific_discovery",
                        "electromagnetics",
                        "optics"
            ],
            "applications": [
                        "Antenna design",
                        "Optical systems",
                        "Electromagnetic compatibility"
            ]
},
        'phase_field_control_discovery': {
            "name": "Phase-Field Equation with Control (Scientific Discovery)",
            "description": "Discover mobility, free energy, or optimal control from microstructure data",
            "icon": "fas fa-cube",
            "color": "#f39c12",
            "formula": "\u2202\u03c6/\u2202t = -M \u03b4F/\u03b4\u03c6 + u",
            "purposes": [
                        "scientific_discovery",
                        "material_science",
                        "control_optimization"
            ],
            "applications": [
                        "Grain growth control",
                        "Phase transformation",
                        "Thin film deposition"
            ]
},
        'hjb_discovery': {
            "name": "Hamilton-Jacobi-Bellman Equation (Scientific Discovery)",
            "description": "Discover dynamics or cost function from control data",
            "icon": "fas fa-route",
            "color": "#e74c3c",
            "formula": "\u2202V/\u2202t + min_u[L(x,u,t) + \u2207V\u00b7f(x,u,t)] = 0",
            "purposes": [
                        "scientific_discovery",
                        "control_optimization",
                        "robotics"
            ],
            "applications": [
                        "Robotics path planning",
                        "Power grid optimization",
                        "Portfolio optimization"
            ]
},
        'phase_field_discovery': {
            "name": "Phase-Field Equation (Scientific Discovery)",
            "description": "Discover mobility or free energy from microstructure data",
            "icon": "fas fa-layer-group",
            "color": "#34495e",
            "formula": "\u2202\u03c6/\u2202t = -M \u03b4F/\u03b4\u03c6",
            "purposes": [
                        "scientific_discovery",
                        "material_science",
                        "multiphysics"
            ],
            "applications": [
                        "Grain growth",
                        "Phase transformations",
                        "Solidification"
            ]
},
        'reaction_diffusion_discovery': {
            "name": "Reaction-Diffusion Equations (Scientific Discovery)",
            "description": "Discover reaction terms or diffusivities from concentration data",
            "icon": "fas fa-flask",
            "color": "#e67e22",
            "formula": "\u2202u/\u2202t = D_u\u2207\u00b2u + f(u,v), \u2202v/\u2202t = D_v\u2207\u00b2v + g(u,v)",
            "purposes": [
                        "scientific_discovery",
                        "chemistry",
                        "biology"
            ],
            "applications": [
                        "Chemical kinetics",
                        "Pattern formation",
                        "Biological systems"
            ]
},
        'reaction_diffusion_sparse_discovery': {
            "name": "Reaction-Diffusion Equations (Sparse Data Discovery)",
            "description": "Discover reaction terms or diffusivities from sparse/noisy concentration data",
            "icon": "fas fa-flask",
            "color": "#d35400",
            "formula": "\u2202u/\u2202t = D_u\u2207\u00b2u + f(u,v), \u2202v/\u2202t = D_v\u2207\u00b2v + g(u,v)",
            "purposes": [
                        "scientific_discovery",
                        "sparse_data",
                        "chemistry"
            ],
            "applications": [
                        "Chemical kinetics",
                        "Pattern formation",
                        "Biological systems"
            ]
},
        'schrodinger_uq_discovery': {
            "name": "Schr\u00f6dinger Equation (Uncertainty Quantification Discovery)",
            "description": "Discover Hamiltonian parameters with uncertainty estimates from noisy wave function data",
            "icon": "fas fa-atom",
            "color": "#16a085",
            "formula": "i\u210f\u2202\u03c8/\u2202t = \u0124\u03c8",
            "purposes": [
                        "scientific_discovery",
                        "uncertainty",
                        "quantum_mechanics"
            ],
            "applications": [
                        "Quantum chemistry",
                        "Material properties",
                        "Quantum computing"
            ]
},
        'heat_transfer_phase_change_discovery': {
            "name": "Heat Transfer with Phase Change (Scientific Discovery)",
            "description": "Discover thermal conductivity, heat source, or phase change dynamics from temperature data",
            "icon": "fas fa-thermometer-half",
            "color": "#e74c3c",
            "formula": "\u03c1c_p\u2202T/\u2202t = \u2207\u00b7(k\u2207T) + Q - L\u2202f_s/\u2202t",
            "purposes": [
                        "scientific_discovery",
                        "additive_manufacturing",
                        "multiphysics"
            ],
            "applications": [
                        "Melt pool dynamics",
                        "Thermal history",
                        "Solidification"
            ]
},
        'stefan_condition_discovery': {
            "name": "Stefan Condition (Scientific Discovery)",
            "description": "Discover thermal conductivities, latent heat, or interface dynamics from boundary data",
            "icon": "fas fa-arrows-alt-h",
            "color": "#9b59b6",
            "formula": "k_s\u2207T_s\u00b7n - k_l\u2207T_l\u00b7n = \u03c1Lv_n",
            "purposes": [
                        "scientific_discovery",
                        "additive_manufacturing",
                        "multiphysics"
            ],
            "applications": [
                        "Melt pool boundary tracking",
                        "Solidification rate"
            ]
},
        'navier_stokes_free_surface_discovery': {
            "name": "Navier-Stokes with Free Surface (Scientific Discovery)",
            "description": "Discover viscosity, surface tension, or Marangoni effects from velocity data",
            "icon": "fas fa-water",
            "color": "#3498db",
            "formula": "\u03c1(\u2202v/\u2202t + v\u00b7\u2207v) = -\u2207p + \u03bc\u2207\u00b2v + f_surface, \u2207\u00b7v = 0",
            "purposes": [
                        "scientific_discovery",
                        "additive_manufacturing",
                        "multiphysics"
            ],
            "applications": [
                        "Melt pool dynamics",
                        "Keyhole formation"
            ]
},
        'thermal_stress_discovery': {
            "name": "Thermal Stress Equation (Scientific Discovery)",
            "description": "Discover elastic modulus or thermal strain from stress or displacement data",
            "icon": "fas fa-compress-arrows-alt",
            "color": "#f39c12",
            "formula": "\u2207\u00b7\u03c3 = 0, \u03c3 = C:(\u03b5 - \u03b5_th)",
            "purposes": [
                        "scientific_discovery",
                        "additive_manufacturing",
                        "multiphysics"
            ],
            "applications": [
                        "Residual stress",
                        "Warping"
            ]
},
        'cahn_hilliard_discovery': {
            "name": "Cahn-Hilliard Equation (Scientific Discovery)",
            "description": "Discover mobility or free energy from concentration data",
            "icon": "fas fa-layer-group",
            "color": "#34495e",
            "formula": "\u2202c/\u2202t = \u2207\u00b7(M\u2207\u03bc), \u03bc = \u03b4F/\u03b4c",
            "purposes": [
                        "scientific_discovery",
                        "material_science",
                        "multiphysics"
            ],
            "applications": [
                        "Spinodal decomposition",
                        "Thin film growth"
            ]
},
        'fick_second_law_discovery': {
            "name": "Fick's Second Law (Scientific Discovery)",
            "description": "Discover diffusivity or diffusion mechanisms from concentration data",
            "icon": "fas fa-exchange-alt",
            "color": "#27ae60",
            "formula": "\u2202c/\u2202t = \u2207\u00b7(D\u2207c)",
            "purposes": [
                        "scientific_discovery",
                        "material_science",
                        "chemistry"
            ],
            "applications": [
                        "Dopant diffusion",
                        "Hydrogen diffusion"
            ]
},
        'crystal_plasticity_discovery': {
            "name": "Crystal Plasticity Equations (Scientific Discovery)",
            "description": "Discover slip parameters or constitutive relations from deformation data",
            "icon": "fas fa-cube",
            "color": "#8e44ad",
            "formula": "\u03b5\u0307^p = \u03a3_\u03b1 \u03b3\u0307^\u03b1 m^\u03b1, \u03b3\u0307^\u03b1 = f(\u03c4^\u03b1, s^\u03b1)",
            "purposes": [
                        "scientific_discovery",
                        "material_science",
                        "multiphysics"
            ],
            "applications": [
                        "Deformation modeling",
                        "Fatigue analysis"
            ]
},
        'nernst_planck_discovery': {
            "name": "Nernst-Planck Equation (Scientific Discovery)",
            "description": "Discover diffusivity or electrochemical interactions from concentration or voltage data",
            "icon": "fas fa-battery-three-quarters",
            "color": "#16a085",
            "formula": "\u2202c/\u2202t = \u2207\u00b7(D\u2207c + zF/(RT)Dc\u2207\u03c6)",
            "purposes": [
                        "scientific_discovery",
                        "battery_systems",
                        "multiphysics"
            ],
            "applications": [
                        "Battery modeling",
                        "Fuel cell analysis"
            ]
},
        'poroelasticity_discovery': {
            "name": "Poroelasticity Equations (Scientific Discovery)",
            "description": "Discover permeability or biomechanical interactions from stress/pressure data",
            "icon": "fas fa-filter",
            "color": "#d35400",
            "formula": "\u2207\u00b7\u03c3 = -\u2207p_f, \u2202p_f/\u2202t + \u2207\u00b7(k\u2207p_f) = S",
            "purposes": [
                        "scientific_discovery",
                        "biomechanics",
                        "geophysics"
            ],
            "applications": [
                        "Tissue mechanics",
                        "Bone mechanics"
            ]
},
        'magnetohydrodynamics_discovery': {
            "name": "Magnetohydrodynamics (Scientific Discovery)",
            "description": "Discover plasma dynamics or resistivity from field measurements",
            "icon": "fas fa-magnet",
            "color": "#8e44ad",
            "formula": "\u03c1(\u2202v/\u2202t + v\u00b7\u2207v) = -\u2207p + J\u00d7B + \u03bc\u2207\u00b2v, \u2202B/\u2202t = \u2207\u00d7(v\u00d7B - \u03b7\u2207\u00d7B)",
            "purposes": [
                        "scientific_discovery",
                        "fusion_energy",
                        "multiphysics"
            ],
            "applications": [
                        "Plasma dynamics",
                        "Fusion diagnostics"
            ]
},
        'advection_diffusion_discovery': {
            "name": "Advection-Diffusion Equation (Scientific Discovery)",
            "description": "Discover transport coefficients or source terms from concentration data",
            "icon": "fas fa-wind",
            "color": "#16a085",
            "formula": "\u2202c/\u2202t + v\u00b7\u2207c = \u2207\u00b7(D\u2207c)",
            "purposes": [
                        "scientific_discovery",
                        "transport",
                        "multiphysics"
            ],
            "applications": [
                        "Atmospheric transport",
                        "Ocean currents",
                        "Pollutant dispersion"
            ]
},
        'elastic_wave_discovery': {
            "name": "Elastic Wave Equation (Scientific Discovery)",
            "description": "Discover elastic properties or wave propagation mechanisms from seismic data",
            "icon": "fas fa-wave-square",
            "color": "#9b59b6",
            "formula": "\u03c1\u2202\u00b2u/\u2202t\u00b2 = \u2207\u00b7(C:\u2207u)",
            "purposes": [
                        "scientific_discovery",
                        "geophysics",
                        "multiphysics"
            ],
            "applications": [
                        "Seismic waves",
                        "Ultrasound",
                        "Structural dynamics"
            ]
},
        'viscoelasticity_discovery': {
            "name": "Viscoelasticity Equations (Scientific Discovery)",
            "description": "Discover viscoelastic parameters or rheological models from deformation data",
            "icon": "fas fa-tint",
            "color": "#3498db",
            "formula": "\u03c3 + \u03c4\u2202\u03c3/\u2202t = E(\u03b5 + \u03c4_\u03b5\u2202\u03b5/\u2202t)",
            "purposes": [
                        "scientific_discovery",
                        "material_science",
                        "biomechanics"
            ],
            "applications": [
                        "Polymer mechanics",
                        "Biological tissues",
                        "Rheology"
            ]
},
        'thermoelasticity_discovery': {
            "name": "Thermoelasticity Equations (Scientific Discovery)",
            "description": "Discover coupled thermal-mechanical parameters from temperature and deformation data",
            "icon": "fas fa-thermometer-half",
            "color": "#e74c3c",
            "formula": "\u2207\u00b7\u03c3 = 0, \u03c1c_p\u2202T/\u2202t = \u2207\u00b7(k\u2207T) - T_0\u03b1\u2207\u00b7\u2202u/\u2202t",
            "purposes": [
                        "scientific_discovery",
                        "additive_manufacturing",
                        "multiphysics"
            ],
            "applications": [
                        "Thermal stress",
                        "Heat exchangers",
                        "Electronic packaging"
            ]
},
        'burgers_generalization': {
            "name": "Burgers Equation (Generalization)",
            "description": "Generalize to unseen viscosity values, domain geometries, or boundary conditions",
            "icon": "fas fa-wave-square",
            "color": "#9b59b6",
            "formula": "\u2202u/\u2202t + u\u2202u/\u2202x = \u03bd\u2202\u00b2u/\u2202x\u00b2",
            "purposes": [
                        "generalization",
                        "fluid_dynamics",
                        "multiphysics"
            ],
            "applications": [
                        "Shock wave propagation",
                        "Traffic flow modeling",
                        "Gas dynamics"
            ]
},
        'heat_generalization': {
            "name": "Heat Equation (Generalization)",
            "description": "Generalize to different thermal diffusivity, domain shapes, or boundary conditions",
            "icon": "fas fa-thermometer-half",
            "color": "#e74c3c",
            "formula": "\u2202u/\u2202t = \u03b1\u2202\u00b2u/\u2202x\u00b2",
            "purposes": [
                        "generalization",
                        "thermal_systems",
                        "multiphysics"
            ],
            "applications": [
                        "Thermal analysis",
                        "Material processing",
                        "Climate modeling"
            ]
},
        'wave_generalization': {
            "name": "Wave Equation (Generalization)",
            "description": "Generalize to unseen wave speed, complex geometries, or boundary conditions",
            "icon": "fas fa-wave-square",
            "color": "#3498db",
            "formula": "\u2202\u00b2u/\u2202t\u00b2 = c\u00b2\u2202\u00b2u/\u2202x\u00b2",
            "purposes": [
                        "generalization",
                        "wave_propagation",
                        "multiphysics"
            ],
            "applications": [
                        "Acoustic waves",
                        "Electromagnetic waves",
                        "Seismic waves"
            ]
},
        'shm_generalization': {
            "name": "Simple Harmonic Motion (Generalization)",
            "description": "Generalize to different natural frequencies or initial conditions",
            "icon": "fas fa-wave-square",
            "color": "#9b59b6",
            "formula": "d\u00b2x/dt\u00b2 + \u03c9\u00b2x = 0",
            "purposes": [
                        "generalization",
                        "mechanical_systems",
                        "control_optimization"
            ],
            "applications": [
                        "Mechanical vibrations",
                        "Electrical circuits",
                        "Molecular dynamics"
            ]
},
        'schrodinger_generalization': {
            "name": "Schr\u00f6dinger Equation (Generalization)",
            "description": "Generalize to different potentials or boundary conditions",
            "icon": "fas fa-atom",
            "color": "#1abc9c",
            "formula": "i\u210f\u2202\u03c8/\u2202t = \u0124\u03c8",
            "purposes": [
                        "generalization",
                        "quantum_mechanics",
                        "chemistry"
            ],
            "applications": [
                        "Quantum chemistry",
                        "Material properties",
                        "Quantum computing"
            ]
},
        'optimal_control_shm_generalization': {
            "name": "Optimal Control - Simple Harmonic Motion (Generalization)",
            "description": "Generalize to different frequencies, control inputs, or initial conditions",
            "icon": "fas fa-sliders-h",
            "color": "#f39c12",
            "formula": "d\u00b2x/dt\u00b2 + \u03c9\u00b2x = u(t)",
            "purposes": [
                        "generalization",
                        "control_optimization",
                        "mechanical_systems"
            ],
            "applications": [
                        "Vibration suppression",
                        "Suspension systems",
                        "LC oscillators"
            ]
},
        'wave_control_generalization': {
            "name": "Wave Control Systems (Generalization)",
            "description": "Generalize to different wave speeds, geometries, or control forces",
            "icon": "fas fa-wave-square",
            "color": "#3498db",
            "formula": "\u2202\u00b2u/\u2202t\u00b2 = c\u00b2\u2207\u00b2u + f",
            "purposes": [
                        "generalization",
                        "control_optimization",
                        "wave_propagation"
            ],
            "applications": [
                        "Structural engineering",
                        "Noise cancellation",
                        "Laser stabilization"
            ]
},
        'hjb_generalization': {
            "name": "Hamilton-Jacobi-Bellman Equation (Generalization)",
            "description": "Generalize to different dynamics, cost functions, or boundary conditions",
            "icon": "fas fa-route",
            "color": "#e74c3c",
            "formula": "\u2202V/\u2202t + min_u[L(x,u,t) + \u2207V\u00b7f(x,u,t)] = 0",
            "purposes": [
                        "generalization",
                        "control_optimization",
                        "robotics"
            ],
            "applications": [
                        "Robotics path planning",
                        "Power grid optimization",
                        "Portfolio optimization"
            ]
},
        'multi_objective_control_generalization': {
            "name": "Multi-Objective Control (Generalization)",
            "description": "Generalize to different weights, objectives, or system dynamics",
            "icon": "fas fa-sliders-h",
            "color": "#f39c12",
            "formula": "J = \u03a3 w_i J_i",
            "purposes": [
                        "generalization",
                        "control_optimization",
                        "multiphysics"
            ],
            "applications": [
                        "Autonomous systems",
                        "Smart cities",
                        "Healthcare"
            ]
},
        'heat_transfer_phase_change_generalization': {
            "name": "Heat Transfer with Phase Change (Generalization)",
            "description": "Generalize to different thermal conductivities, heat sources, or geometries",
            "icon": "fas fa-thermometer-half",
            "color": "#e74c3c",
            "formula": "\u03c1c_p\u2202T/\u2202t = \u2207\u00b7(k\u2207T) + Q - L\u2202f_s/\u2202t",
            "purposes": [
                        "generalization",
                        "additive_manufacturing",
                        "multiphysics"
            ],
            "applications": [
                        "Melt pool dynamics",
                        "Thermal history",
                        "Solidification"
            ]
},
        'stefan_condition_generalization': {
            "name": "Stefan Condition (Generalization)",
            "description": "Adapt to different thermal conductivities or interface conditions",
            "icon": "fas fa-arrows-alt-h",
            "color": "#9b59b6",
            "formula": "k_s\u2207T_s\u00b7n - k_l\u2207T_l\u00b7n = \u03c1Lv_n",
            "purposes": [
                        "generalization",
                        "additive_manufacturing",
                        "multiphysics"
            ],
            "applications": [
                        "Melt pool boundary tracking",
                        "Solidification rate"
            ]
},
        'navier_stokes_free_surface_generalization': {
            "name": "Navier-Stokes with Free Surface (Generalization)",
            "description": "Generalize to different viscosities, densities, or geometries",
            "icon": "fas fa-water",
            "color": "#3498db",
            "formula": "\u03c1(\u2202v/\u2202t + v\u00b7\u2207v) = -\u2207p + \u03bc\u2207\u00b2v + f_surface, \u2207\u00b7v = 0",
            "purposes": [
                        "generalization",
                        "additive_manufacturing",
                        "multiphysics"
            ],
            "applications": [
                        "Melt pool dynamics",
                        "Keyhole formation"
            ]
},
        'thermal_stress_generalization': {
            "name": "Thermal Stress Equation (Generalization)",
            "description": "Generalize to different elastic moduli, thermal strains, or boundary conditions",
            "icon": "fas fa-compress-arrows-alt",
            "color": "#f39c12",
            "formula": "\u2207\u00b7\u03c3 = 0, \u03c3 = C:(\u03b5 - \u03b5_th)",
            "purposes": [
                        "generalization",
                        "additive_manufacturing",
                        "multiphysics"
            ],
            "applications": [
                        "Residual stress",
                        "Warping analysis"
            ]
},
        'phase_field_generalization': {
            "name": "Phase-Field Equation (Generalization)",
            "description": "Generalize to different mobilities, free energies, or domain geometries",
            "icon": "fas fa-layer-group",
            "color": "#34495e",
            "formula": "\u2202\u03c6/\u2202t = -M \u03b4F/\u03b4\u03c6",
            "purposes": [
                        "generalization",
                        "material_science",
                        "multiphysics"
            ],
            "applications": [
                        "Grain growth",
                        "Phase transformation"
            ]
},
        'cahn_hilliard_generalization': {
            "name": "Cahn-Hilliard Equation (Generalization)",
            "description": "Generalize to different mobilities, free energies, or boundary conditions",
            "icon": "fas fa-layer-group",
            "color": "#34495e",
            "formula": "\u2202c/\u2202t = \u2207\u00b7(M\u2207\u03bc), \u03bc = \u03b4F/\u03b4c",
            "purposes": [
                        "generalization",
                        "material_science",
                        "multiphysics"
            ],
            "applications": [
                        "Spinodal decomposition",
                        "Thin film growth"
            ]
},
        'fick_second_law_generalization': {
            "name": "Fick's Second Law (Generalization)",
            "description": "Generalize to different diffusivities or domain shapes",
            "icon": "fas fa-exchange-alt",
            "color": "#27ae60",
            "formula": "\u2202c/\u2202t = \u2207\u00b7(D\u2207c)",
            "purposes": [
                        "generalization",
                        "material_science",
                        "chemistry"
            ],
            "applications": [
                        "Dopant diffusion",
                        "Hydrogen diffusion"
            ]
},
        'crystal_plasticity_generalization': {
            "name": "Crystal Plasticity Equations (Generalization)",
            "description": "Generalize to different slip parameters or loading conditions",
            "icon": "fas fa-cube",
            "color": "#8e44ad",
            "formula": "\u03b5\u0307^p = \u03a3_\u03b1 \u03b3\u0307^\u03b1 m^\u03b1, \u03b3\u0307^\u03b1 = f(\u03c4^\u03b1, s^\u03b1)",
            "purposes": [
                        "generalization",
                        "material_science",
                        "multiphysics"
            ],
            "applications": [
                        "Deformation modeling",
                        "Fatigue analysis"
            ]
},
        'nernst_planck_generalization': {
            "name": "Nernst-Planck Equation (Generalization)",
            "description": "Generalize to different diffusivities, potentials, or electrode geometries",
            "icon": "fas fa-battery-three-quarters",
            "color": "#16a085",
            "formula": "\u2202c/\u2202t = \u2207\u00b7(D\u2207c + zF/(RT)Dc\u2207\u03c6)",
            "purposes": [
                        "generalization",
                        "battery_systems",
                        "multiphysics"
            ],
            "applications": [
                        "Battery modeling",
                        "Fuel cell analysis"
            ]
},
        'poroelasticity_generalization': {
            "name": "Poroelasticity Equations (Generalization)",
            "description": "Generalize to different permeabilities, geometries, or loading conditions",
            "icon": "fas fa-filter",
            "color": "#d35400",
            "formula": "\u2207\u00b7\u03c3 = -\u2207p_f, \u2202p_f/\u2202t + \u2207\u00b7(k\u2207p_f) = S",
            "purposes": [
                        "generalization",
                        "biomechanics",
                        "geophysics"
            ],
            "applications": [
                        "Tissue mechanics",
                        "Bone mechanics"
            ]
},
        'magnetohydrodynamics_generalization': {
            "name": "Magnetohydrodynamics (Generalization)",
            "description": "Generalize to different resistivities, densities, or reactor geometries",
            "icon": "fas fa-magnet",
            "color": "#8e44ad",
            "formula": "\u03c1(\u2202v/\u2202t + v\u00b7\u2207v) = -\u2207p + J\u00d7B + \u03bc\u2207\u00b2v, \u2202B/\u2202t = \u2207\u00d7(v\u00d7B - \u03b7\u2207\u00d7B)",
            "purposes": [
                        "generalization",
                        "fusion_energy",
                        "multiphysics"
            ],
            "applications": [
                        "Plasma dynamics",
                        "Fusion diagnostics"
            ]
},
        'advection_diffusion_generalization': {
            "name": "Advection-Diffusion Equation (Generalization)",
            "description": "Generalize to different velocities, diffusivities, or domain geometries",
            "icon": "fas fa-wind",
            "color": "#16a085",
            "formula": "\u2202c/\u2202t + v\u00b7\u2207c = \u2207\u00b7(D\u2207c)",
            "purposes": [
                        "generalization",
                        "transport",
                        "multiphysics"
            ],
            "applications": [
                        "Atmospheric transport",
                        "Ocean currents",
                        "Pollutant dispersion"
            ]
},
        'elastic_wave_generalization': {
            "name": "Elastic Wave Equation (Generalization)",
            "description": "Generalize to different elastic properties or complex geometries",
            "icon": "fas fa-wave-square",
            "color": "#9b59b6",
            "formula": "\u03c1\u2202\u00b2u/\u2202t\u00b2 = \u2207\u00b7(C:\u2207u)",
            "purposes": [
                        "generalization",
                        "geophysics",
                        "multiphysics"
            ],
            "applications": [
                        "Seismic waves",
                        "Ultrasound",
                        "Structural dynamics"
            ]
},
        'viscoelasticity_generalization': {
            "name": "Viscoelasticity Equations (Generalization)",
            "description": "Generalize to different viscoelastic parameters or loading conditions",
            "icon": "fas fa-tint",
            "color": "#3498db",
            "formula": "\u03c3 + \u03c4\u2202\u03c3/\u2202t = E(\u03b5 + \u03c4_\u03b5\u2202\u03b5/\u2202t)",
            "purposes": [
                        "generalization",
                        "material_science",
                        "biomechanics"
            ],
            "applications": [
                        "Polymer mechanics",
                        "Biological tissues",
                        "Rheology"
            ]
},
        'thermoelasticity_generalization': {
            "name": "Thermoelasticity Equations (Generalization)",
            "description": "Generalize to different thermal-mechanical properties or boundary conditions",
            "icon": "fas fa-thermometer-half",
            "color": "#e74c3c",
            "formula": "\u2207\u00b7\u03c3 = 0, \u03c1c_p\u2202T/\u2202t = \u2207\u00b7(k\u2207T) - T_0\u03b1\u2207\u00b7\u2202u/\u2202t",
            "purposes": [
                        "generalization",
                        "additive_manufacturing",
                        "multiphysics"
            ],
            "applications": [
                        "Thermal stress",
                        "Heat exchangers",
                        "Electronic packaging"
            ]
},
        'thermo_fluid_dynamics': {
            "name": "Thermo-Fluid Dynamics",
            "description": "Coupled heat transfer and fluid flow with buoyancy effects",
            "icon": "fas fa-thermometer-half",
            "color": "#e74c3c",
            "formula": "\u03c1(\u2202v/\u2202t + v\u00b7\u2207v) = -\u2207p + \u03bc\u2207\u00b2v + \u03c1\u03b2g(T-T\u2080), \u03c1c_p(\u2202T/\u2202t + v\u00b7\u2207T) = \u2207\u00b7(k\u2207T)",
            "purposes": [
                        "multiphysics",
                        "thermal_systems",
                        "fluid_dynamics"
            ],
            "applications": [
                        "Natural convection",
                        "Heat exchangers",
                        "Climate modeling"
            ]
},
        'magneto_thermo_elasticity': {
            "name": "Magneto-Thermo-Elasticity",
            "description": "Coupled magnetic, thermal, and elastic phenomena",
            "icon": "fas fa-magnet",
            "color": "#8e44ad",
            "formula": "\u2207\u00b7\u03c3 = J\u00d7B + \u03c1f, \u2207\u00d7E = -\u2202B/\u2202t, \u03c1c_p\u2202T/\u2202t = \u2207\u00b7(k\u2207T) + J\u00b7E",
            "purposes": [
                        "multiphysics",
                        "electromagnetic",
                        "thermal_systems"
            ],
            "applications": [
                        "Magnetic materials",
                        "Electromagnetic devices",
                        "Smart materials"
            ]
},
        'electro_thermo_mechanics': {
            "name": "Electro-Thermo-Mechanics",
            "description": "Coupled electrical, thermal, and mechanical phenomena",
            "icon": "fas fa-bolt",
            "color": "#f39c12",
            "formula": "\u2207\u00b7D = \u03c1_e, \u2207\u00d7E = 0, \u2207\u00b7\u03c3 = \u03c1E + \u03c1f, \u03c1c_p\u2202T/\u2202t = \u2207\u00b7(k\u2207T) + J\u00b7E",
            "purposes": [
                        "multiphysics",
                        "electrical_systems",
                        "mechanical_systems"
            ],
            "applications": [
                        "Piezoelectric materials",
                        "Electronic packaging",
                        "Smart structures"
            ]
},
        'poro_thermo_elasticity': {
            "name": "Poro-Thermo-Elasticity",
            "description": "Coupled fluid flow, heat transfer, and deformation in porous media",
            "icon": "fas fa-filter",
            "color": "#d35400",
            "formula": "\u2207\u00b7\u03c3 = -\u2207p_f, \u2202p_f/\u2202t + \u2207\u00b7(k\u2207p_f) = S, \u03c1c_p\u2202T/\u2202t = \u2207\u00b7(k\u2207T)",
            "purposes": [
                        "multiphysics",
                        "porous_media",
                        "biomechanics"
            ],
            "applications": [
                        "Geothermal systems",
                        "Biomedical tissues",
                        "Soil mechanics"
            ]
},
        'reactive_flow': {
            "name": "Reactive Flow",
            "description": "Coupled fluid dynamics and chemical reactions",
            "icon": "fas fa-flask",
            "color": "#27ae60",
            "formula": "\u2202c/\u2202t + v\u00b7\u2207c = \u2207\u00b7(D\u2207c) + R(c,T), \u03c1(\u2202v/\u2202t + v\u00b7\u2207v) = -\u2207p + \u03bc\u2207\u00b2v",
            "purposes": [
                        "multiphysics",
                        "chemical_engineering",
                        "combustion"
            ],
            "applications": [
                        "Combustion chambers",
                        "Chemical reactors",
                        "Catalytic converters"
            ]
},
        'phase_field_fluid': {
            "name": "Phase-Field Fluid Dynamics",
            "description": "Coupled phase-field evolution and fluid flow",
            "icon": "fas fa-water",
            "color": "#3498db",
            "formula": "\u2202\u03c6/\u2202t + v\u00b7\u2207\u03c6 = -M \u03b4F/\u03b4\u03c6, \u03c1(\u2202v/\u2202t + v\u00b7\u2207v) = -\u2207p + \u03bc\u2207\u00b2v + f_\u03c6",
            "purposes": [
                        "multiphysics",
                        "phase_transitions",
                        "fluid_dynamics"
            ],
            "applications": [
                        "Multiphase flows",
                        "Crystal growth",
                        "Emulsion dynamics"
            ]
},
        'electro_kinetics': {
            "name": "Electrokinetics",
            "description": "Coupled electrical and fluid phenomena in micro/nano systems",
            "icon": "fas fa-microchip",
            "color": "#16a085",
            "formula": "\u2207\u00b2\u03c6 = -\u03c1_e/\u03b5, \u03c1(\u2202v/\u2202t + v\u00b7\u2207v) = -\u2207p + \u03bc\u2207\u00b2v + \u03c1_eE",
            "purposes": [
                        "multiphysics",
                        "microfluidics",
                        "electrical_systems"
            ],
            "applications": [
                        "Lab-on-chip devices",
                        "Electroosmotic pumps",
                        "DNA separation"
            ]
},
        'magneto_hydrodynamics': {
            "name": "Magnetohydrodynamics (MHD)",
            "description": "Coupled magnetic fields and fluid flow",
            "icon": "fas fa-magnet",
            "color": "#8e44ad",
            "formula": "\u03c1(\u2202v/\u2202t + v\u00b7\u2207v) = -\u2207p + J\u00d7B + \u03bc\u2207\u00b2v, \u2202B/\u2202t = \u2207\u00d7(v\u00d7B - \u03b7\u2207\u00d7B)",
            "purposes": [
                        "multiphysics",
                        "plasma_physics",
                        "fusion_energy"
            ],
            "applications": [
                        "Fusion reactors",
                        "Plasma confinement",
                        "Astrophysical flows"
            ]
},
        'thermo_chemical_mechanics': {
            "name": "Thermo-Chemical-Mechanics",
            "description": "Coupled thermal, chemical, and mechanical phenomena",
            "icon": "fas fa-atom",
            "color": "#e67e22",
            "formula": "\u2202c/\u2202t = \u2207\u00b7(D\u2207c) + R(c,T), \u03c1c_p\u2202T/\u2202t = \u2207\u00b7(k\u2207T) + Q_R, \u2207\u00b7\u03c3 = \u03c1f",
            "purposes": [
                        "multiphysics",
                        "material_science",
                        "chemical_engineering"
            ],
            "applications": [
                        "Battery electrodes",
                        "Catalytic materials",
                        "Self-healing materials"
            ]
},
        'acoustic_elasticity': {
            "name": "Acoustic-Elasticity",
            "description": "Coupled acoustic waves and elastic deformation",
            "icon": "fas fa-wave-square",
            "color": "#9b59b6",
            "formula": "\u03c1\u2202\u00b2u/\u2202t\u00b2 = \u2207\u00b7(C:\u2207u), \u2202\u00b2p/\u2202t\u00b2 = c\u00b2\u2207\u00b2p + \u03c1\u2080\u2207\u00b7\u2202\u00b2u/\u2202t\u00b2",
            "purposes": [
                        "multiphysics",
                        "acoustics",
                        "structural_dynamics"
            ],
            "applications": [
                        "Ultrasound imaging",
                        "Structural health monitoring",
                        "Acoustic metamaterials"
            ]
},
        'electro_thermo_fluid': {
            "name": "Electro-Thermo-Fluid Dynamics",
            "description": "Coupled electrical, thermal, and fluid phenomena",
            "icon": "fas fa-bolt",
            "color": "#f39c12",
            "formula": "\u2207\u00b7D = \u03c1_e, \u03c1(\u2202v/\u2202t + v\u00b7\u2207v) = -\u2207p + \u03bc\u2207\u00b2v + \u03c1_eE, \u03c1c_p(\u2202T/\u2202t + v\u00b7\u2207T) = \u2207\u00b7(k\u2207T) + J\u00b7E",
            "purposes": [
                        "multiphysics",
                        "electrical_systems",
                        "thermal_systems"
            ],
            "applications": [
                        "Electrohydrodynamic pumps",
                        "Thermal management",
                        "Energy harvesting"
            ]
},
        'bio_fluid_mechanics': {
            "name": "Bio-Fluid-Mechanics",
            "description": "Coupled fluid flow and biological tissue mechanics",
            "icon": "fas fa-heartbeat",
            "color": "#e74c3c",
            "formula": "\u03c1(\u2202v/\u2202t + v\u00b7\u2207v) = -\u2207p + \u03bc\u2207\u00b2v, \u2207\u00b7\u03c3_tissue = -\u2207p_f + \u03c1f",
            "purposes": [
                        "multiphysics",
                        "biomechanics",
                        "fluid_dynamics"
            ],
            "applications": [
                        "Blood flow in arteries",
                        "Lung mechanics",
                        "Tissue engineering"
            ]
},
        'quantum_thermal': {
            "name": "Quantum-Thermal Systems",
            "description": "Coupled quantum mechanics and thermal transport",
            "icon": "fas fa-atom",
            "color": "#1abc9c",
            "formula": "i\u210f\u2202\u03c8/\u2202t = \u0124\u03c8, \u03c1c_p\u2202T/\u2202t = \u2207\u00b7(k\u2207T) + Q_quantum",
            "purposes": [
                        "multiphysics",
                        "quantum_mechanics",
                        "thermal_systems"
            ],
            "applications": [
                        "Quantum computing",
                        "Thermal management",
                        "Quantum sensors"
            ]
},
        'photo_thermal_mechanics': {
            "name": "Photo-Thermal-Mechanics",
            "description": "Coupled optical, thermal, and mechanical phenomena",
            "icon": "fas fa-lightbulb",
            "color": "#f1c40f",
            "formula": "\u2207\u00b2E + k\u00b2E = 0, \u03c1c_p\u2202T/\u2202t = \u2207\u00b7(k\u2207T) + \u03b1|E|\u00b2, \u2207\u00b7\u03c3 = \u03c1f",
            "purposes": [
                        "multiphysics",
                        "optics",
                        "thermal_systems"
            ],
            "applications": [
                        "Laser processing",
                        "Optical tweezers",
                        "Photothermal therapy"
            ]
},
        'electro_chemical_thermal': {
            "name": "Electro-Chemical-Thermal",
            "description": "Coupled electrochemical reactions and thermal transport",
            "icon": "fas fa-battery-full",
            "color": "#16a085",
            "formula": "\u2202c/\u2202t = \u2207\u00b7(D\u2207c + zF/(RT)Dc\u2207\u03c6), \u03c1c_p\u2202T/\u2202t = \u2207\u00b7(k\u2207T) + I\u00b7E",
            "purposes": [
                        "multiphysics",
                        "electrochemistry",
                        "thermal_systems"
            ],
            "applications": [
                        "Battery systems",
                        "Fuel cells",
                        "Electrochemical sensors"
            ]
},
        'magneto_elastic_thermal': {
            "name": "Magneto-Elastic-Thermal",
            "description": "Coupled magnetic, elastic, and thermal phenomena",
            "icon": "fas fa-magnet",
            "color": "#8e44ad",
            "formula": "\u2207\u00d7H = J, \u2207\u00b7\u03c3 = J\u00d7B + \u03c1f, \u03c1c_p\u2202T/\u2202t = \u2207\u00b7(k\u2207T) + J\u00b7E",
            "purposes": [
                        "multiphysics",
                        "magnetic_materials",
                        "thermal_systems"
            ],
            "applications": [
                        "Magnetic shape memory alloys",
                        "Magnetostrictive materials",
                        "Magnetic refrigeration"
            ]
},
        'fluid_structure_interaction': {
            "name": "Fluid-Structure Interaction",
            "description": "Coupled fluid flow and structural deformation",
            "icon": "fas fa-water",
            "color": "#3498db",
            "formula": "\u03c1(\u2202v/\u2202t + v\u00b7\u2207v) = -\u2207p + \u03bc\u2207\u00b2v, \u03c1_s\u2202\u00b2u/\u2202t\u00b2 = \u2207\u00b7\u03c3 + f_fluid",
            "purposes": [
                        "multiphysics",
                        "fluid_dynamics",
                        "structural_dynamics"
            ],
            "applications": [
                        "Aircraft wings",
                        "Wind turbines",
                        "Biomedical devices"
            ]
},
        'thermal_stress_flow': {
            "name": "Thermal-Stress-Flow",
            "description": "Coupled thermal stress and fluid flow",
            "icon": "fas fa-thermometer-half",
            "color": "#e74c3c",
            "formula": "\u2207\u00b7\u03c3 = \u03c1f, \u03c3 = C:(\u03b5 - \u03b5_th), \u03c1(\u2202v/\u2202t + v\u00b7\u2207v) = -\u2207p + \u03bc\u2207\u00b2v",
            "purposes": [
                        "multiphysics",
                        "thermal_systems",
                        "fluid_dynamics"
            ],
            "applications": [
                        "Thermal management",
                        "Heat exchangers",
                        "Nuclear reactors"
            ]
},
        'electro_optical_thermal': {
            "name": "Electro-Optical-Thermal",
            "description": "Coupled electrical, optical, and thermal phenomena",
            "icon": "fas fa-lightbulb",
            "color": "#f1c40f",
            "formula": "\u2207\u00b7D = \u03c1_e, \u2207\u00b2E + k\u00b2E = 0, \u03c1c_p\u2202T/\u2202t = \u2207\u00b7(k\u2207T) + J\u00b7E + \u03b1|E|\u00b2",
            "purposes": [
                        "multiphysics",
                        "electrical_systems",
                        "optics"
            ],
            "applications": [
                        "Optoelectronic devices",
                        "Laser diodes",
                        "Photovoltaic cells"
            ]
},
        'quantum_mechanical_thermal': {
            "name": "Quantum-Mechanical-Thermal",
            "description": "Coupled quantum mechanics and mechanical-thermal phenomena",
            "icon": "fas fa-atom",
            "color": "#1abc9c",
            "formula": "i\u210f\u2202\u03c8/\u2202t = \u0124\u03c8, \u03c1\u2202\u00b2u/\u2202t\u00b2 = \u2207\u00b7\u03c3, \u03c1c_p\u2202T/\u2202t = \u2207\u00b7(k\u2207T)",
            "purposes": [
                        "multiphysics",
                        "quantum_mechanics",
                        "mechanical_systems"
            ],
            "applications": [
                        "Quantum sensors",
                        "Nanoelectromechanical systems",
                        "Quantum materials"
            ]
},
        'bio_electro_mechanical': {
            "name": "Bio-Electro-Mechanical",
            "description": "Coupled biological, electrical, and mechanical phenomena",
            "icon": "fas fa-heartbeat",
            "color": "#e74c3c",
            "formula": "\u2207\u00b7D = \u03c1_e, \u2207\u00b7\u03c3 = \u03c1E + \u03c1f, \u2202c/\u2202t = \u2207\u00b7(D\u2207c) + R_bio",
            "purposes": [
                        "multiphysics",
                        "biomechanics",
                        "electrical_systems"
            ],
            "applications": [
                        "Neural interfaces",
                        "Cardiac electrophysiology",
                        "Bioelectronic devices"
            ]
},
        'magneto_optical_thermal': {
            "name": "Magneto-Optical-Thermal",
            "description": "Coupled magnetic, optical, and thermal phenomena",
            "icon": "fas fa-magnet",
            "color": "#8e44ad",
            "formula": "\u2207\u00d7H = J, \u2207\u00b2E + k\u00b2E = 0, \u03c1c_p\u2202T/\u2202t = \u2207\u00b7(k\u2207T) + J\u00b7E",
            "purposes": [
                        "multiphysics",
                        "magnetic_materials",
                        "optics"
            ],
            "applications": [
                        "Magneto-optical devices",
                        "Magnetic sensors",
                        "Optical storage"
            ]
},
        'quantum_optical_mechanical': {
            "name": "Quantum-Optical-Mechanical",
            "description": "Coupled quantum, optical, and mechanical phenomena",
            "icon": "fas fa-atom",
            "color": "#1abc9c",
            "formula": "i\u210f\u2202\u03c8/\u2202t = \u0124\u03c8, \u2207\u00b2E + k\u00b2E = 0, \u03c1\u2202\u00b2u/\u2202t\u00b2 = \u2207\u00b7\u03c3",
            "purposes": [
                        "multiphysics",
                        "quantum_mechanics",
                        "optics"
            ],
            "applications": [
                        "Optomechanical systems",
                        "Quantum optics",
                        "Photon-phonon coupling"
            ]
},
        'adaptive_sampling_burgers': {
            "name": "Burgers Equation (Adaptive Sampling)",
            "description": "Burgers equation with adaptive sampling for efficient training",
            "icon": "fas fa-wave-square",
            "color": "#9b59b6",
            "formula": "\u2202u/\u2202t + u\u2202u/\u2202x = \u03bd\u2202\u00b2u/\u2202x\u00b2",
            "purposes": [
                        "efficiency",
                        "fluid_dynamics",
                        "adaptive_methods"
            ],
            "applications": [
                        "Shock wave simulation",
                        "Traffic flow modeling",
                        "Gas dynamics"
            ]
},
        'multiscale_heat': {
            "name": "Heat Equation (Multiscale)",
            "description": "Heat equation with multiscale resolution for computational efficiency",
            "icon": "fas fa-thermometer-half",
            "color": "#e74c3c",
            "formula": "\u2202u/\u2202t = \u03b1\u2202\u00b2u/\u2202x\u00b2",
            "purposes": [
                        "efficiency",
                        "thermal_systems",
                        "multiscale_methods"
            ],
            "applications": [
                        "Thermal analysis",
                        "Material processing",
                        "Climate modeling"
            ]
},
        'adaptive_wave': {
            "name": "Wave Equation (Adaptive Resolution)",
            "description": "Wave equation with adaptive spatial and temporal resolution",
            "icon": "fas fa-wave-square",
            "color": "#3498db",
            "formula": "\u2202\u00b2u/\u2202t\u00b2 = c\u00b2\u2202\u00b2u/\u2202x\u00b2",
            "purposes": [
                        "efficiency",
                        "wave_propagation",
                        "adaptive_methods"
            ],
            "applications": [
                        "Acoustic waves",
                        "Electromagnetic waves",
                        "Seismic waves"
            ]
},
        'fast_fourier_poisson': {
            "name": "Poisson Equation (Fast Fourier Transform)",
            "description": "Poisson equation solved using FFT for computational efficiency",
            "icon": "fas fa-wave-square",
            "color": "#1abc9c",
            "formula": "\u2207\u00b2u = f",
            "purposes": [
                        "efficiency",
                        "elliptic_pdes",
                        "spectral_methods"
            ],
            "applications": [
                        "Electrostatics",
                        "Fluid pressure",
                        "Heat conduction"
            ]
},
        'sparse_laplace': {
            "name": "Laplace Equation (Sparse Grid)",
            "description": "Laplace equation using sparse grid methods for high-dimensional efficiency",
            "icon": "fas fa-th",
            "color": "#34495e",
            "formula": "\u2207\u00b2u = 0",
            "purposes": [
                        "efficiency",
                        "elliptic_pdes",
                        "sparse_methods"
            ],
            "applications": [
                        "Potential theory",
                        "Electrostatics",
                        "Heat conduction"
            ]
},
        'adaptive_navier_stokes': {
            "name": "Navier-Stokes (Adaptive Mesh)",
            "description": "Navier-Stokes equations with adaptive mesh refinement",
            "icon": "fas fa-water",
            "color": "#3498db",
            "formula": "\u03c1(\u2202v/\u2202t + v\u00b7\u2207v) = -\u2207p + \u03bc\u2207\u00b2v + f, \u2207\u00b7v = 0",
            "purposes": [
                        "efficiency",
                        "fluid_dynamics",
                        "adaptive_methods"
            ],
            "applications": [
                        "Aerodynamics",
                        "Hydrodynamics",
                        "Meteorology"
            ]
},
        'fast_reaction_diffusion': {
            "name": "Reaction-Diffusion (Fast Integration)",
            "description": "Reaction-diffusion equations with fast integration schemes",
            "icon": "fas fa-atom",
            "color": "#e67e22",
            "formula": "\u2202u/\u2202t = D\u2207\u00b2u + f(u)",
            "purposes": [
                        "efficiency",
                        "reaction_diffusion",
                        "fast_methods"
            ],
            "applications": [
                        "Chemical kinetics",
                        "Pattern formation",
                        "Biological systems"
            ]
},
        'adaptive_schrodinger': {
            "name": "Schr\u00f6dinger Equation (Adaptive Time)",
            "description": "Schr\u00f6dinger equation with adaptive time stepping",
            "icon": "fas fa-atom",
            "color": "#1abc9c",
            "formula": "i\u210f\u2202\u03c8/\u2202t = \u0124\u03c8",
            "purposes": [
                        "efficiency",
                        "quantum_mechanics",
                        "adaptive_methods"
            ],
            "applications": [
                        "Quantum chemistry",
                        "Material properties",
                        "Quantum computing"
            ]
},
        'fast_maxwell': {
            "name": "Maxwell Equations (Fast Solver)",
            "description": "Maxwell equations with fast electromagnetic solvers",
            "icon": "fas fa-bolt",
            "color": "#f39c12",
            "formula": "\u2207\u00d7E = -\u2202B/\u2202t, \u2207\u00d7B = \u03bc\u2080J + \u03bc\u2080\u03b5\u2080\u2202E/\u2202t",
            "purposes": [
                        "efficiency",
                        "electromagnetic",
                        "fast_methods"
            ],
            "applications": [
                        "Electromagnetic waves",
                        "Antenna design",
                        "Optics"
            ]
},
        'adaptive_elasticity': {
            "name": "Elasticity (Adaptive Elements)",
            "description": "Elasticity equations with adaptive finite elements",
            "icon": "fas fa-compress-arrows-alt",
            "color": "#8e44ad",
            "formula": "\u2207\u00b7\u03c3 = f, \u03c3 = C:\u03b5",
            "purposes": [
                        "efficiency",
                        "mechanical_systems",
                        "adaptive_methods"
            ],
            "applications": [
                        "Structural analysis",
                        "Material deformation",
                        "Geomechanics"
            ]
},
        'fast_porous_flow': {
            "name": "Porous Flow (Fast Solver)",
            "description": "Darcy flow with fast pressure solvers",
            "icon": "fas fa-filter",
            "color": "#d35400",
            "formula": "v = -k/\u03bc \u2207p, \u2207\u00b7v = 0",
            "purposes": [
                        "efficiency",
                        "porous_media",
                        "fast_methods"
            ],
            "applications": [
                        "Groundwater flow",
                        "Oil reservoir simulation",
                        "Filtration"
            ]
},
        'adaptive_phase_field': {
            "name": "Phase Field (Adaptive Resolution)",
            "description": "Phase field equations with adaptive interface resolution",
            "icon": "fas fa-layer-group",
            "color": "#34495e",
            "formula": "\u2202\u03c6/\u2202t = -M \u03b4F/\u03b4\u03c6",
            "purposes": [
                        "efficiency",
                        "phase_field",
                        "adaptive_methods"
            ],
            "applications": [
                        "Phase transitions",
                        "Grain growth",
                        "Crystal growth"
            ]
},
        'fast_kinetic': {
            "name": "Kinetic Equations (Fast Integration)",
            "description": "Kinetic equations with fast collision operators",
            "icon": "fas fa-atom",
            "color": "#e67e22",
            "formula": "\u2202f/\u2202t + v\u00b7\u2207f = Q(f)",
            "purposes": [
                        "efficiency",
                        "kinetic_theory",
                        "fast_methods"
            ],
            "applications": [
                        "Plasma physics",
                        "Rarefied gas dynamics",
                        "Particle transport"
            ]
},
        'adaptive_viscoelastic': {
            "name": "Viscoelasticity (Adaptive Time)",
            "description": "Viscoelastic equations with adaptive time integration",
            "icon": "fas fa-tint",
            "color": "#3498db",
            "formula": "\u03c3 + \u03c4\u2202\u03c3/\u2202t = E(\u03b5 + \u03c4_\u03b5\u2202\u03b5/\u2202t)",
            "purposes": [
                        "efficiency",
                        "viscoelasticity",
                        "adaptive_methods"
            ],
            "applications": [
                        "Polymer mechanics",
                        "Biological tissues",
                        "Rheology"
            ]
},
        'fast_thermoelastic': {
            "name": "Thermoelasticity (Fast Coupling)",
            "description": "Thermoelastic equations with fast thermal-mechanical coupling",
            "icon": "fas fa-thermometer-half",
            "color": "#e74c3c",
            "formula": "\u2207\u00b7\u03c3 = 0, \u03c1c_p\u2202T/\u2202t = \u2207\u00b7(k\u2207T) - T_0\u03b1\u2207\u00b7\u2202u/\u2202t",
            "purposes": [
                        "efficiency",
                        "thermoelasticity",
                        "fast_methods"
            ],
            "applications": [
                        "Thermal stress",
                        "Heat exchangers",
                        "Electronic packaging"
            ]
},
        'adaptive_magnetohydrodynamics': {
            "name": "Magnetohydrodynamics (Adaptive)",
            "description": "MHD equations with adaptive resolution for plasma dynamics",
            "icon": "fas fa-magnet",
            "color": "#8e44ad",
            "formula": "\u03c1(\u2202v/\u2202t + v\u00b7\u2207v) = -\u2207p + J\u00d7B + \u03bc\u2207\u00b2v, \u2202B/\u2202t = \u2207\u00d7(v\u00d7B - \u03b7\u2207\u00d7B)",
            "purposes": [
                        "efficiency",
                        "magnetohydrodynamics",
                        "adaptive_methods"
            ],
            "applications": [
                        "Plasma physics",
                        "Fusion energy",
                        "Astrophysics"
            ]
},
        'fast_electrokinetics': {
            "name": "Electrokinetics (Fast Solver)",
            "description": "Electrokinetic equations with fast charge transport solvers",
            "icon": "fas fa-bolt",
            "color": "#f39c12",
            "formula": "\u2207\u00b7(\u03b5\u2207\u03c6) = -\u03c1_e, \u2202c/\u2202t = \u2207\u00b7(D\u2207c + \u03bcc\u2207\u03c6)",
            "purposes": [
                        "efficiency",
                        "electrokinetics",
                        "fast_methods"
            ],
            "applications": [
                        "Microfluidics",
                        "Battery systems",
                        "Biosensors"
            ]
},
        'adaptive_fluid_structure': {
            "name": "Fluid-Structure Interaction (Adaptive)",
            "description": "FSI equations with adaptive interface tracking",
            "icon": "fas fa-water",
            "color": "#3498db",
            "formula": "\u03c1_f(\u2202v/\u2202t + v\u00b7\u2207v) = -\u2207p + \u03bc\u2207\u00b2v, \u2207\u00b7\u03c3_s = f_s",
            "purposes": [
                        "efficiency",
                        "fluid_structure",
                        "adaptive_methods"
            ],
            "applications": [
                        "Aeroelasticity",
                        "Biomechanics",
                        "Offshore structures"
            ]
},
        'fast_quantum_thermal': {
            "name": "Quantum-Thermal (Fast Coupling)",
            "description": "Quantum-thermal equations with fast coupling schemes",
            "icon": "fas fa-atom",
            "color": "#1abc9c",
            "formula": "i\u210f\u2202\u03c8/\u2202t = \u0124\u03c8, \u03c1c_p\u2202T/\u2202t = \u2207\u00b7(k\u2207T) + Q_quantum",
            "purposes": [
                        "efficiency",
                        "quantum_thermal",
                        "fast_methods"
            ],
            "applications": [
                        "Quantum devices",
                        "Thermal management",
                        "Quantum computing"
            ]
},
        'adaptive_photo_thermal': {
            "name": "Photo-Thermal (Adaptive)",
            "description": "Photo-thermal equations with adaptive laser tracking",
            "icon": "fas fa-laser",
            "color": "#e74c3c",
            "formula": "\u2202I/\u2202t + c\u2207\u00b7I = -\u03b1I, \u03c1c_p\u2202T/\u2202t = \u2207\u00b7(k\u2207T) + \u03b1I",
            "purposes": [
                        "efficiency",
                        "photo_thermal",
                        "adaptive_methods"
            ],
            "applications": [
                        "Laser processing",
                        "Photothermal therapy",
                        "Optical devices"
            ]
},
        'fast_bio_fluid': {
            "name": "Bio-Fluid Mechanics (Fast)",
            "description": "Bio-fluid equations with fast physiological solvers",
            "icon": "fas fa-heartbeat",
            "color": "#e74c3c",
            "formula": "\u03c1(\u2202v/\u2202t + v\u00b7\u2207v) = -\u2207p + \u03bc\u2207\u00b2v + f_bio, \u2207\u00b7v = 0",
            "purposes": [
                        "efficiency",
                        "bio_fluid",
                        "fast_methods"
            ],
            "applications": [
                        "Blood flow",
                        "Respiratory systems",
                        "Drug delivery"
            ]
},
        'adaptive_combustion': {
            "name": "Combustion (Adaptive Chemistry)",
            "description": "Combustion equations with adaptive chemical kinetics",
            "icon": "fas fa-fire",
            "color": "#e67e22",
            "formula": "\u2202Y/\u2202t + v\u00b7\u2207Y = \u2207\u00b7(\u03c1D\u2207Y) + \u03c9, \u2202T/\u2202t + v\u00b7\u2207T = \u2207\u00b7(k\u2207T) + Q_chem",
            "purposes": [
                        "efficiency",
                        "combustion",
                        "adaptive_methods"
            ],
            "applications": [
                        "Engine design",
                        "Fire safety",
                        "Energy systems"
            ]
},
        'fast_multiphase': {
            "name": "Multiphase Flow (Fast Interface)",
            "description": "Multiphase equations with fast interface tracking",
            "icon": "fas fa-water",
            "color": "#3498db",
            "formula": "\u2202\u03c6/\u2202t + v\u00b7\u2207\u03c6 = 0, \u03c1(\u2202v/\u2202t + v\u00b7\u2207v) = -\u2207p + \u03bc\u2207\u00b2v + \u03c3\u03ba\u2207\u03c6",
            "purposes": [
                        "efficiency",
                        "multiphase",
                        "fast_methods"
            ],
            "applications": [
                        "Bubble dynamics",
                        "Droplet formation",
                        "Emulsion flows"
            ]
}}
    
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
    
    # Inverse Problems Research Applications
    INVERSE_PROBLEMS_APPLICATIONS = {
        "additive_manufacturing_inverse": {
        "name": "Additive Manufacturing Parameter Inference",
        "description": "Infer material properties and process parameters in 3D printing",
        "equations": [
                "heat_transfer_phase_change_inverse",
                "stefan_condition_inverse",
                "navier_stokes_free_surface_inverse",
                "thermal_stress_inverse"
        ],
        "challenges": [
                "Multi-physics coupling",
                "Real-time parameter estimation",
                "Process optimization"
        ],
        "benefits": [
                "Improved process control",
                "Defect reduction",
                "Digital twin support"
        ]
},
        "material_science_inverse": {
        "name": "Material Science Parameter Identification",
        "description": "Infer material properties from microstructure and mechanical data",
        "equations": [
                "phase_field_inverse",
                "cahn_hilliard_inverse",
                "fick_second_law_inverse",
                "crystal_plasticity_inverse"
        ],
        "challenges": [
                "Multi-scale modeling",
                "Experimental validation",
                "Parameter sensitivity"
        ],
        "benefits": [
                "Accelerated material discovery",
                "Enhanced multiscale modeling",
                "Property optimization"
        ]
},
        "battery_systems_inverse": {
        "name": "Battery and Energy Systems",
        "description": "Infer electrochemical and thermal properties in energy storage",
        "equations": [
                "nernst_planck_inverse",
                "heat_transfer_phase_change_inverse",
                "reaction_kinetics_inverse"
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
        "biomechanics_inverse": {
        "name": "Biomechanics Parameter Inference",
        "description": "Infer tissue properties and flow parameters from medical data",
        "equations": [
                "poroelasticity_inverse",
                "navier_stokes_inverse",
                "fick_second_law_inverse"
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
        "geophysics_inverse": {
        "name": "Geophysics Parameter Estimation",
        "description": "Infer subsurface properties from geophysical measurements",
        "equations": [
                "wave_inverse",
                "darcy_law_inverse",
                "poroelasticity_inverse"
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
        "fusion_energy_inverse": {
        "name": "Fusion Energy Parameter Inference",
        "description": "Infer plasma properties and magnetic field parameters",
        "equations": [
                "magnetohydrodynamics_inverse",
                "heat_transfer_phase_change_inverse",
                "maxwell_inverse"
        ],
        "challenges": [
                "High-dimensional systems",
                "Complex physics",
                "Safety requirements"
        ],
        "benefits": [
                "Fusion reactor design",
                "Plasma control",
                "Energy production"
        ]
},
        "thermal_property_identification": {
        "name": "Thermal Property Identification",
        "description": "Infer thermal conductivity, heat capacity, and heat sources",
        "equations": [
                "heat_inverse",
                "heat_transfer_phase_change_inverse",
                "stefan_condition_inverse"
        ],
        "challenges": [
                "Spatial variation",
                "Temporal dynamics",
                "Boundary conditions"
        ],
        "benefits": [
                "Material characterization",
                "Process optimization",
                "Quality control"
        ]
},
        "fluid_parameter_estimation": {
        "name": "Fluid Parameter Estimation",
        "description": "Infer viscosity, flow rates, and boundary conditions",
        "equations": [
                "navier_stokes_inverse",
                "burgers_inverse",
                "navier_stokes_free_surface_inverse"
        ],
        "challenges": [
                "Turbulence modeling",
                "Multi-phase flows",
                "Boundary layer effects"
        ],
        "benefits": [
                "Flow optimization",
                "Process control",
                "Performance prediction"
        ]
},
        "wave_source_localization": {
        "name": "Wave Source Localization",
        "description": "Locate sources and estimate wave speeds from field measurements",
        "equations": [
                "wave_inverse",
                "helmholtz_inverse",
                "elastic_wave_inverse"
        ],
        "challenges": [
                "Source localization",
                "Wave speed estimation",
                "Noise filtering"
        ],
        "benefits": [
                "Seismic analysis",
                "Acoustic imaging",
                "Material characterization"
        ]
},
        "quantum_parameter_inference": {
        "name": "Quantum Parameter Inference",
        "description": "Infer quantum potentials and energy states",
        "equations": [
                "schrodinger_inverse",
                "maxwell_inverse"
        ],
        "challenges": [
                "Quantum effects",
                "Energy level determination",
                "Potential reconstruction"
        ],
        "benefits": [
                "Quantum computing",
                "Material properties",
                "Device optimization"
        ]
}
    }

    # Inverse Problems Loss Function Components
    INVERSE_PROBLEMS_LOSS_COMPONENTS = {
        "data_fidelity": {
        "name": "Data Fidelity Loss",
        "formula": "L_data = (1/N_d) \u03a3|u(x_i,t_i) - u_obs(x_i,t_i)|\u00b2",
        "description": "Ensures neural network fits observed data points",
        "weight_range": [
                0.1,
                100.0
        ],
        "default_weight": 10.0
},
        "physics_residual": {
        "name": "Physics Residual Loss",
        "formula": "L_physics = (1/N_r) \u03a3|N[u,\u03b8](x_j,t_j)|\u00b2",
        "description": "Enforces governing physical equations with unknown parameters \u03b8",
        "weight_range": [
                0.1,
                10.0
        ],
        "default_weight": 1.0
},
        "parameter_regularization": {
        "name": "Parameter Regularization Loss",
        "formula": "L_param = \u03bb||\u03b8 - \u03b8_prior||\u00b2",
        "description": "Regularizes unknown parameters with prior knowledge",
        "weight_range": [
                0.001,
                1.0
        ],
        "default_weight": 0.01
},
        "boundary_conditions": {
        "name": "Boundary Condition Loss",
        "formula": "L_bc = (1/N_bc) \u03a3|u(x_bc,t) - u_bc|\u00b2",
        "description": "Ensures solution satisfies known boundary conditions",
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
        "parameter_bounds": {
        "name": "Parameter Bounds Loss",
        "formula": "L_bounds = \u03a3 max(0, \u03b8_min - \u03b8)\u00b2 + max(0, \u03b8 - \u03b8_max)\u00b2",
        "description": "Enforces physical bounds on unknown parameters",
        "weight_range": [
                0.1,
                100.0
        ],
        "default_weight": 10.0
},
        "smoothness_regularization": {
        "name": "Smoothness Regularization Loss",
        "formula": "L_smooth = \u03bb||\u2207\u03b8||\u00b2",
        "description": "Ensures smooth spatial variation of parameters",
        "weight_range": [
                0.001,
                1.0
        ],
        "default_weight": 0.01
},
        "temporal_consistency": {
        "name": "Temporal Consistency Loss",
        "formula": "L_temp = \u03bb||\u2202\u03b8/\u2202t||\u00b2",
        "description": "Ensures temporal consistency of time-varying parameters",
        "weight_range": [
                0.001,
                1.0
        ],
        "default_weight": 0.01
}
    }
    
    # Sparse/Noisy Data Research Applications
    SPARSE_DATA_APPLICATIONS = {
        "additive_manufacturing_sparse": {
        "name": "Additive Manufacturing Data Processing",
        "description": "Reconstruct thermal and mechanical fields from sparse sensor data in 3D printing",
        "equations": [
                "heat_transfer_phase_change_sparse",
                "stefan_condition_sparse",
                "navier_stokes_free_surface_sparse",
                "thermal_stress_sparse"
        ],
        "challenges": [
                "Sparse thermal imaging",
                "Noisy sensor data",
                "Real-time processing"
        ],
        "benefits": [
                "Improved process monitoring",
                "Reduced experimental costs",
                "Real-time analysis"
        ]
},
        "material_science_sparse": {
        "name": "Material Science Data Analysis",
        "description": "Reconstruct microstructure and mechanical properties from sparse experimental data",
        "equations": [
                "phase_field_sparse",
                "cahn_hilliard_sparse",
                "fick_second_law_sparse",
                "crystal_plasticity_sparse"
        ],
        "challenges": [
                "Sparse microscopy data",
                "Noisy mechanical tests",
                "Multi-scale modeling"
        ],
        "benefits": [
                "Accelerated material characterization",
                "Support for multiscale modeling",
                "Reduced experimental time"
        ]
},
        "battery_systems_sparse": {
        "name": "Battery and Energy Systems",
        "description": "Reconstruct electrochemical and thermal fields from sparse voltage/temperature data",
        "equations": [
                "nernst_planck_sparse",
                "heat_transfer_phase_change_sparse",
                "reaction_diffusion_sparse"
        ],
        "challenges": [
                "Sparse voltage measurements",
                "Noisy temperature data",
                "Safety constraints"
        ],
        "benefits": [
                "Enhanced battery design",
                "Improved safety analysis",
                "Better performance prediction"
        ]
},
        "biomechanics_sparse": {
        "name": "Biomechanics Data Processing",
        "description": "Reconstruct tissue mechanics and blood flow from sparse medical imaging data",
        "equations": [
                "poroelasticity_sparse",
                "navier_stokes_sparse",
                "advection_diffusion_sparse"
        ],
        "challenges": [
                "Sparse imaging data",
                "Patient-specific modeling",
                "Validation difficulties"
        ],
        "benefits": [
                "Support for personalized medicine",
                "Reduced imaging requirements",
                "Better treatment planning"
        ]
},
        "geophysics_sparse": {
        "name": "Geophysics Data Reconstruction",
        "description": "Reconstruct subsurface properties and wave fields from sparse geophysical data",
        "equations": [
                "wave_sparse",
                "poroelasticity_sparse",
                "elastic_wave_sparse"
        ],
        "challenges": [
                "Sparse seismometer data",
                "Noisy field measurements",
                "Inverse problems"
        ],
        "benefits": [
                "Improved subsurface imaging",
                "Enhanced disaster prediction",
                "Better resource exploration"
        ]
},
        "fusion_energy_sparse": {
        "name": "Fusion Energy Diagnostics",
        "description": "Reconstruct plasma fields from sparse diagnostic data in fusion reactors",
        "equations": [
                "magnetohydrodynamics_sparse",
                "heat_transfer_sparse",
                "maxwell_sparse"
        ],
        "challenges": [
                "Sparse diagnostic data",
                "High-dimensional systems",
                "Safety requirements"
        ],
        "benefits": [
                "Support for fusion reactor diagnostics",
                "Handles sparse data effectively",
                "Real-time plasma monitoring"
        ]
},
        "experimental_data_analysis": {
        "name": "Experimental Data Analysis",
        "description": "Reconstruct fields from sparse laboratory and field measurements",
        "equations": [
                "burgers_sparse",
                "heat_sparse",
                "wave_sparse",
                "helmholtz_sparse"
        ],
        "challenges": [
                "Limited lab data",
                "Noisy measurements",
                "Field observations"
        ],
        "benefits": [
                "Better data utilization",
                "Reduced experimental costs",
                "Improved accuracy"
        ]
},
        "noisy_data_processing": {
        "name": "Noisy Data Processing",
        "description": "Denoise and reconstruct fields from noisy experimental data",
        "equations": [
                "all_sparse_equations"
        ],
        "challenges": [
                "Signal denoising",
                "Measurement filtering",
                "Data reconstruction"
        ],
        "benefits": [
                "Cleaner data",
                "Better predictions",
                "Robust analysis"
        ]
},
        "data_augmentation": {
        "name": "Data Augmentation",
        "description": "Generate physics-consistent synthetic data to supplement sparse datasets",
        "equations": [
                "all_sparse_equations"
        ],
        "challenges": [
                "Synthetic data generation",
                "Physics-based augmentation",
                "Training data expansion"
        ],
        "benefits": [
                "Larger training datasets",
                "Better model performance",
                "Reduced data requirements"
        ]
},
        "robust_learning": {
        "name": "Robust Learning",
        "description": "Enable robust parameter inference and uncertainty quantification from sparse data",
        "equations": [
                "all_sparse_equations"
        ],
        "challenges": [
                "Outlier detection",
                "Robust estimation",
                "Uncertainty quantification"
        ],
        "benefits": [
                "Better generalization",
                "Confidence intervals",
                "Robust predictions"
        ]
}
    }

    # Sparse/Noisy Data Loss Function Components
    SPARSE_DATA_LOSS_COMPONENTS = {
        "data_fidelity": {
        "name": "Data Fidelity Loss",
        "formula": "L_data = (1/N_d) \u03a3|u(x_i,t_i) - u_obs(x_i,t_i)|\u00b2",
        "description": "Ensures neural network fits observed data points (typically sparse)",
        "weight_range": [
                0.1,
                100.0
        ],
        "default_weight": 10.0
},
        "physics_residual": {
        "name": "Physics Residual Loss",
        "formula": "L_physics = (1/N_r) \u03a3|N[u](x_j,t_j)|\u00b2",
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
        "regularization": {
        "name": "Regularization Loss",
        "formula": "L_reg = \u03bb||\u2207u||\u00b2",
        "description": "Prevents overfitting and ensures smooth solutions",
        "weight_range": [
                0.001,
                1.0
        ],
        "default_weight": 0.01
},
        "noise_robustness": {
        "name": "Noise Robustness Loss",
        "formula": "L_noise = \u03bc||\u2207\u00b2u||\u00b2",
        "description": "Enhances robustness to noisy data",
        "weight_range": [
                0.001,
                1.0
        ],
        "default_weight": 0.01
},
        "consistency": {
        "name": "Consistency Loss",
        "formula": "L_consistency = \u03b3||u - smooth(u)||\u00b2",
        "description": "Ensures consistency across different data points",
        "weight_range": [
                0.01,
                1.0
        ],
        "default_weight": 0.1
},
        "outlier_penalty": {
        "name": "Outlier Penalty Loss",
        "formula": "L_outlier = \u03b4\u03a3 max(0, |u(x_i,t_i) - u_obs(x_i,t_i)| - \u03c4)\u00b2",
        "description": "Penalizes outliers in the data",
        "weight_range": [
                0.1,
                10.0
        ],
        "default_weight": 1.0
},
        "interpolation": {
        "name": "Interpolation Loss",
        "formula": "L_interp = \u03ba||\u2207\u00b3u||\u00b2",
        "description": "Ensures smooth interpolation between sparse data points",
        "weight_range": [
                0.001,
                1.0
        ],
        "default_weight": 0.01
},
        "physics_consistency": {
        "name": "Physics Consistency Loss",
        "formula": "L_physics_consistency = \u03b6||\u2202N[u]/\u2202t||\u00b2",
        "description": "Ensures temporal consistency of physics constraints",
        "weight_range": [
                0.01,
                1.0
        ],
        "default_weight": 0.1
}
    }
    
    # Uncertainty Quantification Research Applications
    UNCERTAINTY_APPLICATIONS = {
        "risk_assessment": {
        "name": "Risk Assessment and Reliability Analysis",
        "description": "Quantify uncertainty in structural failure predictions and safety margins",
        "equations": [
                "heat_equation_uq",
                "navier_stokes_uq",
                "shm_uq",
                "multi_objective_control_uq"
        ],
        "uq_methods": [
                "Bayesian PINNs",
                "Monte Carlo Simulation",
                "First-Order Reliability Method"
        ],
        "challenges": [
                "Rare event probability estimation",
                "High-dimensional uncertainty propagation",
                "Computational cost of reliability analysis"
        ],
        "benefits": [
                "Quantified safety margins",
                "Confidence intervals for failure predictions",
                "Risk-informed decision making"
        ]
},
        "sensitivity_analysis": {
        "name": "Sensitivity Analysis and Parameter Identification",
        "description": "Identify critical parameters and quantify their impact on system behavior",
        "equations": [
                "all_uq_equations"
        ],
        "uq_methods": [
                "Sobol Indices",
                "Global Sensitivity Analysis",
                "Variance-Based Methods"
        ],
        "challenges": [
                "High-dimensional parameter spaces",
                "Nonlinear parameter interactions",
                "Computational efficiency"
        ],
        "benefits": [
                "Parameter importance ranking",
                "Model simplification guidance",
                "Experimental design optimization"
        ]
},
        "data_driven_uq": {
        "name": "Data-Driven Uncertainty Quantification",
        "description": "Quantify measurement uncertainty and experimental errors using physics-informed methods",
        "equations": [
                "all_uq_equations"
        ],
        "uq_methods": [
                "Bayesian PINNs",
                "Gaussian Processes",
                "Ensemble Methods"
        ],
        "challenges": [
                "Noisy experimental data",
                "Limited measurement points",
                "Sensor calibration uncertainty"
        ],
        "benefits": [
                "Physics-regularized uncertainty estimates",
                "Improved data quality assessment",
                "Robust parameter inference"
        ]
},
        "decision_support": {
        "name": "Decision Support Under Uncertainty",
        "description": "Provide probabilistic predictions for optimization and policy-making",
        "equations": [
                "multi_objective_control_uq",
                "navier_stokes_uq",
                "heat_equation_uq"
        ],
        "uq_methods": [
                "Bayesian Optimization",
                "Robust Optimization",
                "Stochastic Programming"
        ],
        "challenges": [
                "Multi-objective optimization under uncertainty",
                "Risk-averse decision making",
                "Real-time uncertainty quantification"
        ],
        "benefits": [
                "Uncertainty-aware optimization",
                "Robust system design",
                "Risk-informed policies"
        ]
},
        "additive_manufacturing_uq": {
        "name": "Additive Manufacturing Uncertainty Quantification",
        "description": "Quantify uncertainty in 3D printing processes and part quality predictions",
        "equations": [
                "heat_transfer_phase_change_uq",
                "stefan_condition_uq",
                "navier_stokes_free_surface_uq",
                "thermal_stress_uq"
        ],
        "uq_methods": [
                "Bayesian PINNs",
                "Monte Carlo Dropout",
                "Ensemble Methods"
        ],
        "challenges": [
                "Process parameter variability",
                "Material property uncertainty",
                "Real-time quality prediction"
        ],
        "benefits": [
                "Process optimization under uncertainty",
                "Quality assurance with confidence intervals",
                "Reduced experimental costs"
        ]
},
        "material_science_uq": {
        "name": "Material Science Uncertainty Quantification",
        "description": "Quantify uncertainty in material properties and microstructure evolution",
        "equations": [
                "phase_field_uq",
                "cahn_hilliard_uq",
                "fick_second_law_uq",
                "crystal_plasticity_uq"
        ],
        "uq_methods": [
                "Bayesian PINNs",
                "Variational Inference",
                "Gaussian Processes"
        ],
        "challenges": [
                "Multi-scale uncertainty propagation",
                "Microstructure variability",
                "Property-structure relationships"
        ],
        "benefits": [
                "Accelerated material discovery",
                "Property prediction with uncertainty",
                "Design optimization under uncertainty"
        ]
},
        "battery_systems_uq": {
        "name": "Battery and Energy Systems Uncertainty Quantification",
        "description": "Quantify uncertainty in battery performance and electrochemical processes",
        "equations": [
                "nernst_planck_uq",
                "heat_transfer_phase_change_uq",
                "reaction_diffusion_uq"
        ],
        "uq_methods": [
                "Bayesian PINNs",
                "Monte Carlo Methods",
                "Gaussian Processes"
        ],
        "challenges": [
                "Aging uncertainty",
                "Temperature-dependent properties",
                "Safety constraints"
        ],
        "benefits": [
                "Battery lifetime prediction",
                "Safety assessment with confidence",
                "Performance optimization"
        ]
},
        "biomechanics_uq": {
        "name": "Biomechanics Uncertainty Quantification",
        "description": "Quantify uncertainty in tissue mechanics and biological systems",
        "equations": [
                "poroelasticity_uq",
                "navier_stokes_uq",
                "advection_diffusion_uq"
        ],
        "uq_methods": [
                "Bayesian PINNs",
                "Variational Inference",
                "Ensemble Methods"
        ],
        "challenges": [
                "Patient-specific variability",
                "Biological uncertainty",
                "Validation difficulties"
        ],
        "benefits": [
                "Personalized medicine support",
                "Treatment planning with uncertainty",
                "Biomechanical modeling"
        ]
},
        "fusion_energy_uq": {
        "name": "Fusion Energy Uncertainty Quantification",
        "description": "Quantify uncertainty in plasma dynamics and fusion reactor performance",
        "equations": [
                "magnetohydrodynamics_uq",
                "heat_transfer_uq",
                "maxwell_uq"
        ],
        "uq_methods": [
                "Bayesian PINNs",
                "Monte Carlo Sampling",
                "Gaussian Processes"
        ],
        "challenges": [
                "High-dimensional plasma physics",
                "Diagnostic uncertainty",
                "Safety requirements"
        ],
        "benefits": [
                "Plasma stability prediction",
                "Reactor design optimization",
                "Safety assessment"
        ]
},
        "quantum_systems_uq": {
        "name": "Quantum Systems Uncertainty Quantification",
        "description": "Quantify uncertainty in quantum mechanical systems and wave functions",
        "equations": [
                "schrodinger_uq",
                "maxwell_uq",
                "quantum_control_uq"
        ],
        "uq_methods": [
                "Variational Quantum Eigensolver",
                "Quantum Monte Carlo",
                "Bayesian Quantum Methods"
        ],
        "challenges": [
                "Quantum measurement uncertainty",
                "Decoherence effects",
                "Computational complexity"
        ],
        "benefits": [
                "Quantum state prediction",
                "Quantum control optimization",
                "Quantum error correction"
        ]
}
    }

    # Uncertainty Quantification Loss Function Components
    UNCERTAINTY_LOSS_COMPONENTS = {
        "data_fidelity_uq": {
        "name": "Data Fidelity Loss (Uncertainty)",
        "formula": "L_data = (1/N_d) \u03a3|u(x_i,t_i) - u_obs(x_i,t_i)|\u00b2",
        "description": "Ensures neural network fits observed data with uncertainty quantification",
        "weight_range": [
                0.1,
                100.0
        ],
        "default_weight": 10.0,
        "uq_methods": [
                "Bayesian PINNs",
                "Ensemble Methods",
                "Monte Carlo Dropout"
        ]
},
        "physics_residual_uq": {
        "name": "Physics Residual Loss (Uncertainty)",
        "formula": "L_physics = (1/N_r) \u03a3|N[u,\u03b8](x_j,t_j)|\u00b2",
        "description": "Enforces governing equations with uncertain parameters \u03b8",
        "weight_range": [
                0.1,
                10.0
        ],
        "default_weight": 1.0,
        "uq_methods": [
                "Bayesian PINNs",
                "Variational Inference",
                "Monte Carlo Methods"
        ]
},
        "boundary_conditions_uq": {
        "name": "Boundary Condition Loss (Uncertainty)",
        "formula": "L_bc = (1/N_bc) \u03a3|u(x_bc,t) - u_bc|\u00b2",
        "description": "Ensures solution satisfies boundary conditions with uncertainty",
        "weight_range": [
                0.1,
                10.0
        ],
        "default_weight": 1.0,
        "uq_methods": [
                "Bayesian PINNs",
                "Gaussian Processes",
                "Ensemble Methods"
        ]
},
        "initial_conditions_uq": {
        "name": "Initial Condition Loss (Uncertainty)",
        "formula": "L_ic = (1/N_ic) \u03a3|u(x,t=0) - u_ic(x)|\u00b2",
        "description": "Ensures solution satisfies initial conditions with uncertainty",
        "weight_range": [
                0.1,
                10.0
        ],
        "default_weight": 1.0,
        "uq_methods": [
                "Bayesian PINNs",
                "Variational Inference",
                "Monte Carlo Methods"
        ]
},
        "kl_divergence": {
        "name": "KL Divergence Loss",
        "formula": "L_KL = KL(q(\u03b8)||p(\u03b8))",
        "description": "Regularizes Bayesian posterior approximation",
        "weight_range": [
                0.001,
                1.0
        ],
        "default_weight": 0.01,
        "uq_methods": [
                "Bayesian PINNs",
                "Variational Inference"
        ]
},
        "uncertainty_regularization": {
        "name": "Uncertainty Regularization Loss",
        "formula": "L_uncertainty = \u03bb||\u03c3\u00b2||\u00b2",
        "description": "Regularizes uncertainty estimates to prevent overconfidence",
        "weight_range": [
                0.001,
                1.0
        ],
        "default_weight": 0.01,
        "uq_methods": [
                "Bayesian PINNs",
                "Ensemble Methods",
                "Monte Carlo Dropout"
        ]
},
        "calibration_loss": {
        "name": "Calibration Loss",
        "formula": "L_calibration = \u03a3|P(y\u2208CI) - \u03b1|\u00b2",
        "description": "Ensures uncertainty estimates are well-calibrated",
        "weight_range": [
                0.01,
                1.0
        ],
        "default_weight": 0.1,
        "uq_methods": [
                "Bayesian PINNs",
                "Ensemble Methods",
                "Conformal Prediction"
        ]
},
        "ensemble_diversity": {
        "name": "Ensemble Diversity Loss",
        "formula": "L_diversity = -\u03bb \u03a3\u1d62\u2260\u2c7c cov(u\u1d62, u\u2c7c)",
        "description": "Promotes diversity in ensemble predictions",
        "weight_range": [
                0.01,
                1.0
        ],
        "default_weight": 0.1,
        "uq_methods": [
                "Deep Ensembles",
                "Monte Carlo Dropout"
        ]
},
        "aleatoric_uncertainty": {
        "name": "Aleatoric Uncertainty Loss",
        "formula": "L_aleatoric = (1/N) \u03a3 log(\u03c3\u00b2_aleatoric) + (y - \u03bc)\u00b2/\u03c3\u00b2_aleatoric",
        "description": "Models data noise and measurement uncertainty",
        "weight_range": [
                0.1,
                10.0
        ],
        "default_weight": 1.0,
        "uq_methods": [
                "Bayesian PINNs",
                "Heteroscedastic Models"
        ]
},
        "epistemic_uncertainty": {
        "name": "Epistemic Uncertainty Loss",
        "formula": "L_epistemic = (1/N) \u03a3 \u03c3\u00b2_epistemic",
        "description": "Models model uncertainty and parameter uncertainty",
        "weight_range": [
                0.01,
                1.0
        ],
        "default_weight": 0.1,
        "uq_methods": [
                "Bayesian PINNs",
                "Monte Carlo Dropout",
                "Deep Ensembles"
        ]
},
        "conformal_prediction": {
        "name": "Conformal Prediction Loss",
        "formula": "L_conformal = \u03a3 max(0, |y - \u03bc| - \u03c3\u00b7q_\u03b1)",
        "description": "Ensures prediction intervals have desired coverage",
        "weight_range": [
                0.1,
                10.0
        ],
        "default_weight": 1.0,
        "uq_methods": [
                "Conformal Prediction",
                "Calibrated Uncertainty"
        ]
},
        "robustness_loss": {
        "name": "Robustness Loss",
        "formula": "L_robust = E_\u03b5[||\u2207u(x+\u03b5) - \u2207u(x)||\u00b2]",
        "description": "Promotes robustness to input perturbations",
        "weight_range": [
                0.001,
                1.0
        ],
        "default_weight": 0.01,
        "uq_methods": [
                "Adversarial Training",
                "Robust Optimization"
        ]
},
        "sensitivity_loss": {
        "name": "Sensitivity Loss",
        "formula": "L_sensitivity = \u03a3\u1d62 (\u2202u/\u2202\u03b8\u1d62)\u00b2",
        "description": "Penalizes high sensitivity to parameter changes",
        "weight_range": [
                0.001,
                1.0
        ],
        "default_weight": 0.01,
        "uq_methods": [
                "Sensitivity Analysis",
                "Robust Design"
        ]
}
    }
    
    # Scientific Discovery Research Applications
    SCIENTIFIC_DISCOVERY_APPLICATIONS = {
        "additive_manufacturing_discovery": {
        "name": "Additive Manufacturing Discovery",
        "description": "Discover governing equations and parameters for 3D printing processes",
        "equations": [
                "heat_transfer_phase_change_discovery",
                "stefan_condition_discovery",
                "navier_stokes_free_surface_discovery",
                "thermal_stress_discovery"
        ],
        "challenges": [
                "Complex multiphysics interactions",
                "Process parameter identification",
                "Material property discovery"
        ],
        "benefits": [
                "Enhanced process understanding",
                "Reduced experimental trials",
                "Support for digital twins"
        ]
},
        "material_science_discovery": {
        "name": "Material Science Discovery",
        "description": "Discover microstructure dynamics and material behavior models",
        "equations": [
                "phase_field_discovery",
                "cahn_hilliard_discovery",
                "fick_second_law_discovery",
                "crystal_plasticity_discovery"
        ],
        "challenges": [
                "Multi-scale modeling",
                "Complex constitutive relations",
                "Experimental data limitations"
        ],
        "benefits": [
                "Accelerated material discovery",
                "Support for multiscale modeling",
                "Enhanced property prediction"
        ]
},
        "battery_energy_discovery": {
        "name": "Battery and Energy Systems Discovery",
        "description": "Discover electrochemical dynamics and energy storage mechanisms",
        "equations": [
                "nernst_planck_discovery",
                "heat_transfer_discovery",
                "reaction_diffusion_discovery"
        ],
        "challenges": [
                "Electrochemical complexity",
                "Safety constraints",
                "Performance optimization"
        ],
        "benefits": [
                "Improved battery design",
                "Enhanced energy system models",
                "Better performance prediction"
        ]
},
        "biomechanics_discovery": {
        "name": "Biomechanics Discovery",
        "description": "Discover biomechanical constitutive relations and tissue dynamics",
        "equations": [
                "navier_stokes_discovery",
                "poroelasticity_discovery",
                "advection_diffusion_discovery"
        ],
        "challenges": [
                "Patient-specific modeling",
                "Biological complexity",
                "Validation difficulties"
        ],
        "benefits": [
                "Support for personalized medicine",
                "Enhanced biomechanical modeling",
                "Better treatment planning"
        ]
},
        "geophysics_discovery": {
        "name": "Geophysics Discovery",
        "description": "Discover subsurface dynamics and geophysical processes",
        "equations": [
                "elastic_wave_discovery",
                "advection_diffusion_discovery",
                "navier_stokes_discovery"
        ],
        "challenges": [
                "Limited subsurface data",
                "Complex geological structures",
                "Multi-scale phenomena"
        ],
        "benefits": [
                "Improved subsurface modeling",
                "Enhanced disaster prediction",
                "Better resource exploration"
        ]
},
        "fusion_energy_discovery": {
        "name": "Fusion Energy Discovery",
        "description": "Discover plasma dynamics and fusion reactor physics",
        "equations": [
                "magnetohydrodynamics_discovery",
                "maxwell_discovery",
                "heat_transfer_discovery"
        ],
        "challenges": [
                "Plasma complexity",
                "High-dimensional systems",
                "Safety requirements"
        ],
        "benefits": [
                "Support for fusion reactor design",
                "Advances plasma physics",
                "Enhanced confinement understanding"
        ]
},
        "quantum_systems_discovery": {
        "name": "Quantum Systems Discovery",
        "description": "Discover quantum dynamics and quantum computing mechanisms",
        "equations": [
                "schrodinger_discovery",
                "schrodinger_uq_discovery",
                "maxwell_discovery"
        ],
        "challenges": [
                "Quantum complexity",
                "Measurement limitations",
                "Decoherence effects"
        ],
        "benefits": [
                "Enhanced quantum computing",
                "Improved quantum chemistry",
                "Better quantum materials"
        ]
},
        "chemical_reactions_discovery": {
        "name": "Chemical Reactions Discovery",
        "description": "Discover reaction mechanisms and catalytic processes",
        "equations": [
                "reaction_diffusion_discovery",
                "reaction_diffusion_sparse_discovery",
                "nernst_planck_discovery"
        ],
        "challenges": [
                "Reaction complexity",
                "Catalyst identification",
                "Kinetic modeling"
        ],
        "benefits": [
                "Improved catalyst design",
                "Enhanced reaction optimization",
                "Better chemical processes"
        ]
},
        "biological_systems_discovery": {
        "name": "Biological Systems Discovery",
        "description": "Discover biological dynamics and cellular processes",
        "equations": [
                "reaction_diffusion_discovery",
                "poroelasticity_discovery",
                "advection_diffusion_discovery"
        ],
        "challenges": [
                "Biological complexity",
                "Multi-scale interactions",
                "Experimental limitations"
        ],
        "benefits": [
                "Enhanced biological understanding",
                "Improved drug design",
                "Better disease modeling"
        ]
},
        "complex_systems_discovery": {
        "name": "Complex Systems Discovery",
        "description": "Discover emergent patterns and collective behavior",
        "equations": [
                "reaction_diffusion_discovery",
                "phase_field_discovery",
                "navier_stokes_discovery"
        ],
        "challenges": [
                "Emergent complexity",
                "Pattern identification",
                "Multi-scale dynamics"
        ],
        "benefits": [
                "Enhanced system understanding",
                "Improved pattern prediction",
                "Better control strategies"
        ]
}
    }

    # Scientific Discovery Loss Function Components
    SCIENTIFIC_DISCOVERY_LOSS_COMPONENTS = {
        "data_fidelity": {
        "name": "Data Fidelity Loss",
        "formula": "L_data = (1/N_d) \u03a3|u(x_i,t_i) - u_obs(x_i,t_i)|\u00b2",
        "description": "Ensures neural network fits observed data points",
        "weight_range": [
                0.1,
                100.0
        ],
        "default_weight": 10.0
},
        "physics_residual": {
        "name": "Physics Residual Loss",
        "formula": "L_physics = (1/N_r) \u03a3|N[u,\u03b8](x_j,t_j)|\u00b2",
        "description": "Enforces candidate or known PDEs/ODEs",
        "weight_range": [
                0.1,
                10.0
        ],
        "default_weight": 1.0
},
        "sparsity_regularization": {
        "name": "Sparsity Regularization Loss",
        "formula": "L_sparse = \u03bb||\u03b8||\u2081",
        "description": "Promotes interpretable, parsimonious models",
        "weight_range": [
                0.001,
                1.0
        ],
        "default_weight": 0.01
},
        "smoothness_regularization": {
        "name": "Smoothness Regularization Loss",
        "formula": "L_smooth = \u03bc||\u2207\u03b8||\u00b2",
        "description": "Ensures smooth parameter fields",
        "weight_range": [
                0.001,
                1.0
        ],
        "default_weight": 0.01
},
        "interpretability": {
        "name": "Interpretability Loss",
        "formula": "L_interpret = \u03b3||\u03b8 - \u03b8_prior||\u00b2",
        "description": "Encourages physically meaningful parameters",
        "weight_range": [
                0.01,
                1.0
        ],
        "default_weight": 0.1
},
        "equation_discovery": {
        "name": "Equation Discovery Loss",
        "formula": "L_discovery = \u03b4||\u2207\u00b2u - f(u,\u2207u,\u03b8)||\u00b2",
        "description": "Discovers governing equations from data",
        "weight_range": [
                0.1,
                10.0
        ],
        "default_weight": 1.0
},
        "parameter_identification": {
        "name": "Parameter Identification Loss",
        "formula": "L_param = \u03b6||\u03b8 - \u03b8_true||\u00b2",
        "description": "Identifies unknown parameters in known equations",
        "weight_range": [
                0.1,
                10.0
        ],
        "default_weight": 1.0
},
        "constitutive_discovery": {
        "name": "Constitutive Discovery Loss",
        "formula": "L_constitutive = \u03b7||\u03c3 - C(\u03b5,\u03b8)||\u00b2",
        "description": "Discovers constitutive relations",
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
        "symmetry_preservation": {
        "name": "Symmetry Preservation Loss",
        "formula": "L_symmetry = \u03ba||u(x) - u(T(x))||\u00b2",
        "description": "Preserves physical symmetries in discovered equations",
        "weight_range": [
                0.01,
                1.0
        ],
        "default_weight": 0.1
},
        "causality": {
        "name": "Causality Loss",
        "formula": "L_causality = \u03bd||\u2202u/\u2202t - f(u,\u2207u,\u03b8)||\u00b2",
        "description": "Ensures discovered equations respect causality",
        "weight_range": [
                0.1,
                10.0
        ],
        "default_weight": 1.0
},
        "conservation_laws": {
        "name": "Conservation Laws Loss",
        "formula": "L_conservation = \u03be||\u2207\u00b7J + \u2202\u03c1/\u2202t||\u00b2",
        "description": "Enforces conservation laws in discovered equations",
        "weight_range": [
                0.1,
                10.0
        ],
        "default_weight": 1.0
}
    }
    
    # Generalization and Robustness Research Applications
    GENERALIZATION_APPLICATIONS = {
        "parameter_space_exploration": {
        "name": "Parameter Space Exploration",
        "description": "Explore diverse parameter combinations and assess robustness to parameter changes",
        "equations": [
                "burgers_generalization",
                "heat_generalization",
                "wave_generalization",
                "schrodinger_generalization",
                "hjb_generalization"
        ],
        "challenges": [
                "High-dimensional parameter spaces",
                "Computational efficiency",
                "Robustness validation"
        ],
        "benefits": [
                "Multi-parameter optimization",
                "Parameter sensitivity analysis",
                "Design space exploration"
        ]
},
        "geometric_generalization": {
        "name": "Geometric Generalization",
        "description": "Adapt to new domain shapes and complex geometries using physics constraints",
        "equations": [
                "all_generalization_equations"
        ],
        "challenges": [
                "Complex domain shapes",
                "Mesh generation",
                "Boundary condition handling"
        ],
        "benefits": [
                "Shape optimization",
                "Geometry transfer learning",
                "Adaptive mesh generation"
        ]
},
        "boundary_condition_adaptation": {
        "name": "Boundary Condition Adaptation",
        "description": "Handle new boundary conditions and ensure stability under condition changes",
        "equations": [
                "all_generalization_equations"
        ],
        "challenges": [
                "BC interpolation",
                "Conditional generation",
                "Stability under BC changes"
        ],
        "benefits": [
                "BC interpolation",
                "Conditional generation",
                "Robust prediction"
        ]
},
        "extrapolation": {
        "name": "Extrapolation Beyond Training Data",
        "description": "Predict beyond training time horizons and parameter ranges using physics",
        "equations": [
                "all_generalization_equations"
        ],
        "challenges": [
                "Time extrapolation",
                "Parameter extrapolation",
                "Physics-guided prediction"
        ],
        "benefits": [
                "Time extrapolation",
                "Parameter extrapolation",
                "Physics-guided prediction"
        ]
},
        "additive_manufacturing_generalization": {
        "name": "Additive Manufacturing Generalization",
        "description": "Predict for new laser powers, material properties, or complex part geometries",
        "equations": [
                "heat_transfer_phase_change_generalization",
                "stefan_condition_generalization",
                "navier_stokes_free_surface_generalization",
                "thermal_stress_generalization"
        ],
        "challenges": [
                "Process parameter adaptation",
                "Part geometry generalization",
                "Thermal/stress extrapolation"
        ],
        "benefits": [
                "Enhanced process robustness",
                "Support for design optimization",
                "Reduced experimental trials"
        ]
},
        "material_science_generalization": {
        "name": "Material Science Generalization",
        "description": "Predict for new material compositions, processing conditions, or loading scenarios",
        "equations": [
                "phase_field_generalization",
                "cahn_hilliard_generalization",
                "fick_second_law_generalization",
                "crystal_plasticity_generalization"
        ],
        "challenges": [
                "Microstructure adaptation",
                "Diffusion generalization",
                "Mechanical behavior extrapolation"
        ],
        "benefits": [
                "Accelerated material design",
                "Support for multiscale modeling robustness",
                "Enhanced property prediction"
        ]
},
        "battery_energy_generalization": {
        "name": "Battery and Energy Systems Generalization",
        "description": "Predict for new electrode materials, cell designs, or operating conditions",
        "equations": [
                "nernst_planck_generalization",
                "heat_generalization",
                "reaction_diffusion_generalization"
        ],
        "challenges": [
                "Electrochemical adaptation",
                "Thermal extrapolation",
                "Fuel cell generalization"
        ],
        "benefits": [
                "Improved battery reliability",
                "Enhanced energy system design",
                "Better performance prediction"
        ]
},
        "biomechanics_generalization": {
        "name": "Biomechanics Generalization",
        "description": "Predict for new tissue types, anatomical geometries, or patient-specific conditions",
        "equations": [
                "navier_stokes_generalization",
                "poroelasticity_generalization",
                "advection_diffusion_generalization"
        ],
        "challenges": [
                "Tissue property adaptation",
                "Blood flow generalization",
                "Drug diffusion extrapolation"
        ],
        "benefits": [
                "Support for personalized medicine",
                "Enhanced diagnostic robustness",
                "Better treatment planning"
        ]
},
        "geophysics_generalization": {
        "name": "Geophysics Generalization",
        "description": "Predict for new subsurface conditions, aquifer properties, or environmental variations",
        "equations": [
                "wave_generalization",
                "advection_diffusion_generalization",
                "navier_stokes_generalization"
        ],
        "challenges": [
                "Seismic adaptation",
                "Groundwater flow generalization",
                "Volcanic extrapolation"
        ],
        "benefits": [
                "Improved resource exploration",
                "Enhanced disaster prediction robustness",
                "Better environmental modeling"
        ]
},
        "fusion_energy_generalization": {
        "name": "Fusion Energy Generalization",
        "description": "Predict for new plasma conditions, reactor designs, or operational scenarios",
        "equations": [
                "magnetohydrodynamics_generalization",
                "maxwell_generalization",
                "heat_generalization"
        ],
        "challenges": [
                "Plasma adaptation",
                "Heat flux generalization",
                "Magnetic field extrapolation"
        ],
        "benefits": [
                "Support for fusion reactor design",
                "Enhanced operational robustness",
                "Better plasma confinement"
        ]
}
    }

    # Generalization and Robustness Loss Function Components
    GENERALIZATION_LOSS_COMPONENTS = {
        "data_fidelity": {
        "name": "Data Fidelity Loss",
        "formula": "L_data = (1/N_d) \u03a3|u(x_i,t_i) - u_obs(x_i,t_i)|\u00b2",
        "description": "Ensures neural network fits training data (if available)",
        "weight_range": [
                0.1,
                100.0
        ],
        "default_weight": 10.0
},
        "physics_residual": {
        "name": "Physics Residual Loss",
        "formula": "L_physics = (1/N_r) \u03a3|N[u,\u03b8](x_j,t_j)|\u00b2",
        "description": "Enforces PDE/ODE residuals across the domain",
        "weight_range": [
                0.1,
                10.0
        ],
        "default_weight": 1.0
},
        "boundary_conditions": {
        "name": "Boundary Condition Loss",
        "formula": "L_bc = (1/N_bc) \u03a3|u(x_bc,t) - u_bc|\u00b2",
        "description": "Ensures compliance with boundary conditions",
        "weight_range": [
                0.1,
                10.0
        ],
        "default_weight": 1.0
},
        "initial_conditions": {
        "name": "Initial Condition Loss",
        "formula": "L_ic = (1/N_ic) \u03a3|u(x,t=0) - u_ic(x)|\u00b2",
        "description": "Ensures compliance with initial conditions",
        "weight_range": [
                0.1,
                10.0
        ],
        "default_weight": 1.0
},
        "regularization": {
        "name": "Regularization Loss",
        "formula": "L_reg = \u03bb||\u2207u||\u00b2",
        "description": "Promotes smooth solutions and prevents overfitting",
        "weight_range": [
                0.001,
                1.0
        ],
        "default_weight": 0.01
},
        "robustness": {
        "name": "Robustness Loss",
        "formula": "L_robust = \u03bc||\u2207\u00b2u||\u00b2",
        "description": "Enhances robustness to parameter variations",
        "weight_range": [
                0.001,
                1.0
        ],
        "default_weight": 0.01
},
        "generalization": {
        "name": "Generalization Loss",
        "formula": "L_gen = \u03b3||u - u_prior||\u00b2",
        "description": "Encourages solutions close to prior knowledge",
        "weight_range": [
                0.01,
                1.0
        ],
        "default_weight": 0.1
},
        "parameter_robustness": {
        "name": "Parameter Robustness Loss",
        "formula": "L_param_robust = \u03b4||\u2202u/\u2202\u03b8||\u00b2",
        "description": "Reduces sensitivity to parameter changes",
        "weight_range": [
                0.01,
                1.0
        ],
        "default_weight": 0.1
},
        "geometry_robustness": {
        "name": "Geometry Robustness Loss",
        "formula": "L_geom_robust = \u03b6||\u2207u\u00b7n||\u00b2",
        "description": "Ensures robustness to geometric variations",
        "weight_range": [
                0.01,
                1.0
        ],
        "default_weight": 0.1
},
        "extrapolation": {
        "name": "Extrapolation Loss",
        "formula": "L_extrap = \u03ba||u(x_ext) - u_expected(x_ext)||\u00b2",
        "description": "Guides extrapolation beyond training domain",
        "weight_range": [
                0.1,
                10.0
        ],
        "default_weight": 1.0
},
        "consistency": {
        "name": "Consistency Loss",
        "formula": "L_consistency = \u03bd||u(x1) - u(x2)||\u00b2",
        "description": "Ensures consistency across similar inputs",
        "weight_range": [
                0.01,
                1.0
        ],
        "default_weight": 0.1
},
        "stability": {
        "name": "Stability Loss",
        "formula": "L_stability = \u03be||\u2202u/\u2202t||\u00b2",
        "description": "Promotes temporal stability",
        "weight_range": [
                0.01,
                1.0
        ],
        "default_weight": 0.1
},
        "invariance": {
        "name": "Invariance Loss",
        "formula": "L_invariance = \u03b7||u(T(x)) - T(u(x))||\u00b2",
        "description": "Preserves physical invariances",
        "weight_range": [
                0.01,
                1.0
        ],
        "default_weight": 0.1
}
    }
    
    # Multiphysics Research Applications
    MULTIPHYSICS_APPLICATIONS = {
        "energy_systems": {
        "name": "Energy Systems",
        "description": "Multiphysics modeling of energy generation, storage, and conversion systems",
        "equations": [
                "thermo_fluid_dynamics",
                "electro_chemical_thermal",
                "magneto_hydrodynamics",
                "thermo_chemical_mechanics"
        ],
        "challenges": [
                "Coupled thermal-electrical-chemical phenomena",
                "Multi-scale physics",
                "Efficiency optimization"
        ],
        "benefits": [
                "Improved energy conversion efficiency",
                "Better thermal management",
                "Enhanced system reliability"
        ]
},
        "biomedical_engineering": {
        "name": "Biomedical Engineering",
        "description": "Multiphysics modeling of biological systems and medical devices",
        "equations": [
                "bio_fluid_mechanics",
                "bio_electro_mechanical",
                "poro_thermo_elasticity",
                "electro_kinetics"
        ],
        "challenges": [
                "Complex biological interactions",
                "Multi-scale phenomena",
                "Patient-specific modeling"
        ],
        "benefits": [
                "Personalized medicine",
                "Improved medical device design",
                "Better treatment planning"
        ]
},
        "additive_manufacturing": {
        "name": "Additive Manufacturing",
        "description": "Multiphysics modeling of 3D printing and material processing",
        "equations": [
                "thermo_fluid_dynamics",
                "phase_field_fluid",
                "thermal_stress_flow",
                "photo_thermal_mechanics"
        ],
        "challenges": [
                "Coupled thermal-fluid-solid phenomena",
                "Phase transitions",
                "Residual stress prediction"
        ],
        "benefits": [
                "Process optimization",
                "Quality control",
                "Design for manufacturing"
        ]
},
        "micro_nano_systems": {
        "name": "Micro/Nano Systems",
        "description": "Multiphysics modeling of microfluidic and nanoelectromechanical systems",
        "equations": [
                "electro_kinetics",
                "quantum_mechanical_thermal",
                "quantum_optical_mechanical",
                "electro_optical_thermal"
        ],
        "challenges": [
                "Quantum effects at nanoscale",
                "Surface phenomena",
                "Fabrication constraints"
        ],
        "benefits": [
                "Miniaturized device design",
                "Enhanced sensitivity",
                "Novel functionality"
        ]
},
        "aerospace_engineering": {
        "name": "Aerospace Engineering",
        "description": "Multiphysics modeling of aircraft, spacecraft, and propulsion systems",
        "equations": [
                "fluid_structure_interaction",
                "thermo_fluid_dynamics",
                "magneto_hydrodynamics",
                "acoustic_elasticity"
        ],
        "challenges": [
                "High-speed flows",
                "Structural dynamics",
                "Thermal management"
        ],
        "benefits": [
                "Improved aerodynamic performance",
                "Enhanced structural integrity",
                "Better thermal protection"
        ]
},
        "material_science": {
        "name": "Material Science",
        "description": "Multiphysics modeling of advanced materials and their properties",
        "equations": [
                "magneto_thermo_elasticity",
                "electro_thermo_mechanics",
                "phase_field_fluid",
                "thermo_chemical_mechanics"
        ],
        "challenges": [
                "Multi-scale material behavior",
                "Phase transformations",
                "Property optimization"
        ],
        "benefits": [
                "Novel material design",
                "Property prediction",
                "Processing optimization"
        ]
},
        "environmental_systems": {
        "name": "Environmental Systems",
        "description": "Multiphysics modeling of environmental processes and climate systems",
        "equations": [
                "thermo_fluid_dynamics",
                "reactive_flow",
                "poro_thermo_elasticity",
                "bio_fluid_mechanics"
        ],
        "challenges": [
                "Multi-scale phenomena",
                "Complex interactions",
                "Uncertainty quantification"
        ],
        "benefits": [
                "Climate prediction",
                "Environmental protection",
                "Resource management"
        ]
},
        "quantum_technologies": {
        "name": "Quantum Technologies",
        "description": "Multiphysics modeling of quantum computing and quantum sensing systems",
        "equations": [
                "quantum_thermal",
                "quantum_mechanical_thermal",
                "quantum_optical_mechanical",
                "electro_optical_thermal"
        ],
        "challenges": [
                "Quantum coherence",
                "Decoherence mechanisms",
                "Control precision"
        ],
        "benefits": [
                "Quantum computing",
                "Quantum sensing",
                "Quantum communication"
        ]
},
        "smart_materials": {
        "name": "Smart Materials",
        "description": "Multiphysics modeling of responsive and adaptive materials",
        "equations": [
                "electro_thermo_mechanics",
                "magneto_elastic_thermal",
                "photo_thermal_mechanics",
                "bio_electro_mechanical"
        ],
        "challenges": [
                "Multi-field coupling",
                "Response optimization",
                "Reliability prediction"
        ],
        "benefits": [
                "Adaptive structures",
                "Responsive systems",
                "Intelligent materials"
        ]
},
        "fusion_energy": {
        "name": "Fusion Energy",
        "description": "Multiphysics modeling of plasma confinement and fusion reactions",
        "equations": [
                "magneto_hydrodynamics",
                "thermo_fluid_dynamics",
                "quantum_thermal",
                "electro_chemical_thermal"
        ],
        "challenges": [
                "Plasma stability",
                "Thermal management",
                "Magnetic confinement"
        ],
        "benefits": [
                "Fusion reactor design",
                "Plasma control",
                "Energy production"
        ]
}
    }

    # Multiphysics Loss Function Components
    MULTIPHYSICS_LOSS_COMPONENTS = {
        "coupled_physics": {
        "name": "Coupled Physics Loss",
        "formula": "L_coupled = \u03a3 w_ij ||R_i - R_j||\u00b2",
        "description": "Ensures consistency between coupled physical phenomena",
        "weight_range": [
                0.1,
                10.0
        ],
        "default_weight": 1.0
},
        "interface_conditions": {
        "name": "Interface Conditions Loss",
        "formula": "L_interface = \u03a3 ||[u]||\u00b2 + ||[flux]||\u00b2",
        "description": "Enforces continuity and jump conditions at interfaces",
        "weight_range": [
                0.1,
                10.0
        ],
        "default_weight": 1.0
},
        "conservation_laws": {
        "name": "Conservation Laws Loss",
        "formula": "L_conservation = \u03a3 ||\u2207\u00b7flux + source||\u00b2",
        "description": "Ensures conservation of mass, momentum, energy, charge",
        "weight_range": [
                0.1,
                10.0
        ],
        "default_weight": 1.0
},
        "cross_coupling": {
        "name": "Cross-Coupling Loss",
        "formula": "L_cross = \u03a3 ||\u2202u_i/\u2202u_j - expected||\u00b2",
        "description": "Enforces correct coupling between different fields",
        "weight_range": [
                0.01,
                1.0
        ],
        "default_weight": 0.1
},
        "scale_separation": {
        "name": "Scale Separation Loss",
        "formula": "L_scale = \u03a3 ||u_fast - u_slow||\u00b2",
        "description": "Handles multi-scale phenomena appropriately",
        "weight_range": [
                0.01,
                1.0
        ],
        "default_weight": 0.1
},
        "energy_balance": {
        "name": "Energy Balance Loss",
        "formula": "L_energy = ||\u2202E/\u2202t + \u2207\u00b7S - Q||\u00b2",
        "description": "Ensures energy conservation across all physics",
        "weight_range": [
                0.1,
                10.0
        ],
        "default_weight": 1.0
},
        "momentum_balance": {
        "name": "Momentum Balance Loss",
        "formula": "L_momentum = ||\u03c1\u2202v/\u2202t + \u2207\u00b7\u03c3 - f||\u00b2",
        "description": "Ensures momentum conservation across all physics",
        "weight_range": [
                0.1,
                10.0
        ],
        "default_weight": 1.0
},
        "charge_conservation": {
        "name": "Charge Conservation Loss",
        "formula": "L_charge = ||\u2202\u03c1_e/\u2202t + \u2207\u00b7J||\u00b2",
        "description": "Ensures charge conservation in electromagnetic systems",
        "weight_range": [
                0.1,
                10.0
        ],
        "default_weight": 1.0
},
        "phase_consistency": {
        "name": "Phase Consistency Loss",
        "formula": "L_phase = ||\u03c6 - \u03c6_expected||\u00b2",
        "description": "Ensures consistency in phase-field formulations",
        "weight_range": [
                0.01,
                1.0
        ],
        "default_weight": 0.1
},
        "boundary_coupling": {
        "name": "Boundary Coupling Loss",
        "formula": "L_boundary = \u03a3 ||u_physics1 - u_physics2||\u00b2",
        "description": "Enforces coupling conditions at domain boundaries",
        "weight_range": [
                0.1,
                10.0
        ],
        "default_weight": 1.0
},
        "temporal_coupling": {
        "name": "Temporal Coupling Loss",
        "formula": "L_temporal = \u03a3 ||\u2202u_i/\u2202t - f(u_j)||\u00b2",
        "description": "Ensures proper temporal coupling between phenomena",
        "weight_range": [
                0.01,
                1.0
        ],
        "default_weight": 0.1
},
        "spatial_coupling": {
        "name": "Spatial Coupling Loss",
        "formula": "L_spatial = \u03a3 ||\u2207u_i - g(u_j)||\u00b2",
        "description": "Ensures proper spatial coupling between phenomena",
        "weight_range": [
                0.01,
                1.0
        ],
        "default_weight": 0.1
},
        "material_properties": {
        "name": "Material Properties Loss",
        "formula": "L_material = \u03a3 ||C_ij - C_expected||\u00b2",
        "description": "Ensures consistency of material property tensors",
        "weight_range": [
                0.01,
                1.0
        ],
        "default_weight": 0.1
},
        "thermodynamic_consistency": {
        "name": "Thermodynamic Consistency Loss",
        "formula": "L_thermo = ||\u2202S/\u2202t - Q/T||\u00b2",
        "description": "Ensures thermodynamic consistency",
        "weight_range": [
                0.01,
                1.0
        ],
        "default_weight": 0.1
},
        "quantum_consistency": {
        "name": "Quantum Consistency Loss",
        "formula": "L_quantum = ||[H,\u03c1] - i\u210f\u2202\u03c1/\u2202t||\u00b2",
        "description": "Ensures quantum mechanical consistency",
        "weight_range": [
                0.01,
                1.0
        ],
        "default_weight": 0.1
}
    }
    
    # Efficiency Research Applications
    EFFICIENCY_APPLICATIONS = {
        "adaptive_sampling": {
        "name": "Adaptive Sampling Strategies",
        "description": "Dynamically adjust sampling points based on solution gradients and residuals",
        "equations": [
                "adaptive_sampling_burgers",
                "adaptive_wave",
                "adaptive_navier_stokes",
                "adaptive_schrodinger",
                "adaptive_elasticity",
                "adaptive_phase_field",
                "adaptive_viscoelastic",
                "adaptive_magnetohydrodynamics",
                "adaptive_fluid_structure",
                "adaptive_photo_thermal",
                "adaptive_combustion"
        ],
        "challenges": [
                "Optimal sampling distribution",
                "Computational overhead",
                "Convergence guarantees"
        ],
        "benefits": [
                "Reduced computational cost",
                "Improved accuracy",
                "Faster convergence"
        ]
},
        "multiscale_methods": {
        "name": "Multiscale Resolution Techniques",
        "description": "Use different resolutions for different regions based on solution complexity",
        "equations": [
                "multiscale_heat",
                "adaptive_navier_stokes",
                "adaptive_elasticity",
                "adaptive_phase_field",
                "adaptive_magnetohydrodynamics",
                "adaptive_fluid_structure"
        ],
        "challenges": [
                "Scale coupling",
                "Interface handling",
                "Consistency maintenance"
        ],
        "benefits": [
                "Computational efficiency",
                "Captures fine-scale features",
                "Reduces memory requirements"
        ]
},
        "fast_solvers": {
        "name": "Fast Numerical Solvers",
        "description": "Implement specialized solvers for specific equation types",
        "equations": [
                "fast_fourier_poisson",
                "sparse_laplace",
                "fast_reaction_diffusion",
                "fast_maxwell",
                "fast_porous_flow",
                "fast_kinetic",
                "fast_thermoelastic",
                "fast_electrokinetics",
                "fast_quantum_thermal",
                "fast_bio_fluid",
                "fast_multiphase"
        ],
        "challenges": [
                "Solver development",
                "Numerical stability",
                "Accuracy preservation"
        ],
        "benefits": [
                "Significant speedup",
                "Reduced computational cost",
                "Scalable algorithms"
        ]
},
        "parallel_computing": {
        "name": "Parallel Computing Strategies",
        "description": "Leverage parallel architectures for distributed PINN training",
        "equations": [
                "all_efficiency_equations"
        ],
        "challenges": [
                "Load balancing",
                "Communication overhead",
                "Scalability limits"
        ],
        "benefits": [
                "Linear speedup",
                "Large-scale problems",
                "Real-time applications"
        ]
},
        "model_compression": {
        "name": "Model Compression and Pruning",
        "description": "Reduce model complexity while maintaining accuracy",
        "equations": [
                "all_efficiency_equations"
        ],
        "challenges": [
                "Accuracy preservation",
                "Compression ratio",
                "Retraining strategies"
        ],
        "benefits": [
                "Reduced memory usage",
                "Faster inference",
                "Deployment efficiency"
        ]
},
        "transfer_learning": {
        "name": "Transfer Learning for Efficiency",
        "description": "Reuse pre-trained models for related problems",
        "equations": [
                "all_efficiency_equations"
        ],
        "challenges": [
                "Domain adaptation",
                "Knowledge transfer",
                "Catastrophic forgetting"
        ],
        "benefits": [
                "Reduced training time",
                "Better initialization",
                "Improved convergence"
        ]
},
        "quantization": {
        "name": "Quantization and Low-Precision",
        "description": "Use reduced precision for faster computation",
        "equations": [
                "all_efficiency_equations"
        ],
        "challenges": [
                "Numerical stability",
                "Accuracy degradation",
                "Hardware compatibility"
        ],
        "benefits": [
                "Memory reduction",
                "Speedup on specialized hardware",
                "Energy efficiency"
        ]
},
        "sparse_networks": {
        "name": "Sparse Neural Networks",
        "description": "Use sparse connectivity for computational efficiency",
        "equations": [
                "sparse_laplace",
                "adaptive_phase_field",
                "fast_kinetic",
                "adaptive_combustion"
        ],
        "challenges": [
                "Sparsity pattern design",
                "Training dynamics",
                "Expressiveness limits"
        ],
        "benefits": [
                "Reduced parameters",
                "Faster training",
                "Better generalization"
        ]
},
        "hardware_acceleration": {
        "name": "Hardware Acceleration",
        "description": "Optimize for specific hardware architectures",
        "equations": [
                "all_efficiency_equations"
        ],
        "challenges": [
                "Hardware-specific optimization",
                "Portability",
                "Cost considerations"
        ],
        "benefits": [
                "Significant speedup",
                "Energy efficiency",
                "Real-time performance"
        ]
},
        "algorithmic_optimization": {
        "name": "Algorithmic Optimizations",
        "description": "Optimize training algorithms and loss functions",
        "equations": [
                "all_efficiency_equations"
        ],
        "challenges": [
                "Algorithm design",
                "Convergence analysis",
                "Implementation complexity"
        ],
        "benefits": [
                "Faster convergence",
                "Better optimization",
                "Improved stability"
        ]
}
    }

    # Efficiency Loss Function Components
    EFFICIENCY_LOSS_COMPONENTS = {
        "computational_efficiency": {
        "name": "Computational Efficiency Loss",
        "formula": "L_comp = \u03bb_comp ||\u2207u||_L1",
        "description": "Promotes sparse gradients for computational efficiency",
        "weight_range": [
                0.001,
                0.1
        ],
        "default_weight": 0.01
},
        "memory_efficiency": {
        "name": "Memory Efficiency Loss",
        "formula": "L_mem = \u03bb_mem ||W||_L1",
        "description": "Promotes sparse weights for memory efficiency",
        "weight_range": [
                0.001,
                0.1
        ],
        "default_weight": 0.01
},
        "adaptive_sampling": {
        "name": "Adaptive Sampling Loss",
        "formula": "L_adapt = \u03bb_adapt \u03a3 w_i |r_i|",
        "description": "Weighted sampling based on residual magnitude",
        "weight_range": [
                0.1,
                10.0
        ],
        "default_weight": 1.0
},
        "multiscale_consistency": {
        "name": "Multiscale Consistency Loss",
        "formula": "L_ms = \u03bb_ms ||u_fine - u_coarse||\u00b2",
        "description": "Ensures consistency across different scales",
        "weight_range": [
                0.1,
                10.0
        ],
        "default_weight": 1.0
},
        "parallel_efficiency": {
        "name": "Parallel Efficiency Loss",
        "formula": "L_par = \u03bb_par ||u_domain1 - u_domain2||\u00b2",
        "description": "Ensures consistency across parallel domains",
        "weight_range": [
                0.1,
                10.0
        ],
        "default_weight": 1.0
},
        "transfer_efficiency": {
        "name": "Transfer Efficiency Loss",
        "formula": "L_transfer = \u03bb_transfer ||u_new - u_pretrained||\u00b2",
        "description": "Encourages similarity to pre-trained solutions",
        "weight_range": [
                0.1,
                10.0
        ],
        "default_weight": 1.0
},
        "quantization_robustness": {
        "name": "Quantization Robustness Loss",
        "formula": "L_quant = \u03bb_quant ||u_fp32 - u_fp16||\u00b2",
        "description": "Ensures robustness to quantization",
        "weight_range": [
                0.01,
                1.0
        ],
        "default_weight": 0.1
},
        "sparse_regularization": {
        "name": "Sparse Regularization Loss",
        "formula": "L_sparse = \u03bb_sparse ||W||_L0",
        "description": "Promotes exact sparsity in network weights",
        "weight_range": [
                0.001,
                0.1
        ],
        "default_weight": 0.01
},
        "hardware_optimization": {
        "name": "Hardware Optimization Loss",
        "formula": "L_hw = \u03bb_hw ||u_gpu - u_cpu||\u00b2",
        "description": "Ensures consistency across hardware platforms",
        "weight_range": [
                0.01,
                1.0
        ],
        "default_weight": 0.1
},
        "algorithmic_stability": {
        "name": "Algorithmic Stability Loss",
        "formula": "L_stab = \u03bb_stab ||\u2202u/\u2202\u03b8||\u00b2",
        "description": "Promotes stable training dynamics",
        "weight_range": [
                0.01,
                1.0
        ],
        "default_weight": 0.1
},
        "convergence_acceleration": {
        "name": "Convergence Acceleration Loss",
        "formula": "L_conv = \u03bb_conv ||\u2207L||\u00b2",
        "description": "Accelerates convergence by gradient smoothing",
        "weight_range": [
                0.001,
                0.1
        ],
        "default_weight": 0.01
},
        "energy_efficiency": {
        "name": "Energy Efficiency Loss",
        "formula": "L_energy = \u03bb_energy ||u||\u00b2",
        "description": "Minimizes energy consumption in solutions",
        "weight_range": [
                0.001,
                0.1
        ],
        "default_weight": 0.01
},
        "real_time_constraint": {
        "name": "Real-Time Constraint Loss",
        "formula": "L_rt = \u03bb_rt ||\u2202u/\u2202t||\u00b2",
        "description": "Ensures real-time computational capability",
        "weight_range": [
                0.1,
                10.0
        ],
        "default_weight": 1.0
},
        "scalability_loss": {
        "name": "Scalability Loss",
        "formula": "L_scale = \u03bb_scale ||u_N - u_2N||\u00b2",
        "description": "Ensures solution scalability with problem size",
        "weight_range": [
                0.1,
                10.0
        ],
        "default_weight": 1.0
},
        "robustness_efficiency": {
        "name": "Robustness Efficiency Loss",
        "formula": "L_rob_eff = \u03bb_rob_eff ||u_perturbed - u_original||\u00b2",
        "description": "Ensures efficiency under perturbations",
        "weight_range": [
                0.01,
                1.0
        ],
        "default_weight": 0.1
}
    }
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