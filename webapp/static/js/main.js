// Main JavaScript for PINN Dashboard

document.addEventListener('DOMContentLoaded', function() {
    // Initialize dashboard
    initializeDashboard();
    
    // Add event listeners
    addEventListeners();
});

function initializeDashboard() {
    console.log('PINN Dashboard initialized');
    
    // Add loading states to equation cards
    const equationCards = document.querySelectorAll('.equation-card');
    equationCards.forEach(card => {
        card.addEventListener('click', function(e) {
            if (e.target.tagName === 'A') {
                addLoadingState(card);
            }
        });
    });
}

function addEventListeners() {
    // Add smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Add tooltip initialization
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
}

function addLoadingState(element) {
    element.classList.add('loading');
    element.style.cursor = 'wait';
    
    // Remove loading state after navigation
    setTimeout(() => {
        element.classList.remove('loading');
        element.style.cursor = 'pointer';
    }, 2000);
}

// API Functions
async function simulateEquation(equationType, parameters) {
    try {
        const response = await fetch(`/api/simulate/${equationType}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(parameters)
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        return await response.json();
    } catch (error) {
        console.error('Simulation error:', error);
        throw error;
    }
}

async function getResults(equationType) {
    try {
        const response = await fetch(`/api/results/${equationType}`);
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        return await response.json();
    } catch (error) {
        console.error('Results fetch error:', error);
        throw error;
    }
}

// Utility Functions
function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
    notification.style.cssText = `
        top: 20px;
        right: 20px;
        z-index: 9999;
        min-width: 300px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    `;
    
    notification.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    document.body.appendChild(notification);
    
    // Auto remove after 5 seconds
    setTimeout(() => {
        if (notification.parentNode) {
            notification.remove();
        }
    }, 5000);
}

function formatNumber(num, decimals = 4) {
    return Number(num).toFixed(decimals);
}

function validateParameters(parameters, equationType) {
    const errors = [];
    
    // Common validations
    for (const [key, value] of Object.entries(parameters)) {
        if (value === null || value === undefined || value === '') {
            errors.push(`${key} is required`);
        }
        
        if (typeof value === 'number' && (isNaN(value) || !isFinite(value))) {
            errors.push(`${key} must be a valid number`);
        }
    }
    
    // Equation-specific validations
    switch (equationType) {
        case 'burgers':
        case 'heat':
        case 'wave':
            if (parameters.x_min >= parameters.x_max) {
                errors.push('x_min must be less than x_max');
            }
            if (parameters.t_min >= parameters.t_max) {
                errors.push('t_min must be less than t_max');
            }
            if (parameters.nx <= 0 || parameters.nt <= 0) {
                errors.push('nx and nt must be positive integers');
            }
            break;
            
        case 'shm':
            if (parameters.t_min >= parameters.t_max) {
                errors.push('t_min must be less than t_max');
            }
            if (parameters.omega <= 0) {
                errors.push('omega must be positive');
            }
            break;
            
        case 'helmholtz':
            if (parameters.x_min >= parameters.x_max) {
                errors.push('x_min must be less than x_max');
            }
            if (parameters.y_min >= parameters.y_max) {
                errors.push('y_min must be less than y_max');
            }
            if (parameters.nx <= 0 || parameters.ny <= 0) {
                errors.push('nx and ny must be positive integers');
            }
            break;
    }
    
    return errors;
}

// Chart Functions
function createLineChart(containerId, data, layout = {}) {
    const defaultLayout = {
        title: 'Simulation Results',
        xaxis: { title: 'X' },
        yaxis: { title: 'Y' },
        showlegend: true,
        hovermode: 'closest'
    };
    
    const finalLayout = { ...defaultLayout, ...layout };
    
    Plotly.newPlot(containerId, data, finalLayout, {
        responsive: true,
        displayModeBar: true,
        modeBarButtonsToRemove: ['pan2d', 'lasso2d', 'select2d']
    });
}

function createSurfacePlot(containerId, data, layout = {}) {
    const defaultLayout = {
        title: '3D Solution Surface',
        scene: {
            xaxis: { title: 'X' },
            yaxis: { title: 'Y' },
            zaxis: { title: 'Z' }
        },
        showlegend: false
    };
    
    const finalLayout = { ...defaultLayout, ...layout };
    
    Plotly.newPlot(containerId, data, finalLayout, {
        responsive: true,
        displayModeBar: true
    });
}

// Export functions for use in other modules
window.PINNUtils = {
    simulateEquation,
    getResults,
    showNotification,
    formatNumber,
    validateParameters,
    createLineChart,
    createSurfacePlot
}; 