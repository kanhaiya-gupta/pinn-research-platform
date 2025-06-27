"""
Comprehensive equation definitions for all PINN purposes.
This file contains all supported equations, organized by purpose.
"""

# Forward Problems
FORWARD_PROBLEMS_EQUATIONS = [
    "burgers",
    "heat",
    "wave",
    "shm",
    "helmholtz",
    "navier_stokes",
    "schrodinger",
    "maxwell",
    "heat_transfer_phase_change",
    "stefan_condition",
    "navier_stokes_free_surface",
    "thermal_stress",
    "phase_field",
    "cahn_hilliard",
    "fick_second_law",
    "crystal_plasticity",
    "advection_diffusion",
    "shallow_water",
    "poroelasticity",
    "radiative_transfer",
    "reaction_diffusion",
    "elastic_wave",
    "magnetohydrodynamics",
    "viscoelasticity",
    "thermoelasticity",
    "fluid_structure_interaction",
    "electromagnetic_thermal",
    "biomechanical_transport",
    "geophysical_flow",
    "atmospheric_oceanic",
    "nuclear_thermal",
    "quantum_mechanical"
]

# Inverse Problems
INVERSE_PROBLEMS_EQUATIONS = [
    "inverse_burgers",
    "inverse_heat",
    "inverse_wave",
    "inverse_navier_stokes",
    "inverse_schrodinger",
    "inverse_helmholtz",
    "inverse_maxwell",
    "inverse_heat_transfer",
    "inverse_elastic",
    "inverse_phase_field",
    "inverse_reaction_diffusion",
    "inverse_poroelasticity",
    "inverse_viscoelasticity",
    "heat_transfer_phase_change_inverse",
    "stefan_condition_inverse",
    "navier_stokes_free_surface_inverse",
    "thermal_stress_inverse",
    "phase_field_inverse",
    "cahn_hilliard_inverse",
    "fick_second_law_inverse",
    "crystal_plasticity_inverse",
    "nernst_planck_inverse",
    "poroelasticity_inverse",
    "magnetohydrodynamics_inverse",
    "darcy_law_inverse",
    "reaction_kinetics_inverse"
]

# Data Assimilation
DATA_ASSIMILATION_EQUATIONS = [
    "data_assimilation_navier_stokes",
    "data_assimilation_heat",
    "data_assimilation_burgers",
    "data_assimilation_wave",
    "data_assimilation_shm",
    "data_assimilation_helmholtz",
    "data_assimilation_schrodinger",
    "data_assimilation_maxwell",
    "data_assimilation_heat_transfer",
    "data_assimilation_elastic",
    "data_assimilation_phase_field",
    "data_assimilation_reaction_diffusion",
    "data_assimilation_poroelasticity",
    "data_assimilation_viscoelasticity",
    "data_assimilation_thermoelasticity",
    "data_assimilation_radiative_transfer",
    "data_assimilation_shallow_water",
    "data_assimilation_magnetohydrodynamics",
    "data_assimilation_advection_diffusion",
    "data_assimilation_elastic_wave",
    "data_assimilation_fluid_structure_interaction",
    "data_assimilation_electromagnetic_thermal",
    "data_assimilation_biomechanical_transport",
    "data_assimilation_geophysical_flow",
    "data_assimilation_atmospheric_oceanic",
    "data_assimilation_nuclear_thermal",
    "data_assimilation_quantum_mechanical"
]

# Control & Optimization
CONTROL_OPTIMIZATION_EQUATIONS = [
    "linear_dynamics",
    "nonlinear_dynamics",
    "optimal_control_shm",
    "fluid_control",
    "thermal_control",
    "wave_control",
    "additive_manufacturing_control",
    "material_control",
    "hjb_equation",
    "multi_objective_control",
    "robust_control",
    "adaptive_control",
    "model_predictive_control",
    "optimal_control_heat",
    "optimal_control_wave",
    "optimal_control_fluid",
    "optimal_control_elastic",
    "optimal_control_phase_field",
    "optimal_control_reaction_diffusion",
    "optimal_control_poroelasticity",
    "optimal_control_viscoelasticity",
    "optimal_control_thermoelasticity",
    "optimal_control_advection_diffusion",
    "optimal_control_shallow_water",
    "optimal_control_magnetohydrodynamics",
    "optimal_control_radiative_transfer",
    "optimal_control_elastic_wave",
    "optimal_control_fluid_structure_interaction",
    "optimal_control_electromagnetic_thermal",
    "optimal_control_biomechanical_transport",
    "optimal_control_geophysical_flow",
    "optimal_control_atmospheric_oceanic",
    "optimal_control_nuclear_thermal",
    "optimal_control_quantum_mechanical"
]

# Simulation Efficiency
EFFICIENCY_EQUATIONS = [
    "efficient_burgers",
    "efficient_heat",
    "efficient_wave",
    "efficient_shm",
    "efficient_navier_stokes",
    "efficient_schrodinger",
    "efficient_helmholtz",
    "efficient_maxwell",
    "efficient_heat_transfer",
    "efficient_elastic",
    "efficient_phase_field",
    "efficient_reaction_diffusion",
    "efficient_poroelasticity",
    "efficient_viscoelasticity",
    "efficient_thermoelasticity",
    "efficient_advection_diffusion",
    "efficient_shallow_water",
    "efficient_magnetohydrodynamics",
    "efficient_radiative_transfer",
    "efficient_elastic_wave",
    "efficient_fluid_structure_interaction",
    "efficient_electromagnetic_thermal",
    "efficient_biomechanical_transport",
    "efficient_geophysical_flow",
    "efficient_atmospheric_oceanic",
    "efficient_nuclear_thermal",
    "efficient_quantum_mechanical"
]

# Generalization & Robustness
GENERALIZATION_EQUATIONS = [
    "generalized_burgers",
    "generalized_heat",
    "generalized_wave",
    "generalized_shm",
    "generalized_navier_stokes",
    "generalized_schrodinger",
    "generalized_helmholtz",
    "generalized_maxwell",
    "generalized_heat_transfer",
    "generalized_elastic",
    "generalized_phase_field",
    "generalized_reaction_diffusion",
    "generalized_poroelasticity",
    "generalized_viscoelasticity",
    "generalized_thermoelasticity",
    "generalized_advection_diffusion",
    "generalized_shallow_water",
    "generalized_magnetohydrodynamics",
    "generalized_radiative_transfer",
    "generalized_elastic_wave",
    "generalized_fluid_structure_interaction",
    "generalized_electromagnetic_thermal",
    "generalized_biomechanical_transport",
    "generalized_geophysical_flow",
    "generalized_atmospheric_oceanic",
    "generalized_nuclear_thermal",
    "generalized_quantum_mechanical"
]

# Multiphysics
MULTIPHYSICS_EQUATIONS = [
    "advection_diffusion",
    "shallow_water",
    "poroelasticity",
    "radiative_transfer",
    "reaction_diffusion",
    "elastic_wave",
    "magnetohydrodynamics",
    "viscoelasticity",
    "thermoelasticity",
    "fluid_structure_interaction",
    "electromagnetic_thermal",
    "biomechanical_transport",
    "geophysical_flow",
    "atmospheric_oceanic",
    "nuclear_thermal",
    "quantum_mechanical"
]

