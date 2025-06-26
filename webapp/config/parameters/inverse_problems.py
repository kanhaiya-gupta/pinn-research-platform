"""
Inverse Problems Parameters
Parameters for solving inverse problems with unknown parameters to be identified.
"""

INVERSE_PROBLEMS_PARAMETERS_DICT = {
    # Unknown Physical Parameters (to be identified)
    'unknown_viscosity': {
        'name': 'Unknown Viscosity',
        'description': 'Dynamic viscosity to be identified from flow data',
        'unit': 'Pa·s',
        'default': 0.001,
        'range': [1e-6, 1e-2],
        'category': 'unknown_fluid_properties',
        'identification_method': 'flow_reconstruction'
    },
    'unknown_thermal_diffusivity': {
        'name': 'Unknown Thermal Diffusivity',
        'description': 'Thermal diffusivity to be identified from temperature data',
        'unit': 'm²/s',
        'default': 1e-5,
        'range': [1e-8, 1e-3],
        'category': 'unknown_thermal_properties',
        'identification_method': 'temperature_reconstruction'
    },
    'unknown_wave_speed': {
        'name': 'Unknown Wave Speed',
        'description': 'Wave speed to be identified from wave propagation data',
        'unit': 'm/s',
        'default': 340.0,
        'range': [1.0, 10000.0],
        'category': 'unknown_wave_properties',
        'identification_method': 'wave_reconstruction'
    },
    'unknown_elastic_modulus': {
        'name': 'Unknown Elastic Modulus',
        'description': 'Elastic modulus to be identified from deformation data',
        'unit': 'GPa',
        'default': 200.0,
        'range': [0.1, 1000.0],
        'category': 'unknown_mechanical_properties',
        'identification_method': 'deformation_reconstruction'
    },
    'unknown_diffusion_coefficient': {
        'name': 'Unknown Diffusion Coefficient',
        'description': 'Diffusion coefficient to be identified from concentration data',
        'unit': 'm²/s',
        'default': 1e-9,
        'range': [1e-12, 1e-6],
        'category': 'unknown_transport_properties',
        'identification_method': 'concentration_reconstruction'
    },
    'unknown_reaction_rate': {
        'name': 'Unknown Reaction Rate',
        'description': 'Reaction rate to be identified from chemical data',
        'unit': '1/s',
        'default': 1e-3,
        'range': [1e-6, 1e0],
        'category': 'unknown_chemical_properties',
        'identification_method': 'chemical_reconstruction'
    },
    'unknown_permeability': {
        'name': 'Unknown Permeability',
        'description': 'Permeability to be identified from pressure data',
        'unit': 'm²',
        'default': 1e-12,
        'range': [1e-20, 1e-8],
        'category': 'unknown_poroelastic_properties',
        'identification_method': 'pressure_reconstruction'
    },
    'unknown_phase_field_mobility': {
        'name': 'Unknown Phase Field Mobility',
        'description': 'Phase field mobility to be identified from microstructure data',
        'unit': 'm²/(J·s)',
        'default': 1e-3,
        'range': [1e-6, 1e-1],
        'category': 'unknown_phase_field_properties',
        'identification_method': 'microstructure_reconstruction'
    },
    'unknown_grain_boundary_energy': {
        'name': 'Unknown Grain Boundary Energy',
        'description': 'Grain boundary energy to be identified from grain growth data',
        'unit': 'J/m²',
        'default': 1.0,
        'range': [0.1, 10.0],
        'category': 'unknown_material_properties',
        'identification_method': 'grain_growth_reconstruction'
    },
    'unknown_laser_power': {
        'name': 'Unknown Laser Power',
        'description': 'Laser power to be identified from thermal response data',
        'unit': 'W',
        'default': 1000.0,
        'range': [1.0, 10000.0],
        'category': 'unknown_am_properties',
        'identification_method': 'thermal_reconstruction'
    },
    
    # Unknown Boundary Conditions
    'unknown_boundary_temperature': {
        'name': 'Unknown Boundary Temperature',
        'description': 'Boundary temperature to be identified from interior temperature data',
        'unit': 'K',
        'default': 300.0,
        'range': [100.0, 2000.0],
        'category': 'unknown_boundary_conditions',
        'identification_method': 'temperature_reconstruction'
    },
    'unknown_boundary_heat_flux': {
        'name': 'Unknown Boundary Heat Flux',
        'description': 'Boundary heat flux to be identified from temperature data',
        'unit': 'W/m²',
        'default': 0.0,
        'range': [-1e6, 1e6],
        'category': 'unknown_boundary_conditions',
        'identification_method': 'heat_flux_reconstruction'
    },
    'unknown_boundary_pressure': {
        'name': 'Unknown Boundary Pressure',
        'description': 'Boundary pressure to be identified from flow data',
        'unit': 'Pa',
        'default': 101325.0,
        'range': [1e3, 1e8],
        'category': 'unknown_boundary_conditions',
        'identification_method': 'pressure_reconstruction'
    },
    
    # Unknown Initial Conditions
    'unknown_initial_temperature': {
        'name': 'Unknown Initial Temperature',
        'description': 'Initial temperature field to be identified from time-series data',
        'unit': 'K',
        'default': 300.0,
        'range': [100.0, 2000.0],
        'category': 'unknown_initial_conditions',
        'identification_method': 'temperature_reconstruction'
    },
    'unknown_initial_concentration': {
        'name': 'Unknown Initial Concentration',
        'description': 'Initial concentration field to be identified from time-series data',
        'unit': 'mol/m³',
        'default': 1.0,
        'range': [0.0, 1000.0],
        'category': 'unknown_initial_conditions',
        'identification_method': 'concentration_reconstruction'
    },
    'unknown_initial_displacement': {
        'name': 'Unknown Initial Displacement',
        'description': 'Initial displacement field to be identified from deformation data',
        'unit': 'm',
        'default': 0.0,
        'range': [-1.0, 1.0],
        'category': 'unknown_initial_conditions',
        'identification_method': 'deformation_reconstruction'
    },
    
    # Unknown Source Terms
    'unknown_heat_source': {
        'name': 'Unknown Heat Source',
        'description': 'Heat source to be identified from temperature data',
        'unit': 'W/m³',
        'default': 0.0,
        'range': [-1e6, 1e6],
        'category': 'unknown_source_terms',
        'identification_method': 'source_reconstruction'
    },
    'unknown_mass_source': {
        'name': 'Unknown Mass Source',
        'description': 'Mass source to be identified from concentration data',
        'unit': 'kg/(m³·s)',
        'default': 0.0,
        'range': [-1e-3, 1e-3],
        'category': 'unknown_source_terms',
        'identification_method': 'source_reconstruction'
    },
    'unknown_force_source': {
        'name': 'Unknown Force Source',
        'description': 'Force source to be identified from velocity data',
        'unit': 'N/m³',
        'default': 0.0,
        'range': [-1e6, 1e6],
        'category': 'unknown_source_terms',
        'identification_method': 'force_reconstruction'
    },
    
    # Unknown Geometric Parameters
    'unknown_domain_size': {
        'name': 'Unknown Domain Size',
        'description': 'Domain size to be identified from field data',
        'unit': 'm',
        'default': 1.0,
        'range': [0.1, 10.0],
        'category': 'unknown_geometric_parameters',
        'identification_method': 'geometry_reconstruction'
    },
    'unknown_boundary_shape': {
        'name': 'Unknown Boundary Shape',
        'description': 'Boundary shape to be identified from field data',
        'unit': 'dimensionless',
        'default': 1.0,
        'range': [0.1, 10.0],
        'category': 'unknown_geometric_parameters',
        'identification_method': 'geometry_reconstruction'
    },
    
    # Unknown Coupling Parameters
    'unknown_coupling_coefficient': {
        'name': 'Unknown Coupling Coefficient',
        'description': 'Coupling coefficient between physical fields',
        'unit': 'dimensionless',
        'default': 1.0,
        'range': [0.0, 10.0],
        'category': 'unknown_coupling_parameters',
        'identification_method': 'coupling_reconstruction'
    },
    'unknown_interface_parameter': {
        'name': 'Unknown Interface Parameter',
        'description': 'Interface parameter for multi-phase systems',
        'unit': 'dimensionless',
        'default': 1.0,
        'range': [0.0, 10.0],
        'category': 'unknown_coupling_parameters',
        'identification_method': 'interface_reconstruction'
    },
    
    # Inverse Problem Solver Parameters
    'regularization_parameter': {
        'name': 'Regularization Parameter',
        'description': 'Regularization parameter for inverse problem stability',
        'unit': 'dimensionless',
        'default': 1e-6,
        'range': [1e-12, 1e-3],
        'category': 'solver_parameters',
        'identification_method': 'regularization'
    },
    'tolerance': {
        'name': 'Solver Tolerance',
        'description': 'Convergence tolerance for inverse problem solver',
        'unit': 'dimensionless',
        'default': 1e-6,
        'range': [1e-12, 1e-3],
        'category': 'solver_parameters',
        'identification_method': 'convergence'
    },
    'max_iterations': {
        'name': 'Maximum Iterations',
        'description': 'Maximum number of iterations for inverse problem solver',
        'unit': 'dimensionless',
        'default': 1000,
        'range': [100, 10000],
        'category': 'solver_parameters',
        'identification_method': 'convergence'
    },
    
    # Observation Parameters
    'noise_level': {
        'name': 'Noise Level',
        'description': 'Level of noise in observational data',
        'unit': 'dimensionless',
        'default': 0.01,
        'range': [0.0, 0.1],
        'category': 'observation_parameters',
        'identification_method': 'noise_estimation'
    },
    'sampling_frequency': {
        'name': 'Sampling Frequency',
        'description': 'Frequency of observational data sampling',
        'unit': 'Hz',
        'default': 1.0,
        'range': [0.1, 100.0],
        'category': 'observation_parameters',
        'identification_method': 'sampling_optimization'
    },
    'sensor_locations': {
        'name': 'Sensor Locations',
        'description': 'Locations of observational sensors',
        'unit': 'm',
        'default': [0.0, 0.5, 1.0],
        'range': [0.0, 10.0],
        'category': 'observation_parameters',
        'identification_method': 'sensor_placement'
    }
}

