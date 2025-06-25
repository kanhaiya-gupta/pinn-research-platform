"""
Efficiency Module for PINN Research Platform.

Computational efficiency improvements for PINNs. Optimize training strategies, network architectures, and numerical methods.
"""

from .trainer import EfficiencyTrainer
from .evaluator import EfficiencyEvaluator
from .models import EfficiencyPINN

__all__ = [
    'EfficiencyTrainer',
    'EfficiencyEvaluator', 
    'EfficiencyPINN'
]