# Sparse/Noisy Data Learning
SPARSE_DATA_EQUATIONS = [
    "sparse_burgers",
    "sparse_heat",
    "sparse_wave",
    "sparse_shm",
    "sparse_helmholtz",
    "sparse_navier_stokes",
    "sparse_schrodinger",
    "sparse_maxwell",
    "sparse_heat_transfer",
    "sparse_elastic",
    "sparse_phase_field",
    "sparse_reaction_diffusion",
    "sparse_poroelasticity",
    "sparse_viscoelasticity",
    "sparse_radiative_transfer",
    "sparse_shallow_water",
    "sparse_magnetohydrodynamics",
    "sparse_thermoelasticity",
    "sparse_advection_diffusion",
    "sparse_elastic_wave",
    "sparse_fluid_structure_interaction",
    "sparse_electromagnetic_thermal",
    "sparse_biomechanical_transport",
    "sparse_geophysical_flow",
    "sparse_atmospheric_oceanic",
    "sparse_nuclear_thermal",
    "sparse_quantum_mechanical",
    "heat_transfer_phase_change_sparse",
    "stefan_condition_sparse",
    "navier_stokes_free_surface_sparse",
    "thermal_stress_sparse",
    "phase_field_sparse",
    "cahn_hilliard_sparse",
    "fick_second_law_sparse",
    "crystal_plasticity_sparse"
]

# Uncertainty Quantification
UNCERTAINTY_EQUATIONS = [
    "uncertainty_burgers",
    "uncertainty_heat",
    "uncertainty_wave",
    "uncertainty_shm",
    "uncertainty_navier_stokes",
    "uncertainty_schrodinger",
    "uncertainty_helmholtz",
    "uncertainty_maxwell",
    "uncertainty_heat_transfer",
    "uncertainty_elastic",
    "uncertainty_phase_field",
    "uncertainty_reaction_diffusion",
    "uncertainty_poroelasticity",
    "uncertainty_viscoelasticity",
    "uncertainty_thermoelasticity",
    "uncertainty_advection_diffusion",
    "uncertainty_shallow_water",
    "uncertainty_magnetohydrodynamics",
    "uncertainty_radiative_transfer",
    "uncertainty_elastic_wave",
    "uncertainty_fluid_structure_interaction",
    "uncertainty_electromagnetic_thermal",
    "uncertainty_biomechanical_transport",
    "uncertainty_geophysical_flow",
    "uncertainty_atmospheric_oceanic",
    "uncertainty_nuclear_thermal",
    "uncertainty_quantum_mechanical"
]

# Scientific Discovery
SCIENTIFIC_DISCOVERY_EQUATIONS = [
    "discovery_burgers",
    "discovery_heat",
    "discovery_wave",
    "discovery_shm",
    "discovery_navier_stokes",
    "discovery_schrodinger",
    "discovery_helmholtz",
    "discovery_maxwell",
    "discovery_heat_transfer",
    "discovery_elastic",
    "discovery_phase_field",
    "discovery_reaction_diffusion",
    "discovery_poroelasticity",
    "discovery_viscoelasticity",
    "discovery_thermoelasticity",
    "discovery_advection_diffusion",
    "discovery_shallow_water",
    "discovery_magnetohydrodynamics",
    "discovery_radiative_transfer",
    "discovery_elastic_wave",
    "discovery_fluid_structure_interaction",
    "discovery_electromagnetic_thermal",
    "discovery_biomechanical_transport",
    "discovery_geophysical_flow",
    "discovery_atmospheric_oceanic",
    "discovery_nuclear_thermal",
    "discovery_quantum_mechanical",
    "discovery_linear_dynamics",
    "discovery_nonlinear_dynamics",
    "discovery_optimal_control_shm",
    "discovery_fluid_control",
    "discovery_thermal_control",
    "discovery_wave_control",
    "discovery_additive_manufacturing_control",
    "discovery_material_control",
    "discovery_hjb_equation",
    "discovery_multi_objective_control"
]


# Comprehensive equation definitions organized by purpose
FORWARD_PROBLEMS_EQUATIONS_DICT = {
    'burgers': {
        'name': 'Burgers Equation',
        'description': 'Nonlinear partial differential equation modeling fluid dynamics and shock waves',
        'icon': 'fas fa-water',
        'color': '#3498db',
        'formula': '∂u/∂t + u∂u/∂x = ν∂²u/∂x²',
        'applications': ['Shock wave propagation', 'Traffic flow modeling', 'Gas dynamics']
    },
    'heat': {
        'name': 'Heat Equation',
        'description': 'Parabolic partial differential equation for heat conduction and diffusion',
        'icon': 'fas fa-fire',
        'color': '#e74c3c',
        'formula': '∂u/∂t = α∂²u/∂x²',
        'applications': ['Thermal analysis', 'Material processing', 'Climate modeling']
    },
    'wave': {
        'name': 'Wave Equation',
        'description': 'Hyperbolic partial differential equation for wave propagation phenomena',
        'icon': 'fas fa-wave-square',
        'color': '#9b59b6',
        'formula': '∂²u/∂t² = c²∂²u/∂x²',
        'applications': ['Acoustic waves', 'Electromagnetic waves', 'Seismic waves']
    },
    'shm': {
        'name': 'Simple Harmonic Motion',
        'description': 'Ordinary differential equation for oscillatory motion and vibrations',
        'icon': 'fas fa-sync',
        'color': '#f39c12',
        'formula': 'd²x/dt² + ω²x = 0',
        'applications': ['Mechanical vibrations', 'Electrical circuits', 'Molecular dynamics']
    },
    'helmholtz': {
        'name': 'Helmholtz Equation',
        'description': 'Elliptic partial differential equation for wave phenomena in steady state',
        'icon': 'fas fa-atom',
        'color': '#1abc9c',
        'formula': '∇²u + k²u = 0',
        'applications': ['Acoustic scattering', 'Electromagnetic fields', 'Quantum mechanics']
    },
    'navier_stokes': {
        'name': 'Navier-Stokes Equations',
        'description': 'System of PDEs describing fluid motion and turbulence',
        'icon': 'fas fa-wind',
        'color': '#34495e',
        'formula': 'ρ(∂v/∂t + v·∇v) = -∇p + μ∇²v + f',
        'applications': ['Aerodynamics', 'Oceanography', 'Blood flow modeling']
    },
    'schrodinger': {
        'name': 'Schrödinger Equation',
        'description': 'Quantum mechanical equation for particle wave functions',
        'icon': 'fas fa-quantum',
        'color': '#8e44ad',
        'formula': 'iℏ∂ψ/∂t = Ĥψ',
        'applications': ['Quantum chemistry', 'Material properties', 'Quantum computing']
    },
    'maxwell': {
        'name': 'Maxwell Equations',
        'description': 'System of PDEs describing electromagnetic fields',
        'icon': 'fas fa-bolt',
        'color': '#e67e22',
        'formula': '∇·E = ρ/ε₀, ∇×E = -∂B/∂t, ∇·B = 0, ∇×B = μ₀J + μ₀ε₀∂E/∂t',
        'applications': ['Antenna design', 'Optical systems', 'Electromagnetic compatibility']
    }
}

