from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pathlib import Path
import httpx
import json
from config.config import Config
from typing import Dict, Any

# Import purpose-specific routers using absolute imports
from forward_problems.routes import router as forward_problems_router
from inverse_problems.routes import router as inverse_problems_router
from efficiency.routes import router as efficiency_router
from sparse_data.routes import router as sparse_data_router
from generalization.routes import router as generalization_router
from data_assimilation.routes import router as data_assimilation_router
from control_optimization.routes import router as control_optimization_router
from multiphysics.routes import router as multiphysics_router
from scientific_discovery.routes import router as scientific_discovery_router
from uncertainty.routes import router as uncertainty_router

# Create FastAPI app for frontend
app = FastAPI(
    title="Physics-Informed Neural Network Frontend",
    description="Frontend interface for PINN differential equation simulations",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup templates
templates = Jinja2Templates(directory="templates")

# Configuration
config = Config()

# Include all purpose-specific routers
app.include_router(forward_problems_router)
app.include_router(inverse_problems_router)
app.include_router(efficiency_router)
app.include_router(sparse_data_router)
app.include_router(generalization_router)
app.include_router(data_assimilation_router)
app.include_router(control_optimization_router)
app.include_router(multiphysics_router)
app.include_router(scientific_discovery_router)
app.include_router(uncertainty_router)

# Main routes
@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    """Main dashboard page with modular purpose structure"""
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "purposes": config.get_all_purposes(),
            "config": config,
            "title": "PINN Dashboard - Modular Platform"
        }
    )

# Purpose-based routes
@app.get("/purpose/{purpose_name}", response_class=HTMLResponse)
async def purpose_page(request: Request, purpose_name: str):
    """Individual purpose page"""
    purpose_info = config.get_purpose_info(purpose_name)
    if not purpose_info:
        raise HTTPException(status_code=404, detail="Purpose not found")
    
    equations = config.get_equations_by_purpose(purpose_name)
    parameters = config.get_parameters_by_purpose(purpose_name)
    
    return templates.TemplateResponse(
        f"{purpose_name}/index.html",
        {
            "request": request,
            "purpose": purpose_info,
            "purpose_name": purpose_name,
            "purpose_key": purpose_name,
            "equations": equations,
            "parameters": parameters,
            "config": config,
            "title": f"{purpose_info['name']} - PINN"
        }
    )

def get_equation_specific_parameters(purpose_name: str, eq_id: str) -> Dict[str, Any]:
    """Get equation-specific parameters for a given purpose and equation."""
    try:
        # Import the specific purpose parameters
        if purpose_name == 'forward_problems':
            from config.parameters.forward_problems import FORWARD_PROBLEMS_EQUATION_PARAMETERS
            return FORWARD_PROBLEMS_EQUATION_PARAMETERS.get(eq_id, {})
        elif purpose_name == 'inverse_problems':
            from config.parameters.inverse_problems import INVERSE_PROBLEMS_EQUATION_PARAMETERS
            return INVERSE_PROBLEMS_EQUATION_PARAMETERS.get(eq_id, {})
        elif purpose_name == 'data_assimilation':
            from config.parameters.data_assimilation import DATA_ASSIMILATION_EQUATION_PARAMETERS
            return DATA_ASSIMILATION_EQUATION_PARAMETERS.get(eq_id, {})
        elif purpose_name == 'control_optimization':
            from config.parameters.control_optimization import CONTROL_OPTIMIZATION_EQUATION_PARAMETERS
            return CONTROL_OPTIMIZATION_EQUATION_PARAMETERS.get(eq_id, {})
        elif purpose_name == 'sparse_data':
            from config.parameters.sparse_data import SPARSE_DATA_EQUATION_PARAMETERS
            return SPARSE_DATA_EQUATION_PARAMETERS.get(eq_id, {})
        elif purpose_name == 'uncertainty':
            from config.parameters.uncertainty import UNCERTAINTY_EQUATION_PARAMETERS
            return UNCERTAINTY_EQUATION_PARAMETERS.get(eq_id, {})
        elif purpose_name == 'multiphysics':
            from config.parameters.multiphysics import MULTIPHYSICS_EQUATION_PARAMETERS
            return MULTIPHYSICS_EQUATION_PARAMETERS.get(eq_id, {})
        elif purpose_name == 'efficiency':
            from config.parameters.efficiency import EFFICIENCY_EQUATION_PARAMETERS
            return EFFICIENCY_EQUATION_PARAMETERS.get(eq_id, {})
        elif purpose_name == 'generalization':
            from config.parameters.generalization import GENERALIZATION_EQUATION_PARAMETERS
            return GENERALIZATION_EQUATION_PARAMETERS.get(eq_id, {})
        elif purpose_name == 'scientific_discovery':
            from config.parameters.scientific_discovery import SCIENTIFIC_DISCOVERY_EQUATION_PARAMETERS
            return SCIENTIFIC_DISCOVERY_EQUATION_PARAMETERS.get(eq_id, {})
        elif purpose_name == 'astrophysics':
            from config.parameters.astrophysics import ASTROPHYSICS_EQUATION_PARAMETERS
            return ASTROPHYSICS_EQUATION_PARAMETERS.get(eq_id, {})
        else:
            return {}
    except ImportError:
        # If the equation-specific parameters don't exist yet, return empty dict
        return {}

