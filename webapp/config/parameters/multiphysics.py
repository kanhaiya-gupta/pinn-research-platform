"""
Multiphysics Parameters
Parameters for coupled physical phenomena and multiphysics systems.
"""

MULTIPHYSICS_PARAMETERS_DICT = {
    # Coupling Parameters
    'coupling_strength': {
        'name': 'Coupling Strength',
        'description': 'Strength of coupling between physical fields',
        'unit': 'dimensionless',
        'default': 1.0,
        'range': [0.0, 10.0],
        'category': 'coupling_parameters',
        'coupling_type': 'bidirectional'
    },
    'thermal_mechanical_coupling': {
        'name': 'Thermal-Mechanical Coupling',
        'description': 'Coupling coefficient between thermal and mechanical fields',
        'unit': '1/K',
        'default': 1e-5,
        'range': [1e-7, 1e-3],
        'category': 'coupling_parameters',
        'coupling_type': 'thermoelasticity'
    },
    'electromagnetic_thermal_coupling': {
        'name': 'Electromagnetic-Thermal Coupling',
        'description': 'Coupling coefficient between EM and thermal fields',
        'unit': 'W/(m³·A²)',
        'default': 1e-3,
        'range': [1e-6, 1e-1],
        'category': 'coupling_parameters',
        'coupling_type': 'electromagnetic_thermal'
    },
    'fluid_structure_coupling': {
        'name': 'Fluid-Structure Coupling',
        'description': 'Coupling coefficient between fluid and structural fields',
        'unit': 'N/(m³·Pa)',
        'default': 1.0,
        'range': [0.1, 10.0],
        'category': 'coupling_parameters',
        'coupling_type': 'fluid_structure_interaction'
    },
    'phase_field_mechanics_coupling': {
        'name': 'Phase Field-Mechanics Coupling',
        'description': 'Coupling coefficient between phase field and mechanics',
        'unit': 'J/m³',
        'default': 1e6,
        'range': [1e3, 1e9],
        'category': 'coupling_parameters',
        'coupling_type': 'phase_field_mechanics'
    },
    
    # Thermoelasticity Parameters
    'thermal_expansion_coefficient': {
        'name': 'Thermal Expansion Coefficient',
        'description': 'Coefficient of thermal expansion',
        'unit': '1/K',
        'default': 1e-5,
        'range': [1e-7, 1e-3],
        'category': 'thermoelasticity_parameters',
        'coupling_type': 'thermoelasticity'
    },
    'thermal_stress_coefficient': {
        'name': 'Thermal Stress Coefficient',
        'description': 'Coefficient for thermal stress calculation',
        'unit': 'Pa/K',
        'default': 1e6,
        'range': [1e3, 1e9],
        'category': 'thermoelasticity_parameters',
        'coupling_type': 'thermoelasticity'
    },
    'thermoelastic_dissipation': {
        'name': 'Thermoelastic Dissipation',
        'description': 'Thermoelastic dissipation coefficient',
        'unit': 'W/(m³·K)',
        'default': 1e-3,
        'range': [1e-6, 1e-1],
        'category': 'thermoelasticity_parameters',
        'coupling_type': 'thermoelasticity'
    },
    
    # Electromagnetic-Thermal Parameters
    'joule_heating_coefficient': {
        'name': 'Joule Heating Coefficient',
        'description': 'Coefficient for Joule heating',
        'unit': 'W/(m³·A²)',
        'default': 1e-3,
        'range': [1e-6, 1e-1],
        'category': 'electromagnetic_thermal_parameters',
        'coupling_type': 'electromagnetic_thermal'
    },
    'electromagnetic_loss': {
        'name': 'Electromagnetic Loss',
        'description': 'Electromagnetic loss coefficient',
        'unit': 'W/m³',
        'default': 1e-3,
        'range': [1e-6, 1e-1],
        'category': 'electromagnetic_thermal_parameters',
        'coupling_type': 'electromagnetic_thermal'
    },
    'eddy_current_coefficient': {
        'name': 'Eddy Current Coefficient',
        'description': 'Coefficient for eddy current losses',
        'unit': 'W/(m³·T²)',
        'default': 1e-3,
        'range': [1e-6, 1e-1],
        'category': 'electromagnetic_thermal_parameters',
        'coupling_type': 'electromagnetic_thermal'
    },
    
    # Fluid-Structure Interaction Parameters
    'added_mass_coefficient': {
        'name': 'Added Mass Coefficient',
        'description': 'Added mass coefficient for FSI',
        'unit': 'kg/m³',
        'default': 1000.0,
        'range': [100.0, 10000.0],
        'category': 'fsi_parameters',
        'coupling_type': 'fluid_structure_interaction'
    },
    'hydrodynamic_damping': {
        'name': 'Hydrodynamic Damping',
        'description': 'Hydrodynamic damping coefficient',
        'unit': 'N·s/m',
        'default': 1.0,
        'range': [0.1, 10.0],
        'category': 'fsi_parameters',
        'coupling_type': 'fluid_structure_interaction'
    },
    'interface_stiffness': {
        'name': 'Interface Stiffness',
        'description': 'Stiffness at fluid-structure interface',
        'unit': 'N/m³',
        'default': 1e6,
        'range': [1e3, 1e9],
        'category': 'fsi_parameters',
        'coupling_type': 'fluid_structure_interaction'
    },
    
    # Phase Field Coupling Parameters
    'phase_field_elastic_coupling': {
        'name': 'Phase Field-Elastic Coupling',
        'description': 'Coupling between phase field and elastic energy',
        'unit': 'J/m³',
        'default': 1e6,
        'range': [1e3, 1e9],
        'category': 'phase_field_coupling_parameters',
        'coupling_type': 'phase_field_mechanics'
    },
    'phase_field_thermal_coupling': {
        'name': 'Phase Field-Thermal Coupling',
        'description': 'Coupling between phase field and thermal energy',
        'unit': 'J/(m³·K)',
        'default': 1e3,
        'range': [1e0, 1e6],
        'category': 'phase_field_coupling_parameters',
        'coupling_type': 'phase_field_thermal'
    },
    'phase_field_chemical_coupling': {
        'name': 'Phase Field-Chemical Coupling',
        'description': 'Coupling between phase field and chemical energy',
        'unit': 'J/m³',
        'default': 1e6,
        'range': [1e3, 1e9],
        'category': 'phase_field_coupling_parameters',
        'coupling_type': 'phase_field_chemical'
    },
    
    # Poroelasticity Parameters
    'biot_coefficient': {
        'name': 'Biot Coefficient',
        'description': 'Biot coefficient for poroelasticity',
        'unit': 'dimensionless',
        'default': 0.8,
        'range': [0.0, 1.0],
        'category': 'poroelasticity_parameters',
        'coupling_type': 'poroelasticity'
    },
    'skempton_coefficient': {
        'name': 'Skempton Coefficient',
        'description': 'Skempton coefficient for poroelasticity',
        'unit': 'dimensionless',
        'default': 0.5,
        'range': [0.0, 1.0],
        'category': 'poroelasticity_parameters',
        'coupling_type': 'poroelasticity'
    },
    'storage_coefficient': {
        'name': 'Storage Coefficient',
        'description': 'Storage coefficient for poroelasticity',
        'unit': '1/Pa',
        'default': 1e-9,
        'range': [1e-12, 1e-6],
        'category': 'poroelasticity_parameters',
        'coupling_type': 'poroelasticity'
    },
    
    # Viscoelasticity Parameters
    'relaxation_time': {
        'name': 'Relaxation Time',
        'description': 'Viscoelastic relaxation time',
        'unit': 's',
        'default': 1.0,
        'range': [1e-3, 1e3],
        'category': 'viscoelasticity_parameters',
        'coupling_type': 'viscoelasticity'
    },
    'retardation_time': {
        'name': 'Retardation Time',
        'description': 'Viscoelastic retardation time',
        'unit': 's',
        'default': 0.1,
        'range': [1e-4, 1e2],
        'category': 'viscoelasticity_parameters',
        'coupling_type': 'viscoelasticity'
    },
    'viscoelastic_modulus': {
        'name': 'Viscoelastic Modulus',
        'description': 'Viscoelastic modulus',
        'unit': 'Pa',
        'default': 1e9,
        'range': [1e6, 1e12],
        'category': 'viscoelasticity_parameters',
        'coupling_type': 'viscoelasticity'
    },
    
    # Magnetohydrodynamics Parameters
    'magnetic_reynolds_number': {
        'name': 'Magnetic Reynolds Number',
        'description': 'Magnetic Reynolds number for MHD',
        'unit': 'dimensionless',
        'default': 1.0,
        'range': [0.1, 100.0],
        'category': 'mhd_parameters',
        'coupling_type': 'magnetohydrodynamics'
    },
    'alfven_speed': {
        'name': 'Alfven Speed',
        'description': 'Alfven speed for MHD waves',
        'unit': 'm/s',
        'default': 1000.0,
        'range': [10.0, 10000.0],
        'category': 'mhd_parameters',
        'coupling_type': 'magnetohydrodynamics'
    },
    'magnetic_prandtl_number': {
        'name': 'Magnetic Prandtl Number',
        'description': 'Magnetic Prandtl number',
        'unit': 'dimensionless',
        'default': 1.0,
        'range': [0.1, 10.0],
        'category': 'mhd_parameters',
        'coupling_type': 'magnetohydrodynamics'
    },
    
    # Additive Manufacturing Parameters
    'laser_material_coupling': {
        'name': 'Laser-Material Coupling',
        'description': 'Coupling between laser and material response',
        'unit': 'W/(m³·W)',
        'default': 1e-3,
        'range': [1e-6, 1e-1],
        'category': 'am_parameters',
        'coupling_type': 'additive_manufacturing'
    },
    'melt_pool_thermomechanics': {
        'name': 'Melt Pool Thermomechanics',
        'description': 'Coupling in melt pool thermomechanics',
        'unit': 'N/(m³·K)',
        'default': 1e6,
        'range': [1e3, 1e9],
        'category': 'am_parameters',
        'coupling_type': 'additive_manufacturing'
    },
    'powder_fluid_coupling': {
        'name': 'Powder-Fluid Coupling',
        'description': 'Coupling between powder and fluid dynamics',
        'unit': 'kg/(m³·s)',
        'default': 1e-3,
        'range': [1e-6, 1e-1],
        'category': 'am_parameters',
        'coupling_type': 'additive_manufacturing'
    },
    
    # Coupling Solution Parameters
    'coupling_iterations': {
        'name': 'Coupling Iterations',
        'description': 'Number of coupling iterations',
        'unit': 'dimensionless',
        'default': 10,
        'range': [1, 100],
        'category': 'solution_parameters',
        'coupling_type': 'general'
    },
    'coupling_tolerance': {
        'name': 'Coupling Tolerance',
        'description': 'Tolerance for coupling convergence',
        'unit': 'dimensionless',
        'default': 1e-6,
        'range': [1e-12, 1e-3],
        'category': 'solution_parameters',
        'coupling_type': 'general'
    },
    'coupling_relaxation': {
        'name': 'Coupling Relaxation',
        'description': 'Relaxation factor for coupling',
        'unit': 'dimensionless',
        'default': 0.5,
        'range': [0.1, 1.0],
        'category': 'solution_parameters',
        'coupling_type': 'general'
    },
    
    # Time Integration Parameters
    'coupling_timestep': {
        'name': 'Coupling Timestep',
        'description': 'Timestep for coupled simulations',
        'unit': 's',
        'default': 1e-3,
        'range': [1e-6, 1e-1],
        'category': 'time_integration_parameters',
        'coupling_type': 'general'
    },
    'subcycling_ratio': {
        'name': 'Subcycling Ratio',
        'description': 'Ratio for subcycling in coupled simulations',
        'unit': 'dimensionless',
        'default': 1,
        'range': [1, 100],
        'category': 'time_integration_parameters',
        'coupling_type': 'general'
    }
}

