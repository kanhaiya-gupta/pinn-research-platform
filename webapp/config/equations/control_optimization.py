"""
Control Optimization Equations
Equations for optimal control and parameter optimization problems.
"""

CONTROL_OPTIMIZATION_EQUATIONS_DICT = {
    'control_burgers': {
        'name': 'Control - Burgers',
        'description': 'Optimal control of Burgers equation with control input',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': '∂u/∂t + u∂u/∂x = ν∂²u/∂x² + f(x,t)',
        'applications': ['Flow control', 'Shock wave suppression', 'Traffic flow optimization']
    },
    'control_heat': {
        'name': 'Control - Heat',
        'description': 'Optimal control of heat equation with heat source control',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': '∂u/∂t = α∂²u/∂x² + Q(x,t)',
        'applications': ['Thermal control', 'Temperature regulation', 'Heat transfer optimization']
    },
    'control_wave': {
        'name': 'Control - Wave',
        'description': 'Optimal control of wave equation with source control',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': '∂²u/∂t² = c²∂²u/∂x² + f(x,t)',
        'applications': ['Wave control', 'Vibration suppression', 'Acoustic field optimization']
    },
    'control_shm': {
        'name': 'Control - SHM',
        'description': 'Optimal control of simple harmonic motion with forcing',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': 'd²x/dt² + ω²x = f(t)',
        'applications': ['Oscillation control', 'Vibration suppression', 'Mechanical system optimization']
    },
    'control_helmholtz': {
        'name': 'Control - Helmholtz',
        'description': 'Optimal control of Helmholtz equation with source control',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': '∇²u + k²u = f(x)',
        'applications': ['Acoustic field control', 'Electromagnetic field optimization', 'Wave field shaping']
    },
    'control_navier_stokes': {
        'name': 'Control - Navier-Stokes',
        'description': 'Optimal control of Navier-Stokes equations with body force control',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': 'ρ(∂v/∂t + v·∇v) = -∇p + μ∇²v + f(x,t)',
        'applications': ['Flow control', 'Turbulence suppression', 'Fluid dynamics optimization']
    },
    'control_schrodinger': {
        'name': 'Control - Schrödinger',
        'description': 'Optimal control of Schrödinger equation with potential control',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': 'iℏ∂ψ/∂t = Ĥψ + V_control(x,t)ψ',
        'applications': ['Quantum control', 'Wave function shaping', 'Quantum state optimization']
    },
    'control_maxwell': {
        'name': 'Control - Maxwell',
        'description': 'Optimal control of Maxwell equations with source control',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': '∇·E = ρ/ε₀ + ρ_control, ∇×E = -∂B/∂t + J_control',
        'applications': ['Electromagnetic control', 'Antenna optimization', 'EM field shaping']
    },
    'control_heat_transfer': {
        'name': 'Control - Heat Transfer',
        'description': 'Optimal control of heat transfer with heat source control',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': 'ρc_p ∂T/∂t = ∇·(k∇T) + Q_control(x,t)',
        'applications': ['Thermal control', 'Heat transfer optimization', 'Temperature field shaping']
    },
    'control_elastic': {
        'name': 'Control - Elastic',
        'description': 'Optimal control of elasticity equations with boundary control',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': '∇·σ = f_control, σ = C:ε',
        'applications': ['Deformation control', 'Stress optimization', 'Structural control']
    },
    'control_phase_field': {
        'name': 'Control - Phase Field',
        'description': 'Optimal control of phase field equation with external field control',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': '∂φ/∂t = -M δF/δφ + H_control(x,t)',
        'applications': ['Microstructure control', 'Phase transformation optimization', 'Material evolution control']
    },
    'control_reaction_diffusion': {
        'name': 'Control - Reaction-Diffusion',
        'description': 'Optimal control of reaction-diffusion equation with source control',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': '∂u/∂t = D∇²u + f(u) + S_control(x,t)',
        'applications': ['Chemical reaction control', 'Pattern formation optimization', 'Concentration field control']
    },
    'control_poroelasticity': {
        'name': 'Control - Poroelasticity',
        'description': 'Optimal control of poroelasticity equations with pressure control',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': '∇·σ = 0, ∂p/∂t = κ∇²p + Q_control(x,t)',
        'applications': ['Pressure control', 'Fluid flow optimization', 'Poroelastic system control']
    },
    'control_viscoelasticity': {
        'name': 'Control - Viscoelasticity',
        'description': 'Optimal control of viscoelasticity equation with stress control',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': 'σ + τ∂σ/∂t = E(ε + τ∂ε/∂t) + σ_control(t)',
        'applications': ['Viscoelastic control', 'Relaxation optimization', 'Time-dependent deformation control']
    },
    'control_radiative_transfer': {
        'name': 'Control - Radiative Transfer',
        'description': 'Optimal control of radiative transfer equation with source control',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': '∂I/∂s + (κ + σ)I = σ/4π ∫I dΩ + S_control(s)',
        'applications': ['Radiation control', 'Atmospheric radiation optimization', 'Radiative field shaping']
    },
    'control_shallow_water': {
        'name': 'Control - Shallow Water',
        'description': 'Optimal control of shallow water equations with source control',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': '∂h/∂t + ∇·(hv) = S_control(x,t)',
        'applications': ['Water level control', 'Tsunami mitigation', 'Ocean surface optimization']
    },
    'control_magnetohydrodynamics': {
        'name': 'Control - Magnetohydrodynamics',
        'description': 'Optimal control of MHD equations with electromagnetic control',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': 'Navier-Stokes + Maxwell + control_sources',
        'applications': ['Plasma control', 'MHD optimization', 'Fusion plasma control']
    },
    'control_thermoelasticity': {
        'name': 'Control - Thermoelasticity',
        'description': 'Optimal control of thermoelasticity equations with thermal-mechanical control',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': 'Heat equation + Elasticity + control_sources',
        'applications': ['Thermoelastic control', 'Thermal stress optimization', 'Coupled system control']
    },
    'control_advection_diffusion': {
        'name': 'Control - Advection-Diffusion',
        'description': 'Optimal control of advection-diffusion equation with source control',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': '∂c/∂t + v·∇c = D∇²c + S_control(x,t)',
        'applications': ['Transport control', 'Pollutant mitigation', 'Contaminant field optimization']
    },
    'control_elastic_wave': {
        'name': 'Control - Elastic Wave',
        'description': 'Optimal control of elastic wave equation with source control',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': 'ρ∂²u/∂t² = ∇·σ + f_control(x,t)',
        'applications': ['Seismic control', 'Wave field optimization', 'Elastic wave shaping']
    },
    'control_fluid_structure_interaction': {
        'name': 'Control - Fluid-Structure Interaction',
        'description': 'Optimal control of FSI equations with coupled control',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': 'Navier-Stokes + Elasticity + FSI_control',
        'applications': ['FSI control', 'Aeroelastic optimization', 'Coupled system control']
    },
    'control_electromagnetic_thermal': {
        'name': 'Control - Electromagnetic-Thermal',
        'description': 'Optimal control of EM-thermal equations with coupled control',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': 'Maxwell + Heat equation + EM_thermal_control',
        'applications': ['EM-thermal control', 'Electromagnetic heating optimization', 'Coupled field control']
    },
    'control_biomechanical_transport': {
        'name': 'Control - Biomechanical Transport',
        'description': 'Optimal control of biomechanical transport equations with biological control',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': 'Elasticity + Diffusion + bio_control',
        'applications': ['Biological control', 'Tissue optimization', 'Biomechanical transport control']
    },
    'control_geophysical_flow': {
        'name': 'Control - Geophysical Flow',
        'description': 'Optimal control of geophysical flow equations with geophysical control',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': 'Shallow water + Coriolis + geo_control',
        'applications': ['Ocean circulation control', 'Atmospheric flow optimization', 'Geophysical system control']
    },
    'control_atmospheric_oceanic': {
        'name': 'Control - Atmospheric-Oceanic',
        'description': 'Optimal control of atmospheric-oceanic equations with climate control',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': 'Atmospheric + Oceanic equations + climate_control',
        'applications': ['Climate control', 'Weather modification', 'Earth system optimization']
    },
    'control_nuclear_thermal': {
        'name': 'Control - Nuclear Thermal',
        'description': 'Optimal control of nuclear thermal equations with nuclear control',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': 'Heat equation + Nuclear source + nuclear_control',
        'applications': ['Nuclear reactor control', 'Fusion device optimization', 'Nuclear safety control']
    },
    'control_quantum_mechanical': {
        'name': 'Control - Quantum Mechanical',
        'description': 'Optimal control of quantum mechanical equations with quantum control',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': 'Schrödinger equation + quantum_control',
        'applications': ['Quantum control', 'Wave function optimization', 'Quantum system control']
    },
    'control_phase_field_allen_cahn': {
        'name': 'Control - Allen-Cahn Phase Field',
        'description': 'Optimal control of Allen-Cahn equation with external field control',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': '∂φ/∂t = -M δF/δφ + H_control(x,t)',
        'applications': ['Microstructure control', 'Phase transformation optimization', 'Material evolution control']
    },
    'control_phase_field_cahn_hilliard': {
        'name': 'Control - Cahn-Hilliard Phase Field',
        'description': 'Optimal control of Cahn-Hilliard equation with source control',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': '∂φ/∂t = ∇·(M∇(δF/δφ)) + S_control(x,t)',
        'applications': ['Concentration control', 'Phase separation optimization', 'Spinodal decomposition control']
    },
    'control_solidification_stefan': {
        'name': 'Control - Stefan Problem',
        'description': 'Optimal control of solidification with heat source control',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': '∂T/∂t = α∇²T + Q_control(x,t)',
        'applications': ['Solidification control', 'Phase change optimization', 'Thermal processing control']
    },
    'control_grain_growth': {
        'name': 'Control - Grain Growth',
        'description': 'Optimal control of grain growth with external field control',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': '∂R/∂t = Mγ/R + F_control(x,t)',
        'applications': ['Grain size control', 'Microstructure optimization', 'Material property control']
    },
    'control_sintering': {
        'name': 'Control - Sintering',
        'description': 'Optimal control of sintering with pressure and temperature control',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': '∂ρ/∂t = D∇²ρ + P_control(x,t)',
        'applications': ['Densification control', 'Sintering optimization', 'Powder processing control']
    },
    'control_laser_heat_source': {
        'name': 'Control - Laser Heat Source',
        'description': 'Optimal control of laser parameters for AM processing',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': 'Q(x, y, z, t) = Q₀(t) exp(-((x-x₀(t))²+(y-y₀(t))²)/2σ²(t))',
        'applications': ['Laser power control', 'AM process optimization', 'Thermal processing control']
    },
    'control_melt_pool_dynamics': {
        'name': 'Control - Melt Pool Dynamics',
        'description': 'Optimal control of melt pool with laser and cooling control',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': 'Navier-Stokes + Surface tension + melt_pool_control',
        'applications': ['Melt pool control', 'AM process optimization', 'Fluid dynamics control']
    },
    'control_crystal_plasticity': {
        'name': 'Control - Crystal Plasticity',
        'description': 'Optimal control of crystal plasticity with stress control',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': 'τ = τ₀ + αμb√ρ + stress_control(t)',
        'applications': ['Mechanical property control', 'Crystal plasticity optimization', 'Material behavior control']
    },
    'control_diffusion_solids': {
        'name': 'Control - Diffusion in Solids',
        'description': 'Optimal control of diffusion with concentration control',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': '∂c/∂t = ∇·(D∇c) + S_control(x,t)',
        'applications': ['Concentration control', 'Diffusion optimization', 'Material transport control']
    },
    'control_precipitation_nucleation': {
        'name': 'Control - Precipitation and Nucleation',
        'description': 'Optimal control of precipitation with temperature control',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': 'J = J₀ exp(-ΔG*/kT) + nucleation_control(t)',
        'applications': ['Precipitation control', 'Nucleation optimization', 'Phase transformation control']
    },
    'control_residual_stress': {
        'name': 'Control - Residual Stress',
        'description': 'Optimal control of residual stress with thermal-mechanical control',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': '∇·σ = 0, σ = C:(ε - εᵗ) + stress_control',
        'applications': ['Residual stress control', 'Thermal stress optimization', 'Material processing control']
    },
    'control_microstructure_evolution': {
        'name': 'Control - Microstructure Evolution',
        'description': 'Optimal control of microstructure evolution with multi-field control',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': 'Multiple phase field equations + microstructure_control',
        'applications': ['Microstructure control', 'Evolution optimization', 'Material design control']
    }
} 