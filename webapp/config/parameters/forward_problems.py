"""
Forward Problems Parameters
Parameters for solving forward problems with known parameters and initial/boundary conditions.
"""

FORWARD_PROBLEMS_PARAMETERS_DICT = {
    # Physical Parameters
    'viscosity': {
        'name': 'Viscosity',
        'description': 'Dynamic viscosity of the fluid',
        'unit': 'Pa·s',
        'default': 0.001,
        'range': [1e-6, 1e-2],
        'category': 'fluid_properties'
    },
    'thermal_diffusivity': {
        'name': 'Thermal Diffusivity',
        'description': 'Thermal diffusivity coefficient',
        'unit': 'm²/s',
        'default': 1e-5,
        'range': [1e-8, 1e-3],
        'category': 'thermal_properties'
    },
    'wave_speed': {
        'name': 'Wave Speed',
        'description': 'Speed of wave propagation',
        'unit': 'm/s',
        'default': 340.0,
        'range': [1.0, 10000.0],
        'category': 'wave_properties'
    },
    'natural_frequency': {
        'name': 'Natural Frequency',
        'description': 'Natural frequency of oscillation',
        'unit': 'rad/s',
        'default': 1.0,
        'range': [0.1, 100.0],
        'category': 'mechanical_properties'
    },
    'wavenumber': {
        'name': 'Wavenumber',
        'description': 'Wavenumber for wave equations',
        'unit': '1/m',
        'default': 1.0,
        'range': [0.01, 100.0],
        'category': 'wave_properties'
    },
    'density': {
        'name': 'Density',
        'description': 'Material density',
        'unit': 'kg/m³',
        'default': 1000.0,
        'range': [1.0, 20000.0],
        'category': 'material_properties'
    },
    'thermal_conductivity': {
        'name': 'Thermal Conductivity',
        'description': 'Thermal conductivity coefficient',
        'unit': 'W/(m·K)',
        'default': 50.0,
        'range': [0.01, 1000.0],
        'category': 'thermal_properties'
    },
    'specific_heat': {
        'name': 'Specific Heat',
        'description': 'Specific heat capacity',
        'unit': 'J/(kg·K)',
        'default': 1000.0,
        'range': [100.0, 10000.0],
        'category': 'thermal_properties'
    },
    'elastic_modulus': {
        'name': 'Elastic Modulus',
        'description': 'Young\'s modulus of elasticity',
        'unit': 'GPa',
        'default': 200.0,
        'range': [0.1, 1000.0],
        'category': 'mechanical_properties'
    },
    'poisson_ratio': {
        'name': 'Poisson Ratio',
        'description': 'Poisson\'s ratio',
        'unit': 'dimensionless',
        'default': 0.3,
        'range': [0.0, 0.5],
        'category': 'mechanical_properties'
    },
    
    # Phase Field Parameters
    'mobility': {
        'name': 'Mobility',
        'description': 'Phase field mobility coefficient',
        'unit': 'm²/(J·s)',
        'default': 1e-3,
        'range': [1e-6, 1e-1],
        'category': 'phase_field'
    },
    'interface_thickness': {
        'name': 'Interface Thickness',
        'description': 'Phase field interface thickness parameter',
        'unit': 'm',
        'default': 1e-6,
        'range': [1e-9, 1e-3],
        'category': 'phase_field'
    },
    'free_energy_barrier': {
        'name': 'Free Energy Barrier',
        'description': 'Free energy barrier for phase transitions',
        'unit': 'J/m³',
        'default': 1e6,
        'range': [1e3, 1e9],
        'category': 'phase_field'
    },
    
    # Chemical Parameters
    'diffusion_coefficient': {
        'name': 'Diffusion Coefficient',
        'description': 'Diffusion coefficient for transport',
        'unit': 'm²/s',
        'default': 1e-9,
        'range': [1e-12, 1e-6],
        'category': 'transport_properties'
    },
    'reaction_rate': {
        'name': 'Reaction Rate',
        'description': 'Chemical reaction rate constant',
        'unit': '1/s',
        'default': 1e-3,
        'range': [1e-6, 1e0],
        'category': 'chemical_properties'
    },
    
    # Poroelastic Parameters
    'permeability': {
        'name': 'Permeability',
        'description': 'Material permeability',
        'unit': 'm²',
        'default': 1e-12,
        'range': [1e-20, 1e-8],
        'category': 'poroelastic_properties'
    },
    'biot_coefficient': {
        'name': 'Biot Coefficient',
        'description': 'Biot coefficient for poroelasticity',
        'unit': 'dimensionless',
        'default': 0.8,
        'range': [0.0, 1.0],
        'category': 'poroelastic_properties'
    },
    
    # Viscoelastic Parameters
    'relaxation_time': {
        'name': 'Relaxation Time',
        'description': 'Viscoelastic relaxation time',
        'unit': 's',
        'default': 1.0,
        'range': [1e-3, 1e3],
        'category': 'viscoelastic_properties'
    },
    'retardation_time': {
        'name': 'Retardation Time',
        'description': 'Viscoelastic retardation time',
        'unit': 's',
        'default': 0.1,
        'range': [1e-4, 1e2],
        'category': 'viscoelastic_properties'
    },
    
    # Radiation Parameters
    'absorption_coefficient': {
        'name': 'Absorption Coefficient',
        'description': 'Radiation absorption coefficient',
        'unit': '1/m',
        'default': 1.0,
        'range': [1e-3, 1e3],
        'category': 'radiation_properties'
    },
    'scattering_coefficient': {
        'name': 'Scattering Coefficient',
        'description': 'Radiation scattering coefficient',
        'unit': '1/m',
        'default': 0.1,
        'range': [1e-4, 1e2],
        'category': 'radiation_properties'
    },
    
    # Shallow Water Parameters
    'gravity': {
        'name': 'Gravity',
        'description': 'Acceleration due to gravity',
        'unit': 'm/s²',
        'default': 9.81,
        'range': [1.0, 20.0],
        'category': 'geophysical_properties'
    },
    'coriolis_parameter': {
        'name': 'Coriolis Parameter',
        'description': 'Coriolis parameter for geophysical flows',
        'unit': '1/s',
        'default': 1e-4,
        'range': [1e-5, 1e-3],
        'category': 'geophysical_properties'
    },
    
    # Quantum Parameters
    'planck_constant': {
        'name': 'Planck Constant',
        'description': 'Reduced Planck constant',
        'unit': 'J·s',
        'default': 1.055e-34,
        'range': [1e-35, 1e-33],
        'category': 'quantum_properties'
    },
    'mass': {
        'name': 'Mass',
        'description': 'Particle mass',
        'unit': 'kg',
        'default': 9.109e-31,
        'range': [1e-32, 1e-29],
        'category': 'quantum_properties'
    },
    
    # Electromagnetic Parameters
    'permittivity': {
        'name': 'Permittivity',
        'description': 'Electric permittivity',
        'unit': 'F/m',
        'default': 8.854e-12,
        'range': [1e-13, 1e-10],
        'category': 'electromagnetic_properties'
    },
    'permeability': {
        'name': 'Permeability',
        'description': 'Magnetic permeability',
        'unit': 'H/m',
        'default': 1.257e-6,
        'range': [1e-7, 1e-5],
        'category': 'electromagnetic_properties'
    },
    
    # Additive Manufacturing Parameters
    'laser_power': {
        'name': 'Laser Power',
        'description': 'Laser power for AM processing',
        'unit': 'W',
        'default': 1000.0,
        'range': [1.0, 10000.0],
        'category': 'am_properties'
    },
    'laser_spot_size': {
        'name': 'Laser Spot Size',
        'description': 'Laser beam spot size',
        'unit': 'm',
        'default': 1e-3,
        'range': [1e-5, 1e-2],
        'category': 'am_properties'
    },
    'scan_speed': {
        'name': 'Scan Speed',
        'description': 'Laser scan speed',
        'unit': 'm/s',
        'default': 1.0,
        'range': [0.01, 10.0],
        'category': 'am_properties'
    },
    'powder_density': {
        'name': 'Powder Density',
        'description': 'Powder bed density',
        'unit': 'kg/m³',
        'default': 4000.0,
        'range': [1000.0, 10000.0],
        'category': 'am_properties'
    },
    
    # Material Science Parameters
    'grain_boundary_energy': {
        'name': 'Grain Boundary Energy',
        'description': 'Grain boundary energy',
        'unit': 'J/m²',
        'default': 1.0,
        'range': [0.1, 10.0],
        'category': 'material_properties'
    },
    'grain_boundary_mobility': {
        'name': 'Grain Boundary Mobility',
        'description': 'Grain boundary mobility',
        'unit': 'm²/(J·s)',
        'default': 1e-6,
        'range': [1e-9, 1e-3],
        'category': 'material_properties'
    },
    'nucleation_rate': {
        'name': 'Nucleation Rate',
        'description': 'Nucleation rate constant',
        'unit': '1/(m³·s)',
        'default': 1e12,
        'range': [1e8, 1e16],
        'category': 'material_properties'
    },
    'activation_energy': {
        'name': 'Activation Energy',
        'description': 'Activation energy for processes',
        'unit': 'J/mol',
        'default': 50000.0,
        'range': [1000.0, 500000.0],
        'category': 'material_properties'
    },
    
    # Boundary Conditions
    'boundary_temperature': {
        'name': 'Boundary Temperature',
        'description': 'Temperature at boundaries',
        'unit': 'K',
        'default': 300.0,
        'range': [100.0, 2000.0],
        'category': 'boundary_conditions'
    },
    'boundary_pressure': {
        'name': 'Boundary Pressure',
        'description': 'Pressure at boundaries',
        'unit': 'Pa',
        'default': 101325.0,
        'range': [1e3, 1e8],
        'category': 'boundary_conditions'
    },
    'boundary_velocity': {
        'name': 'Boundary Velocity',
        'description': 'Velocity at boundaries',
        'unit': 'm/s',
        'default': 0.0,
        'range': [-100.0, 100.0],
        'category': 'boundary_conditions'
    },
    
    # Initial Conditions
    'initial_temperature': {
        'name': 'Initial Temperature',
        'description': 'Initial temperature field',
        'unit': 'K',
        'default': 300.0,
        'range': [100.0, 2000.0],
        'category': 'initial_conditions'
    },
    'initial_concentration': {
        'name': 'Initial Concentration',
        'description': 'Initial concentration field',
        'unit': 'mol/m³',
        'default': 1.0,
        'range': [0.0, 1000.0],
        'category': 'initial_conditions'
    },
    'initial_displacement': {
        'name': 'Initial Displacement',
        'description': 'Initial displacement field',
        'unit': 'm',
        'default': 0.0,
        'range': [-1.0, 1.0],
        'category': 'initial_conditions'
    }
} 