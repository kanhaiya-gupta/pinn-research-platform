
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from enum import Enum

class SamplingMethod(str, Enum):
    UNIFORM = "uniform"
    RANDOM = "random"
    LATIN_HYPERCUBE = "latin_hypercube"
    SOBOL = "sobol"
    ADAPTIVE = "adaptive"

class BoundaryConditionType(str, Enum):
    DIRICHLET = "dirichlet"
    NEUMANN = "neumann"
    PERIODIC = "periodic"
    MIXED = "mixed"

class InitialConditionType(str, Enum):
    SINUSOIDAL = "sinusoidal"
    GAUSSIAN = "gaussian"
    STEP = "step"
    CUSTOM = "custom"

class ComprehensiveTrainingRequest(BaseModel):
    """Comprehensive training request with all PINN parameters."""
    
    # Neural Network Architecture
    hidden_layers: int = Field(default=4, ge=2, le=10, description="Number of hidden layers")
    neurons_per_layer: int = Field(default=20, ge=10, le=100, description="Neurons per layer")
    hidden_activation: str = Field(default="tanh", description="Hidden layer activation")
    output_activation: str = Field(default="linear", description="Output layer activation")
    optimizer: str = Field(default="adam_lbfgs", description="Optimization algorithm")
    weight_init: str = Field(default="xavier", description="Weight initialization method")
    dropout_rate: float = Field(default=0.0, ge=0.0, le=0.5, description="Dropout rate")
    
    # Training Parameters
    learning_rate: float = Field(default=0.001, ge=0.0001, le=0.1, description="Learning rate")
    epochs: int = Field(default=10000, ge=1000, le=100000, description="Training epochs")
    learning_rate_scheduler: str = Field(default="constant", description="LR scheduler")
    scheduler_step_size: Optional[int] = Field(default=1000, description="Scheduler step size")
    scheduler_gamma: Optional[float] = Field(default=0.9, description="Scheduler gamma")
    gradient_clipping: Optional[float] = Field(default=None, ge=0.1, le=10.0, description="Gradient clipping")
    early_stopping_patience: int = Field(default=1000, ge=100, le=5000, description="Early stopping patience")
    
    # Loss Weights
    physics_weight: float = Field(default=1.0, ge=0.1, le=10.0, description="Physics loss weight")
    boundary_weight: float = Field(default=1.0, ge=0.1, le=10.0, description="Boundary loss weight")
    initial_weight: float = Field(default=1.0, ge=0.1, le=10.0, description="Initial condition weight")
    data_weight: Optional[float] = Field(default=1.0, ge=0.1, le=10.0, description="Data loss weight")
    
    # Sampling Parameters
    n_interior_points: int = Field(default=1000, ge=100, le=10000, description="Interior collocation points")
    n_boundary_points: int = Field(default=200, ge=50, le=2000, description="Boundary points")
    n_initial_points: int = Field(default=200, ge=50, le=2000, description="Initial condition points")
    n_data_points: Optional[int] = Field(default=100, ge=10, le=1000, description="Observational data points")
    
    # Time Domain Parameters
    time_duration: float = Field(default=1.0, ge=0.1, le=10.0, description="Time duration")
    time_points: int = Field(default=100, ge=20, le=500, description="Time sampling points")
    
    # Boundary and Initial Conditions
    initial_condition: InitialConditionType = Field(default=InitialConditionType.SINUSOIDAL, description="Initial condition type")
    boundary_condition: BoundaryConditionType = Field(default=BoundaryConditionType.DIRICHLET, description="Boundary condition type")
    left_boundary_value: float = Field(default=0.0, description="Left boundary value")
    right_boundary_value: float = Field(default=0.0, description="Right boundary value")
    
    # Sampling Strategy
    sampling_method: SamplingMethod = Field(default=SamplingMethod.UNIFORM, description="Sampling method")
    adaptive_sampling: bool = Field(default=False, description="Enable adaptive sampling")
    
    # Validation and Testing
    validation_split: float = Field(default=0.2, ge=0.05, le=0.5, description="Validation split")
    test_points: int = Field(default=500, ge=100, le=2000, description="Test points")
    error_metrics: List[str] = Field(default=["l2_norm", "relative_error"], description="Error metrics")
    
    # Advanced Configuration
    random_seed: Optional[int] = Field(default=42, ge=0, le=999999, description="Random seed")
    checkpoint_frequency: int = Field(default=1000, ge=100, le=10000, description="Checkpoint frequency")
    pde_residual_scaling: str = Field(default="none", description="PDE residual scaling")
    multi_fidelity: bool = Field(default=False, description="Multi-fidelity training")
    
    # Observational Data (for inverse problems)
    noise_level: Optional[float] = Field(default=0.0, ge=0.0, le=1.0, description="Noise level")
    
    # Equation-specific parameters
    equation_params: Dict[str, Any] = Field(default_factory=dict, description="Equation-specific parameters")
