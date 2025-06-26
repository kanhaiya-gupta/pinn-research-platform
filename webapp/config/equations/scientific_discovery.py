"""
Scientific Discovery Equations
Equations for discovering new physical laws and data-driven scientific modeling.
"""

SCIENTIFIC_DISCOVERY_EQUATIONS_DICT = {
    'discovery_burgers': {
        'name': 'Discovery - Burgers',
        'description': 'Data-driven discovery of Burgers equation from observations',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': '∂u/∂t + u∂u/∂x = ν∂²u/∂x² (discovered)',
        'applications': ['Equation discovery', 'Model identification', 'Data-driven fluid dynamics']
    },
    'discovery_heat': {
        'name': 'Discovery - Heat',
        'description': 'Data-driven discovery of heat equation from temperature data',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': '∂u/∂t = α∂²u/∂x² (discovered)',
        'applications': ['Equation discovery', 'Thermal model identification', 'Data-driven heat transfer']
    },
    'discovery_wave': {
        'name': 'Discovery - Wave',
        'description': 'Data-driven discovery of wave equation from oscillation data',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': '∂²u/∂t² = c²∂²u/∂x² (discovered)',
        'applications': ['Equation discovery', 'Wave model identification', 'Data-driven acoustics']
    },
    'discovery_shm': {
        'name': 'Discovery - SHM',
        'description': 'Data-driven discovery of simple harmonic motion from time series',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': 'd²x/dt² + ω²x = 0 (discovered)',
        'applications': ['Equation discovery', 'Oscillator identification', 'Data-driven mechanics']
    },
    'discovery_helmholtz': {
        'name': 'Discovery - Helmholtz',
        'description': 'Data-driven discovery of Helmholtz equation from field data',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': '∇²u + k²u = 0 (discovered)',
        'applications': ['Equation discovery', 'Field model identification', 'Data-driven wave analysis']
    },
    'discovery_navier_stokes': {
        'name': 'Discovery - Navier-Stokes',
        'description': 'Data-driven discovery of Navier-Stokes equations from flow data',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': 'ρ(∂v/∂t + v·∇v) = -∇p + μ∇²v + f (discovered)',
        'applications': ['Equation discovery', 'Flow model identification', 'Data-driven fluid dynamics']
    },
    'discovery_schrodinger': {
        'name': 'Discovery - Schrödinger',
        'description': 'Data-driven discovery of Schrödinger equation from quantum data',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': 'iℏ∂ψ/∂t = Ĥψ (discovered)',
        'applications': ['Equation discovery', 'Quantum model identification', 'Data-driven quantum mechanics']
    },
    'discovery_maxwell': {
        'name': 'Discovery - Maxwell',
        'description': 'Data-driven discovery of Maxwell equations from EM data',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': '∇·E = ρ/ε₀, ∇×E = -∂B/∂t (discovered)',
        'applications': ['Equation discovery', 'EM model identification', 'Data-driven electromagnetism']
    },
    'discovery_heat_transfer': {
        'name': 'Discovery - Heat Transfer',
        'description': 'Data-driven discovery of heat transfer equation from thermal data',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': 'ρc_p ∂T/∂t = ∇·(k∇T) + Q (discovered)',
        'applications': ['Equation discovery', 'Thermal model identification', 'Data-driven heat transfer']
    },
    'discovery_elastic': {
        'name': 'Discovery - Elastic',
        'description': 'Data-driven discovery of elasticity equations from deformation data',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': '∇·σ = 0, σ = C:ε (discovered)',
        'applications': ['Equation discovery', 'Elastic model identification', 'Data-driven mechanics']
    },
    'discovery_phase_field': {
        'name': 'Discovery - Phase Field',
        'description': 'Data-driven discovery of phase field equation from microstructure data',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': '∂φ/∂t = -M δF/δφ (discovered)',
        'applications': ['Equation discovery', 'Phase model identification', 'Data-driven material science']
    },
    'discovery_reaction_diffusion': {
        'name': 'Discovery - Reaction-Diffusion',
        'description': 'Data-driven discovery of reaction-diffusion equation from concentration data',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': '∂u/∂t = D∇²u + f(u) (discovered)',
        'applications': ['Equation discovery', 'Chemical model identification', 'Data-driven reaction kinetics']
    },
    'discovery_poroelasticity': {
        'name': 'Discovery - Poroelasticity',
        'description': 'Data-driven discovery of poroelasticity equations from pressure and deformation data',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': '∇·σ = 0, ∂p/∂t = κ∇²p (discovered)',
        'applications': ['Equation discovery', 'Poroelastic model identification', 'Data-driven geomechanics']
    },
    'discovery_viscoelasticity': {
        'name': 'Discovery - Viscoelasticity',
        'description': 'Data-driven discovery of viscoelasticity equation from time-dependent data',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': 'σ + τ∂σ/∂t = E(ε + τ∂ε/∂t) (discovered)',
        'applications': ['Equation discovery', 'Viscoelastic model identification', 'Data-driven rheology']
    },
    'discovery_radiative_transfer': {
        'name': 'Discovery - Radiative Transfer',
        'description': 'Data-driven discovery of radiative transfer equation from radiation data',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': '∂I/∂s + (κ + σ)I = σ/4π ∫I dΩ (discovered)',
        'applications': ['Equation discovery', 'Radiation model identification', 'Data-driven atmospheric science']
    },
    'discovery_shallow_water': {
        'name': 'Discovery - Shallow Water',
        'description': 'Data-driven discovery of shallow water equations from water level data',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': '∂h/∂t + ∇·(hv) = 0 (discovered)',
        'applications': ['Equation discovery', 'Hydrodynamic model identification', 'Data-driven oceanography']
    },
    'discovery_magnetohydrodynamics': {
        'name': 'Discovery - Magnetohydrodynamics',
        'description': 'Data-driven discovery of MHD equations from plasma data',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': 'Navier-Stokes + Maxwell (discovered)',
        'applications': ['Equation discovery', 'Plasma model identification', 'Data-driven fusion science']
    },
    'discovery_thermoelasticity': {
        'name': 'Discovery - Thermoelasticity',
        'description': 'Data-driven discovery of thermoelasticity equations from coupled data',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': 'Heat equation + Elasticity (discovered)',
        'applications': ['Equation discovery', 'Thermoelastic model identification', 'Data-driven coupled systems']
    },
    'discovery_advection_diffusion': {
        'name': 'Discovery - Advection-Diffusion',
        'description': 'Data-driven discovery of advection-diffusion equation from transport data',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': '∂c/∂t + v·∇c = D∇²c (discovered)',
        'applications': ['Equation discovery', 'Transport model identification', 'Data-driven pollutant tracking']
    },
    'discovery_elastic_wave': {
        'name': 'Discovery - Elastic Wave',
        'description': 'Data-driven discovery of elastic wave equation from seismic data',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': 'ρ∂²u/∂t² = ∇·σ (discovered)',
        'applications': ['Equation discovery', 'Seismic model identification', 'Data-driven wave propagation']
    },
    'discovery_fluid_structure_interaction': {
        'name': 'Discovery - Fluid-Structure Interaction',
        'description': 'Data-driven discovery of FSI equations from coupled data',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': 'Navier-Stokes + Elasticity (discovered)',
        'applications': ['Equation discovery', 'FSI model identification', 'Data-driven coupled systems']
    },
    'discovery_electromagnetic_thermal': {
        'name': 'Discovery - Electromagnetic-Thermal',
        'description': 'Data-driven discovery of EM-thermal equations from coupled data',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': 'Maxwell + Heat equation (discovered)',
        'applications': ['Equation discovery', 'EM-thermal model identification', 'Data-driven coupled fields']
    },
    'discovery_biomechanical_transport': {
        'name': 'Discovery - Biomechanical Transport',
        'description': 'Data-driven discovery of biomechanical transport equations from biological data',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': 'Elasticity + Diffusion (discovered)',
        'applications': ['Equation discovery', 'Biomechanical model identification', 'Data-driven tissue modeling']
    },
    'discovery_geophysical_flow': {
        'name': 'Discovery - Geophysical Flow',
        'description': 'Data-driven discovery of geophysical flow equations from environmental data',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': 'Shallow water + Coriolis (discovered)',
        'applications': ['Equation discovery', 'Geophysical model identification', 'Data-driven earth science']
    },
    'discovery_atmospheric_oceanic': {
        'name': 'Discovery - Atmospheric-Oceanic',
        'description': 'Data-driven discovery of atmospheric-oceanic equations from climate data',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': 'Atmospheric + Oceanic equations (discovered)',
        'applications': ['Equation discovery', 'Climate model identification', 'Data-driven earth system science']
    },
    'discovery_nuclear_thermal': {
        'name': 'Discovery - Nuclear Thermal',
        'description': 'Data-driven discovery of nuclear thermal equations from reactor data',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': 'Heat equation + Nuclear source (discovered)',
        'applications': ['Equation discovery', 'Nuclear model identification', 'Data-driven reactor modeling']
    },
    'discovery_quantum_mechanical': {
        'name': 'Discovery - Quantum Mechanical',
        'description': 'Data-driven discovery of quantum mechanical equations from quantum data',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': 'Schrödinger equation (discovered)',
        'applications': ['Equation discovery', 'Quantum model identification', 'Data-driven quantum systems']
    },
    'discovery_phase_field_allen_cahn': {
        'name': 'Discovery - Allen-Cahn Phase Field',
        'description': 'Data-driven discovery of Allen-Cahn equation from microstructure data',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': '∂φ/∂t = -M δF/δφ (discovered)',
        'applications': ['Equation discovery', 'Phase field identification', 'Data-driven microstructure evolution']
    },
    'discovery_phase_field_cahn_hilliard': {
        'name': 'Discovery - Cahn-Hilliard Phase Field',
        'description': 'Data-driven discovery of Cahn-Hilliard equation from concentration data',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': '∂φ/∂t = ∇·(M∇(δF/δφ)) (discovered)',
        'applications': ['Equation discovery', 'Spinodal decomposition identification', 'Data-driven phase separation']
    },
    'discovery_solidification_stefan': {
        'name': 'Discovery - Stefan Problem',
        'description': 'Data-driven discovery of Stefan problem from temperature and phase boundary data',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': '∂T/∂t = α∇²T (discovered)',
        'applications': ['Equation discovery', 'Solidification identification', 'Data-driven phase change']
    },
    'discovery_grain_growth': {
        'name': 'Discovery - Grain Growth',
        'description': 'Data-driven discovery of grain growth equation from microstructure data',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': '∂R/∂t = Mγ/R (discovered)',
        'applications': ['Equation discovery', 'Grain growth identification', 'Data-driven microstructure evolution']
    },
    'discovery_sintering': {
        'name': 'Discovery - Sintering',
        'description': 'Data-driven discovery of sintering equation from densification data',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': '∂ρ/∂t = D∇²ρ (discovered)',
        'applications': ['Equation discovery', 'Sintering identification', 'Data-driven densification']
    },
    'discovery_laser_heat_source': {
        'name': 'Discovery - Laser Heat Source',
        'description': 'Data-driven discovery of laser heat source model from thermal data',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': 'Q(x, y, z, t) = Q₀ exp(-((x-x₀)²+(y-y₀)²)/2σ²) (discovered)',
        'applications': ['Equation discovery', 'Laser model identification', 'Data-driven AM processing']
    },
    'discovery_melt_pool_dynamics': {
        'name': 'Discovery - Melt Pool Dynamics',
        'description': 'Data-driven discovery of melt pool dynamics from fluid data',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': 'Navier-Stokes + Surface tension (discovered)',
        'applications': ['Equation discovery', 'Melt pool identification', 'Data-driven fluid dynamics']
    },
    'discovery_crystal_plasticity': {
        'name': 'Discovery - Crystal Plasticity',
        'description': 'Data-driven discovery of crystal plasticity from mechanical data',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': 'τ = τ₀ + αμb√ρ (discovered)',
        'applications': ['Equation discovery', 'Crystal plasticity identification', 'Data-driven mechanical behavior']
    },
    'discovery_diffusion_solids': {
        'name': 'Discovery - Diffusion in Solids',
        'description': 'Data-driven discovery of diffusion equation from concentration data',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': '∂c/∂t = ∇·(D∇c) (discovered)',
        'applications': ['Equation discovery', 'Diffusion identification', 'Data-driven material transport']
    },
    'discovery_precipitation_nucleation': {
        'name': 'Discovery - Precipitation and Nucleation',
        'description': 'Data-driven discovery of precipitation equation from nucleation data',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': 'J = J₀ exp(-ΔG*/kT) (discovered)',
        'applications': ['Equation discovery', 'Precipitation identification', 'Data-driven phase transformations']
    },
    'discovery_residual_stress': {
        'name': 'Discovery - Residual Stress',
        'description': 'Data-driven discovery of residual stress from deformation data',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': '∇·σ = 0, σ = C:(ε - εᵗ) (discovered)',
        'applications': ['Equation discovery', 'Residual stress identification', 'Data-driven thermal-mechanical']
    },
    'discovery_microstructure_evolution': {
        'name': 'Discovery - Microstructure Evolution',
        'description': 'Data-driven discovery of microstructure evolution from time-series data',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': 'Multiple phase field equations (discovered)',
        'applications': ['Equation discovery', 'Microstructure identification', 'Data-driven material transformation']
    },
    'discovery_additive_manufacturing': {
        'name': 'Discovery - Additive Manufacturing',
        'description': 'Data-driven discovery of AM process equations from process data',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': 'Laser + Melt pool + Solidification + Mechanics (discovered)',
        'applications': ['Equation discovery', 'AM process identification', 'Data-driven 3D printing']
    },
    'discovery_material_processing': {
        'name': 'Discovery - Material Processing',
        'description': 'Data-driven discovery of material processing equations from processing data',
        'icon': 'fas fa-flask',
        'color': '#e84393',
        'formula': 'Heat + Mechanics + Phase transformations (discovered)',
        'applications': ['Equation discovery', 'Processing identification', 'Data-driven manufacturing']
    }
} 