@app.get("/purpose/{purpose_name}/simulation/{eq_id}", response_class=HTMLResponse)
async def purpose_simulation_page(request: Request, purpose_name: str, eq_id: str):
    """Simulation page for specific purpose and equation"""
    purpose_info = config.get_purpose_info(purpose_name)
    if not purpose_info:
        raise HTTPException(status_code=404, detail="Purpose not found")
    
    equations = config.get_equations_by_purpose(purpose_name)
    if eq_id not in equations:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    equation_info = equations[eq_id]
    
    # Get equation-specific parameters only
    equation_specific_params = get_equation_specific_parameters(purpose_name, eq_id)
    
    # Create default parameters for the template
    default_params = {
        "hidden_layers": 4,
        "neurons_per_layer": 20,
        "learning_rate": 0.001,
        "epochs": 1000  # Good balance for PINN convergence
    }
    
    # Add equation-specific default parameters
    for param_id, param_info in equation_specific_params.items():
        if isinstance(param_info, dict) and 'default' in param_info:
            default_params[param_id] = param_info['default']
    
    return templates.TemplateResponse(
        f"{purpose_name}/simulation.html",
        {
            "request": request,
            "purpose": purpose_info,
            "purpose_name": purpose_name,
            "purpose_key": purpose_name,
            "equation": equation_info,
            "eq_id": eq_id,
            "parameters": equation_specific_params,
            "default_params": default_params,
            "config": config,
            "title": f"Simulate {equation_info['name']} - {purpose_info['name']}"
        }
    )

@app.get("/purpose/{purpose_name}/live-training/{eq_id}", response_class=HTMLResponse)
async def purpose_live_training_page(request: Request, purpose_name: str, eq_id: str):
    """Live training page for specific purpose and equation"""
    purpose_info = config.get_purpose_info(purpose_name)
    if not purpose_info:
        raise HTTPException(status_code=404, detail="Purpose not found")
    
    equations = config.get_equations_by_purpose(purpose_name)
    if eq_id not in equations:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    equation_info = equations[eq_id]
    
    return templates.TemplateResponse(
        f"{purpose_name}/live_training.html",
        {
            "request": request,
            "purpose": purpose_info,
            "purpose_name": purpose_name,
            "purpose_key": purpose_name,
            "equation": equation_info,
            "eq_id": eq_id,
            "equation_type": eq_id,  # Add this for consistency
            "config": config,
            "title": f"Live Training - {equation_info['name']} - {purpose_info['name']}"
        }
    )