INVERSE_PROBLEMS_EQUATIONS_DICT = {
    'inverse_burgers': {
        'name': 'Inverse Burgers Equation',
        'description': 'Parameter identification for Burgers equation from observed data',
        'icon': 'fas fa-search',
        'color': '#e74c3c',
        'formula': '∂u/∂t + u∂u/∂x = ν∂²u/∂x² (ν unknown)',
        'applications': ['Viscosity identification', 'Shock wave analysis', 'Fluid parameter estimation']
    },
    'inverse_heat': {
        'name': 'Inverse Heat Equation',
        'description': 'Thermal conductivity identification from temperature measurements',
        'icon': 'fas fa-thermometer-half',
        'color': '#e74c3c',
        'formula': '∂u/∂t = α∂²u/∂x² (α unknown)',
        'applications': ['Material property identification', 'Thermal analysis', 'Heat transfer coefficient estimation']
    },
    'inverse_wave': {
        'name': 'Inverse Wave Equation',
        'description': 'Wave speed identification from wave propagation data',
        'icon': 'fas fa-wave-square',
        'color': '#e74c3c',
        'formula': '∂²u/∂t² = c²∂²u/∂x² (c unknown)',
        'applications': ['Wave speed estimation', 'Acoustic property identification', 'Seismic parameter calibration']
    },
    'inverse_navier_stokes': {
        'name': 'Inverse Navier-Stokes',
        'description': 'Fluid parameter identification from flow measurements',
        'icon': 'fas fa-wind',
        'color': '#e74c3c',
        'formula': 'ρ(∂v/∂t + v·∇v) = -∇p + μ∇²v + f (μ unknown)',
        'applications': ['Viscosity identification', 'Reynolds number estimation', 'Flow parameter calibration']
    },
    'inverse_schrodinger': {
        'name': 'Inverse Schrödinger',
        'description': 'Potential identification from quantum measurements',
        'icon': 'fas fa-quantum',
        'color': '#e74c3c',
        'formula': 'iℏ∂ψ/∂t = Ĥψ (Ĥ unknown)',
        'applications': ['Quantum system identification', 'Material property discovery', 'Potential reconstruction']
    },
    'inverse_helmholtz': {
        'name': 'Inverse Helmholtz',
        'description': 'Wave number identification from steady-state wave data',
        'icon': 'fas fa-atom',
        'color': '#e74c3c',
        'formula': '∇²u + k²u = 0 (k unknown)',
        'applications': ['Wave number estimation', 'Acoustic scattering analysis', 'Electromagnetic parameter identification']
    },
    'inverse_maxwell': {
        'name': 'Inverse Maxwell',
        'description': 'Electromagnetic parameter identification from field measurements',
        'icon': 'fas fa-bolt',
        'color': '#e74c3c',
        'formula': '∇·E = ρ/ε₀, ∇×E = -∂B/∂t (ε₀, μ₀ unknown)',
        'applications': ['Dielectric constant identification', 'Magnetic permeability estimation', 'Electromagnetic material properties']
    },
    'inverse_heat_transfer': {
        'name': 'Inverse Heat Transfer',
        'description': 'Thermal conductivity identification in complex heat transfer',
        'icon': 'fas fa-thermometer-half',
        'color': '#e74c3c',
        'formula': 'ρc_p ∂T/∂t = ∇·(k∇T) + Q (k unknown)',
        'applications': ['Thermal conductivity mapping', 'Heat transfer coefficient estimation', 'Material thermal properties']
    },
    'inverse_elastic': {
        'name': 'Inverse Elasticity',
        'description': 'Elastic modulus identification from deformation measurements',
        'icon': 'fas fa-compress-arrows-alt',
        'color': '#e74c3c',
        'formula': '∇·σ = 0, σ = C:ε (C unknown)',
        'applications': ['Young\'s modulus identification', 'Poisson ratio estimation', 'Elastic material properties']
    },
    'inverse_phase_field': {
        'name': 'Inverse Phase Field',
        'description': 'Interface energy identification from microstructure evolution',
        'icon': 'fas fa-atom',
        'color': '#e74c3c',
        'formula': '∂φ/∂t = -M δF/δφ (interface energy unknown)',
        'applications': ['Interface energy estimation', 'Microstructure parameter identification', 'Phase transformation kinetics']
    },
    'inverse_reaction_diffusion': {
        'name': 'Inverse Reaction-Diffusion',
        'description': 'Reaction rate identification from concentration measurements',
        'icon': 'fas fa-flask',
        'color': '#e74c3c',
        'formula': '∂u/∂t = D∇²u + f(u) (f unknown)',
        'applications': ['Reaction rate identification', 'Diffusion coefficient estimation', 'Chemical kinetics']
    },
    'inverse_poroelasticity': {
        'name': 'Inverse Poroelasticity',
        'description': 'Permeability identification from fluid-solid coupling',
        'icon': 'fas fa-tint',
        'color': '#e74c3c',
        'formula': '∇·σ = 0, ∂p/∂t = κ∇²p (κ unknown)',
        'applications': ['Permeability mapping', 'Poroelastic parameter identification', 'Geological property estimation']
    },
    'inverse_viscoelasticity': {
        'name': 'Inverse Viscoelasticity',
        'description': 'Viscoelastic parameter identification from time-dependent deformation',
        'icon': 'fas fa-clock',
        'color': '#e74c3c',
        'formula': 'σ + τ∂σ/∂t = E(ε + τ∂ε/∂t) (τ, E unknown)',
        'applications': ['Relaxation time estimation', 'Viscoelastic modulus identification', 'Polymer property characterization']
    },
    'heat_transfer_phase_change_inverse': {
        'name': 'Inverse Heat Transfer with Phase Change',
        'description': 'Latent heat identification in phase change processes',
        'icon': 'fas fa-thermometer-half',
        'color': '#e74c3c',
        'formula': 'ρc_p ∂T/∂t = ∇·(k∇T) - L ∂f_s/∂t (L unknown)',
        'applications': ['Latent heat estimation', 'Phase change parameter identification', 'Solidification kinetics']
    },
    'stefan_condition_inverse': {
        'name': 'Inverse Stefan Condition',
        'description': 'Interface velocity identification in moving boundary problems',
        'icon': 'fas fa-arrows-alt-h',
        'color': '#e74c3c',
        'formula': 'k_s ∇T_s·n - k_l ∇T_l·n = ρL v_n (v_n unknown)',
        'applications': ['Interface velocity estimation', 'Moving boundary identification', 'Phase front tracking']
    },
    'navier_stokes_free_surface_inverse': {
        'name': 'Inverse Navier-Stokes with Free Surface',
        'description': 'Surface tension identification in free surface flows',
        'icon': 'fas fa-water',
        'color': '#e74c3c',
        'formula': 'ρ(∂v/∂t + v·∇v) = -∇p + μ∇²v + σκn (σ unknown)',
        'applications': ['Surface tension estimation', 'Free surface parameter identification', 'Capillary effect analysis']
    },
    'thermal_stress_inverse': {
        'name': 'Inverse Thermal Stress',
        'description': 'Thermal expansion coefficient identification from stress measurements',
        'icon': 'fas fa-compress-arrows-alt',
        'color': '#e74c3c',
        'formula': 'σ = C:(ε - αΔT) (α unknown)',
        'applications': ['Thermal expansion coefficient estimation', 'Thermal stress parameter identification', 'Thermoelastic properties']
    },
    'phase_field_inverse': {
        'name': 'Inverse Phase Field (Interface Thickness)',
        'description': 'Interface thickness identification from phase field evolution',
        'icon': 'fas fa-atom',
        'color': '#e74c3c',
        'formula': '∂φ/∂t = -M δF/δφ (interface thickness unknown)',
        'applications': ['Interface thickness estimation', 'Phase field parameter identification', 'Microstructure evolution']
    },
    'cahn_hilliard_inverse': {
        'name': 'Inverse Cahn-Hilliard',
        'description': 'Interface energy identification in phase separation',
        'icon': 'fas fa-layer-group',
        'color': '#e74c3c',
        'formula': '∂c/∂t = ∇·(M∇μ), μ = δF/δc (interface energy unknown)',
        'applications': ['Interface energy estimation', 'Phase separation kinetics', 'Spinodal decomposition analysis']
    },
    'fick_second_law_inverse': {
        'name': 'Inverse Fick\'s Second Law',
        'description': 'Diffusion coefficient identification from concentration profiles',
        'icon': 'fas fa-exchange-alt',
        'color': '#e74c3c',
        'formula': '∂c/∂t = ∇·(D∇c) (D unknown)',
        'applications': ['Diffusion coefficient mapping', 'Mass transport parameter identification', 'Diffusion kinetics']
    },
    'crystal_plasticity_inverse': {
        'name': 'Inverse Crystal Plasticity',
        'description': 'Slip system parameter identification from plastic deformation',
        'icon': 'fas fa-cube',
        'color': '#e74c3c',
        'formula': 'ε̇^p = Σ_α γ̇^α m^α (slip parameters unknown)',
        'applications': ['Slip system identification', 'Crystal plasticity parameter estimation', 'Deformation mechanism analysis']
    },
    'nernst_planck_inverse': {
        'name': 'Inverse Nernst-Planck',
        'description': 'Ion mobility identification in electrochemical systems',
        'icon': 'fas fa-battery-half',
        'color': '#e74c3c',
        'formula': '∂c/∂t = ∇·(D∇c + μc∇φ) (μ unknown)',
        'applications': ['Ion mobility estimation', 'Electrochemical parameter identification', 'Battery material characterization']
    },
    'poroelasticity_inverse': {
        'name': 'Inverse Poroelasticity (Young\'s Modulus)',
        'description': 'Young\'s modulus identification in poroelastic materials',
        'icon': 'fas fa-tint',
        'color': '#e74c3c',
        'formula': '∇·σ = 0, σ = C:ε (C unknown)',
        'applications': ['Poroelastic modulus estimation', 'Geological material properties', 'Bone tissue characterization']
    },
    'magnetohydrodynamics_inverse': {
        'name': 'Inverse Magnetohydrodynamics',
        'description': 'Magnetic permeability identification in MHD flows',
        'icon': 'fas fa-magnet',
        'color': '#e74c3c',
        'formula': 'ρ(∂v/∂t + v·∇v) = -∇p + μ∇²v + J×B (μ_m unknown)',
        'applications': ['Magnetic permeability estimation', 'MHD parameter identification', 'Plasma property characterization']
    },
    'darcy_law_inverse': {
        'name': 'Inverse Darcy Law',
        'description': 'Permeability identification in porous media flow',
        'icon': 'fas fa-filter',
        'color': '#e74c3c',
        'formula': 'v = -k/μ ∇p (k unknown)',
        'applications': ['Permeability mapping', 'Porous media characterization', 'Groundwater flow analysis']
    },
    'reaction_kinetics_inverse': {
        'name': 'Inverse Reaction Kinetics',
        'description': 'Activation energy identification in chemical reactions',
        'icon': 'fas fa-flask',
        'color': '#e74c3c',
        'formula': 'dc/dt = k(T)c^n, k(T) = A exp(-E_a/RT) (E_a unknown)',
        'applications': ['Activation energy estimation', 'Reaction rate constant identification', 'Chemical kinetics analysis']
    }
}

