"""
Routes for Sparse Data Learning PINN Application
"""

from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import httpx
from pathlib import Path
import sys

# Add parent directory to path to import config
sys.path.append(str(Path(__file__).parent.parent))
from config import Config

# Add comprehensive models import
sys.path.append(str(Path(__file__).parent.parent.parent))
from utils.comprehensive_models import ComprehensiveTrainingRequest, SamplingMethod, BoundaryConditionType, InitialConditionType

router = APIRouter(prefix="/purpose/sparse_data", tags=["Sparse Data Learning"])
templates = Jinja2Templates(directory="templates")
config = Config()

@router.get("/", response_class=HTMLResponse)
async def sparse_data_page(request: Request):
    """Sparse Data Learning main page"""
    purpose_info = config.PINN_PURPOSES["sparse_data"]
    
    # Get equations that support this purpose
    supported_equations = {}
    for eq_key, eq_info in config.SUPPORTED_EQUATIONS.items():
        if "sparse_data" in eq_info.get('purposes', []):
            supported_equations[eq_key] = eq_info
    
    return templates.TemplateResponse(
        "sparse_data/index.html",
        {
            "request": request,
            "purpose": purpose_info,
            "purpose_key": "sparse_data",
            "supported_equations": supported_equations,
            "config": config,
            "title": f"{purpose_info['name']} - PINN Applications"
        }
    )

@router.get("/simulation/{eq_type}", response_class=HTMLResponse)
async def sparse_data_simulation(request: Request, eq_type: str):
    """Simulation page for sparse data learning and specific equation"""
    if eq_type not in config.SUPPORTED_EQUATIONS:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    purpose_info = config.PINN_PURPOSES["sparse_data"]
    equation_info = config.SUPPORTED_EQUATIONS[eq_type]
    default_params = config.DEFAULT_PARAMETERS.get(eq_type, {})
    
    # Verify that this equation supports this purpose
    if "sparse_data" not in equation_info.get('purposes', []):
        raise HTTPException(status_code=400, detail="Equation does not support sparse data learning")
    
    return templates.TemplateResponse(
        "sparse_data/simulation.html",
        {
            "request": request,
            "purpose": purpose_info,
            "purpose_key": "sparse_data",
            "equation": equation_info,
            "eq_type": eq_type,
            "default_params": default_params,
            "config": config,
            "title": f"Simulate {equation_info['name']} - {purpose_info['name']}"
        }
    )

@router.get("/results/{eq_type}", response_class=HTMLResponse)
async def sparse_data_results(request: Request, eq_type: str):
    """Results page for sparse data learning and specific equation"""
    if eq_type not in config.SUPPORTED_EQUATIONS:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    purpose_info = config.PINN_PURPOSES["sparse_data"]
    equation_info = config.SUPPORTED_EQUATIONS[eq_type]
    
    return templates.TemplateResponse(
        "sparse_data/results.html",
        {
            "request": request,
            "purpose": purpose_info,
            "purpose_key": "sparse_data",
            "equation": equation_info,
            "eq_type": eq_type,
            "config": config,
            "title": f"Results - {equation_info['name']} - {purpose_info['name']}"
        }
    )

# API endpoints for sparse data learning
@router.post("/api/simulate/{eq_type}")
async def sparse_data_simulate(eq_type: str, request: Request):
    """Submit training request for sparse data learning"""
    if eq_type not in config.SUPPORTED_EQUATIONS:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    try:
        body = await request.json()
        
        # Add sparse_data specific parameters
        body["purpose"] = "sparse_data"
        
        # Map frontend parameters to backend format
        backend_params = map_parameters_to_backend(eq_type, body)
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{config.API_BASE_URL}/api/{eq_type}/train",
                json=backend_params,
                timeout=300.0
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                raise HTTPException(status_code=response.status_code, 
                                  detail=f"Backend error: {response.text}")
                
    except httpx.TimeoutException:
        raise HTTPException(status_code=408, detail="Training timeout - model may still be training")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Training failed: {str(e)}")

@router.get("/api/results/{eq_type}")
async def sparse_data_get_results(eq_type: str):
    """Get results for sparse data learning simulation"""
    if eq_type not in config.SUPPORTED_EQUATIONS:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{config.API_BASE_URL}/api/{eq_type}/results",
                timeout=30.0
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                raise HTTPException(status_code=response.status_code, 
                                  detail=f"Backend error: {response.text}")
                
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get results: {str(e)}")

