# PINN Research Platform - Backend Documentation

## 📋 Table of Contents

1. [Overview](#overview)
2. [Project Structure](#project-structure)
3. [Core Modules](#core-modules)
4. [PINN Purposes](#pinn-purposes)
5. [Getting Started](#getting-started)
6. [Usage Examples](#usage-examples)
7. [API Integration](#api-integration)
8. [Development Guidelines](#development-guidelines)
9. [Troubleshooting](#troubleshooting)

## 🎯 Overview

The backend of the PINN Research Platform provides a comprehensive framework for implementing Physics-Informed Neural Networks (PINNs) across various research applications. The architecture is designed to be modular, extensible, and research-driven.

### Key Features

- **Modular Design**: Each PINN purpose has its own module with trainer, evaluator, and models
- **Comprehensive Logging**: Purpose-specific logging with detailed training and evaluation tracking
- **Shared Utilities**: Common models, physics functions, and data generation utilities
- **Extensible Architecture**: Easy to add new purposes, equations, and model architectures
- **Research-Focused**: Organized by PINN applications rather than just equations

## 🏗️ Project Structure

```
physics-informed-neural-network/
├── utils/                          # Shared utilities
│   ├── __init__.py                # Module exports
│   ├── loggers.py                 # Enhanced logging system
│   ├── models.py                  # Shared PINN models
│   ├── physics.py                 # Physics functions and equations
│   └── data_generator.py          # Data generation utilities
│
├── forward_problems/              # Forward problem solving
│   ├── __init__.py
│   ├── trainer.py
│   ├── evaluator.py
│   └── models.py
│
├── inverse_problems/              # Inverse problem solving
├── data_assimilation/             # Data assimilation
├── control_optimization/          # Control optimization
├── uncertainty/                   # Uncertainty quantification
├── multiphysics/                  # Multi-physics problems
├── efficiency/                    # Computational efficiency
├── generalization/                # Generalization capabilities
├── scientific_discovery/          # Scientific discovery
├── sparse_data/                   # Sparse and noisy data
│
├── scripts/                       # Utility scripts
│   ├── generate_backend_structure.py
│   └── example_forward_problem.py
│
├── results/                       # Training results and outputs
├── logs/                          # Log files
└── data/                          # Generated and stored data
```

## 🔧 Core Modules

### 1. Logging System (`utils/loggers.py`)

**Purpose**: Comprehensive logging for PINN training and evaluation.

**Key Classes**:
- `LoggerFactory`: Creates and configures loggers with file and console output
- `PurposeLogger`: Purpose-specific logger for different PINN applications

**Usage**:
```python
from utils.loggers import get_purpose_logger, get_general_logger

# Purpose-specific logger
logger = get_purpose_logger("forward_problems", "heat")

# General logger
logger = get_general_logger("data_processing")
```

**Features**:
- Timestamped log files
- Purpose and equation-specific logging
- Training progress tracking
- Error handling and reporting
- Different log levels (DEBUG, INFO, WARNING, ERROR)

### 2. Models (`utils/models.py`)

**Purpose**: Shared PINN model architectures.

**Key Classes**:
- `MLP`: Multi-Layer Perceptron with customizable architecture
- `FourierFeatureMLP`: MLP with Fourier feature embedding

**Usage**:
```python
from utils.models import create_pinn_model, get_model_summary

# Create standard PINN
model = create_pinn_model(
    model_type="standard",
    input_dim=2,
    output_dim=1,
    hidden_dims=[50, 50, 50, 50],
    activation="tanh"
)

# Get model summary
summary = get_model_summary(model)
```

**Supported Model Types**:
- `standard`: Basic MLP
- `fourier`: Fourier feature MLP

### 3. Physics Functions (`utils/physics.py`)

**Purpose**: Physics-informed loss functions and differential equations.

**Key Classes**:
- `PhysicsFunctions`: Collection of physics residuals
- `BoundaryConditions`: Boundary condition implementations
- `InitialConditions`: Initial condition functions

**Supported Equations**:
- Heat equation: `u_t - α∇²u = 0`
- Wave equation: `u_tt - c²∇²u = 0`
- Burgers equation: `u_t + uu_x - νu_xx = 0`
- Advection equation: `u_t + cu_x = 0`
- Reaction-diffusion: `u_t - D∇²u + ku = 0`

**Usage**:
```python
from utils.physics import get_physics_function, get_boundary_condition

# Get physics function
physics_fn = get_physics_function("heat")

# Get boundary condition
bc_fn = get_boundary_condition("dirichlet")
```

### 4. Data Generator (`utils/data_generator.py`)

**Purpose**: Generate training and testing data for PINNs.

**Key Class**: `DataGenerator`

**Features**:
- Training data generation (interior, boundary, initial points)
- Test data generation
- Analytical solutions for comparison
- Data saving and loading

**Usage**:
```python
from utils.data_generator import DataGenerator

generator = DataGenerator()

# Generate training data
training_data = generator.generate_training_data(
    x_range=(0.0, 1.0),
    t_range=(0.0, 1.0),
    n_interior=1000,
    n_boundary=200,
    n_initial=200,
    equation_type="heat",
    alpha=1.0
)
```

## 🎯 PINN Purposes

The platform supports 10 different PINN purposes, each with its own module:

### 1. Forward Problems (`forward_problems/`)
**Purpose**: Solve differential equations with known parameters.
- **Trainer**: `ForwardProblemsTrainer`
- **Evaluator**: `ForwardProblemsEvaluator`
- **Models**: `ForwardProblemsPINN`

### 2. Inverse Problems (`inverse_problems/`)
**Purpose**: Infer unknown parameters from observed data.
- **Trainer**: `InverseProblemsTrainer`
- **Evaluator**: `InverseProblemsEvaluator`
- **Models**: `InverseProblemsPINN`

### 3. Data Assimilation (`data_assimilation/`)
**Purpose**: Combine model predictions with observational data.
- **Trainer**: `DataAssimilationTrainer`
- **Evaluator**: `DataAssimilationEvaluator`
- **Models**: `DataAssimilationPINN`

### 4. Control Optimization (`control_optimization/`)
**Purpose**: Find optimal control strategies.
- **Trainer**: `ControlOptimizationTrainer`
- **Evaluator**: `ControlOptimizationEvaluator`
- **Models**: `ControlOptimizationPINN`

### 5. Uncertainty (`uncertainty/`)
**Purpose**: Quantify and propagate uncertainties.
- **Trainer**: `UncertaintyTrainer`
- **Evaluator**: `UncertaintyEvaluator`
- **Models**: `UncertaintyPINN`

### 6. Multi-physics (`multiphysics/`)
**Purpose**: Solve coupled systems of differential equations.
- **Trainer**: `MultiphysicsTrainer`
- **Evaluator**: `MultiphysicsEvaluator`
- **Models**: `MultiphysicsPINN`

### 7. Efficiency (`efficiency/`)
**Purpose**: Optimize computational efficiency.
- **Trainer**: `EfficiencyTrainer`
- **Evaluator**: `EfficiencyEvaluator`
- **Models**: `EfficiencyPINN`

### 8. Generalization (`generalization/`)
**Purpose**: Study generalization capabilities.
- **Trainer**: `GeneralizationTrainer`
- **Evaluator**: `GeneralizationEvaluator`
- **Models**: `GeneralizationPINN`

### 9. Scientific Discovery (`scientific_discovery/`)
**Purpose**: Discover governing equations and physical laws.
- **Trainer**: `ScientificDiscoveryTrainer`
- **Evaluator**: `ScientificDiscoveryEvaluator`
- **Models**: `ScientificDiscoveryPINN`

### 10. Sparse Data (`sparse_data/`)
**Purpose**: Handle limited, irregular, or noisy data.
- **Trainer**: `SparseDataTrainer`
- **Evaluator**: `SparseDataEvaluator`
- **Models**: `SparseDataPINN`

## 🚀 Getting Started

### Prerequisites

```bash
# Install required packages
pip install torch numpy matplotlib scikit-learn seaborn
```

### Quick Start

1. **Run the example script**:
```bash
python scripts/example_forward_problem.py
```

2. **Check the results**:
- Logs: `logs/forward_problems/heat/`
- Results: `results/forward_problems/heat/`
- Visualizations: `results/forward_problems/heat/visualization.png`

### Basic Usage Pattern

```python
# 1. Import modules
from utils import get_purpose_logger, create_pinn_model, DataGenerator
from forward_problems import ForwardProblemsTrainer, ForwardProblemsEvaluator

# 2. Setup logging
logger = get_purpose_logger("forward_problems", "heat")

# 3. Create model
model = create_pinn_model(
    model_type="standard",
    input_dim=2,
    output_dim=1,
    hidden_dims=[50, 50, 50, 50],
    activation="tanh"
)

# 4. Generate data
generator = DataGenerator()
training_data = generator.generate_training_data(
    x_range=(0.0, 1.0),
    t_range=(0.0, 1.0),
    equation_type="heat"
)

# 5. Setup trainer
trainer = ForwardProblemsTrainer(model, "forward_problems", "heat")
trainer.setup_optimizer(learning_rate=0.001)

# 6. Train model
history = trainer.train(training_data, epochs=5000)

# 7. Evaluate model
evaluator = ForwardProblemsEvaluator(model, "forward_problems", "heat")
results = evaluator.evaluate_on_grid(x_grid, t_grid, u_true)
```

## 📊 Usage Examples

### Example 1: Heat Equation

```python
# Complete heat equation example
from scripts.example_forward_problem import main
main()
```

### Example 2: Custom Purpose Implementation

```python
# Create custom purpose-specific trainer
class CustomTrainer(ForwardProblemsTrainer):
    def train_step(self, train_data, physics_fn, weights):
        # Custom training logic
        pass

# Use custom trainer
trainer = CustomTrainer(model, "custom_purpose", "custom_equation")
```

### Example 3: Multiple Equations

```python
# Train on multiple equations
equations = ["heat", "wave", "burgers"]
for eq in equations:
    training_data = generator.generate_training_data(equation_type=eq)
    trainer = ForwardProblemsTrainer(model, "forward_problems", eq)
    history = trainer.train(training_data, epochs=5000)
```

## 🔌 API Integration

### FastAPI Integration

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from forward_problems import ForwardProblemsTrainer

app = FastAPI()

class TrainingRequest(BaseModel):
    equation_type: str
    epochs: int
    learning_rate: float

@app.post("/train")
async def train_pinn(request: TrainingRequest):
    try:
        # Setup training
        model = create_pinn_model(model_type="standard")
        trainer = ForwardProblemsTrainer(model, "forward_problems", request.equation_type)
        
        # Generate data and train
        training_data = generator.generate_training_data(equation_type=request.equation_type)
        history = trainer.train(training_data, epochs=request.epochs)
        
        return {"status": "success", "final_loss": history['total_loss'][-1]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

### WebSocket Integration

```python
from fastapi import WebSocket
import json

@app.websocket("/training-progress")
async def training_progress(websocket: WebSocket):
    await websocket.accept()
    
    # Send training progress updates
    for epoch in range(epochs):
        loss = trainer.train_step(...)
        await websocket.send_text(json.dumps({
            "epoch": epoch,
            "loss": loss
        }))
```

## 🛠️ Development Guidelines

### Adding New Purposes

1. **Create purpose directory**:
```bash
mkdir new_purpose
```

2. **Generate structure**:
```bash
python scripts/generate_backend_structure.py
```

3. **Customize implementation**:
- Modify `trainer.py` for purpose-specific training logic
- Update `evaluator.py` for specialized evaluation metrics
- Customize `models.py` for purpose-specific architectures

### Adding New Equations

1. **Add physics function** in `utils/physics.py`:
```python
@staticmethod
def new_equation_residual(x, t, u, **params):
    # Implement physics residual
    return residual
```

2. **Update physics function registry**:
```python
physics_functions = {
    'new_equation': PhysicsFunctions.new_equation_residual,
    # ... existing equations
}
```

3. **Add analytical solution** in `utils/data_generator.py`:
```python
def generate_analytical_solution(self, x, t, equation_type="new_equation"):
    if equation_type.lower() == "new_equation":
        # Implement analytical solution
        return u_analytical
```

### Code Style Guidelines

- **Type Hints**: Use type hints for all function parameters and return values
- **Docstrings**: Include comprehensive docstrings for all classes and methods
- **Logging**: Use appropriate logging levels and include context
- **Error Handling**: Implement proper exception handling with meaningful messages
- **Testing**: Write unit tests for critical functions

### File Naming Conventions

- **Modules**: snake_case (e.g., `data_generator.py`)
- **Classes**: PascalCase (e.g., `DataGenerator`)
- **Functions**: snake_case (e.g., `generate_training_data`)
- **Constants**: UPPER_SNAKE_CASE (e.g., `DEFAULT_LEARNING_RATE`)

## 🔍 Troubleshooting

### Common Issues

1. **Import Errors**:
```bash
# Ensure you're in the correct directory
cd physics-informed-neural-network

# Check Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

2. **CUDA/GPU Issues**:
```python
# Check if CUDA is available
import torch
print(f"CUDA available: {torch.cuda.is_available()}")

# Force CPU if needed
device = torch.device('cpu')
model = model.to(device)
```

3. **Memory Issues**:
```python
# Reduce batch size or model size
model = create_pinn_model(hidden_dims=[30, 30, 30])  # Smaller model
training_data = generator.generate_training_data(n_interior=500)  # Fewer points
```

4. **Training Convergence**:
```python
# Adjust learning rate
trainer.setup_optimizer(learning_rate=0.0001)  # Lower learning rate

# Use different optimizer
trainer.setup_optimizer(optimizer_type="adamw")

# Adjust loss weights
weights = {'physics': 10.0, 'boundary': 1.0, 'initial': 1.0}
```

### Debug Mode

```python
# Enable debug logging
logger = get_purpose_logger("forward_problems", "heat")
logger.logger.setLevel(logging.DEBUG)

# Check gradients
for name, param in model.named_parameters():
    if param.grad is not None:
        print(f"{name}: grad_norm = {param.grad.norm()}")
```

### Performance Optimization

1. **Use GPU acceleration**:
```python
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)
```

2. **Enable mixed precision**:
```python
from torch.cuda.amp import autocast, GradScaler

scaler = GradScaler()
with autocast():
    loss = model(inputs)
```

3. **Optimize data loading**:
```python
# Use DataLoader for large datasets
from torch.utils.data import DataLoader, TensorDataset

dataset = TensorDataset(x, t, u)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)
```

## 📚 Additional Resources

### Documentation
- [PyTorch Documentation](https://pytorch.org/docs/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [PINN Literature](https://www.sciencedirect.com/science/article/pii/S0021999118307125)

### Research Papers
- Raissi, M., Perdikaris, P., & Karniadakis, G. E. (2019). Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations.
- Lu, L., Meng, X., Mao, Z., & Karniadakis, G. E. (2021). DeepXDE: A deep learning library for solving differential equations.

### Community
- [PINN Research Community](https://github.com/maziarraissi/PINNs)
- [DeepXDE Library](https://github.com/lululxvi/deepxde)

---

**Note**: This documentation is a living document. Please update it as you add new features or make changes to the backend structure. 