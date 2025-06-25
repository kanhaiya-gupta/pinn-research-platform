"""
ForwardProblems Module for PINN Research Platform.

Forward problem solving using PINNs. Solve differential equations with known parameters, initial conditions, and boundary conditions to predict solutions.
"""

from .trainer import ForwardProblemsTrainer
from .evaluator import ForwardProblemsEvaluator
from .models import ForwardProblemsPINN

__all__ = [
    'ForwardProblemsTrainer',
    'ForwardProblemsEvaluator', 
    'ForwardProblemsPINN'
]