DATA_ASSIMILATION_EQUATIONS_DICT = {
    'data_assimilation_navier_stokes': {
        'name': 'Data Assimilation - Navier-Stokes',
        'description': 'Combine flow observations with Navier-Stokes physics for improved state estimation',
        'icon': 'fas fa-sync',
        'color': '#9b59b6',
        'formula': 'ρ(∂v/∂t + v·∇v) = -∇p + μ∇²v + f + λ(obs - pred)',
        'applications': ['Weather forecasting', 'Ocean modeling', 'Atmospheric prediction']
    },
    'data_assimilation_heat': {
        'name': 'Data Assimilation - Heat',
        'description': 'Combine temperature observations with heat equation for thermal state estimation',
        'icon': 'fas fa-thermometer-half',
        'color': '#9b59b6',
        'formula': '∂u/∂t = α∂²u/∂x² + λ(obs - pred)',
        'applications': ['Climate modeling', 'Thermal monitoring', 'Heat transfer analysis']
    },
    'data_assimilation_burgers': {
        'name': 'Data Assimilation - Burgers',
        'description': 'Combine flow observations with Burgers physics',
        'icon': 'fas fa-sync',
        'color': '#9b59b6',
        'formula': '∂u/∂t + u∂u/∂x = ν∂²u/∂x² + λ(obs - pred)',
        'applications': ['Traffic flow prediction', 'Shock wave tracking', 'Fluid state estimation']
    },
    'data_assimilation_wave': {
        'name': 'Data Assimilation - Wave',
        'description': 'Combine wave observations with wave equation for improved wave field estimation',
        'icon': 'fas fa-wave-square',
        'color': '#9b59b6',
        'formula': '∂²u/∂t² = c²∂²u/∂x² + λ(obs - pred)',
        'applications': ['Seismic wave tracking', 'Acoustic field reconstruction', 'Wave propagation monitoring']
    },
    'data_assimilation_shm': {
        'name': 'Data Assimilation - SHM',
        'description': 'Combine oscillation observations with SHM physics',
        'icon': 'fas fa-sync',
        'color': '#9b59b6',
        'formula': 'd²x/dt² + ω²x = 0 + λ(obs - pred)',
        'applications': ['Vibration monitoring', 'Oscillator state estimation', 'Mechanical system tracking']
    },
    'data_assimilation_helmholtz': {
        'name': 'Data Assimilation - Helmholtz',
        'description': 'Combine steady-state wave observations with Helmholtz physics',
        'icon': 'fas fa-atom',
        'color': '#9b59b6',
        'formula': '∇²u + k²u = 0 + λ(obs - pred)',
        'applications': ['Acoustic field reconstruction', 'Electromagnetic field estimation', 'Steady-state wave analysis']
    },
    'data_assimilation_schrodinger': {
        'name': 'Data Assimilation - Schrödinger',
        'description': 'Combine quantum measurements with Schrödinger physics',
        'icon': 'fas fa-quantum',
        'color': '#9b59b6',
        'formula': 'iℏ∂ψ/∂t = Ĥψ + λ(obs - pred)',
        'applications': ['Quantum state estimation', 'Wave function reconstruction', 'Quantum system monitoring']
    },
    'data_assimilation_maxwell': {
        'name': 'Data Assimilation - Maxwell',
        'description': 'Combine electromagnetic field observations with Maxwell physics',
        'icon': 'fas fa-bolt',
        'color': '#9b59b6',
        'formula': '∇·E = ρ/ε₀ + λ(obs - pred), ∇×E = -∂B/∂t + λ(obs - pred)',
        'applications': ['Electromagnetic field reconstruction', 'Antenna pattern estimation', 'EM field monitoring']
    },
    'data_assimilation_heat_transfer': {
        'name': 'Data Assimilation - Heat Transfer',
        'description': 'Combine thermal observations with heat transfer physics',
        'icon': 'fas fa-thermometer-half',
        'color': '#9b59b6',
        'formula': 'ρc_p ∂T/∂t = ∇·(k∇T) + Q + λ(obs - pred)',
        'applications': ['Thermal field reconstruction', 'Heat transfer monitoring', 'Temperature field estimation']
    },
    'data_assimilation_elastic': {
        'name': 'Data Assimilation - Elasticity',
        'description': 'Combine deformation observations with elasticity physics',
        'icon': 'fas fa-compress-arrows-alt',
        'color': '#9b59b6',
        'formula': '∇·σ = 0 + λ(obs - pred), σ = C:ε + λ(obs - pred)',
        'applications': ['Stress field reconstruction', 'Deformation monitoring', 'Elastic field estimation']
    },
    'data_assimilation_phase_field': {
        'name': 'Data Assimilation - Phase Field',
        'description': 'Combine microstructure observations with phase field physics',
        'icon': 'fas fa-atom',
        'color': '#9b59b6',
        'formula': '∂φ/∂t = -M δF/δφ + λ(obs - pred)',
        'applications': ['Microstructure evolution tracking', 'Phase field reconstruction', 'Material evolution monitoring']
    },
    'data_assimilation_reaction_diffusion': {
        'name': 'Data Assimilation - Reaction-Diffusion',
        'description': 'Combine concentration observations with reaction-diffusion physics',
        'icon': 'fas fa-flask',
        'color': '#9b59b6',
        'formula': '∂u/∂t = D∇²u + f(u) + λ(obs - pred)',
        'applications': ['Chemical concentration tracking', 'Reaction front monitoring', 'Diffusion field reconstruction']
    },
    'data_assimilation_poroelasticity': {
        'name': 'Data Assimilation - Poroelasticity',
        'description': 'Combine fluid-solid observations with poroelastic physics',
        'icon': 'fas fa-tint',
        'color': '#9b59b6',
        'formula': '∇·σ = 0 + λ(obs - pred), ∂p/∂t = κ∇²p + λ(obs - pred)',
        'applications': ['Poroelastic field reconstruction', 'Fluid-solid coupling monitoring', 'Geological system tracking']
    },
    'data_assimilation_viscoelasticity': {
        'name': 'Data Assimilation - Viscoelasticity',
        'description': 'Combine time-dependent deformation observations with viscoelastic physics',
        'icon': 'fas fa-clock',
        'color': '#9b59b6',
        'formula': 'σ + τ∂σ/∂t = E(ε + τ∂ε/∂t) + λ(obs - pred)',
        'applications': ['Viscoelastic response tracking', 'Time-dependent deformation monitoring', 'Polymer behavior estimation']
    },
    'data_assimilation_thermoelasticity': {
        'name': 'Data Assimilation - Thermoelasticity',
        'description': 'Combine thermal-mechanical observations with thermoelastic physics',
        'icon': 'fas fa-thermometer-half',
        'color': '#9b59b6',
        'formula': 'Heat equation + Elasticity + λ(obs - pred)',
        'applications': ['Thermal stress monitoring', 'Thermoelastic field reconstruction', 'Coupled thermal-mechanical tracking']
    },
    'data_assimilation_radiative_transfer': {
        'name': 'Data Assimilation - Radiative Transfer',
        'description': 'Combine radiation observations with radiative transfer physics',
        'icon': 'fas fa-sun',
        'color': '#9b59b6',
        'formula': '∂I/∂s + (κ + σ)I = σ/4π ∫I dΩ + λ(obs - pred)',
        'applications': ['Radiation field reconstruction', 'Atmospheric radiation monitoring', 'Radiative transfer tracking']
    },
    'data_assimilation_shallow_water': {
        'name': 'Data Assimilation - Shallow Water',
        'description': 'Combine water level observations with shallow water physics',
        'icon': 'fas fa-water',
        'color': '#9b59b6',
        'formula': '∂h/∂t + ∇·(hv) = 0 + λ(obs - pred), ∂v/∂t + v·∇v = -g∇h + λ(obs - pred)',
        'applications': ['Tsunami tracking', 'Ocean surface monitoring', 'Shallow water wave prediction']
    },
    'data_assimilation_magnetohydrodynamics': {
        'name': 'Data Assimilation - Magnetohydrodynamics',
        'description': 'Combine MHD observations with magnetohydrodynamic physics',
        'icon': 'fas fa-magnet',
        'color': '#9b59b6',
        'formula': 'Navier-Stokes + Maxwell + λ(obs - pred)',
        'applications': ['Plasma state estimation', 'MHD field reconstruction', 'Fusion plasma monitoring']
    },
    'data_assimilation_advection_diffusion': {
        'name': 'Data Assimilation - Advection-Diffusion',
        'description': 'Combine transport observations with advection-diffusion physics',
        'icon': 'fas fa-wind',
        'color': '#9b59b6',
        'formula': '∂c/∂t + v·∇c = D∇²c + λ(obs - pred)',
        'applications': ['Pollutant tracking', 'Contaminant transport monitoring', 'Advection-diffusion field reconstruction']
    },
    'data_assimilation_elastic_wave': {
        'name': 'Data Assimilation - Elastic Wave',
        'description': 'Combine elastic wave observations with elastic wave physics',
        'icon': 'fas fa-wave-square',
        'color': '#9b59b6',
        'formula': 'ρ∂²u/∂t² = ∇·σ + λ(obs - pred), σ = C:ε + λ(obs - pred)',
        'applications': ['Seismic wave tracking', 'Elastic wave field reconstruction', 'Earthquake monitoring']
    },
    'data_assimilation_fluid_structure_interaction': {
        'name': 'Data Assimilation - Fluid-Structure Interaction',
        'description': 'Combine FSI observations with fluid-structure interaction physics',
        'icon': 'fas fa-cogs',
        'color': '#9b59b6',
        'formula': 'Navier-Stokes + Elasticity + λ(obs - pred)',
        'applications': ['FSI system monitoring', 'Coupled field reconstruction', 'Fluid-structure tracking']
    },
    'data_assimilation_electromagnetic_thermal': {
        'name': 'Data Assimilation - Electromagnetic-Thermal',
        'description': 'Combine EM-thermal observations with electromagnetic-thermal physics',
        'icon': 'fas fa-bolt',
        'color': '#9b59b6',
        'formula': 'Maxwell + Heat equation + λ(obs - pred)',
        'applications': ['EM-thermal field reconstruction', 'Coupled EM-thermal monitoring', 'Electromagnetic heating tracking']
    },
    'data_assimilation_biomechanical_transport': {
        'name': 'Data Assimilation - Biomechanical Transport',
        'description': 'Combine biomechanical observations with transport physics',
        'icon': 'fas fa-heartbeat',
        'color': '#9b59b6',
        'formula': 'Elasticity + Diffusion + λ(obs - pred)',
        'applications': ['Biological tissue monitoring', 'Biomechanical field reconstruction', 'Biological transport tracking']
    },
    'data_assimilation_geophysical_flow': {
        'name': 'Data Assimilation - Geophysical Flow',
        'description': 'Combine geophysical observations with flow physics',
        'icon': 'fas fa-mountain',
        'color': '#9b59b6',
        'formula': 'Shallow water + Coriolis + λ(obs - pred)',
        'applications': ['Ocean circulation monitoring', 'Atmospheric flow tracking', 'Geophysical field reconstruction']
    },
    'data_assimilation_atmospheric_oceanic': {
        'name': 'Data Assimilation - Atmospheric-Oceanic',
        'description': 'Combine atmospheric-oceanic observations with coupled physics',
        'icon': 'fas fa-cloud',
        'color': '#9b59b6',
        'formula': 'Atmospheric + Oceanic equations + λ(obs - pred)',
        'applications': ['Climate system monitoring', 'Atmospheric-oceanic coupling tracking', 'Weather-ocean prediction']
    },
    'data_assimilation_nuclear_thermal': {
        'name': 'Data Assimilation - Nuclear Thermal',
        'description': 'Combine nuclear-thermal observations with nuclear thermal physics',
        'icon': 'fas fa-atom',
        'color': '#9b59b6',
        'formula': 'Heat equation + Nuclear source + λ(obs - pred)',
        'applications': ['Nuclear reactor monitoring', 'Thermal field reconstruction', 'Nuclear thermal tracking']
    },
    'data_assimilation_quantum_mechanical': {
        'name': 'Data Assimilation - Quantum Mechanical',
        'description': 'Combine quantum observations with quantum mechanical physics',
        'icon': 'fas fa-quantum',
        'color': '#9b59b6',
        'formula': 'Schrödinger + Measurement + λ(obs - pred)',
        'applications': ['Quantum state reconstruction', 'Quantum system monitoring', 'Quantum measurement tracking']
    }
}

