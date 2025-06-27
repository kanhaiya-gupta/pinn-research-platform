"""
Routes for Data Assimilation PINN Application
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

router = APIRouter(prefix="/purpose/data_assimilation", tags=["Data Assimilation"])
templates = Jinja2Templates(directory="templates")
config = Config()

# Get data_assimilation equations and parameters from modular structure
DATA_ASSIMILATION_EQUATIONS = ALL_PURPOSE_EQUATIONS.get('data_assimilation', {})
DATA_ASSIMILATION_PARAMETERS = ALL_PURPOSE_PARAMETERS.get('data_assimilation', {})

# API endpoints for data assimilation
@router.post("/api/simulate/{eq_id}")
async def data_assimilation_simulate(eq_id: str, request: Request):
    """Submit training request for data assimilation"""
    purpose_info = config.get_purpose_info("data_assimilation")
    equations = config.get_equations_by_purpose("data_assimilation")
    
    if eq_id not in equations:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    try:
        body = await request.json()
        
        # Add data_assimilation specific parameters
        body["purpose"] = "data_assimilation"
        body["equation_id"] = eq_id
        
        # Map frontend parameters to backend format
        backend_params = map_parameters_to_backend(eq_id, body)
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{config.API_BASE_URL}/api/data_assimilation/{eq_id}/train",
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
async def data_assimilation_get_results(eq_id: str):
    """Get results for data assimilation simulation"""
    purpose_info = config.get_purpose_info("data_assimilation")
    equations = config.get_equations_by_purpose("data_assimilation")
    
    if eq_id not in equations:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{config.API_BASE_URL}/api/data_assimilation/{eq_id}/results",
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
    """Map frontend parameters to backend format for data assimilation"""
    backend_params = {
        "hidden_layers": frontend_params.get("hidden_layers", 4),
        "neurons_per_layer": frontend_params.get("neurons_per_layer", 20),
        "learning_rate": frontend_params.get("learning_rate", 0.001),
        "epochs": frontend_params.get("epochs", 10000),
        "purpose": "data_assimilation",
        "equation_id": eq_id
    }
    
    # Add equation-specific parameters from the modular structure
    parameters = config.get_parameters_by_purpose("data_assimilation")
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
    """Get comprehensive parameters for data assimilation"""
    parameters = config.get_parameters_by_purpose("data_assimilation")
    equations = config.get_equations_by_purpose("data_assimilation")
    
    return {
        "parameters": parameters,
        "equations": equations,
        "purpose": "data_assimilation"
    }

@router.get("/parameter-recommendations")
async def get_parameter_recommendations(equation: str = "burgers"):
    """Get parameter recommendations for specific equation"""
    equations = config.get_equations_by_purpose("data_assimilation")
    parameters = config.get_parameters_by_purpose("data_assimilation")
    
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
        "purpose": "data_assimilation"
    }

@router.post("/validate-parameters")
async def validate_parameters(request: Request):
    """Validate parameters for data assimilation"""
    try:
        body = await request.json()
        equation = body.get("equation", "burgers")
        parameters = body.get("parameters", {})
        
        equations = config.get_equations_by_purpose("data_assimilation")
        if equation not in equations:
            raise HTTPException(status_code=404, detail="Equation not found")
        
        # Basic validation
        validation_results = {}
        for param_id, value in parameters.items():
            if param_id in DATA_ASSIMILATION_PARAMETERS:
                param_info = DATA_ASSIMILATION_PARAMETERS[param_id]
                if isinstance(param_info, dict) and 'range' in param_info:
                    min_val, max_val = param_info['range']
                    if value < min_val or value > max_val:
                        validation_results[param_id] = f"Value {value} outside range [{min_val}, {max_val}]"
                    else:
                        validation_results[param_id] = "Valid"
                else:
                    validation_results[param_id] = "Valid"
            else:
                validation_results[param_id] = "Unknown parameter"
        
        return {
            "equation": equation,
            "validation_results": validation_results,
            "purpose": "data_assimilation"
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Validation failed: {str(e)}")

@router.get("/training-status/{eq_id}")
async def get_training_status(eq_id: str):
    """Get training status for data assimilation simulation"""
    purpose_info = config.get_purpose_info("data_assimilation")
    equations = config.get_equations_by_purpose("data_assimilation")
    
    if eq_id not in equations:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{config.API_BASE_URL}/api/data_assimilation/{eq_id}/status",
                timeout=10.0
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                raise HTTPException(status_code=response.status_code, 
                                  detail=f"Backend error: {response.text}")
                
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get status: {str(e)}")

@router.delete("/cancel-training/{eq_id}")
async def cancel_training(eq_id: str):
    """Cancel ongoing training for data assimilation"""
    purpose_info = config.get_purpose_info("data_assimilation")
    equations = config.get_equations_by_purpose("data_assimilation")
    
    if eq_id not in equations:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.delete(
                f"{config.API_BASE_URL}/api/data_assimilation/{eq_id}/cancel",
                timeout=10.0
            )
            
            if response.status_code == 200:
                return {"message": "Training cancelled successfully"}
            else:
                raise HTTPException(status_code=response.status_code, 
                                  detail=f"Backend error: {response.text}")
                
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to cancel training: {str(e)}")
