"""
Sparse Data Equations
Equations for learning from limited or sparse observational data.
"""

SPARSE_DATA_EQUATIONS_DICT = {
    'sparse_burgers': {
        'name': 'Sparse Data - Burgers',
        'description': 'Burgers equation learning from limited observations',
        'icon': 'fas fa-database',
        'color': '#f39c12',
        'formula': '∂u/∂t + u∂u/∂x = ν∂²u/∂x² (sparse data)',
        'applications': ['Limited flow measurements', 'Shock wave analysis', 'Traffic modeling']
    },
    'sparse_heat': {
        'name': 'Sparse Data - Heat',
        'description': 'Heat equation learning from limited temperature measurements',
        'icon': 'fas fa-database',
        'color': '#f39c12',
        'formula': '∂u/∂t = α∂²u/∂x² (sparse data)',
        'applications': ['Limited thermal sensors', 'Material characterization', 'Climate modeling']
    },
    'sparse_wave': {
        'name': 'Sparse Data - Wave',
        'description': 'Wave equation learning from limited wave measurements',
        'icon': 'fas fa-database',
        'color': '#f39c12',
        'formula': '∂²u/∂t² = c²∂²u/∂x² (sparse data)',
        'applications': ['Limited acoustic sensors', 'Seismic monitoring', 'Wave propagation']
    },
    'sparse_shm': {
        'name': 'Sparse Data - SHM',
        'description': 'Simple harmonic motion learning from limited oscillation data',
        'icon': 'fas fa-database',
        'color': '#f39c12',
        'formula': 'd²x/dt² + ω²x = 0 (sparse data)',
        'applications': ['Limited vibration sensors', 'Oscillator characterization', 'Mechanical system identification']
    },
    'sparse_helmholtz': {
        'name': 'Sparse Data - Helmholtz',
        'description': 'Helmholtz equation learning from limited steady-state measurements',
        'icon': 'fas fa-database',
        'color': '#f39c12',
        'formula': '∇²u + k²u = 0 (sparse data)',
        'applications': ['Limited acoustic sensors', 'Electromagnetic field reconstruction', 'Steady-state wave analysis']
    },
    'sparse_navier_stokes': {
        'name': 'Sparse Data - Navier-Stokes',
        'description': 'Navier-Stokes learning from limited flow measurements',
        'icon': 'fas fa-database',
        'color': '#f39c12',
        'formula': 'ρ(∂v/∂t + v·∇v) = -∇p + μ∇²v + f (sparse data)',
        'applications': ['Limited flow sensors', 'Turbulence modeling', 'Fluid dynamics reconstruction']
    },
    'sparse_schrodinger': {
        'name': 'Sparse Data - Schrödinger',
        'description': 'Schrödinger equation learning from limited quantum measurements',
        'icon': 'fas fa-database',
        'color': '#f39c12',
        'formula': 'iℏ∂ψ/∂t = Ĥψ (sparse data)',
        'applications': ['Limited quantum measurements', 'Wave function reconstruction', 'Quantum state estimation']
    },
    'sparse_maxwell': {
        'name': 'Sparse Data - Maxwell',
        'description': 'Maxwell equations learning from limited electromagnetic measurements',
        'icon': 'fas fa-database',
        'color': '#f39c12',
        'formula': '∇·E = ρ/ε₀, ∇×E = -∂B/∂t (sparse data)',
        'applications': ['Limited EM sensors', 'Electromagnetic field reconstruction', 'Antenna pattern estimation']
    },
    'sparse_heat_transfer': {
        'name': 'Sparse Data - Heat Transfer',
        'description': 'Heat transfer learning from limited thermal measurements',
        'icon': 'fas fa-database',
        'color': '#f39c12',
        'formula': 'ρc_p ∂T/∂t = ∇·(k∇T) + Q (sparse data)',
        'applications': ['Limited thermal sensors', 'Heat transfer coefficient estimation', 'Thermal field reconstruction']
    },
    'sparse_elastic': {
        'name': 'Sparse Data - Elastic',
        'description': 'Elasticity learning from limited deformation measurements',
        'icon': 'fas fa-database',
        'color': '#f39c12',
        'formula': '∇·σ = 0, σ = C:ε (sparse data)',
        'applications': ['Limited strain sensors', 'Elastic modulus identification', 'Stress field reconstruction']
    },
    'sparse_phase_field': {
        'name': 'Sparse Data - Phase Field',
        'description': 'Phase field learning from limited microstructure observations',
        'icon': 'fas fa-database',
        'color': '#f39c12',
        'formula': '∂φ/∂t = -M δF/δφ (sparse data)',
        'applications': ['Limited microstructure data', 'Phase transformation tracking', 'Grain growth modeling']
    },
    'sparse_reaction_diffusion': {
        'name': 'Sparse Data - Reaction-Diffusion',
        'description': 'Reaction-diffusion learning from limited concentration measurements',
        'icon': 'fas fa-database',
        'color': '#f39c12',
        'formula': '∂u/∂t = D∇²u + f(u) (sparse data)',
        'applications': ['Limited chemical sensors', 'Reaction front tracking', 'Concentration field reconstruction']
    },
    'sparse_poroelasticity': {
        'name': 'Sparse Data - Poroelasticity',
        'description': 'Poroelasticity learning from limited fluid-solid measurements',
        'icon': 'fas fa-database',
        'color': '#f39c12',
        'formula': '∇·σ = 0, ∂p/∂t = κ∇²p (sparse data)',
        'applications': ['Limited pressure sensors', 'Permeability estimation', 'Poroelastic field reconstruction']
    },
    'sparse_viscoelasticity': {
        'name': 'Sparse Data - Viscoelasticity',
        'description': 'Viscoelasticity learning from limited time-dependent measurements',
        'icon': 'fas fa-database',
        'color': '#f39c12',
        'formula': 'σ + τ∂σ/∂t = E(ε + τ∂ε/∂t) (sparse data)',
        'applications': ['Limited time-series data', 'Viscoelastic parameter identification', 'Relaxation time estimation']
    },
    'sparse_radiative_transfer': {
        'name': 'Sparse Data - Radiative Transfer',
        'description': 'Radiative transfer learning from limited radiation measurements',
        'icon': 'fas fa-database',
        'color': '#f39c12',
        'formula': '∂I/∂s + (κ + σ)I = σ/4π ∫I dΩ (sparse data)',
        'applications': ['Limited radiation sensors', 'Atmospheric radiation modeling', 'Radiative field reconstruction']
    },
    'sparse_shallow_water': {
        'name': 'Sparse Data - Shallow Water',
        'description': 'Shallow water learning from limited water level measurements',
        'icon': 'fas fa-database',
        'color': '#f39c12',
        'formula': '∂h/∂t + ∇·(hv) = 0 (sparse data)',
        'applications': ['Limited water level sensors', 'Tsunami modeling', 'Ocean surface reconstruction']
    },
    'sparse_magnetohydrodynamics': {
        'name': 'Sparse Data - Magnetohydrodynamics',
        'description': 'MHD learning from limited plasma measurements',
        'icon': 'fas fa-database',
        'color': '#f39c12',
        'formula': 'Navier-Stokes + Maxwell (sparse data)',
        'applications': ['Limited plasma diagnostics', 'MHD field reconstruction', 'Fusion plasma modeling']
    },
    'sparse_thermoelasticity': {
        'name': 'Sparse Data - Thermoelasticity',
        'description': 'Thermoelasticity learning from limited thermal-mechanical measurements',
        'icon': 'fas fa-database',
        'color': '#f39c12',
        'formula': 'Heat equation + Elasticity (sparse data)',
        'applications': ['Limited coupled sensors', 'Thermal stress estimation', 'Thermoelastic field reconstruction']
    },
    'sparse_advection_diffusion': {
        'name': 'Sparse Data - Advection-Diffusion',
        'description': 'Advection-diffusion learning from limited transport measurements',
        'icon': 'fas fa-database',
        'color': '#f39c12',
        'formula': '∂c/∂t + v·∇c = D∇²c (sparse data)',
        'applications': ['Limited transport sensors', 'Pollutant tracking', 'Contaminant field reconstruction']
    },
    'sparse_elastic_wave': {
        'name': 'Sparse Data - Elastic Wave',
        'description': 'Elastic wave learning from limited seismic measurements',
        'icon': 'fas fa-database',
        'color': '#f39c12',
        'formula': 'ρ∂²u/∂t² = ∇·σ (sparse data)',
        'applications': ['Limited seismic sensors', 'Earthquake modeling', 'Elastic wave field reconstruction']
    },
    'sparse_fluid_structure_interaction': {
        'name': 'Sparse Data - Fluid-Structure Interaction',
        'description': 'FSI learning from limited coupled measurements',
        'icon': 'fas fa-database',
        'color': '#f39c12',
        'formula': 'Navier-Stokes + Elasticity (sparse data)',
        'applications': ['Limited FSI sensors', 'Coupled field reconstruction', 'Fluid-structure tracking']
    },
    'sparse_electromagnetic_thermal': {
        'name': 'Sparse Data - Electromagnetic-Thermal',
        'description': 'EM-thermal learning from limited coupled measurements',
        'icon': 'fas fa-database',
        'color': '#f39c12',
        'formula': 'Maxwell + Heat equation (sparse data)',
        'applications': ['Limited EM-thermal sensors', 'Coupled field reconstruction', 'Electromagnetic heating modeling']
    },
    'sparse_biomechanical_transport': {
        'name': 'Sparse Data - Biomechanical Transport',
        'description': 'Biomechanical transport learning from limited biological measurements',
        'icon': 'fas fa-database',
        'color': '#f39c12',
        'formula': 'Elasticity + Diffusion (sparse data)',
        'applications': ['Limited biological sensors', 'Tissue modeling', 'Biological transport reconstruction']
    },
    'sparse_geophysical_flow': {
        'name': 'Sparse Data - Geophysical Flow',
        'description': 'Geophysical flow learning from limited geophysical measurements',
        'icon': 'fas fa-database',
        'color': '#f39c12',
        'formula': 'Shallow water + Coriolis (sparse data)',
        'applications': ['Limited geophysical sensors', 'Ocean circulation modeling', 'Atmospheric flow reconstruction']
    },
    'sparse_atmospheric_oceanic': {
        'name': 'Sparse Data - Atmospheric-Oceanic',
        'description': 'Atmospheric-oceanic learning from limited climate measurements',
        'icon': 'fas fa-database',
        'color': '#f39c12',
        'formula': 'Atmospheric + Oceanic equations (sparse data)',
        'applications': ['Limited climate sensors', 'Climate system modeling', 'Weather-ocean reconstruction']
    },
    'sparse_nuclear_thermal': {
        'name': 'Sparse Data - Nuclear Thermal',
        'description': 'Nuclear thermal learning from limited nuclear measurements',
        'icon': 'fas fa-database',
        'color': '#f39c12',
        'formula': 'Heat equation + Nuclear source (sparse data)',
        'applications': ['Limited nuclear sensors', 'Reactor modeling', 'Nuclear thermal field reconstruction']
    },
    'sparse_quantum_mechanical': {
        'name': 'Sparse Data - Quantum Mechanical',
        'description': 'Quantum mechanics learning from limited quantum measurements',
        'icon': 'fas fa-database',
        'color': '#f39c12',
        'formula': 'Schrödinger equation (sparse data)',
        'applications': ['Limited quantum measurements', 'Quantum state reconstruction', 'Quantum system modeling']
    },
    'sparse_phase_field_allen_cahn': {
        'name': 'Sparse Data - Allen-Cahn Phase Field',
        'description': 'Allen-Cahn equation learning from limited microstructure observations',
        'icon': 'fas fa-database',
        'color': '#f39c12',
        'formula': '∂φ/∂t = -M δF/δφ (sparse data)',
        'applications': ['Limited microstructure data', 'Phase field reconstruction', 'Material evolution modeling']
    },
    'sparse_phase_field_cahn_hilliard': {
        'name': 'Sparse Data - Cahn-Hilliard Phase Field',
        'description': 'Cahn-Hilliard equation learning from limited concentration measurements',
        'icon': 'fas fa-database',
        'color': '#f39c12',
        'formula': '∂φ/∂t = ∇·(M∇(δF/δφ)) (sparse data)',
        'applications': ['Limited concentration data', 'Spinodal decomposition reconstruction', 'Phase separation modeling']
    },
    'sparse_solidification_stefan': {
        'name': 'Sparse Data - Stefan Problem',
        'description': 'Stefan problem learning from limited temperature and phase boundary data',
        'icon': 'fas fa-database',
        'color': '#f39c12',
        'formula': '∂T/∂t = α∇²T (sparse data)',
        'applications': ['Limited thermal sensors', 'Solidification front reconstruction', 'Phase change modeling']
    },
    'sparse_grain_growth': {
        'name': 'Sparse Data - Grain Growth',
        'description': 'Grain growth learning from limited grain size measurements',
        'icon': 'fas fa-database',
        'color': '#f39c12',
        'formula': '∂R/∂t = Mγ/R (sparse data)',
        'applications': ['Limited grain size data', 'Microstructure evolution reconstruction', 'Grain growth modeling']
    },
    'sparse_sintering': {
        'name': 'Sparse Data - Sintering',
        'description': 'Sintering learning from limited density measurements',
        'icon': 'fas fa-database',
        'color': '#f39c12',
        'formula': '∂ρ/∂t = D∇²ρ (sparse data)',
        'applications': ['Limited density sensors', 'Sintering process reconstruction', 'Densification modeling']
    },
    'sparse_laser_heat_source': {
        'name': 'Sparse Data - Laser Heat Source',
        'description': 'Laser heat source learning from limited thermal measurements',
        'icon': 'fas fa-database',
        'color': '#f39c12',
        'formula': 'Q(x, y, z, t) = Q₀ exp(-((x-x₀)²+(y-y₀)²)/2σ²) (sparse data)',
        'applications': ['Limited thermal sensors', 'Laser heat source reconstruction', 'AM process modeling']
    },
    'sparse_melt_pool_dynamics': {
        'name': 'Sparse Data - Melt Pool Dynamics',
        'description': 'Melt pool dynamics learning from limited fluid measurements',
        'icon': 'fas fa-database',
        'color': '#f39c12',
        'formula': 'Navier-Stokes + Surface tension (sparse data)',
        'applications': ['Limited fluid sensors', 'Melt pool reconstruction', 'AM fluid dynamics modeling']
    },
    'sparse_crystal_plasticity': {
        'name': 'Sparse Data - Crystal Plasticity',
        'description': 'Crystal plasticity learning from limited mechanical measurements',
        'icon': 'fas fa-database',
        'color': '#f39c12',
        'formula': 'τ = τ₀ + αμb√ρ (sparse data)',
        'applications': ['Limited mechanical sensors', 'Crystal plasticity reconstruction', 'Dislocation modeling']
    },
    'sparse_diffusion_solids': {
        'name': 'Sparse Data - Diffusion in Solids',
        'description': 'Diffusion learning from limited concentration measurements',
        'icon': 'fas fa-database',
        'color': '#f39c12',
        'formula': '∂c/∂t = ∇·(D∇c) (sparse data)',
        'applications': ['Limited concentration sensors', 'Diffusion field reconstruction', 'Material transport modeling']
    },
    'sparse_precipitation_nucleation': {
        'name': 'Sparse Data - Precipitation and Nucleation',
        'description': 'Precipitation learning from limited nucleation measurements',
        'icon': 'fas fa-database',
        'color': '#f39c12',
        'formula': 'J = J₀ exp(-ΔG*/kT) (sparse data)',
        'applications': ['Limited nucleation data', 'Precipitation reconstruction', 'Phase transformation modeling']
    },
    'sparse_residual_stress': {
        'name': 'Sparse Data - Residual Stress',
        'description': 'Residual stress learning from limited stress measurements',
        'icon': 'fas fa-database',
        'color': '#f39c12',
        'formula': '∇·σ = 0, σ = C:(ε - εᵗ) (sparse data)',
        'applications': ['Limited stress sensors', 'Residual stress reconstruction', 'Thermal-mechanical modeling']
    },
    'sparse_microstructure_evolution': {
        'name': 'Sparse Data - Microstructure Evolution',
        'description': 'Microstructure evolution learning from limited evolution data',
        'icon': 'fas fa-database',
        'color': '#f39c12',
        'formula': 'Multiple phase field equations (sparse data)',
        'applications': ['Limited microstructure data', 'Evolution reconstruction', 'Material transformation modeling']
    }
} 