CONTROL_OPTIMIZATION_EQUATIONS_DICT = {
    'optimal_control_shm': {
        'name': 'Optimal Control - SHM',
        'description': 'Optimal control of simple harmonic oscillator with physics constraints',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': 'd²x/dt² + ω²x = u(t), J = ∫(x² + u²)dt',
        'applications': ['Vibration control', 'Robotic systems', 'Precision positioning']
    },
    'linear_dynamics': {
        'name': 'Linear Dynamics Control',
        'description': 'Optimal control of linear dynamical systems',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': 'ẋ = Ax + Bu, J = ∫(xᵀQx + uᵀRu)dt',
        'applications': ['Aerospace control', 'Process control', 'Robotic navigation']
    },
    'nonlinear_dynamics': {
        'name': 'Nonlinear Dynamics Control',
        'description': 'Optimal control of nonlinear dynamical systems',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': 'ẋ = f(x,u), J = ∫L(x,u)dt',
        'applications': ['Chemical processes', 'Biological systems', 'Complex mechanical systems']
    },
    'fluid_control': {
        'name': 'Fluid Control',
        'description': 'Optimal control of fluid flow systems',
        'icon': 'fas fa-wind',
        'color': '#8e44ad',
        'formula': 'Navier-Stokes + Control input, J = ∫(flow objective + control cost)dt',
        'applications': ['Aerodynamic control', 'Flow optimization', 'Drag reduction']
    },
    'thermal_control': {
        'name': 'Thermal Control',
        'description': 'Optimal control of thermal systems',
        'icon': 'fas fa-thermometer-half',
        'color': '#8e44ad',
        'formula': 'Heat equation + Heat source control, J = ∫(temperature objective + control cost)dt',
        'applications': ['Temperature regulation', 'Thermal management', 'Heat exchanger optimization']
    },
    'wave_control': {
        'name': 'Wave Control',
        'description': 'Optimal control of wave propagation',
        'icon': 'fas fa-wave-square',
        'color': '#8e44ad',
        'formula': 'Wave equation + Boundary control, J = ∫(wave objective + control cost)dt',
        'applications': ['Acoustic control', 'Wave focusing', 'Vibration suppression']
    },
    'additive_manufacturing_control': {
        'name': 'Additive Manufacturing Control',
        'description': 'Optimal control of additive manufacturing processes',
        'icon': 'fas fa-3d-modeling',
        'color': '#8e44ad',
        'formula': 'Heat transfer + Phase change + Process control, J = ∫(quality objective + control cost)dt',
        'applications': ['3D printing optimization', 'Laser power control', 'Build quality improvement']
    },
    'material_control': {
        'name': 'Material Control',
        'description': 'Optimal control of material processing',
        'icon': 'fas fa-cube',
        'color': '#8e44ad',
        'formula': 'Phase field + Processing control, J = ∫(microstructure objective + control cost)dt',
        'applications': ['Microstructure control', 'Material property optimization', 'Processing parameter tuning']
    },
    'hjb_equation': {
        'name': 'Hamilton-Jacobi-Bellman Equation',
        'description': 'Optimal control formulation for dynamic programming',
        'icon': 'fas fa-sliders-h',
        'color': '#8e44ad',
        'formula': '∂V/∂t + min_u{L(x,u) + ∇V·f(x,u)} = 0',
        'applications': ['Optimal control theory', 'Dynamic programming', 'Value function approximation']
    },
    'multi_objective_control': {
        'name': 'Multi-Objective Control',
        'description': 'Optimal control with multiple competing objectives',
        'icon': 'fas fa-balance-scale',
        'color': '#8e44ad',
        'formula': 'J = Σᵢ wᵢJᵢ, subject to physics constraints',
        'applications': ['Trade-off optimization', 'Multi-criteria control', 'Pareto optimal solutions']
    },
    'robust_control': {
        'name': 'Robust Control',
        'description': 'Control design for uncertain systems',
        'icon': 'fas fa-shield-alt',
        'color': '#8e44ad',
        'formula': 'ẋ = f(x,u,θ), θ ∈ Θ, J = max_θ ∫L(x,u)dt',
        'applications': ['Uncertainty handling', 'Robust performance', 'Worst-case optimization']
    },
    'adaptive_control': {
        'name': 'Adaptive Control',
        'description': 'Control with online parameter estimation',
        'icon': 'fas fa-sync',
        'color': '#8e44ad',
        'formula': 'ẋ = f(x,u,θ), θ̇ = adaptation law, u = control law(x,θ̂)',
        'applications': ['Parameter adaptation', 'Online learning', 'Self-tuning control']
    },
    'model_predictive_control': {
        'name': 'Model Predictive Control',
        'description': 'Receding horizon optimal control',
        'icon': 'fas fa-eye',
        'color': '#8e44ad',
        'formula': 'min_u ∫ₜᵗ⁺ᴴ L(x,u)dt, subject to constraints',
        'applications': ['Predictive control', 'Constraint handling', 'Real-time optimization']
    },
    'optimal_control_heat': {
        'name': 'Optimal Control - Heat',
        'description': 'Optimal control of heat conduction systems',
        'icon': 'fas fa-thermometer-half',
        'color': '#8e44ad',
        'formula': '∂T/∂t = α∇²T + Q_control, J = ∫(temperature objective + control cost)dt',
        'applications': ['Thermal system control', 'Heat exchanger optimization', 'Temperature regulation']
    },
    'optimal_control_wave': {
        'name': 'Optimal Control - Wave',
        'description': 'Optimal control of wave propagation systems',
        'icon': 'fas fa-wave-square',
        'color': '#8e44ad',
        'formula': '∂²u/∂t² = c²∇²u + f_control, J = ∫(wave objective + control cost)dt',
        'applications': ['Acoustic control', 'Wave focusing', 'Vibration suppression']
    },
    'optimal_control_fluid': {
        'name': 'Optimal Control - Fluid',
        'description': 'Optimal control of fluid dynamics systems',
        'icon': 'fas fa-wind',
        'color': '#8e44ad',
        'formula': 'Navier-Stokes + Control force, J = ∫(flow objective + control cost)dt',
        'applications': ['Flow control', 'Drag reduction', 'Mixing optimization']
    },
    'optimal_control_elastic': {
        'name': 'Optimal Control - Elastic',
        'description': 'Optimal control of elastic deformation systems',
        'icon': 'fas fa-compress-arrows-alt',
        'color': '#8e44ad',
        'formula': 'Elasticity + Control force, J = ∫(deformation objective + control cost)dt',
        'applications': ['Deformation control', 'Stress optimization', 'Shape control']
    },
    'optimal_control_phase_field': {
        'name': 'Optimal Control - Phase Field',
        'description': 'Optimal control of phase field evolution',
        'icon': 'fas fa-atom',
        'color': '#8e44ad',
        'formula': '∂φ/∂t = -M δF/δφ + u_control, J = ∫(microstructure objective + control cost)dt',
        'applications': ['Microstructure control', 'Phase transformation control', 'Grain growth optimization']
    },
    'optimal_control_reaction_diffusion': {
        'name': 'Optimal Control - Reaction-Diffusion',
        'description': 'Optimal control of chemical reaction-diffusion systems',
        'icon': 'fas fa-flask',
        'color': '#8e44ad',
        'formula': '∂c/∂t = D∇²c + f(c) + u_control, J = ∫(concentration objective + control cost)dt',
        'applications': ['Chemical process control', 'Reaction optimization', 'Concentration control']
    },
    'optimal_control_poroelasticity': {
        'name': 'Optimal Control - Poroelasticity',
        'description': 'Optimal control of fluid-solid coupling systems',
        'icon': 'fas fa-tint',
        'color': '#8e44ad',
        'formula': 'Poroelasticity + Control pressure, J = ∫(deformation objective + control cost)dt',
        'applications': ['Geological control', 'Bone tissue control', 'Porous media optimization']
    },
    'optimal_control_viscoelasticity': {
        'name': 'Optimal Control - Viscoelasticity',
        'description': 'Optimal control of viscoelastic material systems',
        'icon': 'fas fa-clock',
        'color': '#8e44ad',
        'formula': 'Viscoelasticity + Control stress, J = ∫(deformation objective + control cost)dt',
        'applications': ['Polymer processing control', 'Viscoelastic response optimization', 'Time-dependent control']
    },
    'optimal_control_thermoelasticity': {
        'name': 'Optimal Control - Thermoelasticity',
        'description': 'Optimal control of coupled thermal-mechanical systems',
        'icon': 'fas fa-thermometer-half',
        'color': '#8e44ad',
        'formula': 'Thermoelasticity + Control heat source, J = ∫(thermal-mechanical objective + control cost)dt',
        'applications': ['Thermal stress control', 'Thermoelastic optimization', 'Coupled system control']
    },
    'optimal_control_advection_diffusion': {
        'name': 'Optimal Control - Advection-Diffusion',
        'description': 'Optimal control of transport phenomena',
        'icon': 'fas fa-wind',
        'color': '#8e44ad',
        'formula': '∂c/∂t + v·∇c = D∇²c + u_control, J = ∫(concentration objective + control cost)dt',
        'applications': ['Pollutant control', 'Contaminant transport optimization', 'Mixing control']
    },
    'optimal_control_shallow_water': {
        'name': 'Optimal Control - Shallow Water',
        'description': 'Optimal control of shallow water wave systems',
        'icon': 'fas fa-water',
        'color': '#8e44ad',
        'formula': 'Shallow water + Control source, J = ∫(wave height objective + control cost)dt',
        'applications': ['Tsunami control', 'Ocean wave optimization', 'Water level control']
    },
    'optimal_control_magnetohydrodynamics': {
        'name': 'Optimal Control - Magnetohydrodynamics',
        'description': 'Optimal control of MHD systems',
        'icon': 'fas fa-magnet',
        'color': '#8e44ad',
        'formula': 'MHD + Control magnetic field, J = ∫(plasma objective + control cost)dt',
        'applications': ['Plasma control', 'Fusion reactor optimization', 'MHD flow control']
    },
    'optimal_control_radiative_transfer': {
        'name': 'Optimal Control - Radiative Transfer',
        'description': 'Optimal control of radiation transport',
        'icon': 'fas fa-sun',
        'color': '#8e44ad',
        'formula': 'Radiative transfer + Control source, J = ∫(radiation objective + control cost)dt',
        'applications': ['Radiation control', 'Atmospheric radiation optimization', 'Radiative heating control']
    },
    'optimal_control_elastic_wave': {
        'name': 'Optimal Control - Elastic Wave',
        'description': 'Optimal control of elastic wave propagation',
        'icon': 'fas fa-wave-square',
        'color': '#8e44ad',
        'formula': 'Elastic wave + Control force, J = ∫(wave objective + control cost)dt',
        'applications': ['Seismic wave control', 'Elastic wave focusing', 'Vibration control']
    },
    'optimal_control_fluid_structure_interaction': {
        'name': 'Optimal Control - Fluid-Structure Interaction',
        'description': 'Optimal control of FSI systems',
        'icon': 'fas fa-cogs',
        'color': '#8e44ad',
        'formula': 'FSI + Control inputs, J = ∫(coupled objective + control cost)dt',
        'applications': ['Aircraft control', 'Biomechanical control', 'FSI system optimization']
    },
    'optimal_control_electromagnetic_thermal': {
        'name': 'Optimal Control - Electromagnetic-Thermal',
        'description': 'Optimal control of EM-thermal systems',
        'icon': 'fas fa-bolt',
        'color': '#8e44ad',
        'formula': 'EM-thermal + Control fields, J = ∫(coupled objective + control cost)dt',
        'applications': ['EM heating control', 'Thermal field optimization', 'Coupled EM-thermal control']
    },
    'optimal_control_biomechanical_transport': {
        'name': 'Optimal Control - Biomechanical Transport',
        'description': 'Optimal control of biological transport systems',
        'icon': 'fas fa-heartbeat',
        'color': '#8e44ad',
        'formula': 'Biomechanical transport + Control inputs, J = ∫(biological objective + control cost)dt',
        'applications': ['Drug delivery optimization', 'Biological transport control', 'Tissue engineering']
    },
    'optimal_control_geophysical_flow': {
        'name': 'Optimal Control - Geophysical Flow',
        'description': 'Optimal control of geophysical flow systems',
        'icon': 'fas fa-mountain',
        'color': '#8e44ad',
        'formula': 'Geophysical flow + Control sources, J = ∫(flow objective + control cost)dt',
        'applications': ['Ocean circulation control', 'Atmospheric flow optimization', 'Geophysical system control']
    },
    'optimal_control_atmospheric_oceanic': {
        'name': 'Optimal Control - Atmospheric-Oceanic',
        'description': 'Optimal control of coupled atmospheric-oceanic systems',
        'icon': 'fas fa-cloud',
        'color': '#8e44ad',
        'formula': 'Atmospheric-oceanic + Control inputs, J = ∫(climate objective + control cost)dt',
        'applications': ['Climate system control', 'Weather modification', 'Ocean-atmosphere optimization']
    },
    'optimal_control_nuclear_thermal': {
        'name': 'Optimal Control - Nuclear Thermal',
        'description': 'Optimal control of nuclear thermal systems',
        'icon': 'fas fa-atom',
        'color': '#8e44ad',
        'formula': 'Nuclear thermal + Control sources, J = ∫(nuclear objective + control cost)dt',
        'applications': ['Nuclear reactor control', 'Thermal field optimization', 'Nuclear thermal management']
    },
    'optimal_control_quantum_mechanical': {
        'name': 'Optimal Control - Quantum Mechanical',
        'description': 'Optimal control of quantum systems',
        'icon': 'fas fa-quantum',
        'color': '#8e44ad',
        'formula': 'Schrödinger + Control potential, J = ∫(quantum objective + control cost)dt',
        'applications': ['Quantum state control', 'Quantum gate optimization', 'Quantum system manipulation']
    }
}