# Equation-specific parameters for multiphysics simulations
MULTIPHYSICS_EQUATION_PARAMETERS = {
    'multiphysics_thermoelasticity': {
        'thermal_expansion_coefficient': {'default': 1e-5, 'range': [1e-7, 1e-3]},
        'thermal_stress_coefficient': {'default': 1e6, 'range': [1e3, 1e9]},
        'coupling_strength': {'default': 1.0, 'range': [0.0, 10.0]},
        'coupling_iterations': {'default': 10, 'range': [1, 100]},
        'coupling_tolerance': {'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'multiphysics_electromagnetic_thermal': {
        'joule_heating_coefficient': {'default': 1e-3, 'range': [1e-6, 1e-1]},
        'electromagnetic_loss': {'default': 1e-3, 'range': [1e-6, 1e-1]},
        'coupling_strength': {'default': 1.0, 'range': [0.0, 10.0]},
        'coupling_iterations': {'default': 10, 'range': [1, 100]},
        'coupling_tolerance': {'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'multiphysics_fluid_structure_interaction': {
        'added_mass_coefficient': {'default': 1000.0, 'range': [100.0, 10000.0]},
        'hydrodynamic_damping': {'default': 1.0, 'range': [0.1, 10.0]},
        'interface_stiffness': {'default': 1e6, 'range': [1e3, 1e9]},
        'coupling_iterations': {'default': 15, 'range': [5, 50]},
        'coupling_tolerance': {'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'multiphysics_biomechanical_transport': {
        'elastic_modulus': {'default': 1e6, 'range': [1e3, 1e9]},
        'diffusion_coefficient': {'default': 1e-9, 'range': [1e-12, 1e-6]},
        'coupling_strength': {'default': 1.0, 'range': [0.0, 10.0]},
        'coupling_iterations': {'default': 10, 'range': [1, 100]},
        'coupling_tolerance': {'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'multiphysics_geophysical_flow': {
        'coriolis_parameter': {'default': 1e-4, 'range': [1e-5, 1e-3]},
        'friction_coefficient': {'default': 0.01, 'range': [1e-4, 1e-1]},
        'coupling_strength': {'default': 1.0, 'range': [0.0, 10.0]},
        'coupling_iterations': {'default': 10, 'range': [1, 100]},
        'coupling_tolerance': {'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'multiphysics_atmospheric_oceanic': {
        'atmospheric_coupling': {'default': 1.0, 'range': [0.1, 10.0]},
        'oceanic_coupling': {'default': 1.0, 'range': [0.1, 10.0]},
        'coupling_strength': {'default': 1.0, 'range': [0.0, 10.0]},
        'coupling_iterations': {'default': 20, 'range': [10, 100]},
        'coupling_tolerance': {'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'multiphysics_nuclear_thermal': {
        'nuclear_cross_section': {'default': 1e-24, 'range': [1e-28, 1e-20]},
        'neutron_flux': {'default': 1e14, 'range': [1e10, 1e18]},
        'coupling_strength': {'default': 1.0, 'range': [0.0, 10.0]},
        'coupling_iterations': {'default': 15, 'range': [5, 50]},
        'coupling_tolerance': {'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'multiphysics_magnetohydrodynamics': {
        'magnetic_reynolds_number': {'default': 1.0, 'range': [0.1, 100.0]},
        'alfven_speed': {'default': 1000.0, 'range': [10.0, 10000.0]},
        'magnetic_prandtl_number': {'default': 1.0, 'range': [0.1, 10.0]},
        'coupling_iterations': {'default': 15, 'range': [5, 50]},
        'coupling_tolerance': {'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'multiphysics_poroelasticity': {
        'biot_coefficient': {'default': 0.8, 'range': [0.0, 1.0]},
        'skempton_coefficient': {'default': 0.5, 'range': [0.0, 1.0]},
        'storage_coefficient': {'default': 1e-9, 'range': [1e-12, 1e-6]},
        'coupling_iterations': {'default': 10, 'range': [1, 100]},
        'coupling_tolerance': {'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'multiphysics_viscoelasticity': {
        'relaxation_time': {'default': 1.0, 'range': [1e-3, 1e3]},
        'retardation_time': {'default': 0.1, 'range': [1e-4, 1e2]},
        'viscoelastic_modulus': {'default': 1e9, 'range': [1e6, 1e12]},
        'coupling_iterations': {'default': 10, 'range': [1, 100]},
        'coupling_tolerance': {'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'multiphysics_radiative_transfer': {
        'absorption_coefficient': {'default': 1.0, 'range': [1e-3, 1e3]},
        'scattering_coefficient': {'default': 0.1, 'range': [1e-4, 1e2]},
        'coupling_strength': {'default': 1.0, 'range': [0.0, 10.0]},
        'coupling_iterations': {'default': 15, 'range': [5, 50]},
        'coupling_tolerance': {'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'multiphysics_phase_field': {
        'phase_field_elastic_coupling': {'default': 1e6, 'range': [1e3, 1e9]},
        'mobility': {'default': 1.0, 'range': [1e-3, 1e3]},
        'interface_energy': {'default': 1.0, 'range': [1e-3, 1e3]},
        'coupling_iterations': {'default': 10, 'range': [1, 100]},
        'coupling_tolerance': {'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'multiphysics_reaction_diffusion': {
        'diffusion_coefficient': {'default': 1e-9, 'range': [1e-12, 1e-6]},
        'reaction_rate': {'default': 1e-3, 'range': [1e-6, 1e-1]},
        'coupling_strength': {'default': 1.0, 'range': [0.0, 10.0]},
        'coupling_iterations': {'default': 10, 'range': [1, 100]},
        'coupling_tolerance': {'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'multiphysics_advection_diffusion': {
        'velocity': {'default': 1.0, 'range': [1e-3, 1e3]},
        'diffusion_coefficient': {'default': 1e-9, 'range': [1e-12, 1e-6]},
        'coupling_strength': {'default': 1.0, 'range': [0.0, 10.0]},
        'coupling_iterations': {'default': 10, 'range': [1, 100]},
        'coupling_tolerance': {'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'multiphysics_elastic_wave': {
        'elastic_modulus': {'default': 1e9, 'range': [1e6, 1e12]},
        'density': {'default': 1000.0, 'range': [100.0, 10000.0]},
        'coupling_strength': {'default': 1.0, 'range': [0.0, 10.0]},
        'coupling_iterations': {'default': 10, 'range': [1, 100]},
        'coupling_tolerance': {'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'multiphysics_quantum_mechanical': {
        'potential_energy': {'default': 1.0, 'range': [1e-3, 1e3]},
        'wave_function': {'default': 1.0, 'range': [1e-3, 1e3]},
        'coupling_strength': {'default': 1.0, 'range': [0.0, 10.0]},
        'coupling_iterations': {'default': 10, 'range': [1, 100]},
        'coupling_tolerance': {'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'multiphysics_thermoelectric': {
        'seebeck_coefficient': {'default': 1e-5, 'range': [1e-7, 1e-3]},
        'thermal_conductivity': {'default': 1.0, 'range': [1e-3, 1e3]},
        'electrical_conductivity': {'default': 1e6, 'range': [1e3, 1e9]},
        'coupling_iterations': {'default': 10, 'range': [1, 100]},
        'coupling_tolerance': {'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'multiphysics_electrochemical': {
        'electrical_conductivity': {'default': 1e6, 'range': [1e3, 1e9]},
        'reaction_rate': {'default': 1e-3, 'range': [1e-6, 1e-1]},
        'coupling_strength': {'default': 1.0, 'range': [0.0, 10.0]},
        'coupling_iterations': {'default': 10, 'range': [1, 100]},
        'coupling_tolerance': {'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'multiphysics_thermochemical': {
        'thermal_conductivity': {'default': 1.0, 'range': [1e-3, 1e3]},
        'reaction_rate': {'default': 1e-3, 'range': [1e-6, 1e-1]},
        'coupling_strength': {'default': 1.0, 'range': [0.0, 10.0]},
        'coupling_iterations': {'default': 10, 'range': [1, 100]},
        'coupling_tolerance': {'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'multiphysics_mechanical_electrical': {
        'elastic_modulus': {'default': 1e9, 'range': [1e6, 1e12]},
        'electrical_conductivity': {'default': 1e6, 'range': [1e3, 1e9]},
        'piezoelectric_coefficient': {'default': 1e-9, 'range': [1e-12, 1e-6]},
        'coupling_iterations': {'default': 10, 'range': [1, 100]},
        'coupling_tolerance': {'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'multiphysics_optical_mechanical': {
        'optical_index': {'default': 1.5, 'range': [1.0, 3.0]},
        'elastic_modulus': {'default': 1e9, 'range': [1e6, 1e12]},
        'coupling_strength': {'default': 1.0, 'range': [0.0, 10.0]},
        'coupling_iterations': {'default': 10, 'range': [1, 100]},
        'coupling_tolerance': {'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'multiphysics_magnetic_mechanical': {
        'magnetic_permeability': {'default': 1e-6, 'range': [1e-9, 1e-3]},
        'elastic_modulus': {'default': 1e9, 'range': [1e6, 1e12]},
        'magnetostrictive_coefficient': {'default': 1e-5, 'range': [1e-7, 1e-3]},
        'coupling_iterations': {'default': 10, 'range': [1, 100]},
        'coupling_tolerance': {'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'multiphysics_acoustic_elastic': {
        'acoustic_speed': {'default': 340.0, 'range': [100.0, 1000.0]},
        'elastic_modulus': {'default': 1e9, 'range': [1e6, 1e12]},
        'coupling_strength': {'default': 1.0, 'range': [0.0, 10.0]},
        'coupling_iterations': {'default': 10, 'range': [1, 100]},
        'coupling_tolerance': {'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'multiphysics_thermal_optical': {
        'thermal_conductivity': {'default': 1.0, 'range': [1e-3, 1e3]},
        'optical_index': {'default': 1.5, 'range': [1.0, 3.0]},
        'thermo_optic_coefficient': {'default': 1e-5, 'range': [1e-7, 1e-3]},
        'coupling_iterations': {'default': 10, 'range': [1, 100]},
        'coupling_tolerance': {'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'multiphysics_chemical_mechanical': {
        'reaction_rate': {'default': 1e-3, 'range': [1e-6, 1e-1]},
        'elastic_modulus': {'default': 1e9, 'range': [1e6, 1e12]},
        'coupling_strength': {'default': 1.0, 'range': [0.0, 10.0]},
        'coupling_iterations': {'default': 10, 'range': [1, 100]},
        'coupling_tolerance': {'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'multiphysics_biological_mechanical': {
        'biological_rate': {'default': 1e-3, 'range': [1e-6, 1e-1]},
        'elastic_modulus': {'default': 1e6, 'range': [1e3, 1e9]},
        'coupling_strength': {'default': 1.0, 'range': [0.0, 10.0]},
        'coupling_iterations': {'default': 10, 'range': [1, 100]},
        'coupling_tolerance': {'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'phase_field_mechanics': {
        'phase_field_elastic_coupling': {'default': 1e6, 'range': [1e3, 1e9]},
        'mobility': {'default': 1.0, 'range': [1e-3, 1e3]},
        'interface_energy': {'default': 1.0, 'range': [1e-3, 1e3]},
        'coupling_iterations': {'default': 10, 'range': [1, 100]},
        'coupling_tolerance': {'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'phase_field_heat': {
        'phase_field_thermal_coupling': {'default': 1e3, 'range': [1e0, 1e6]},
        'mobility': {'default': 1.0, 'range': [1e-3, 1e3]},
        'thermal_conductivity': {'default': 1.0, 'range': [1e-3, 1e3]},
        'coupling_iterations': {'default': 10, 'range': [1, 100]},
        'coupling_tolerance': {'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'solidification_mechanics': {
        'latent_heat': {'default': 1e6, 'range': [1e3, 1e9]},
        'elastic_modulus': {'default': 1e9, 'range': [1e6, 1e12]},
        'coupling_strength': {'default': 1.0, 'range': [0.0, 10.0]},
        'coupling_iterations': {'default': 10, 'range': [1, 100]},
        'coupling_tolerance': {'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'sintering_mechanics': {
        'sintering_rate': {'default': 1e-3, 'range': [1e-6, 1e-1]},
        'elastic_modulus': {'default': 1e9, 'range': [1e6, 1e12]},
        'coupling_strength': {'default': 1.0, 'range': [0.0, 10.0]},
        'coupling_iterations': {'default': 10, 'range': [1, 100]},
        'coupling_tolerance': {'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'laser_material_interaction': {
        'laser_material_coupling': {'default': 1e-3, 'range': [1e-6, 1e-1]},
        'absorption_coefficient': {'default': 1.0, 'range': [1e-3, 1e3]},
        'coupling_strength': {'default': 1.0, 'range': [0.0, 10.0]},
        'coupling_iterations': {'default': 10, 'range': [1, 100]},
        'coupling_tolerance': {'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'melt_pool_thermomechanics': {
        'melt_pool_thermomechanics': {'default': 1e6, 'range': [1e3, 1e9]},
        'surface_tension': {'default': 1.0, 'range': [1e-3, 1e3]},
        'coupling_strength': {'default': 1.0, 'range': [0.0, 10.0]},
        'coupling_iterations': {'default': 15, 'range': [5, 50]},
        'coupling_tolerance': {'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'crystal_plasticity_heat': {
        'critical_resolved_shear_stress': {'default': 1e6, 'range': [1e3, 1e9]},
        'thermal_conductivity': {'default': 1.0, 'range': [1e-3, 1e3]},
        'coupling_strength': {'default': 1.0, 'range': [0.0, 10.0]},
        'coupling_iterations': {'default': 10, 'range': [1, 100]},
        'coupling_tolerance': {'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'diffusion_mechanics': {
        'diffusion_coefficient': {'default': 1e-9, 'range': [1e-12, 1e-6]},
        'elastic_modulus': {'default': 1e9, 'range': [1e6, 1e12]},
        'coupling_strength': {'default': 1.0, 'range': [0.0, 10.0]},
        'coupling_iterations': {'default': 10, 'range': [1, 100]},
        'coupling_tolerance': {'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'precipitation_mechanics': {
        'nucleation_rate': {'default': 1e-3, 'range': [1e-6, 1e-1]},
        'elastic_modulus': {'default': 1e9, 'range': [1e6, 1e12]},
        'coupling_strength': {'default': 1.0, 'range': [0.0, 10.0]},
        'coupling_iterations': {'default': 10, 'range': [1, 100]},
        'coupling_tolerance': {'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'grain_growth_mechanics': {
        'mobility': {'default': 1.0, 'range': [1e-3, 1e3]},
        'elastic_modulus': {'default': 1e9, 'range': [1e6, 1e12]},
        'coupling_strength': {'default': 1.0, 'range': [0.0, 10.0]},
        'coupling_iterations': {'default': 10, 'range': [1, 100]},
        'coupling_tolerance': {'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'additive_manufacturing_process': {
        'laser_material_coupling': {'default': 1e-3, 'range': [1e-6, 1e-1]},
        'melt_pool_thermomechanics': {'default': 1e6, 'range': [1e3, 1e9]},
        'powder_fluid_coupling': {'default': 1e-3, 'range': [1e-6, 1e-1]},
        'coupling_iterations': {'default': 20, 'range': [10, 100]},
        'coupling_tolerance': {'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'material_processing_thermomechanics': {
        'thermal_conductivity': {'default': 1.0, 'range': [1e-3, 1e3]},
        'elastic_modulus': {'default': 1e9, 'range': [1e6, 1e12]},
        'phase_transformation_rate': {'default': 1e-3, 'range': [1e-6, 1e-1]},
        'coupling_iterations': {'default': 15, 'range': [5, 50]},
        'coupling_tolerance': {'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'microstructure_mechanics': {
        'phase_field_mobility': {'default': 1.0, 'range': [1e-3, 1e3]},
        'elastic_modulus': {'default': 1e9, 'range': [1e6, 1e12]},
        'interface_energy': {'default': 1.0, 'range': [1e-3, 1e3]},
        'coupling_iterations': {'default': 15, 'range': [5, 50]},
        'coupling_tolerance': {'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'powder_processing_thermomechanics': {
        'powder_flow_rate': {'default': 1e-3, 'range': [1e-6, 1e-1]},
        'thermal_conductivity': {'default': 1.0, 'range': [1e-3, 1e3]},
        'elastic_modulus': {'default': 1e9, 'range': [1e6, 1e12]},
        'coupling_iterations': {'default': 15, 'range': [5, 50]},
        'coupling_tolerance': {'default': 1e-6, 'range': [1e-12, 1e-3]}
    }
} 