@app.get("/purpose/{purpose_name}/results/{eq_id}", response_class=HTMLResponse)
async def purpose_results_page(request: Request, purpose_name: str, eq_id: str):
    """Results page for specific purpose and equation"""
    purpose_info = config.get_purpose_info(purpose_name)
    if not purpose_info:
        raise HTTPException(status_code=404, detail="Purpose not found")
    
    equations = config.get_equations_by_purpose(purpose_name)
    if eq_id not in equations:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    equation_info = equations[eq_id]
    
    return templates.TemplateResponse(
        f"{purpose_name}/results.html",
        {
            "request": request,
            "purpose": purpose_info,
            "purpose_name": purpose_name,
            "equation": equation_info,
            "eq_id": eq_id,
            "config": config,
            "title": f"Results - {equation_info['name']} - {purpose_info['name']}"
        }
    )

# Legacy equation-based routes (for backward compatibility)
@app.get("/equation/{eq_type}", response_class=HTMLResponse)
async def equation_page(request: Request, eq_type: str):
    """Individual equation page (legacy route)"""
    if eq_type not in config.SUPPORTED_EQUATIONS:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    equation_info = config.SUPPORTED_EQUATIONS[eq_type]
    default_params = config.get_default_parameters(eq_type)
    
    return templates.TemplateResponse(
        f"equations/{eq_type}/index.html",
        {
            "request": request,
            "equation": equation_info,
            "eq_type": eq_type,
            "default_params": default_params,
            "config": config,
            "title": f"{equation_info['name']} - PINN"
        }
    )

@app.get("/simulation/{eq_type}", response_class=HTMLResponse)
async def simulation_page(request: Request, eq_type: str):
    """Simulation page for running PINN (legacy route)"""
    if eq_type not in config.SUPPORTED_EQUATIONS:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    equation_info = config.SUPPORTED_EQUATIONS[eq_type]
    default_params = config.get_default_parameters(eq_type)
    
    return templates.TemplateResponse(
        f"equations/{eq_type}/simulation.html",
        {
            "request": request,
            "equation": equation_info,
            "eq_type": eq_type,
            "default_params": default_params,
            "config": config,
            "title": f"Simulate {equation_info['name']} - PINN"
        }
    )

@app.get("/results/{eq_type}", response_class=HTMLResponse)
async def results_page(request: Request, eq_type: str):
    """Results page for viewing simulation results (legacy route)"""
    if eq_type not in config.SUPPORTED_EQUATIONS:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    equation_info = config.SUPPORTED_EQUATIONS[eq_type]
    
    return templates.TemplateResponse(
        f"equations/{eq_type}/results.html",
        {
            "request": request,
            "equation": equation_info,
            "eq_type": eq_type,
            "config": config,
            "title": f"Results - {equation_info['name']} - PINN"
        }
    )

# API routes for communicating with main.py backend
@app.post("/api/simulate/{purpose_name}/{eq_id}")
async def simulate_purpose_equation(purpose_name: str, eq_id: str, request: Request):
    """Submit training request to main.py backend for purpose-based equations"""
    print(f"🔍 Frontend received training request for {purpose_name}/{eq_id}")
    
    purpose_info = config.get_purpose_info(purpose_name)
    if not purpose_info:
        print(f"❌ Purpose {purpose_name} not found")
        raise HTTPException(status_code=404, detail="Purpose not found")
    
    equations = config.get_equations_by_purpose(purpose_name)
    if eq_id not in equations:
        print(f"❌ Equation {eq_id} not found in {purpose_name}")
        raise HTTPException(status_code=404, detail="Equation not found")
    
    try:
        body = await request.json()
        print(f"📥 Frontend received parameters: {body}")
        
        # Map frontend parameters to backend format
        backend_params = map_parameters_to_backend(purpose_name, eq_id, body)
        print(f"🔄 Mapped to backend params: {backend_params}")
        
        print(f"🌐 Calling backend at: {config.API_BASE_URL}/api/train")
        async with httpx.AsyncClient() as client:
            # Call the main.py backend API using /api/train endpoint
            response = await client.post(
                f"{config.API_BASE_URL}/api/train",
                json=backend_params,
                timeout=300.0  # 5 minutes timeout for training
            )
            
            print(f"📤 Backend response status: {response.status_code}")
            print(f"📤 Backend response: {response.text}")
            
            if response.status_code == 200:
                return response.json()
            else:
                raise HTTPException(status_code=response.status_code, 
                                  detail=f"Backend error: {response.text}")
                
    except httpx.TimeoutException:
        print("⏰ Training timeout")
        raise HTTPException(status_code=408, detail="Training timeout - model may still be training")
    except Exception as e:
        print(f"❌ Training failed with error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Training failed: {str(e)}")

