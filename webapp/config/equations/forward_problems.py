"""
Forward Problems Equations
Equations for solving forward problems with known parameters and initial/boundary conditions.
"""

FORWARD_PROBLEMS_EQUATIONS_DICT = {
    'burgers': {
        'name': 'Burgers Equation',
        'description': 'Nonlinear partial differential equation for fluid dynamics',
        'icon': 'fas fa-water',
        'color': '#3498db',
        'formula': '∂u/∂t + u∂u/∂x = ν∂²u/∂x²',
        'applications': ['Shock waves', 'Traffic flow', 'Fluid dynamics']
    },
    'heat': {
        'name': 'Heat Equation',
        'description': 'Parabolic partial differential equation for heat conduction',
        'icon': 'fas fa-fire',
        'color': '#e74c3c',
        'formula': '∂u/∂t = α∂²u/∂x²',
        'applications': ['Heat transfer', 'Diffusion', 'Thermal analysis']
    },
    'wave': {
        'name': 'Wave Equation',
        'description': 'Hyperbolic partial differential equation for wave propagation',
        'icon': 'fas fa-wave-square',
        'color': '#9b59b6',
        'formula': '∂²u/∂t² = c²∂²u/∂x²',
        'applications': ['Acoustics', 'Seismology', 'Electromagnetic waves']
    },
    'shm': {
        'name': 'Simple Harmonic Motion',
        'description': 'Second-order differential equation for oscillatory motion',
        'icon': 'fas fa-sync',
        'color': '#f39c12',
        'formula': 'd²x/dt² + ω²x = 0',
        'applications': ['Pendulum motion', 'Spring-mass systems', 'Vibrations']
    },
    'helmholtz': {
        'name': 'Helmholtz Equation',
        'description': 'Elliptic partial differential equation for steady-state waves',
        'icon': 'fas fa-broadcast-tower',
        'color': '#1abc9c',
        'formula': '∇²u + k²u = 0',
        'applications': ['Acoustic scattering', 'Electromagnetic waves', 'Quantum mechanics']
    },
    'navier_stokes': {
        'name': 'Navier-Stokes Equations',
        'description': 'System of partial differential equations for fluid flow',
        'icon': 'fas fa-wind',
        'color': '#34495e',
        'formula': 'ρ(∂v/∂t + v·∇v) = -∇p + μ∇²v + f',
        'applications': ['Aerodynamics', 'Oceanography', 'Meteorology']
    },
    'schrodinger': {
        'name': 'Schrödinger Equation',
        'description': 'Partial differential equation for quantum mechanics',
        'icon': 'fas fa-atom',
        'color': '#e67e22',
        'formula': 'iℏ∂ψ/∂t = Ĥψ',
        'applications': ['Quantum mechanics', 'Molecular dynamics', 'Quantum chemistry']
    },
    'maxwell': {
        'name': 'Maxwell Equations',
        'description': 'Complete system of Maxwell equations for electromagnetism',
        'icon': 'fas fa-bolt',
        'color': '#f1c40f',
        'formula': '∇·E = ρ/ε₀, ∇×E = -∂B/∂t, ∇·B = 0, ∇×B = μ₀J + μ₀ε₀∂E/∂t',
        'variables': ['E', 'B', 'ρ', 'J', 'ε₀', 'μ₀'],
        'category': 'electromagnetism',
        'difficulty': 'intermediate',
        'applications': ['Electromagnetism', 'Optics', 'Antenna design', 'Wave propagation']
    },
    'heat_transfer': {
        'name': 'Heat Transfer Equation',
        'description': 'Generalized heat equation with convection and radiation',
        'icon': 'fas fa-thermometer-half',
        'color': '#e74c3c',
        'formula': 'ρc_p ∂T/∂t = ∇·(k∇T) + Q',
        'applications': ['Thermal engineering', 'Climate modeling', 'Material processing']
    },
    'elastic': {
        'name': 'Elasticity Equations',
        'description': 'System of equations for elastic deformation',
        'icon': 'fas fa-compress-arrows-alt',
        'color': '#95a5a6',
        'formula': '∇·σ = 0, σ = C:ε',
        'applications': ['Structural mechanics', 'Geomechanics', 'Biomechanics']
    },
    'phase_field': {
        'name': 'Phase Field Equation',
        'description': 'Nonlinear partial differential equation for phase transitions',
        'icon': 'fas fa-snowflake',
        'color': '#3498db',
        'formula': '∂φ/∂t = -M δF/δφ',
        'formula_latex': r'$\frac{\partial \phi}{\partial t} = -M \frac{\delta F}{\delta \phi}$',
        'applications': ['Phase transitions', 'Crystal growth', 'Material science']
    },
    'reaction_diffusion': {
        'name': 'Reaction-Diffusion Equation',
        'description': 'Nonlinear partial differential equation for chemical reactions',
        'icon': 'fas fa-flask',
        'color': '#9b59b6',
        'formula': '∂u/∂t = D∇²u + f(u)',
        'applications': ['Chemical kinetics', 'Pattern formation', 'Biological systems']
    },
    'poroelasticity': {
        'name': 'Poroelasticity Equations',
        'description': 'Coupled equations for fluid flow in porous media',
        'icon': 'fas fa-tint',
        'color': '#1abc9c',
        'formula': '∇·σ = 0, ∂p/∂t = κ∇²p',
        'applications': ['Geomechanics', 'Hydrology', 'Petroleum engineering']
    },
    'viscoelasticity': {
        'name': 'Viscoelasticity Equation',
        'description': 'Constitutive equation for viscoelastic materials',
        'icon': 'fas fa-clock',
        'color': '#f39c12',
        'formula': 'σ + τ∂σ/∂t = E(ε + τ∂ε/∂t)',
        'applications': ['Polymer mechanics', 'Biological tissues', 'Rheology']
    },
    'radiative_transfer': {
        'name': 'Radiative Transfer Equation',
        'description': 'Integro-differential equation for radiation transport',
        'icon': 'fas fa-sun',
        'color': '#f1c40f',
        'formula': '∂I/∂s + (κ + σ)I = σ/4π ∫I dΩ',
        'applications': ['Atmospheric radiation', 'Astrophysics', 'Remote sensing']
    },
    'shallow_water': {
        'name': 'Shallow Water Equations',
        'description': 'System of equations for shallow water flow',
        'icon': 'fas fa-water',
        'color': '#3498db',
        'formula': '∂h/∂t + ∇·(hv) = 0',
        'applications': ['Oceanography', 'Hydrology', 'Tsunami modeling']
    },
    'magnetohydrodynamics': {
        'name': 'Magnetohydrodynamics',
        'description': 'Coupled equations for plasma dynamics',
        'icon': 'fas fa-magnet',
        'color': '#e74c3c',
        'formula': 'Navier-Stokes + Maxwell',
        'applications': ['Fusion plasma', 'Astrophysics', 'Space physics']
    },
    'thermoelasticity': {
        'name': 'Thermoelasticity',
        'description': 'Coupled heat and elasticity equations',
        'icon': 'fas fa-fire',
        'color': '#e67e22',
        'formula': 'Heat equation + Elasticity',
        'applications': ['Thermal stress', 'Material processing', 'Structural analysis']
    },
    'advection_diffusion': {
        'name': 'Advection-Diffusion',
        'description': 'Transport equation with advection and diffusion',
        'icon': 'fas fa-route',
        'color': '#9b59b6',
        'formula': '∂c/∂t + v·∇c = D∇²c',
        'applications': ['Pollutant transport', 'Ocean circulation', 'Atmospheric dispersion']
    },
    'elastic_wave': {
        'name': 'Elastic Wave Equation',
        'description': 'Wave equation for elastic media',
        'icon': 'fas fa-wave-square',
        'color': '#34495e',
        'formula': 'ρ∂²u/∂t² = ∇·σ',
        'applications': ['Seismology', 'Ultrasound', 'Non-destructive testing']
    },
    'fluid_structure_interaction': {
        'name': 'Fluid-Structure Interaction',
        'description': 'Coupled fluid and structural dynamics',
        'icon': 'fas fa-link',
        'color': '#1abc9c',
        'formula': 'Navier-Stokes + Elasticity',
        'applications': ['Aeroelasticity', 'Biomechanics', 'Offshore structures']
    },
    'electromagnetic_thermal': {
        'name': 'Electromagnetic-Thermal',
        'description': 'Coupled electromagnetic and thermal effects',
        'icon': 'fas fa-bolt',
        'color': '#f1c40f',
        'formula': 'Maxwell + Heat equation',
        'applications': ['Electromagnetic heating', 'Microwave processing', 'Induction heating']
    },
    'biomechanical_transport': {
        'name': 'Biomechanical Transport',
        'description': 'Coupled mechanics and transport in biological systems',
        'icon': 'fas fa-heartbeat',
        'color': '#e74c3c',
        'formula': 'Elasticity + Diffusion',
        'applications': ['Tissue engineering', 'Drug delivery', 'Biomechanics']
    },
    'geophysical_flow': {
        'name': 'Geophysical Flow',
        'description': 'Large-scale geophysical fluid dynamics',
        'icon': 'fas fa-globe',
        'color': '#3498db',
        'formula': 'Shallow water + Coriolis',
        'applications': ['Ocean circulation', 'Atmospheric dynamics', 'Climate modeling']
    },
    'atmospheric_oceanic': {
        'name': 'Atmospheric-Oceanic',
        'description': 'Coupled atmospheric and oceanic dynamics',
        'icon': 'fas fa-cloud',
        'color': '#95a5a6',
        'formula': 'Atmospheric + Oceanic equations',
        'applications': ['Climate modeling', 'Weather prediction', 'Earth system science']
    },
    'nuclear_thermal': {
        'name': 'Nuclear Thermal',
        'description': 'Coupled nuclear reactions and heat transfer',
        'icon': 'fas fa-radiation',
        'color': '#e67e22',
        'formula': 'Heat equation + Nuclear source',
        'applications': ['Nuclear reactors', 'Fusion devices', 'Nuclear safety']
    },
    'quantum_mechanical': {
        'name': 'Quantum Mechanical',
        'description': 'Quantum mechanical systems and dynamics',
        'icon': 'fas fa-atom',
        'color': '#9b59b6',
        'formula': 'Schrödinger equation',
        'applications': ['Quantum chemistry', 'Molecular dynamics', 'Quantum computing']
    },
    'phase_field_allen_cahn': {
        'name': 'Allen-Cahn Phase Field',
        'description': 'Phase field equation for non-conserved order parameter evolution',
        'icon': 'fas fa-cube',
        'color': '#3498db',
        'formula': '∂φ/∂t = -M δF/δφ',
        'applications': ['Microstructure evolution', 'Phase separation', 'Material science']
    },
    'phase_field_cahn_hilliard': {
        'name': 'Cahn-Hilliard Phase Field',
        'description': 'Phase field equation for conserved order parameter evolution',
        'icon': 'fas fa-cube',
        'color': '#3498db',
        'formula': '∂φ/∂t = ∇·(M∇(δF/δφ))',
        'applications': ['Spinodal decomposition', 'Microstructure evolution', 'Material science']
    },
    'solidification_stefan': {
        'name': 'Stefan Problem (Solidification)',
        'description': 'Phase change problem with moving boundary',
        'icon': 'fas fa-icicles',
        'color': '#3498db',
        'formula': '∂T/∂t = α∇²T, with moving boundary',
        'applications': ['Solidification', 'Melting', 'Additive manufacturing']
    },
    'grain_growth': {
        'name': 'Grain Growth',
        'description': 'Curvature-driven grain growth in polycrystalline materials',
        'icon': 'fas fa-th-large',
        'color': '#3498db',
        'formula': '∂R/∂t = Mγ/R',
        'applications': ['Grain growth', 'Material science', 'Metallurgy']
    },
    'sintering': {
        'name': 'Sintering',
        'description': 'Densification process in powder materials',
        'icon': 'fas fa-dot-circle',
        'color': '#3498db',
        'formula': '∂ρ/∂t = D∇²ρ',
        'applications': ['Sintering', 'Powder metallurgy', 'Ceramics']
    },
    'laser_heat_source': {
        'name': 'Laser Heat Source',
        'description': 'Gaussian laser heat source for additive manufacturing',
        'icon': 'fas fa-burn',
        'color': '#3498db',
        'formula': 'Q(x, y, z, t) = Q₀ exp(-((x-x₀)²+(y-y₀)²)/2σ²)',
        'applications': ['Additive manufacturing', 'Laser processing', 'Thermal modeling']
    },
    'melt_pool_dynamics': {
        'name': 'Melt Pool Dynamics',
        'description': 'Fluid dynamics of molten metal pool in AM',
        'icon': 'fas fa-water',
        'color': '#3498db',
        'formula': 'Navier-Stokes + Surface tension + Marangoni',
        'applications': ['Additive manufacturing', 'Welding', 'Laser processing']
    },
    'powder_spreading': {
        'name': 'Powder Spreading',
        'description': 'Powder bed spreading and packing in AM',
        'icon': 'fas fa-layer-group',
        'color': '#3498db',
        'formula': 'Granular flow + Packing density',
        'applications': ['Additive manufacturing', 'Powder metallurgy', 'Granular materials']
    },
    'crystal_plasticity': {
        'name': 'Crystal Plasticity',
        'description': 'Dislocation-based plasticity in crystalline materials',
        'icon': 'fas fa-crystal-ball',
        'color': '#3498db',
        'formula': 'τ = τ₀ + αμb√ρ',
        'applications': ['Metal forming', 'Material science', 'Mechanical behavior']
    },
    'diffusion_solids': {
        'name': 'Diffusion in Solids',
        'description': 'Multi-component diffusion in solid materials',
        'icon': 'fas fa-arrows-alt',
        'color': '#3498db',
        'formula': '∂c/∂t = ∇·(D∇c)',
        'applications': ['Heat treatment', 'Alloying', 'Material processing']
    },
    'precipitation_nucleation': {
        'name': 'Precipitation and Nucleation',
        'description': 'Classical nucleation theory and precipitation kinetics',
        'icon': 'fas fa-seedling',
        'color': '#3498db',
        'formula': 'J = J₀ exp(-ΔG*/kT)',
        'applications': ['Age hardening', 'Phase transformations', 'Material science']
    },
    'porosity_evolution': {
        'name': 'Porosity Evolution',
        'description': 'Evolution of porosity in materials during processing',
        'icon': 'fas fa-circle-notch',
        'color': '#3498db',
        'formula': '∂φ/∂t = -∇·(vφ) + S',
        'applications': ['Additive manufacturing', 'Casting', 'Material processing']
    },
    'residual_stress': {
        'name': 'Residual Stress',
        'description': 'Thermal and mechanical residual stress development',
        'icon': 'fas fa-compress-arrows-alt',
        'color': '#3498db',
        'formula': '∇·σ = 0, σ = C:(ε - εᵗ)',
        'applications': ['Additive manufacturing', 'Welding', 'Material processing']
    },
    'microstructure_evolution': {
        'name': 'Microstructure Evolution',
        'description': 'Multi-phase microstructure evolution in materials',
        'icon': 'fas fa-microscope',
        'color': '#3498db',
        'formula': 'Multiple phase field equations',
        'applications': ['Material science', 'Phase transformations', 'Microstructure design']
    },
    'electromagnetic_wave': {
        'name': 'Electromagnetic Wave Equation',
        'description': 'Wave equation for electromagnetic fields in vacuum',
        'icon': 'fas fa-wave-square',
        'color': '#9b59b6',
        'formula': '∇²E - (1/c²)∂²E/∂t² = 0, ∇²B - (1/c²)∂²B/∂t² = 0',
        'variables': ['E', 'B', 'c'],
        'category': 'electromagnetism',
        'difficulty': 'intermediate',
        'applications': ['Optics', 'Radio waves', 'Light propagation', 'Waveguides']
    },
    'helmholtz_equation': {
        'name': 'Helmholtz Equation',
        'description': 'Time-harmonic wave equation for electromagnetic fields',
        'icon': 'fas fa-sync',
        'color': '#3498db',
        'formula': '∇²E + k²E = 0, where k = ω/c',
        'variables': ['E', 'k', 'ω', 'c'],
        'category': 'electromagnetism',
        'difficulty': 'intermediate',
        'applications': ['Frequency domain EM', 'Antenna analysis', 'Scattering problems']
    },
    'poisson_equation': {
        'name': 'Poisson Equation',
        'description': 'Electrostatic potential equation',
        'icon': 'fas fa-charging-station',
        'color': '#e74c3c',
        'formula': '∇²φ = -ρ/ε₀',
        'variables': ['φ', 'ρ', 'ε₀'],
        'category': 'electromagnetism',
        'difficulty': 'basic',
        'applications': ['Electrostatics', 'Capacitor design', 'Electric field calculation']
    },
    'vector_potential': {
        'name': 'Vector Potential Equation',
        'description': 'Magnetic vector potential formulation',
        'icon': 'fas fa-magnet',
        'color': '#2c3e50',
        'formula': '∇²A - μ₀ε₀∂²A/∂t² = -μ₀J',
        'variables': ['A', 'J', 'μ₀', 'ε₀'],
        'category': 'electromagnetism',
        'difficulty': 'advanced',
        'applications': ['Magnetostatics', 'Induction problems', 'Magnetic field calculation']
    },
    'telegraph_equation': {
        'name': 'Telegraph Equation',
        'description': 'Transmission line equation for electromagnetic waves',
        'icon': 'fas fa-broadcast-tower',
        'color': '#f39c12',
        'formula': '∂²V/∂x² = LC∂²V/∂t² + (RC+GL)∂V/∂t + RGV',
        'variables': ['V', 'L', 'C', 'R', 'G'],
        'category': 'electromagnetism',
        'difficulty': 'intermediate',
        'applications': ['Transmission lines', 'Cable analysis', 'Signal propagation']
    },
    'scalar_wave': {
        'name': 'Scalar Wave Equation',
        'description': 'Simplified wave equation for scalar electromagnetic fields',
        'icon': 'fas fa-wave-square',
        'color': '#1abc9c',
        'formula': '∇²ψ - (1/c²)∂²ψ/∂t² = 0',
        'variables': ['ψ', 'c'],
        'category': 'electromagnetism',
        'difficulty': 'basic',
        'applications': ['Acoustic waves', 'Scalar EM approximation', 'Wave propagation']
    }
} 