"""
Multiphysics Equations
Equations for coupled physical phenomena and multiphysics systems.
"""

MULTIPHYSICS_EQUATIONS_DICT = {
    'multiphysics_thermoelasticity': {
        'name': 'Multiphysics - Thermoelasticity',
        'description': 'Coupled heat transfer and elasticity equations',
        'icon': 'fas fa-link',
        'color': '#16a085',
        'formula': 'Heat equation + Elasticity (coupled)',
        'applications': ['Thermal stress analysis', 'Material processing', 'Structural thermal analysis']
    },
    'multiphysics_electromagnetic_thermal': {
        'name': 'Multiphysics - Electromagnetic-Thermal',
        'description': 'Coupled electromagnetic and thermal effects',
        'icon': 'fas fa-link',
        'color': '#16a085',
        'formula': 'Maxwell + Heat equation (coupled)',
        'applications': ['Electromagnetic heating', 'Microwave processing', 'Induction heating']
    },
    'multiphysics_fluid_structure_interaction': {
        'name': 'Multiphysics - Fluid-Structure Interaction',
        'description': 'Coupled fluid dynamics and structural mechanics',
        'icon': 'fas fa-link',
        'color': '#16a085',
        'formula': 'Navier-Stokes + Elasticity (coupled)',
        'applications': ['Aeroelasticity', 'Biomechanics', 'Offshore structures']
    },
    'multiphysics_biomechanical_transport': {
        'name': 'Multiphysics - Biomechanical Transport',
        'description': 'Coupled mechanics and transport in biological systems',
        'icon': 'fas fa-link',
        'color': '#16a085',
        'formula': 'Elasticity + Diffusion (coupled)',
        'applications': ['Tissue engineering', 'Drug delivery', 'Biomechanics']
    },
    'multiphysics_geophysical_flow': {
        'name': 'Multiphysics - Geophysical Flow',
        'description': 'Large-scale geophysical fluid dynamics with rotation',
        'icon': 'fas fa-link',
        'color': '#16a085',
        'formula': 'Shallow water + Coriolis (coupled)',
        'applications': ['Ocean circulation', 'Atmospheric dynamics', 'Climate modeling']
    },
    'multiphysics_atmospheric_oceanic': {
        'name': 'Multiphysics - Atmospheric-Oceanic',
        'description': 'Coupled atmospheric and oceanic dynamics',
        'icon': 'fas fa-link',
        'color': '#16a085',
        'formula': 'Atmospheric + Oceanic equations (coupled)',
        'applications': ['Climate modeling', 'Weather prediction', 'Earth system science']
    },
    'multiphysics_nuclear_thermal': {
        'name': 'Multiphysics - Nuclear Thermal',
        'description': 'Coupled nuclear reactions and heat transfer',
        'icon': 'fas fa-link',
        'color': '#16a085',
        'formula': 'Heat equation + Nuclear source (coupled)',
        'applications': ['Nuclear reactors', 'Fusion devices', 'Nuclear safety']
    },
    'multiphysics_magnetohydrodynamics': {
        'name': 'Multiphysics - Magnetohydrodynamics',
        'description': 'Coupled fluid dynamics and electromagnetism',
        'icon': 'fas fa-link',
        'color': '#16a085',
        'formula': 'Navier-Stokes + Maxwell (coupled)',
        'applications': ['Fusion plasma', 'Astrophysics', 'Space physics']
    },
    'multiphysics_poroelasticity': {
        'name': 'Multiphysics - Poroelasticity',
        'description': 'Coupled fluid flow and elastic deformation',
        'icon': 'fas fa-link',
        'color': '#16a085',
        'formula': 'Elasticity + Darcy flow (coupled)',
        'applications': ['Geomechanics', 'Hydrology', 'Petroleum engineering']
    },
    'multiphysics_viscoelasticity': {
        'name': 'Multiphysics - Viscoelasticity',
        'description': 'Coupled elastic and viscous behavior',
        'icon': 'fas fa-link',
        'color': '#16a085',
        'formula': 'Elasticity + Viscosity (coupled)',
        'applications': ['Polymer mechanics', 'Biological tissues', 'Rheology']
    },
    'multiphysics_radiative_transfer': {
        'name': 'Multiphysics - Radiative Transfer',
        'description': 'Coupled radiation and material properties',
        'icon': 'fas fa-link',
        'color': '#16a085',
        'formula': 'Radiative transfer + Heat equation (coupled)',
        'applications': ['Atmospheric radiation', 'Astrophysics', 'Remote sensing']
    },
    'multiphysics_phase_field': {
        'name': 'Multiphysics - Phase Field',
        'description': 'Coupled phase transitions and mechanics',
        'icon': 'fas fa-link',
        'color': '#16a085',
        'formula': 'Phase field + Elasticity (coupled)',
        'applications': ['Phase transformations', 'Crystal growth', 'Material science']
    },
    'multiphysics_reaction_diffusion': {
        'name': 'Multiphysics - Reaction-Diffusion',
        'description': 'Coupled chemical reactions and transport',
        'icon': 'fas fa-link',
        'color': '#16a085',
        'formula': 'Diffusion + Chemical kinetics (coupled)',
        'applications': ['Chemical kinetics', 'Pattern formation', 'Biological systems']
    },
    'multiphysics_advection_diffusion': {
        'name': 'Multiphysics - Advection-Diffusion',
        'description': 'Coupled transport and diffusion',
        'icon': 'fas fa-link',
        'color': '#16a085',
        'formula': 'Advection + Diffusion (coupled)',
        'applications': ['Pollutant transport', 'Ocean circulation', 'Atmospheric dispersion']
    },
    'multiphysics_elastic_wave': {
        'name': 'Multiphysics - Elastic Wave',
        'description': 'Coupled elastic waves and material properties',
        'icon': 'fas fa-link',
        'color': '#16a085',
        'formula': 'Wave equation + Elasticity (coupled)',
        'applications': ['Seismology', 'Ultrasound', 'Non-destructive testing']
    },
    'multiphysics_quantum_mechanical': {
        'name': 'Multiphysics - Quantum Mechanical',
        'description': 'Coupled quantum mechanics and classical physics',
        'icon': 'fas fa-link',
        'color': '#16a085',
        'formula': 'Schrödinger + Classical equations (coupled)',
        'applications': ['Quantum chemistry', 'Molecular dynamics', 'Quantum computing']
    },
    'multiphysics_thermoelectric': {
        'name': 'Multiphysics - Thermoelectric',
        'description': 'Coupled heat and electrical transport',
        'icon': 'fas fa-link',
        'color': '#16a085',
        'formula': 'Heat equation + Electrical conduction (coupled)',
        'applications': ['Thermoelectric devices', 'Energy harvesting', 'Thermal management']
    },
    'multiphysics_electrochemical': {
        'name': 'Multiphysics - Electrochemical',
        'description': 'Coupled electrical and chemical processes',
        'icon': 'fas fa-link',
        'color': '#16a085',
        'formula': 'Electrical conduction + Chemical kinetics (coupled)',
        'applications': ['Batteries', 'Fuel cells', 'Electrochemical sensors']
    },
    'multiphysics_thermochemical': {
        'name': 'Multiphysics - Thermochemical',
        'description': 'Coupled thermal and chemical processes',
        'icon': 'fas fa-link',
        'color': '#16a085',
        'formula': 'Heat equation + Chemical kinetics (coupled)',
        'applications': ['Combustion', 'Chemical reactors', 'Material synthesis']
    },
    'multiphysics_mechanical_electrical': {
        'name': 'Multiphysics - Mechanical-Electrical',
        'description': 'Coupled mechanical and electrical effects',
        'icon': 'fas fa-link',
        'color': '#16a085',
        'formula': 'Elasticity + Electrical conduction (coupled)',
        'applications': ['Piezoelectric devices', 'Smart materials', 'Energy harvesting']
    },
    'multiphysics_optical_mechanical': {
        'name': 'Multiphysics - Optical-Mechanical',
        'description': 'Coupled optical and mechanical effects',
        'icon': 'fas fa-link',
        'color': '#16a085',
        'formula': 'Optical equations + Elasticity (coupled)',
        'applications': ['Optomechanics', 'Photonic devices', 'Optical sensors']
    },
    'multiphysics_magnetic_mechanical': {
        'name': 'Multiphysics - Magnetic-Mechanical',
        'description': 'Coupled magnetic and mechanical effects',
        'icon': 'fas fa-link',
        'color': '#16a085',
        'formula': 'Magnetic equations + Elasticity (coupled)',
        'applications': ['Magnetostriction', 'Magnetic materials', 'Magnetic sensors']
    },
    'multiphysics_acoustic_elastic': {
        'name': 'Multiphysics - Acoustic-Elastic',
        'description': 'Coupled acoustic and elastic waves',
        'icon': 'fas fa-link',
        'color': '#16a085',
        'formula': 'Acoustic equations + Elasticity (coupled)',
        'applications': ['Seismology', 'Ultrasound imaging', 'Acoustic metamaterials']
    },
    'multiphysics_thermal_optical': {
        'name': 'Multiphysics - Thermal-Optical',
        'description': 'Coupled thermal and optical effects',
        'icon': 'fas fa-link',
        'color': '#16a085',
        'formula': 'Heat equation + Optical equations (coupled)',
        'applications': ['Thermal imaging', 'Optical sensors', 'Thermal optics']
    },
    'multiphysics_chemical_mechanical': {
        'name': 'Multiphysics - Chemical-Mechanical',
        'description': 'Coupled chemical and mechanical processes',
        'icon': 'fas fa-link',
        'color': '#16a085',
        'formula': 'Chemical kinetics + Elasticity (coupled)',
        'applications': ['Corrosion', 'Material degradation', 'Chemical-mechanical polishing']
    },
    'multiphysics_biological_mechanical': {
        'name': 'Multiphysics - Biological-Mechanical',
        'description': 'Coupled biological and mechanical processes',
        'icon': 'fas fa-link',
        'color': '#16a085',
        'formula': 'Biological equations + Elasticity (coupled)',
        'applications': ['Cell mechanics', 'Tissue engineering', 'Biomechanics']
    },
    'phase_field_mechanics': {
        'name': 'Multiphysics - Phase Field-Mechanics',
        'description': 'Coupled phase field and mechanical deformation',
        'icon': 'fas fa-link',
        'color': '#16a085',
        'formula': 'Phase field + Elasticity (coupled)',
        'applications': ['Phase transformations', 'Microstructure evolution', 'Material science']
    },
    'phase_field_heat': {
        'name': 'Multiphysics - Phase Field-Heat',
        'description': 'Coupled phase field and heat transfer',
        'icon': 'fas fa-link',
        'color': '#16a085',
        'formula': 'Phase field + Heat equation (coupled)',
        'applications': ['Thermal phase transformations', 'Solidification', 'Material processing']
    },
    'solidification_mechanics': {
        'name': 'Multiphysics - Solidification-Mechanics',
        'description': 'Coupled solidification and mechanical stress',
        'icon': 'fas fa-link',
        'color': '#16a085',
        'formula': 'Stefan problem + Elasticity (coupled)',
        'applications': ['Solidification stress', 'Casting', 'Additive manufacturing']
    },
    'sintering_mechanics': {
        'name': 'Multiphysics - Sintering-Mechanics',
        'description': 'Coupled sintering and mechanical deformation',
        'icon': 'fas fa-link',
        'color': '#16a085',
        'formula': 'Sintering + Elasticity (coupled)',
        'applications': ['Sintering stress', 'Powder metallurgy', 'Ceramics']
    },
    'laser_material_interaction': {
        'name': 'Multiphysics - Laser-Material Interaction',
        'description': 'Coupled laser heating and material response',
        'icon': 'fas fa-link',
        'color': '#16a085',
        'formula': 'Laser heat source + Material equations (coupled)',
        'applications': ['Additive manufacturing', 'Laser processing', 'Material modification']
    },
    'melt_pool_thermomechanics': {
        'name': 'Multiphysics - Melt Pool-Thermomechanics',
        'description': 'Coupled melt pool dynamics and thermal-mechanical response',
        'icon': 'fas fa-link',
        'color': '#16a085',
        'formula': 'Melt pool + Heat + Elasticity (coupled)',
        'applications': ['Additive manufacturing', 'Welding', 'Laser processing']
    },
    'crystal_plasticity_heat': {
        'name': 'Multiphysics - Crystal Plasticity-Heat',
        'description': 'Coupled crystal plasticity and heat generation',
        'icon': 'fas fa-link',
        'color': '#16a085',
        'formula': 'Crystal plasticity + Heat equation (coupled)',
        'applications': ['Metal forming', 'Thermal-mechanical processing', 'Material science']
    },
    'diffusion_mechanics': {
        'name': 'Multiphysics - Diffusion-Mechanics',
        'description': 'Coupled diffusion and mechanical stress',
        'icon': 'fas fa-link',
        'color': '#16a085',
        'formula': 'Diffusion + Elasticity (coupled)',
        'applications': ['Stress-assisted diffusion', 'Material processing', 'Heat treatment']
    },
    'precipitation_mechanics': {
        'name': 'Multiphysics - Precipitation-Mechanics',
        'description': 'Coupled precipitation and mechanical response',
        'icon': 'fas fa-link',
        'color': '#16a085',
        'formula': 'Precipitation + Elasticity (coupled)',
        'applications': ['Age hardening', 'Precipitation strengthening', 'Material science']
    },
    'grain_growth_mechanics': {
        'name': 'Multiphysics - Grain Growth-Mechanics',
        'description': 'Coupled grain growth and mechanical stress',
        'icon': 'fas fa-link',
        'color': '#16a085',
        'formula': 'Grain growth + Elasticity (coupled)',
        'applications': ['Stress-assisted grain growth', 'Recrystallization', 'Material processing']
    },
    'additive_manufacturing_process': {
        'name': 'Multiphysics - Additive Manufacturing Process',
        'description': 'Coupled AM process physics including laser, melt pool, and solidification',
        'icon': 'fas fa-link',
        'color': '#16a085',
        'formula': 'Laser + Melt pool + Solidification + Mechanics (coupled)',
        'applications': ['Additive manufacturing', '3D printing', 'Laser processing']
    },
    'material_processing_thermomechanics': {
        'name': 'Multiphysics - Material Processing-Thermomechanics',
        'description': 'Coupled thermal-mechanical response in material processing',
        'icon': 'fas fa-link',
        'color': '#16a085',
        'formula': 'Heat equation + Elasticity + Phase transformations (coupled)',
        'applications': ['Material processing', 'Heat treatment', 'Thermal-mechanical processing']
    },
    'microstructure_mechanics': {
        'name': 'Multiphysics - Microstructure-Mechanics',
        'description': 'Coupled microstructure evolution and mechanical response',
        'icon': 'fas fa-link',
        'color': '#16a085',
        'formula': 'Multiple phase fields + Elasticity (coupled)',
        'applications': ['Microstructure design', 'Material science', 'Mechanical behavior']
    },
    'powder_processing_thermomechanics': {
        'name': 'Multiphysics - Powder Processing-Thermomechanics',
        'description': 'Coupled powder processing and thermal-mechanical response',
        'icon': 'fas fa-link',
        'color': '#16a085',
        'formula': 'Powder flow + Heat + Mechanics (coupled)',
        'applications': ['Powder metallurgy', 'Additive manufacturing', 'Powder processing']
    }
} 