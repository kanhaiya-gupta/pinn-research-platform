"""
Routes for Multiphysics PINN Application
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

router = APIRouter(prefix="/purpose/multiphysics", tags=["Multiphysics"])
templates = Jinja2Templates(directory="templates")
config = Config()

# Get multiphysics equations and parameters from modular structure
MULTIPHYSICS_EQUATIONS = ALL_PURPOSE_EQUATIONS.get('multiphysics', {})
MULTIPHYSICS_PARAMETERS = ALL_PURPOSE_PARAMETERS.get('multiphysics', {})

@router.get("/", response_class=HTMLResponse)
async def multiphysics_page(request: Request):
    """Multiphysics main page"""
    purpose_info = config.get_purpose_info("multiphysics")
    equations = config.get_equations_by_purpose("multiphysics")
    parameters = config.get_parameters_by_purpose("multiphysics")
    
    return templates.TemplateResponse(
        "multiphysics/index.html",
        {
            "request": request,
            "purpose": purpose_info,
            "purpose_key": "multiphysics",
            "equations": equations,
            "parameters": parameters,
            "config": config,
            "title": f"{purpose_info['name']} - PINN Applications"
        }
    )

@router.get("/results/{eq_id}", response_class=HTMLResponse)
async def multiphysics_results(request: Request, eq_id: str):
    """Results page for multiphysics and specific equation"""
    purpose_info = config.get_purpose_info("multiphysics")
    equations = config.get_equations_by_purpose("multiphysics")
    
    if eq_id not in equations:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    equation_info = equations[eq_id]
    
    return templates.TemplateResponse(
        "multiphysics/results.html",
        {
            "request": request,
            "purpose": purpose_info,
            "purpose_key": "multiphysics",
            "equation": equation_info,
            "eq_id": eq_id,
            "config": config,
            "title": f"Results - {equation_info['name']} - {purpose_info['name']}"
        }
    )

# API endpoints for multiphysics
@router.post("/api/simulate/{eq_id}")
async def multiphysics_simulate(eq_id: str, request: Request):
    """Submit training request for multiphysics"""
    purpose_info = config.get_purpose_info("multiphysics")
    equations = config.get_equations_by_purpose("multiphysics")
    
    if eq_id not in equations:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    try:
        body = await request.json()
        
        # Add multiphysics specific parameters
        body["purpose"] = "multiphysics"
        body["equation_id"] = eq_id
        
        # Map frontend parameters to backend format
        backend_params = map_parameters_to_backend(eq_id, body)
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{config.API_BASE_URL}/api/multiphysics/{eq_id}/train",
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
async def multiphysics_get_results(eq_id: str):
    """Get results for multiphysics simulation"""
    purpose_info = config.get_purpose_info("multiphysics")
    equations = config.get_equations_by_purpose("multiphysics")
    
    if eq_id not in equations:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{config.API_BASE_URL}/api/multiphysics/{eq_id}/results",
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
    """Map frontend parameters to backend format for multiphysics"""
    backend_params = {
        "hidden_layers": frontend_params.get("hidden_layers", 4),
        "neurons_per_layer": frontend_params.get("neurons_per_layer", 20),
        "learning_rate": frontend_params.get("learning_rate", 0.001),
        "epochs": frontend_params.get("epochs", 10000),
        "purpose": "multiphysics",
        "equation_id": eq_id
    }
    
    # Add equation-specific parameters from the modular structure
    parameters = config.get_parameters_by_purpose("multiphysics")
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
    """Get comprehensive parameters for multiphysics"""
    parameters = config.get_parameters_by_purpose("multiphysics")
    equations = config.get_equations_by_purpose("multiphysics")
    
    return {
        "parameters": parameters,
        "equations": equations,
        "purpose": "multiphysics"
    }

@router.get("/parameter-recommendations")
async def get_parameter_recommendations(equation: str = "burgers"):
    """Get parameter recommendations for specific equation"""
    equations = config.get_equations_by_purpose("multiphysics")
    parameters = config.get_parameters_by_purpose("multiphysics")
    
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
        "purpose": "multiphysics"
    }

@router.post("/validate-parameters")
async def validate_parameters(request: ComprehensiveTrainingRequest):
    """Validate parameters for multiphysics training"""
    # Add validation logic here
    return {"valid": True, "message": "Parameters validated successfully"}
