"""
Uncertainty Quantification Equations
Equations for quantifying and propagating uncertainty in physical systems.
"""

UNCERTAINTY_EQUATIONS_DICT = {
    'uncertainty_burgers': {
        'name': 'Uncertainty - Burgers',
        'description': 'Burgers equation with uncertain parameters and initial conditions',
        'icon': 'fas fa-chart-line',
        'color': '#e67e22',
        'formula': '∂u/∂t + u∂u/∂x = ν∂²u/∂x² (ν, u₀ uncertain)',
        'applications': ['Flow uncertainty quantification', 'Shock wave variability', 'Traffic flow uncertainty']
    },
    'uncertainty_heat': {
        'name': 'Uncertainty - Heat',
        'description': 'Heat equation with uncertain thermal diffusivity and boundary conditions',
        'icon': 'fas fa-chart-line',
        'color': '#e67e22',
        'formula': '∂u/∂t = α∂²u/∂x² (α, BC uncertain)',
        'applications': ['Thermal uncertainty quantification', 'Heat transfer variability', 'Temperature field uncertainty']
    },
    'uncertainty_wave': {
        'name': 'Uncertainty - Wave',
        'description': 'Wave equation with uncertain wave speed and initial conditions',
        'icon': 'fas fa-chart-line',
        'color': '#e67e22',
        'formula': '∂²u/∂t² = c²∂²u/∂x² (c, u₀ uncertain)',
        'applications': ['Wave uncertainty quantification', 'Seismic variability', 'Acoustic field uncertainty']
    },
    'uncertainty_shm': {
        'name': 'Uncertainty - SHM',
        'description': 'Simple harmonic motion with uncertain frequency and damping',
        'icon': 'fas fa-chart-line',
        'color': '#e67e22',
        'formula': 'd²x/dt² + 2ζωdx/dt + ω²x = 0 (ω, ζ uncertain)',
        'applications': ['Oscillation uncertainty quantification', 'Vibration variability', 'Mechanical system uncertainty']
    },
    'uncertainty_helmholtz': {
        'name': 'Uncertainty - Helmholtz',
        'description': 'Helmholtz equation with uncertain wavenumber and boundary conditions',
        'icon': 'fas fa-chart-line',
        'color': '#e67e22',
        'formula': '∇²u + k²u = 0 (k, BC uncertain)',
        'applications': ['Steady-state uncertainty quantification', 'Acoustic field variability', 'Electromagnetic uncertainty']
    },
    'uncertainty_navier_stokes': {
        'name': 'Uncertainty - Navier-Stokes',
        'description': 'Navier-Stokes equations with uncertain viscosity and boundary conditions',
        'icon': 'fas fa-chart-line',
        'color': '#e67e22',
        'formula': 'ρ(∂v/∂t + v·∇v) = -∇p + μ∇²v + f (μ, BC uncertain)',
        'applications': ['Flow uncertainty quantification', 'Turbulence variability', 'Fluid dynamics uncertainty']
    },
    'uncertainty_schrodinger': {
        'name': 'Uncertainty - Schrödinger',
        'description': 'Schrödinger equation with uncertain potential and initial state',
        'icon': 'fas fa-chart-line',
        'color': '#e67e22',
        'formula': 'iℏ∂ψ/∂t = Ĥψ (V, ψ₀ uncertain)',
        'applications': ['Quantum uncertainty quantification', 'Wave function variability', 'Quantum state uncertainty']
    },
    'uncertainty_maxwell': {
        'name': 'Uncertainty - Maxwell',
        'description': 'Maxwell equations with uncertain electromagnetic properties',
        'icon': 'fas fa-chart-line',
        'color': '#e67e22',
        'formula': '∇·E = ρ/ε₀, ∇×E = -∂B/∂t (ε, μ uncertain)',
        'applications': ['Electromagnetic uncertainty quantification', 'EM field variability', 'Antenna uncertainty']
    },
    'uncertainty_heat_transfer': {
        'name': 'Uncertainty - Heat Transfer',
        'description': 'Heat transfer equation with uncertain thermal properties',
        'icon': 'fas fa-chart-line',
        'color': '#e67e22',
        'formula': 'ρc_p ∂T/∂t = ∇·(k∇T) + Q (k, c_p uncertain)',
        'applications': ['Thermal uncertainty quantification', 'Heat transfer variability', 'Thermal field uncertainty']
    },
    'uncertainty_elastic': {
        'name': 'Uncertainty - Elastic',
        'description': 'Elasticity equations with uncertain elastic moduli',
        'icon': 'fas fa-chart-line',
        'color': '#e67e22',
        'formula': '∇·σ = 0, σ = C:ε (C uncertain)',
        'applications': ['Elastic uncertainty quantification', 'Deformation variability', 'Stress field uncertainty']
    },
    'uncertainty_phase_field': {
        'name': 'Uncertainty - Phase Field',
        'description': 'Phase field equation with uncertain mobility and free energy',
        'icon': 'fas fa-chart-line',
        'color': '#e67e22',
        'formula': '∂φ/∂t = -M δF/δφ (M, F uncertain)',
        'applications': ['Phase field uncertainty quantification', 'Microstructure variability', 'Phase transformation uncertainty']
    },
    'uncertainty_reaction_diffusion': {
        'name': 'Uncertainty - Reaction-Diffusion',
        'description': 'Reaction-diffusion equation with uncertain parameters',
        'icon': 'fas fa-chart-line',
        'color': '#e67e22',
        'formula': '∂u/∂t = D∇²u + f(u) (D, f uncertain)',
        'applications': ['Chemical uncertainty quantification', 'Reaction variability', 'Concentration field uncertainty']
    },
    'uncertainty_poroelasticity': {
        'name': 'Uncertainty - Poroelasticity',
        'description': 'Poroelasticity equations with uncertain permeability and elastic moduli',
        'icon': 'fas fa-chart-line',
        'color': '#e67e22',
        'formula': '∇·σ = 0, ∂p/∂t = κ∇²p (κ, C uncertain)',
        'applications': ['Poroelastic uncertainty quantification', 'Pressure variability', 'Fluid-solid uncertainty']
    },
    'uncertainty_viscoelasticity': {
        'name': 'Uncertainty - Viscoelasticity',
        'description': 'Viscoelasticity equation with uncertain parameters',
        'icon': 'fas fa-chart-line',
        'color': '#e67e22',
        'formula': 'σ + τ∂σ/∂t = E(ε + τ∂ε/∂t) (E, τ uncertain)',
        'applications': ['Viscoelastic uncertainty quantification', 'Relaxation variability', 'Time-dependent uncertainty']
    },
    'uncertainty_radiative_transfer': {
        'name': 'Uncertainty - Radiative Transfer',
        'description': 'Radiative transfer equation with uncertain optical properties',
        'icon': 'fas fa-chart-line',
        'color': '#e67e22',
        'formula': '∂I/∂s + (κ + σ)I = σ/4π ∫I dΩ (κ, σ uncertain)',
        'applications': ['Radiation uncertainty quantification', 'Atmospheric variability', 'Radiative field uncertainty']
    },
    'uncertainty_shallow_water': {
        'name': 'Uncertainty - Shallow Water',
        'description': 'Shallow water equations with uncertain bathymetry and friction',
        'icon': 'fas fa-chart-line',
        'color': '#e67e22',
        'formula': '∂h/∂t + ∇·(hv) = 0 (bathymetry, friction uncertain)',
        'applications': ['Water uncertainty quantification', 'Tsunami variability', 'Ocean surface uncertainty']
    },
    'uncertainty_magnetohydrodynamics': {
        'name': 'Uncertainty - Magnetohydrodynamics',
        'description': 'MHD equations with uncertain plasma parameters',
        'icon': 'fas fa-chart-line',
        'color': '#e67e22',
        'formula': 'Navier-Stokes + Maxwell (plasma parameters uncertain)',
        'applications': ['Plasma uncertainty quantification', 'MHD variability', 'Fusion plasma uncertainty']
    },
    'uncertainty_thermoelasticity': {
        'name': 'Uncertainty - Thermoelasticity',
        'description': 'Thermoelasticity equations with uncertain coupled parameters',
        'icon': 'fas fa-chart-line',
        'color': '#e67e22',
        'formula': 'Heat equation + Elasticity (coupled parameters uncertain)',
        'applications': ['Thermoelastic uncertainty quantification', 'Thermal stress variability', 'Coupled system uncertainty']
    },
    'uncertainty_advection_diffusion': {
        'name': 'Uncertainty - Advection-Diffusion',
        'description': 'Advection-diffusion equation with uncertain velocity and diffusivity',
        'icon': 'fas fa-chart-line',
        'color': '#e67e22',
        'formula': '∂c/∂t + v·∇c = D∇²c (v, D uncertain)',
        'applications': ['Transport uncertainty quantification', 'Pollutant variability', 'Contaminant field uncertainty']
    },
    'uncertainty_elastic_wave': {
        'name': 'Uncertainty - Elastic Wave',
        'description': 'Elastic wave equation with uncertain elastic moduli',
        'icon': 'fas fa-chart-line',
        'color': '#e67e22',
        'formula': 'ρ∂²u/∂t² = ∇·σ (elastic moduli uncertain)',
        'applications': ['Seismic uncertainty quantification', 'Wave field variability', 'Elastic wave uncertainty']
    },
    'uncertainty_fluid_structure_interaction': {
        'name': 'Uncertainty - Fluid-Structure Interaction',
        'description': 'FSI equations with uncertain coupled parameters',
        'icon': 'fas fa-chart-line',
        'color': '#e67e22',
        'formula': 'Navier-Stokes + Elasticity (FSI parameters uncertain)',
        'applications': ['FSI uncertainty quantification', 'Aeroelastic variability', 'Coupled system uncertainty']
    },
    'uncertainty_electromagnetic_thermal': {
        'name': 'Uncertainty - Electromagnetic-Thermal',
        'description': 'EM-thermal equations with uncertain coupled parameters',
        'icon': 'fas fa-chart-line',
        'color': '#e67e22',
        'formula': 'Maxwell + Heat equation (EM-thermal parameters uncertain)',
        'applications': ['EM-thermal uncertainty quantification', 'Electromagnetic heating variability', 'Coupled field uncertainty']
    },
    'uncertainty_biomechanical_transport': {
        'name': 'Uncertainty - Biomechanical Transport',
        'description': 'Biomechanical transport equations with uncertain biological parameters',
        'icon': 'fas fa-chart-line',
        'color': '#e67e22',
        'formula': 'Elasticity + Diffusion (biological parameters uncertain)',
        'applications': ['Biological uncertainty quantification', 'Tissue variability', 'Biomechanical transport uncertainty']
    },
    'uncertainty_geophysical_flow': {
        'name': 'Uncertainty - Geophysical Flow',
        'description': 'Geophysical flow equations with uncertain geophysical parameters',
        'icon': 'fas fa-chart-line',
        'color': '#e67e22',
        'formula': 'Shallow water + Coriolis (geophysical parameters uncertain)',
        'applications': ['Geophysical uncertainty quantification', 'Ocean circulation variability', 'Atmospheric flow uncertainty']
    },
    'uncertainty_atmospheric_oceanic': {
        'name': 'Uncertainty - Atmospheric-Oceanic',
        'description': 'Atmospheric-oceanic equations with uncertain climate parameters',
        'icon': 'fas fa-chart-line',
        'color': '#e67e22',
        'formula': 'Atmospheric + Oceanic equations (climate parameters uncertain)',
        'applications': ['Climate uncertainty quantification', 'Weather variability', 'Earth system uncertainty']
    },
    'uncertainty_nuclear_thermal': {
        'name': 'Uncertainty - Nuclear Thermal',
        'description': 'Nuclear thermal equations with uncertain nuclear parameters',
        'icon': 'fas fa-chart-line',
        'color': '#e67e22',
        'formula': 'Heat equation + Nuclear source (nuclear parameters uncertain)',
        'applications': ['Nuclear uncertainty quantification', 'Reactor variability', 'Nuclear safety uncertainty']
    },
    'uncertainty_quantum_mechanical': {
        'name': 'Uncertainty - Quantum Mechanical',
        'description': 'Quantum mechanical equations with uncertain quantum parameters',
        'icon': 'fas fa-chart-line',
        'color': '#e67e22',
        'formula': 'Schrödinger equation (quantum parameters uncertain)',
        'applications': ['Quantum uncertainty quantification', 'Wave function variability', 'Quantum system uncertainty']
    },
    'uncertainty_phase_field_allen_cahn': {
        'name': 'Uncertainty - Allen-Cahn Phase Field',
        'description': 'Allen-Cahn equation with uncertain phase field parameters',
        'icon': 'fas fa-chart-line',
        'color': '#e67e22',
        'formula': '∂φ/∂t = -M δF/δφ (M, F uncertain)',
        'applications': ['Phase field uncertainty quantification', 'Microstructure variability', 'Material evolution uncertainty']
    },
    'uncertainty_phase_field_cahn_hilliard': {
        'name': 'Uncertainty - Cahn-Hilliard Phase Field',
        'description': 'Cahn-Hilliard equation with uncertain conserved parameters',
        'icon': 'fas fa-chart-line',
        'color': '#e67e22',
        'formula': '∂φ/∂t = ∇·(M∇(δF/δφ)) (M, F uncertain)',
        'applications': ['Spinodal decomposition uncertainty', 'Concentration variability', 'Phase separation uncertainty']
    },
    'uncertainty_solidification_stefan': {
        'name': 'Uncertainty - Stefan Problem',
        'description': 'Stefan problem with uncertain phase change parameters',
        'icon': 'fas fa-chart-line',
        'color': '#e67e22',
        'formula': '∂T/∂t = α∇²T (α, latent heat uncertain)',
        'applications': ['Solidification uncertainty quantification', 'Phase boundary variability', 'Thermal property uncertainty']
    },
    'uncertainty_grain_growth': {
        'name': 'Uncertainty - Grain Growth',
        'description': 'Grain growth with uncertain grain boundary parameters',
        'icon': 'fas fa-chart-line',
        'color': '#e67e22',
        'formula': '∂R/∂t = Mγ/R (M, γ uncertain)',
        'applications': ['Grain growth uncertainty quantification', 'Microstructure variability', 'Material property uncertainty']
    },
    'uncertainty_sintering': {
        'name': 'Uncertainty - Sintering',
        'description': 'Sintering with uncertain densification parameters',
        'icon': 'fas fa-chart-line',
        'color': '#e67e22',
        'formula': '∂ρ/∂t = D∇²ρ (D, sintering mechanism uncertain)',
        'applications': ['Sintering uncertainty quantification', 'Densification variability', 'Powder property uncertainty']
    },
    'uncertainty_laser_heat_source': {
        'name': 'Uncertainty - Laser Heat Source',
        'description': 'Laser heat source with uncertain laser parameters',
        'icon': 'fas fa-chart-line',
        'color': '#e67e22',
        'formula': 'Q(x, y, z, t) = Q₀ exp(-((x-x₀)²+(y-y₀)²)/2σ²) (Q₀, σ uncertain)',
        'applications': ['Laser uncertainty quantification', 'Heat source variability', 'AM process uncertainty']
    },
    'uncertainty_melt_pool_dynamics': {
        'name': 'Uncertainty - Melt Pool Dynamics',
        'description': 'Melt pool dynamics with uncertain fluid parameters',
        'icon': 'fas fa-chart-line',
        'color': '#e67e22',
        'formula': 'Navier-Stokes + Surface tension (fluid parameters uncertain)',
        'applications': ['Melt pool uncertainty quantification', 'Fluid dynamics variability', 'AM process uncertainty']
    },
    'uncertainty_crystal_plasticity': {
        'name': 'Uncertainty - Crystal Plasticity',
        'description': 'Crystal plasticity with uncertain dislocation parameters',
        'icon': 'fas fa-chart-line',
        'color': '#e67e22',
        'formula': 'τ = τ₀ + αμb√ρ (dislocation parameters uncertain)',
        'applications': ['Crystal plasticity uncertainty quantification', 'Mechanical variability', 'Material behavior uncertainty']
    },
    'uncertainty_diffusion_solids': {
        'name': 'Uncertainty - Diffusion in Solids',
        'description': 'Diffusion with uncertain diffusion coefficients',
        'icon': 'fas fa-chart-line',
        'color': '#e67e22',
        'formula': '∂c/∂t = ∇·(D∇c) (D uncertain)',
        'applications': ['Diffusion uncertainty quantification', 'Concentration variability', 'Material transport uncertainty']
    },
    'uncertainty_precipitation_nucleation': {
        'name': 'Uncertainty - Precipitation and Nucleation',
        'description': 'Precipitation with uncertain nucleation parameters',
        'icon': 'fas fa-chart-line',
        'color': '#e67e22',
        'formula': 'J = J₀ exp(-ΔG*/kT) (nucleation parameters uncertain)',
        'applications': ['Precipitation uncertainty quantification', 'Nucleation variability', 'Phase transformation uncertainty']
    },
    'uncertainty_residual_stress': {
        'name': 'Uncertainty - Residual Stress',
        'description': 'Residual stress with uncertain thermal-mechanical parameters',
        'icon': 'fas fa-chart-line',
        'color': '#e67e22',
        'formula': '∇·σ = 0, σ = C:(ε - εᵗ) (thermal-mechanical parameters uncertain)',
        'applications': ['Residual stress uncertainty quantification', 'Stress variability', 'Material processing uncertainty']
    },
    'uncertainty_microstructure_evolution': {
        'name': 'Uncertainty - Microstructure Evolution',
        'description': 'Microstructure evolution with uncertain evolution parameters',
        'icon': 'fas fa-chart-line',
        'color': '#e67e22',
        'formula': 'Multiple phase field equations (evolution parameters uncertain)',
        'applications': ['Microstructure uncertainty quantification', 'Evolution variability', 'Material transformation uncertainty']
    }
} 