MULTIPHYSICS_EQUATIONS_DICT = {
    'advection_diffusion': {
        'name': 'Advection-Diffusion Equation',
        'description': 'Combined transport and diffusion phenomena',
        'icon': 'fas fa-cogs',
        'color': '#1abc9c',
        'formula': '∂c/∂t + v·∇c = D∇²c',
        'applications': ['Pollutant transport', 'Heat transfer', 'Chemical reactions']
    },
    'fluid_structure_interaction': {
        'name': 'Fluid-Structure Interaction',
        'description': 'Coupled fluid flow and structural deformation',
        'icon': 'fas fa-cogs',
        'color': '#1abc9c',
        'formula': 'Navier-Stokes + Elasticity equations',
        'applications': ['Aircraft design', 'Biomechanics', 'Offshore structures']
    },
    'thermoelasticity': {
        'name': 'Thermoelasticity',
        'description': 'Coupled thermal and mechanical deformation',
        'icon': 'fas fa-cogs',
        'color': '#1abc9c',
        'formula': 'Heat equation + Elasticity with thermal strain',
        'applications': ['Thermal stress analysis', 'Electronic packaging', 'Nuclear reactors']
    },
    'magnetohydrodynamics': {
        'name': 'Magnetohydrodynamics',
        'description': 'Coupled fluid dynamics and electromagnetic fields',
        'icon': 'fas fa-cogs',
        'color': '#1abc9c',
        'formula': 'Navier-Stokes + Maxwell equations',
        'applications': ['Plasma physics', 'Fusion reactors', 'Astrophysics']
    }
}

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
    }
}

