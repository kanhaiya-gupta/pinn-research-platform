"""
Astrophysics Parameters
Parameters for astrophysical and cosmological applications using PINNs.
"""

ASTROPHYSICS_PARAMETERS_DICT = {
    # Gravitational Astrophysics Parameters
    'gravitational_constant': {
        'name': 'Gravitational Constant (G)',
        'description': 'Newtonian gravitational constant',
        'unit': 'm³/(kg·s²)',
        'default': 6.674e-11,
        'range': [6.67e-11, 6.68e-11],
        'category': 'fundamental_constants',
        'astrophysics_type': 'gravitational_physics'
    },
    'speed_of_light': {
        'name': 'Speed of Light (c)',
        'description': 'Speed of light in vacuum',
        'unit': 'm/s',
        'default': 2.998e8,
        'range': [2.997e8, 2.999e8],
        'category': 'fundamental_constants',
        'astrophysics_type': 'relativistic_physics'
    },
    'planck_constant': {
        'name': 'Planck Constant (h)',
        'description': 'Planck constant',
        'unit': 'J·s',
        'default': 6.626e-34,
        'range': [6.62e-34, 6.63e-34],
        'category': 'fundamental_constants',
        'astrophysics_type': 'quantum_physics'
    },
    'solar_mass': {
        'name': 'Solar Mass (M☉)',
        'description': 'Mass of the Sun',
        'unit': 'kg',
        'default': 1.989e30,
        'range': [1.98e30, 1.99e30],
        'category': 'astronomical_constants',
        'astrophysics_type': 'stellar_physics'
    },
    'parsec': {
        'name': 'Parsec (pc)',
        'description': 'Parallax second distance unit',
        'unit': 'm',
        'default': 3.086e16,
        'range': [3.08e16, 3.09e16],
        'category': 'astronomical_constants',
        'astrophysics_type': 'cosmology'
    },
    
    # General Relativity Parameters
    'schwarzschild_radius': {
        'name': 'Schwarzschild Radius (rs)',
        'description': 'Event horizon radius for black hole',
        'unit': 'm',
        'default': 1e3,
        'range': [1e2, 1e6],
        'category': 'relativistic_properties',
        'astrophysics_type': 'black_hole_physics'
    },
    'kerr_parameter': {
        'name': 'Kerr Parameter (a)',
        'description': 'Dimensionless spin parameter for rotating black hole',
        'unit': 'dimensionless',
        'default': 0.5,
        'range': [0.0, 1.0],
        'category': 'relativistic_properties',
        'astrophysics_type': 'black_hole_physics'
    },
    'cosmological_constant': {
        'name': 'Cosmological Constant (Λ)',
        'description': 'Dark energy density parameter',
        'unit': '1/m²',
        'default': 1e-52,
        'range': [1e-53, 1e-51],
        'category': 'cosmological_properties',
        'astrophysics_type': 'cosmology'
    },
    
    # Gravitational Wave Parameters
    'gravitational_wave_frequency': {
        'name': 'Gravitational Wave Frequency (fgw)',
        'description': 'Frequency of gravitational wave signal',
        'unit': 'Hz',
        'default': 100.0,
        'range': [1.0, 1000.0],
        'category': 'wave_properties',
        'astrophysics_type': 'gravitational_waves'
    },
    'chirp_mass': {
        'name': 'Chirp Mass (Mc)',
        'description': 'Chirp mass of binary system',
        'unit': 'M☉',
        'default': 10.0,
        'range': [1.0, 100.0],
        'category': 'binary_properties',
        'astrophysics_type': 'gravitational_waves'
    },
    'mass_ratio': {
        'name': 'Mass Ratio (q)',
        'description': 'Ratio of masses in binary system',
        'unit': 'dimensionless',
        'default': 0.8,
        'range': [0.1, 1.0],
        'category': 'binary_properties',
        'astrophysics_type': 'gravitational_waves'
    },
    
    # Cosmology Parameters
    'hubble_parameter': {
        'name': 'Hubble Parameter (H₀)',
        'description': 'Current expansion rate of the universe',
        'unit': 'km/(s·Mpc)',
        'default': 70.0,
        'range': [60.0, 80.0],
        'category': 'cosmological_properties',
        'astrophysics_type': 'cosmology'
    },
    'matter_density': {
        'name': 'Matter Density Parameter (Ωm)',
        'description': 'Density parameter for matter',
        'unit': 'dimensionless',
        'default': 0.3,
        'range': [0.1, 0.5],
        'category': 'cosmological_properties',
        'astrophysics_type': 'cosmology'
    },
    'dark_energy_density': {
        'name': 'Dark Energy Density Parameter (ΩΛ)',
        'description': 'Density parameter for dark energy',
        'unit': 'dimensionless',
        'default': 0.7,
        'range': [0.5, 0.9],
        'category': 'cosmological_properties',
        'astrophysics_type': 'cosmology'
    },
    'curvature_density': {
        'name': 'Curvature Density Parameter (Ωk)',
        'description': 'Density parameter for spatial curvature',
        'unit': 'dimensionless',
        'default': 0.0,
        'range': [-0.1, 0.1],
        'category': 'cosmological_properties',
        'astrophysics_type': 'cosmology'
    },
    
    # Stellar Physics Parameters
    'stellar_mass': {
        'name': 'Stellar Mass (M*)',
        'description': 'Mass of star',
        'unit': 'M☉',
        'default': 1.0,
        'range': [0.1, 100.0],
        'category': 'stellar_properties',
        'astrophysics_type': 'stellar_physics'
    },
    'stellar_radius': {
        'name': 'Stellar Radius (R*)',
        'description': 'Radius of star',
        'unit': 'R☉',
        'default': 1.0,
        'range': [0.1, 1000.0],
        'category': 'stellar_properties',
        'astrophysics_type': 'stellar_physics'
    },
    'stellar_temperature': {
        'name': 'Stellar Temperature (T*)',
        'description': 'Effective temperature of star',
        'unit': 'K',
        'default': 5778.0,
        'range': [1000.0, 50000.0],
        'category': 'stellar_properties',
        'astrophysics_type': 'stellar_physics'
    },
    'stellar_luminosity': {
        'name': 'Stellar Luminosity (L*)',
        'description': 'Luminosity of star',
        'unit': 'L☉',
        'default': 1.0,
        'range': [1e-4, 1e6],
        'category': 'stellar_properties',
        'astrophysics_type': 'stellar_physics'
    },
    
    # Neutron Star Parameters
    'neutron_star_mass': {
        'name': 'Neutron Star Mass (Mns)',
        'description': 'Mass of neutron star',
        'unit': 'M☉',
        'default': 1.4,
        'range': [1.0, 3.0],
        'category': 'compact_object_properties',
        'astrophysics_type': 'neutron_star_physics'
    },
    'neutron_star_radius': {
        'name': 'Neutron Star Radius (Rns)',
        'description': 'Radius of neutron star',
        'unit': 'km',
        'default': 12.0,
        'range': [8.0, 20.0],
        'category': 'compact_object_properties',
        'astrophysics_type': 'neutron_star_physics'
    },
    'equation_of_state_parameter': {
        'name': 'Equation of State Parameter (γ)',
        'description': 'Polytropic index for neutron star EOS',
        'unit': 'dimensionless',
        'default': 2.0,
        'range': [1.5, 3.0],
        'category': 'compact_object_properties',
        'astrophysics_type': 'neutron_star_physics'
    },
    
    # Particle Astrophysics Parameters
    'neutrino_energy': {
        'name': 'Neutrino Energy (Eν)',
        'description': 'Energy of neutrino',
        'unit': 'MeV',
        'default': 10.0,
        'range': [0.1, 1000.0],
        'category': 'particle_properties',
        'astrophysics_type': 'neutrino_physics'
    },
    'neutrino_cross_section': {
        'name': 'Neutrino Cross Section (σν)',
        'description': 'Neutrino interaction cross section',
        'unit': 'cm²',
        'default': 1e-44,
        'range': [1e-46, 1e-42],
        'category': 'particle_properties',
        'astrophysics_type': 'neutrino_physics'
    },
    'dark_matter_mass': {
        'name': 'Dark Matter Particle Mass (mDM)',
        'description': 'Mass of dark matter particle',
        'unit': 'GeV/c²',
        'default': 100.0,
        'range': [1.0, 10000.0],
        'category': 'particle_properties',
        'astrophysics_type': 'dark_matter_physics'
    },
    'dark_matter_cross_section': {
        'name': 'Dark Matter Cross Section (σDM)',
        'description': 'Dark matter interaction cross section',
        'unit': 'cm²',
        'default': 1e-46,
        'range': [1e-50, 1e-40],
        'category': 'particle_properties',
        'astrophysics_type': 'dark_matter_physics'
    },
    
    # Plasma Physics Parameters
    'plasma_density': {
        'name': 'Plasma Density (np)',
        'description': 'Number density of plasma particles',
        'unit': '1/m³',
        'default': 1e20,
        'range': [1e15, 1e25],
        'category': 'plasma_properties',
        'astrophysics_type': 'plasma_physics'
    },
    'plasma_temperature': {
        'name': 'Plasma Temperature (Tp)',
        'description': 'Temperature of plasma',
        'unit': 'K',
        'default': 1e6,
        'range': [1e4, 1e8],
        'category': 'plasma_properties',
        'astrophysics_type': 'plasma_physics'
    },
    'magnetic_field_strength': {
        'name': 'Magnetic Field Strength (B)',
        'description': 'Magnetic field strength',
        'unit': 'T',
        'default': 1e-6,
        'range': [1e-9, 1e-3],
        'category': 'magnetic_properties',
        'astrophysics_type': 'magnetohydrodynamics'
    },
    
    # Computational Parameters
    'spatial_resolution': {
        'name': 'Spatial Resolution',
        'description': 'Spatial discretization resolution',
        'unit': 'm',
        'default': 1e6,
        'range': [1e3, 1e9],
        'category': 'computational_parameters',
        'astrophysics_type': 'numerical_methods'
    },
    'temporal_resolution': {
        'name': 'Temporal Resolution',
        'description': 'Temporal discretization resolution',
        'unit': 's',
        'default': 1e-3,
        'range': [1e-6, 1e0],
        'category': 'computational_parameters',
        'astrophysics_type': 'numerical_methods'
    },
    'collocation_points': {
        'name': 'Collocation Points',
        'description': 'Number of collocation points for PINN',
        'unit': 'dimensionless',
        'default': 10000,
        'range': [1000, 100000],
        'category': 'computational_parameters',
        'astrophysics_type': 'numerical_methods'
    },
    'boundary_points': {
        'name': 'Boundary Points',
        'description': 'Number of boundary condition points',
        'unit': 'dimensionless',
        'default': 1000,
        'range': [100, 10000],
        'category': 'computational_parameters',
        'astrophysics_type': 'numerical_methods'
    },
    'initial_points': {
        'name': 'Initial Points',
        'description': 'Number of initial condition points',
        'unit': 'dimensionless',
        'default': 1000,
        'range': [100, 10000],
        'category': 'computational_parameters',
        'astrophysics_type': 'numerical_methods'
    },
    'data_points': {
        'name': 'Data Points',
        'description': 'Number of observational data points',
        'unit': 'dimensionless',
        'default': 1000,
        'range': [100, 10000],
        'category': 'computational_parameters',
        'astrophysics_type': 'numerical_methods'
    },
    
    # Training Parameters
    'learning_rate': {
        'name': 'Learning Rate',
        'description': 'Learning rate for neural network training',
        'unit': 'dimensionless',
        'default': 1e-3,
        'range': [1e-5, 1e-1],
        'category': 'training_parameters',
        'astrophysics_type': 'neural_network'
    },
    'epochs': {
        'name': 'Training Epochs',
        'description': 'Number of training epochs',
        'unit': 'dimensionless',
        'default': 10000,
        'range': [1000, 100000],
        'category': 'training_parameters',
        'astrophysics_type': 'neural_network'
    },
    'physics_weight': {
        'name': 'Physics Loss Weight',
        'description': 'Weight for physics loss term',
        'unit': 'dimensionless',
        'default': 1.0,
        'range': [0.1, 10.0],
        'category': 'training_parameters',
        'astrophysics_type': 'neural_network'
    },
    'data_weight': {
        'name': 'Data Loss Weight',
        'description': 'Weight for data loss term',
        'unit': 'dimensionless',
        'default': 1.0,
        'range': [0.1, 10.0],
        'category': 'training_parameters',
        'astrophysics_type': 'neural_network'
    },
    'boundary_weight': {
        'name': 'Boundary Loss Weight',
        'description': 'Weight for boundary condition loss term',
        'unit': 'dimensionless',
        'default': 1.0,
        'range': [0.1, 10.0],
        'category': 'training_parameters',
        'astrophysics_type': 'neural_network'
    }
}

