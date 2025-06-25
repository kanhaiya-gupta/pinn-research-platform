"""
ControlOptimization Module for PINN Research Platform.

Control optimization using PINNs. Find optimal control strategies for dynamical systems governed by differential equations.
"""

from .trainer import ControlOptimizationTrainer
from .evaluator import ControlOptimizationEvaluator
from .models import ControlOptimizationPINN

__all__ = [
    'ControlOptimizationTrainer',
    'ControlOptimizationEvaluator', 
    'ControlOptimizationPINN'
]
