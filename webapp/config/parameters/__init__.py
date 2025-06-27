"""
Parameter definitions for all PINN purposes.
This module imports parameter dictionaries from separate files for each purpose.
"""

from .forward_problems import FORWARD_PROBLEMS_PARAMETERS_DICT
from .inverse_problems import INVERSE_PROBLEMS_PARAMETERS_DICT
from .data_assimilation import DATA_ASSIMILATION_PARAMETERS_DICT
from .control_optimization import CONTROL_OPTIMIZATION_PARAMETERS_DICT
from .sparse_data import SPARSE_DATA_PARAMETERS_DICT
from .uncertainty import UNCERTAINTY_PARAMETERS_DICT
from .multiphysics import MULTIPHYSICS_PARAMETERS_DICT
from .efficiency import EFFICIENCY_PARAMETERS_DICT
from .generalization import GENERALIZATION_PARAMETERS_DICT
from .scientific_discovery import SCIENTIFIC_DISCOVERY_PARAMETERS_DICT
from .astrophysics import ASTROPHYSICS_PARAMETERS_DICT, ASTROPHYSICS_EQUATION_PARAMETERS

# Combine all parameters into a single dictionary
ALL_PURPOSE_PARAMETERS = {
    'forward_problems': FORWARD_PROBLEMS_PARAMETERS_DICT,
    'inverse_problems': INVERSE_PROBLEMS_PARAMETERS_DICT,
    'data_assimilation': DATA_ASSIMILATION_PARAMETERS_DICT,
    'control_optimization': CONTROL_OPTIMIZATION_PARAMETERS_DICT,
    'sparse_data': SPARSE_DATA_PARAMETERS_DICT,
    'uncertainty': UNCERTAINTY_PARAMETERS_DICT,
    'multiphysics': MULTIPHYSICS_PARAMETERS_DICT,
    'efficiency': EFFICIENCY_PARAMETERS_DICT,
    'generalization': GENERALIZATION_PARAMETERS_DICT,
    'scientific_discovery': SCIENTIFIC_DISCOVERY_PARAMETERS_DICT,
    'astrophysics': ASTROPHYSICS_PARAMETERS_DICT
}

# Create a flat dictionary of all parameters
SUPPORTED_PARAMETERS = {}
for purpose, parameters in ALL_PURPOSE_PARAMETERS.items():
    SUPPORTED_PARAMETERS.update(parameters)

# Function to get equation-specific parameters
def get_equation_parameters(purpose, eq_id):
    """Get parameters for a specific equation in a specific purpose."""
    if purpose == 'forward_problems':
        return FORWARD_PROBLEMS_EQUATION_PARAMETERS.get(eq_id, {})
    elif purpose == 'inverse_problems':
        return INVERSE_PROBLEMS_EQUATION_PARAMETERS.get(eq_id, {})
    else:
        # For other purposes, return empty dict for now
        return {}

def get_purpose_equations(purpose):
    """Get all equations for a specific purpose."""
    if purpose == 'forward_problems':
        return list(FORWARD_PROBLEMS_EQUATION_PARAMETERS.keys())
    elif purpose == 'inverse_problems':
        return list(INVERSE_PROBLEMS_EQUATION_PARAMETERS.keys())
    else:
        # For other purposes, return empty list for now
        return []

ALL_PURPOSE_PARAMETERS['astrophysics'] = ASTROPHYSICS_PARAMETERS_DICT
SUPPORTED_PARAMETERS.update(ASTROPHYSICS_PARAMETERS_DICT) 