"""
SparseData Module for PINN Research Platform.

PINNs for sparse and noisy data. Handle limited, irregular, or noisy observational data in PINN training.
"""

from .trainer import SparseDataTrainer
from .evaluator import SparseDataEvaluator
from .models import SparseDataPINN

__all__ = [
    'SparseDataTrainer',
    'SparseDataEvaluator', 
    'SparseDataPINN'
]
