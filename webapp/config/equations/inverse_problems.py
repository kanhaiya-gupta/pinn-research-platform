"""
Inverse Problems Equations
Equations for solving inverse problems with unknown parameters to be identified.
"""

INVERSE_PROBLEMS_EQUATIONS_DICT = {
    'inverse_burgers': {
        'name': 'Inverse Burgers',
        'description': 'Identify viscosity and initial conditions from observations',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': '∂u/∂t + u∂u/∂x = ν∂²u/∂x² (ν unknown)',
        'applications': ['Flow parameter identification', 'Shock wave analysis', 'Traffic flow modeling']
    },
    'inverse_heat': {
        'name': 'Inverse Heat',
        'description': 'Identify thermal diffusivity and boundary conditions',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': '∂u/∂t = α∂²u/∂x² (α unknown)',
        'applications': ['Thermal property identification', 'Heat source localization', 'Material characterization']
    },
    'inverse_wave': {
        'name': 'Inverse Wave',
        'description': 'Identify wave speed and initial conditions',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': '∂²u/∂t² = c²∂²u/∂x² (c unknown)',
        'applications': ['Medium property identification', 'Seismic inversion', 'Acoustic tomography']
    },
    'inverse_shm': {
        'name': 'Inverse SHM',
        'description': 'Identify natural frequency and damping parameters',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': 'd²x/dt² + 2ζωdx/dt + ω²x = 0 (ω, ζ unknown)',
        'applications': ['System identification', 'Vibration analysis', 'Structural health monitoring']
    },
    'inverse_helmholtz': {
        'name': 'Inverse Helmholtz',
        'description': 'Identify medium properties from frequency domain measurements',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': '∇²E + k²E = 0 (k, medium properties unknown)',
        'variables': ['E', 'k', 'ε', 'μ'],
        'category': 'electromagnetism',
        'difficulty': 'intermediate',
        'applications': ['Frequency domain EM tomography', 'Antenna parameter identification', 'Scattering problem inversion']
    },
    'inverse_navier_stokes': {
        'name': 'Inverse Navier-Stokes',
        'description': 'Identify viscosity and boundary conditions',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': 'ρ(∂v/∂t + v·∇v) = -∇p + μ∇²v + f (μ unknown)',
        'applications': ['Flow property identification', 'Turbulence modeling', 'Fluid parameter estimation']
    },
    'inverse_schrodinger': {
        'name': 'Inverse Schrödinger',
        'description': 'Identify potential and wave function',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': 'iℏ∂ψ/∂t = Ĥψ (V unknown)',
        'applications': ['Potential reconstruction', 'Quantum state tomography', 'Molecular structure determination']
    },
    'inverse_maxwell': {
        'name': 'Inverse Maxwell',
        'description': 'Identify electromagnetic properties from field measurements',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': '∇·E = ρ/ε₀, ∇×E = -∂B/∂t (ε, μ, σ unknown)',
        'variables': ['E', 'B', 'ε', 'μ', 'σ'],
        'category': 'electromagnetism',
        'difficulty': 'advanced',
        'applications': ['Electromagnetic property identification', 'Antenna design', 'Material characterization', 'EM tomography']
    },
    'inverse_heat_transfer': {
        'name': 'Inverse Heat Transfer',
        'description': 'Identify thermal conductivity and heat sources',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': 'ρc_p ∂T/∂t = ∇·(k∇T) + Q (k, Q unknown)',
        'applications': ['Thermal property identification', 'Heat source localization', 'Thermal imaging']
    },
    'inverse_elastic': {
        'name': 'Inverse Elastic',
        'description': 'Identify elastic moduli and boundary conditions',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': '∇·σ = 0, σ = C:ε (C unknown)',
        'applications': ['Elastic modulus identification', 'Stress field reconstruction', 'Material property estimation']
    },
    'inverse_phase_field': {
        'name': 'Inverse Phase Field',
        'description': 'Identify phase field parameters and free energy',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': '∂φ/∂t = -M δF/δφ (M, F unknown)',
        'applications': ['Phase field parameter identification', 'Free energy reconstruction', 'Microstructure evolution']
    },
    'inverse_reaction_diffusion': {
        'name': 'Inverse Reaction-Diffusion',
        'description': 'Identify diffusion coefficient and reaction rates',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': '∂u/∂t = D∇²u + f(u) (D, f unknown)',
        'applications': ['Chemical parameter identification', 'Reaction mechanism determination', 'Diffusion coefficient estimation']
    },
    'inverse_poroelasticity': {
        'name': 'Inverse Poroelasticity',
        'description': 'Identify permeability and elastic moduli',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': '∇·σ = 0, ∂p/∂t = κ∇²p (κ, C unknown)',
        'applications': ['Permeability identification', 'Poroelastic parameter estimation', 'Reservoir characterization']
    },
    'inverse_viscoelasticity': {
        'name': 'Inverse Viscoelasticity',
        'description': 'Identify viscoelastic parameters and relaxation times',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': 'σ + τ∂σ/∂t = E(ε + τ∂ε/∂t) (E, τ unknown)',
        'applications': ['Viscoelastic parameter identification', 'Relaxation time estimation', 'Polymer characterization']
    },
    'inverse_radiative_transfer': {
        'name': 'Inverse Radiative Transfer',
        'description': 'Identify absorption and scattering coefficients',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': '∂I/∂s + (κ + σ)I = σ/4π ∫I dΩ (κ, σ unknown)',
        'applications': ['Atmospheric property identification', 'Remote sensing', 'Optical property estimation']
    },
    'inverse_shallow_water': {
        'name': 'Inverse Shallow Water',
        'description': 'Identify bottom topography and friction coefficients',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': '∂h/∂t + ∇·(hv) = 0 (bathymetry, friction unknown)',
        'applications': ['Bathymetry reconstruction', 'Friction coefficient identification', 'Tsunami source estimation']
    },
    'inverse_magnetohydrodynamics': {
        'name': 'Inverse Magnetohydrodynamics',
        'description': 'Identify plasma parameters and magnetic field',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': 'Navier-Stokes + Maxwell (plasma parameters unknown)',
        'applications': ['Plasma parameter identification', 'Magnetic field reconstruction', 'Fusion plasma diagnostics']
    },
    'inverse_thermoelasticity': {
        'name': 'Inverse Thermoelasticity',
        'description': 'Identify thermal and elastic parameters',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': 'Heat equation + Elasticity (coupled parameters unknown)',
        'applications': ['Thermoelastic parameter identification', 'Thermal stress estimation', 'Material characterization']
    },
    'inverse_advection_diffusion': {
        'name': 'Inverse Advection-Diffusion',
        'description': 'Identify velocity field and diffusion coefficient',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': '∂c/∂t + v·∇c = D∇²c (v, D unknown)',
        'applications': ['Velocity field reconstruction', 'Diffusion coefficient identification', 'Transport parameter estimation']
    },
    'inverse_elastic_wave': {
        'name': 'Inverse Elastic Wave',
        'description': 'Identify elastic moduli and wave speeds',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': 'ρ∂²u/∂t² = ∇·σ (elastic moduli unknown)',
        'applications': ['Elastic modulus identification', 'Seismic tomography', 'Wave speed estimation']
    },
    'inverse_fluid_structure_interaction': {
        'name': 'Inverse Fluid-Structure Interaction',
        'description': 'Identify fluid and structural parameters',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': 'Navier-Stokes + Elasticity (coupled parameters unknown)',
        'applications': ['FSI parameter identification', 'Coupled system characterization', 'Aeroelastic parameter estimation']
    },
    'inverse_electromagnetic_thermal': {
        'name': 'Inverse Electromagnetic-Thermal',
        'description': 'Identify electromagnetic and thermal parameters',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': 'Maxwell + Heat equation (coupled parameters unknown)',
        'applications': ['EM-thermal parameter identification', 'Electromagnetic property estimation', 'Thermal property identification']
    },
    'inverse_biomechanical_transport': {
        'name': 'Inverse Biomechanical Transport',
        'description': 'Identify mechanical and transport parameters',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': 'Elasticity + Diffusion (biological parameters unknown)',
        'applications': ['Tissue property identification', 'Biological parameter estimation', 'Biomechanical characterization']
    },
    'inverse_geophysical_flow': {
        'name': 'Inverse Geophysical Flow',
        'description': 'Identify geophysical parameters and forcing',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': 'Shallow water + Coriolis (geophysical parameters unknown)',
        'applications': ['Ocean parameter identification', 'Atmospheric parameter estimation', 'Geophysical field reconstruction']
    },
    'inverse_atmospheric_oceanic': {
        'name': 'Inverse Atmospheric-Oceanic',
        'description': 'Identify coupled atmospheric-oceanic parameters',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': 'Atmospheric + Oceanic equations (coupled parameters unknown)',
        'applications': ['Climate parameter identification', 'Coupled system characterization', 'Earth system parameter estimation']
    },
    'inverse_nuclear_thermal': {
        'name': 'Inverse Nuclear Thermal',
        'description': 'Identify nuclear and thermal parameters',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': 'Heat equation + Nuclear source (nuclear parameters unknown)',
        'applications': ['Nuclear parameter identification', 'Reactor characterization', 'Nuclear safety assessment']
    },
    'inverse_quantum_mechanical': {
        'name': 'Inverse Quantum Mechanical',
        'description': 'Identify quantum mechanical parameters and states',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': 'Schrödinger equation (quantum parameters unknown)',
        'applications': ['Quantum parameter identification', 'Wave function reconstruction', 'Quantum state tomography']
    },
    'inverse_phase_field_allen_cahn': {
        'name': 'Inverse Allen-Cahn Phase Field',
        'description': 'Identify phase field parameters and free energy from microstructure data',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': '∂φ/∂t = -M δF/δφ (M, F unknown)',
        'applications': ['Phase field parameter identification', 'Free energy reconstruction', 'Microstructure evolution']
    },
    'inverse_phase_field_cahn_hilliard': {
        'name': 'Inverse Cahn-Hilliard Phase Field',
        'description': 'Identify conserved phase field parameters from concentration data',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': '∂φ/∂t = ∇·(M∇(δF/δφ)) (M, F unknown)',
        'applications': ['Spinodal decomposition identification', 'Phase field parameter estimation', 'Concentration field reconstruction']
    },
    'inverse_solidification_stefan': {
        'name': 'Inverse Stefan Problem',
        'description': 'Identify phase change parameters and boundary conditions',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': '∂T/∂t = α∇²T (α, latent heat unknown)',
        'applications': ['Phase change parameter identification', 'Solidification front tracking', 'Thermal property estimation']
    },
    'inverse_grain_growth': {
        'name': 'Inverse Grain Growth',
        'description': 'Identify grain boundary mobility and energy from microstructure evolution',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': '∂R/∂t = Mγ/R (M, γ unknown)',
        'applications': ['Grain boundary property identification', 'Microstructure evolution tracking', 'Material property estimation']
    },
    'inverse_sintering': {
        'name': 'Inverse Sintering',
        'description': 'Identify sintering parameters from densification data',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': '∂ρ/∂t = D∇²ρ (D, sintering mechanism unknown)',
        'applications': ['Sintering parameter identification', 'Densification mechanism determination', 'Powder property estimation']
    },
    'inverse_laser_heat_source': {
        'name': 'Inverse Laser Heat Source',
        'description': 'Identify laser parameters from thermal response',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': 'Q(x, y, z, t) = Q₀ exp(-((x-x₀)²+(y-y₀)²)/2σ²) (Q₀, σ unknown)',
        'applications': ['Laser parameter identification', 'Heat source characterization', 'AM process optimization']
    },
    'inverse_melt_pool_dynamics': {
        'name': 'Inverse Melt Pool Dynamics',
        'description': 'Identify melt pool parameters from fluid dynamics data',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': 'Navier-Stokes + Surface tension (surface tension, viscosity unknown)',
        'applications': ['Melt pool parameter identification', 'Fluid property estimation', 'AM process characterization']
    },
    'inverse_crystal_plasticity': {
        'name': 'Inverse Crystal Plasticity',
        'description': 'Identify dislocation parameters from mechanical response',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': 'τ = τ₀ + αμb√ρ (dislocation parameters unknown)',
        'applications': ['Dislocation parameter identification', 'Mechanical property estimation', 'Crystal plasticity characterization']
    },
    'inverse_diffusion_solids': {
        'name': 'Inverse Diffusion in Solids',
        'description': 'Identify diffusion coefficients from concentration profiles',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': '∂c/∂t = ∇·(D∇c) (D unknown)',
        'applications': ['Diffusion coefficient identification', 'Concentration profile reconstruction', 'Material property estimation']
    },
    'inverse_precipitation_nucleation': {
        'name': 'Inverse Precipitation and Nucleation',
        'description': 'Identify nucleation parameters from precipitation data',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': 'J = J₀ exp(-ΔG*/kT) (nucleation parameters unknown)',
        'applications': ['Nucleation parameter identification', 'Precipitation kinetics determination', 'Phase transformation characterization']
    },
    'inverse_residual_stress': {
        'name': 'Inverse Residual Stress',
        'description': 'Identify residual stress from deformation measurements',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': '∇·σ = 0, σ = C:(ε - εᵗ) (residual stress unknown)',
        'applications': ['Residual stress identification', 'Thermal strain estimation', 'Stress field reconstruction']
    },
    'inverse_microstructure_evolution': {
        'name': 'Inverse Microstructure Evolution',
        'description': 'Identify microstructure evolution parameters from time-series data',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': 'Multiple phase field equations (evolution parameters unknown)',
        'applications': ['Microstructure parameter identification', 'Evolution mechanism determination', 'Material design optimization']
    },
    'inverse_poisson': {
        'name': 'Inverse Poisson',
        'description': 'Identify charge distribution from potential measurements',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': '∇²φ = -ρ/ε₀ (ρ, ε unknown)',
        'variables': ['φ', 'ρ', 'ε'],
        'category': 'electromagnetism',
        'difficulty': 'intermediate',
        'applications': ['Charge distribution reconstruction', 'Electrostatic tomography', 'Capacitor design optimization']
    },
    'inverse_wave_equation': {
        'name': 'Inverse Wave Equation',
        'description': 'Identify wave speed and medium properties from wave propagation data',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': '∇²E - (1/c²)∂²E/∂t² = 0 (c, medium properties unknown)',
        'variables': ['E', 'c', 'ε', 'μ'],
        'category': 'electromagnetism',
        'difficulty': 'advanced',
        'applications': ['Wave speed tomography', 'Medium property identification', 'Wave propagation inversion']
    },
    'inverse_telegraph': {
        'name': 'Inverse Telegraph',
        'description': 'Identify transmission line parameters from voltage/current measurements',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': '∂²V/∂x² = LC∂²V/∂t² + (RC+GL)∂V/∂t + RGV (L, C, R, G unknown)',
        'variables': ['V', 'L', 'C', 'R', 'G'],
        'category': 'electromagnetism',
        'difficulty': 'intermediate',
        'applications': ['Transmission line characterization', 'Cable parameter identification', 'Signal integrity analysis']
    }
} 