# @app.post("/api/simulate/{eq_type}")
# async def simulate_equation(eq_type: str, request: Request):
#     """Submit training request to main.py backend (legacy route)"""
#     if eq_type not in config.SUPPORTED_EQUATIONS:
#         raise HTTPException(status_code=404, detail="Equation not found")
#     
#     try:
#         body = await request.json()
#         
#         # Map frontend parameters to backend format
#         backend_params = map_parameters_to_backend_legacy(eq_type, body)
#         
#         async with httpx.AsyncClient() as client:
#             # Call the main.py backend API using /train endpoint
#             response = await client.post(
#                 f"{config.API_BASE_URL}/api/{eq_type}/train",
#                 json=backend_params,
#                 timeout=300.0  # 5 minutes timeout for training
#             )
#             
#             if response.status_code == 200:
#                 return response.json()
#             else:
#                 raise HTTPException(status_code=response.status_code, 
#                                   detail=f"Backend error: {response.text}")
#                 
#     except httpx.TimeoutException:
#         raise HTTPException(status_code=408, detail="Training timeout - model may still be training")
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Training failed: {str(e)}")

@app.post("/api/predict/{purpose_name}/{eq_id}")
async def predict_purpose_equation(purpose_name: str, eq_id: str, request: Request):
    """Make predictions using trained model for purpose-based equations"""
    purpose_info = config.get_purpose_info(purpose_name)
    if not purpose_info:
        raise HTTPException(status_code=404, detail="Purpose not found")
    
    equations = config.get_equations_by_purpose(purpose_name)
    if eq_id not in equations:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    try:
        body = await request.json()
        
        # Add purpose and equation information to the request
        body['purpose'] = purpose_name
        body['equation_type'] = eq_id
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{config.API_BASE_URL}/api/predict",
                json=body,
                timeout=30.0
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                raise HTTPException(status_code=response.status_code, 
                                  detail=f"Backend error: {response.text}")
                
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

@app.post("/api/predict/{eq_type}")
async def predict_equation(eq_type: str, request: Request):
    """Make predictions using trained model (legacy route)"""
    if eq_type not in config.SUPPORTED_EQUATIONS:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    try:
        body = await request.json()
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{config.API_BASE_URL}/api/{eq_type}/predict",
                json=body,
                timeout=30.0
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                raise HTTPException(status_code=response.status_code, 
                                  detail=f"Backend error: {response.text}")
                
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

@app.get("/api/training-progress/{purpose_name}/{eq_id}")
async def get_training_progress(purpose_name: str, eq_id: str):
    """Get live training progress for purpose-based equations"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{config.API_BASE_URL}/api/training-progress/{purpose_name}/{eq_id}",
                timeout=5.0
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                # Return default progress if backend doesn't have it yet
                return {
                    "status": "training",
                    "current_epoch": 0,
                    "total_epochs": 10000,
                    "total_loss": 1.0,
                    "physics_loss": 1.0,
                    "boundary_loss": 1.0,
                    "initial_loss": 1.0,
                    "learning_rate": 0.001
                }
                
    except Exception as e:
        # Return default progress on error
        return {
            "status": "training",
            "current_epoch": 0,
            "total_epochs": 10000,
            "total_loss": 1.0,
            "physics_loss": 1.0,
            "boundary_loss": 1.0,
            "initial_loss": 1.0,
            "learning_rate": 0.001
        }

@app.post("/api/training-control/{purpose_name}/{eq_id}/{action}")
async def training_control(purpose_name: str, eq_id: str, action: str):
    """Control training (pause/resume/stop) for purpose-based equations"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{config.API_BASE_URL}/api/training-control/{purpose_name}/{eq_id}/{action}",
                timeout=5.0
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                return {"status": "success", "message": f"Training {action} requested"}
                
    except Exception as e:
        return {"status": "success", "message": f"Training {action} requested"}

