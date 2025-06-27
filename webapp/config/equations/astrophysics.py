"""
Astrophysics Equations
Equations for astrophysical and cosmological applications using PINNs.
"""

ASTROPHYSICS_EQUATIONS = {
    # General Relativity Equations
    'einstein_field_equations': {
        'name': 'Einstein Field Equations',
        'description': 'Fundamental equations of general relativity relating spacetime curvature to energy-momentum',
        'formula': 'Gμν + Λgμν = (8πG/c⁴)Tμν',
        'icon': 'fas fa-grav',
        'color': '#9b59b6',
        'variables': ['gμν', 'Rμν', 'R', 'Tμν', 'Λ'],
        'category': 'general_relativity',
        'difficulty': 'advanced',
        'applications': ['black_holes', 'cosmology', 'gravitational_waves']
    },
    'schwarzschild_metric': {
        'name': 'Schwarzschild Metric',
        'description': 'Spacetime metric around a spherically symmetric mass',
        'formula': 'ds² = -(1-2GM/rc²)dt² + (1-2GM/rc²)⁻¹dr² + r²(dθ² + sin²θdφ²)',
        'icon': 'fas fa-circle',
        'color': '#2c3e50',
        'variables': ['M', 'r', 't', 'θ', 'φ'],
        'category': 'black_hole_physics',
        'difficulty': 'intermediate',
        'applications': ['black_holes', 'stellar_physics']
    },
    'kerr_metric': {
        'name': 'Kerr Metric',
        'description': 'Spacetime metric around a rotating black hole',
        'formula': 'ds² = -(1-2GMr/Σc²)dt² - (4GMar sin²θ/Σc²)dtdφ + (Σ/Δ)dr² + Σdθ² + (r²+a²+2GMa²r sin²θ/Σc²)sin²θdφ²',
        'icon': 'fas fa-sync',
        'color': '#34495e',
        'variables': ['M', 'a', 'r', 't', 'θ', 'φ'],
        'category': 'black_hole_physics',
        'difficulty': 'advanced',
        'applications': ['rotating_black_holes', 'accretion_disks']
    },
    
    # Compact Object Equations
    'tolman_oppenheimer_volkoff': {
        'name': 'Tolman-Oppenheimer-Volkoff Equations',
        'description': 'Equations for hydrostatic equilibrium in general relativity',
        'formula': 'dP/dr = -G(M+4πr³P/c²)(ρ+P/c²)/(r²(1-2GM/rc²))',
        'icon': 'fas fa-compress-arrows-alt',
        'color': '#e74c3c',
        'variables': ['P', 'ρ', 'M', 'r'],
        'category': 'neutron_star_physics',
        'difficulty': 'advanced',
        'applications': ['neutron_stars', 'white_dwarfs']
    },
    'chandrasekhar_limit': {
        'name': 'Chandrasekhar Limit',
        'description': 'Maximum mass of a white dwarf supported by electron degeneracy pressure',
        'formula': 'MCh = (5.76/μe²)M☉',
        'icon': 'fas fa-balance-scale',
        'color': '#f39c12',
        'variables': ['M', 'μe'],
        'category': 'stellar_physics',
        'difficulty': 'intermediate',
        'applications': ['white_dwarfs', 'supernovae']
    },
    
    # Cosmology Equations
    'friedmann_equations': {
        'name': 'Friedmann Equations',
        'description': 'Equations governing the expansion of the universe',
        'formula': '(ȧ/a)² = (8πG/3)ρ - kc²/a² + Λc²/3',
        'icon': 'fas fa-expand-arrows-alt',
        'color': '#3498db',
        'variables': ['a', 'ρ', 'k', 'Λ'],
        'category': 'cosmology',
        'difficulty': 'intermediate',
        'applications': ['universe_expansion', 'dark_energy']
    },
    'friedmann_acceleration': {
        'name': 'Friedmann Acceleration Equation',
        'description': 'Second Friedmann equation for cosmic acceleration',
        'formula': 'ä/a = -(4πG/3)(ρ+3P/c²) + Λc²/3',
        'icon': 'fas fa-rocket',
        'color': '#2980b9',
        'variables': ['a', 'ρ', 'P', 'Λ'],
        'category': 'cosmology',
        'difficulty': 'intermediate',
        'applications': ['dark_energy', 'inflation']
    },
    'redshift_distance': {
        'name': 'Redshift-Distance Relation',
        'description': 'Relationship between redshift and distance in expanding universe',
        'formula': 'd = (c/H₀)∫₀^z dz/√(Ωm(1+z)³ + ΩΛ)',
        'icon': 'fas fa-arrows-alt-h',
        'color': '#1abc9c',
        'variables': ['z', 'd', 'H₀', 'Ωm', 'ΩΛ'],
        'category': 'cosmology',
        'difficulty': 'intermediate',
        'applications': ['distance_measurements', 'dark_energy']
    },
    
    # Gravitational Wave Equations
    'gravitational_wave_equation': {
        'name': 'Gravitational Wave Equation',
        'description': 'Wave equation for gravitational radiation in weak field limit',
        'formula': '□hμν = -16πG/c⁴ Tμν',
        'icon': 'fas fa-wave-square',
        'color': '#8e44ad',
        'variables': ['hμν', 'Tμν'],
        'category': 'gravitational_waves',
        'difficulty': 'advanced',
        'applications': ['binary_mergers', 'lisa_detector']
    },
    'quadrupole_formula': {
        'name': 'Quadrupole Formula',
        'description': 'Gravitational wave luminosity from quadrupole radiation',
        'formula': 'L = (32G/5c⁵)⟨ḊᵢⱼḊⁱʲ⟩',
        'icon': 'fas fa-broadcast-tower',
        'color': '#7d3c98',
        'variables': ['L', 'Ḋᵢⱼ'],
        'category': 'gravitational_waves',
        'difficulty': 'intermediate',
        'applications': ['binary_evolution', 'wave_emission']
    },
    'chirp_mass': {
        'name': 'Chirp Mass',
        'description': 'Effective mass parameter for binary gravitational wave sources',
        'formula': 'Mc = (m₁m₂)³/⁵/(m₁+m₂)¹/⁵',
        'icon': 'fas fa-link',
        'color': '#6c3483',
        'variables': ['Mc', 'm₁', 'm₂'],
        'category': 'gravitational_waves',
        'difficulty': 'basic',
        'applications': ['binary_mergers', 'parameter_estimation']
    },
    
    # Particle Astrophysics Equations
    'neutrino_transport': {
        'name': 'Neutrino Transport Equation',
        'description': 'Boltzmann equation for neutrino transport in dense matter',
        'formula': '∂f/∂t + v·∇f = (∂f/∂t)collision',
        'icon': 'fas fa-atom',
        'color': '#e67e22',
        'variables': ['f', 'v', 't'],
        'category': 'neutrino_physics',
        'difficulty': 'advanced',
        'applications': ['supernovae', 'neutron_stars']
    },
    'dark_matter_halo': {
        'name': 'Dark Matter Halo Profile',
        'description': 'NFW profile for dark matter density distribution',
        'formula': 'ρ(r) = ρ₀/((r/rs)(1+r/rs)²)',
        'icon': 'fas fa-moon',
        'color': '#2c3e50',
        'variables': ['ρ', 'r', 'ρ₀', 'rs'],
        'category': 'dark_matter_physics',
        'difficulty': 'intermediate',
        'applications': ['galaxy_formation', 'structure_formation']
    },
    'cosmic_ray_transport': {
        'name': 'Cosmic Ray Transport Equation',
        'description': 'Diffusion equation for cosmic ray propagation',
        'formula': '∂N/∂t = ∇·(D∇N) - ∇·(vN) + Q',
        'icon': 'fas fa-bolt',
        'color': '#f1c40f',
        'variables': ['N', 'D', 'v', 'Q'],
        'category': 'cosmic_ray_physics',
        'difficulty': 'intermediate',
        'applications': ['galactic_cosmic_rays', 'interstellar_medium']
    },
    
    # Stellar Physics Equations
    'stellar_structure': {
        'name': 'Stellar Structure Equations',
        'description': 'Basic equations of stellar structure and evolution',
        'formula': 'dP/dr = -GM(r)ρ/r², dM/dr = 4πr²ρ',
        'icon': 'fas fa-star',
        'color': '#f39c12',
        'variables': ['P', 'M', 'ρ', 'r'],
        'category': 'stellar_physics',
        'difficulty': 'intermediate',
        'applications': ['stellar_evolution', 'stellar_interiors']
    },
    'nuclear_burning': {
        'name': 'Nuclear Burning Rate',
        'description': 'Nuclear reaction rate for stellar fusion',
        'formula': 'ε = ε₀ρ²Tⁿ exp(-E₀/kT)',
        'icon': 'fas fa-fire',
        'color': '#e74c3c',
        'variables': ['ε', 'ρ', 'T', 'E₀'],
        'category': 'stellar_physics',
        'difficulty': 'intermediate',
        'applications': ['stellar_evolution', 'nucleosynthesis']
    },
    'convection': {
        'name': 'Convection Criterion',
        'description': 'Schwarzschild criterion for convective instability',
        'formula': '∇ > ∇ad',
        'icon': 'fas fa-arrows-alt-v',
        'color': '#3498db',
        'variables': ['∇', '∇ad'],
        'category': 'stellar_physics',
        'difficulty': 'basic',
        'applications': ['stellar_interiors', 'mixing']
    },
    
    # Binary System Equations
    'binary_evolution': {
        'name': 'Binary Evolution Equations',
        'description': 'Equations for orbital evolution of binary systems',
        'formula': 'ȧ/a = -2Ṁ/M - 2J̇/J',
        'icon': 'fas fa-sync-alt',
        'color': '#9b59b6',
        'variables': ['a', 'M', 'J'],
        'category': 'binary_physics',
        'difficulty': 'intermediate',
        'applications': ['binary_evolution', 'mass_transfer']
    },
    'roche_lobe': {
        'name': 'Roche Lobe Radius',
        'description': 'Approximate radius of Roche lobe in binary system',
        'formula': 'RL/a ≈ 0.49q^(2/3)/(0.6q^(2/3) + ln(1+q^(1/3)))',
        'icon': 'fas fa-circle-notch',
        'color': '#34495e',
        'variables': ['RL', 'a', 'q'],
        'category': 'binary_physics',
        'difficulty': 'basic',
        'applications': ['mass_transfer', 'binary_evolution']
    },
    
    # Explosion Physics
    'supernova_explosion': {
        'name': 'Supernova Explosion Dynamics',
        'description': 'Shock wave propagation in supernova explosion',
        'formula': '∂ρ/∂t + ∇·(ρv) = 0, ρ(∂v/∂t + v·∇v) = -∇P',
        'icon': 'fas fa-bomb',
        'color': '#e74c3c',
        'variables': ['ρ', 'v', 'P'],
        'category': 'supernova_physics',
        'difficulty': 'advanced',
        'applications': ['supernovae', 'nucleosynthesis']
    },
    'shock_jump_conditions': {
        'name': 'Shock Jump Conditions',
        'description': 'Rankine-Hugoniot conditions across shock front',
        'formula': 'ρ₁v₁ = ρ₂v₂, P₁ + ρ₁v₁² = P₂ + ρ₂v₂²',
        'icon': 'fas fa-arrow-right',
        'color': '#c0392b',
        'variables': ['ρ₁', 'ρ₂', 'v₁', 'v₂', 'P₁', 'P₂'],
        'category': 'supernova_physics',
        'difficulty': 'intermediate',
        'applications': ['shock_waves', 'explosions']
    },
    
    # Accretion Physics
    'accretion_disk': {
        'name': 'Accretion Disk Equations',
        'description': 'Thin disk equations for accretion onto compact objects',
        'formula': 'Ṁ = 3πνΣ, ν = αcsH',
        'icon': 'fas fa-compress',
        'color': '#8e44ad',
        'variables': ['Ṁ', 'ν', 'Σ', 'α', 'cs', 'H'],
        'category': 'accretion_physics',
        'difficulty': 'intermediate',
        'applications': ['black_holes', 'neutron_stars']
    },
    'eddington_luminosity': {
        'name': 'Eddington Luminosity',
        'description': 'Maximum luminosity for radiation pressure balance',
        'formula': 'LEdd = 4πGMc/κes',
        'icon': 'fas fa-sun',
        'color': '#f39c12',
        'variables': ['LEdd', 'M', 'κes'],
        'category': 'accretion_physics',
        'difficulty': 'basic',
        'applications': ['accretion_disks', 'quasars']
    },
    
    # Galaxy Formation
    'galaxy_formation': {
        'name': 'Galaxy Formation Equations',
        'description': 'Equations for galaxy formation and evolution',
        'formula': '∂ρ/∂t + ∇·(ρv) = -ρ/tcool',
        'icon': 'fas fa-galaxy',
        'color': '#3498db',
        'variables': ['ρ', 'v', 'tcool'],
        'category': 'galaxy_formation',
        'difficulty': 'advanced',
        'applications': ['galaxy_evolution', 'structure_formation']
    },
    'star_formation_rate': {
        'name': 'Star Formation Rate',
        'description': 'Kennicutt-Schmidt relation for star formation',
        'formula': 'ΣSFR = A(Σgas)^N',
        'icon': 'fas fa-baby',
        'color': '#2ecc71',
        'variables': ['ΣSFR', 'Σgas', 'A', 'N'],
        'category': 'galaxy_formation',
        'difficulty': 'basic',
        'applications': ['galaxy_evolution', 'star_formation']
    },
    
    # Magnetohydrodynamics
    'magnetohydrodynamics': {
        'name': 'Magnetohydrodynamics Equations',
        'description': 'MHD equations for magnetized plasma',
        'formula': '∂B/∂t = ∇×(v×B) + η∇²B',
        'icon': 'fas fa-magnet',
        'color': '#9b59b6',
        'variables': ['B', 'v', 'η'],
        'category': 'magnetohydrodynamics',
        'difficulty': 'advanced',
        'applications': ['accretion_disks', 'galactic_dynamics']
    },
    'alfven_wave': {
        'name': 'Alfvén Wave Equation',
        'description': 'Wave equation for Alfvén waves in magnetized plasma',
        'formula': '∂²B/∂t² = vA²∇²B',
        'icon': 'fas fa-wave-square',
        'color': '#8e44ad',
        'variables': ['B', 'vA'],
        'category': 'magnetohydrodynamics',
        'difficulty': 'intermediate',
        'applications': ['plasma_waves', 'magnetic_fields']
    },
    
    # Quantum Astrophysics
    'quantum_tunneling': {
        'name': 'Quantum Tunneling',
        'description': 'Tunneling probability for quantum processes',
        'formula': 'T ≈ exp(-2∫√(2m(V-E)/ℏ²)dx)',
        'icon': 'fas fa-atom',
        'color': '#e67e22',
        'variables': ['T', 'm', 'V', 'E'],
        'category': 'quantum_physics',
        'difficulty': 'intermediate',
        'applications': ['nuclear_fusion', 'quantum_effects']
    },
    'hawking_radiation': {
        'name': 'Hawking Radiation',
        'description': 'Black body radiation from black hole horizon',
        'formula': 'T = ℏc³/(8πGMk)',
        'icon': 'fas fa-radiation',
        'color': '#2c3e50',
        'variables': ['T', 'M'],
        'category': 'quantum_physics',
        'difficulty': 'advanced',
        'applications': ['black_holes', 'quantum_gravity']
    },
    
    # Relativistic Hydrodynamics
    'relativistic_hydrodynamics': {
        'name': 'Relativistic Hydrodynamics',
        'description': 'Relativistic fluid equations for high-energy astrophysics',
        'formula': '∂Tμν/∂xν = 0',
        'icon': 'fas fa-tachometer-alt',
        'color': '#e74c3c',
        'variables': ['Tμν'],
        'category': 'relativistic_physics',
        'difficulty': 'advanced',
        'applications': ['gamma_ray_bursts', 'relativistic_jets']
    },
    'relativistic_blast_wave': {
        'name': 'Relativistic Blast Wave',
        'description': 'Blandford-McKee solution for relativistic blast wave',
        'formula': 'γ² = (17E/8πρ₀c²r³)',
        'icon': 'fas fa-expand',
        'color': '#c0392b',
        'variables': ['γ', 'E', 'ρ₀', 'r'],
        'category': 'relativistic_physics',
        'difficulty': 'advanced',
        'applications': ['gamma_ray_bursts', 'supernovae']
    }
}

