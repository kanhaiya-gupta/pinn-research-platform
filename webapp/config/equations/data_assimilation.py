"""
Data Assimilation Equations
Equations for assimilating observational data into physical models.
"""

DATA_ASSIMILATION_EQUATIONS_DICT = {
    'assimilation_burgers': {
        'name': 'Data Assimilation - Burgers',
        'description': 'Assimilate flow observations into Burgers equation',
        'icon': 'fas fa-sync',
        'color': '#27ae60',
        'formula': '∂u/∂t + u∂u/∂x = ν∂²u/∂x² + λ(u_obs - u)',
        'applications': ['Flow field reconstruction', 'Shock wave tracking', 'Traffic flow assimilation']
    },
    'assimilation_heat': {
        'name': 'Data Assimilation - Heat',
        'description': 'Assimilate temperature observations into heat equation',
        'icon': 'fas fa-sync',
        'color': '#27ae60',
        'formula': '∂u/∂t = α∂²u/∂x² + λ(u_obs - u)',
        'applications': ['Temperature field reconstruction', 'Thermal monitoring', 'Heat transfer assimilation']
    },
    'assimilation_wave': {
        'name': 'Data Assimilation - Wave',
        'description': 'Assimilate wave observations into wave equation',
        'icon': 'fas fa-sync',
        'color': '#27ae60',
        'formula': '∂²u/∂t² = c²∂²u/∂x² + λ(u_obs - u)',
        'applications': ['Wave field reconstruction', 'Seismic monitoring', 'Acoustic field assimilation']
    },
    'assimilation_shm': {
        'name': 'Data Assimilation - SHM',
        'description': 'Assimilate oscillation observations into SHM equation',
        'icon': 'fas fa-sync',
        'color': '#27ae60',
        'formula': 'd²x/dt² + ω²x = λ(x_obs - x)',
        'applications': ['Oscillation tracking', 'Vibration monitoring', 'Mechanical system assimilation']
    },
    'assimilation_helmholtz': {
        'name': 'Data Assimilation - Helmholtz',
        'description': 'Assimilate steady-state observations into Helmholtz equation',
        'icon': 'fas fa-sync',
        'color': '#27ae60',
        'formula': '∇²u + k²u = λ(u_obs - u)',
        'applications': ['Steady-state field reconstruction', 'Acoustic field assimilation', 'Electromagnetic field tracking']
    },
    'assimilation_navier_stokes': {
        'name': 'Data Assimilation - Navier-Stokes',
        'description': 'Assimilate flow observations into Navier-Stokes equations',
        'icon': 'fas fa-sync',
        'color': '#27ae60',
        'formula': 'ρ(∂v/∂t + v·∇v) = -∇p + μ∇²v + f + λ(v_obs - v)',
        'applications': ['Flow field reconstruction', 'Turbulence assimilation', 'Fluid dynamics monitoring']
    },
    'assimilation_schrodinger': {
        'name': 'Data Assimilation - Schrödinger',
        'description': 'Assimilate quantum observations into Schrödinger equation',
        'icon': 'fas fa-sync',
        'color': '#27ae60',
        'formula': 'iℏ∂ψ/∂t = Ĥψ + λ(ψ_obs - ψ)',
        'applications': ['Quantum state reconstruction', 'Wave function tracking', 'Quantum system monitoring']
    },
    'assimilation_maxwell': {
        'name': 'Data Assimilation - Maxwell',
        'description': 'Assimilate electromagnetic observations into Maxwell equations',
        'icon': 'fas fa-sync',
        'color': '#27ae60',
        'formula': '∇·E = ρ/ε₀ + λ(E_obs - E), ∇×E = -∂B/∂t + λ(B_obs - B)',
        'applications': ['Electromagnetic field reconstruction', 'Antenna pattern assimilation', 'EM field monitoring']
    },
    'assimilation_heat_transfer': {
        'name': 'Data Assimilation - Heat Transfer',
        'description': 'Assimilate thermal observations into heat transfer equation',
        'icon': 'fas fa-sync',
        'color': '#27ae60',
        'formula': 'ρc_p ∂T/∂t = ∇·(k∇T) + Q + λ(T_obs - T)',
        'applications': ['Thermal field reconstruction', 'Heat transfer monitoring', 'Thermal system assimilation']
    },
    'assimilation_elastic': {
        'name': 'Data Assimilation - Elastic',
        'description': 'Assimilate deformation observations into elasticity equations',
        'icon': 'fas fa-sync',
        'color': '#27ae60',
        'formula': '∇·σ = 0, σ = C:ε + λ(ε_obs - ε)',
        'applications': ['Deformation field reconstruction', 'Stress monitoring', 'Elastic system assimilation']
    },
    'assimilation_phase_field': {
        'name': 'Data Assimilation - Phase Field',
        'description': 'Assimilate microstructure observations into phase field equation',
        'icon': 'fas fa-sync',
        'color': '#27ae60',
        'formula': '∂φ/∂t = -M δF/δφ + λ(φ_obs - φ)',
        'applications': ['Microstructure reconstruction', 'Phase transformation tracking', 'Material evolution assimilation']
    },
    'assimilation_reaction_diffusion': {
        'name': 'Data Assimilation - Reaction-Diffusion',
        'description': 'Assimilate concentration observations into reaction-diffusion equation',
        'icon': 'fas fa-sync',
        'color': '#27ae60',
        'formula': '∂u/∂t = D∇²u + f(u) + λ(u_obs - u)',
        'applications': ['Concentration field reconstruction', 'Chemical reaction tracking', 'Diffusion monitoring']
    },
    'assimilation_poroelasticity': {
        'name': 'Data Assimilation - Poroelasticity',
        'description': 'Assimilate fluid-solid observations into poroelasticity equations',
        'icon': 'fas fa-sync',
        'color': '#27ae60',
        'formula': '∇·σ = 0, ∂p/∂t = κ∇²p + λ(p_obs - p)',
        'applications': ['Poroelastic field reconstruction', 'Pressure monitoring', 'Fluid-solid coupling assimilation']
    },
    'assimilation_viscoelasticity': {
        'name': 'Data Assimilation - Viscoelasticity',
        'description': 'Assimilate time-dependent observations into viscoelasticity equation',
        'icon': 'fas fa-sync',
        'color': '#27ae60',
        'formula': 'σ + τ∂σ/∂t = E(ε + τ∂ε/∂t) + λ(σ_obs - σ)',
        'applications': ['Viscoelastic response tracking', 'Time-dependent deformation monitoring', 'Relaxation behavior assimilation']
    },
    'assimilation_radiative_transfer': {
        'name': 'Data Assimilation - Radiative Transfer',
        'description': 'Assimilate radiation observations into radiative transfer equation',
        'icon': 'fas fa-sync',
        'color': '#27ae60',
        'formula': '∂I/∂s + (κ + σ)I = σ/4π ∫I dΩ + λ(I_obs - I)',
        'applications': ['Radiation field reconstruction', 'Atmospheric radiation monitoring', 'Radiative transfer assimilation']
    },
    'assimilation_shallow_water': {
        'name': 'Data Assimilation - Shallow Water',
        'description': 'Assimilate water level observations into shallow water equations',
        'icon': 'fas fa-sync',
        'color': '#27ae60',
        'formula': '∂h/∂t + ∇·(hv) = 0 + λ(h_obs - h)',
        'applications': ['Water level reconstruction', 'Tsunami tracking', 'Ocean surface assimilation']
    },
    'assimilation_magnetohydrodynamics': {
        'name': 'Data Assimilation - Magnetohydrodynamics',
        'description': 'Assimilate plasma observations into MHD equations',
        'icon': 'fas fa-sync',
        'color': '#27ae60',
        'formula': 'Navier-Stokes + Maxwell + λ(plasma_obs - plasma)',
        'applications': ['Plasma field reconstruction', 'MHD monitoring', 'Fusion plasma assimilation']
    },
    'assimilation_thermoelasticity': {
        'name': 'Data Assimilation - Thermoelasticity',
        'description': 'Assimilate thermal-mechanical observations into thermoelasticity equations',
        'icon': 'fas fa-sync',
        'color': '#27ae60',
        'formula': 'Heat equation + Elasticity + λ(coupled_obs - coupled)',
        'applications': ['Thermoelastic field reconstruction', 'Thermal stress monitoring', 'Coupled system assimilation']
    },
    'assimilation_advection_diffusion': {
        'name': 'Data Assimilation - Advection-Diffusion',
        'description': 'Assimilate transport observations into advection-diffusion equation',
        'icon': 'fas fa-sync',
        'color': '#27ae60',
        'formula': '∂c/∂t + v·∇c = D∇²c + λ(c_obs - c)',
        'applications': ['Transport field reconstruction', 'Pollutant tracking', 'Contaminant monitoring']
    },
    'assimilation_elastic_wave': {
        'name': 'Data Assimilation - Elastic Wave',
        'description': 'Assimilate seismic observations into elastic wave equation',
        'icon': 'fas fa-sync',
        'color': '#27ae60',
        'formula': 'ρ∂²u/∂t² = ∇·σ + λ(u_obs - u)',
        'applications': ['Seismic field reconstruction', 'Earthquake monitoring', 'Elastic wave tracking']
    },
    'assimilation_fluid_structure_interaction': {
        'name': 'Data Assimilation - Fluid-Structure Interaction',
        'description': 'Assimilate coupled observations into FSI equations',
        'icon': 'fas fa-sync',
        'color': '#27ae60',
        'formula': 'Navier-Stokes + Elasticity + λ(FSI_obs - FSI)',
        'applications': ['FSI field reconstruction', 'Coupled system monitoring', 'Fluid-structure tracking']
    },
    'assimilation_electromagnetic_thermal': {
        'name': 'Data Assimilation - Electromagnetic-Thermal',
        'description': 'Assimilate EM-thermal observations into coupled equations',
        'icon': 'fas fa-sync',
        'color': '#27ae60',
        'formula': 'Maxwell + Heat equation + λ(EM_thermal_obs - EM_thermal)',
        'applications': ['EM-thermal field reconstruction', 'Coupled field monitoring', 'Electromagnetic heating tracking']
    },
    'assimilation_biomechanical_transport': {
        'name': 'Data Assimilation - Biomechanical Transport',
        'description': 'Assimilate biological observations into biomechanical transport equations',
        'icon': 'fas fa-sync',
        'color': '#27ae60',
        'formula': 'Elasticity + Diffusion + λ(bio_obs - bio)',
        'applications': ['Biological field reconstruction', 'Tissue monitoring', 'Biomechanical transport tracking']
    },
    'assimilation_geophysical_flow': {
        'name': 'Data Assimilation - Geophysical Flow',
        'description': 'Assimilate geophysical observations into geophysical flow equations',
        'icon': 'fas fa-sync',
        'color': '#27ae60',
        'formula': 'Shallow water + Coriolis + λ(geo_obs - geo)',
        'applications': ['Geophysical field reconstruction', 'Ocean circulation monitoring', 'Atmospheric flow tracking']
    },
    'assimilation_atmospheric_oceanic': {
        'name': 'Data Assimilation - Atmospheric-Oceanic',
        'description': 'Assimilate climate observations into atmospheric-oceanic equations',
        'icon': 'fas fa-sync',
        'color': '#27ae60',
        'formula': 'Atmospheric + Oceanic equations + λ(climate_obs - climate)',
        'applications': ['Climate field reconstruction', 'Weather-ocean monitoring', 'Earth system tracking']
    },
    'assimilation_nuclear_thermal': {
        'name': 'Data Assimilation - Nuclear Thermal',
        'description': 'Assimilate nuclear observations into nuclear thermal equations',
        'icon': 'fas fa-sync',
        'color': '#27ae60',
        'formula': 'Heat equation + Nuclear source + λ(nuclear_obs - nuclear)',
        'applications': ['Nuclear thermal field reconstruction', 'Reactor monitoring', 'Nuclear safety tracking']
    },
    'assimilation_quantum_mechanical': {
        'name': 'Data Assimilation - Quantum Mechanical',
        'description': 'Assimilate quantum observations into quantum mechanical equations',
        'icon': 'fas fa-sync',
        'color': '#27ae60',
        'formula': 'Schrödinger equation + λ(quantum_obs - quantum)',
        'applications': ['Quantum field reconstruction', 'Quantum state monitoring', 'Quantum system tracking']
    },
    'assimilation_phase_field_allen_cahn': {
        'name': 'Data Assimilation - Allen-Cahn Phase Field',
        'description': 'Assimilate microstructure observations into Allen-Cahn equation',
        'icon': 'fas fa-sync',
        'color': '#27ae60',
        'formula': '∂φ/∂t = -M δF/δφ + λ(φ_obs - φ)',
        'applications': ['Microstructure reconstruction', 'Phase field tracking', 'Material evolution assimilation']
    },
    'assimilation_phase_field_cahn_hilliard': {
        'name': 'Data Assimilation - Cahn-Hilliard Phase Field',
        'description': 'Assimilate concentration observations into Cahn-Hilliard equation',
        'icon': 'fas fa-sync',
        'color': '#27ae60',
        'formula': '∂φ/∂t = ∇·(M∇(δF/δφ)) + λ(φ_obs - φ)',
        'applications': ['Concentration field reconstruction', 'Spinodal decomposition tracking', 'Phase separation assimilation']
    },
    'assimilation_solidification_stefan': {
        'name': 'Data Assimilation - Stefan Problem',
        'description': 'Assimilate temperature and phase boundary observations',
        'icon': 'fas fa-sync',
        'color': '#27ae60',
        'formula': '∂T/∂t = α∇²T + λ(T_obs - T)',
        'applications': ['Solidification front tracking', 'Temperature field reconstruction', 'Phase change assimilation']
    },
    'assimilation_grain_growth': {
        'name': 'Data Assimilation - Grain Growth',
        'description': 'Assimilate grain size observations into grain growth equation',
        'icon': 'fas fa-sync',
        'color': '#27ae60',
        'formula': '∂R/∂t = Mγ/R + λ(R_obs - R)',
        'applications': ['Grain size reconstruction', 'Microstructure evolution tracking', 'Grain growth assimilation']
    },
    'assimilation_sintering': {
        'name': 'Data Assimilation - Sintering',
        'description': 'Assimilate density observations into sintering equation',
        'icon': 'fas fa-sync',
        'color': '#27ae60',
        'formula': '∂ρ/∂t = D∇²ρ + λ(ρ_obs - ρ)',
        'applications': ['Density field reconstruction', 'Sintering process tracking', 'Densification assimilation']
    },
    'assimilation_laser_heat_source': {
        'name': 'Data Assimilation - Laser Heat Source',
        'description': 'Assimilate thermal observations into laser heat source model',
        'icon': 'fas fa-sync',
        'color': '#27ae60',
        'formula': 'Q(x, y, z, t) = Q₀ exp(-((x-x₀)²+(y-y₀)²)/2σ²) + λ(T_obs - T)',
        'applications': ['Laser heat source reconstruction', 'Thermal field tracking', 'AM process assimilation']
    },
    'assimilation_melt_pool_dynamics': {
        'name': 'Data Assimilation - Melt Pool Dynamics',
        'description': 'Assimilate melt pool observations into fluid dynamics equations',
        'icon': 'fas fa-sync',
        'color': '#27ae60',
        'formula': 'Navier-Stokes + Surface tension + λ(melt_pool_obs - melt_pool)',
        'applications': ['Melt pool reconstruction', 'Fluid dynamics tracking', 'AM process assimilation']
    },
    'assimilation_crystal_plasticity': {
        'name': 'Data Assimilation - Crystal Plasticity',
        'description': 'Assimilate mechanical observations into crystal plasticity equations',
        'icon': 'fas fa-sync',
        'color': '#27ae60',
        'formula': 'τ = τ₀ + αμb√ρ + λ(mechanical_obs - mechanical)',
        'applications': ['Crystal plasticity reconstruction', 'Mechanical response tracking', 'Dislocation evolution assimilation']
    },
    'assimilation_diffusion_solids': {
        'name': 'Data Assimilation - Diffusion in Solids',
        'description': 'Assimilate concentration observations into diffusion equation',
        'icon': 'fas fa-sync',
        'color': '#27ae60',
        'formula': '∂c/∂t = ∇·(D∇c) + λ(c_obs - c)',
        'applications': ['Concentration field reconstruction', 'Diffusion tracking', 'Material transport assimilation']
    },
    'assimilation_precipitation_nucleation': {
        'name': 'Data Assimilation - Precipitation and Nucleation',
        'description': 'Assimilate precipitation observations into nucleation equation',
        'icon': 'fas fa-sync',
        'color': '#27ae60',
        'formula': 'J = J₀ exp(-ΔG*/kT) + λ(precipitation_obs - precipitation)',
        'applications': ['Precipitation reconstruction', 'Nucleation tracking', 'Phase transformation assimilation']
    },
    'assimilation_residual_stress': {
        'name': 'Data Assimilation - Residual Stress',
        'description': 'Assimilate stress observations into residual stress equations',
        'icon': 'fas fa-sync',
        'color': '#27ae60',
        'formula': '∇·σ = 0, σ = C:(ε - εᵗ) + λ(stress_obs - stress)',
        'applications': ['Residual stress reconstruction', 'Stress field tracking', 'Thermal-mechanical assimilation']
    },
    'assimilation_microstructure_evolution': {
        'name': 'Data Assimilation - Microstructure Evolution',
        'description': 'Assimilate microstructure observations into evolution equations',
        'icon': 'fas fa-sync',
        'color': '#27ae60',
        'formula': 'Multiple phase field equations + λ(microstructure_obs - microstructure)',
        'applications': ['Microstructure reconstruction', 'Evolution tracking', 'Material transformation assimilation']
    }
} 