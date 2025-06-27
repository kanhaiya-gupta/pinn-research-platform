"""
Efficiency Parameters
Parameters for optimizing computational efficiency and performance.
"""

EFFICIENCY_PARAMETERS_DICT = {
    # Sampling Parameters
    'collocation_points': {
        'name': 'Collocation Points',
        'description': 'Number of collocation points',
        'unit': 'dimensionless',
        'default': 1000,
        'range': [100, 100000],
        'category': 'sampling_parameters',
        'optimization_target': 'accuracy'
    },
    'boundary_points': {
        'name': 'Boundary Points',
        'description': 'Number of boundary points',
        'unit': 'dimensionless',
        'default': 100,
        'range': [10, 10000],
        'category': 'sampling_parameters',
        'optimization_target': 'accuracy'
    },
    'initial_points': {
        'name': 'Initial Points',
        'description': 'Number of initial condition points',
        'unit': 'dimensionless',
        'default': 100,
        'range': [10, 10000],
        'category': 'sampling_parameters',
        'optimization_target': 'accuracy'
    },
    'data_points': {
        'name': 'Data Points',
        'description': 'Number of observational data points',
        'unit': 'dimensionless',
        'default': 100,
        'range': [10, 10000],
        'category': 'sampling_parameters',
        'optimization_target': 'accuracy'
    },
    'spatial_discretization': {
        'name': 'Spatial Discretization',
        'description': 'Spatial discretization step size',
        'unit': 'm',
        'default': 1e-2,
        'range': [1e-4, 1e-1],
        'category': 'discretization_parameters',
        'optimization_target': 'accuracy'
    },
    'tolerance': {
        'name': 'Convergence Tolerance',
        'description': 'Tolerance for convergence criteria',
        'unit': 'dimensionless',
        'default': 1e-6,
        'range': [1e-12, 1e-3],
        'category': 'convergence_parameters',
        'optimization_target': 'accuracy'
    },
    
    # Adaptive Parameters
    'adaptive_sampling': {
        'name': 'Adaptive Sampling',
        'description': 'Whether to use adaptive sampling',
        'unit': 'dimensionless',
        'default': True,
        'range': [True, False],
        'category': 'adaptive_parameters',
        'optimization_target': 'efficiency'
    },
    'error_threshold': {
        'name': 'Error Threshold',
        'description': 'Threshold for adaptive sampling',
        'unit': 'dimensionless',
        'default': 0.01,
        'range': [1e-6, 1e-1],
        'category': 'adaptive_parameters',
        'optimization_target': 'accuracy'
    },
    'refinement_factor': {
        'name': 'Refinement Factor',
        'description': 'Factor for mesh refinement',
        'unit': 'dimensionless',
        'default': 2.0,
        'range': [1.1, 10.0],
        'category': 'adaptive_parameters',
        'optimization_target': 'efficiency'
    },
    
    # Parallel Computing Parameters
    'num_processes': {
        'name': 'Number of Processes',
        'description': 'Number of parallel processes',
        'unit': 'dimensionless',
        'default': 1,
        'range': [1, 100],
        'category': 'parallel_parameters',
        'optimization_target': 'speed'
    },
    'chunk_size': {
        'name': 'Chunk Size',
        'description': 'Size of data chunks for parallel processing',
        'unit': 'dimensionless',
        'default': 1000,
        'range': [100, 100000],
        'category': 'parallel_parameters',
        'optimization_target': 'memory'
    },
    'load_balancing': {
        'name': 'Load Balancing',
        'description': 'Load balancing strategy',
        'unit': 'dimensionless',
        'default': 'dynamic',
        'range': ['static', 'dynamic', 'adaptive'],
        'category': 'parallel_parameters',
        'optimization_target': 'speed'
    },
    
    # Memory Management Parameters
    'memory_limit': {
        'name': 'Memory Limit',
        'description': 'Memory limit for computations',
        'unit': 'GB',
        'default': 8.0,
        'range': [1.0, 100.0],
        'category': 'memory_parameters',
        'optimization_target': 'memory'
    },
    'cache_size': {
        'name': 'Cache Size',
        'description': 'Size of computation cache',
        'unit': 'MB',
        'default': 1000,
        'range': [100, 10000],
        'category': 'memory_parameters',
        'optimization_target': 'speed'
    },
    'garbage_collection': {
        'name': 'Garbage Collection',
        'description': 'Garbage collection frequency',
        'unit': 'dimensionless',
        'default': 1000,
        'range': [100, 10000],
        'category': 'memory_parameters',
        'optimization_target': 'memory'
    },
    
    # Algorithm Parameters
    'optimization_algorithm': {
        'name': 'Optimization Algorithm',
        'description': 'Optimization algorithm for training',
        'unit': 'dimensionless',
        'default': 'adam',
        'range': ['sgd', 'adam', 'lbfgs', 'rmsprop'],
        'category': 'algorithm_parameters',
        'optimization_target': 'convergence'
    },
    'line_search': {
        'name': 'Line Search',
        'description': 'Whether to use line search',
        'unit': 'dimensionless',
        'default': True,
        'range': [True, False],
        'category': 'algorithm_parameters',
        'optimization_target': 'convergence'
    },
    'momentum': {
        'name': 'Momentum',
        'description': 'Momentum parameter for optimization',
        'unit': 'dimensionless',
        'default': 0.9,
        'range': [0.0, 1.0],
        'category': 'algorithm_parameters',
        'optimization_target': 'convergence'
    },
    
    # Preconditioning Parameters
    'preconditioner': {
        'name': 'Preconditioner',
        'description': 'Type of preconditioner for linear solvers',
        'unit': 'dimensionless',
        'default': 'ilu',
        'range': ['none', 'ilu', 'amg', 'jacobi'],
        'category': 'preconditioning_parameters',
        'optimization_target': 'convergence'
    },
    'preconditioner_tolerance': {
        'name': 'Preconditioner Tolerance',
        'description': 'Tolerance for preconditioner',
        'unit': 'dimensionless',
        'default': 1e-3,
        'range': [1e-6, 1e-1],
        'category': 'preconditioning_parameters',
        'optimization_target': 'convergence'
    },
    
    # Performance Monitoring
    'performance_monitoring': {
        'name': 'Performance Monitoring',
        'description': 'Whether to monitor performance',
        'unit': 'dimensionless',
        'default': True,
        'range': [True, False],
        'category': 'monitoring_parameters',
        'optimization_target': 'efficiency'
    },
    'profiling_level': {
        'name': 'Profiling Level',
        'description': 'Level of performance profiling',
        'unit': 'dimensionless',
        'default': 'basic',
        'range': ['none', 'basic', 'detailed', 'full'],
        'category': 'monitoring_parameters',
        'optimization_target': 'efficiency'
    },
    'timing_precision': {
        'name': 'Timing Precision',
        'description': 'Precision for timing measurements',
        'unit': 's',
        'default': 1e-6,
        'range': [1e-9, 1e-3],
        'category': 'monitoring_parameters',
        'optimization_target': 'efficiency'
    }
}

