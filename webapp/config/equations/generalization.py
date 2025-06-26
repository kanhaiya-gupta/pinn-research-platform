"""
Generalization Equations
Equations for improving model generalization and transfer learning.
"""

GENERALIZATION_EQUATIONS_DICT = {
    'generalization_burgers': {
        'name': 'Generalization - Burgers',
        'description': 'Burgers equation with improved generalization across parameter ranges',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': '∂u/∂t + u∂u/∂x = ν∂²u/∂x² (generalized)',
        'applications': ['Multi-scale flow modeling', 'Parameter space exploration', 'Transfer learning for flows']
    },
    'generalization_heat': {
        'name': 'Generalization - Heat',
        'description': 'Heat equation with improved generalization across thermal properties',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': '∂u/∂t = α∂²u/∂x² (generalized)',
        'applications': ['Multi-material thermal modeling', 'Thermal property generalization', 'Transfer learning for heat transfer']
    },
    'generalization_wave': {
        'name': 'Generalization - Wave',
        'description': 'Wave equation with improved generalization across wave speeds',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': '∂²u/∂t² = c²∂²u/∂x² (generalized)',
        'applications': ['Multi-medium wave modeling', 'Wave speed generalization', 'Transfer learning for waves']
    },
    'generalization_shm': {
        'name': 'Generalization - SHM',
        'description': 'Simple harmonic motion with improved generalization across frequencies',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': 'd²x/dt² + ω²x = 0 (generalized)',
        'applications': ['Multi-frequency oscillation modeling', 'Frequency generalization', 'Transfer learning for oscillations']
    },
    'generalization_helmholtz': {
        'name': 'Generalization - Helmholtz',
        'description': 'Helmholtz equation with improved generalization across wavenumbers',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': '∇²u + k²u = 0 (generalized)',
        'applications': ['Multi-wavenumber modeling', 'Wavenumber generalization', 'Transfer learning for steady-state waves']
    },
    'generalization_navier_stokes': {
        'name': 'Generalization - Navier-Stokes',
        'description': 'Navier-Stokes equations with improved generalization across Reynolds numbers',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': 'ρ(∂v/∂t + v·∇v) = -∇p + μ∇²v + f (generalized)',
        'applications': ['Multi-Reynolds flow modeling', 'Reynolds number generalization', 'Transfer learning for fluid dynamics']
    },
    'generalization_schrodinger': {
        'name': 'Generalization - Schrödinger',
        'description': 'Schrödinger equation with improved generalization across potentials',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': 'iℏ∂ψ/∂t = Ĥψ (generalized)',
        'applications': ['Multi-potential quantum modeling', 'Potential generalization', 'Transfer learning for quantum systems']
    },
    'generalization_maxwell': {
        'name': 'Generalization - Maxwell',
        'description': 'Maxwell equations with improved generalization across electromagnetic properties',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': '∇·E = ρ/ε₀, ∇×E = -∂B/∂t (generalized)',
        'applications': ['Multi-material EM modeling', 'EM property generalization', 'Transfer learning for electromagnetism']
    },
    'generalization_heat_transfer': {
        'name': 'Generalization - Heat Transfer',
        'description': 'Heat transfer equation with improved generalization across thermal properties',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': 'ρc_p ∂T/∂t = ∇·(k∇T) + Q (generalized)',
        'applications': ['Multi-material thermal modeling', 'Thermal property generalization', 'Transfer learning for heat transfer']
    },
    'generalization_elastic': {
        'name': 'Generalization - Elastic',
        'description': 'Elasticity equations with improved generalization across elastic moduli',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': '∇·σ = 0, σ = C:ε (generalized)',
        'applications': ['Multi-material structural modeling', 'Elastic modulus generalization', 'Transfer learning for elasticity']
    },
    'generalization_phase_field': {
        'name': 'Generalization - Phase Field',
        'description': 'Phase field equation with improved generalization across materials',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': '∂φ/∂t = -M δF/δφ (generalized)',
        'applications': ['Multi-material phase modeling', 'Material generalization', 'Transfer learning for phase transformations']
    },
    'generalization_reaction_diffusion': {
        'name': 'Generalization - Reaction-Diffusion',
        'description': 'Reaction-diffusion equation with improved generalization across reaction rates',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': '∂u/∂t = D∇²u + f(u) (generalized)',
        'applications': ['Multi-reaction chemical modeling', 'Reaction rate generalization', 'Transfer learning for chemical kinetics']
    },
    'generalization_poroelasticity': {
        'name': 'Generalization - Poroelasticity',
        'description': 'Poroelasticity equations with improved generalization across poroelastic properties',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': '∇·σ = 0, ∂p/∂t = κ∇²p (generalized)',
        'applications': ['Multi-material poroelastic modeling', 'Poroelastic property generalization', 'Transfer learning for poroelasticity']
    },
    'generalization_viscoelasticity': {
        'name': 'Generalization - Viscoelasticity',
        'description': 'Viscoelasticity equation with improved generalization across viscoelastic parameters',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': 'σ + τ∂σ/∂t = E(ε + τ∂ε/∂t) (generalized)',
        'applications': ['Multi-material viscoelastic modeling', 'Viscoelastic parameter generalization', 'Transfer learning for viscoelasticity']
    },
    'generalization_radiative_transfer': {
        'name': 'Generalization - Radiative Transfer',
        'description': 'Radiative transfer equation with improved generalization across optical properties',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': '∂I/∂s + (κ + σ)I = σ/4π ∫I dΩ (generalized)',
        'applications': ['Multi-medium radiative modeling', 'Optical property generalization', 'Transfer learning for radiative transfer']
    },
    'generalization_shallow_water': {
        'name': 'Generalization - Shallow Water',
        'description': 'Shallow water equations with improved generalization across bathymetry',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': '∂h/∂t + ∇·(hv) = 0 (generalized)',
        'applications': ['Multi-bathymetry hydrodynamic modeling', 'Bathymetry generalization', 'Transfer learning for shallow water']
    },
    'generalization_magnetohydrodynamics': {
        'name': 'Generalization - Magnetohydrodynamics',
        'description': 'MHD equations with improved generalization across plasma parameters',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': 'Navier-Stokes + Maxwell (generalized)',
        'applications': ['Multi-parameter plasma modeling', 'Plasma parameter generalization', 'Transfer learning for MHD']
    },
    'generalization_thermoelasticity': {
        'name': 'Generalization - Thermoelasticity',
        'description': 'Thermoelasticity equations with improved generalization across coupled parameters',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': 'Heat equation + Elasticity (generalized)',
        'applications': ['Multi-material thermoelastic modeling', 'Coupled parameter generalization', 'Transfer learning for thermoelasticity']
    },
    'generalization_advection_diffusion': {
        'name': 'Generalization - Advection-Diffusion',
        'description': 'Advection-diffusion equation with improved generalization across transport parameters',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': '∂c/∂t + v·∇c = D∇²c (generalized)',
        'applications': ['Multi-parameter transport modeling', 'Transport parameter generalization', 'Transfer learning for advection-diffusion']
    },
    'generalization_elastic_wave': {
        'name': 'Generalization - Elastic Wave',
        'description': 'Elastic wave equation with improved generalization across elastic properties',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': 'ρ∂²u/∂t² = ∇·σ (generalized)',
        'applications': ['Multi-material seismic modeling', 'Elastic property generalization', 'Transfer learning for elastic waves']
    },
    'generalization_fluid_structure_interaction': {
        'name': 'Generalization - Fluid-Structure Interaction',
        'description': 'FSI equations with improved generalization across coupling parameters',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': 'Navier-Stokes + Elasticity (generalized)',
        'applications': ['Multi-parameter FSI modeling', 'Coupling parameter generalization', 'Transfer learning for FSI']
    },
    'generalization_electromagnetic_thermal': {
        'name': 'Generalization - Electromagnetic-Thermal',
        'description': 'EM-thermal equations with improved generalization across coupled parameters',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': 'Maxwell + Heat equation (generalized)',
        'applications': ['Multi-parameter EM-thermal modeling', 'Coupled parameter generalization', 'Transfer learning for EM-thermal']
    },
    'generalization_biomechanical_transport': {
        'name': 'Generalization - Biomechanical Transport',
        'description': 'Biomechanical transport equations with improved generalization across biological parameters',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': 'Elasticity + Diffusion (generalized)',
        'applications': ['Multi-tissue biological modeling', 'Biological parameter generalization', 'Transfer learning for biomechanics']
    },
    'generalization_geophysical_flow': {
        'name': 'Generalization - Geophysical Flow',
        'description': 'Geophysical flow equations with improved generalization across geophysical parameters',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': 'Shallow water + Coriolis (generalized)',
        'applications': ['Multi-scale geophysical modeling', 'Geophysical parameter generalization', 'Transfer learning for geophysical flows']
    },
    'generalization_atmospheric_oceanic': {
        'name': 'Generalization - Atmospheric-Oceanic',
        'description': 'Atmospheric-oceanic equations with improved generalization across climate parameters',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': 'Atmospheric + Oceanic equations (generalized)',
        'applications': ['Multi-scale climate modeling', 'Climate parameter generalization', 'Transfer learning for climate systems']
    },
    'generalization_nuclear_thermal': {
        'name': 'Generalization - Nuclear Thermal',
        'description': 'Nuclear thermal equations with improved generalization across nuclear parameters',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': 'Heat equation + Nuclear source (generalized)',
        'applications': ['Multi-reactor nuclear modeling', 'Nuclear parameter generalization', 'Transfer learning for nuclear systems']
    },
    'generalization_quantum_mechanical': {
        'name': 'Generalization - Quantum Mechanical',
        'description': 'Quantum mechanical equations with improved generalization across quantum parameters',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': 'Schrödinger equation (generalized)',
        'applications': ['Multi-system quantum modeling', 'Quantum parameter generalization', 'Transfer learning for quantum mechanics']
    },
    'generalization_phase_field_allen_cahn': {
        'name': 'Generalization - Allen-Cahn Phase Field',
        'description': 'Allen-Cahn equation with improved generalization across materials',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': '∂φ/∂t = -M δF/δφ (generalized)',
        'applications': ['Multi-material phase field modeling', 'Material generalization', 'Transfer learning for phase transformations']
    },
    'generalization_phase_field_cahn_hilliard': {
        'name': 'Generalization - Cahn-Hilliard Phase Field',
        'description': 'Cahn-Hilliard equation with improved generalization across concentration ranges',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': '∂φ/∂t = ∇·(M∇(δF/δφ)) (generalized)',
        'applications': ['Multi-concentration phase separation modeling', 'Concentration generalization', 'Transfer learning for spinodal decomposition']
    },
    'generalization_solidification_stefan': {
        'name': 'Generalization - Stefan Problem',
        'description': 'Stefan problem with improved generalization across phase change materials',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': '∂T/∂t = α∇²T (generalized)',
        'applications': ['Multi-material solidification modeling', 'Phase change generalization', 'Transfer learning for solidification']
    },
    'generalization_grain_growth': {
        'name': 'Generalization - Grain Growth',
        'description': 'Grain growth with improved generalization across polycrystalline materials',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': '∂R/∂t = Mγ/R (generalized)',
        'applications': ['Multi-material grain growth modeling', 'Grain boundary generalization', 'Transfer learning for microstructure evolution']
    },
    'generalization_sintering': {
        'name': 'Generalization - Sintering',
        'description': 'Sintering with improved generalization across powder materials',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': '∂ρ/∂t = D∇²ρ (generalized)',
        'applications': ['Multi-powder sintering modeling', 'Powder property generalization', 'Transfer learning for densification']
    },
    'generalization_laser_heat_source': {
        'name': 'Generalization - Laser Heat Source',
        'description': 'Laser heat source with improved generalization across materials and processes',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': 'Q(x, y, z, t) = Q₀ exp(-((x-x₀)²+(y-y₀)²)/2σ²) (generalized)',
        'applications': ['Multi-material laser processing modeling', 'Laser parameter generalization', 'Transfer learning for AM']
    },
    'generalization_melt_pool_dynamics': {
        'name': 'Generalization - Melt Pool Dynamics',
        'description': 'Melt pool dynamics with improved generalization across metals',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': 'Navier-Stokes + Surface tension (generalized)',
        'applications': ['Multi-metal melt pool modeling', 'Metal property generalization', 'Transfer learning for fluid dynamics']
    },
    'generalization_crystal_plasticity': {
        'name': 'Generalization - Crystal Plasticity',
        'description': 'Crystal plasticity with improved generalization across crystal structures',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': 'τ = τ₀ + αμb√ρ (generalized)',
        'applications': ['Multi-crystal plasticity modeling', 'Crystal structure generalization', 'Transfer learning for mechanical behavior']
    },
    'generalization_diffusion_solids': {
        'name': 'Generalization - Diffusion in Solids',
        'description': 'Diffusion with improved generalization across solid materials',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': '∂c/∂t = ∇·(D∇c) (generalized)',
        'applications': ['Multi-material diffusion modeling', 'Diffusion coefficient generalization', 'Transfer learning for material transport']
    },
    'generalization_precipitation_nucleation': {
        'name': 'Generalization - Precipitation and Nucleation',
        'description': 'Precipitation with improved generalization across alloy systems',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': 'J = J₀ exp(-ΔG*/kT) (generalized)',
        'applications': ['Multi-alloy precipitation modeling', 'Alloy system generalization', 'Transfer learning for phase transformations']
    },
    'generalization_residual_stress': {
        'name': 'Generalization - Residual Stress',
        'description': 'Residual stress with improved generalization across processing conditions',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': '∇·σ = 0, σ = C:(ε - εᵗ) (generalized)',
        'applications': ['Multi-process residual stress modeling', 'Processing condition generalization', 'Transfer learning for thermal-mechanical']
    },
    'generalization_microstructure_evolution': {
        'name': 'Generalization - Microstructure Evolution',
        'description': 'Microstructure evolution with improved generalization across material systems',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': 'Multiple phase field equations (generalized)',
        'applications': ['Multi-material microstructure modeling', 'Material system generalization', 'Transfer learning for microstructure design']
    },
    'generalization_additive_manufacturing': {
        'name': 'Generalization - Additive Manufacturing',
        'description': 'AM processes with improved generalization across materials and processes',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': 'Laser + Melt pool + Solidification + Mechanics (generalized)',
        'applications': ['Multi-material AM modeling', 'AM process generalization', 'Transfer learning for 3D printing']
    },
    'generalization_material_processing': {
        'name': 'Generalization - Material Processing',
        'description': 'Material processing with improved generalization across processing routes',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#9b59b6',
        'formula': 'Heat + Mechanics + Phase transformations (generalized)',
        'applications': ['Multi-route material processing modeling', 'Processing route generalization', 'Transfer learning for manufacturing']
    }
} 