UNCERTAINTY_EQUATIONS_DICT = {
    'uncertainty_burgers': {
        'name': 'Uncertainty - Burgers',
        'description': 'Probabilistic Burgers equation with parameter uncertainties',
        'icon': 'fas fa-chart-area',
        'color': '#e67e22',
        'formula': '∂u/∂t + u∂u/∂x = ν∂²u/∂x² (ν ~ N(μ,σ))',
        'applications': ['Confidence intervals', 'Risk assessment', 'Robust design']
    },
    'uncertainty_heat': {
        'name': 'Uncertainty - Heat',
        'description': 'Probabilistic heat equation with uncertain thermal properties',
        'icon': 'fas fa-chart-area',
        'color': '#e67e22',
        'formula': '∂u/∂t = α∂²u/∂x² (α ~ N(μ,σ))',
        'applications': ['Thermal uncertainty', 'Material property variation', 'Process variability']
    },
    'uncertainty_navier_stokes': {
        'name': 'Uncertainty - Navier-Stokes',
        'description': 'Probabilistic fluid dynamics with uncertain parameters',
        'icon': 'fas fa-chart-area',
        'color': '#e67e22',
        'formula': 'ρ(∂v/∂t + v·∇v) = -∇p + μ∇²v + f (μ ~ N(μ,σ))',
        'applications': ['Flow uncertainty', 'Turbulence modeling', 'Risk assessment']
    }
}

