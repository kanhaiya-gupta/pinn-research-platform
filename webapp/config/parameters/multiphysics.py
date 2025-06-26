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