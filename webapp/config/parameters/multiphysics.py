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
    },
    
    # Geophysical Flow Parameters
    'coriolis_parameter': {
        'name': 'Coriolis Parameter',
        'description': 'Coriolis parameter for geophysical flows',
        'unit': '1/s',
        'default': 1e-4,
        'range': [1e-5, 1e-3],
        'category': 'geophysical_parameters',
        'coupling_type': 'geophysical_flow'
    },
    'friction_coefficient': {
        'name': 'Friction Coefficient',
        'description': 'Bottom friction coefficient for shallow water flows',
        'unit': 'dimensionless',
        'default': 0.01,
        'range': [1e-4, 1e-1],
        'category': 'geophysical_parameters',
        'coupling_type': 'geophysical_flow'
    },
    'gravity': {
        'name': 'Gravity',
        'description': 'Gravitational acceleration',
        'unit': 'm/s²',
        'default': 9.81,
        'range': [1.0, 20.0],
        'category': 'geophysical_parameters',
        'coupling_type': 'geophysical_flow'
    },
    
    # Radiative Transfer Parameters
    'absorption_coefficient': {
        'name': 'Absorption Coefficient',
        'description': 'Absorption coefficient for radiative transfer',
        'unit': '1/m',
        'default': 1.0,
        'range': [1e-3, 1e3],
        'category': 'radiative_parameters',
        'coupling_type': 'radiative_transfer'
    },
    'scattering_coefficient': {
        'name': 'Scattering Coefficient',
        'description': 'Scattering coefficient for radiative transfer',
        'unit': '1/m',
        'default': 0.1,
        'range': [1e-4, 1e2],
        'category': 'radiative_parameters',
        'coupling_type': 'radiative_transfer'
    },
    'emissivity': {
        'name': 'Emissivity',
        'description': 'Surface emissivity for thermal radiation',
        'unit': 'dimensionless',
        'default': 0.8,
        'range': [0.0, 1.0],
        'category': 'radiative_parameters',
        'coupling_type': 'radiative_transfer'
    },
    
    # Reaction-Diffusion Parameters
    'diffusion_coefficient': {
        'name': 'Diffusion Coefficient',
        'description': 'Diffusion coefficient for transport processes',
        'unit': 'm²/s',
        'default': 1e-9,
        'range': [1e-12, 1e-6],
        'category': 'transport_parameters',
        'coupling_type': 'reaction_diffusion'
    },
    'reaction_rate': {
        'name': 'Reaction Rate',
        'description': 'Chemical reaction rate constant',
        'unit': '1/s',
        'default': 1e-3,
        'range': [1e-6, 1e-1],
        'category': 'chemical_parameters',
        'coupling_type': 'reaction_diffusion'
    },
    'activation_energy': {
        'name': 'Activation Energy',
        'description': 'Activation energy for chemical reactions',
        'unit': 'J/mol',
        'default': 1e5,
        'range': [1e3, 1e6],
        'category': 'chemical_parameters',
        'coupling_type': 'reaction_diffusion'
    },
    
    # Advection-Diffusion Parameters
    'velocity': {
        'name': 'Velocity',
        'description': 'Flow velocity for advection',
        'unit': 'm/s',
        'default': 1.0,
        'range': [1e-3, 1e3],
        'category': 'transport_parameters',
        'coupling_type': 'advection_diffusion'
    },
    'peclet_number': {
        'name': 'Peclet Number',
        'description': 'Peclet number for advection-diffusion',
        'unit': 'dimensionless',
        'default': 1.0,
        'range': [0.1, 100.0],
        'category': 'transport_parameters',
        'coupling_type': 'advection_diffusion'
    },
    
    # Elastic Wave Parameters
    'elastic_modulus': {
        'name': 'Elastic Modulus',
        'description': 'Elastic modulus for wave propagation',
        'unit': 'Pa',
        'default': 1e9,
        'range': [1e6, 1e12],
        'category': 'mechanical_parameters',
        'coupling_type': 'elastic_wave'
    },
    'density': {
        'name': 'Density',
        'description': 'Material density',
        'unit': 'kg/m³',
        'default': 1000.0,
        'range': [100.0, 10000.0],
        'category': 'mechanical_parameters',
        'coupling_type': 'elastic_wave'
    },
    'poisson_ratio': {
        'name': 'Poisson Ratio',
        'description': 'Poisson ratio for elastic materials',
        'unit': 'dimensionless',
        'default': 0.3,
        'range': [0.0, 0.5],
        'category': 'mechanical_parameters',
        'coupling_type': 'elastic_wave'
    },
    
    # Quantum Mechanical Parameters
    'potential_energy': {
        'name': 'Potential Energy',
        'description': 'Potential energy for quantum systems',
        'unit': 'J',
        'default': 1.0,
        'range': [1e-3, 1e3],
        'category': 'quantum_parameters',
        'coupling_type': 'quantum_mechanical'
    },
    'wave_function': {
        'name': 'Wave Function',
        'description': 'Wave function amplitude',
        'unit': 'dimensionless',
        'default': 1.0,
        'range': [1e-3, 1e3],
        'category': 'quantum_parameters',
        'coupling_type': 'quantum_mechanical'
    },
    'planck_constant': {
        'name': 'Planck Constant',
        'description': 'Reduced Planck constant',
        'unit': 'J·s',
        'default': 1.055e-34,
        'range': [1e-35, 1e-33],
        'category': 'quantum_parameters',
        'coupling_type': 'quantum_mechanical'
    },
    
    # Thermoelectric Parameters
    'seebeck_coefficient': {
        'name': 'Seebeck Coefficient',
        'description': 'Seebeck coefficient for thermoelectric effects',
        'unit': 'V/K',
        'default': 1e-5,
        'range': [1e-7, 1e-3],
        'category': 'thermoelectric_parameters',
        'coupling_type': 'thermoelectric'
    },
    'thermal_conductivity': {
        'name': 'Thermal Conductivity',
        'description': 'Thermal conductivity',
        'unit': 'W/(m·K)',
        'default': 1.0,
        'range': [1e-3, 1e3],
        'category': 'thermal_parameters',
        'coupling_type': 'thermoelectric'
    },
    'electrical_conductivity': {
        'name': 'Electrical Conductivity',
        'description': 'Electrical conductivity',
        'unit': 'S/m',
        'default': 1e6,
        'range': [1e3, 1e9],
        'category': 'electrical_parameters',
        'coupling_type': 'thermoelectric'
    },
    
    # Electrochemical Parameters
    'faraday_constant': {
        'name': 'Faraday Constant',
        'description': 'Faraday constant for electrochemical reactions',
        'unit': 'C/mol',
        'default': 96485.0,
        'range': [90000.0, 100000.0],
        'category': 'electrochemical_parameters',
        'coupling_type': 'electrochemical'
    },
    'gas_constant': {
        'name': 'Gas Constant',
        'description': 'Universal gas constant',
        'unit': 'J/(mol·K)',
        'default': 8.314,
        'range': [8.0, 9.0],
        'category': 'electrochemical_parameters',
        'coupling_type': 'electrochemical'
    },
    
    # Thermochemical Parameters
    'heat_of_reaction': {
        'name': 'Heat of Reaction',
        'description': 'Heat released/absorbed in chemical reactions',
        'unit': 'J/mol',
        'default': 1e5,
        'range': [1e3, 1e6],
        'category': 'thermochemical_parameters',
        'coupling_type': 'thermochemical'
    },
    
    # Mechanical-Electrical Parameters
    'piezoelectric_coefficient': {
        'name': 'Piezoelectric Coefficient',
        'description': 'Piezoelectric coupling coefficient',
        'unit': 'C/N',
        'default': 1e-9,
        'range': [1e-12, 1e-6],
        'category': 'piezoelectric_parameters',
        'coupling_type': 'mechanical_electrical'
    },
    
    # Optical-Mechanical Parameters
    'optical_index': {
        'name': 'Optical Index',
        'description': 'Refractive index for optical effects',
        'unit': 'dimensionless',
        'default': 1.5,
        'range': [1.0, 3.0],
        'category': 'optical_parameters',
        'coupling_type': 'optical_mechanical'
    },
    'photoelastic_coefficient': {
        'name': 'Photoelastic Coefficient',
        'description': 'Photoelastic coefficient for stress-optical coupling',
        'unit': '1/Pa',
        'default': 1e-12,
        'range': [1e-15, 1e-9],
        'category': 'optical_parameters',
        'coupling_type': 'optical_mechanical'
    },
    
    # Magnetic-Mechanical Parameters
    'magnetic_permeability': {
        'name': 'Magnetic Permeability',
        'description': 'Magnetic permeability',
        'unit': 'H/m',
        'default': 1e-6,
        'range': [1e-9, 1e-3],
        'category': 'magnetic_parameters',
        'coupling_type': 'magnetic_mechanical'
    },
    'magnetostrictive_coefficient': {
        'name': 'Magnetostrictive Coefficient',
        'description': 'Magnetostrictive coupling coefficient',
        'unit': '1/T',
        'default': 1e-5,
        'range': [1e-7, 1e-3],
        'category': 'magnetic_parameters',
        'coupling_type': 'magnetic_mechanical'
    },
    
    # Acoustic-Elastic Parameters
    'acoustic_speed': {
        'name': 'Acoustic Speed',
        'description': 'Speed of sound in the medium',
        'unit': 'm/s',
        'default': 340.0,
        'range': [100.0, 1000.0],
        'category': 'acoustic_parameters',
        'coupling_type': 'acoustic_elastic'
    },
    'acoustic_impedance': {
        'name': 'Acoustic Impedance',
        'description': 'Acoustic impedance of the medium',
        'unit': 'Pa·s/m',
        'default': 400.0,
        'range': [100.0, 1000.0],
        'category': 'acoustic_parameters',
        'coupling_type': 'acoustic_elastic'
    },
    
    # Thermal-Optical Parameters
    'thermo_optic_coefficient': {
        'name': 'Thermo-Optic Coefficient',
        'description': 'Thermo-optic coefficient for thermal-optical coupling',
        'unit': '1/K',
        'default': 1e-5,
        'range': [1e-7, 1e-3],
        'category': 'thermo_optic_parameters',
        'coupling_type': 'thermal_optical'
    },
    
    # Chemical-Mechanical Parameters
    'stress_corrosion_coefficient': {
        'name': 'Stress Corrosion Coefficient',
        'description': 'Stress corrosion coupling coefficient',
        'unit': '1/(Pa·s)',
        'default': 1e-12,
        'range': [1e-15, 1e-9],
        'category': 'chemical_mechanical_parameters',
        'coupling_type': 'chemical_mechanical'
    },
    
    # Biological-Mechanical Parameters
    'biological_rate': {
        'name': 'Biological Rate',
        'description': 'Biological process rate',
        'unit': '1/s',
        'default': 1e-3,
        'range': [1e-6, 1e-1],
        'category': 'biological_parameters',
        'coupling_type': 'biological_mechanical'
    },
    'cell_modulus': {
        'name': 'Cell Modulus',
        'description': 'Elastic modulus of biological cells',
        'unit': 'Pa',
        'default': 1e6,
        'range': [1e3, 1e9],
        'category': 'biological_parameters',
        'coupling_type': 'biological_mechanical'
    },
    
    # Solidification-Mechanics Parameters
    'latent_heat': {
        'name': 'Latent Heat',
        'description': 'Latent heat of phase transformation',
        'unit': 'J/kg',
        'default': 1e6,
        'range': [1e3, 1e9],
        'category': 'solidification_parameters',
        'coupling_type': 'solidification_mechanics'
    },
    'solidification_rate': {
        'name': 'Solidification Rate',
        'description': 'Rate of solidification process',
        'unit': 'm/s',
        'default': 1e-3,
        'range': [1e-6, 1e-1],
        'category': 'solidification_parameters',
        'coupling_type': 'solidification_mechanics'
    },
    
    # Sintering-Mechanics Parameters
    'sintering_rate': {
        'name': 'Sintering Rate',
        'description': 'Rate of sintering process',
        'unit': '1/s',
        'default': 1e-3,
        'range': [1e-6, 1e-1],
        'category': 'sintering_parameters',
        'coupling_type': 'sintering_mechanics'
    },
    'sintering_temperature': {
        'name': 'Sintering Temperature',
        'description': 'Temperature for sintering process',
        'unit': 'K',
        'default': 1000.0,
        'range': [300.0, 2000.0],
        'category': 'sintering_parameters',
        'coupling_type': 'sintering_mechanics'
    },
    
    # Crystal Plasticity-Heat Parameters
    'critical_resolved_shear_stress': {
        'name': 'Critical Resolved Shear Stress',
        'description': 'Critical resolved shear stress for crystal plasticity',
        'unit': 'Pa',
        'default': 1e6,
        'range': [1e3, 1e9],
        'category': 'crystal_plasticity_parameters',
        'coupling_type': 'crystal_plasticity_heat'
    },
    'dislocation_density': {
        'name': 'Dislocation Density',
        'description': 'Dislocation density in crystalline materials',
        'unit': '1/m²',
        'default': 1e12,
        'range': [1e9, 1e15],
        'category': 'crystal_plasticity_parameters',
        'coupling_type': 'crystal_plasticity_heat'
    },
    
    # Precipitation-Mechanics Parameters
    'nucleation_rate': {
        'name': 'Nucleation Rate',
        'description': 'Rate of precipitate nucleation',
        'unit': '1/(m³·s)',
        'default': 1e3,
        'range': [1e0, 1e6],
        'category': 'precipitation_parameters',
        'coupling_type': 'precipitation_mechanics'
    },
    'growth_rate': {
        'name': 'Growth Rate',
        'description': 'Rate of precipitate growth',
        'unit': 'm/s',
        'default': 1e-9,
        'range': [1e-12, 1e-6],
        'category': 'precipitation_parameters',
        'coupling_type': 'precipitation_mechanics'
    },
    
    # Grain Growth-Mechanics Parameters
    'grain_boundary_energy': {
        'name': 'Grain Boundary Energy',
        'description': 'Energy of grain boundaries',
        'unit': 'J/m²',
        'default': 1.0,
        'range': [1e-3, 1e3],
        'category': 'grain_growth_parameters',
        'coupling_type': 'grain_growth_mechanics'
    },
    'grain_growth_rate': {
        'name': 'Grain Growth Rate',
        'description': 'Rate of grain growth',
        'unit': 'm²/s',
        'default': 1e-12,
        'range': [1e-15, 1e-9],
        'category': 'grain_growth_parameters',
        'coupling_type': 'grain_growth_mechanics'
    },
    
    # Material Processing-Thermomechanics Parameters
    'phase_transformation_rate': {
        'name': 'Phase Transformation Rate',
        'description': 'Rate of phase transformations',
        'unit': '1/s',
        'default': 1e-3,
        'range': [1e-6, 1e-1],
        'category': 'material_processing_parameters',
        'coupling_type': 'material_processing_thermomechanics'
    },
    
    # Microstructure-Mechanics Parameters
    'interface_energy': {
        'name': 'Interface Energy',
        'description': 'Energy of phase interfaces',
        'unit': 'J/m²',
        'default': 1.0,
        'range': [1e-3, 1e3],
        'category': 'microstructure_parameters',
        'coupling_type': 'microstructure_mechanics'
    },
    'mobility': {
        'name': 'Mobility',
        'description': 'Interface mobility for phase field evolution',
        'unit': 'm²/(J·s)',
        'default': 1.0,
        'range': [1e-3, 1e3],
        'category': 'microstructure_parameters',
        'coupling_type': 'microstructure_mechanics'
    },
    
    # Powder Processing-Thermomechanics Parameters
    'powder_flow_rate': {
        'name': 'Powder Flow Rate',
        'description': 'Rate of powder flow',
        'unit': 'kg/(m²·s)',
        'default': 1e-3,
        'range': [1e-6, 1e-1],
        'category': 'powder_processing_parameters',
        'coupling_type': 'powder_processing_thermomechanics'
    },
    'powder_density': {
        'name': 'Powder Density',
        'description': 'Density of powder material',
        'unit': 'kg/m³',
        'default': 1000.0,
        'range': [100.0, 10000.0],
        'category': 'powder_processing_parameters',
        'coupling_type': 'powder_processing_thermomechanics'
    }
}