def map_parameters_to_backend(eq_type: str, frontend_params: dict) -> dict:
    """Map frontend parameters to backend format for sparse data learning"""
    backend_params = {
        "hidden_layers": frontend_params.get("hidden_layers", 4),
        "neurons_per_layer": frontend_params.get("neurons_per_layer", 20),
        "learning_rate": frontend_params.get("learning_rate", 0.001),
        "epochs": frontend_params.get("epochs", 10000),
        "purpose": "sparse_data"
    }
    
    # Add purpose-specific parameters
    backend_params["data_points"] = frontend_params.get("data_points", 50)  # Number of data points
    backend_params["noise_level"] = frontend_params.get("noise_level", 0.05)  # Measurement noise level
    
    # Add equation-specific parameters
    if eq_type == "heat":
        backend_params.update({
            "thermal_diffusivity": frontend_params.get("thermal_diffusivity", 0.1),
            "domain_size": frontend_params.get("domain_size", 1.0)
        })
    elif eq_type == "wave":
        backend_params.update({
            "wave_speed": frontend_params.get("wave_speed", 1.0),
            "domain_size": frontend_params.get("domain_size", 1.0)
        })
    elif eq_type == "burgers":
        backend_params.update({
            "viscosity": frontend_params.get("viscosity", 0.01),
            "domain_size": frontend_params.get("domain_size", 1.0)
        })
    elif eq_type == "shm":
        backend_params.update({
            "frequency": frontend_params.get("frequency", 1.0),
            "amplitude": frontend_params.get("amplitude", 1.0)
        })
    
    return backend_params


@router.get("/comprehensive-parameters")
async def get_comprehensive_parameters():
    """Get comprehensive parameter options and recommendations."""
    return {
        "sampling_methods": [method.value for method in SamplingMethod],
        "boundary_conditions": [bc.value for bc in BoundaryConditionType],
        "initial_conditions": [ic.value for ic in InitialConditionType],
        "activation_functions": {
            "hidden": ["tanh", "sin", "softplus", "sigmoid", "relu"],
            "output": ["linear", "tanh", "sigmoid", "softplus"]
        },
        "optimizers": ["adam", "lbfgs", "adam_lbfgs", "sgd"],
        "weight_inits": ["xavier", "normal", "uniform", "he"],
        "schedulers": ["constant", "step", "cosine", "exponential"],
        "error_metrics": ["l2_norm", "relative_error", "rmse", "mae", "max_error"],
        "scaling_methods": ["none", "domain_size", "adaptive"]
    }

@router.get("/parameter-recommendations")
async def get_parameter_recommendations(equation: str = "burgers"):
    """Get parameter recommendations for specific equations."""
    recommendations = {
        "burgers": {
            "hidden_activation": "tanh",
            "output_activation": "linear",
            "optimizer": "adam_lbfgs",
            "time_duration": 1.0,
            "time_points": 100,
            "n_interior_points": 1000,
            "n_boundary_points": 200,
            "physics_weight": 1.0,
            "boundary_weight": 1.0,
            "initial_weight": 1.0,
            "notes": "Burgers equation benefits from smooth activations and careful loss balancing"
        },
        "heat": {
            "hidden_activation": "tanh",
            "output_activation": "linear",
            "optimizer": "adam_lbfgs",
            "time_duration": 1.0,
            "time_points": 100,
            "n_interior_points": 800,
            "n_boundary_points": 150,
            "physics_weight": 1.0,
            "boundary_weight": 1.0,
            "initial_weight": 1.0,
            "notes": "Heat equation is well-behaved, standard parameters work well"
        },
        "wave": {
            "hidden_activation": "sin",
            "output_activation": "linear",
            "optimizer": "adam_lbfgs",
            "time_duration": 2.0,
            "time_points": 200,
            "n_interior_points": 1200,
            "n_boundary_points": 300,
            "physics_weight": 1.0,
            "boundary_weight": 1.0,
            "initial_weight": 1.0,
            "notes": "Wave equation benefits from sin activation for oscillatory behavior"
        }
    }
    
    return recommendations.get(equation, recommendations["burgers"])

@router.post("/validate-parameters")
async def validate_parameters(request: ComprehensiveTrainingRequest):
    """Validate comprehensive training parameters."""
    validation_results = {
        "valid": True,
        "warnings": [],
        "errors": []
    }
    
    # Check for potential issues
    if request.hidden_activation == "relu":
        validation_results["warnings"].append("ReLU activation may not be smooth enough for PDEs")
    
    if request.optimizer == "sgd":
        validation_results["warnings"].append("SGD optimizer is not recommended for PINNs")
    
    if request.learning_rate > 0.01:
        validation_results["warnings"].append("High learning rate may cause instability")
    
    if request.n_interior_points < 500:
        validation_results["warnings"].append("Low number of interior points may affect accuracy")
    
    if request.physics_weight < 0.1 or request.physics_weight > 10.0:
        validation_results["errors"].append("Physics weight should be between 0.1 and 10.0")
    
    if validation_results["errors"]:
        validation_results["valid"] = False
    
    return validation_results
