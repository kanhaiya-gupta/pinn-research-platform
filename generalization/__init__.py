"""
Generalization Module for PINN Research Platform.

Generalization capabilities of PINNs. Study how well PINNs generalize to unseen parameter regimes, geometries, and conditions.
"""

from .trainer import GeneralizationTrainer
from .evaluator import GeneralizationEvaluator
from .models import GeneralizationPINN

__all__ = [
    'GeneralizationTrainer',
    'GeneralizationEvaluator', 
    'GeneralizationPINN'
]
