// Simulation JavaScript for PINN Frontend

class SimulationManager {
    constructor() {
        this.isRunning = false;
        this.startTime = null;
        this.progressInterval = null;
    }

    async startSimulation(equationType, parameters) {
        if (this.isRunning) {
            PINNUtils.showNotification('Simulation already running', 'warning');
            return;
        }

        this.isRunning = true;
        this.startTime = Date.now();
        
        // Show progress panel
        this.showProgressPanel();
        
        // Start progress updates
        this.startProgressUpdates();
        
        try {
            // Call the simulation API
            const result = await PINNUtils.simulateEquation(equationType, parameters);
            
            // Update progress to 100%
            this.updateProgress(100, 'Simulation completed');
            
            PINNUtils.showNotification('Simulation completed successfully!', 'success');
            
            // Redirect to results after a short delay
            setTimeout(() => {
                window.location.href = `/results/${equationType}`;
            }, 2000);
            
        } catch (error) {
            PINNUtils.showNotification('Simulation failed: ' + error.message, 'danger');
            this.stopSimulation();
        }
    }

    stopSimulation() {
        this.isRunning = false;
        this.hideProgressPanel();
        this.stopProgressUpdates();
    }

    showProgressPanel() {
        const progressPanel = document.getElementById('progressPanel');
        const statusPanel = document.getElementById('simulationStatus');
        
        if (progressPanel) {
            progressPanel.style.display = 'block';
        }
        
        if (statusPanel) {
            statusPanel.innerHTML = `
                <div class="status-item">
                    <i class="fas fa-spinner fa-spin text-primary"></i>
                    <span>Simulation running...</span>
                </div>
            `;
        }
    }

    hideProgressPanel() {
        const progressPanel = document.getElementById('progressPanel');
        const statusPanel = document.getElementById('simulationStatus');
        
        if (progressPanel) {
            progressPanel.style.display = 'none';
        }
        
        if (statusPanel) {
            statusPanel.innerHTML = `
                <div class="status-item">
                    <i class="fas fa-circle text-muted"></i>
                    <span>Ready to run</span>
                </div>
            `;
        }
    }

    startProgressUpdates() {
        this.progressInterval = setInterval(() => {
            if (this.isRunning) {
                // Simulate progress updates (in real implementation, this would come from the backend)
                const elapsed = Date.now() - this.startTime;
                const progress = Math.min((elapsed / 30000) * 100, 95); // Simulate 30 second simulation
                
                this.updateProgress(progress, `Training... (${Math.floor(elapsed / 1000)}s)`);
            }
        }, 1000);
    }

    stopProgressUpdates() {
        if (this.progressInterval) {
            clearInterval(this.progressInterval);
            this.progressInterval = null;
        }
    }

    updateProgress(percentage, status) {
        const progressBar = document.getElementById('progressBar');
        const currentEpoch = document.getElementById('currentEpoch');
        const currentLoss = document.getElementById('currentLoss');
        const elapsedTime = document.getElementById('elapsedTime');
        
        if (progressBar) {
            progressBar.style.width = `${percentage}%`;
            progressBar.setAttribute('aria-valuenow', percentage);
        }
        
        if (currentEpoch) {
            currentEpoch.textContent = Math.floor(percentage * 100); // Simulate epoch count
        }
        
        if (currentLoss) {
            currentLoss.textContent = (Math.random() * 0.1).toFixed(6); // Simulate loss
        }
        
        if (elapsedTime && this.startTime) {
            const elapsed = Math.floor((Date.now() - this.startTime) / 1000);
            const minutes = Math.floor(elapsed / 60);
            const seconds = elapsed % 60;
            elapsedTime.textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
        }
    }
}

// Form validation functions
function validateBurgersParameters(parameters) {
    const errors = [];
    
    if (parameters.nu <= 0 || parameters.nu > 1) {
        errors.push('Viscosity coefficient must be between 0 and 1');
    }
    
    if (parameters.x_min >= parameters.x_max) {
        errors.push('Minimum x value must be less than maximum x value');
    }
    
    if (parameters.t_min >= parameters.t_max) {
        errors.push('Minimum time value must be less than maximum time value');
    }
    
    if (parameters.nx < 50 || parameters.nx > 1000) {
        errors.push('Number of spatial points must be between 50 and 1000');
    }
    
    if (parameters.nt < 50 || parameters.nt > 500) {
        errors.push('Number of time points must be between 50 and 500');
    }
    
    return errors;
}

function validateHeatParameters(parameters) {
    const errors = [];
    
    if (parameters.alpha <= 0) {
        errors.push('Thermal diffusivity must be positive');
    }
    
    if (parameters.x_min >= parameters.x_max) {
        errors.push('Minimum x value must be less than maximum x value');
    }
    
    if (parameters.t_min >= parameters.t_max) {
        errors.push('Minimum time value must be less than maximum time value');
    }
    
    if (parameters.nx < 50 || parameters.nx > 1000) {
        errors.push('Number of spatial points must be between 50 and 1000');
    }
    
    if (parameters.nt < 50 || parameters.nt > 500) {
        errors.push('Number of time points must be between 50 and 500');
    }
    
    return errors;
}

function validateWaveParameters(parameters) {
    const errors = [];
    
    if (parameters.c <= 0) {
        errors.push('Wave speed must be positive');
    }
    
    if (parameters.x_min >= parameters.x_max) {
        errors.push('Minimum x value must be less than maximum x value');
    }
    
    if (parameters.t_min >= parameters.t_max) {
        errors.push('Minimum time value must be less than maximum time value');
    }
    
    if (parameters.nx < 50 || parameters.nx > 1000) {
        errors.push('Number of spatial points must be between 50 and 1000');
    }
    
    if (parameters.nt < 50 || parameters.nt > 500) {
        errors.push('Number of time points must be between 50 and 500');
    }
    
    return errors;
}

function validateSHMParameters(parameters) {
    const errors = [];
    
    if (parameters.omega <= 0) {
        errors.push('Angular frequency must be positive');
    }
    
    if (parameters.t_min >= parameters.t_max) {
        errors.push('Minimum time value must be less than maximum time value');
    }
    
    if (parameters.nt < 100 || parameters.nt > 5000) {
        errors.push('Number of time points must be between 100 and 5000');
    }
    
    return errors;
}

function validateHelmholtzParameters(parameters) {
    const errors = [];
    
    if (parameters.k <= 0) {
        errors.push('Wavenumber must be positive');
    }
    
    if (parameters.x_min >= parameters.x_max) {
        errors.push('Minimum x value must be less than maximum x value');
    }
    
    if (parameters.y_min >= parameters.y_max) {
        errors.push('Minimum y value must be less than maximum y value');
    }
    
    if (parameters.nx < 20 || parameters.nx > 200) {
        errors.push('Number of x points must be between 20 and 200');
    }
    
    if (parameters.ny < 20 || parameters.ny > 200) {
        errors.push('Number of y points must be between 20 and 200');
    }
    
    return errors;
}

// Export for global use
window.SimulationManager = SimulationManager;
window.validateBurgersParameters = validateBurgersParameters;
window.validateHeatParameters = validateHeatParameters;
window.validateWaveParameters = validateWaveParameters;
window.validateSHMParameters = validateSHMParameters;
window.validateHelmholtzParameters = validateHelmholtzParameters; 