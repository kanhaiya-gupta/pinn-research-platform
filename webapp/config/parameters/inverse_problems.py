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