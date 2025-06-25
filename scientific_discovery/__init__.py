"""
ScientificDiscovery Module for PINN Research Platform.

Scientific discovery using PINNs. Discover governing equations, physical laws, and hidden patterns from data.
"""

from .trainer import ScientificDiscoveryTrainer
from .evaluator import ScientificDiscoveryEvaluator
from .models import ScientificDiscoveryPINN

__all__ = [
    'ScientificDiscoveryTrainer',
    'ScientificDiscoveryEvaluator', 
    'ScientificDiscoveryPINN'
]
