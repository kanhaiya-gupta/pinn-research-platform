from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import httpx
import sys
import os

# Add the parent directory to the path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import config

# Create templates instance
templates = Jinja2Templates(directory="templates")

# Create router instance
router = APIRouter(prefix="/control_optimization", tags=["control_optimization"])

@router.get("/", response_class=HTMLResponse)
async def control_optimization_page(request: Request):
    """Main page for control optimization"""
    purpose_info = config.get_purpose_info("control_optimization")
    equations = config.get_equations_by_purpose("control_optimization")
    parameters = config.get_parameters_by_purpose("control_optimization")
    
    return templates.TemplateResponse(
        "control_optimization/index.html",
        {
            "request": request,
            "purpose": purpose_info,
            "purpose_key": "control_optimization",
            "equations": equations,
            "parameters": parameters,
            "config": config,
            "title": f"{purpose_info['name']} - PINN Platform"
        }
    )

@router.get("/simulation/{{eq_id}}", response_class=HTMLResponse)
async def control_optimization_simulation(request: Request, eq_id: str):
    """Simulation page for control optimization and specific equation"""
    purpose_info = config.get_purpose_info("control_optimization")
    equations = config.get_equations_by_purpose("control_optimization")
    parameters = config.get_parameters_by_purpose("control_optimization")
    
    if eq_id not in equations:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    equation_info = equations[eq_id]
    
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
        "control_optimization/simulation.html",
        {
            "request": request,
            "purpose": purpose_info,
            "purpose_key": "control_optimization",
            "equation": equation_info,
            "eq_id": eq_id,
            "parameters": parameters,
            "default_params": default_params,
            "config": config,
            "title": f"Simulate {equation_info['name']} - {purpose_info['name']}"
        }
    )

@router.get("/results/{{eq_id}}", response_class=HTMLResponse)
async def control_optimization_results(request: Request, eq_id: str):
    """Results page for control optimization and specific equation"""
    purpose_info = config.get_purpose_info("control_optimization")
    equations = config.get_equations_by_purpose("control_optimization")
    
    if eq_id not in equations:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    equation_info = equations[eq_id]
    
    return templates.TemplateResponse(
        "control_optimization/results.html",
        {
            "request": request,
            "purpose": purpose_info,
            "purpose_key": "control_optimization",
            "equation": equation_info,
            "eq_id": eq_id,
            "config": config,
            "title": f"Results - {equation_info['name']} - {purpose_info['name']}"
        }
    )

# API endpoints for control optimization
@router.post("/api/simulate/{{eq_id}}")
async def control_optimization_simulate(eq_id: str, request: Request):
    """Submit training request for control optimization"""
    purpose_info = config.get_purpose_info("control_optimization")
    equations = config.get_equations_by_purpose("control_optimization")
    
    if eq_id not in equations:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    try:
        body = await request.json()
        
        # Add control_optimization specific parameters
        body["purpose"] = "control_optimization"
        body["equation_id"] = eq_id
        
        # Map frontend parameters to backend format
        backend_params = map_parameters_to_backend(eq_id, body)
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{{config.API_BASE_URL}}/api/control_optimization/{{eq_id}}/train",
                json=backend_params,
                timeout=300.0
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                raise HTTPException(status_code=response.status_code, 
                                  detail=f"Backend error: {{response.text}}")
                
    except httpx.TimeoutException:
        raise HTTPException(status_code=408, detail="Training timeout - model may still be training")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Training failed: {{str(e)}}")

@router.get("/api/results/{{eq_id}}")
async def control_optimization_get_results(eq_id: str):
    """Get results for control optimization simulation"""
    purpose_info = config.get_purpose_info("control_optimization")
    equations = config.get_equations_by_purpose("control_optimization")
    
    if eq_id not in equations:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{{config.API_BASE_URL}}/api/control_optimization/{{eq_id}}/results",
                timeout=30.0
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                raise HTTPException(status_code=response.status_code, 
                                  detail=f"Backend error: {{response.text}}")
                
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get results: {{str(e)}}")

def map_parameters_to_backend(eq_id: str, frontend_params: dict) -> dict:
    """Map frontend parameters to backend format for control optimization"""
    backend_params = {
        "hidden_layers": frontend_params.get("hidden_layers", 4),
        "neurons_per_layer": frontend_params.get("neurons_per_layer", 20),
        "learning_rate": frontend_params.get("learning_rate", 0.001),
        "epochs": frontend_params.get("epochs", 10000),
        "purpose": "control_optimization",
        "equation_id": eq_id
    }
    
    # Add equation-specific parameters from the modular structure
    parameters = config.get_parameters_by_purpose("control_optimization")
    for param_id, param_info in parameters.items():
        if isinstance(param_info, dict) and 'default' in param_info:
            if param_id in frontend_params:
                backend_params[param_id] = frontend_params[param_id]
            else:
                backend_params[param_id] = param_info['default']
    
    return backend_params
