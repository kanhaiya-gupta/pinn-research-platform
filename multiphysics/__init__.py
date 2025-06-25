"""
Multiphysics Module for PINN Research Platform.

Multi-physics problems using PINNs. Solve coupled systems of differential equations representing multiple physical phenomena.
"""

from .trainer import MultiphysicsTrainer
from .evaluator import MultiphysicsEvaluator
from .models import MultiphysicsPINN

__all__ = [
    'MultiphysicsTrainer',
    'MultiphysicsEvaluator', 
    'MultiphysicsPINN'
]
