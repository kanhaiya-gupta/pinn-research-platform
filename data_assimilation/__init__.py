"""
DataAssimilation Module for PINN Research Platform.

Data assimilation using PINNs. Combine model predictions with observational data to improve state estimation and forecasting.
"""

from .trainer import DataAssimilationTrainer
from .evaluator import DataAssimilationEvaluator
from .models import DataAssimilationPINN

__all__ = [
    'DataAssimilationTrainer',
    'DataAssimilationEvaluator', 
    'DataAssimilationPINN'
]