# Equation-specific parameter mappings for inverse problems
INVERSE_PROBLEMS_EQUATION_PARAMETERS = {
    'inverse_burgers': {
        'unknown_viscosity': {
            'name': 'Unknown Viscosity (ν)',
            'description': 'Dynamic viscosity to be identified from flow data',
            'unit': 'Pa·s',
            'default': 0.01,
            'range': [1e-6, 1e-1],
            'category': 'unknown_fluid_properties',
            'identification_method': 'flow_reconstruction'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties'
        },
        'regularization_parameter': {
            'name': 'Regularization Parameter',
            'description': 'Regularization parameter for inverse problem stability',
            'unit': 'dimensionless',
            'default': 1e-6,
            'range': [1e-12, 1e-3],
            'category': 'solver_parameters'
        }
    },
    
    'inverse_heat': {
        'unknown_thermal_diffusivity': {
            'name': 'Unknown Thermal Diffusivity (α)',
            'description': 'Thermal diffusivity to be identified from temperature data',
            'unit': 'm²/s',
            'default': 1e-5,
            'range': [1e-8, 1e-3],
            'category': 'unknown_thermal_properties',
            'identification_method': 'temperature_reconstruction'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties'
        },
        'regularization_parameter': {
            'name': 'Regularization Parameter',
            'description': 'Regularization parameter for inverse problem stability',
            'unit': 'dimensionless',
            'default': 1e-6,
            'range': [1e-12, 1e-3],
            'category': 'solver_parameters'
        }
    },
    
    'inverse_wave': {
        'unknown_wave_speed': {
            'name': 'Unknown Wave Speed (c)',
            'description': 'Wave speed to be identified from wave propagation data',
            'unit': 'm/s',
            'default': 340.0,
            'range': [1.0, 10000.0],
            'category': 'unknown_wave_properties',
            'identification_method': 'wave_reconstruction'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties'
        },
        'regularization_parameter': {
            'name': 'Regularization Parameter',
            'description': 'Regularization parameter for inverse problem stability',
            'unit': 'dimensionless',
            'default': 1e-6,
            'range': [1e-12, 1e-3],
            'category': 'solver_parameters'
        }
    },
    
    'inverse_shm': {
        'unknown_natural_frequency': {
            'name': 'Unknown Natural Frequency (ω)',
            'description': 'Natural frequency to be identified from oscillation data',
            'unit': 'rad/s',
            'default': 1.0,
            'range': [0.1, 100.0],
            'category': 'unknown_mechanical_properties',
            'identification_method': 'oscillation_reconstruction'
        },
        'unknown_damping_ratio': {
            'name': 'Unknown Damping Ratio (ζ)',
            'description': 'Damping ratio to be identified from oscillation data',
            'unit': 'dimensionless',
            'default': 0.1,
            'range': [0.0, 1.0],
            'category': 'unknown_mechanical_properties',
            'identification_method': 'oscillation_reconstruction'
        },
        'amplitude': {
            'name': 'Amplitude',
            'description': 'Oscillation amplitude',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'mechanical_properties'
        }
    },
    
    'inverse_helmholtz': {
        'unknown_wavenumber': {
            'name': 'Unknown Wavenumber (k)',
            'description': 'Wavenumber to be identified from wave field data',
            'unit': '1/m',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'unknown_wave_properties',
            'identification_method': 'wave_field_reconstruction'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties'
        },
        'regularization_parameter': {
            'name': 'Regularization Parameter',
            'description': 'Regularization parameter for inverse problem stability',
            'unit': 'dimensionless',
            'default': 1e-6,
            'range': [1e-12, 1e-3],
            'category': 'solver_parameters'
        }
    },
    
    'inverse_navier_stokes': {
        'unknown_viscosity': {
            'name': 'Unknown Viscosity (μ)',
            'description': 'Dynamic viscosity to be identified from flow data',
            'unit': 'Pa·s',
            'default': 0.001,
            'range': [1e-6, 1e-1],
            'category': 'unknown_fluid_properties',
            'identification_method': 'flow_reconstruction'
        },
        'unknown_density': {
            'name': 'Unknown Density (ρ)',
            'description': 'Fluid density to be identified from flow data',
            'unit': 'kg/m³',
            'default': 1000.0,
            'range': [1.0, 20000.0],
            'category': 'unknown_fluid_properties',
            'identification_method': 'flow_reconstruction'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties'
        },
        
    },
    
    'inverse_schrodinger': {
        'unknown_planck_constant': {
            'name': 'Unknown Planck Constant (ℏ)',
            'description': 'Reduced Planck constant to be identified',
            'unit': 'J·s',
            'default': 1.055e-34,
            'range': [1e-35, 1e-33],
            'category': 'unknown_quantum_properties',
            'identification_method': 'quantum_reconstruction'
        },
        'unknown_mass': {
            'name': 'Unknown Mass (m)',
            'description': 'Particle mass to be identified',
            'unit': 'kg',
            'default': 9.109e-31,
            'range': [1e-32, 1e-29],
            'category': 'unknown_quantum_properties',
            'identification_method': 'quantum_reconstruction'
        },
        'unknown_potential_strength': {
            'name': 'Unknown Potential Strength',
            'description': 'Strength of potential energy to be identified',
            'unit': 'J',
            'default': 1e-20,
            'range': [1e-25, 1e-15],
            'category': 'unknown_quantum_properties',
            'identification_method': 'potential_reconstruction'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length',
            'unit': 'm',
            'default': 1e-9,
            'range': [1e-12, 1e-6],
            'category': 'domain_properties'
        }
    },
    
    'inverse_phase_field': {
        'unknown_mobility': {
            'name': 'Unknown Mobility (M)',
            'description': 'Phase field mobility to be identified from microstructure data',
            'unit': 'm²/(J·s)',
            'default': 1e-3,
            'range': [1e-6, 1e-1],
            'category': 'unknown_phase_field_properties',
            'identification_method': 'microstructure_reconstruction'
        },
        'unknown_interface_thickness': {
            'name': 'Unknown Interface Thickness (ε)',
            'description': 'Phase field interface thickness to be identified',
            'unit': 'm',
            'default': 1e-6,
            'range': [1e-9, 1e-3],
            'category': 'unknown_phase_field_properties',
            'identification_method': 'interface_reconstruction'
        },
        'unknown_free_energy_barrier': {
            'name': 'Unknown Free Energy Barrier (W)',
            'description': 'Free energy barrier to be identified from phase transitions',
            'unit': 'J/m³',
            'default': 1e6,
            'range': [1e3, 1e9],
            'category': 'unknown_phase_field_properties',
            'identification_method': 'energy_reconstruction'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1e-3,
            'range': [1e-6, 1e-1],
            'category': 'domain_properties'
        },
        
    },
    
    'inverse_reaction_diffusion': {
        'unknown_diffusion_coefficient': {
            'name': 'Unknown Diffusion Coefficient (D)',
            'description': 'Diffusion coefficient to be identified from concentration data',
            'unit': 'm²/s',
            'default': 1e-9,
            'range': [1e-12, 1e-6],
            'category': 'unknown_transport_properties',
            'identification_method': 'concentration_reconstruction'
        },
        'unknown_reaction_rate': {
            'name': 'Unknown Reaction Rate (k)',
            'description': 'Reaction rate to be identified from chemical data',
            'unit': '1/s',
            'default': 1e-3,
            'range': [1e-6, 1e0],
            'category': 'unknown_chemical_properties',
            'identification_method': 'chemical_reconstruction'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties'
        },
        
    },
    
    'inverse_poroelasticity': {
        'unknown_permeability': {
            'name': 'Unknown Permeability (κ)',
            'description': 'Permeability to be identified from pressure data',
            'unit': 'm²',
            'default': 1e-12,
            'range': [1e-20, 1e-8],
            'category': 'unknown_poroelastic_properties',
            'identification_method': 'pressure_reconstruction'
        },
        'unknown_elastic_modulus': {
            'name': 'Unknown Elastic Modulus (E)',
            'description': 'Elastic modulus to be identified from deformation data',
            'unit': 'GPa',
            'default': 200.0,
            'range': [0.1, 1000.0],
            'category': 'unknown_mechanical_properties',
            'identification_method': 'deformation_reconstruction'
        },
        'unknown_biot_coefficient': {
            'name': 'Unknown Biot Coefficient (α)',
            'description': 'Biot coefficient to be identified from poroelastic data',
            'unit': 'dimensionless',
            'default': 0.8,
            'range': [0.0, 1.0],
            'category': 'unknown_poroelastic_properties',
            'identification_method': 'poroelastic_reconstruction'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties'
        },
        
    },
    
    'inverse_viscoelasticity': {
        'unknown_elastic_modulus': {
            'name': 'Unknown Elastic Modulus (E)',
            'description': 'Elastic modulus to be identified from deformation data',
            'unit': 'GPa',
            'default': 200.0,
            'range': [0.1, 1000.0],
            'category': 'unknown_mechanical_properties',
            'identification_method': 'deformation_reconstruction'
        },
        'unknown_relaxation_time': {
            'name': 'Unknown Relaxation Time (τ)',
            'description': 'Viscoelastic relaxation time to be identified',
            'unit': 's',
            'default': 1.0,
            'range': [1e-3, 1e3],
            'category': 'unknown_viscoelastic_properties',
            'identification_method': 'viscoelastic_reconstruction'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties'
        },
        
    },
    
    'inverse_radiative_transfer': {
        'unknown_absorption_coefficient': {
            'name': 'Unknown Absorption Coefficient (κ)',
            'description': 'Absorption coefficient to be identified from radiative data',
            'unit': '1/m',
            'default': 1.0,
            'range': [1e-3, 1e3],
            'category': 'unknown_radiation_properties',
            'identification_method': 'radiation_reconstruction'
        },
        'unknown_scattering_coefficient': {
            'name': 'Unknown Scattering Coefficient (σ)',
            'description': 'Scattering coefficient to be identified from radiative data',
            'unit': '1/m',
            'default': 0.1,
            'range': [1e-4, 1e2],
            'category': 'unknown_radiation_properties',
            'identification_method': 'radiation_reconstruction'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties'
        }
    },
    
    'inverse_shallow_water': {
        'unknown_gravity': {
            'name': 'Unknown Gravity (g)',
            'description': 'Acceleration due to gravity to be identified',
            'unit': 'm/s²',
            'default': 9.81,
            'range': [1.0, 20.0],
            'category': 'unknown_geophysical_properties',
            'identification_method': 'geophysical_reconstruction'
        },
        'unknown_coriolis_parameter': {
            'name': 'Unknown Coriolis Parameter (f)',
            'description': 'Coriolis parameter to be identified from geophysical data',
            'unit': '1/s',
            'default': 1e-4,
            'range': [1e-6, 1e-2],
            'category': 'unknown_geophysical_properties',
            'identification_method': 'geophysical_reconstruction'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1000.0,
            'range': [100.0, 10000.0],
            'category': 'domain_properties'
        },
        
    },
    
    'inverse_magnetohydrodynamics': {
        'unknown_magnetic_permeability': {
            'name': 'Unknown Magnetic Permeability (μ)',
            'description': 'Magnetic permeability to be identified from MHD data',
            'unit': 'H/m',
            'default': 1.257e-6,
            'range': [1e-7, 1e-5],
            'category': 'unknown_electromagnetic_properties',
            'identification_method': 'mhd_reconstruction'
        },
        'unknown_electrical_conductivity': {
            'name': 'Unknown Electrical Conductivity (σ)',
            'description': 'Electrical conductivity to be identified from MHD data',
            'unit': 'S/m',
            'default': 1e6,
            'range': [1e3, 1e9],
            'category': 'unknown_electromagnetic_properties',
            'identification_method': 'mhd_reconstruction'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties'
        },
        
    },
    
    'inverse_thermoelasticity': {
        'unknown_thermal_conductivity': {
            'name': 'Unknown Thermal Conductivity (k)',
            'description': 'Thermal conductivity to be identified from thermal data',
            'unit': 'W/(m·K)',
            'default': 50.0,
            'range': [0.01, 1000.0],
            'category': 'unknown_thermal_properties',
            'identification_method': 'thermal_reconstruction'
        },
        'unknown_elastic_modulus': {
            'name': 'Unknown Elastic Modulus (E)',
            'description': 'Elastic modulus to be identified from deformation data',
            'unit': 'GPa',
            'default': 200.0,
            'range': [0.1, 1000.0],
            'category': 'unknown_mechanical_properties',
            'identification_method': 'deformation_reconstruction'
        },
        'unknown_thermal_expansion': {
            'name': 'Unknown Thermal Expansion (α)',
            'description': 'Thermal expansion coefficient to be identified',
            'unit': '1/K',
            'default': 1e-5,
            'range': [1e-7, 1e-3],
            'category': 'unknown_thermoelastic_properties',
            'identification_method': 'thermoelastic_reconstruction'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties'
        },
        
    },
    
    'inverse_advection_diffusion': {
        'unknown_velocity': {
            'name': 'Unknown Velocity (v)',
            'description': 'Velocity field to be identified from transport data',
            'unit': 'm/s',
            'default': 1.0,
            'range': [0.1, 100.0],
            'category': 'unknown_transport_properties',
            'identification_method': 'velocity_reconstruction'
        },
        'unknown_diffusion_coefficient': {
            'name': 'Unknown Diffusion Coefficient (D)',
            'description': 'Diffusion coefficient to be identified from transport data',
            'unit': 'm²/s',
            'default': 1e-9,
            'range': [1e-12, 1e-6],
            'category': 'unknown_transport_properties',
            'identification_method': 'diffusion_reconstruction'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties'
        },
        
    },
    
    'inverse_elastic_wave': {
        'unknown_elastic_modulus': {
            'name': 'Unknown Elastic Modulus (E)',
            'description': 'Elastic modulus to be identified from wave data',
            'unit': 'GPa',
            'default': 200.0,
            'range': [0.1, 1000.0],
            'category': 'unknown_mechanical_properties',
            'identification_method': 'wave_reconstruction'
        },
        'unknown_poisson_ratio': {
            'name': 'Unknown Poisson Ratio (ν)',
            'description': 'Poisson ratio to be identified from wave data',
            'unit': 'dimensionless',
            'default': 0.3,
            'range': [0.0, 0.5],
            'category': 'unknown_mechanical_properties',
            'identification_method': 'wave_reconstruction'
        },
        'unknown_density': {
            'name': 'Unknown Density (ρ)',
            'description': 'Material density to be identified from wave data',
            'unit': 'kg/m³',
            'default': 1000.0,
            'range': [1.0, 20000.0],
            'category': 'unknown_material_properties',
            'identification_method': 'wave_reconstruction'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties'
        },
        
    },
    
    'inverse_fluid_structure_interaction': {
        'unknown_fluid_viscosity': {
            'name': 'Unknown Fluid Viscosity (μ)',
            'description': 'Fluid viscosity to be identified from FSI data',
            'unit': 'Pa·s',
            'default': 0.001,
            'range': [1e-6, 1e-1],
            'category': 'unknown_fluid_properties',
            'identification_method': 'fsi_reconstruction'
        },
        'unknown_structural_modulus': {
            'name': 'Unknown Structural Modulus (E)',
            'description': 'Structural elastic modulus to be identified from FSI data',
            'unit': 'GPa',
            'default': 200.0,
            'range': [0.1, 1000.0],
            'category': 'unknown_structural_properties',
            'identification_method': 'fsi_reconstruction'
        },
        'unknown_coupling_coefficient': {
            'name': 'Unknown Coupling Coefficient (α)',
            'description': 'Fluid-structure coupling coefficient to be identified',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'unknown_coupling_parameters',
            'identification_method': 'coupling_reconstruction'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties'
        },
        
    },
    
    'inverse_electromagnetic_thermal': {
        'unknown_electrical_conductivity': {
            'name': 'Unknown Electrical Conductivity (σ)',
            'description': 'Electrical conductivity to be identified from EM-thermal data',
            'unit': 'S/m',
            'default': 1e6,
            'range': [1e3, 1e9],
            'category': 'unknown_electromagnetic_properties',
            'identification_method': 'em_thermal_reconstruction'
        },
        'unknown_thermal_conductivity': {
            'name': 'Unknown Thermal Conductivity (k)',
            'description': 'Thermal conductivity to be identified from EM-thermal data',
            'unit': 'W/(m·K)',
            'default': 50.0,
            'range': [0.01, 1000.0],
            'category': 'unknown_thermal_properties',
            'identification_method': 'em_thermal_reconstruction'
        },
        'unknown_coupling_coefficient': {
            'name': 'Unknown Coupling Coefficient (α)',
            'description': 'Electromagnetic-thermal coupling coefficient to be identified',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'unknown_coupling_parameters',
            'identification_method': 'coupling_reconstruction'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties'
        },
        
    },
    
    'inverse_biomechanical_transport': {
        'unknown_elastic_modulus': {
            'name': 'Unknown Elastic Modulus (E)',
            'description': 'Tissue elastic modulus to be identified from biomechanical data',
            'unit': 'kPa',
            'default': 100.0,
            'range': [1.0, 10000.0],
            'category': 'unknown_biomechanical_properties',
            'identification_method': 'biomechanical_reconstruction'
        },
        'unknown_diffusion_coefficient': {
            'name': 'Unknown Diffusion Coefficient (D)',
            'description': 'Transport diffusion coefficient to be identified from biological data',
            'unit': 'm²/s',
            'default': 1e-9,
            'range': [1e-12, 1e-6],
            'category': 'unknown_transport_properties',
            'identification_method': 'transport_reconstruction'
        },
        'unknown_coupling_coefficient': {
            'name': 'Unknown Coupling Coefficient (α)',
            'description': 'Biomechanical-transport coupling coefficient to be identified',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'unknown_coupling_parameters',
            'identification_method': 'coupling_reconstruction'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1e-2,
            'range': [1e-4, 1e-1],
            'category': 'domain_properties'
        },
        
    },
    
    'inverse_geophysical_flow': {
        'unknown_coriolis_parameter': {
            'name': 'Unknown Coriolis Parameter (f)',
            'description': 'Coriolis parameter to be identified from geophysical data',
            'unit': '1/s',
            'default': 1e-4,
            'range': [1e-6, 1e-2],
            'category': 'unknown_geophysical_properties',
            'identification_method': 'geophysical_reconstruction'
        },
        'unknown_friction_coefficient': {
            'name': 'Unknown Friction Coefficient (r)',
            'description': 'Bottom friction coefficient to be identified from flow data',
            'unit': '1/s',
            'default': 1e-3,
            'range': [1e-5, 1e-1],
            'category': 'unknown_geophysical_properties',
            'identification_method': 'friction_reconstruction'
        },
        'unknown_bathymetry': {
            'name': 'Unknown Bathymetry (h)',
            'description': 'Bottom topography to be identified from flow data',
            'unit': 'm',
            'default': 100.0,
            'range': [1.0, 1000.0],
            'category': 'unknown_geometric_parameters',
            'identification_method': 'bathymetry_reconstruction'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1000.0,
            'range': [100.0, 10000.0],
            'category': 'domain_properties'
        },
        
    },
    
    'inverse_atmospheric_oceanic': {
        'unknown_atmospheric_pressure': {
            'name': 'Unknown Atmospheric Pressure (P)',
            'description': 'Atmospheric pressure to be identified from coupled data',
            'unit': 'Pa',
            'default': 101325.0,
            'range': [1e4, 1e6],
            'category': 'unknown_atmospheric_properties',
            'identification_method': 'atmospheric_reconstruction'
        },
        'unknown_ocean_temperature': {
            'name': 'Unknown Ocean Temperature (T)',
            'description': 'Ocean temperature to be identified from coupled data',
            'unit': 'K',
            'default': 288.0,
            'range': [273.0, 313.0],
            'category': 'unknown_oceanic_properties',
            'identification_method': 'oceanic_reconstruction'
        },
        'unknown_coupling_strength': {
            'name': 'Unknown Coupling Strength (α)',
            'description': 'Atmosphere-ocean coupling strength to be identified',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'unknown_coupling_parameters',
            'identification_method': 'coupling_reconstruction'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1000.0,
            'range': [100.0, 10000.0],
            'category': 'domain_properties'
        },
        
    },
    
    'inverse_maxwell': {
        'unknown_electric_permittivity': {
            'name': 'Unknown Electric Permittivity (ε)',
            'description': 'Electric permittivity to be identified from electromagnetic data',
            'unit': 'F/m',
            'default': 8.854e-12,
            'range': [1e-13, 1e-10],
            'category': 'unknown_electromagnetic_properties',
            'identification_method': 'em_reconstruction'
        },
        'unknown_magnetic_permeability': {
            'name': 'Unknown Magnetic Permeability (μ)',
            'description': 'Magnetic permeability to be identified from electromagnetic data',
            'unit': 'H/m',
            'default': 1.257e-6,
            'range': [1e-7, 1e-5],
            'category': 'unknown_electromagnetic_properties',
            'identification_method': 'em_reconstruction'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties'
        },
        
    },
    
    'inverse_heat_transfer': {
        'unknown_thermal_conductivity': {
            'name': 'Unknown Thermal Conductivity (k)',
            'description': 'Thermal conductivity to be identified from heat transfer data',
            'unit': 'W/(m·K)',
            'default': 50.0,
            'range': [0.01, 1000.0],
            'category': 'unknown_thermal_properties',
            'identification_method': 'heat_transfer_reconstruction'
        },
        'unknown_heat_source': {
            'name': 'Unknown Heat Source (Q)',
            'description': 'Heat source to be identified from temperature data',
            'unit': 'W/m³',
            'default': 0.0,
            'range': [-1e6, 1e6],
            'category': 'unknown_source_terms',
            'identification_method': 'source_reconstruction'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties'
        },
        
    },
    
    'inverse_elastic': {
        'unknown_elastic_modulus': {
            'name': 'Unknown Elastic Modulus (E)',
            'description': 'Elastic modulus to be identified from deformation data',
            'unit': 'GPa',
            'default': 200.0,
            'range': [0.1, 1000.0],
            'category': 'unknown_mechanical_properties',
            'identification_method': 'deformation_reconstruction'
        },
        'unknown_poisson_ratio': {
            'name': 'Unknown Poisson Ratio (ν)',
            'description': 'Poisson ratio to be identified from deformation data',
            'unit': 'dimensionless',
            'default': 0.3,
            'range': [0.0, 0.5],
            'category': 'unknown_mechanical_properties',
            'identification_method': 'deformation_reconstruction'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties'
        }
    },
    
    'inverse_nuclear_thermal': {
        'unknown_neutron_cross_section': {
            'name': 'Unknown Neutron Cross Section (σ)',
            'description': 'Neutron cross section to be identified from nuclear data',
            'unit': 'barn',
            'default': 1.0,
            'range': [1e-3, 1e3],
            'category': 'unknown_nuclear_properties',
            'identification_method': 'nuclear_reconstruction'
        },
        'unknown_thermal_conductivity': {
            'name': 'Unknown Thermal Conductivity (k)',
            'description': 'Thermal conductivity to be identified from thermal data',
            'unit': 'W/(m·K)',
            'default': 50.0,
            'range': [0.01, 1000.0],
            'category': 'unknown_thermal_properties',
            'identification_method': 'thermal_reconstruction'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties'
        },
        
    },
    
    'inverse_quantum_mechanical': {
        'unknown_potential_energy': {
            'name': 'Unknown Potential Energy (V)',
            'description': 'Potential energy to be identified from quantum data',
            'unit': 'J',
            'default': 1e-20,
            'range': [1e-25, 1e-15],
            'category': 'unknown_quantum_properties',
            'identification_method': 'quantum_reconstruction'
        },
        'unknown_wave_function': {
            'name': 'Unknown Wave Function (ψ)',
            'description': 'Wave function to be identified from quantum data',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'unknown_quantum_properties',
            'identification_method': 'wave_function_reconstruction'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1e-9,
            'range': [1e-12, 1e-6],
            'category': 'domain_properties'
        },
        
    },
    
    'inverse_phase_field_allen_cahn': {
        'unknown_mobility': {
            'name': 'Unknown Mobility (M)',
            'description': 'Phase field mobility to be identified from Allen-Cahn data',
            'unit': 'm²/(J·s)',
            'default': 1e-3,
            'range': [1e-6, 1e-1],
            'category': 'unknown_phase_field_properties',
            'identification_method': 'allen_cahn_reconstruction'
        },
        'unknown_free_energy_barrier': {
            'name': 'Unknown Free Energy Barrier (W)',
            'description': 'Free energy barrier to be identified from phase transitions',
            'unit': 'J/m³',
            'default': 1e6,
            'range': [1e3, 1e9],
            'category': 'unknown_phase_field_properties',
            'identification_method': 'energy_reconstruction'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1e-3,
            'range': [1e-6, 1e-1],
            'category': 'domain_properties'
        },
        
    },
    
    'inverse_phase_field_cahn_hilliard': {
        'unknown_mobility': {
            'name': 'Unknown Mobility (M)',
            'description': 'Phase field mobility to be identified from Cahn-Hilliard data',
            'unit': 'm²/(J·s)',
            'default': 1e-3,
            'range': [1e-6, 1e-1],
            'category': 'unknown_phase_field_properties',
            'identification_method': 'cahn_hilliard_reconstruction'
        },
        'unknown_gradient_coefficient': {
            'name': 'Unknown Gradient Coefficient (κ)',
            'description': 'Gradient coefficient to be identified from Cahn-Hilliard data',
            'unit': 'J·m',
            'default': 1e-9,
            'range': [1e-12, 1e-6],
            'category': 'unknown_phase_field_properties',
            'identification_method': 'gradient_reconstruction'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1e-3,
            'range': [1e-6, 1e-1],
            'category': 'domain_properties'
        },
        
    },
    
    'inverse_solidification_stefan': {
        'unknown_latent_heat': {
            'name': 'Unknown Latent Heat (L)',
            'description': 'Latent heat to be identified from solidification data',
            'unit': 'J/kg',
            'default': 3.34e5,
            'range': [1e4, 1e7],
            'category': 'unknown_thermal_properties',
            'identification_method': 'solidification_reconstruction'
        },
        'unknown_thermal_conductivity': {
            'name': 'Unknown Thermal Conductivity (k)',
            'description': 'Thermal conductivity to be identified from solidification data',
            'unit': 'W/(m·K)',
            'default': 50.0,
            'range': [0.01, 1000.0],
            'category': 'unknown_thermal_properties',
            'identification_method': 'thermal_reconstruction'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1e-2,
            'range': [1e-4, 1e-1],
            'category': 'domain_properties'
        },
        
    },
    
    'inverse_grain_growth': {
        'unknown_grain_boundary_energy': {
            'name': 'Unknown Grain Boundary Energy (γ)',
            'description': 'Grain boundary energy to be identified from grain growth data',
            'unit': 'J/m²',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'unknown_material_properties',
            'identification_method': 'grain_growth_reconstruction'
        },
        'unknown_mobility': {
            'name': 'Unknown Mobility (M)',
            'description': 'Grain boundary mobility to be identified from grain growth data',
            'unit': 'm²/(J·s)',
            'default': 1e-3,
            'range': [1e-6, 1e-1],
            'category': 'unknown_material_properties',
            'identification_method': 'mobility_reconstruction'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1e-3,
            'range': [1e-6, 1e-1],
            'category': 'domain_properties'
        },
        
    },
    
    'inverse_sintering': {
        'unknown_sintering_temperature': {
            'name': 'Unknown Sintering Temperature (T)',
            'description': 'Sintering temperature to be identified from sintering data',
            'unit': 'K',
            'default': 1500.0,
            'range': [1000.0, 2000.0],
            'category': 'unknown_thermal_properties',
            'identification_method': 'sintering_reconstruction'
        },
        'unknown_sintering_pressure': {
            'name': 'Unknown Sintering Pressure (P)',
            'description': 'Sintering pressure to be identified from sintering data',
            'unit': 'Pa',
            'default': 1e6,
            'range': [1e5, 1e8],
            'category': 'unknown_mechanical_properties',
            'identification_method': 'pressure_reconstruction'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1e-3,
            'range': [1e-6, 1e-1],
            'category': 'domain_properties'
        },
        
    },
    
    'inverse_laser_heat_source': {
        'unknown_laser_power': {
            'name': 'Unknown Laser Power (P)',
            'description': 'Laser power to be identified from thermal response data',
            'unit': 'W',
            'default': 1000.0,
            'range': [1.0, 10000.0],
            'category': 'unknown_am_properties',
            'identification_method': 'thermal_reconstruction'
        },
        'unknown_laser_radius': {
            'name': 'Unknown Laser Radius (r)',
            'description': 'Laser beam radius to be identified from thermal response data',
            'unit': 'm',
            'default': 1e-3,
            'range': [1e-5, 1e-2],
            'category': 'unknown_am_properties',
            'identification_method': 'beam_reconstruction'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1e-2,
            'range': [1e-4, 1e-1],
            'category': 'domain_properties'
        },
        
    },
    
    'inverse_melt_pool_dynamics': {
        'unknown_melt_pool_depth': {
            'name': 'Unknown Melt Pool Depth (d)',
            'description': 'Melt pool depth to be identified from melt pool data',
            'unit': 'm',
            'default': 1e-3,
            'range': [1e-5, 1e-2],
            'category': 'unknown_am_properties',
            'identification_method': 'melt_pool_reconstruction'
        },
        'unknown_melt_pool_width': {
            'name': 'Unknown Melt Pool Width (w)',
            'description': 'Melt pool width to be identified from melt pool data',
            'unit': 'm',
            'default': 2e-3,
            'range': [1e-5, 1e-2],
            'category': 'unknown_am_properties',
            'identification_method': 'melt_pool_reconstruction'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1e-2,
            'range': [1e-4, 1e-1],
            'category': 'domain_properties'
        },
        
    },
    
    'inverse_crystal_plasticity': {
        'unknown_critical_resolved_shear_stress': {
            'name': 'Unknown CRSS (τ₀)',
            'description': 'Critical resolved shear stress to be identified from plasticity data',
            'unit': 'MPa',
            'default': 100.0,
            'range': [1.0, 1000.0],
            'category': 'unknown_mechanical_properties',
            'identification_method': 'plasticity_reconstruction'
        },
        'unknown_hardening_modulus': {
            'name': 'Unknown Hardening Modulus (h)',
            'description': 'Hardening modulus to be identified from plasticity data',
            'unit': 'MPa',
            'default': 1000.0,
            'range': [10.0, 10000.0],
            'category': 'unknown_mechanical_properties',
            'identification_method': 'hardening_reconstruction'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1e-3,
            'range': [1e-6, 1e-1],
            'category': 'domain_properties'
        },
        
    },
    
    'inverse_diffusion_solids': {
        'unknown_diffusion_coefficient': {
            'name': 'Unknown Diffusion Coefficient (D)',
            'description': 'Diffusion coefficient to be identified from solid diffusion data',
            'unit': 'm²/s',
            'default': 1e-12,
            'range': [1e-15, 1e-9],
            'category': 'unknown_transport_properties',
            'identification_method': 'diffusion_reconstruction'
        },
        'unknown_activation_energy': {
            'name': 'Unknown Activation Energy (Eₐ)',
            'description': 'Activation energy to be identified from diffusion data',
            'unit': 'J/mol',
            'default': 1e5,
            'range': [1e4, 1e6],
            'category': 'unknown_transport_properties',
            'identification_method': 'activation_reconstruction'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1e-3,
            'range': [1e-6, 1e-1],
            'category': 'domain_properties'
        },
        
    },
    
    'inverse_precipitation_nucleation': {
        'unknown_nucleation_rate': {
            'name': 'Unknown Nucleation Rate (J)',
            'description': 'Nucleation rate to be identified from precipitation data',
            'unit': '1/(m³·s)',
            'default': 1e12,
            'range': [1e8, 1e16],
            'category': 'unknown_kinetic_properties',
            'identification_method': 'nucleation_reconstruction'
        },
        'unknown_growth_rate': {
            'name': 'Unknown Growth Rate (G)',
            'description': 'Growth rate to be identified from precipitation data',
            'unit': 'm/s',
            'default': 1e-9,
            'range': [1e-12, 1e-6],
            'category': 'unknown_kinetic_properties',
            'identification_method': 'growth_reconstruction'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1e-3,
            'range': [1e-6, 1e-1],
            'category': 'domain_properties'
        },
        
    },
    
    'inverse_residual_stress': {
        'unknown_residual_stress_magnitude': {
            'name': 'Unknown Residual Stress Magnitude (σᵣ)',
            'description': 'Residual stress magnitude to be identified from stress data',
            'unit': 'MPa',
            'default': 100.0,
            'range': [1.0, 1000.0],
            'category': 'unknown_mechanical_properties',
            'identification_method': 'stress_reconstruction'
        },
        'unknown_stress_distribution': {
            'name': 'Unknown Stress Distribution (f)',
            'description': 'Stress distribution function to be identified from stress data',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'unknown_mechanical_properties',
            'identification_method': 'distribution_reconstruction'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1e-2,
            'range': [1e-4, 1e-1],
            'category': 'domain_properties'
        }
    },
    
    'inverse_microstructure_evolution': {
        'unknown_evolution_rate': {
            'name': 'Unknown Evolution Rate (k)',
            'description': 'Microstructure evolution rate to be identified from evolution data',
            'unit': '1/s',
            'default': 1e-3,
            'range': [1e-6, 1e0],
            'category': 'unknown_kinetic_properties',
            'identification_method': 'evolution_reconstruction'
        },
        'unknown_equilibrium_state': {
            'name': 'Unknown Equilibrium State (φₑ)',
            'description': 'Equilibrium microstructure state to be identified',
            'unit': 'dimensionless',
            'default': 0.5,
            'range': [0.0, 1.0],
            'category': 'unknown_equilibrium_properties',
            'identification_method': 'equilibrium_reconstruction'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1e-3,
            'range': [1e-6, 1e-1],
            'category': 'domain_properties'
        },
        
    }
} 