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
    'magnetic_permeability': {
        'name': 'Magnetic Permeability',
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
        'description': 'Laser beam diameter',
        'unit': 'μm',
        'default': 100.0,
        'range': [10.0, 1000.0],
        'category': 'am_properties'
    },
    'scan_speed': {
        'name': 'Scan Speed',
        'description': 'Laser scanning velocity',
        'unit': 'mm/s',
        'default': 1000.0,
        'range': [10.0, 10000.0],
        'category': 'am_properties'
    },
    'powder_density': {
        'name': 'Powder Density',
        'description': 'Powder bed density',
        'unit': 'kg/m³',
        'default': 4000.0,
        'range': [1000.0, 8000.0],
        'category': 'am_properties'
    },
    'melting_temperature': {
        'name': 'Melting Temperature',
        'description': 'Material melting point',
        'unit': 'K',
        'default': 1700.0,
        'range': [300.0, 4000.0],
        'category': 'am_properties'
    },
    'latent_heat': {
        'name': 'Latent Heat',
        'description': 'Latent heat of fusion',
        'unit': 'J/kg',
        'default': 2.5e5,
        'range': [1e4, 1e6],
        'category': 'am_properties'
    },
    'grain_size': {
        'name': 'Grain Size',
        'description': 'Initial grain size',
        'unit': 'μm',
        'default': 10.0,
        'range': [0.1, 100.0],
        'category': 'am_properties'
    },
    'nucleation_rate': {
        'name': 'Nucleation Rate',
        'description': 'Nucleation rate constant',
        'unit': '1/(m³·s)',
        'default': 1e12,
        'range': [1e8, 1e16],
        'category': 'am_properties'
    },
    'growth_rate': {
        'name': 'Growth Rate',
        'description': 'Grain growth rate constant',
        'unit': 'm²/s',
        'default': 1e-12,
        'range': [1e-16, 1e-8],
        'category': 'am_properties'
    },
    'sintering_temperature': {
        'name': 'Sintering Temperature',
        'description': 'Sintering temperature',
        'unit': 'K',
        'default': 1500.0,
        'range': [300.0, 3000.0],
        'category': 'am_properties'
    },
    'sintering_time': {
        'name': 'Sintering Time',
        'description': 'Sintering duration',
        'unit': 's',
        'default': 3600.0,
        'range': [1.0, 86400.0],
        'category': 'am_properties'
    },
    'porosity': {
        'name': 'Porosity',
        'description': 'Initial porosity fraction',
        'unit': 'dimensionless',
        'default': 0.4,
        'range': [0.0, 0.8],
        'category': 'am_properties'
    },
    'residual_stress': {
        'name': 'Residual Stress',
        'description': 'Initial residual stress',
        'unit': 'MPa',
        'default': 0.0,
        'range': [-500.0, 500.0],
        'category': 'am_properties'
    }
}

