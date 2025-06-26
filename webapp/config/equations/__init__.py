"""
Equation definitions for all PINN purposes.
This module imports equation dictionaries from separate files for each purpose.
"""

from .forward_problems import FORWARD_PROBLEMS_EQUATIONS_DICT
from .inverse_problems import INVERSE_PROBLEMS_EQUATIONS_DICT
from .data_assimilation import DATA_ASSIMILATION_EQUATIONS_DICT
from .control_optimization import CONTROL_OPTIMIZATION_EQUATIONS_DICT
from .sparse_data import SPARSE_DATA_EQUATIONS_DICT
from .uncertainty import UNCERTAINTY_EQUATIONS_DICT
from .multiphysics import MULTIPHYSICS_EQUATIONS_DICT
from .efficiency import EFFICIENCY_EQUATIONS_DICT
from .generalization import GENERALIZATION_EQUATIONS_DICT
from .scientific_discovery import SCIENTIFIC_DISCOVERY_EQUATIONS_DICT

# Combine all equations into a single dictionary
ALL_PURPOSE_EQUATIONS = {
    'forward_problems': FORWARD_PROBLEMS_EQUATIONS_DICT,
    'inverse_problems': INVERSE_PROBLEMS_EQUATIONS_DICT,
    'data_assimilation': DATA_ASSIMILATION_EQUATIONS_DICT,
    'control_optimization': CONTROL_OPTIMIZATION_EQUATIONS_DICT,
    'sparse_data': SPARSE_DATA_EQUATIONS_DICT,
    'uncertainty': UNCERTAINTY_EQUATIONS_DICT,
    'multiphysics': MULTIPHYSICS_EQUATIONS_DICT,
    'efficiency': EFFICIENCY_EQUATIONS_DICT,
    'generalization': GENERALIZATION_EQUATIONS_DICT,
    'scientific_discovery': SCIENTIFIC_DISCOVERY_EQUATIONS_DICT
}

# Create a flat dictionary of all equations
SUPPORTED_EQUATIONS = {}
for purpose, equations in ALL_PURPOSE_EQUATIONS.items():
    SUPPORTED_EQUATIONS.update(equations) 