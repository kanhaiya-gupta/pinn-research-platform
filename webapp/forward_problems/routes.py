"""
Routes for Forward Problems PINN Application
"""

from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import httpx
from pathlib import Path
import sys

# Add parent directory to path to import config
sys.path.append(str(Path(__file__).parent.parent))
from config.config import Config
from config.equations import ALL_PURPOSE_EQUATIONS
from config.parameters import ALL_PURPOSE_PARAMETERS

# Add comprehensive models import
sys.path.append(str(Path(__file__).parent.parent.parent))
from utils.comprehensive_models import ComprehensiveTrainingRequest, SamplingMethod, BoundaryConditionType, InitialConditionType


router = APIRouter(prefix="/purpose/forward_problems", tags=["Forward Problems"])
templates = Jinja2Templates(directory="templates")
config = Config()

# Get forward problems equations and parameters from modular structure
FORWARD_PROBLEMS_EQUATIONS = ALL_PURPOSE_EQUATIONS.get('forward_problems', {})
FORWARD_PROBLEMS_PARAMETERS = ALL_PURPOSE_PARAMETERS.get('forward_problems', {})

@router.get("/", response_class=HTMLResponse)
async def forward_problems_page(request: Request):
    """Forward Problems main page"""
    purpose_info = config.get_purpose_info("forward_problems")
    equations = config.get_equations_by_purpose("forward_problems")
    parameters = config.get_parameters_by_purpose("forward_problems")
    
    return templates.TemplateResponse(
        "forward_problems/index.html",
        {
            "request": request,
            "purpose": purpose_info,
            "purpose_key": "forward_problems",
            "equations": equations,
            "parameters": parameters,
            "config": config,
            "title": f"{purpose_info['name']} - PINN Applications"
        }
    )

@router.get("/simulation/{eq_id}", response_class=HTMLResponse)
async def forward_problems_simulation(request: Request, eq_id: str):
    """Simulation page for forward problems and specific equation"""
    purpose_info = config.get_purpose_info("forward_problems")
    equations = config.get_equations_by_purpose("forward_problems")
    
    if eq_id not in equations:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    equation_info = equations[eq_id]
    parameters = config.get_parameters_by_purpose("forward_problems")
    
    # Create default parameters for the template
    default_params = {
        "hidden_layers": 4,
        "neurons_per_layer": 20,
        "learning_rate": 0.001,
        "epochs": 10000
    }
    
    # Add equation-specific default parameters
    for param_id, param_info in parameters.items():
        if isinstance(param_info, dict) and 'default' in param_info:
            default_params[param_id] = param_info['default']
    
    return templates.TemplateResponse(
        "forward_problems/simulation.html",
        {
            "request": request,
            "purpose": purpose_info,
            "purpose_key": "forward_problems",
            "equation": equation_info,
            "eq_id": eq_id,
            "parameters": parameters,
            "default_params": default_params,
            "config": config,
            "title": f"Simulate {equation_info['name']} - {purpose_info['name']}"
        }
    )

@router.get("/results/{eq_id}", response_class=HTMLResponse)
async def forward_problems_results(request: Request, eq_id: str):
    """Results page for forward problems and specific equation"""
    purpose_info = config.get_purpose_info("forward_problems")
    equations = config.get_equations_by_purpose("forward_problems")
    
    if eq_id not in equations:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    equation_info = equations[eq_id]
    
    return templates.TemplateResponse(
        "forward_problems/results.html",
        {
            "request": request,
            "purpose": purpose_info,
            "purpose_key": "forward_problems",
            "equation": equation_info,
            "eq_id": eq_id,
            "config": config,
            "title": f"Results - {equation_info['name']} - {purpose_info['name']}"
        }
    )