# Equation-specific parameter mappings
FORWARD_PROBLEMS_EQUATION_PARAMETERS = {
    'burgers': {
        'viscosity': {
            'name': 'Viscosity (ν)',
            'description': 'Dynamic viscosity coefficient in Burgers equation',
            'unit': 'Pa·s',
            'default': 0.01,
            'range': [1e-6, 1e-1],
            'category': 'fluid_properties',
            'equation': '∂u/∂t + u∂u/∂x = ν∂²u/∂x²'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties'
        }
    },
    
    'heat': {
        'thermal_diffusivity': {
            'name': 'Thermal Diffusivity (α)',
            'description': 'Thermal diffusivity coefficient in heat equation',
            'unit': 'm²/s',
            'default': 1e-5,
            'range': [1e-8, 1e-3],
            'category': 'thermal_properties',
            'equation': '∂u/∂t = α∂²u/∂x²'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties'
        }
    },
    
    'wave': {
        'wave_speed': {
            'name': 'Wave Speed (c)',
            'description': 'Wave propagation speed in wave equation',
            'unit': 'm/s',
            'default': 340.0,
            'range': [1.0, 10000.0],
            'category': 'wave_properties',
            'equation': '∂²u/∂t² = c²∂²u/∂x²'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration',
            'unit': 's',
            'default': 2.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties'
        }
    },
    
    'shm': {
        'natural_frequency': {
            'name': 'Natural Frequency (ω)',
            'description': 'Natural frequency in simple harmonic motion',
            'unit': 'rad/s',
            'default': 1.0,
            'range': [0.1, 100.0],
            'category': 'mechanical_properties',
            'equation': 'd²x/dt² + ω²x = 0'
        },
        'amplitude': {
            'name': 'Amplitude',
            'description': 'Oscillation amplitude',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'mechanical_properties'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration',
            'unit': 's',
            'default': 10.0,
            'range': [1.0, 100.0],
            'category': 'temporal_properties'
        }
    },
    
    'helmholtz': {
        'wavenumber': {
            'name': 'Wavenumber (k)',
            'description': 'Wavenumber in Helmholtz equation',
            'unit': '1/m',
            'default': 1.0,
            'range': [0.01, 100.0],
            'category': 'wave_properties',
            'equation': '∇²u + k²u = 0'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties'
        }
    },
    
    'navier_stokes': {
        'viscosity': {
            'name': 'Viscosity (μ)',
            'description': 'Dynamic viscosity in Navier-Stokes equations',
            'unit': 'Pa·s',
            'default': 0.001,
            'range': [1e-6, 1e-1],
            'category': 'fluid_properties'
        },
        'density': {
            'name': 'Density (ρ)',
            'description': 'Fluid density',
            'unit': 'kg/m³',
            'default': 1000.0,
            'range': [1.0, 20000.0],
            'category': 'fluid_properties'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties'
        }
    },
    
    'schrodinger': {
        'planck_constant': {
            'name': 'Planck Constant (ℏ)',
            'description': 'Reduced Planck constant',
            'unit': 'J·s',
            'default': 1.055e-34,
            'range': [1e-35, 1e-33],
            'category': 'quantum_properties'
        },
        'mass': {
            'name': 'Mass (m)',
            'description': 'Particle mass',
            'unit': 'kg',
            'default': 9.109e-31,
            'range': [1e-32, 1e-29],
            'category': 'quantum_properties'
        },
        'potential_strength': {
            'name': 'Potential Strength',
            'description': 'Strength of potential energy',
            'unit': 'J',
            'default': 1e-20,
            'range': [1e-25, 1e-15],
            'category': 'quantum_properties'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain length',
            'unit': 'm',
            'default': 1e-9,
            'range': [1e-12, 1e-6],
            'category': 'domain_properties'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration',
            'unit': 's',
            'default': 1e-15,
            'range': [1e-18, 1e-12],
            'category': 'temporal_properties'
        }
    },
    
    'maxwell': {
        'permittivity': {
            'name': 'Permittivity (ε)',
            'description': 'Electric permittivity',
            'unit': 'F/m',
            'default': 8.854e-12,
            'range': [1e-13, 1e-10],
            'category': 'electromagnetic_properties'
        },
        'magnetic_permeability': {
            'name': 'Magnetic Permeability (μ)',
            'description': 'Magnetic permeability',
            'unit': 'H/m',
            'default': 1.257e-6,
            'range': [1e-7, 1e-5],
            'category': 'electromagnetic_properties'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration',
            'unit': 's',
            'default': 1e-9,
            'range': [1e-12, 1e-6],
            'category': 'temporal_properties'
        }
    },
    
    'heat_transfer': {
        'thermal_conductivity': {
            'name': 'Thermal Conductivity (k)',
            'description': 'Thermal conductivity coefficient',
            'unit': 'W/(m·K)',
            'default': 50.0,
            'range': [0.01, 1000.0],
            'category': 'thermal_properties'
        },
        'density': {
            'name': 'Density (ρ)',
            'description': 'Material density',
            'unit': 'kg/m³',
            'default': 1000.0,
            'range': [1.0, 20000.0],
            'category': 'material_properties'
        },
        'specific_heat': {
            'name': 'Specific Heat (c_p)',
            'description': 'Specific heat capacity',
            'unit': 'J/(kg·K)',
            'default': 1000.0,
            'range': [100.0, 10000.0],
            'category': 'thermal_properties'
        },
        'heat_source': {
            'name': 'Heat Source (Q)',
            'description': 'Heat source/sink term',
            'unit': 'W/m³',
            'default': 0.0,
            'range': [-1e6, 1e6],
            'category': 'thermal_properties'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties'
        }
    },
    
    'elastic': {
        'elastic_modulus': {
            'name': 'Elastic Modulus (E)',
            'description': 'Young\'s modulus of elasticity',
            'unit': 'GPa',
            'default': 200.0,
            'range': [0.1, 1000.0],
            'category': 'mechanical_properties'
        },
        'poisson_ratio': {
            'name': 'Poisson Ratio (ν)',
            'description': 'Poisson\'s ratio',
            'unit': 'dimensionless',
            'default': 0.3,
            'range': [0.0, 0.5],
            'category': 'mechanical_properties'
        },
        'density': {
            'name': 'Density (ρ)',
            'description': 'Material density',
            'unit': 'kg/m³',
            'default': 1000.0,
            'range': [1.0, 20000.0],
            'category': 'material_properties'
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
    
    'phase_field': {
        'mobility': {
            'name': 'Mobility (M)',
            'description': 'Phase field mobility coefficient',
            'unit': 'm²/(J·s)',
            'default': 1e-3,
            'range': [1e-6, 1e-1],
            'category': 'phase_field'
        },
        'interface_thickness': {
            'name': 'Interface Thickness (ε)',
            'description': 'Phase field interface thickness parameter',
            'unit': 'm',
            'default': 1e-6,
            'range': [1e-9, 1e-3],
            'category': 'phase_field'
        },
        'free_energy_barrier': {
            'name': 'Free Energy Barrier (W)',
            'description': 'Free energy barrier for phase transitions',
            'unit': 'J/m³',
            'default': 1e6,
            'range': [1e3, 1e9],
            'category': 'phase_field'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1e-3,
            'range': [1e-6, 1e-1],
            'category': 'domain_properties'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties'
        }
    },
    
    'reaction_diffusion': {
        'diffusion_coefficient': {
            'name': 'Diffusion Coefficient (D)',
            'description': 'Diffusion coefficient for transport',
            'unit': 'm²/s',
            'default': 1e-9,
            'range': [1e-12, 1e-6],
            'category': 'transport_properties'
        },
        'reaction_rate': {
            'name': 'Reaction Rate (k)',
            'description': 'Chemical reaction rate constant',
            'unit': '1/s',
            'default': 1e-3,
            'range': [1e-6, 1e0],
            'category': 'chemical_properties'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties'
        }
    },
    
    'poroelasticity': {
        'permeability': {
            'name': 'Permeability (κ)',
            'description': 'Material permeability',
            'unit': 'm²',
            'default': 1e-12,
            'range': [1e-20, 1e-8],
            'category': 'poroelastic_properties'
        },
        'biot_coefficient': {
            'name': 'Biot Coefficient (α)',
            'description': 'Biot coefficient for poroelasticity',
            'unit': 'dimensionless',
            'default': 0.8,
            'range': [0.0, 1.0],
            'category': 'poroelastic_properties'
        },
        'elastic_modulus': {
            'name': 'Elastic Modulus (E)',
            'description': 'Young\'s modulus of elasticity',
            'unit': 'GPa',
            'default': 200.0,
            'range': [0.1, 1000.0],
            'category': 'mechanical_properties'
        },
        'poisson_ratio': {
            'name': 'Poisson Ratio (ν)',
            'description': 'Poisson\'s ratio',
            'unit': 'dimensionless',
            'default': 0.3,
            'range': [0.0, 0.5],
            'category': 'mechanical_properties'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties'
        }
    },
    
    'viscoelasticity': {
        'relaxation_time': {
            'name': 'Relaxation Time (τ)',
            'description': 'Viscoelastic relaxation time',
            'unit': 's',
            'default': 1.0,
            'range': [1e-3, 1e3],
            'category': 'viscoelastic_properties'
        },
        'retardation_time': {
            'name': 'Retardation Time (τ_r)',
            'description': 'Viscoelastic retardation time',
            'unit': 's',
            'default': 0.1,
            'range': [1e-4, 1e2],
            'category': 'viscoelastic_properties'
        },
        'elastic_modulus': {
            'name': 'Elastic Modulus (E)',
            'description': 'Young\'s modulus of elasticity',
            'unit': 'GPa',
            'default': 200.0,
            'range': [0.1, 1000.0],
            'category': 'mechanical_properties'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'domain_properties'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration',
            'unit': 's',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'temporal_properties'
        }
    },
    
    'radiative_transfer': {
        'absorption_coefficient': {
            'name': 'Absorption Coefficient (κ)',
            'description': 'Radiation absorption coefficient',
            'unit': '1/m',
            'default': 1.0,
            'range': [1e-3, 1e3],
            'category': 'radiation_properties'
        },
        'scattering_coefficient': {
            'name': 'Scattering Coefficient (σ)',
            'description': 'Radiation scattering coefficient',
            'unit': '1/m',
            'default': 0.1,
            'range': [1e-4, 1e2],
            'category': 'radiation_properties'
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
    
    'shallow_water': {
        'gravity': {
            'name': 'Gravity (g)',
            'description': 'Acceleration due to gravity',
            'unit': 'm/s²',
            'default': 9.81,
            'range': [1.0, 20.0],
            'category': 'geophysical_properties'
        },
        'coriolis_parameter': {
            'name': 'Coriolis Parameter (f)',
            'description': 'Coriolis parameter for geophysical flows',
            'unit': '1/s',
            'default': 1e-4,
            'range': [1e-5, 1e-3],
            'category': 'geophysical_properties'
        },
        'domain_size': {
            'name': 'Domain Size',
            'description': 'Spatial domain dimensions',
            'unit': 'm',
            'default': 1000.0,
            'range': [100.0, 10000.0],
            'category': 'domain_properties'
        },
        'time_duration': {
            'name': 'Time Duration',
            'description': 'Simulation time duration',
            'unit': 's',
            'default': 3600.0,
            'range': [100.0, 86400.0],
            'category': 'temporal_properties'
        }
    }
} 