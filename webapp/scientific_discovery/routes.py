"""
Routes for Scientific Discovery PINN Application
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

router = APIRouter(prefix="/purpose/scientific_discovery", tags=["Scientific Discovery"])
templates = Jinja2Templates(directory="templates")
config = Config()

@router.get("/", response_class=HTMLResponse)
async def scientific_discovery_page(request: Request):
    """Scientific Discovery main page"""
    purpose_info = config.PINN_PURPOSES["scientific_discovery"]
    
    # Get equations that support this purpose
    supported_equations = {}
    for eq_key, eq_info in config.SUPPORTED_EQUATIONS.items():
        if "scientific_discovery" in eq_info.get('purposes', []):
            supported_equations[eq_key] = eq_info
    
    return templates.TemplateResponse(
        "scientific_discovery/index.html",
        {
            "request": request,
            "purpose": purpose_info,
            "purpose_key": "scientific_discovery",
            "supported_equations": supported_equations,
            "config": config,
            "title": f"{purpose_info['name']} - PINN Applications"
        }
    )

@router.get("/simulation/{eq_type}", response_class=HTMLResponse)
async def scientific_discovery_simulation(request: Request, eq_type: str):
    """Simulation page for scientific discovery and specific equation"""
    if eq_type not in config.SUPPORTED_EQUATIONS:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    purpose_info = config.PINN_PURPOSES["scientific_discovery"]
    equation_info = config.SUPPORTED_EQUATIONS[eq_type]
    default_params = config.DEFAULT_PARAMETERS.get(eq_type, {})
    
    # Verify that this equation supports this purpose
    if "scientific_discovery" not in equation_info.get('purposes', []):
        raise HTTPException(status_code=400, detail="Equation does not support scientific discovery")
    
    return templates.TemplateResponse(
        "scientific_discovery/simulation.html",
        {
            "request": request,
            "purpose": purpose_info,
            "purpose_key": "scientific_discovery",
            "equation": equation_info,
            "eq_type": eq_type,
            "default_params": default_params,
            "config": config,
            "title": f"Simulate {equation_info['name']} - {purpose_info['name']}"
        }
    )

@router.get("/results/{eq_type}", response_class=HTMLResponse)
async def scientific_discovery_results(request: Request, eq_type: str):
    """Results page for scientific discovery and specific equation"""
    if eq_type not in config.SUPPORTED_EQUATIONS:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    purpose_info = config.PINN_PURPOSES["scientific_discovery"]
    equation_info = config.SUPPORTED_EQUATIONS[eq_type]
    
    return templates.TemplateResponse(
        "scientific_discovery/results.html",
        {
            "request": request,
            "purpose": purpose_info,
            "purpose_key": "scientific_discovery",
            "equation": equation_info,
            "eq_type": eq_type,
            "config": config,
            "title": f"Results - {equation_info['name']} - {purpose_info['name']}"
        }
    )

# API endpoints for scientific discovery
@router.post("/api/simulate/{eq_type}")
async def scientific_discovery_simulate(eq_type: str, request: Request):
    """Submit training request for scientific discovery"""
    if eq_type not in config.SUPPORTED_EQUATIONS:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    try:
        body = await request.json()
        
        # Add scientific_discovery specific parameters
        body["purpose"] = "scientific_discovery"
        
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
async def scientific_discovery_get_results(eq_type: str):
    """Get results for scientific discovery simulation"""
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
    """Map frontend parameters to backend format for scientific discovery"""
    backend_params = {
        "hidden_layers": frontend_params.get("hidden_layers", 4),
        "neurons_per_layer": frontend_params.get("neurons_per_layer", 20),
        "learning_rate": frontend_params.get("learning_rate", 0.001),
        "epochs": frontend_params.get("epochs", 10000),
        "purpose": "scientific_discovery"
    }
    
    # Add purpose-specific parameters
    backend_params["hypothesis_complexity"] = frontend_params.get("hypothesis_complexity", 3)  # Complexity of hypotheses to test
    backend_params["discovery_threshold"] = frontend_params.get("discovery_threshold", 0.01)  # Threshold for new discoveries
    
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