# Equation categories for astrophysics
ASTROPHYSICS_EQUATION_CATEGORIES = {
    'general_relativity': {
        'name': 'General Relativity',
        'description': 'Einstein\'s theory of gravity and spacetime',
        'equations': ['einstein_field_equations', 'schwarzschild_metric', 'kerr_metric']
    },
    'black_hole_physics': {
        'name': 'Black Hole Physics',
        'description': 'Physics of black holes and event horizons',
        'equations': ['schwarzschild_metric', 'kerr_metric', 'hawking_radiation']
    },
    'neutron_star_physics': {
        'name': 'Neutron Star Physics',
        'description': 'Physics of neutron stars and dense matter',
        'equations': ['tolman_oppenheimer_volkoff', 'chandrasekhar_limit']
    },
    'cosmology': {
        'name': 'Cosmology',
        'description': 'Study of the universe as a whole',
        'equations': ['friedmann_equations', 'friedmann_acceleration', 'redshift_distance']
    },
    'gravitational_waves': {
        'name': 'Gravitational Waves',
        'description': 'Ripples in spacetime from massive objects',
        'equations': ['gravitational_wave_equation', 'quadrupole_formula', 'chirp_mass']
    },
    'neutrino_physics': {
        'name': 'Neutrino Physics',
        'description': 'Physics of neutrino interactions and transport',
        'equations': ['neutrino_transport']
    },
    'dark_matter_physics': {
        'name': 'Dark Matter Physics',
        'description': 'Physics of dark matter and its distribution',
        'equations': ['dark_matter_halo']
    },
    'cosmic_ray_physics': {
        'name': 'Cosmic Ray Physics',
        'description': 'Physics of high-energy cosmic rays',
        'equations': ['cosmic_ray_transport']
    },
    'stellar_physics': {
        'name': 'Stellar Physics',
        'description': 'Physics of stars and stellar evolution',
        'equations': ['stellar_structure', 'nuclear_burning', 'convection']
    },
    'binary_physics': {
        'name': 'Binary Physics',
        'description': 'Physics of binary star systems',
        'equations': ['binary_evolution', 'roche_lobe']
    },
    'supernova_physics': {
        'name': 'Supernova Physics',
        'description': 'Physics of stellar explosions',
        'equations': ['supernova_explosion', 'shock_jump_conditions']
    },
    'accretion_physics': {
        'name': 'Accretion Physics',
        'description': 'Physics of mass accretion onto compact objects',
        'equations': ['accretion_disk', 'eddington_luminosity']
    },
    'galaxy_formation': {
        'name': 'Galaxy Formation',
        'description': 'Formation and evolution of galaxies',
        'equations': ['galaxy_formation', 'star_formation_rate']
    },
    'magnetohydrodynamics': {
        'name': 'Magnetohydrodynamics',
        'description': 'Physics of magnetized plasmas',
        'equations': ['magnetohydrodynamics', 'alfven_wave']
    },
    'quantum_physics': {
        'name': 'Quantum Physics',
        'description': 'Quantum effects in astrophysics',
        'equations': ['quantum_tunneling', 'hawking_radiation']
    },
    'relativistic_physics': {
        'name': 'Relativistic Physics',
        'description': 'Relativistic effects in astrophysics',
        'equations': ['relativistic_hydrodynamics', 'relativistic_blast_wave']
    }
} 