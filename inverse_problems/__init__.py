"""
InverseProblems Module for PINN Research Platform.

Inverse problem solving using PINNs. Infer unknown parameters, initial conditions, or boundary conditions from observed data.
"""

from .trainer import InverseProblemsTrainer
from .evaluator import InverseProblemsEvaluator
from .models import InverseProblemsPINN

__all__ = [
    'InverseProblemsTrainer',
    'InverseProblemsEvaluator', 
    'InverseProblemsPINN'
]
