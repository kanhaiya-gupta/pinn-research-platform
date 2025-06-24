from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pathlib import Path
import httpx
import json
from config import Config

# Import purpose-specific routers
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
    """Main dashboard page"""
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "equations": config.SUPPORTED_EQUATIONS,
            "config": config,  # Pass entire config to access PINN_PURPOSES
            "title": "PINN Dashboard"
        }
    )

# Legacy equation-based routes (for backward compatibility)
@app.get("/equation/{eq_type}", response_class=HTMLResponse)
async def equation_page(request: Request, eq_type: str):
    """Individual equation page (legacy route)"""
    if eq_type not in config.SUPPORTED_EQUATIONS:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    equation_info = config.SUPPORTED_EQUATIONS[eq_type]
    default_params = config.DEFAULT_PARAMETERS.get(eq_type, {})
    
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
    default_params = config.DEFAULT_PARAMETERS.get(eq_type, {})
    
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
@app.post("/api/simulate/{eq_type}")
async def simulate_equation(eq_type: str, request: Request):
    """Submit training request to main.py backend"""
    if eq_type not in config.SUPPORTED_EQUATIONS:
        raise HTTPException(status_code=404, detail="Equation not found")
    
    try:
        body = await request.json()
        
        # Map frontend parameters to backend format
        backend_params = map_parameters_to_backend(eq_type, body)
        
        async with httpx.AsyncClient() as client:
            # Call the main.py backend API using /train endpoint
            response = await client.post(
                f"{config.API_BASE_URL}/api/{eq_type}/train",
                json=backend_params,
                timeout=300.0  # 5 minutes timeout for training
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

@app.post("/api/predict/{eq_type}")
async def predict_equation(eq_type: str, request: Request):
    """Make predictions using trained model"""
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

@app.get("/api/results/{eq_type}")
async def get_results(eq_type: str):
    """Get training results and model status"""
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

def map_parameters_to_backend(eq_type: str, frontend_params: dict) -> dict:
    """Map frontend parameters to backend API format"""
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
