"""
Efficiency Equations
Equations for optimizing computational efficiency and performance.
"""

EFFICIENCY_EQUATIONS_DICT = {
    'efficiency_burgers': {
        'name': 'Efficiency - Burgers',
        'description': 'Optimized Burgers equation with efficient numerical schemes',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': '∂u/∂t + u∂u/∂x = ν∂²u/∂x² (optimized)',
        'applications': ['Fast flow simulation', 'Real-time traffic modeling', 'Efficient shock wave computation']
    },
    'efficiency_heat': {
        'name': 'Efficiency - Heat',
        'description': 'Optimized heat equation with efficient discretization',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': '∂u/∂t = α∂²u/∂x² (optimized)',
        'applications': ['Fast thermal simulation', 'Real-time heat transfer', 'Efficient temperature computation']
    },
    'efficiency_wave': {
        'name': 'Efficiency - Wave',
        'description': 'Optimized wave equation with efficient time integration',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': '∂²u/∂t² = c²∂²u/∂x² (optimized)',
        'applications': ['Fast wave simulation', 'Real-time acoustics', 'Efficient seismic computation']
    },
    'efficiency_shm': {
        'name': 'Efficiency - SHM',
        'description': 'Optimized simple harmonic motion with efficient solvers',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': 'd²x/dt² + ω²x = 0 (optimized)',
        'applications': ['Fast oscillation simulation', 'Real-time vibration analysis', 'Efficient mechanical computation']
    },
    'efficiency_helmholtz': {
        'name': 'Efficiency - Helmholtz',
        'description': 'Optimized Helmholtz equation with efficient solvers',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': '∇²u + k²u = 0 (optimized)',
        'applications': ['Fast steady-state simulation', 'Real-time acoustic field', 'Efficient wave computation']
    },
    'efficiency_navier_stokes': {
        'name': 'Efficiency - Navier-Stokes',
        'description': 'Optimized Navier-Stokes equations with efficient algorithms',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': 'ρ(∂v/∂t + v·∇v) = -∇p + μ∇²v + f (optimized)',
        'applications': ['Fast flow simulation', 'Real-time fluid dynamics', 'Efficient turbulence computation']
    },
    'efficiency_schrodinger': {
        'name': 'Efficiency - Schrödinger',
        'description': 'Optimized Schrödinger equation with efficient quantum algorithms',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': 'iℏ∂ψ/∂t = Ĥψ (optimized)',
        'applications': ['Fast quantum simulation', 'Real-time wave function evolution', 'Efficient quantum computation']
    },
    'efficiency_maxwell': {
        'name': 'Efficiency - Maxwell',
        'description': 'Optimized Maxwell equations with efficient electromagnetic algorithms',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': '∇·E = ρ/ε₀, ∇×E = -∂B/∂t (optimized)',
        'applications': ['Fast EM simulation', 'Real-time electromagnetic field', 'Efficient antenna computation']
    },
    'efficiency_heat_transfer': {
        'name': 'Efficiency - Heat Transfer',
        'description': 'Optimized heat transfer equation with efficient thermal algorithms',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': 'ρc_p ∂T/∂t = ∇·(k∇T) + Q (optimized)',
        'applications': ['Fast thermal simulation', 'Real-time heat transfer', 'Efficient thermal computation']
    },
    'efficiency_elastic': {
        'name': 'Efficiency - Elastic',
        'description': 'Optimized elasticity equations with efficient structural algorithms',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': '∇·σ = 0, σ = C:ε (optimized)',
        'applications': ['Fast structural simulation', 'Real-time deformation analysis', 'Efficient stress computation']
    },
    'efficiency_phase_field': {
        'name': 'Efficiency - Phase Field',
        'description': 'Optimized phase field equation with efficient evolution algorithms',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': '∂φ/∂t = -M δF/δφ (optimized)',
        'applications': ['Fast microstructure simulation', 'Real-time phase evolution', 'Efficient transformation computation']
    },
    'efficiency_reaction_diffusion': {
        'name': 'Efficiency - Reaction-Diffusion',
        'description': 'Optimized reaction-diffusion equation with efficient chemical algorithms',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': '∂u/∂t = D∇²u + f(u) (optimized)',
        'applications': ['Fast chemical simulation', 'Real-time reaction tracking', 'Efficient concentration computation']
    },
    'efficiency_poroelasticity': {
        'name': 'Efficiency - Poroelasticity',
        'description': 'Optimized poroelasticity equations with efficient coupled algorithms',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': '∇·σ = 0, ∂p/∂t = κ∇²p (optimized)',
        'applications': ['Fast poroelastic simulation', 'Real-time fluid-solid coupling', 'Efficient pressure computation']
    },
    'efficiency_viscoelasticity': {
        'name': 'Efficiency - Viscoelasticity',
        'description': 'Optimized viscoelasticity equation with efficient time algorithms',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': 'σ + τ∂σ/∂t = E(ε + τ∂ε/∂t) (optimized)',
        'applications': ['Fast viscoelastic simulation', 'Real-time relaxation analysis', 'Efficient time-dependent computation']
    },
    'efficiency_radiative_transfer': {
        'name': 'Efficiency - Radiative Transfer',
        'description': 'Optimized radiative transfer equation with efficient radiation algorithms',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': '∂I/∂s + (κ + σ)I = σ/4π ∫I dΩ (optimized)',
        'applications': ['Fast radiation simulation', 'Real-time radiative transfer', 'Efficient radiation computation']
    },
    'efficiency_shallow_water': {
        'name': 'Efficiency - Shallow Water',
        'description': 'Optimized shallow water equations with efficient hydrodynamic algorithms',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': '∂h/∂t + ∇·(hv) = 0 (optimized)',
        'applications': ['Fast hydrodynamic simulation', 'Real-time water level tracking', 'Efficient ocean computation']
    },
    'efficiency_magnetohydrodynamics': {
        'name': 'Efficiency - Magnetohydrodynamics',
        'description': 'Optimized MHD equations with efficient plasma algorithms',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': 'Navier-Stokes + Maxwell (optimized)',
        'applications': ['Fast plasma simulation', 'Real-time MHD evolution', 'Efficient fusion computation']
    },
    'efficiency_thermoelasticity': {
        'name': 'Efficiency - Thermoelasticity',
        'description': 'Optimized thermoelasticity equations with efficient coupled algorithms',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': 'Heat equation + Elasticity (optimized)',
        'applications': ['Fast thermoelastic simulation', 'Real-time thermal stress', 'Efficient coupled computation']
    },
    'efficiency_advection_diffusion': {
        'name': 'Efficiency - Advection-Diffusion',
        'description': 'Optimized advection-diffusion equation with efficient transport algorithms',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': '∂c/∂t + v·∇c = D∇²c (optimized)',
        'applications': ['Fast transport simulation', 'Real-time pollutant tracking', 'Efficient contaminant computation']
    },
    'efficiency_elastic_wave': {
        'name': 'Efficiency - Elastic Wave',
        'description': 'Optimized elastic wave equation with efficient seismic algorithms',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': 'ρ∂²u/∂t² = ∇·σ (optimized)',
        'applications': ['Fast seismic simulation', 'Real-time wave propagation', 'Efficient earthquake computation']
    },
    'efficiency_fluid_structure_interaction': {
        'name': 'Efficiency - Fluid-Structure Interaction',
        'description': 'Optimized FSI equations with efficient coupling algorithms',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': 'Navier-Stokes + Elasticity (optimized)',
        'applications': ['Fast FSI simulation', 'Real-time fluid-structure coupling', 'Efficient aeroelastic computation']
    },
    'efficiency_electromagnetic_thermal': {
        'name': 'Efficiency - Electromagnetic-Thermal',
        'description': 'Optimized EM-thermal equations with efficient coupled algorithms',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': 'Maxwell + Heat equation (optimized)',
        'applications': ['Fast EM-thermal simulation', 'Real-time electromagnetic heating', 'Efficient coupled computation']
    },
    'efficiency_biomechanical_transport': {
        'name': 'Efficiency - Biomechanical Transport',
        'description': 'Optimized biomechanical transport equations with efficient biological algorithms',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': 'Elasticity + Diffusion (optimized)',
        'applications': ['Fast biological simulation', 'Real-time tissue modeling', 'Efficient biomechanical computation']
    },
    'efficiency_geophysical_flow': {
        'name': 'Efficiency - Geophysical Flow',
        'description': 'Optimized geophysical flow equations with efficient geophysical algorithms',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': 'Shallow water + Coriolis (optimized)',
        'applications': ['Fast geophysical simulation', 'Real-time ocean circulation', 'Efficient atmospheric computation']
    },
    'efficiency_atmospheric_oceanic': {
        'name': 'Efficiency - Atmospheric-Oceanic',
        'description': 'Optimized atmospheric-oceanic equations with efficient climate algorithms',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': 'Atmospheric + Oceanic equations (optimized)',
        'applications': ['Fast climate simulation', 'Real-time weather-ocean coupling', 'Efficient earth system computation']
    },
    'efficiency_nuclear_thermal': {
        'name': 'Efficiency - Nuclear Thermal',
        'description': 'Optimized nuclear thermal equations with efficient nuclear algorithms',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': 'Heat equation + Nuclear source (optimized)',
        'applications': ['Fast nuclear simulation', 'Real-time reactor modeling', 'Efficient nuclear computation']
    },
    'efficiency_quantum_mechanical': {
        'name': 'Efficiency - Quantum Mechanical',
        'description': 'Optimized quantum mechanical equations with efficient quantum algorithms',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': 'Schrödinger equation (optimized)',
        'applications': ['Fast quantum simulation', 'Real-time wave function evolution', 'Efficient quantum computation']
    },
    'efficiency_phase_field_allen_cahn': {
        'name': 'Efficiency - Allen-Cahn Phase Field',
        'description': 'Optimized Allen-Cahn equation with efficient phase field algorithms',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': '∂φ/∂t = -M δF/δφ (optimized)',
        'applications': ['Fast phase field simulation', 'Real-time microstructure evolution', 'Efficient material modeling']
    },
    'efficiency_phase_field_cahn_hilliard': {
        'name': 'Efficiency - Cahn-Hilliard Phase Field',
        'description': 'Optimized Cahn-Hilliard equation with efficient conserved algorithms',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': '∂φ/∂t = ∇·(M∇(δF/δφ)) (optimized)',
        'applications': ['Fast spinodal decomposition', 'Real-time concentration evolution', 'Efficient phase separation']
    },
    'efficiency_solidification_stefan': {
        'name': 'Efficiency - Stefan Problem',
        'description': 'Optimized Stefan problem with efficient phase change algorithms',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': '∂T/∂t = α∇²T (optimized)',
        'applications': ['Fast solidification simulation', 'Real-time phase change tracking', 'Efficient thermal modeling']
    },
    'efficiency_grain_growth': {
        'name': 'Efficiency - Grain Growth',
        'description': 'Optimized grain growth with efficient microstructure algorithms',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': '∂R/∂t = Mγ/R (optimized)',
        'applications': ['Fast grain growth simulation', 'Real-time microstructure evolution', 'Efficient material science']
    },
    'efficiency_sintering': {
        'name': 'Efficiency - Sintering',
        'description': 'Optimized sintering with efficient densification algorithms',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': '∂ρ/∂t = D∇²ρ (optimized)',
        'applications': ['Fast sintering simulation', 'Real-time densification tracking', 'Efficient powder processing']
    },
    'efficiency_laser_heat_source': {
        'name': 'Efficiency - Laser Heat Source',
        'description': 'Optimized laser heat source with efficient thermal algorithms',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': 'Q(x, y, z, t) = Q₀ exp(-((x-x₀)²+(y-y₀)²)/2σ²) (optimized)',
        'applications': ['Fast laser simulation', 'Real-time heat source tracking', 'Efficient AM modeling']
    },
    'efficiency_melt_pool_dynamics': {
        'name': 'Efficiency - Melt Pool Dynamics',
        'description': 'Optimized melt pool dynamics with efficient fluid algorithms',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': 'Navier-Stokes + Surface tension (optimized)',
        'applications': ['Fast melt pool simulation', 'Real-time fluid dynamics', 'Efficient AM process modeling']
    },
    'efficiency_crystal_plasticity': {
        'name': 'Efficiency - Crystal Plasticity',
        'description': 'Optimized crystal plasticity with efficient dislocation algorithms',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': 'τ = τ₀ + αμb√ρ (optimized)',
        'applications': ['Fast crystal plasticity simulation', 'Real-time dislocation evolution', 'Efficient mechanical modeling']
    },
    'efficiency_diffusion_solids': {
        'name': 'Efficiency - Diffusion in Solids',
        'description': 'Optimized diffusion with efficient transport algorithms',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': '∂c/∂t = ∇·(D∇c) (optimized)',
        'applications': ['Fast diffusion simulation', 'Real-time concentration evolution', 'Efficient material transport']
    },
    'efficiency_precipitation_nucleation': {
        'name': 'Efficiency - Precipitation and Nucleation',
        'description': 'Optimized precipitation with efficient nucleation algorithms',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': 'J = J₀ exp(-ΔG*/kT) (optimized)',
        'applications': ['Fast precipitation simulation', 'Real-time nucleation tracking', 'Efficient phase transformation']
    },
    'efficiency_residual_stress': {
        'name': 'Efficiency - Residual Stress',
        'description': 'Optimized residual stress with efficient thermal-mechanical algorithms',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': '∇·σ = 0, σ = C:(ε - εᵗ) (optimized)',
        'applications': ['Fast residual stress simulation', 'Real-time stress evolution', 'Efficient thermal-mechanical modeling']
    },
    'efficiency_microstructure_evolution': {
        'name': 'Efficiency - Microstructure Evolution',
        'description': 'Optimized microstructure evolution with efficient multi-phase algorithms',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': 'Multiple phase field equations (optimized)',
        'applications': ['Fast microstructure simulation', 'Real-time evolution tracking', 'Efficient material transformation']
    },
    'efficiency_additive_manufacturing': {
        'name': 'Efficiency - Additive Manufacturing',
        'description': 'Optimized AM process with efficient multi-physics algorithms',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': 'Laser + Melt pool + Solidification + Mechanics (optimized)',
        'applications': ['Fast AM simulation', 'Real-time process tracking', 'Efficient 3D printing modeling']
    },
    'efficiency_material_processing': {
        'name': 'Efficiency - Material Processing',
        'description': 'Optimized material processing with efficient multi-scale algorithms',
        'icon': 'fas fa-tachometer-alt',
        'color': '#2ecc71',
        'formula': 'Heat + Mechanics + Phase transformations (optimized)',
        'applications': ['Fast material processing simulation', 'Real-time process optimization', 'Efficient manufacturing modeling']
    }
} 