SCIENTIFIC_DISCOVERY_EQUATIONS_DICT = {
    'discovery_burgers': {
        'name': 'Discovery - Burgers',
        'description': 'Discover unknown terms in Burgers equation from data',
        'icon': 'fas fa-microscope',
        'color': '#34495e',
        'formula': '∂u/∂t + u∂u/∂x = f(u,∇u,∇²u) (f unknown)',
        'applications': ['New physics discovery', 'Model validation', 'Constitutive law identification']
    },
    'discovery_heat': {
        'name': 'Discovery - Heat',
        'description': 'Discover unknown heat transfer mechanisms',
        'icon': 'fas fa-microscope',
        'color': '#34495e',
        'formula': '∂u/∂t = f(u,∇u,∇²u) (f unknown)',
        'applications': ['Novel heat transfer', 'Material property discovery', 'Thermal mechanism identification']
    },
    'discovery_navier_stokes': {
        'name': 'Discovery - Navier-Stokes',
        'description': 'Discover unknown terms in fluid dynamics',
        'icon': 'fas fa-microscope',
        'color': '#34495e',
        'formula': 'ρ(∂v/∂t + v·∇v) = f(v,∇v,∇²v) (f unknown)',
        'applications': ['Turbulence modeling', 'New fluid laws', 'Complex flow physics']
    }
}

EFFICIENCY_EQUATIONS_DICT = {
    'efficient_burgers': {
        'name': 'Efficient - Burgers',
        'description': 'Fast surrogate model for Burgers equation',
        'icon': 'fas fa-tachometer-alt',
        'color': '#27ae60',
        'formula': '∂u/∂t + u∂u/∂x = ν∂²u/∂x² (optimized)',
        'applications': ['Real-time simulation', 'Fast prototyping', 'Optimization loops']
    },
    'efficient_heat': {
        'name': 'Efficient - Heat',
        'description': 'Fast surrogate model for heat equation',
        'icon': 'fas fa-tachometer-alt',
        'color': '#27ae60',
        'formula': '∂u/∂t = α∂²u/∂x² (optimized)',
        'applications': ['Real-time thermal analysis', 'Fast design iteration', 'Optimization']
    },
    'efficient_navier_stokes': {
        'name': 'Efficient - Navier-Stokes',
        'description': 'Fast surrogate model for fluid dynamics',
        'icon': 'fas fa-tachometer-alt',
        'color': '#27ae60',
        'formula': 'ρ(∂v/∂t + v·∇v) = -∇p + μ∇²v + f (optimized)',
        'applications': ['Real-time flow simulation', 'Fast aerodynamic analysis', 'Optimization']
    }
}

GENERALIZATION_EQUATIONS_DICT = {
    'generalized_burgers': {
        'name': 'Generalized - Burgers',
        'description': 'Burgers equation with domain generalization',
        'icon': 'fas fa-shield-alt',
        'color': '#16a085',
        'formula': '∂u/∂t + u∂u/∂x = ν∂²u/∂x² (domain shift)',
        'applications': ['Out-of-distribution prediction', 'Domain adaptation', 'Robust modeling']
    },
    'generalized_heat': {
        'name': 'Generalized - Heat',
        'description': 'Heat equation with domain generalization',
        'icon': 'fas fa-shield-alt',
        'color': '#16a085',
        'formula': '∂u/∂t = α∂²u/∂x² (domain shift)',
        'applications': ['Cross-domain thermal analysis', 'Robust heat transfer', 'Generalization']
    },
    'generalized_navier_stokes': {
        'name': 'Generalized - Navier-Stokes',
        'description': 'Navier-Stokes with domain generalization',
        'icon': 'fas fa-shield-alt',
        'color': '#16a085',
        'formula': 'ρ(∂v/∂t + v·∇v) = -∇p + μ∇²v + f (domain shift)',
        'applications': ['Cross-domain flow prediction', 'Robust fluid modeling', 'Generalization']
    }
}

# Master dictionary combining all purposes
SUPPORTED_EQUATIONS = {
    **FORWARD_PROBLEMS_EQUATIONS_DICT,
    **INVERSE_PROBLEMS_EQUATIONS_DICT,
    **DATA_ASSIMILATION_EQUATIONS_DICT,
    **CONTROL_OPTIMIZATION_EQUATIONS_DICT,
    **MULTIPHYSICS_EQUATIONS_DICT,
    **SPARSE_DATA_EQUATIONS_DICT,
    **UNCERTAINTY_EQUATIONS_DICT,
    **SCIENTIFIC_DISCOVERY_EQUATIONS_DICT,
    **EFFICIENCY_EQUATIONS_DICT,
    **GENERALIZATION_EQUATIONS_DICT
}

# Master list of all equations by purpose
ALL_PURPOSE_EQUATIONS = {
    'forward_problems': FORWARD_PROBLEMS_EQUATIONS_DICT,
    'inverse_problems': INVERSE_PROBLEMS_EQUATIONS_DICT,
    'data_assimilation': DATA_ASSIMILATION_EQUATIONS_DICT,
    'control_optimization': CONTROL_OPTIMIZATION_EQUATIONS_DICT,
    'efficiency': EFFICIENCY_EQUATIONS_DICT,
    'generalization': GENERALIZATION_EQUATIONS_DICT,
    'multiphysics': MULTIPHYSICS_EQUATIONS_DICT,
    'sparse_data': SPARSE_DATA_EQUATIONS_DICT,
    'uncertainty': UNCERTAINTY_EQUATIONS_DICT,
    'scientific_discovery': SCIENTIFIC_DISCOVERY_EQUATIONS_DICT
}
