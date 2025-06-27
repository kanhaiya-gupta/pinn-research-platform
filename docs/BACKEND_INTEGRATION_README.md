# Backend Integration and Parameter Flow Guide

## Overview

This document provides a comprehensive guide to understanding how parameters flow from the frontend to the backend in the Physics-Informed Neural Network (PINN) research platform. It covers the complete data pipeline, parameter mapping, and how to access and use training parameters in your backend code.

## Table of Contents

1. [Parameter Flow Overview](#parameter-flow-overview)
2. [Frontend Parameter Collection](#frontend-parameter-collection)
3. [JavaScript Form Processing](#javascript-form-processing)
4. [Frontend API Endpoints](#frontend-api-endpoints)
5. [Parameter Mapping and Conversion](#parameter-mapping-and-conversion)
6. [Backend API Reception](#backend-api-reception)
7. [Purpose-Specific Training](#purpose-specific-training)
8. [Accessing Parameters in Backend Code](#accessing-parameters-in-backend-code)
9. [Parameter Sources and Hierarchy](#parameter-sources-and-hierarchy)
10. [Complete Examples](#complete-examples)
11. [Troubleshooting](#troubleshooting)

## Parameter Flow Overview

The parameter flow follows this sequence:

```
Frontend Form → JavaScript Processing → Frontend API → Parameter Mapping → Backend API → Training Execution
```

### Architecture Components

- **Frontend**: `webapp/templates/{purpose}/simulation.html`
- **JavaScript**: `webapp/static/js/simulation.js` and `webapp/static/js/main.js`
- **Frontend API**: `webapp/app.py`
- **Backend API**: `main.py`
- **Purpose-Specific Trainers**: `{purpose}/trainer.py`

## Frontend Parameter Collection

### Form Structure

Parameters are collected through HTML forms in the simulation templates:

```html
<!-- Neural Network Architecture -->
<div class="config-section">
    <h3>Neural Network Architecture</h3>
    <div class="form-row">
        <div class="form-group">
            <label for="hidden_layers">Hidden Layers</label>
            <input type="number" id="hidden_layers" name="hidden_layers" 
                   value="4" min="2" max="10" required>
        </div>
        <div class="form-group">
            <label for="neurons_per_layer">Neurons per Layer</label>
            <input type="number" id="neurons_per_layer" name="neurons_per_layer" 
                   value="20" min="10" max="100" required>
        </div>
    </div>
</div>

<!-- Training Parameters -->
<div class="config-section">
    <h3>Training Parameters</h3>
    <div class="form-row">
        <div class="form-group">
            <label for="learning_rate">Learning Rate</label>
            <input type="number" id="learning_rate" name="learning_rate" 
                   value="0.001" step="0.0001" min="0.0001" max="0.1" required>
        </div>
        <div class="form-group">
            <label for="epochs">Training Epochs</label>
            <input type="number" id="epochs" name="epochs" 
                   value="10000" min="1000" max="100000" required>
        </div>
    </div>
</div>

<!-- Equation-Specific Parameters (Dynamically Loaded) -->
<div class="config-section">
    <h3>Equation Parameters</h3>
    <div class="form-row">
        <div class="form-group">
            <label for="thermal_diffusivity">Thermal Diffusivity (α)</label>
            <input type="number" id="thermal_diffusivity" name="thermal_diffusivity" 
                   value="1.0" step="0.1" min="0.01" max="10.0">
        </div>
    </div>
</div>
```

### Dynamic Parameter Loading

Equation-specific parameters are dynamically loaded from the backend configuration:

```python
# In webapp/app.py
def get_equation_specific_parameters(purpose_name: str, eq_id: str) -> Dict[str, Any]:
    """Get equation-specific parameters for a given purpose and equation."""
    if purpose_name == 'forward_problems':
        from config.parameters.forward_problems import FORWARD_PROBLEMS_EQUATION_PARAMETERS
        return FORWARD_PROBLEMS_EQUATION_PARAMETERS.get(eq_id, {})
    # ... other purposes
```

## JavaScript Form Processing

### Form Submission Handler

```javascript
// In webapp/static/js/simulation.js
document.getElementById('simulation-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    // Collect all form data
    const formData = new FormData(e.target);
    const parameters = {};
    
    for (let [key, value] of formData.entries()) {
        // Convert string values to appropriate types
        if (value === 'true') parameters[key] = true;
        else if (value === 'false') parameters[key] = false;
        else if (!isNaN(value) && value !== '') parameters[key] = Number(value);
        else parameters[key] = value;
    }
    
    // Add purpose and equation context
    parameters.purpose = purposeKey;
    parameters.equation_id = equationType;
    
    // Validate parameters
    const errors = validateParameters(parameters, equationType);
    if (errors.length > 0) {
        showNotification('Validation errors: ' + errors.join(', '), 'error');
        return;
    }
    
    // Send to backend
    try {
        const result = await PINNUtils.simulateEquation(equationType, parameters);
        showNotification('Training started successfully!', 'success');
    } catch (error) {
        showNotification('Training failed: ' + error.message, 'error');
    }
});
```

### API Call Function

```javascript
// In webapp/static/js/main.js
async function simulateEquation(equationType, parameters) {
    try {
        const response = await fetch(`/api/simulate/${equationType}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(parameters)
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        return await response.json();
    } catch (error) {
        console.error('Simulation error:', error);
        throw error;
    }
}
```

## Frontend API Endpoints

### Purpose-Based Simulation Endpoint

```python
# In webapp/app.py
@app.post("/api/simulate/{purpose_name}/{eq_id}")
async def simulate_purpose_equation(purpose_name: str, eq_id: str, request: Request):
    """Submit training request to main.py backend for purpose-based equations"""
    purpose_info = config.get_purpose_info(purpose_name)
    if not purpose_info:
        raise HTTPException(status_code=404, detail="Purpose not found")
    
    equations = config.get_equations_by_purpose(purpose_name)
    if eq_id not in equations:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    try:
        body = await request.json()
        
        # Map frontend parameters to backend format
        backend_params = map_parameters_to_backend(purpose_name, eq_id, body)
        
        async with httpx.AsyncClient() as client:
            # Call the main.py backend API
            response = await client.post(
                f"{config.API_BASE_URL}/api/{purpose_name}/{eq_id}/train",
                json=backend_params,
                timeout=300.0  # 5 minutes timeout for training
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                raise HTTPException(status_code=response.status_code, 
                                  detail=f"Backend error: {response.text}")
                
    except httpx.TimeoutException:
        raise HTTPException(status_code=408, detail="Training timeout")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Training failed: {str(e)}")
```

## Parameter Mapping and Conversion

### Parameter Mapping Function

```python
# In webapp/app.py
def map_parameters_to_backend(purpose_name: str, eq_id: str, frontend_params: dict) -> dict:
    """Map frontend parameters to backend API format for purpose-based equations"""
    params = {}
    
    # Convert string values to appropriate types
    for key, value in frontend_params.items():
        if isinstance(value, str):
            try:
                params[key] = float(value) if '.' in value else int(value)
            except ValueError:
                params[key] = value
        else:
            params[key] = value
    
    # Add purpose and equation information
    params['purpose'] = purpose_name
    params['equation_id'] = eq_id
    
    # Add default training parameters if not provided
    training_params = config.get_training_parameters()
    for key, default_value in training_params.items():
        if key not in params:
            params[key] = default_value
    
    return params
```

### Type Conversion Examples

```python
# String to number conversion
"4" → 4 (integer)
"20" → 20 (integer)
"0.001" → 0.001 (float)
"1.0" → 1.0 (float)

# Boolean conversion
"true" → True
"false" → False

# Preserve strings
"tanh" → "tanh"
"adam" → "adam"
```

## Backend API Reception

### Training Request Model

```python
# In main.py
class TrainingRequest(BaseModel):
    equation_type: str
    purpose: str = "forward_problems"
    
    # Neural Network Architecture
    hidden_layers: int = 4
    neurons_per_layer: int = 20
    hidden_activation: str = "tanh"
    output_activation: str = "linear"
    
    # Training Parameters
    learning_rate: float = 0.001
    epochs: int = 10000
    optimizer: str = "adam"
    
    # Advanced Training Parameters
    batch_size: Optional[int] = None
    learning_rate_scheduler: str = "constant"
    scheduler_step_size: Optional[int] = 1000
    scheduler_gamma: Optional[float] = 0.9
    
    # Loss Weights (PINN-specific)
    physics_weight: float = 1.0
    boundary_weight: float = 1.0
    initial_weight: float = 1.0
    data_weight: float = 1.0
    
    # Sampling Strategy
    n_interior_points: int = 1000
    n_boundary_points: int = 200
    n_initial_points: int = 200
    n_data_points: Optional[int] = None
    
    # Weight Initialization
    weight_init: str = "xavier"
    
    # Equation-specific parameters
    thermal_diffusivity: Optional[float] = 1.0
    wave_speed: Optional[float] = 1.0
    viscosity: Optional[float] = 0.01
    frequency: Optional[float] = 1.0
    amplitude: Optional[float] = 1.0
```

### Training Endpoint

```python
# In main.py
@app.post("/api/train")
async def train_pinn(request: TrainingRequest):
    """Train a PINN model"""
    try:
        logger = get_purpose_logger(request.purpose, request.equation_type)
        logger.log_purpose_specific_info(f"Starting training for {request.equation_type}")
        
        # Create model using parameters
        hidden_dims = [request.neurons_per_layer] * request.hidden_layers
        model = create_pinn_model(
            model_type="standard",
            input_dim=2,
            output_dim=1,
            hidden_dims=hidden_dims,
            activation=request.hidden_activation,
            output_activation=request.output_activation
        )
        
        # Generate training data with equation-specific parameters
        generator = DataGenerator()
        training_data = generator.generate_training_data(
            x_range=(0.0, 1.0),
            t_range=(0.0, 1.0),
            n_interior=request.n_interior_points,
            n_boundary=request.n_boundary_points,
            n_initial=request.n_initial_points,
            equation_type=request.equation_type,
            alpha=request.thermal_diffusivity,  # For heat equation
            c=request.wave_speed,               # For wave equation
            nu=request.viscosity                # For Burgers equation
        )
        
        # Setup trainer with parameters
        trainer = ForwardProblemsTrainer(model, request.purpose, request.equation_type)
        trainer.setup_optimizer(learning_rate=request.learning_rate, optimizer_type=request.optimizer)
        
        # Train model
        history = trainer.train(
            train_data=training_data,
            physics_fn=training_data['physics_fn'],
            epochs=request.epochs,
            weights={
                'physics': request.physics_weight,
                'boundary': request.boundary_weight,
                'initial': request.initial_weight,
                'data': request.data_weight
            }
        )
        
        return {
            "status": "success",
            "message": "Training completed successfully",
            "final_loss": history['total_loss'][-1],
            "model_key": f"{request.purpose}_{request.equation_type}"
        }
        
    except Exception as e:
        logger = get_purpose_logger(request.purpose, request.equation_type)
        logger.log_error(e, "Training failed")
        raise HTTPException(status_code=500, detail=f"Training failed: {str(e)}")
```

## Purpose-Specific Training

### Trainer Class Structure

```python
# In forward_problems/trainer.py
class ForwardProblemsTrainer:
    """Trainer class for forward problems using PINNs."""

    def __init__(self, model: nn.Module, purpose: str, equation: str):
        self.model = model
        self.purpose = purpose
        self.equation = equation
        self.logger = get_purpose_logger(purpose, equation)
        
        # Training state
        self.optimizer = None
        self.scheduler = None
        self.training_history = {
            'physics_loss': [],
            'boundary_loss': [],
            'initial_loss': [],
            'total_loss': [],
            'epochs': []
        }

    def setup_optimizer(self, learning_rate: float = 0.001, optimizer_type: str = "adam"):
        """Setup optimizer for training."""
        if optimizer_type.lower() == "adam":
            self.optimizer = optim.Adam(self.model.parameters(), lr=learning_rate)
        elif optimizer_type.lower() == "sgd":
            self.optimizer = optim.SGD(self.model.parameters(), lr=learning_rate)
        # ... other optimizers

    def train(self, train_data: Dict[str, torch.Tensor], 
              physics_fn: Callable, epochs: int = 10000,
              weights: Optional[Dict[str, float]] = None):
        """Train the PINN model."""
        if weights is None:
            weights = {'physics': 1.0, 'boundary': 1.0, 'initial': 1.0}
        
        for epoch in range(epochs):
            losses = self.train_step(train_data, physics_fn, weights)
            
            # Store history
            for key, value in losses.items():
                self.training_history[key].append(value)
            self.training_history['epochs'].append(epoch)
            
            # Log progress
            if epoch % 100 == 0:
                self.logger.log_training_progress(
                    epoch, epochs, losses.get('physics_loss', 0.0), losses['total_loss']
                )
        
        return self.training_history
```

## Accessing Parameters in Backend Code

### 1. In main.py Training Endpoint

```python
@app.post("/api/train")
async def train_pinn(request: TrainingRequest):
    # Access all parameters directly from request object
    print(f"Hidden layers: {request.hidden_layers}")
    print(f"Neurons per layer: {request.neurons_per_layer}")
    print(f"Learning rate: {request.learning_rate}")
    print(f"Epochs: {request.epochs}")
    print(f"Optimizer: {request.optimizer}")
    
    # Access equation-specific parameters
    print(f"Thermal diffusivity: {request.thermal_diffusivity}")
    print(f"Wave speed: {request.wave_speed}")
    print(f"Viscosity: {request.viscosity}")
    
    # Use parameters in model creation
    hidden_dims = [request.neurons_per_layer] * request.hidden_layers
    model = create_pinn_model(
        hidden_dims=hidden_dims,
        activation=request.hidden_activation,
        output_activation=request.output_activation
    )
```

### 2. In Purpose-Specific Trainers

```python
def train(self, train_data, physics_fn, epochs, weights=None):
    # Parameters are passed as function arguments
    print(f"Training for {epochs} epochs")
    print(f"Loss weights: {weights}")
    
    for epoch in range(epochs):
        # Use the parameters here
        losses = self.train_step(train_data, physics_fn, weights)
```

### 3. In Equation-Specific Modules

```python
# Access parameters from configuration
from config.parameters.forward_problems import FORWARD_PROBLEMS_PARAMETERS_DICT

def get_parameter_value(param_name):
    """Get parameter value from configuration."""
    if param_name in FORWARD_PROBLEMS_PARAMETERS_DICT:
        return FORWARD_PROBLEMS_PARAMETERS_DICT[param_name]['default']
    return None

def get_parameter_range(param_name):
    """Get parameter range from configuration."""
    if param_name in FORWARD_PROBLEMS_PARAMETERS_DICT:
        return FORWARD_PROBLEMS_PARAMETERS_DICT[param_name]['range']
    return None
```

### 4. In Data Generation

```python
# In utils/data_generator.py
class DataGenerator:
    def generate_training_data(self, equation_type: str, **kwargs):
        """Generate training data with equation-specific parameters."""
        
        if equation_type == "heat":
            alpha = kwargs.get('alpha', 1.0)
            # Use thermal diffusivity in heat equation
            return self._generate_heat_data(alpha)
            
        elif equation_type == "wave":
            c = kwargs.get('c', 1.0)
            # Use wave speed in wave equation
            return self._generate_wave_data(c)
            
        elif equation_type == "burgers":
            nu = kwargs.get('nu', 0.01)
            # Use viscosity in Burgers equation
            return self._generate_burgers_data(nu)
```

## Parameter Sources and Hierarchy

### Parameter Hierarchy (Highest to Lowest Priority)

1. **User Input**: Values entered in frontend forms
2. **Equation-Specific Defaults**: From `config/parameters/{purpose}.py`
3. **Purpose-Specific Defaults**: From training recommendations
4. **System Defaults**: Hardcoded fallbacks in backend models

### Parameter Sources

```python
# 1. User Input (Frontend Form)
user_params = {
    "hidden_layers": 6,           # User specified
    "learning_rate": 0.0005,      # User specified
    "thermal_diffusivity": 2.0    # User specified
}

# 2. Equation-Specific Defaults (config/parameters/forward_problems.py)
equation_params = {
    "thermal_diffusivity": {
        "name": "Thermal Diffusivity (α)",
        "description": "Thermal diffusivity coefficient",
        "unit": "m²/s",
        "default": 1.0,           # Default value
        "range": [0.01, 10.0]     # Valid range
    }
}

# 3. Purpose-Specific Defaults (config/config.py)
purpose_params = {
    "forward_problems": {
        "learning_rate": 0.001,
        "optimizer": "adam",
        "epochs": 10000
    }
}

# 4. System Defaults (main.py TrainingRequest)
system_params = {
    "hidden_layers": 4,
    "neurons_per_layer": 20,
    "hidden_activation": "tanh"
}
```

## Complete Examples

### Example 1: Heat Equation Training

**Frontend Form Data:**
```javascript
{
    "hidden_layers": 4,
    "neurons_per_layer": 20,
    "learning_rate": 0.001,
    "epochs": 10000,
    "thermal_diffusivity": 1.5,
    "purpose": "forward_problems",
    "equation_id": "heat"
}
```

**Frontend API Processing:**
```python
# webapp/app.py
backend_params = map_parameters_to_backend("forward_problems", "heat", form_data)
# Result:
{
    "hidden_layers": 4,
    "neurons_per_layer": 20,
    "learning_rate": 0.001,
    "epochs": 10000,
    "thermal_diffusivity": 1.5,
    "purpose": "forward_problems",
    "equation_type": "heat"
}
```

**Backend Training:**
```python
# main.py
@app.post("/api/train")
async def train_pinn(request: TrainingRequest):
    # Create model
    hidden_dims = [request.neurons_per_layer] * request.hidden_layers  # [20, 20, 20, 20]
    model = create_pinn_model(
        hidden_dims=hidden_dims,
        activation=request.hidden_activation,  # "tanh"
        output_activation=request.output_activation  # "linear"
    )
    
    # Generate data with thermal diffusivity
    training_data = generator.generate_training_data(
        equation_type=request.equation_type,  # "heat"
        alpha=request.thermal_diffusivity,    # 1.5
        n_interior=request.n_interior_points, # 1000
        n_boundary=request.n_boundary_points  # 200
    )
    
    # Train model
    trainer = ForwardProblemsTrainer(model, request.purpose, request.equation_type)
    trainer.setup_optimizer(learning_rate=request.learning_rate, optimizer_type=request.optimizer)
    history = trainer.train(
        train_data=training_data,
        physics_fn=training_data['physics_fn'],
        epochs=request.epochs  # 10000
    )
```

### Example 2: Burgers Equation with Custom Parameters

**Frontend Form Data:**
```javascript
{
    "hidden_layers": 6,
    "neurons_per_layer": 30,
    "learning_rate": 0.0005,
    "epochs": 15000,
    "viscosity": 0.005,
    "optimizer": "adam_lbfgs",
    "physics_weight": 2.0,
    "boundary_weight": 1.0,
    "purpose": "forward_problems",
    "equation_id": "burgers"
}
```

**Backend Processing:**
```python
# main.py
@app.post("/api/train")
async def train_pinn(request: TrainingRequest):
    # Model with 6 layers of 30 neurons each
    hidden_dims = [30] * 6  # [30, 30, 30, 30, 30, 30]
    model = create_pinn_model(hidden_dims=hidden_dims)
    
    # Data with custom viscosity
    training_data = generator.generate_training_data(
        equation_type="burgers",
        nu=request.viscosity,  # 0.005
        n_interior=request.n_interior_points
    )
    
    # Training with custom weights
    trainer = ForwardProblemsTrainer(model, request.purpose, request.equation_type)
    trainer.setup_optimizer(learning_rate=request.learning_rate, optimizer_type=request.optimizer)
    history = trainer.train(
        train_data=training_data,
        physics_fn=training_data['physics_fn'],
        epochs=request.epochs,  # 15000
        weights={
            'physics': request.physics_weight,    # 2.0
            'boundary': request.boundary_weight,  # 1.0
            'initial': request.initial_weight     # 1.0 (default)
        }
    )
```

## Troubleshooting

### Common Issues and Solutions

#### 1. Parameter Type Conversion Errors

**Problem:** String values not converting to numbers properly.

**Solution:** Check the parameter mapping function:

```python
def map_parameters_to_backend(purpose_name: str, eq_id: str, frontend_params: dict) -> dict:
    params = {}
    for key, value in frontend_params.items():
        if isinstance(value, str):
            try:
                # Handle boolean values first
                if value.lower() in ['true', 'false']:
                    params[key] = value.lower() == 'true'
                # Then handle numbers
                elif '.' in value:
                    params[key] = float(value)
                else:
                    params[key] = int(value)
            except ValueError:
                params[key] = value  # Keep as string
        else:
            params[key] = value
    return params
```

#### 2. Missing Parameters

**Problem:** Required parameters not being passed to backend.

**Solution:** Add parameter validation:

```python
def validate_required_parameters(params: dict, equation_type: str) -> List[str]:
    errors = []
    
    # Common required parameters
    required_common = ['hidden_layers', 'neurons_per_layer', 'learning_rate', 'epochs']
    for param in required_common:
        if param not in params or params[param] is None:
            errors.append(f"Missing required parameter: {param}")
    
    # Equation-specific required parameters
    if equation_type == "heat" and "thermal_diffusivity" not in params:
        errors.append("Missing thermal_diffusivity for heat equation")
    elif equation_type == "wave" and "wave_speed" not in params:
        errors.append("Missing wave_speed for wave equation")
    elif equation_type == "burgers" and "viscosity" not in params:
        errors.append("Missing viscosity for Burgers equation")
    
    return errors
```

#### 3. Parameter Range Validation

**Problem:** Parameters outside valid ranges causing training issues.

**Solution:** Add range validation:

```python
def validate_parameter_ranges(params: dict) -> List[str]:
    errors = []
    
    # Learning rate validation
    if 'learning_rate' in params:
        lr = params['learning_rate']
        if lr <= 0 or lr > 0.1:
            errors.append("Learning rate must be between 0 and 0.1")
    
    # Hidden layers validation
    if 'hidden_layers' in params:
        hl = params['hidden_layers']
        if hl < 2 or hl > 10:
            errors.append("Hidden layers must be between 2 and 10")
    
    # Epochs validation
    if 'epochs' in params:
        epochs = params['epochs']
        if epochs < 1000 or epochs > 100000:
            errors.append("Epochs must be between 1000 and 100000")
    
    return errors
```

#### 4. Backend Connection Issues

**Problem:** Frontend cannot connect to backend API.

**Solution:** Check configuration and network:

```python
# In webapp/config/config.py
class Config:
    def __init__(self):
        self.API_BASE_URL = "http://localhost:8000"  # Backend URL
        
    def get_api_url(self, endpoint: str) -> str:
        """Get full API URL for backend endpoint."""
        return f"{self.API_BASE_URL}{endpoint}"

# Test connection
async def test_backend_connection():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{config.API_BASE_URL}/api/health")
            if response.status_code == 200:
                print("Backend connection successful")
                return True
            else:
                print(f"Backend health check failed: {response.status_code}")
                return False
    except Exception as e:
        print(f"Backend connection error: {e}")
        return False
```

### Debugging Tips

1. **Enable Logging**: Use the purpose-specific loggers to track parameter flow
2. **Check Network Tab**: Monitor API calls in browser developer tools
3. **Validate Parameters**: Add validation at each step of the pipeline
4. **Test Individual Components**: Test frontend and backend separately
5. **Use Default Values**: Ensure all parameters have sensible defaults

## Conclusion

This guide provides a comprehensive overview of how parameters flow from the frontend to the backend in the PINN research platform. Understanding this flow is essential for:

- **Adding new parameters**: Know where to add them in the pipeline
- **Debugging issues**: Trace parameter flow through the system
- **Customizing training**: Modify parameters for specific use cases
- **Extending functionality**: Add new parameter types and validation

The modular architecture ensures that parameters are properly validated, converted, and used throughout the training process, providing a robust foundation for PINN research and development.

For additional information, refer to:
- [Forward Problems README](FORWARD_PROBLEMS_README.md)
- [Inverse Problems README](INVERSE_PROBLEMS_README.md)
- [Configuration Guide](CONFIGURATION_README.md)
- [API Documentation](API_README.md) 