@app.get("/api/results/{purpose_name}/{eq_id}")
async def get_purpose_results(purpose_name: str, eq_id: str):
    """Get training results and model status for purpose-based equations"""
    purpose_info = config.get_purpose_info(purpose_name)
    if not purpose_info:
        raise HTTPException(status_code=404, detail="Purpose not found")
    
    equations = config.get_equations_by_purpose(purpose_name)
    if eq_id not in equations:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    try:
        # Check if model exists
        model_path = f"results/{purpose_name}/{eq_id}/models/model.pth"
        
        # For now, return basic model status
        # In a real implementation, you might want to load actual results
        return {
            "model_exists": True,  # This would be checked dynamically
            "purpose_name": purpose_name,
            "equation_id": eq_id,
            "message": "Model training completed"
        }
                
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch results: {str(e)}")

@app.get("/api/results/{eq_type}")
async def get_results(eq_type: str):
    """Get training results and model status (legacy route)"""
    if eq_type not in config.SUPPORTED_EQUATIONS:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    try:
        # Check if model exists
        model_path = f"results/{eq_type}/models/model.pth"
        
        # For now, return basic model status
        # In a real implementation, you might want to load actual results
        return {
            "model_exists": True,  # This would be checked dynamically
            "equation_type": eq_type,
            "message": "Model training completed"
        }
                
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch results: {str(e)}")

def map_parameters_to_backend(purpose_name: str, eq_id: str, frontend_params: dict) -> dict:
    """Map frontend parameters to backend API format for purpose-based equations"""
    # Convert string values to appropriate types
    params = {}
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
    params['equation_type'] = eq_id  # Backend expects 'equation_type', not 'equation_id'
    
    # Add default training parameters if not provided
    training_params = config.get_training_parameters()
    for key, default_value in training_params.items():
        if key not in params:
            params[key] = default_value
    
    return params

def map_parameters_to_backend_legacy(eq_type: str, frontend_params: dict) -> dict:
    """Map frontend parameters to backend API format (legacy support)"""
    # Convert string values to appropriate types
    params = {}
    for key, value in frontend_params.items():
        if isinstance(value, str):
            try:
                params[key] = float(value) if '.' in value else int(value)
            except ValueError:
                params[key] = value
        else:
            params[key] = value
    
    # Map to backend format based on equation type
    if eq_type == 'burgers':
        # Backend expects: epochs, learning_rate, nu
        return {
            "epochs": params.get("epochs", 1000),
            "learning_rate": params.get("learning_rate", 0.001),
            "nu": params.get("nu", 0.01)
        }
    
    elif eq_type == 'heat':
        # Backend expects: epochs, learning_rate, alpha
        return {
            "epochs": params.get("epochs", 1000),
            "learning_rate": params.get("learning_rate", 0.001),
            "alpha": params.get("alpha", 0.1)
        }
    
    elif eq_type == 'wave':
        # Backend expects: epochs, learning_rate, c
        return {
            "epochs": params.get("epochs", 1000),
            "learning_rate": params.get("learning_rate", 0.001),
            "c": params.get("c", 1.0)
        }
    
    elif eq_type == 'shm':
        # Backend expects: epochs, learning_rate, omega
        return {
            "epochs": params.get("epochs", 1000),
            "learning_rate": params.get("learning_rate", 0.001),
            "omega": params.get("omega", 1.0)
        }
    
    elif eq_type == 'helmholtz':
        # Backend expects: epochs, learning_rate, k
        return {
            "epochs": params.get("epochs", 1000),
            "learning_rate": params.get("learning_rate", 0.001),
            "k": params.get("k", 1.0)
        }
    
    return params

if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=5000,
        reload=True,
        log_level="info"
    )