# Equation-specific parameters for astrophysics applications
ASTROPHYSICS_EQUATION_PARAMETERS = {
    'einstein_field_equations': {
        'energy_momentum_tensor': {
            'name': 'Energy-Momentum Tensor (Tμν)',
            'description': 'Energy-momentum tensor for Einstein field equations',
            'unit': 'kg/(m·s²)',
            'default': 1e-10,
            'range': [1e-12, 1e-8],
            'category': 'relativistic_properties',
            'astrophysics_type': 'general_relativity'
        },
        'metric_tensor': {
            'name': 'Metric Tensor (gμν)',
            'description': 'Spacetime metric tensor components',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'relativistic_properties',
            'astrophysics_type': 'general_relativity'
        },
        'ricci_tensor': {
            'name': 'Ricci Tensor (Rμν)',
            'description': 'Ricci curvature tensor components',
            'unit': '1/m²',
            'default': 1e-20,
            'range': [1e-22, 1e-18],
            'category': 'relativistic_properties',
            'astrophysics_type': 'general_relativity'
        },
        'ricci_scalar': {
            'name': 'Ricci Scalar (R)',
            'description': 'Ricci scalar curvature',
            'unit': '1/m²',
            'default': 1e-20,
            'range': [1e-22, 1e-18],
            'category': 'relativistic_properties',
            'astrophysics_type': 'general_relativity'
        }
    },
    'schwarzschild_metric': {
        'black_hole_mass': {
            'name': 'Black Hole Mass (M)',
            'description': 'Mass of Schwarzschild black hole',
            'unit': 'M☉',
            'default': 10.0,
            'range': [1.0, 1000.0],
            'category': 'compact_object_properties',
            'astrophysics_type': 'black_hole_physics'
        },
        'radial_coordinate': {
            'name': 'Radial Coordinate (r)',
            'description': 'Radial coordinate in Schwarzschild metric',
            'unit': 'm',
            'default': 1e4,
            'range': [1e3, 1e6],
            'category': 'spatial_coordinates',
            'astrophysics_type': 'black_hole_physics'
        },
        'time_coordinate': {
            'name': 'Time Coordinate (t)',
            'description': 'Time coordinate in Schwarzschild metric',
            'unit': 's',
            'default': 1e-3,
            'range': [1e-6, 1e0],
            'category': 'temporal_coordinates',
            'astrophysics_type': 'black_hole_physics'
        }
    },
    'kerr_metric': {
        'black_hole_mass': {
            'name': 'Black Hole Mass (M)',
            'description': 'Mass of Kerr black hole',
            'unit': 'M☉',
            'default': 10.0,
            'range': [1.0, 1000.0],
            'category': 'compact_object_properties',
            'astrophysics_type': 'black_hole_physics'
        },
        'angular_momentum': {
            'name': 'Angular Momentum (J)',
            'description': 'Angular momentum of Kerr black hole',
            'unit': 'kg·m²/s',
            'default': 1e42,
            'range': [1e40, 1e44],
            'category': 'compact_object_properties',
            'astrophysics_type': 'black_hole_physics'
        },
        'spin_parameter': {
            'name': 'Spin Parameter (a)',
            'description': 'Dimensionless spin parameter',
            'unit': 'dimensionless',
            'default': 0.5,
            'range': [0.0, 1.0],
            'category': 'compact_object_properties',
            'astrophysics_type': 'black_hole_physics'
        }
    },
    'tolman_oppenheimer_volkoff': {
        'central_pressure': {
            'name': 'Central Pressure (Pc)',
            'description': 'Central pressure in neutron star',
            'unit': 'Pa',
            'default': 1e35,
            'range': [1e33, 1e37],
            'category': 'compact_object_properties',
            'astrophysics_type': 'neutron_star_physics'
        },
        'central_density': {
            'name': 'Central Density (ρc)',
            'description': 'Central density in neutron star',
            'unit': 'kg/m³',
            'default': 1e18,
            'range': [1e17, 1e19],
            'category': 'compact_object_properties',
            'astrophysics_type': 'neutron_star_physics'
        },
        'equation_of_state_parameter': {
            'name': 'EOS Parameter (γ)',
            'description': 'Polytropic index for neutron star',
            'unit': 'dimensionless',
            'default': 2.0,
            'range': [1.5, 3.0],
            'category': 'compact_object_properties',
            'astrophysics_type': 'neutron_star_physics'
        }
    },
    'friedmann_equations': {
        'scale_factor': {
            'name': 'Scale Factor (a)',
            'description': 'Cosmic scale factor',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.1, 10.0],
            'category': 'cosmological_properties',
            'astrophysics_type': 'cosmology'
        },
        'hubble_parameter': {
            'name': 'Hubble Parameter (H)',
            'description': 'Hubble parameter at given time',
            'unit': '1/s',
            'default': 2.3e-18,
            'range': [1e-19, 1e-17],
            'category': 'cosmological_properties',
            'astrophysics_type': 'cosmology'
        },
        'energy_density': {
            'name': 'Energy Density (ρ)',
            'description': 'Total energy density of universe',
            'unit': 'kg/m³',
            'default': 1e-27,
            'range': [1e-29, 1e-25],
            'category': 'cosmological_properties',
            'astrophysics_type': 'cosmology'
        }
    },
    'gravitational_wave_equation': {
        'wave_amplitude': {
            'name': 'Wave Amplitude (h)',
            'description': 'Gravitational wave strain amplitude',
            'unit': 'dimensionless',
            'default': 1e-21,
            'range': [1e-23, 1e-19],
            'category': 'wave_properties',
            'astrophysics_type': 'gravitational_waves'
        },
        'wave_frequency': {
            'name': 'Wave Frequency (f)',
            'description': 'Gravitational wave frequency',
            'unit': 'Hz',
            'default': 100.0,
            'range': [1.0, 1000.0],
            'category': 'wave_properties',
            'astrophysics_type': 'gravitational_waves'
        },
        'phase': {
            'name': 'Wave Phase (φ)',
            'description': 'Gravitational wave phase',
            'unit': 'rad',
            'default': 0.0,
            'range': [0.0, 2*3.14159],
            'category': 'wave_properties',
            'astrophysics_type': 'gravitational_waves'
        }
    },
    'neutrino_transport': {
        'neutrino_density': {
            'name': 'Neutrino Density (nν)',
            'description': 'Neutrino number density',
            'unit': '1/m³',
            'default': 1e38,
            'range': [1e36, 1e40],
            'category': 'particle_properties',
            'astrophysics_type': 'neutrino_physics'
        },
        'neutrino_energy': {
            'name': 'Neutrino Energy (Eν)',
            'description': 'Average neutrino energy',
            'unit': 'MeV',
            'default': 10.0,
            'range': [1.0, 100.0],
            'category': 'particle_properties',
            'astrophysics_type': 'neutrino_physics'
        },
        'cross_section': {
            'name': 'Cross Section (σ)',
            'description': 'Neutrino interaction cross section',
            'unit': 'cm²',
            'default': 1e-44,
            'range': [1e-46, 1e-42],
            'category': 'particle_properties',
            'astrophysics_type': 'neutrino_physics'
        }
    },
    'dark_matter_halo': {
        'halo_mass': {
            'name': 'Halo Mass (Mh)',
            'description': 'Total mass of dark matter halo',
            'unit': 'M☉',
            'default': 1e12,
            'range': [1e10, 1e15],
            'category': 'dark_matter_properties',
            'astrophysics_type': 'dark_matter_physics'
        },
        'scale_radius': {
            'name': 'Scale Radius (rs)',
            'description': 'Characteristic radius of halo',
            'unit': 'kpc',
            'default': 20.0,
            'range': [1.0, 100.0],
            'category': 'dark_matter_properties',
            'astrophysics_type': 'dark_matter_physics'
        },
        'central_density': {
            'name': 'Central Density (ρ₀)',
            'description': 'Central density of dark matter',
            'unit': 'M☉/kpc³',
            'default': 1e8,
            'range': [1e6, 1e10],
            'category': 'dark_matter_properties',
            'astrophysics_type': 'dark_matter_physics'
        }
    },
    'cosmic_ray_transport': {
        'diffusion_coefficient': {
            'name': 'Diffusion Coefficient (D)',
            'description': 'Spatial diffusion coefficient',
            'unit': 'cm²/s',
            'default': 1e28,
            'range': [1e26, 1e30],
            'category': 'transport_properties',
            'astrophysics_type': 'cosmic_ray_physics'
        },
        'advection_velocity': {
            'name': 'Advection Velocity (v)',
            'description': 'Advection velocity of cosmic rays',
            'unit': 'km/s',
            'default': 100.0,
            'range': [10.0, 1000.0],
            'category': 'transport_properties',
            'astrophysics_type': 'cosmic_ray_physics'
        },
        'source_function': {
            'name': 'Source Function (Q)',
            'description': 'Cosmic ray source function',
            'unit': '1/(cm³·s)',
            'default': 1e-30,
            'range': [1e-32, 1e-28],
            'category': 'transport_properties',
            'astrophysics_type': 'cosmic_ray_physics'
        }
    },
    'stellar_structure': {
        'stellar_mass': {
            'name': 'Stellar Mass (M*)',
            'description': 'Mass of the star',
            'unit': 'M☉',
            'default': 1.0,
            'range': [0.1, 100.0],
            'category': 'stellar_properties',
            'astrophysics_type': 'stellar_physics'
        },
        'stellar_radius': {
            'name': 'Stellar Radius (R*)',
            'description': 'Radius of the star',
            'unit': 'R☉',
            'default': 1.0,
            'range': [0.1, 1000.0],
            'category': 'stellar_properties',
            'astrophysics_type': 'stellar_physics'
        },
        'central_temperature': {
            'name': 'Central Temperature (Tc)',
            'description': 'Central temperature of star',
            'unit': 'K',
            'default': 1e7,
            'range': [1e6, 1e8],
            'category': 'stellar_properties',
            'astrophysics_type': 'stellar_physics'
        }
    },
    'nuclear_burning': {
        'burning_rate': {
            'name': 'Burning Rate (ε)',
            'description': 'Nuclear energy generation rate',
            'unit': 'erg/(g·s)',
            'default': 1e-10,
            'range': [1e-12, 1e-8],
            'category': 'nuclear_properties',
            'astrophysics_type': 'stellar_physics'
        },
        'temperature_exponent': {
            'name': 'Temperature Exponent (n)',
            'description': 'Temperature dependence exponent',
            'unit': 'dimensionless',
            'default': 4.0,
            'range': [2.0, 6.0],
            'category': 'nuclear_properties',
            'astrophysics_type': 'stellar_physics'
        },
        'activation_energy': {
            'name': 'Activation Energy (E₀)',
            'description': 'Nuclear reaction activation energy',
            'unit': 'keV',
            'default': 100.0,
            'range': [10.0, 1000.0],
            'category': 'nuclear_properties',
            'astrophysics_type': 'stellar_physics'
        }
    },
    'convection': {
        'temperature_gradient': {
            'name': 'Temperature Gradient (∇)',
            'description': 'Actual temperature gradient',
            'unit': 'dimensionless',
            'default': 0.4,
            'range': [0.1, 1.0],
            'category': 'convective_properties',
            'astrophysics_type': 'stellar_physics'
        },
        'adiabatic_gradient': {
            'name': 'Adiabatic Gradient (∇ad)',
            'description': 'Adiabatic temperature gradient',
            'unit': 'dimensionless',
            'default': 0.4,
            'range': [0.2, 0.6],
            'category': 'convective_properties',
            'astrophysics_type': 'stellar_physics'
        },
        'mixing_length': {
            'name': 'Mixing Length (l)',
            'description': 'Convective mixing length',
            'unit': 'Hp',
            'default': 1.5,
            'range': [0.5, 3.0],
            'category': 'convective_properties',
            'astrophysics_type': 'stellar_physics'
        }
    },
    'chandrasekhar_limit': {
        'electron_molecular_weight': {
            'name': 'Electron Molecular Weight (μe)',
            'description': 'Mean molecular weight per electron',
            'unit': 'dimensionless',
            'default': 2.0,
            'range': [1.0, 3.0],
            'category': 'degenerate_matter_properties',
            'astrophysics_type': 'stellar_physics'
        },
        'chandrasekhar_mass': {
            'name': 'Chandrasekhar Mass (MCh)',
            'description': 'Maximum white dwarf mass',
            'unit': 'M☉',
            'default': 1.44,
            'range': [1.0, 2.0],
            'category': 'degenerate_matter_properties',
            'astrophysics_type': 'stellar_physics'
        }
    },
    'friedmann_acceleration': {
        'pressure': {
            'name': 'Pressure (P)',
            'description': 'Pressure of cosmic fluid',
            'unit': 'Pa',
            'default': 1e-10,
            'range': [1e-12, 1e-8],
            'category': 'cosmological_properties',
            'astrophysics_type': 'cosmology'
        },
        'equation_of_state': {
            'name': 'Equation of State (w)',
            'description': 'Dark energy equation of state parameter',
            'unit': 'dimensionless',
            'default': -1.0,
            'range': [-1.5, -0.5],
            'category': 'cosmological_properties',
            'astrophysics_type': 'cosmology'
        }
    },
    'redshift_distance': {
        'redshift': {
            'name': 'Redshift (z)',
            'description': 'Cosmological redshift',
            'unit': 'dimensionless',
            'default': 1.0,
            'range': [0.0, 10.0],
            'category': 'cosmological_properties',
            'astrophysics_type': 'cosmology'
        },
        'luminosity_distance': {
            'name': 'Luminosity Distance (dL)',
            'description': 'Luminosity distance',
            'unit': 'Mpc',
            'default': 1000.0,
            'range': [10.0, 10000.0],
            'category': 'cosmological_properties',
            'astrophysics_type': 'cosmology'
        }
    },
    'quadrupole_formula': {
        'quadrupole_moment': {
            'name': 'Quadrupole Moment (Ḋᵢⱼ)',
            'description': 'Second time derivative of quadrupole moment',
            'unit': 'kg·m²/s³',
            'default': 1e30,
            'range': [1e28, 1e32],
            'category': 'wave_properties',
            'astrophysics_type': 'gravitational_waves'
        },
        'wave_luminosity': {
            'name': 'Wave Luminosity (L)',
            'description': 'Gravitational wave luminosity',
            'unit': 'W',
            'default': 1e30,
            'range': [1e25, 1e35],
            'category': 'wave_properties',
            'astrophysics_type': 'gravitational_waves'
        }
    },
    'chirp_mass': {
        'primary_mass': {
            'name': 'Primary Mass (m₁)',
            'description': 'Mass of primary component',
            'unit': 'M☉',
            'default': 10.0,
            'range': [1.0, 100.0],
            'category': 'binary_properties',
            'astrophysics_type': 'gravitational_waves'
        },
        'secondary_mass': {
            'name': 'Secondary Mass (m₂)',
            'description': 'Mass of secondary component',
            'unit': 'M☉',
            'default': 8.0,
            'range': [1.0, 100.0],
            'category': 'binary_properties',
            'astrophysics_type': 'gravitational_waves'
        },
        'effective_chirp_mass': {
            'name': 'Effective Chirp Mass (Mc)',
            'description': 'Effective chirp mass of binary',
            'unit': 'M☉',
            'default': 8.9,
            'range': [1.0, 50.0],
            'category': 'binary_properties',
            'astrophysics_type': 'gravitational_waves'
        }
    }
} 