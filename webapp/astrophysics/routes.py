"""
Routes for Astrophysics PINN Application
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

router = APIRouter(prefix="/purpose/astrophysics", tags=["Astrophysics"])
templates = Jinja2Templates(directory="templates")
config = Config()

# Get astrophysics equations and parameters from modular structure
ASTROPHYSICS_EQUATIONS = ALL_PURPOSE_EQUATIONS.get('astrophysics', {})
ASTROPHYSICS_PARAMETERS = ALL_PURPOSE_PARAMETERS.get('astrophysics', {})

@router.get("/", response_class=HTMLResponse)
async def astrophysics_page(request: Request):
    """Astrophysics main page"""
    purpose_info = config.get_purpose_info("astrophysics")
    equations = config.get_equations_by_purpose("astrophysics")
    parameters = config.get_parameters_by_purpose("astrophysics")
    
    return templates.TemplateResponse(
        "astrophysics/index.html",
        {
            "request": request,
            "purpose": purpose_info,
            "purpose_key": "astrophysics",
            "equations": equations,
            "parameters": parameters,
            "config": config,
            "title": f"{purpose_info['name']} - PINN Applications"
        }
    )

@router.get("/results/{eq_id}", response_class=HTMLResponse)
async def astrophysics_results(request: Request, eq_id: str):
    """Results page for astrophysics and specific equation"""
    purpose_info = config.get_purpose_info("astrophysics")
    equations = config.get_equations_by_purpose("astrophysics")
    
    if eq_id not in equations:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    equation_info = equations[eq_id]
    
    return templates.TemplateResponse(
        "astrophysics/results.html",
        {
            "request": request,
            "purpose": purpose_info,
            "purpose_key": "astrophysics",
            "equation": equation_info,
            "eq_id": eq_id,
            "config": config,
            "title": f"Results - {equation_info['name']} - {purpose_info['name']}"
        }
    )

# API endpoints for astrophysics
@router.post("/api/simulate/{eq_id}")
async def astrophysics_simulate(eq_id: str, request: Request):
    """Submit training request for astrophysics"""
    purpose_info = config.get_purpose_info("astrophysics")
    equations = config.get_equations_by_purpose("astrophysics")
    
    if eq_id not in equations:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    try:
        body = await request.json()
        
        # Add astrophysics specific parameters
        body["purpose"] = "astrophysics"
        body["equation_id"] = eq_id
        
        # Map frontend parameters to backend format
        backend_params = map_parameters_to_backend(eq_id, body)
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{config.API_BASE_URL}/api/astrophysics/{eq_id}/train",
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
async def astrophysics_get_results(eq_id: str):
    """Get results for astrophysics simulation"""
    purpose_info = config.get_purpose_info("astrophysics")
    equations = config.get_equations_by_purpose("astrophysics")
    
    if eq_id not in equations:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{config.API_BASE_URL}/api/astrophysics/{eq_id}/results",
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
    """Map frontend parameters to backend format for astrophysics"""
    backend_params = {
        "hidden_layers": frontend_params.get("hidden_layers", 4),
        "neurons_per_layer": frontend_params.get("neurons_per_layer", 20),
        "learning_rate": frontend_params.get("learning_rate", 0.001),
        "epochs": frontend_params.get("epochs", 10000),
        "purpose": "astrophysics",
        "equation_id": eq_id
    }
    
    # Add equation-specific parameters from the modular structure
    parameters = config.get_parameters_by_purpose("astrophysics")
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
    """Get comprehensive parameters for astrophysics"""
    parameters = config.get_parameters_by_purpose("astrophysics")
    equations = config.get_equations_by_purpose("astrophysics")
    
    return {
        "parameters": parameters,
        "equations": equations,
        "purpose": "astrophysics"
    }

@router.get("/parameter-recommendations")
async def get_parameter_recommendations(equation: str = "schwarzschild_metric"):
    """Get parameter recommendations for specific equation"""
    equations = config.get_equations_by_purpose("astrophysics")
    parameters = config.get_parameters_by_purpose("astrophysics")
    
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
        "purpose": "astrophysics"
    }

@router.post("/validate-parameters")
async def validate_parameters(request: Request):
    """Validate astrophysics parameters"""
    try:
        body = await request.json()
        equation_id = body.get("equation_id")
        parameters = body.get("parameters", {})
        
        if not equation_id:
            raise HTTPException(status_code=400, detail="Equation ID is required")
        
        equations = config.get_equations_by_purpose("astrophysics")
        if equation_id not in equations:
            raise HTTPException(status_code=404, detail="Equation not found")
        
        # Validate parameters
        validation_results = {}
        astrophysics_params = config.get_parameters_by_purpose("astrophysics")
        
        for param_id, param_info in astrophysics_params.items():
            if isinstance(param_info, dict) and 'range' in param_info:
                if param_id in parameters:
                    value = parameters[param_id]
                    min_val, max_val = param_info['range']
                    if value < min_val or value > max_val:
                        validation_results[param_id] = {
                            "valid": False,
                            "message": f"Value must be between {min_val} and {max_val}"
                        }
                    else:
                        validation_results[param_id] = {"valid": True}
        
        return {
            "valid": all(result.get("valid", True) for result in validation_results.values()),
            "validation_results": validation_results
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Validation failed: {str(e)}")

@router.get("/equation-info/{eq_id}")
async def get_equation_info(eq_id: str):
    """Get detailed information about a specific astrophysics equation"""
    equations = config.get_equations_by_purpose("astrophysics")
    
    if eq_id not in equations:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    equation_info = equations[eq_id]
    parameters = config.get_parameters_by_purpose("astrophysics")
    
    # Get equation-specific parameters
    eq_params = {}
    for param_id, param_info in parameters.items():
        if isinstance(param_info, dict):
            eq_params[param_id] = param_info
    
    return {
        "equation": equation_info,
        "parameters": eq_params,
        "purpose": "astrophysics"
    }

@router.get("/training-status/{eq_id}")
async def get_training_status(eq_id: str):
    """Get training status for astrophysics simulation"""
    equations = config.get_equations_by_purpose("astrophysics")
    
    if eq_id not in equations:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{config.API_BASE_URL}/api/astrophysics/{eq_id}/status",
                timeout=10.0
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                return {"status": "unknown", "message": "Status unavailable"}
                
    except Exception as e:
        return {"status": "error", "message": f"Failed to get status: {str(e)}"}

@router.delete("/api/cancel-training/{eq_id}")
async def cancel_training(eq_id: str):
    """Cancel ongoing astrophysics training"""
    equations = config.get_equations_by_purpose("astrophysics")
    
    if eq_id not in equations:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.delete(
                f"{config.API_BASE_URL}/api/astrophysics/{eq_id}/cancel",
                timeout=10.0
            )
            
            if response.status_code == 200:
                return {"message": "Training cancelled successfully"}
            else:
                raise HTTPException(status_code=response.status_code, 
                                  detail=f"Failed to cancel training: {response.text}")
                
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to cancel training: {str(e)}")

@router.get("/export-results/{eq_id}")
async def export_results(eq_id: str, format: str = "json"):
    """Export astrophysics simulation results"""
    equations = config.get_equations_by_purpose("astrophysics")
    
    if eq_id not in equations:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    if format not in ["json", "csv", "matplotlib"]:
        raise HTTPException(status_code=400, detail="Unsupported format")
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{config.API_BASE_URL}/api/astrophysics/{eq_id}/export",
                params={"format": format},
                timeout=30.0
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                raise HTTPException(status_code=response.status_code, 
                                  detail=f"Export failed: {response.text}")
                
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Export failed: {str(e)}")

@router.get("/performance-metrics/{eq_id}")
async def get_performance_metrics(eq_id: str):
    """Get performance metrics for astrophysics simulation"""
    equations = config.get_equations_by_purpose("astrophysics")
    
    if eq_id not in equations:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{config.API_BASE_URL}/api/astrophysics/{eq_id}/metrics",
                timeout=15.0
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": "Metrics unavailable"}
                
    except Exception as e:
        return {"error": f"Failed to get metrics: {str(e)}"}

@router.post("/compare-simulations")
async def compare_simulations(request: Request):
    """Compare multiple astrophysics simulations"""
    try:
        body = await request.json()
        equation_ids = body.get("equation_ids", [])
        
        if not equation_ids:
            raise HTTPException(status_code=400, detail="At least one equation ID is required")
        
        equations = config.get_equations_by_purpose("astrophysics")
        for eq_id in equation_ids:
            if eq_id not in equations:
                raise HTTPException(status_code=404, detail=f"Equation {eq_id} not found")
        
        # Get results for all equations
        comparison_results = {}
        for eq_id in equation_ids:
            try:
                async with httpx.AsyncClient() as client:
                    response = await client.get(
                        f"{config.API_BASE_URL}/api/astrophysics/{eq_id}/results",
                        timeout=15.0
                    )
                    
                    if response.status_code == 200:
                        comparison_results[eq_id] = response.json()
                    else:
                        comparison_results[eq_id] = {"error": "Results unavailable"}
                        
            except Exception as e:
                comparison_results[eq_id] = {"error": f"Failed to get results: {str(e)}"}
        
        return {
            "comparison": comparison_results,
            "purpose": "astrophysics"
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Comparison failed: {str(e)}")

@router.get("/astrophysics-applications")
async def get_astrophysics_applications():
    """Get astrophysics applications and use cases"""
    return {
        "applications": {
            "black_hole_physics": {
                "name": "Black Hole Physics",
                "description": "Modeling spacetime around black holes and gravitational effects",
                "equations": ["schwarzschild_metric", "kerr_metric", "reissner_nordstrom"],
                "challenges": ["Singularities", "Event horizons", "Gravitational waves"]
            },
            "cosmology": {
                "name": "Cosmology",
                "description": "Large-scale structure of the universe and cosmic evolution",
                "equations": ["friedmann_equations", "cosmological_constant", "dark_energy"],
                "challenges": ["Dark matter", "Dark energy", "Cosmic inflation"]
            },
            "stellar_evolution": {
                "name": "Stellar Evolution",
                "description": "Star formation, evolution, and stellar structure",
                "equations": ["stellar_structure", "nuclear_fusion", "stellar_wind"],
                "challenges": ["Nuclear reactions", "Convection", "Mass loss"]
            },
            "galaxy_formation": {
                "name": "Galaxy Formation",
                "description": "Formation and evolution of galaxies and galactic dynamics",
                "equations": ["galactic_dynamics", "dark_matter_halo", "merger_trees"],
                "challenges": ["Dark matter distribution", "Galactic mergers", "Star formation"]
            },
            "gravitational_waves": {
                "name": "Gravitational Waves",
                "description": "Detection and analysis of gravitational wave signals",
                "equations": ["einstein_equations", "wave_propagation", "binary_merger"],
                "challenges": ["Signal detection", "Noise filtering", "Source localization"]
            }
        },
        "purpose": "astrophysics"
    } 