# API endpoints for forward problems
@router.post("/api/simulate/{eq_id}")
async def forward_problems_simulate(eq_id: str, request: Request):
    """Submit training request for forward problems"""
    purpose_info = config.get_purpose_info("forward_problems")
    equations = config.get_equations_by_purpose("forward_problems")
    
    if eq_id not in equations:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    try:
        body = await request.json()
        
        # Add forward problems specific parameters
        body["purpose"] = "forward_problems"
        body["equation_id"] = eq_id
        
        # Map frontend parameters to backend format
        backend_params = map_parameters_to_backend(eq_id, body)
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{config.API_BASE_URL}/api/forward_problems/{eq_id}/train",
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

@router.get("/api/results/{eq_id}")
async def forward_problems_get_results(eq_id: str):
    """Get results for forward problems simulation"""
    purpose_info = config.get_purpose_info("forward_problems")
    equations = config.get_equations_by_purpose("forward_problems")
    
    if eq_id not in equations:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{config.API_BASE_URL}/api/forward_problems/{eq_id}/results",
                timeout=30.0
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                raise HTTPException(status_code=response.status_code, 
                                  detail=f"Backend error: {response.text}")
                
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get results: {str(e)}")

def map_parameters_to_backend(eq_id: str, frontend_params: dict) -> dict:
    """Map frontend parameters to backend format for forward problems"""
    backend_params = {
        "hidden_layers": frontend_params.get("hidden_layers", 4),
        "neurons_per_layer": frontend_params.get("neurons_per_layer", 20),
        "learning_rate": frontend_params.get("learning_rate", 0.001),
        "epochs": frontend_params.get("epochs", 10000),
        "purpose": "forward_problems",
        "equation_id": eq_id
    }
    
    # Add equation-specific parameters from the modular structure
    parameters = config.get_parameters_by_purpose("forward_problems")
    for param_id, param_info in parameters.items():
        if isinstance(param_info, dict) and 'default' in param_info:
            if param_id in frontend_params:
                backend_params[param_id] = frontend_params[param_id]
            else:
                backend_params[param_id] = param_info['default']
    
    return backend_params

# Comprehensive parameter endpoints
@router.get("/comprehensive-parameters")
async def get_comprehensive_parameters():
    """Get comprehensive parameters for forward problems"""
    parameters = config.get_parameters_by_purpose("forward_problems")
    equations = config.get_equations_by_purpose("forward_problems")
    
    return {
        "parameters": parameters,
        "equations": equations,
        "purpose": "forward_problems"
    }

@router.get("/parameter-recommendations")
async def get_parameter_recommendations(equation: str = "burgers"):
    """Get parameter recommendations for specific equation"""
    equations = config.get_equations_by_purpose("forward_problems")
    parameters = config.get_parameters_by_purpose("forward_problems")
    
    if equation not in equations:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    # Get equation-specific parameter recommendations
    recommendations = {}
    for param_id, param_info in parameters.items():
        if isinstance(param_info, dict):
            recommendations[param_id] = {
                "name": param_info.get("name", param_id),
                "description": param_info.get("description", ""),
                "default": param_info.get("default", 0.0),
                "range": param_info.get("range", [0.0, 1.0]),
                "unit": param_info.get("unit", ""),
                "category": param_info.get("category", "")
            }
    
    return {
        "equation": equation,
        "recommendations": recommendations,
        "purpose": "forward_problems"
    }

@router.post("/validate-parameters")
async def validate_parameters(request: ComprehensiveTrainingRequest):
    """Validate training parameters for forward problems"""
    # Basic validation
    if request.epochs <= 0:
        raise HTTPException(status_code=400, detail="Epochs must be positive")
    
    if request.learning_rate <= 0:
        raise HTTPException(status_code=400, detail="Learning rate must be positive")
    
    if request.hidden_layers <= 0:
        raise HTTPException(status_code=400, detail="Hidden layers must be positive")
    
    if request.neurons_per_layer <= 0:
        raise HTTPException(status_code=400, detail="Neurons per layer must be positive")
    
    return {
        "valid": True,
        "message": "Parameters are valid for forward problems training",
        "purpose": "forward_problems"
    }
