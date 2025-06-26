"""
Comprehensive parameter definitions for all equations in the PINN platform.
This file contains default parameters for all supported equations organized by purpose.
"""

# Forward Problems Parameters
FORWARD_PROBLEMS_PARAMETERS = {
    "burgers": {
        "nu": 0.01, "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "heat": {
        "alpha": 0.1, "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "wave": {
        "c": 1.0, "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "shm": {
        "omega": 1.0, "nt": 1000,
        "t_min": 0.0, "t_max": 10.0
    },
    "helmholtz": {
        "k": 1.0, "nx": 100, "ny": 100,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0
    },
    "navier_stokes": {
        "reynolds": 100.0, "nx": 128, "ny": 128, "nt": 50,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "schrodinger": {
        "hbar": 1.0, "mass": 1.0, "nx": 256, "nt": 100,
        "x_min": -5.0, "x_max": 5.0, "t_min": 0.0, "t_max": 1.0
    },
    "maxwell": {
        "epsilon": 1.0, "mu": 1.0, "nx": 128, "ny": 128, "nt": 50,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "heat_transfer_phase_change": {
        "alpha": 0.1, "latent_heat": 334000.0, "melting_temp": 273.15,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "stefan_condition": {
        "thermal_conductivity_solid": 2.0, "thermal_conductivity_liquid": 0.6,
        "latent_heat": 334000.0, "density": 1000.0,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "navier_stokes_free_surface": {
        "reynolds": 100.0, "surface_tension": 0.072, "gravity": 9.81,
        "nx": 128, "ny": 128, "nt": 50,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "thermal_stress": {
        "youngs_modulus": 200e9, "poisson_ratio": 0.3, "thermal_expansion": 12e-6,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "phase_field": {
        "mobility": 1.0, "interface_thickness": 0.01,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "cahn_hilliard": {
        "mobility": 1.0, "interface_energy": 1.0,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "fick_second_law": {
        "diffusion_coefficient": 1e-9,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "crystal_plasticity": {
        "shear_modulus": 80e9, "burgers_vector": 2.5e-10,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "advection_diffusion": {
        "velocity": 1.0, "diffusion_coefficient": 0.1, "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "shallow_water": {
        "gravity": 9.81, "friction_coefficient": 0.01, "nx": 256, "ny": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "poroelasticity": {
        "permeability": 1e-12, "youngs_modulus": 1e9, "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "radiative_transfer": {
        "absorption_coefficient": 1.0, "scattering_coefficient": 0.1, "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "reaction_diffusion": {
        "diffusion_coefficient_u": 1.0, "diffusion_coefficient_v": 0.5,
        "reaction_rate_a": 1.0, "reaction_rate_b": 1.0, "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "elastic_wave": {
        "youngs_modulus": 200e9, "poisson_ratio": 0.3, "density": 2700.0, "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "magnetohydrodynamics": {
        "density": 1000.0, "viscosity": 1e-3, "magnetic_permeability": 1.26e-6,
        "electrical_conductivity": 1e6, "nx": 128, "ny": 128, "nt": 50,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "viscoelasticity": {
        "viscosity": 1e3, "relaxation_time": 1.0, "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "thermoelasticity": {
        "youngs_modulus": 200e9, "poisson_ratio": 0.3, "thermal_expansion": 12e-6,
        "thermal_conductivity": 50.0, "specific_heat": 500.0, "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "fluid_structure_interaction": {
        "fluid_density": 1000.0, "fluid_viscosity": 1e-3, "solid_density": 2700.0,
        "youngs_modulus": 200e9, "poisson_ratio": 0.3, "nx": 128, "ny": 128, "nt": 50,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "electromagnetic_thermal": {
        "electrical_conductivity": 1e6, "thermal_conductivity": 50.0, "specific_heat": 500.0,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "biomechanical_transport": {
        "permeability": 1e-12, "diffusion_coefficient": 1e-9, "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "geophysical_flow": {
        "gravity": 9.81, "friction_coefficient": 0.01, "nx": 256, "ny": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "atmospheric_oceanic": {
        "gravity": 9.81, "coriolis_parameter": 1e-4, "nx": 256, "ny": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "nuclear_thermal": {
        "thermal_conductivity": 50.0, "specific_heat": 500.0, "nuclear_heat": 1e6, "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "quantum_mechanical": {
        "hbar": 1.0, "mass": 1.0, "potential": 1.0, "nx": 256, "nt": 100,
        "x_min": -5.0, "x_max": 5.0, "t_min": 0.0, "t_max": 1.0
    }
}

# Inverse Problems Parameters
INVERSE_PROBLEMS_PARAMETERS = {
    "inverse_burgers": {
        "nu_initial": 0.01, "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "inverse_heat": {
        "alpha_initial": 0.1, "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "inverse_wave": {
        "c_initial": 1.0, "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "inverse_navier_stokes": {
        "reynolds_initial": 100.0, "nx": 128, "ny": 128, "nt": 50,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "inverse_schrodinger": {
        "potential_initial": 1.0, "nx": 256, "nt": 100,
        "x_min": -5.0, "x_max": 5.0, "t_min": 0.0, "t_max": 1.0
    },
    "inverse_helmholtz": {
        "k_initial": 1.0, "nx": 100, "ny": 100,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0
    },
    "inverse_maxwell": {
        "epsilon_initial": 1.0, "mu_initial": 1.0, "nx": 128, "ny": 128, "nt": 50,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "inverse_heat_transfer": {
        "thermal_conductivity_initial": 50.0, "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "inverse_elastic": {
        "youngs_modulus_initial": 200e9, "poisson_ratio_initial": 0.3,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "inverse_phase_field": {
        "mobility_initial": 1.0, "interface_energy_initial": 1.0,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "inverse_reaction_diffusion": {
        "diffusion_coefficient_u_initial": 1.0, "diffusion_coefficient_v_initial": 0.5,
        "reaction_rate_a_initial": 1.0, "reaction_rate_b_initial": 1.0,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "inverse_poroelasticity": {
        "permeability_initial": 1e-12, "youngs_modulus_initial": 1e9,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "inverse_viscoelasticity": {
        "viscosity_initial": 1e3, "relaxation_time_initial": 1.0,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "heat_transfer_phase_change_inverse": {
        "alpha_initial": 0.1, "latent_heat_initial": 334000.0, "melting_temp_initial": 273.15,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "stefan_condition_inverse": {
        "thermal_conductivity_solid_initial": 2.0, "thermal_conductivity_liquid_initial": 0.6,
        "latent_heat_initial": 334000.0, "density_initial": 1000.0,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "navier_stokes_free_surface_inverse": {
        "reynolds_initial": 100.0, "surface_tension_initial": 0.072, "gravity_initial": 9.81,
        "nx": 128, "ny": 128, "nt": 50,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "thermal_stress_inverse": {
        "youngs_modulus_initial": 200e9, "poisson_ratio_initial": 0.3, "thermal_expansion_initial": 12e-6,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "phase_field_inverse": {
        "mobility_initial": 1.0, "interface_thickness_initial": 0.01,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "cahn_hilliard_inverse": {
        "mobility_initial": 1.0, "interface_energy_initial": 1.0,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "fick_second_law_inverse": {
        "diffusion_coefficient_initial": 1e-9,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "crystal_plasticity_inverse": {
        "shear_modulus_initial": 80e9, "burgers_vector_initial": 2.5e-10,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "nernst_planck_inverse": {
        "diffusion_coefficient_initial": 1e-9, "mobility_initial": 1e-9,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "poroelasticity_inverse": {
        "permeability_initial": 1e-12, "youngs_modulus_initial": 1e9,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "magnetohydrodynamics_inverse": {
        "density_initial": 1000.0, "viscosity_initial": 1e-3, "magnetic_permeability_initial": 1.26e-6,
        "electrical_conductivity_initial": 1e6, "nx": 128, "ny": 128, "nt": 50,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "darcy_law_inverse": {
        "permeability_initial": 1e-12, "viscosity_initial": 1e-3,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "reaction_kinetics_inverse": {
        "reaction_rate_initial": 1.0, "activation_energy_initial": 50000.0,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    }
}

# Data Assimilation Parameters
DATA_ASSIMILATION_PARAMETERS = {
    "data_assimilation_navier_stokes": {
        "reynolds": 100.0, "observation_noise": 0.01, "nx": 128, "ny": 128, "nt": 50,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "data_assimilation_heat": {
        "alpha": 0.1, "observation_noise": 0.01, "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "data_assimilation_burgers": {
        "nu": 0.01, "observation_noise": 0.01, "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "data_assimilation_wave": {
        "c": 1.0, "observation_noise": 0.01, "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "data_assimilation_shm": {
        "omega": 1.0, "observation_noise": 0.01, "nt": 1000,
        "t_min": 0.0, "t_max": 10.0
    },
    "data_assimilation_helmholtz": {
        "k": 1.0, "observation_noise": 0.01, "nx": 100, "ny": 100,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0
    },
    "data_assimilation_schrodinger": {
        "hbar": 1.0, "mass": 1.0, "observation_noise": 0.01, "nx": 256, "nt": 100,
        "x_min": -5.0, "x_max": 5.0, "t_min": 0.0, "t_max": 1.0
    },
    "data_assimilation_maxwell": {
        "epsilon": 1.0, "mu": 1.0, "observation_noise": 0.01, "nx": 128, "ny": 128, "nt": 50,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "data_assimilation_heat_transfer": {
        "alpha": 0.1, "observation_noise": 0.01, "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "data_assimilation_elastic": {
        "youngs_modulus": 200e9, "poisson_ratio": 0.3, "observation_noise": 0.01,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "data_assimilation_phase_field": {
        "mobility": 1.0, "interface_energy": 1.0, "observation_noise": 0.01,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "data_assimilation_reaction_diffusion": {
        "diffusion_coefficient_u": 1.0, "diffusion_coefficient_v": 0.5,
        "reaction_rate_a": 1.0, "reaction_rate_b": 1.0, "observation_noise": 0.01,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "data_assimilation_poroelasticity": {
        "permeability": 1e-12, "youngs_modulus": 1e9, "observation_noise": 0.01,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "data_assimilation_viscoelasticity": {
        "viscosity": 1e3, "relaxation_time": 1.0, "observation_noise": 0.01,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "data_assimilation_thermoelasticity": {
        "youngs_modulus": 200e9, "poisson_ratio": 0.3, "thermal_expansion": 12e-6,
        "thermal_conductivity": 50.0, "specific_heat": 500.0, "observation_noise": 0.01,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "data_assimilation_radiative_transfer": {
        "absorption_coefficient": 1.0, "scattering_coefficient": 0.1, "observation_noise": 0.01,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "data_assimilation_shallow_water": {
        "gravity": 9.81, "friction_coefficient": 0.01, "observation_noise": 0.01,
        "nx": 256, "ny": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "data_assimilation_magnetohydrodynamics": {
        "density": 1000.0, "viscosity": 1e-3, "magnetic_permeability": 1.26e-6,
        "electrical_conductivity": 1e6, "observation_noise": 0.01,
        "nx": 128, "ny": 128, "nt": 50,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    }
}

# Control & Optimization Parameters
CONTROL_OPTIMIZATION_PARAMETERS = {
    "linear_dynamics": {
        "A11": 1.0, "A12": 0.0, "A21": 0.0, "A22": 1.0,
        "B1": 1.0, "B2": 1.0,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "nonlinear_dynamics": {
        "alpha": 1.0, "beta": 1.0, "gamma": 1.0,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "optimal_control_shm": {
        "omega": 1.0, "Q": 1.0, "R": 0.1,
        "nt": 1000, "t_min": 0.0, "t_max": 10.0
    },
    "fluid_control": {
        "reynolds": 100.0, "control_strength": 1.0,
        "nx": 128, "ny": 128, "nt": 50,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "thermal_control": {
        "alpha": 0.1, "control_heat": 1.0,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "wave_control": {
        "c": 1.0, "control_force": 1.0,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "additive_manufacturing_control": {
        "alpha": 0.1, "laser_power": 1000.0, "latent_heat": 334000.0,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "material_control": {
        "mobility": 1.0, "control_field": 1.0,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "hjb_equation": {
        "discount_factor": 0.95, "cost_weight": 1.0,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "multi_objective_control": {
        "weight1": 0.5, "weight2": 0.5, "weight3": 0.0,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "robust_control": {
        "uncertainty_level": 0.1, "robustness_weight": 1.0,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "adaptive_control": {
        "adaptation_rate": 0.01, "parameter_uncertainty": 0.1,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "model_predictive_control": {
        "prediction_horizon": 10, "control_horizon": 5,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "optimal_control_heat": {
        "alpha": 0.1, "control_strength": 1.0, "cost_weight": 1.0,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "optimal_control_wave": {
        "c": 1.0, "control_strength": 1.0, "cost_weight": 1.0,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "optimal_control_fluid": {
        "reynolds": 100.0, "control_strength": 1.0, "cost_weight": 1.0,
        "nx": 128, "ny": 128, "nt": 50,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    }
}

# Multiphysics Parameters
MULTIPHYSICS_PARAMETERS = {
    "advection_diffusion": {
        "velocity": 1.0, "diffusion_coefficient": 0.1,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "shallow_water": {
        "gravity": 9.81, "friction_coefficient": 0.01,
        "nx": 256, "ny": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "poroelasticity": {
        "youngs_modulus": 1e9, "poisson_ratio": 0.3, "permeability": 1e-12,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "radiative_transfer": {
        "absorption_coefficient": 1.0, "scattering_coefficient": 0.1,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "reaction_diffusion": {
        "diffusion_coefficient_u": 1.0, "diffusion_coefficient_v": 0.5,
        "reaction_rate_a": 1.0, "reaction_rate_b": 1.0,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "elastic_wave": {
        "density": 2700.0, "youngs_modulus": 70e9, "poisson_ratio": 0.3,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "magnetohydrodynamics": {
        "density": 1000.0, "viscosity": 1e-3, "magnetic_permeability": 1.26e-6,
        "electrical_conductivity": 1e6,
        "nx": 128, "ny": 128, "nt": 50,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "viscoelasticity": {
        "youngs_modulus": 1e9, "viscosity": 1e3, "relaxation_time": 1.0,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "thermoelasticity": {
        "youngs_modulus": 200e9, "poisson_ratio": 0.3, "thermal_expansion": 12e-6,
        "thermal_conductivity": 50.0, "specific_heat": 500.0,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "fluid_structure_interaction": {
        "fluid_density": 1000.0, "fluid_viscosity": 1e-3, "solid_density": 2700.0,
        "youngs_modulus": 70e9, "poisson_ratio": 0.3,
        "nx": 128, "ny": 128, "nt": 50,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "electromagnetic_thermal": {
        "electrical_conductivity": 1e6, "thermal_conductivity": 50.0,
        "specific_heat": 500.0, "magnetic_permeability": 1.26e-6,
        "nx": 128, "ny": 128, "nt": 50,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "biomechanical_transport": {
        "youngs_modulus": 1e6, "poisson_ratio": 0.3, "diffusion_coefficient": 1e-9,
        "permeability": 1e-12,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "geophysical_flow": {
        "gravity": 9.81, "friction_coefficient": 0.01, "porosity": 0.3,
        "permeability": 1e-12,
        "nx": 256, "ny": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "atmospheric_oceanic": {
        "atmospheric_density": 1.225, "ocean_density": 1025.0,
        "wind_speed": 10.0, "ocean_current": 1.0,
        "nx": 256, "ny": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "nuclear_thermal": {
        "thermal_conductivity": 50.0, "specific_heat": 500.0,
        "nuclear_heat_source": 1e6, "neutron_flux": 1e14,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "quantum_mechanical": {
        "hbar": 1.0, "mass": 1.0, "potential_strength": 1.0,
        "nx": 256, "nt": 100,
        "x_min": -5.0, "x_max": 5.0, "t_min": 0.0, "t_max": 1.0
    }
}

# Sparse Data Parameters
SPARSE_DATA_PARAMETERS = {
    "sparse_burgers": {
        "nu": 0.01, "sparse_ratio": 0.1, "noise_level": 0.01,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "sparse_heat": {
        "alpha": 0.1, "sparse_ratio": 0.1, "noise_level": 0.01,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "sparse_wave": {
        "c": 1.0, "sparse_ratio": 0.1, "noise_level": 0.01,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "sparse_navier_stokes": {
        "reynolds": 100.0, "sparse_ratio": 0.1, "noise_level": 0.01,
        "nx": 128, "ny": 128, "nt": 50,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "sparse_schrodinger": {
        "hbar": 1.0, "mass": 1.0, "sparse_ratio": 0.1, "noise_level": 0.01,
        "nx": 256, "nt": 100,
        "x_min": -5.0, "x_max": 5.0, "t_min": 0.0, "t_max": 1.0
    },
    "sparse_helmholtz": {
        "k": 1.0, "sparse_ratio": 0.1, "noise_level": 0.01,
        "nx": 100, "ny": 100,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0
    },
    "sparse_maxwell": {
        "epsilon": 1.0, "mu": 1.0, "sparse_ratio": 0.1, "noise_level": 0.01,
        "nx": 128, "ny": 128, "nt": 50,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "sparse_heat_transfer": {
        "alpha": 0.1, "sparse_ratio": 0.1, "noise_level": 0.01,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "sparse_elastic": {
        "youngs_modulus": 200e9, "poisson_ratio": 0.3, "sparse_ratio": 0.1, "noise_level": 0.01,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "sparse_phase_field": {
        "mobility": 1.0, "interface_energy": 1.0, "sparse_ratio": 0.1, "noise_level": 0.01,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "sparse_reaction_diffusion": {
        "diffusion_coefficient_u": 1.0, "diffusion_coefficient_v": 0.5,
        "reaction_rate_a": 1.0, "reaction_rate_b": 1.0,
        "diffusion_u_std": 0.1, "diffusion_v_std": 0.05,
        "reaction_a_std": 0.1, "reaction_b_std": 0.1,
        "sparse_ratio": 0.1, "noise_level": 0.01,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "sparse_poroelasticity": {
        "permeability": 1e-12, "youngs_modulus": 1e9, "sparse_ratio": 0.1, "noise_level": 0.01,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "sparse_viscoelasticity": {
        "viscosity": 1e3, "relaxation_time": 1.0, "sparse_ratio": 0.1, "noise_level": 0.01,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "sparse_thermoelasticity": {
        "youngs_modulus": 200e9, "poisson_ratio": 0.3, "thermal_expansion": 12e-6,
        "thermal_conductivity": 50.0, "specific_heat": 500.0, "sparse_ratio": 0.1, "noise_level": 0.01,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "sparse_advection_diffusion": {
        "velocity": 1.0, "diffusion_coefficient": 0.1, "velocity_std": 0.1, "diffusion_std": 0.01,
        "sparse_ratio": 0.1, "noise_level": 0.01,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "sparse_shallow_water": {
        "gravity": 9.81, "friction_coefficient": 0.01, "gravity_std": 0.1, "friction_std": 0.001,
        "sparse_ratio": 0.1, "noise_level": 0.01,
        "nx": 256, "ny": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "sparse_magnetohydrodynamics": {
        "density": 1000.0, "viscosity": 1e-3, "magnetic_permeability": 1.26e-6,
        "electrical_conductivity": 1e6, "sparse_ratio": 0.1, "noise_level": 0.01,
        "density_std": 100.0, "viscosity_std": 1e-4, "magnetic_std": 1.26e-7,
        "electrical_std": 1e5,
        "nx": 128, "ny": 128, "nt": 50,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "sparse_shm": {
        "omega": 1.0, "sparse_ratio": 0.1, "noise_level": 0.01,
        "nt": 1000, "t_min": 0.0, "t_max": 10.0
    },
    "sparse_radiative_transfer": {
        "absorption_coefficient": 1.0, "scattering_coefficient": 0.1, "sparse_ratio": 0.1, "noise_level": 0.01,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    }
}


# Uncertainty Quantification Parameters
UNCERTAINTY_PARAMETERS = {
    "uncertainty_burgers": {
        "nu": 0.01, "nu_std": 0.001, "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "uncertainty_heat": {
        "alpha": 0.1, "alpha_std": 0.01, "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "uncertainty_wave": {
        "c": 1.0, "c_std": 0.1, "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "uncertainty_navier_stokes": {
        "reynolds": 100.0, "reynolds_std": 10.0, "nx": 128, "ny": 128, "nt": 50,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "uncertainty_schrodinger": {
        "hbar": 1.0, "mass": 1.0, "hbar_std": 0.1, "mass_std": 0.1,
        "nx": 256, "nt": 100,
        "x_min": -5.0, "x_max": 5.0, "t_min": 0.0, "t_max": 1.0
    },
    "uncertainty_helmholtz": {
        "k": 1.0, "k_std": 0.1, "nx": 100, "ny": 100,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0
    },
    "uncertainty_maxwell": {
        "epsilon": 1.0, "mu": 1.0, "epsilon_std": 0.1, "mu_std": 0.1,
        "nx": 128, "ny": 128, "nt": 50,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "uncertainty_heat_transfer": {
        "alpha": 0.1, "alpha_std": 0.01, "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "uncertainty_elastic": {
        "youngs_modulus": 200e9, "poisson_ratio": 0.3, "youngs_std": 20e9, "poisson_std": 0.03,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "uncertainty_phase_field": {
        "mobility": 1.0, "interface_energy": 1.0, "mobility_std": 0.1, "interface_std": 0.1,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "uncertainty_reaction_diffusion": {
        "diffusion_coefficient_u": 1.0, "diffusion_coefficient_v": 0.5,
        "reaction_rate_a": 1.0, "reaction_rate_b": 1.0,
        "diffusion_u_std": 0.1, "diffusion_v_std": 0.05,
        "reaction_a_std": 0.1, "reaction_b_std": 0.1,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "uncertainty_poroelasticity": {
        "permeability": 1e-12, "youngs_modulus": 1e9, "permeability_std": 1e-13, "youngs_std": 1e8,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "uncertainty_viscoelasticity": {
        "viscosity": 1e3, "relaxation_time": 1.0, "viscosity_std": 1e2, "relaxation_std": 0.1,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "uncertainty_thermoelasticity": {
        "youngs_modulus": 200e9, "poisson_ratio": 0.3, "thermal_expansion": 12e-6,
        "thermal_conductivity": 50.0, "specific_heat": 500.0,
        "youngs_std": 20e9, "poisson_std": 0.03, "thermal_expansion_std": 1e-6,
        "thermal_conductivity_std": 5.0, "specific_heat_std": 50.0,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "uncertainty_advection_diffusion": {
        "velocity": 1.0, "diffusion_coefficient": 0.1, "velocity_std": 0.1, "diffusion_std": 0.01,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "uncertainty_shallow_water": {
        "gravity": 9.81, "friction_coefficient": 0.01, "gravity_std": 0.1, "friction_std": 0.001,
        "nx": 256, "ny": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "uncertainty_magnetohydrodynamics": {
        "density": 1000.0, "viscosity": 1e-3, "magnetic_permeability": 1.26e-6,
        "electrical_conductivity": 1e6,
        "density_std": 100.0, "viscosity_std": 1e-4, "magnetic_std": 1.26e-7,
        "electrical_std": 1e5,
        "nx": 128, "ny": 128, "nt": 50,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "uncertainty_shm": {
        "omega": 1.0, "omega_std": 0.1, "nt": 1000,
        "t_min": 0.0, "t_max": 10.0
    },
    "uncertainty_radiative_transfer": {
        "absorption_coefficient": 1.0, "scattering_coefficient": 0.1,
        "absorption_std": 0.1, "scattering_std": 0.01,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    }
}

# Scientific Discovery Parameters
SCIENTIFIC_DISCOVERY_PARAMETERS = {
    "discovery_burgers": {
        "nu": 0.01, "unknown_coefficient": 1.0, "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "discovery_heat": {
        "alpha": 0.1, "unknown_coefficient": 1.0, "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "discovery_wave": {
        "c": 1.0, "unknown_coefficient": 1.0, "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "discovery_navier_stokes": {
        "reynolds": 100.0, "unknown_coefficient": 1.0, "nx": 128, "ny": 128, "nt": 50,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "discovery_schrodinger": {
        "hbar": 1.0, "mass": 1.0, "unknown_coefficient": 1.0,
        "nx": 256, "nt": 100,
        "x_min": -5.0, "x_max": 5.0, "t_min": 0.0, "t_max": 1.0
    },
    "discovery_helmholtz": {
        "k": 1.0, "unknown_coefficient": 1.0, "nx": 100, "ny": 100,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0
    },
    "discovery_maxwell": {
        "epsilon": 1.0, "mu": 1.0, "unknown_coefficient": 1.0,
        "nx": 128, "ny": 128, "nt": 50,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "discovery_heat_transfer": {
        "alpha": 0.1, "unknown_coefficient": 1.0, "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "discovery_elastic": {
        "youngs_modulus": 200e9, "poisson_ratio": 0.3, "unknown_coefficient": 1.0,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "discovery_phase_field": {
        "mobility": 1.0, "interface_energy": 1.0, "unknown_coefficient": 1.0,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "discovery_reaction_diffusion": {
        "diffusion_coefficient_u": 1.0, "diffusion_coefficient_v": 0.5,
        "reaction_rate_a": 1.0, "reaction_rate_b": 1.0, "unknown_coefficient": 1.0,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "discovery_poroelasticity": {
        "permeability": 1e-12, "youngs_modulus": 1e9, "unknown_coefficient": 1.0,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "discovery_viscoelasticity": {
        "viscosity": 1e3, "relaxation_time": 1.0, "unknown_coefficient": 1.0,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "discovery_thermoelasticity": {
        "youngs_modulus": 200e9, "poisson_ratio": 0.3, "thermal_expansion": 12e-6,
        "thermal_conductivity": 50.0, "specific_heat": 500.0, "unknown_coefficient": 1.0,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "discovery_advection_diffusion": {
        "velocity": 1.0, "diffusion_coefficient": 0.1, "unknown_coefficient": 1.0,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "discovery_shallow_water": {
        "gravity": 9.81, "friction_coefficient": 0.01, "unknown_coefficient": 1.0,
        "nx": 256, "ny": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "discovery_magnetohydrodynamics": {
        "density": 1000.0, "viscosity": 1e-3, "magnetic_permeability": 1.26e-6,
        "electrical_conductivity": 1e6, "unknown_coefficient": 1.0,
        "nx": 128, "ny": 128, "nt": 50,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "discovery_linear_dynamics": {
        "A11": 1.0, "A12": 0.0, "A21": 0.0, "A22": 1.0, "unknown_coefficient": 1.0,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "discovery_nonlinear_dynamics": {
        "alpha": 1.0, "beta": 1.0, "gamma": 1.0, "unknown_coefficient": 1.0,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "discovery_optimal_control_shm": {
        "omega": 1.0, "Q": 1.0, "R": 0.1, "unknown_coefficient": 1.0,
        "nt": 1000, "t_min": 0.0, "t_max": 10.0
    },
    "discovery_fluid_control": {
        "reynolds": 100.0, "control_strength": 1.0, "unknown_coefficient": 1.0,
        "nx": 128, "ny": 128, "nt": 50,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "discovery_thermal_control": {
        "alpha": 0.1, "control_heat": 1.0, "unknown_coefficient": 1.0,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "discovery_wave_control": {
        "c": 1.0, "control_force": 1.0, "unknown_coefficient": 1.0,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "discovery_additive_manufacturing_control": {
        "alpha": 0.1, "laser_power": 1000.0, "latent_heat": 334000.0, "unknown_coefficient": 1.0,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "discovery_material_control": {
        "mobility": 1.0, "control_field": 1.0, "unknown_coefficient": 1.0,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "discovery_hjb_equation": {
        "discount_factor": 0.95, "cost_weight": 1.0, "unknown_coefficient": 1.0,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "discovery_multi_objective_control": {
        "weight1": 0.5, "weight2": 0.5, "weight3": 0.0, "unknown_coefficient": 1.0,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "discovery_shm": {
        "omega": 1.0, "unknown_coefficient": 1.0, "nt": 1000,
        "t_min": 0.0, "t_max": 10.0
    },
    "discovery_helmholtz": {
        "k": 1.0, "unknown_coefficient": 1.0, "nx": 100, "ny": 100,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0
    },
    "discovery_maxwell": {
        "epsilon": 1.0, "mu": 1.0, "unknown_coefficient": 1.0,
        "nx": 128, "ny": 128, "nt": 50,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "discovery_radiative_transfer": {
        "absorption_coefficient": 1.0, "scattering_coefficient": 0.1, "unknown_coefficient": 1.0,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    }
}

# Efficiency Parameters
EFFICIENCY_PARAMETERS = {
    "efficient_burgers": {
        "nu": 0.01, "adaptive_sampling": True, "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "efficient_heat": {
        "alpha": 0.1, "adaptive_sampling": True, "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "efficient_wave": {
        "c": 1.0, "adaptive_sampling": True, "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "efficient_navier_stokes": {
        "reynolds": 100.0, "adaptive_sampling": True, "nx": 128, "ny": 128, "nt": 50,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "efficient_schrodinger": {
        "hbar": 1.0, "mass": 1.0, "adaptive_sampling": True,
        "nx": 256, "nt": 100,
        "x_min": -5.0, "x_max": 5.0, "t_min": 0.0, "t_max": 1.0
    },
    "efficient_helmholtz": {
        "k": 1.0, "adaptive_sampling": True, "nx": 100, "ny": 100,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0
    },
    "efficient_maxwell": {
        "epsilon": 1.0, "mu": 1.0, "adaptive_sampling": True,
        "nx": 128, "ny": 128, "nt": 50,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "efficient_heat_transfer": {
        "alpha": 0.1, "adaptive_sampling": True, "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "efficient_elastic": {
        "youngs_modulus": 200e9, "poisson_ratio": 0.3, "adaptive_sampling": True,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "efficient_phase_field": {
        "mobility": 1.0, "interface_energy": 1.0, "adaptive_sampling": True,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "efficient_reaction_diffusion": {
        "diffusion_coefficient_u": 1.0, "diffusion_coefficient_v": 0.5,
        "reaction_rate_a": 1.0, "reaction_rate_b": 1.0, "adaptive_sampling": True,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "efficient_poroelasticity": {
        "permeability": 1e-12, "youngs_modulus": 1e9, "adaptive_sampling": True,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "efficient_viscoelasticity": {
        "viscosity": 1e3, "relaxation_time": 1.0, "adaptive_sampling": True,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "efficient_thermoelasticity": {
        "youngs_modulus": 200e9, "poisson_ratio": 0.3, "thermal_expansion": 12e-6,
        "thermal_conductivity": 50.0, "specific_heat": 500.0, "adaptive_sampling": True,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "efficient_advection_diffusion": {
        "velocity": 1.0, "diffusion_coefficient": 0.1, "adaptive_sampling": True,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "efficient_shallow_water": {
        "gravity": 9.81, "friction_coefficient": 0.01, "adaptive_sampling": True,
        "nx": 256, "ny": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "efficient_magnetohydrodynamics": {
        "density": 1000.0, "viscosity": 1e-3, "magnetic_permeability": 1.26e-6,
        "electrical_conductivity": 1e6, "adaptive_sampling": True,
        "nx": 128, "ny": 128, "nt": 50,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "efficient_shm": {
        "omega": 1.0, "adaptive_sampling": True, "nt": 1000,
        "t_min": 0.0, "t_max": 10.0
    },
    "efficient_radiative_transfer": {
        "absorption_coefficient": 1.0, "scattering_coefficient": 0.1, "adaptive_sampling": True,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    }
}

# Generalization Parameters
GENERALIZATION_PARAMETERS = {
    "generalized_burgers": {
        "nu": 0.01, "domain_shift": 0.1, "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "generalized_heat": {
        "alpha": 0.1, "domain_shift": 0.1, "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "generalized_wave": {
        "c": 1.0, "domain_shift": 0.1, "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "generalized_navier_stokes": {
        "reynolds": 100.0, "domain_shift": 0.1, "nx": 128, "ny": 128, "nt": 50,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "generalized_schrodinger": {
        "hbar": 1.0, "mass": 1.0, "domain_shift": 0.1,
        "nx": 256, "nt": 100,
        "x_min": -5.0, "x_max": 5.0, "t_min": 0.0, "t_max": 1.0
    },
    "generalized_helmholtz": {
        "k": 1.0, "domain_shift": 0.1, "nx": 100, "ny": 100,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0
    },
    "generalized_maxwell": {
        "epsilon": 1.0, "mu": 1.0, "domain_shift": 0.1,
        "nx": 128, "ny": 128, "nt": 50,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "generalized_heat_transfer": {
        "alpha": 0.1, "domain_shift": 0.1, "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "generalized_elastic": {
        "youngs_modulus": 200e9, "poisson_ratio": 0.3, "domain_shift": 0.1,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "generalized_phase_field": {
        "mobility": 1.0, "interface_energy": 1.0, "domain_shift": 0.1,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "generalized_reaction_diffusion": {
        "diffusion_coefficient_u": 1.0, "diffusion_coefficient_v": 0.5,
        "reaction_rate_a": 1.0, "reaction_rate_b": 1.0, "domain_shift": 0.1,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "generalized_poroelasticity": {
        "permeability": 1e-12, "youngs_modulus": 1e9, "domain_shift": 0.1,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "generalized_viscoelasticity": {
        "viscosity": 1e3, "relaxation_time": 1.0, "domain_shift": 0.1,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "generalized_thermoelasticity": {
        "youngs_modulus": 200e9, "poisson_ratio": 0.3, "thermal_expansion": 12e-6,
        "thermal_conductivity": 50.0, "specific_heat": 500.0, "domain_shift": 0.1,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "generalized_advection_diffusion": {
        "velocity": 1.0, "diffusion_coefficient": 0.1, "domain_shift": 0.1,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    },
    "generalized_shallow_water": {
        "gravity": 9.81, "friction_coefficient": 0.01, "domain_shift": 0.1,
        "nx": 256, "ny": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "generalized_magnetohydrodynamics": {
        "density": 1000.0, "viscosity": 1e-3, "magnetic_permeability": 1.26e-6,
        "electrical_conductivity": 1e6, "domain_shift": 0.1,
        "nx": 128, "ny": 128, "nt": 50,
        "x_min": 0.0, "x_max": 1.0, "y_min": 0.0, "y_max": 1.0,
        "t_min": 0.0, "t_max": 1.0
    },
    "generalized_shm": {
        "omega": 1.0, "domain_shift": 0.1, "nt": 1000,
        "t_min": 0.0, "t_max": 10.0
    },
    "generalized_radiative_transfer": {
        "absorption_coefficient": 1.0, "scattering_coefficient": 0.1, "domain_shift": 0.1,
        "nx": 256, "nt": 100,
        "x_min": 0.0, "x_max": 1.0, "t_min": 0.0, "t_max": 1.0
    }
} 

# Purpose-specific parameter mappings
PURPOSE_PARAMETERS = {
    'forward_problems': FORWARD_PROBLEMS_PARAMETERS,
    'inverse_problems': INVERSE_PROBLEMS_PARAMETERS,
    'data_assimilation': DATA_ASSIMILATION_PARAMETERS,
    'control_optimization': CONTROL_OPTIMIZATION_PARAMETERS,
    'multiphysics': MULTIPHYSICS_PARAMETERS,
    'sparse_data': SPARSE_DATA_PARAMETERS,
    'uncertainty': UNCERTAINTY_PARAMETERS,
    'scientific_discovery': SCIENTIFIC_DISCOVERY_PARAMETERS,
    'efficiency': EFFICIENCY_PARAMETERS,
    'generalization': GENERALIZATION_PARAMETERS
}

# Parameter descriptions for UI
PARAMETER_DESCRIPTIONS = {
    # Classical parameters
    'nu': 'Viscosity coefficient',
    'alpha': 'Thermal diffusivity',
    'c': 'Wave speed',
    'omega': 'Angular frequency',
    'k': 'Wavenumber',
    'reynolds': 'Reynolds number',
    'hbar': 'Reduced Planck constant',
    'mass': 'Particle mass',
    'epsilon': 'Permittivity',
    'mu': 'Permeability',
    
    # Control parameters
    'A11': 'State matrix element A11',
    'A12': 'State matrix element A12',
    'A21': 'State matrix element A21',
    'A22': 'State matrix element A22',
    'B1': 'Input matrix element B1',
    'B2': 'Input matrix element B2',
    'Q': 'State cost weight',
    'R': 'Control cost weight',
    'control_strength': 'Control input strength',
    'control_heat': 'Control heat source',
    'control_force': 'Control force magnitude',
    'laser_power': 'Laser power (W)',
    'control_field': 'External control field',
    'discount_factor': 'Discount factor for optimal control',
    'cost_weight': 'Cost function weight',
    'weight1': 'Multi-objective weight 1',
    'weight2': 'Multi-objective weight 2',
    'weight3': 'Multi-objective weight 3',
    
    # Additive manufacturing parameters
    'latent_heat': 'Latent heat of fusion (J/kg)',
    'melting_temp': 'Melting temperature (K)',
    'thermal_conductivity_solid': 'Thermal conductivity of solid (W/m·K)',
    'thermal_conductivity_liquid': 'Thermal conductivity of liquid (W/m·K)',
    'density': 'Material density (kg/m³)',
    'surface_tension': 'Surface tension coefficient (N/m)',
    'gravity': 'Gravitational acceleration (m/s²)',
    'youngs_modulus': 'Young\'s modulus (Pa)',
    'poisson_ratio': 'Poisson\'s ratio',
    'thermal_expansion': 'Thermal expansion coefficient (1/K)',
    
    # Material science parameters
    'mobility': 'Phase field mobility',
    'interface_thickness': 'Interface thickness parameter',
    'interface_energy': 'Interface energy (J/m²)',
    'diffusion_coefficient': 'Diffusion coefficient (m²/s)',
    'shear_modulus': 'Shear modulus (Pa)',
    'burgers_vector': 'Burgers vector magnitude (m)',
    
    # Multiphysics parameters
    'velocity': 'Flow velocity (m/s)',
    'diffusion_coefficient_u': 'Diffusion coefficient for species u',
    'diffusion_coefficient_v': 'Diffusion coefficient for species v',
    'reaction_rate_a': 'Reaction rate constant a',
    'reaction_rate_b': 'Reaction rate constant b',
    'friction_coefficient': 'Friction coefficient',
    'permeability': 'Permeability (m²)',
    'absorption_coefficient': 'Absorption coefficient (1/m)',
    'scattering_coefficient': 'Scattering coefficient (1/m)',
    'density': 'Material density (kg/m³)',
    'viscosity': 'Dynamic viscosity (Pa·s)',
    'magnetic_permeability': 'Magnetic permeability (H/m)',
    'electrical_conductivity': 'Electrical conductivity (S/m)',
    'relaxation_time': 'Relaxation time (s)',
    'thermal_conductivity': 'Thermal conductivity (W/m·K)',
    'specific_heat': 'Specific heat capacity (J/kg·K)',
    
    # Uncertainty parameters
    'nu_std': 'Standard deviation of viscosity',
    'alpha_std': 'Standard deviation of thermal diffusivity',
    'c_std': 'Standard deviation of wave speed',
    'k_std': 'Standard deviation of wavenumber',
    'reynolds_std': 'Standard deviation of Reynolds number',
    'hbar_std': 'Standard deviation of Planck constant',
    'mass_std': 'Standard deviation of particle mass',
    'epsilon_std': 'Standard deviation of permittivity',
    'mu_std': 'Standard deviation of permeability',
    'youngs_std': 'Standard deviation of Young\'s modulus',
    'poisson_std': 'Standard deviation of Poisson\'s ratio',
    'mobility_std': 'Standard deviation of mobility',
    'interface_std': 'Standard deviation of interface energy',
    'diffusion_u_std': 'Standard deviation of diffusion coefficient u',
    'diffusion_v_std': 'Standard deviation of diffusion coefficient v',
    'reaction_a_std': 'Standard deviation of reaction rate a',
    'reaction_b_std': 'Standard deviation of reaction rate b',
    'permeability_std': 'Standard deviation of permeability',
    'viscosity_std': 'Standard deviation of viscosity',
    'relaxation_std': 'Standard deviation of relaxation time',
    'thermal_expansion_std': 'Standard deviation of thermal expansion',
    'thermal_conductivity_std': 'Standard deviation of thermal conductivity',
    'specific_heat_std': 'Standard deviation of specific heat',
    'velocity_std': 'Standard deviation of velocity',
    'diffusion_std': 'Standard deviation of diffusion coefficient',
    'gravity_std': 'Standard deviation of gravity',
    'friction_std': 'Standard deviation of friction coefficient',
    'density_std': 'Standard deviation of density',
    'magnetic_std': 'Standard deviation of magnetic permeability',
    'electrical_std': 'Standard deviation of electrical conductivity',
    
    # Scientific discovery parameters
    'unknown_coefficient': 'Unknown coefficient to be discovered',
    
    # Efficiency parameters
    'adaptive_sampling': 'Enable adaptive sampling strategy',
    
    # Generalization parameters
    'domain_shift': 'Domain shift parameter for generalization',
    
    # Sparse data parameters
    'sparse_ratio': 'Ratio of sparse data points',
    'noise_level': 'Noise level in data',
    
    # Grid parameters
    'nx': 'Number of spatial points in x-direction',
    'ny': 'Number of spatial points in y-direction',
    'nt': 'Number of temporal points',
    'x_min': 'Minimum x-coordinate',
    'x_max': 'Maximum x-coordinate',
    'y_min': 'Minimum y-coordinate',
    'y_max': 'Maximum y-coordinate',
    't_min': 'Minimum time',
    't_max': 'Maximum time'
}

def get_parameters_for_equation(equation_name):
    """Get parameters for a specific equation"""
    return DEFAULT_PARAMETERS.get(equation_name, {})

def get_parameter_description(param_name):
    """Get description for a specific parameter"""
    return PARAMETER_DESCRIPTIONS.get(param_name, 'No description available')

def get_all_equations_with_parameters():
    """Get list of all equations that have parameters defined"""
    return list(DEFAULT_PARAMETERS.keys())

def get_parameters_by_category():
    """Get parameters organized by category"""
    return {
        'forward_problems': FORWARD_PROBLEMS_PARAMETERS,
        'inverse_problems': INVERSE_PROBLEMS_PARAMETERS,
        'data_assimilation': DATA_ASSIMILATION_PARAMETERS,
        'control_optimization': CONTROL_OPTIMIZATION_PARAMETERS,
        'multiphysics': MULTIPHYSICS_PARAMETERS,
        'sparse_data': SPARSE_DATA_PARAMETERS
    }

# Combine all for easy lookup
ALL_EQUATION_PARAMETERS = {
    **FORWARD_PROBLEMS_PARAMETERS,
    **INVERSE_PROBLEMS_PARAMETERS,
    **DATA_ASSIMILATION_PARAMETERS,
    **CONTROL_OPTIMIZATION_PARAMETERS,
    **MULTIPHYSICS_PARAMETERS,
    **SPARSE_DATA_PARAMETERS,
    **UNCERTAINTY_PARAMETERS,
    **SCIENTIFIC_DISCOVERY_PARAMETERS,
    **EFFICIENCY_PARAMETERS,
    **GENERALIZATION_PARAMETERS
}

# Default Parameters for all equations (comprehensive lookup)
DEFAULT_PARAMETERS = {
    # Forward Problems
    'burgers': FORWARD_PROBLEMS_PARAMETERS['burgers'],
    'heat': FORWARD_PROBLEMS_PARAMETERS['heat'],
    'wave': FORWARD_PROBLEMS_PARAMETERS['wave'],
    'shm': FORWARD_PROBLEMS_PARAMETERS['shm'],
    'helmholtz': FORWARD_PROBLEMS_PARAMETERS['helmholtz'],
    'navier_stokes': FORWARD_PROBLEMS_PARAMETERS['navier_stokes'],
    'schrodinger': FORWARD_PROBLEMS_PARAMETERS['schrodinger'],
    'maxwell': FORWARD_PROBLEMS_PARAMETERS['maxwell'],
    'heat_transfer_phase_change': FORWARD_PROBLEMS_PARAMETERS['heat_transfer_phase_change'],
    'stefan_condition': FORWARD_PROBLEMS_PARAMETERS['stefan_condition'],
    'navier_stokes_free_surface': FORWARD_PROBLEMS_PARAMETERS['navier_stokes_free_surface'],
    'thermal_stress': FORWARD_PROBLEMS_PARAMETERS['thermal_stress'],
    'phase_field': FORWARD_PROBLEMS_PARAMETERS['phase_field'],
    'cahn_hilliard': FORWARD_PROBLEMS_PARAMETERS['cahn_hilliard'],
    'fick_second_law': FORWARD_PROBLEMS_PARAMETERS['fick_second_law'],
    'crystal_plasticity': FORWARD_PROBLEMS_PARAMETERS['crystal_plasticity'],
    
    # Inverse Problems
    'inverse_burgers': INVERSE_PROBLEMS_PARAMETERS['inverse_burgers'],
    'inverse_heat': INVERSE_PROBLEMS_PARAMETERS['inverse_heat'],
    'inverse_wave': INVERSE_PROBLEMS_PARAMETERS['inverse_wave'],
    'inverse_navier_stokes': INVERSE_PROBLEMS_PARAMETERS['inverse_navier_stokes'],
    'inverse_schrodinger': INVERSE_PROBLEMS_PARAMETERS['inverse_schrodinger'],
    'inverse_helmholtz': INVERSE_PROBLEMS_PARAMETERS['inverse_helmholtz'],
    'inverse_maxwell': INVERSE_PROBLEMS_PARAMETERS['inverse_maxwell'],
    'inverse_heat_transfer': INVERSE_PROBLEMS_PARAMETERS['inverse_heat_transfer'],
    'inverse_elastic': INVERSE_PROBLEMS_PARAMETERS['inverse_elastic'],
    'inverse_phase_field': INVERSE_PROBLEMS_PARAMETERS['inverse_phase_field'],
    'inverse_reaction_diffusion': INVERSE_PROBLEMS_PARAMETERS['inverse_reaction_diffusion'],
    'inverse_poroelasticity': INVERSE_PROBLEMS_PARAMETERS['inverse_poroelasticity'],
    'inverse_viscoelasticity': INVERSE_PROBLEMS_PARAMETERS['inverse_viscoelasticity'],
    
    # Data Assimilation
    'data_assimilation_navier_stokes': DATA_ASSIMILATION_PARAMETERS['data_assimilation_navier_stokes'],
    'data_assimilation_heat': DATA_ASSIMILATION_PARAMETERS['data_assimilation_heat'],
    'data_assimilation_burgers': DATA_ASSIMILATION_PARAMETERS['data_assimilation_burgers'],
    'data_assimilation_wave': DATA_ASSIMILATION_PARAMETERS['data_assimilation_wave'],
    'data_assimilation_shm': DATA_ASSIMILATION_PARAMETERS['data_assimilation_shm'],
    'data_assimilation_helmholtz': DATA_ASSIMILATION_PARAMETERS['data_assimilation_helmholtz'],
    'data_assimilation_schrodinger': DATA_ASSIMILATION_PARAMETERS['data_assimilation_schrodinger'],
    'data_assimilation_maxwell': DATA_ASSIMILATION_PARAMETERS['data_assimilation_maxwell'],
    'data_assimilation_heat_transfer': DATA_ASSIMILATION_PARAMETERS['data_assimilation_heat_transfer'],
    'data_assimilation_elastic': DATA_ASSIMILATION_PARAMETERS['data_assimilation_elastic'],
    'data_assimilation_phase_field': DATA_ASSIMILATION_PARAMETERS['data_assimilation_phase_field'],
    'data_assimilation_reaction_diffusion': DATA_ASSIMILATION_PARAMETERS['data_assimilation_reaction_diffusion'],
    'data_assimilation_poroelasticity': DATA_ASSIMILATION_PARAMETERS['data_assimilation_poroelasticity'],
    'data_assimilation_viscoelasticity': DATA_ASSIMILATION_PARAMETERS['data_assimilation_viscoelasticity'],
    'data_assimilation_thermoelasticity': DATA_ASSIMILATION_PARAMETERS['data_assimilation_thermoelasticity'],
    'data_assimilation_radiative_transfer': DATA_ASSIMILATION_PARAMETERS['data_assimilation_radiative_transfer'],
    'data_assimilation_shallow_water': DATA_ASSIMILATION_PARAMETERS['data_assimilation_shallow_water'],
    'data_assimilation_magnetohydrodynamics': DATA_ASSIMILATION_PARAMETERS['data_assimilation_magnetohydrodynamics'],
    
    # Control & Optimization
    'linear_dynamics': CONTROL_OPTIMIZATION_PARAMETERS['linear_dynamics'],
    'nonlinear_dynamics': CONTROL_OPTIMIZATION_PARAMETERS['nonlinear_dynamics'],
    'optimal_control_shm': CONTROL_OPTIMIZATION_PARAMETERS['optimal_control_shm'],
    'fluid_control': CONTROL_OPTIMIZATION_PARAMETERS['fluid_control'],
    'thermal_control': CONTROL_OPTIMIZATION_PARAMETERS['thermal_control'],
    'wave_control': CONTROL_OPTIMIZATION_PARAMETERS['wave_control'],
    'additive_manufacturing_control': CONTROL_OPTIMIZATION_PARAMETERS['additive_manufacturing_control'],
    'material_control': CONTROL_OPTIMIZATION_PARAMETERS['material_control'],
    'hjb_equation': CONTROL_OPTIMIZATION_PARAMETERS['hjb_equation'],
    'multi_objective_control': CONTROL_OPTIMIZATION_PARAMETERS['multi_objective_control'],
    'robust_control': CONTROL_OPTIMIZATION_PARAMETERS['robust_control'],
    'adaptive_control': CONTROL_OPTIMIZATION_PARAMETERS['adaptive_control'],
    'model_predictive_control': CONTROL_OPTIMIZATION_PARAMETERS['model_predictive_control'],
    'optimal_control_heat': CONTROL_OPTIMIZATION_PARAMETERS['optimal_control_heat'],
    'optimal_control_wave': CONTROL_OPTIMIZATION_PARAMETERS['optimal_control_wave'],
    'optimal_control_fluid': CONTROL_OPTIMIZATION_PARAMETERS['optimal_control_fluid'],
    
    # Multiphysics
    'advection_diffusion': MULTIPHYSICS_PARAMETERS['advection_diffusion'],
    'shallow_water': MULTIPHYSICS_PARAMETERS['shallow_water'],
    'poroelasticity': MULTIPHYSICS_PARAMETERS['poroelasticity'],
    'radiative_transfer': MULTIPHYSICS_PARAMETERS['radiative_transfer'],
    'reaction_diffusion': MULTIPHYSICS_PARAMETERS['reaction_diffusion'],
    'elastic_wave': MULTIPHYSICS_PARAMETERS['elastic_wave'],
    'magnetohydrodynamics': MULTIPHYSICS_PARAMETERS['magnetohydrodynamics'],
    'viscoelasticity': MULTIPHYSICS_PARAMETERS['viscoelasticity'],
    'thermoelasticity': MULTIPHYSICS_PARAMETERS['thermoelasticity'],
    'fluid_structure_interaction': MULTIPHYSICS_PARAMETERS['fluid_structure_interaction'],
    'electromagnetic_thermal': MULTIPHYSICS_PARAMETERS['electromagnetic_thermal'],
    'biomechanical_transport': MULTIPHYSICS_PARAMETERS['biomechanical_transport'],
    'geophysical_flow': MULTIPHYSICS_PARAMETERS['geophysical_flow'],
    'atmospheric_oceanic': MULTIPHYSICS_PARAMETERS['atmospheric_oceanic'],
    'nuclear_thermal': MULTIPHYSICS_PARAMETERS['nuclear_thermal'],
    'quantum_mechanical': MULTIPHYSICS_PARAMETERS['quantum_mechanical'],
    
    # Sparse Data
    'sparse_burgers': SPARSE_DATA_PARAMETERS['sparse_burgers'],
    'sparse_heat': SPARSE_DATA_PARAMETERS['sparse_heat'],
    'sparse_wave': SPARSE_DATA_PARAMETERS['sparse_wave'],
    'sparse_shm': SPARSE_DATA_PARAMETERS['sparse_shm'],
    'sparse_helmholtz': SPARSE_DATA_PARAMETERS['sparse_helmholtz'],
    'sparse_navier_stokes': SPARSE_DATA_PARAMETERS['sparse_navier_stokes'],
    'sparse_schrodinger': SPARSE_DATA_PARAMETERS['sparse_schrodinger'],
    'sparse_maxwell': SPARSE_DATA_PARAMETERS['sparse_maxwell'],
    'sparse_heat_transfer': SPARSE_DATA_PARAMETERS['sparse_heat_transfer'],
    'sparse_elastic': SPARSE_DATA_PARAMETERS['sparse_elastic'],
    'sparse_phase_field': SPARSE_DATA_PARAMETERS['sparse_phase_field'],
    'sparse_reaction_diffusion': SPARSE_DATA_PARAMETERS['sparse_reaction_diffusion'],
    'sparse_poroelasticity': SPARSE_DATA_PARAMETERS['sparse_poroelasticity'],
    'sparse_viscoelasticity': SPARSE_DATA_PARAMETERS['sparse_viscoelasticity'],
    'sparse_radiative_transfer': SPARSE_DATA_PARAMETERS['sparse_radiative_transfer'],
    'sparse_shallow_water': SPARSE_DATA_PARAMETERS['sparse_shallow_water'],
    'sparse_magnetohydrodynamics': SPARSE_DATA_PARAMETERS['sparse_magnetohydrodynamics'],
    'sparse_thermoelasticity': SPARSE_DATA_PARAMETERS['sparse_thermoelasticity'],
    
    # Uncertainty
    'uncertainty_burgers': UNCERTAINTY_PARAMETERS['uncertainty_burgers'],
    'uncertainty_heat': UNCERTAINTY_PARAMETERS['uncertainty_heat'],
    'uncertainty_wave': UNCERTAINTY_PARAMETERS['uncertainty_wave'],
    'uncertainty_shm': UNCERTAINTY_PARAMETERS['uncertainty_shm'],
    'uncertainty_helmholtz': UNCERTAINTY_PARAMETERS['uncertainty_helmholtz'],
    'uncertainty_navier_stokes': UNCERTAINTY_PARAMETERS['uncertainty_navier_stokes'],
    'uncertainty_schrodinger': UNCERTAINTY_PARAMETERS['uncertainty_schrodinger'],
    'uncertainty_maxwell': UNCERTAINTY_PARAMETERS['uncertainty_maxwell'],
    'uncertainty_heat_transfer': UNCERTAINTY_PARAMETERS['uncertainty_heat_transfer'],
    'uncertainty_elastic': UNCERTAINTY_PARAMETERS['uncertainty_elastic'],
    'uncertainty_phase_field': UNCERTAINTY_PARAMETERS['uncertainty_phase_field'],
    'uncertainty_reaction_diffusion': UNCERTAINTY_PARAMETERS['uncertainty_reaction_diffusion'],
    'uncertainty_poroelasticity': UNCERTAINTY_PARAMETERS['uncertainty_poroelasticity'],
    'uncertainty_viscoelasticity': UNCERTAINTY_PARAMETERS['uncertainty_viscoelasticity'],
    'uncertainty_radiative_transfer': UNCERTAINTY_PARAMETERS['uncertainty_radiative_transfer'],
    'uncertainty_shallow_water': UNCERTAINTY_PARAMETERS['uncertainty_shallow_water'],
    'uncertainty_magnetohydrodynamics': UNCERTAINTY_PARAMETERS['uncertainty_magnetohydrodynamics'],
    'uncertainty_thermoelasticity': UNCERTAINTY_PARAMETERS['uncertainty_thermoelasticity'],
    
    # Scientific Discovery
    'discovery_burgers': SCIENTIFIC_DISCOVERY_PARAMETERS['discovery_burgers'],
    'discovery_heat': SCIENTIFIC_DISCOVERY_PARAMETERS['discovery_heat'],
    'discovery_wave': SCIENTIFIC_DISCOVERY_PARAMETERS['discovery_wave'],
    'discovery_shm': SCIENTIFIC_DISCOVERY_PARAMETERS['discovery_shm'],
    'discovery_helmholtz': SCIENTIFIC_DISCOVERY_PARAMETERS['discovery_helmholtz'],
    'discovery_navier_stokes': SCIENTIFIC_DISCOVERY_PARAMETERS['discovery_navier_stokes'],
    'discovery_schrodinger': SCIENTIFIC_DISCOVERY_PARAMETERS['discovery_schrodinger'],
    'discovery_maxwell': SCIENTIFIC_DISCOVERY_PARAMETERS['discovery_maxwell'],
    'discovery_heat_transfer': SCIENTIFIC_DISCOVERY_PARAMETERS['discovery_heat_transfer'],
    'discovery_elastic': SCIENTIFIC_DISCOVERY_PARAMETERS['discovery_elastic'],
    'discovery_phase_field': SCIENTIFIC_DISCOVERY_PARAMETERS['discovery_phase_field'],
    'discovery_reaction_diffusion': SCIENTIFIC_DISCOVERY_PARAMETERS['discovery_reaction_diffusion'],
    'discovery_poroelasticity': SCIENTIFIC_DISCOVERY_PARAMETERS['discovery_poroelasticity'],
    'discovery_viscoelasticity': SCIENTIFIC_DISCOVERY_PARAMETERS['discovery_viscoelasticity'],
    'discovery_radiative_transfer': SCIENTIFIC_DISCOVERY_PARAMETERS['discovery_radiative_transfer'],
    'discovery_shallow_water': SCIENTIFIC_DISCOVERY_PARAMETERS['discovery_shallow_water'],
    'discovery_magnetohydrodynamics': SCIENTIFIC_DISCOVERY_PARAMETERS['discovery_magnetohydrodynamics'],
    'discovery_thermoelasticity': SCIENTIFIC_DISCOVERY_PARAMETERS['discovery_thermoelasticity'],
    
    # Efficiency
    'efficient_burgers': EFFICIENCY_PARAMETERS['efficient_burgers'],
    'efficient_heat': EFFICIENCY_PARAMETERS['efficient_heat'],
    'efficient_wave': EFFICIENCY_PARAMETERS['efficient_wave'],
    'efficient_shm': EFFICIENCY_PARAMETERS['efficient_shm'],
    'efficient_helmholtz': EFFICIENCY_PARAMETERS['efficient_helmholtz'],
    'efficient_navier_stokes': EFFICIENCY_PARAMETERS['efficient_navier_stokes'],
    'efficient_schrodinger': EFFICIENCY_PARAMETERS['efficient_schrodinger'],
    'efficient_maxwell': EFFICIENCY_PARAMETERS['efficient_maxwell'],
    'efficient_heat_transfer': EFFICIENCY_PARAMETERS['efficient_heat_transfer'],
    'efficient_elastic': EFFICIENCY_PARAMETERS['efficient_elastic'],
    'efficient_phase_field': EFFICIENCY_PARAMETERS['efficient_phase_field'],
    'efficient_reaction_diffusion': EFFICIENCY_PARAMETERS['efficient_reaction_diffusion'],
    'efficient_poroelasticity': EFFICIENCY_PARAMETERS['efficient_poroelasticity'],
    'efficient_viscoelasticity': EFFICIENCY_PARAMETERS['efficient_viscoelasticity'],
    'efficient_radiative_transfer': EFFICIENCY_PARAMETERS['efficient_radiative_transfer'],
    'efficient_shallow_water': EFFICIENCY_PARAMETERS['efficient_shallow_water'],
    'efficient_magnetohydrodynamics': EFFICIENCY_PARAMETERS['efficient_magnetohydrodynamics'],
    'efficient_thermoelasticity': EFFICIENCY_PARAMETERS['efficient_thermoelasticity'],
    
    # Generalization
    'generalized_burgers': GENERALIZATION_PARAMETERS['generalized_burgers'],
    'generalized_heat': GENERALIZATION_PARAMETERS['generalized_heat'],
    'generalized_wave': GENERALIZATION_PARAMETERS['generalized_wave'],
    'generalized_shm': GENERALIZATION_PARAMETERS['generalized_shm'],
    'generalized_helmholtz': GENERALIZATION_PARAMETERS['generalized_helmholtz'],
    'generalized_navier_stokes': GENERALIZATION_PARAMETERS['generalized_navier_stokes'],
    'generalized_schrodinger': GENERALIZATION_PARAMETERS['generalized_schrodinger'],
    'generalized_maxwell': GENERALIZATION_PARAMETERS['generalized_maxwell'],
    'generalized_heat_transfer': GENERALIZATION_PARAMETERS['generalized_heat_transfer'],
    'generalized_elastic': GENERALIZATION_PARAMETERS['generalized_elastic'],
    'generalized_phase_field': GENERALIZATION_PARAMETERS['generalized_phase_field'],
    'generalized_reaction_diffusion': GENERALIZATION_PARAMETERS['generalized_reaction_diffusion'],
    'generalized_poroelasticity': GENERALIZATION_PARAMETERS['generalized_poroelasticity'],
    'generalized_viscoelasticity': GENERALIZATION_PARAMETERS['generalized_viscoelasticity'],
    'generalized_radiative_transfer': GENERALIZATION_PARAMETERS['generalized_radiative_transfer'],
    'generalized_shallow_water': GENERALIZATION_PARAMETERS['generalized_shallow_water'],
    'generalized_magnetohydrodynamics': GENERALIZATION_PARAMETERS['generalized_magnetohydrodynamics']
}