# Equation-specific parameters for efficiency optimization
EFFICIENCY_EQUATION_PARAMETERS = {
    'efficiency_burgers': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1000, 'range': [100, 100000]}
    },
    'efficiency_heat': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1000, 'range': [100, 100000]}
    },
    'efficiency_wave': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1000, 'range': [100, 100000]}
    },
    'efficiency_shm': {
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 500, 'range': [100, 10000]},
        'tolerance': {**EFFICIENCY_PARAMETERS_DICT['tolerance'], 'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'efficiency_helmholtz': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1000, 'range': [100, 100000]},
        'preconditioner': {**EFFICIENCY_PARAMETERS_DICT['preconditioner'], 'default': 'ilu', 'range': ['none', 'ilu', 'amg', 'jacobi']},
        'tolerance': {**EFFICIENCY_PARAMETERS_DICT['tolerance'], 'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'efficiency_navier_stokes': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 2000, 'range': [500, 50000]},
        'preconditioner': {**EFFICIENCY_PARAMETERS_DICT['preconditioner'], 'default': 'ilu', 'range': ['none', 'ilu', 'amg', 'jacobi']}
    },
    'efficiency_schrodinger': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1000, 'range': [100, 100000]}
    },
    'efficiency_maxwell': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1000, 'range': [100, 100000]},
        'preconditioner': {**EFFICIENCY_PARAMETERS_DICT['preconditioner'], 'default': 'ilu', 'range': ['none', 'ilu', 'amg', 'jacobi']}
    },
    'efficiency_heat_transfer': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1000, 'range': [100, 100000]}
    },
    'efficiency_elastic': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1000, 'range': [100, 100000]},
        'preconditioner': {**EFFICIENCY_PARAMETERS_DICT['preconditioner'], 'default': 'ilu', 'range': ['none', 'ilu', 'amg', 'jacobi']},
        'tolerance': {**EFFICIENCY_PARAMETERS_DICT['tolerance'], 'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'efficiency_phase_field': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1000, 'range': [100, 100000]}
    },
    'efficiency_reaction_diffusion': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1000, 'range': [100, 100000]}
    },
    'efficiency_poroelasticity': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1500, 'range': [500, 20000]},
        'preconditioner': {**EFFICIENCY_PARAMETERS_DICT['preconditioner'], 'default': 'ilu', 'range': ['none', 'ilu', 'amg', 'jacobi']}
    },
    'efficiency_viscoelasticity': {
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1000, 'range': [100, 100000]},
        'tolerance': {**EFFICIENCY_PARAMETERS_DICT['tolerance'], 'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'efficiency_radiative_transfer': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1500, 'range': [500, 20000]},
        'num_processes': {**EFFICIENCY_PARAMETERS_DICT['num_processes'], 'default': 4, 'range': [1, 100]}
    },
    'efficiency_shallow_water': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1000, 'range': [100, 100000]}
    },
    'efficiency_magnetohydrodynamics': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 2000, 'range': [500, 50000]},
        'preconditioner': {**EFFICIENCY_PARAMETERS_DICT['preconditioner'], 'default': 'ilu', 'range': ['none', 'ilu', 'amg', 'jacobi']}
    },
    'efficiency_thermoelasticity': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1500, 'range': [500, 20000]},
        'preconditioner': {**EFFICIENCY_PARAMETERS_DICT['preconditioner'], 'default': 'ilu', 'range': ['none', 'ilu', 'amg', 'jacobi']}
    },
    'efficiency_advection_diffusion': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1000, 'range': [100, 100000]}
    },
    'efficiency_elastic_wave': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1000, 'range': [100, 100000]}
    },
    'efficiency_fluid_structure_interaction': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 2000, 'range': [500, 50000]},
        'preconditioner': {**EFFICIENCY_PARAMETERS_DICT['preconditioner'], 'default': 'ilu', 'range': ['none', 'ilu', 'amg', 'jacobi']}
    },
    'efficiency_electromagnetic_thermal': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1500, 'range': [500, 20000]},
        'preconditioner': {**EFFICIENCY_PARAMETERS_DICT['preconditioner'], 'default': 'ilu', 'range': ['none', 'ilu', 'amg', 'jacobi']}
    },
    'efficiency_biomechanical_transport': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1500, 'range': [500, 20000]},
        'preconditioner': {**EFFICIENCY_PARAMETERS_DICT['preconditioner'], 'default': 'ilu', 'range': ['none', 'ilu', 'amg', 'jacobi']}
    },
    'efficiency_geophysical_flow': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1000, 'range': [100, 100000]}
    },
    'efficiency_atmospheric_oceanic': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 2000, 'range': [500, 50000]},
        'num_processes': {**EFFICIENCY_PARAMETERS_DICT['num_processes'], 'default': 8, 'range': [1, 100]}
    },
    'efficiency_nuclear_thermal': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1500, 'range': [500, 20000]},
        'preconditioner': {**EFFICIENCY_PARAMETERS_DICT['preconditioner'], 'default': 'ilu', 'range': ['none', 'ilu', 'amg', 'jacobi']}
    },
    'efficiency_quantum_mechanical': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1000, 'range': [100, 100000]}
    },
    'efficiency_phase_field_allen_cahn': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1000, 'range': [100, 100000]}
    },
    'efficiency_phase_field_cahn_hilliard': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1000, 'range': [100, 100000]}
    },
    'efficiency_solidification_stefan': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1000, 'range': [100, 100000]}
    },
    'efficiency_phase_field_ginzburg_landau': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1000, 'range': [100, 100000]}
    },
    'efficiency_phase_field_swift_hohenberg': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1000, 'range': [100, 100000]}
    },
    'efficiency_phase_field_kuramoto_sivashinsky': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1000, 'range': [100, 100000]}
    },
    'efficiency_phase_field_benard_marangoni': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1000, 'range': [100, 100000]}
    },
    'efficiency_phase_field_hele_shaw': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1000, 'range': [100, 100000]}
    },
    'efficiency_phase_field_mullins_sekerka': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1000, 'range': [100, 100000]}
    },
    'efficiency_phase_field_ostwald_ripening': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1000, 'range': [100, 100000]}
    },
    'efficiency_phase_field_coarsening': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1000, 'range': [100, 100000]}
    },
    'efficiency_phase_field_grain_growth': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1000, 'range': [100, 100000]}
    },
    'efficiency_phase_field_dendritic_growth': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1000, 'range': [100, 100000]}
    },
    'efficiency_phase_field_eutectic_solidification': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1000, 'range': [100, 100000]}
    },
    'efficiency_phase_field_peritectic_solidification': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1000, 'range': [100, 100000]}
    },
    'efficiency_phase_field_monotectic_solidification': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1000, 'range': [100, 100000]}
    },
    'efficiency_grain_growth': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1000, 'range': [100, 100000]}
    },
    'efficiency_sintering': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1000, 'range': [100, 100000]}
    },
    'efficiency_laser_heat_source': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1000, 'range': [100, 100000]}
    },
    'efficiency_melt_pool_dynamics': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1500, 'range': [500, 20000]},
        'preconditioner': {**EFFICIENCY_PARAMETERS_DICT['preconditioner'], 'default': 'ilu', 'range': ['none', 'ilu', 'amg', 'jacobi']}
    },
    'efficiency_crystal_plasticity': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1000, 'range': [100, 100000]}
    },
    'efficiency_diffusion_solids': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1000, 'range': [100, 100000]}
    },
    'efficiency_precipitation_nucleation': {
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1000, 'range': [100, 100000]},
        'tolerance': {**EFFICIENCY_PARAMETERS_DICT['tolerance'], 'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'efficiency_residual_stress': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1500, 'range': [500, 20000]},
        'preconditioner': {**EFFICIENCY_PARAMETERS_DICT['preconditioner'], 'default': 'ilu', 'range': ['none', 'ilu', 'amg', 'jacobi']},
        'tolerance': {**EFFICIENCY_PARAMETERS_DICT['tolerance'], 'default': 1e-6, 'range': [1e-12, 1e-3]}
    },
    'efficiency_microstructure_evolution': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 2000, 'range': [500, 50000]},
        'num_processes': {**EFFICIENCY_PARAMETERS_DICT['num_processes'], 'default': 4, 'range': [1, 100]}
    },
    'efficiency_additive_manufacturing': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 2000, 'range': [500, 50000]},
        'num_processes': {**EFFICIENCY_PARAMETERS_DICT['num_processes'], 'default': 8, 'range': [1, 100]}
    },
    'efficiency_material_processing': {
        'spatial_discretization': {**EFFICIENCY_PARAMETERS_DICT['spatial_discretization'], 'default': 1e-2, 'range': [1e-4, 1e-1]},
        'collocation_points': {**EFFICIENCY_PARAMETERS_DICT['collocation_points'], 'default': 1500, 'range': [500, 20000]},
        'preconditioner': {**EFFICIENCY_PARAMETERS_DICT['preconditioner'], 'default': 'ilu', 'range': ['none', 'ilu', 'amg', 'jacobi']}
    }
} 