# Equation-specific parameters for multiphysics simulations
MULTIPHYSICS_EQUATION_PARAMETERS = {
    'multiphysics_thermoelasticity': {
        'thermal_expansion_coefficient': {**MULTIPHYSICS_PARAMETERS_DICT['thermal_expansion_coefficient'], 'default': 1e-5, 'range': [1e-7, 1e-3]},
        'thermal_stress_coefficient': {**MULTIPHYSICS_PARAMETERS_DICT['thermal_stress_coefficient'], 'default': 1e6, 'range': [1e3, 1e9]},
        'coupling_strength': {**MULTIPHYSICS_PARAMETERS_DICT['coupling_strength'], 'default': 1.0, 'range': [0.0, 10.0]}
    },
    'multiphysics_electromagnetic_thermal': {
        'joule_heating_coefficient': {**MULTIPHYSICS_PARAMETERS_DICT['joule_heating_coefficient'], 'default': 1e-3, 'range': [1e-6, 1e-1]},
        'electromagnetic_loss': {**MULTIPHYSICS_PARAMETERS_DICT['electromagnetic_loss'], 'default': 1e-3, 'range': [1e-6, 1e-1]},
        'coupling_strength': {**MULTIPHYSICS_PARAMETERS_DICT['coupling_strength'], 'default': 1.0, 'range': [0.0, 10.0]}
    },
    'multiphysics_fluid_structure_interaction': {
        'added_mass_coefficient': {**MULTIPHYSICS_PARAMETERS_DICT['added_mass_coefficient'], 'default': 1000.0, 'range': [100.0, 10000.0]},
        'hydrodynamic_damping': {**MULTIPHYSICS_PARAMETERS_DICT['hydrodynamic_damping'], 'default': 1.0, 'range': [0.1, 10.0]},
        'interface_stiffness': {**MULTIPHYSICS_PARAMETERS_DICT['interface_stiffness'], 'default': 1e6, 'range': [1e3, 1e9]}
    },
    'multiphysics_biomechanical_transport': {
        'coupling_strength': {**MULTIPHYSICS_PARAMETERS_DICT['coupling_strength'], 'default': 1.0, 'range': [0.0, 10.0]}
    },
    'multiphysics_geophysical_flow': {
        'coriolis_parameter': {**MULTIPHYSICS_PARAMETERS_DICT['coriolis_parameter'], 'default': 1e-4, 'range': [1e-5, 1e-3]},
        'friction_coefficient': {**MULTIPHYSICS_PARAMETERS_DICT['friction_coefficient'], 'default': 0.01, 'range': [1e-4, 1e-1]},
        'gravity': {**MULTIPHYSICS_PARAMETERS_DICT['gravity'], 'default': 9.81, 'range': [1.0, 20.0]},
        'coupling_strength': {**MULTIPHYSICS_PARAMETERS_DICT['coupling_strength'], 'default': 1.0, 'range': [0.0, 10.0]}
    },
    'multiphysics_atmospheric_oceanic': {
        'coriolis_parameter': {**MULTIPHYSICS_PARAMETERS_DICT['coriolis_parameter'], 'default': 1e-4, 'range': [1e-5, 1e-3]},
        'friction_coefficient': {**MULTIPHYSICS_PARAMETERS_DICT['friction_coefficient'], 'default': 0.01, 'range': [1e-4, 1e-1]},
        'coupling_strength': {**MULTIPHYSICS_PARAMETERS_DICT['coupling_strength'], 'default': 1.0, 'range': [0.0, 10.0]}
    },
    'multiphysics_nuclear_thermal': {
        'thermal_conductivity': {**MULTIPHYSICS_PARAMETERS_DICT['thermal_conductivity'], 'default': 1.0, 'range': [1e-3, 1e3]},
        'coupling_strength': {**MULTIPHYSICS_PARAMETERS_DICT['coupling_strength'], 'default': 1.0, 'range': [0.0, 10.0]}
    },
    'multiphysics_magnetohydrodynamics': {
        'magnetic_reynolds_number': {**MULTIPHYSICS_PARAMETERS_DICT['magnetic_reynolds_number'], 'default': 1.0, 'range': [0.1, 100.0]},
        'alfven_speed': {**MULTIPHYSICS_PARAMETERS_DICT['alfven_speed'], 'default': 1000.0, 'range': [10.0, 10000.0]},
        'magnetic_prandtl_number': {**MULTIPHYSICS_PARAMETERS_DICT['magnetic_prandtl_number'], 'default': 1.0, 'range': [0.1, 10.0]}
    },
    'multiphysics_poroelasticity': {
        'biot_coefficient': {**MULTIPHYSICS_PARAMETERS_DICT['biot_coefficient'], 'default': 0.8, 'range': [0.0, 1.0]},
        'skempton_coefficient': {**MULTIPHYSICS_PARAMETERS_DICT['skempton_coefficient'], 'default': 0.5, 'range': [0.0, 1.0]},
        'storage_coefficient': {**MULTIPHYSICS_PARAMETERS_DICT['storage_coefficient'], 'default': 1e-9, 'range': [1e-12, 1e-6]}
    },
    'multiphysics_viscoelasticity': {
        'relaxation_time': {**MULTIPHYSICS_PARAMETERS_DICT['relaxation_time'], 'default': 1.0, 'range': [1e-3, 1e3]},
        'retardation_time': {**MULTIPHYSICS_PARAMETERS_DICT['retardation_time'], 'default': 0.1, 'range': [1e-4, 1e2]},
        'viscoelastic_modulus': {**MULTIPHYSICS_PARAMETERS_DICT['viscoelastic_modulus'], 'default': 1e9, 'range': [1e6, 1e12]}
    },
    'multiphysics_radiative_transfer': {
        'absorption_coefficient': {**MULTIPHYSICS_PARAMETERS_DICT['absorption_coefficient'], 'default': 1.0, 'range': [1e-3, 1e3]},
        'scattering_coefficient': {**MULTIPHYSICS_PARAMETERS_DICT['scattering_coefficient'], 'default': 0.1, 'range': [1e-4, 1e2]},
        'emissivity': {**MULTIPHYSICS_PARAMETERS_DICT['emissivity'], 'default': 0.8, 'range': [0.0, 1.0]},
        'coupling_strength': {**MULTIPHYSICS_PARAMETERS_DICT['coupling_strength'], 'default': 1.0, 'range': [0.0, 10.0]}
    },
    'multiphysics_phase_field': {
        'phase_field_elastic_coupling': {**MULTIPHYSICS_PARAMETERS_DICT['phase_field_elastic_coupling'], 'default': 1e6, 'range': [1e3, 1e9]},
        'coupling_strength': {**MULTIPHYSICS_PARAMETERS_DICT['coupling_strength'], 'default': 1.0, 'range': [0.0, 10.0]}
    },
    'multiphysics_reaction_diffusion': {
        'diffusion_coefficient': {**MULTIPHYSICS_PARAMETERS_DICT['diffusion_coefficient'], 'default': 1e-9, 'range': [1e-12, 1e-6]},
        'reaction_rate': {**MULTIPHYSICS_PARAMETERS_DICT['reaction_rate'], 'default': 1e-3, 'range': [1e-6, 1e-1]},
        'activation_energy': {**MULTIPHYSICS_PARAMETERS_DICT['activation_energy'], 'default': 1e5, 'range': [1e3, 1e6]},
        'coupling_strength': {**MULTIPHYSICS_PARAMETERS_DICT['coupling_strength'], 'default': 1.0, 'range': [0.0, 10.0]}
    },
    'multiphysics_advection_diffusion': {
        'velocity': {**MULTIPHYSICS_PARAMETERS_DICT['velocity'], 'default': 1.0, 'range': [1e-3, 1e3]},
        'diffusion_coefficient': {**MULTIPHYSICS_PARAMETERS_DICT['diffusion_coefficient'], 'default': 1e-9, 'range': [1e-12, 1e-6]},
        'peclet_number': {**MULTIPHYSICS_PARAMETERS_DICT['peclet_number'], 'default': 1.0, 'range': [0.1, 100.0]},
        'coupling_strength': {**MULTIPHYSICS_PARAMETERS_DICT['coupling_strength'], 'default': 1.0, 'range': [0.0, 10.0]}
    },
    'multiphysics_elastic_wave': {
        'elastic_modulus': {**MULTIPHYSICS_PARAMETERS_DICT['elastic_modulus'], 'default': 1e9, 'range': [1e6, 1e12]},
        'density': {**MULTIPHYSICS_PARAMETERS_DICT['density'], 'default': 1000.0, 'range': [100.0, 10000.0]},
        'poisson_ratio': {**MULTIPHYSICS_PARAMETERS_DICT['poisson_ratio'], 'default': 0.3, 'range': [0.0, 0.5]},
        'coupling_strength': {**MULTIPHYSICS_PARAMETERS_DICT['coupling_strength'], 'default': 1.0, 'range': [0.0, 10.0]}
    },
    'multiphysics_quantum_mechanical': {
        'potential_energy': {**MULTIPHYSICS_PARAMETERS_DICT['potential_energy'], 'default': 1.0, 'range': [1e-3, 1e3]},
        'wave_function': {**MULTIPHYSICS_PARAMETERS_DICT['wave_function'], 'default': 1.0, 'range': [1e-3, 1e3]},
        'planck_constant': {**MULTIPHYSICS_PARAMETERS_DICT['planck_constant'], 'default': 1.055e-34, 'range': [1e-35, 1e-33]},
        'coupling_strength': {**MULTIPHYSICS_PARAMETERS_DICT['coupling_strength'], 'default': 1.0, 'range': [0.0, 10.0]}
    },
    'multiphysics_thermoelectric': {
        'seebeck_coefficient': {**MULTIPHYSICS_PARAMETERS_DICT['seebeck_coefficient'], 'default': 1e-5, 'range': [1e-7, 1e-3]},
        'thermal_conductivity': {**MULTIPHYSICS_PARAMETERS_DICT['thermal_conductivity'], 'default': 1.0, 'range': [1e-3, 1e3]},
        'electrical_conductivity': {**MULTIPHYSICS_PARAMETERS_DICT['electrical_conductivity'], 'default': 1e6, 'range': [1e3, 1e9]},
        'coupling_strength': {**MULTIPHYSICS_PARAMETERS_DICT['coupling_strength'], 'default': 1.0, 'range': [0.0, 10.0]}
    },
    'multiphysics_electrochemical': {
        'electrical_conductivity': {**MULTIPHYSICS_PARAMETERS_DICT['electrical_conductivity'], 'default': 1e6, 'range': [1e3, 1e9]},
        'reaction_rate': {**MULTIPHYSICS_PARAMETERS_DICT['reaction_rate'], 'default': 1e-3, 'range': [1e-6, 1e-1]},
        'faraday_constant': {**MULTIPHYSICS_PARAMETERS_DICT['faraday_constant'], 'default': 96485.0, 'range': [90000.0, 100000.0]},
        'gas_constant': {**MULTIPHYSICS_PARAMETERS_DICT['gas_constant'], 'default': 8.314, 'range': [8.0, 9.0]},
        'coupling_strength': {**MULTIPHYSICS_PARAMETERS_DICT['coupling_strength'], 'default': 1.0, 'range': [0.0, 10.0]}
    },
    'multiphysics_thermochemical': {
        'thermal_conductivity': {**MULTIPHYSICS_PARAMETERS_DICT['thermal_conductivity'], 'default': 1.0, 'range': [1e-3, 1e3]},
        'reaction_rate': {**MULTIPHYSICS_PARAMETERS_DICT['reaction_rate'], 'default': 1e-3, 'range': [1e-6, 1e-1]},
        'heat_of_reaction': {**MULTIPHYSICS_PARAMETERS_DICT['heat_of_reaction'], 'default': 1e5, 'range': [1e3, 1e6]},
        'coupling_strength': {**MULTIPHYSICS_PARAMETERS_DICT['coupling_strength'], 'default': 1.0, 'range': [0.0, 10.0]}
    },
    'multiphysics_mechanical_electrical': {
        'elastic_modulus': {**MULTIPHYSICS_PARAMETERS_DICT['elastic_modulus'], 'default': 1e9, 'range': [1e6, 1e12]},
        'electrical_conductivity': {**MULTIPHYSICS_PARAMETERS_DICT['electrical_conductivity'], 'default': 1e6, 'range': [1e3, 1e9]},
        'piezoelectric_coefficient': {**MULTIPHYSICS_PARAMETERS_DICT['piezoelectric_coefficient'], 'default': 1e-9, 'range': [1e-12, 1e-6]},
        'coupling_strength': {**MULTIPHYSICS_PARAMETERS_DICT['coupling_strength'], 'default': 1.0, 'range': [0.0, 10.0]}
    },
    'multiphysics_optical_mechanical': {
        'optical_index': {**MULTIPHYSICS_PARAMETERS_DICT['optical_index'], 'default': 1.5, 'range': [1.0, 3.0]},
        'elastic_modulus': {**MULTIPHYSICS_PARAMETERS_DICT['elastic_modulus'], 'default': 1e9, 'range': [1e6, 1e12]},
        'photoelastic_coefficient': {**MULTIPHYSICS_PARAMETERS_DICT['photoelastic_coefficient'], 'default': 1e-12, 'range': [1e-15, 1e-9]},
        'coupling_strength': {**MULTIPHYSICS_PARAMETERS_DICT['coupling_strength'], 'default': 1.0, 'range': [0.0, 10.0]}
    },
    'multiphysics_magnetic_mechanical': {
        'magnetic_permeability': {**MULTIPHYSICS_PARAMETERS_DICT['magnetic_permeability'], 'default': 1e-6, 'range': [1e-9, 1e-3]},
        'elastic_modulus': {**MULTIPHYSICS_PARAMETERS_DICT['elastic_modulus'], 'default': 1e9, 'range': [1e6, 1e12]},
        'magnetostrictive_coefficient': {**MULTIPHYSICS_PARAMETERS_DICT['magnetostrictive_coefficient'], 'default': 1e-5, 'range': [1e-7, 1e-3]},
        'coupling_strength': {**MULTIPHYSICS_PARAMETERS_DICT['coupling_strength'], 'default': 1.0, 'range': [0.0, 10.0]}
    },
    'multiphysics_acoustic_elastic': {
        'acoustic_speed': {**MULTIPHYSICS_PARAMETERS_DICT['acoustic_speed'], 'default': 340.0, 'range': [100.0, 1000.0]},
        'elastic_modulus': {**MULTIPHYSICS_PARAMETERS_DICT['elastic_modulus'], 'default': 1e9, 'range': [1e6, 1e12]},
        'acoustic_impedance': {**MULTIPHYSICS_PARAMETERS_DICT['acoustic_impedance'], 'default': 400.0, 'range': [100.0, 1000.0]},
        'coupling_strength': {**MULTIPHYSICS_PARAMETERS_DICT['coupling_strength'], 'default': 1.0, 'range': [0.0, 10.0]}
    },
    'multiphysics_thermal_optical': {
        'thermal_conductivity': {**MULTIPHYSICS_PARAMETERS_DICT['thermal_conductivity'], 'default': 1.0, 'range': [1e-3, 1e3]},
        'optical_index': {**MULTIPHYSICS_PARAMETERS_DICT['optical_index'], 'default': 1.5, 'range': [1.0, 3.0]},
        'thermo_optic_coefficient': {**MULTIPHYSICS_PARAMETERS_DICT['thermo_optic_coefficient'], 'default': 1e-5, 'range': [1e-7, 1e-3]},
        'coupling_strength': {**MULTIPHYSICS_PARAMETERS_DICT['coupling_strength'], 'default': 1.0, 'range': [0.0, 10.0]}
    },
    'multiphysics_chemical_mechanical': {
        'reaction_rate': {**MULTIPHYSICS_PARAMETERS_DICT['reaction_rate'], 'default': 1e-3, 'range': [1e-6, 1e-1]},
        'elastic_modulus': {**MULTIPHYSICS_PARAMETERS_DICT['elastic_modulus'], 'default': 1e9, 'range': [1e6, 1e12]},
        'stress_corrosion_coefficient': {**MULTIPHYSICS_PARAMETERS_DICT['stress_corrosion_coefficient'], 'default': 1e-12, 'range': [1e-15, 1e-9]},
        'coupling_strength': {**MULTIPHYSICS_PARAMETERS_DICT['coupling_strength'], 'default': 1.0, 'range': [0.0, 10.0]}
    },
    'multiphysics_biological_mechanical': {
        'biological_rate': {**MULTIPHYSICS_PARAMETERS_DICT['biological_rate'], 'default': 1e-3, 'range': [1e-6, 1e-1]},
        'elastic_modulus': {**MULTIPHYSICS_PARAMETERS_DICT['elastic_modulus'], 'default': 1e6, 'range': [1e3, 1e9]},
        'cell_modulus': {**MULTIPHYSICS_PARAMETERS_DICT['cell_modulus'], 'default': 1e6, 'range': [1e3, 1e9]},
        'coupling_strength': {**MULTIPHYSICS_PARAMETERS_DICT['coupling_strength'], 'default': 1.0, 'range': [0.0, 10.0]}
    },
    'solidification_mechanics': {
        'latent_heat': {**MULTIPHYSICS_PARAMETERS_DICT['latent_heat'], 'default': 1e6, 'range': [1e3, 1e9]},
        'solidification_rate': {**MULTIPHYSICS_PARAMETERS_DICT['solidification_rate'], 'default': 1e-3, 'range': [1e-6, 1e-1]},
        'elastic_modulus': {**MULTIPHYSICS_PARAMETERS_DICT['elastic_modulus'], 'default': 1e9, 'range': [1e6, 1e12]},
        'coupling_strength': {**MULTIPHYSICS_PARAMETERS_DICT['coupling_strength'], 'default': 1.0, 'range': [0.0, 10.0]}
    },
    'sintering_mechanics': {
        'sintering_rate': {**MULTIPHYSICS_PARAMETERS_DICT['sintering_rate'], 'default': 1e-3, 'range': [1e-6, 1e-1]},
        'sintering_temperature': {**MULTIPHYSICS_PARAMETERS_DICT['sintering_temperature'], 'default': 1000.0, 'range': [300.0, 2000.0]},
        'elastic_modulus': {**MULTIPHYSICS_PARAMETERS_DICT['elastic_modulus'], 'default': 1e9, 'range': [1e6, 1e12]},
        'coupling_strength': {**MULTIPHYSICS_PARAMETERS_DICT['coupling_strength'], 'default': 1.0, 'range': [0.0, 10.0]}
    },
    'crystal_plasticity_heat': {
        'critical_resolved_shear_stress': {**MULTIPHYSICS_PARAMETERS_DICT['critical_resolved_shear_stress'], 'default': 1e6, 'range': [1e3, 1e9]},
        'dislocation_density': {**MULTIPHYSICS_PARAMETERS_DICT['dislocation_density'], 'default': 1e12, 'range': [1e9, 1e15]},
        'thermal_conductivity': {**MULTIPHYSICS_PARAMETERS_DICT['thermal_conductivity'], 'default': 1.0, 'range': [1e-3, 1e3]},
        'coupling_strength': {**MULTIPHYSICS_PARAMETERS_DICT['coupling_strength'], 'default': 1.0, 'range': [0.0, 10.0]}
    },
    'diffusion_mechanics': {
        'diffusion_coefficient': {**MULTIPHYSICS_PARAMETERS_DICT['diffusion_coefficient'], 'default': 1e-9, 'range': [1e-12, 1e-6]},
        'elastic_modulus': {**MULTIPHYSICS_PARAMETERS_DICT['elastic_modulus'], 'default': 1e9, 'range': [1e6, 1e12]},
        'coupling_strength': {**MULTIPHYSICS_PARAMETERS_DICT['coupling_strength'], 'default': 1.0, 'range': [0.0, 10.0]}
    },
    'precipitation_mechanics': {
        'nucleation_rate': {**MULTIPHYSICS_PARAMETERS_DICT['nucleation_rate'], 'default': 1e3, 'range': [1e0, 1e6]},
        'growth_rate': {**MULTIPHYSICS_PARAMETERS_DICT['growth_rate'], 'default': 1e-9, 'range': [1e-12, 1e-6]},
        'elastic_modulus': {**MULTIPHYSICS_PARAMETERS_DICT['elastic_modulus'], 'default': 1e9, 'range': [1e6, 1e12]},
        'coupling_strength': {**MULTIPHYSICS_PARAMETERS_DICT['coupling_strength'], 'default': 1.0, 'range': [0.0, 10.0]}
    },
    'grain_growth_mechanics': {
        'grain_boundary_energy': {**MULTIPHYSICS_PARAMETERS_DICT['grain_boundary_energy'], 'default': 1.0, 'range': [1e-3, 1e3]},
        'grain_growth_rate': {**MULTIPHYSICS_PARAMETERS_DICT['grain_growth_rate'], 'default': 1e-12, 'range': [1e-15, 1e-9]},
        'elastic_modulus': {**MULTIPHYSICS_PARAMETERS_DICT['elastic_modulus'], 'default': 1e9, 'range': [1e6, 1e12]},
        'coupling_strength': {**MULTIPHYSICS_PARAMETERS_DICT['coupling_strength'], 'default': 1.0, 'range': [0.0, 10.0]}
    },
    'material_processing_thermomechanics': {
        'thermal_conductivity': {**MULTIPHYSICS_PARAMETERS_DICT['thermal_conductivity'], 'default': 1.0, 'range': [1e-3, 1e3]},
        'elastic_modulus': {**MULTIPHYSICS_PARAMETERS_DICT['elastic_modulus'], 'default': 1e9, 'range': [1e6, 1e12]},
        'phase_transformation_rate': {**MULTIPHYSICS_PARAMETERS_DICT['phase_transformation_rate'], 'default': 1e-3, 'range': [1e-6, 1e-1]},
        'coupling_strength': {**MULTIPHYSICS_PARAMETERS_DICT['coupling_strength'], 'default': 1.0, 'range': [0.0, 10.0]}
    },
    'microstructure_mechanics': {
        'phase_field_elastic_coupling': {**MULTIPHYSICS_PARAMETERS_DICT['phase_field_elastic_coupling'], 'default': 1e6, 'range': [1e3, 1e9]},
        'interface_energy': {**MULTIPHYSICS_PARAMETERS_DICT['interface_energy'], 'default': 1.0, 'range': [1e-3, 1e3]},
        'mobility': {**MULTIPHYSICS_PARAMETERS_DICT['mobility'], 'default': 1.0, 'range': [1e-3, 1e3]},
        'coupling_strength': {**MULTIPHYSICS_PARAMETERS_DICT['coupling_strength'], 'default': 1.0, 'range': [0.0, 10.0]}
    },
    'powder_processing_thermomechanics': {
        'powder_flow_rate': {**MULTIPHYSICS_PARAMETERS_DICT['powder_flow_rate'], 'default': 1e-3, 'range': [1e-6, 1e-1]},
        'powder_density': {**MULTIPHYSICS_PARAMETERS_DICT['powder_density'], 'default': 1000.0, 'range': [100.0, 10000.0]},
        'thermal_conductivity': {**MULTIPHYSICS_PARAMETERS_DICT['thermal_conductivity'], 'default': 1.0, 'range': [1e-3, 1e3]},
        'elastic_modulus': {**MULTIPHYSICS_PARAMETERS_DICT['elastic_modulus'], 'default': 1e9, 'range': [1e6, 1e12]},
        'coupling_strength': {**MULTIPHYSICS_PARAMETERS_DICT['coupling_strength'], 'default': 1.0, 'range': [0.0, 10.0]}
    },
    'phase_field_mechanics': {
        'phase_field_elastic_coupling': {**MULTIPHYSICS_PARAMETERS_DICT['phase_field_elastic_coupling'], 'default': 1e6, 'range': [1e3, 1e9]},
        'coupling_strength': {**MULTIPHYSICS_PARAMETERS_DICT['coupling_strength'], 'default': 1.0, 'range': [0.0, 10.0]}
    },
    'phase_field_heat': {
        'phase_field_thermal_coupling': {**MULTIPHYSICS_PARAMETERS_DICT['phase_field_thermal_coupling'], 'default': 1e3, 'range': [1e0, 1e6]},
        'coupling_strength': {**MULTIPHYSICS_PARAMETERS_DICT['coupling_strength'], 'default': 1.0, 'range': [0.0, 10.0]}
    },
    'laser_material_interaction': {
        'laser_material_coupling': {**MULTIPHYSICS_PARAMETERS_DICT['laser_material_coupling'], 'default': 1e-3, 'range': [1e-6, 1e-1]},
        'coupling_strength': {**MULTIPHYSICS_PARAMETERS_DICT['coupling_strength'], 'default': 1.0, 'range': [0.0, 10.0]}
    },
    'melt_pool_thermomechanics': {
        'melt_pool_thermomechanics': {**MULTIPHYSICS_PARAMETERS_DICT['melt_pool_thermomechanics'], 'default': 1e6, 'range': [1e3, 1e9]},
        'coupling_strength': {**MULTIPHYSICS_PARAMETERS_DICT['coupling_strength'], 'default': 1.0, 'range': [0.0, 10.0]}
    },
    'additive_manufacturing_process': {
        'laser_material_coupling': {**MULTIPHYSICS_PARAMETERS_DICT['laser_material_coupling'], 'default': 1e-3, 'range': [1e-6, 1e-1]},
        'melt_pool_thermomechanics': {**MULTIPHYSICS_PARAMETERS_DICT['melt_pool_thermomechanics'], 'default': 1e6, 'range': [1e3, 1e9]},
        'powder_fluid_coupling': {**MULTIPHYSICS_PARAMETERS_DICT['powder_fluid_coupling'], 'default': 1e-3, 'range': [1e-6, 1e-1]}
    }
} 