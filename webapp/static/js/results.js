// Results Page JavaScript for PINN Frontend

document.addEventListener('DOMContentLoaded', function() {
    console.log('Results page loaded');
    
    // Initialize results page features
    initializeResultsPage();
});

function initializeResultsPage() {
    // Add smooth scrolling for anchor links
    initializeSmoothScrolling();
    
    // Add loading animations
    initializeLoadingAnimations();
    
    // Add copy functionality for metrics
    initializeCopyButtons();
}

// Load training results for the specific purpose and equation
function loadResults(purposeKey, equationType) {
    console.log('Loading results for:', purposeKey, equationType);
    
    // Show loading state
    showLoadingState();
    
    // Fetch results from the backend
    fetch(`/purpose/${purposeKey}/api/results/${equationType}`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log('Results loaded:', data);
            displayResults(data);
        })
        .catch(error => {
            console.error('Error loading results:', error);
            showErrorState(error.message);
        });
}

function showLoadingState() {
    // Update summary stats with loading indicators
    const elements = ['final-loss', 'training-time', 'convergence-status'];
    elements.forEach(id => {
        const element = document.getElementById(id);
        if (element) {
            element.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Loading...';
        }
    });
    
    // Show loading spinners in chart containers
    const chartContainers = document.querySelectorAll('.chart-container');
    chartContainers.forEach(container => {
        container.innerHTML = `
            <div class="text-center loading-placeholder">
                <i class="fas fa-spinner fa-spin fa-2x text-primary"></i>
                <p class="mt-2">Loading chart data...</p>
            </div>
        `;
    });
    
    // Update metrics table with loading states
    const metricElements = ['l2-error', 'linf-error', 'relative-error', 'training-time-metric', 'convergence-rate'];
    metricElements.forEach(id => {
        const element = document.getElementById(id);
        if (element) {
            element.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
        }
    });
}

function displayResults(data) {
    // Update summary statistics
    if (data.final_loss !== undefined) {
        updateElement('final-loss', data.final_loss.toFixed(6));
    }
    
    if (data.training_time !== undefined) {
        updateElement('training-time', `${data.training_time.toFixed(2)}s`);
    }
    
    if (data.convergence_status !== undefined) {
        updateElement('convergence-status', data.convergence_status);
    }
    
    // Update metrics table
    if (data.metrics) {
        if (data.metrics.l2_error !== undefined) {
            updateElement('l2-error', data.metrics.l2_error.toFixed(6));
        }
        if (data.metrics.linf_error !== undefined) {
            updateElement('linf-error', data.metrics.linf_error.toFixed(6));
        }
        if (data.metrics.relative_error !== undefined) {
            updateElement('relative-error', `${(data.metrics.relative_error * 100).toFixed(2)}%`);
        }
        if (data.training_time !== undefined) {
            updateElement('training-time-metric', `${data.training_time.toFixed(2)}s`);
        }
        if (data.metrics.convergence_rate !== undefined) {
            updateElement('convergence-rate', data.metrics.convergence_rate.toFixed(4));
        }
    }
    
    // Display charts if data is available
    if (data.loss_history) {
        displayLossChart(data.loss_history);
    }
    
    if (data.solution_data) {
        displaySolutionChart(data.solution_data);
    }
    
    if (data.error_data) {
        displayErrorChart(data.error_data);
    }
    
    if (data.surface_data) {
        displaySurfaceChart(data.surface_data);
    }
    
    // Show success notification
    showNotification('Results loaded successfully!', 'success');
}

function updateElement(elementId, value) {
    const element = document.getElementById(elementId);
    if (element) {
        element.textContent = value;
    }
}

function showErrorState(errorMessage) {
    // Show error message
    showNotification(`Failed to load results: ${errorMessage}`, 'danger');
    
    // Update summary stats with error indicators
    const elements = ['final-loss', 'training-time', 'convergence-status'];
    elements.forEach(id => {
        updateElement(id, 'Error');
    });
    
    // Show error message in chart containers
    const chartContainers = document.querySelectorAll('.chart-container');
    chartContainers.forEach(container => {
        container.innerHTML = `
            <div class="text-center text-danger error-placeholder">
                <i class="fas fa-exclamation-triangle fa-2x"></i>
                <p class="mt-2">Failed to load chart data</p>
                <small class="text-muted">${errorMessage}</small>
            </div>
        `;
    });
    
    // Update metrics table with error states
    const metricElements = ['l2-error', 'linf-error', 'relative-error', 'training-time-metric', 'convergence-rate'];
    metricElements.forEach(id => {
        updateElement(id, 'Error');
    });
}

function displayLossChart(lossHistory) {
    const container = document.getElementById('loss-chart');
    if (!container) return;
    
    // Create a simple chart display - in a real implementation, you'd use Chart.js or similar
    container.innerHTML = `
        <div class="chart-content">
            <div class="chart-header">
                <h5>Training Loss Evolution</h5>
            </div>
            <div class="chart-body">
                <div class="loss-summary">
                    <div class="loss-item">
                        <span class="loss-label">Final Loss:</span>
                        <span class="loss-value">${lossHistory.final_loss?.toFixed(6) || 'N/A'}</span>
                    </div>
                    <div class="loss-item">
                        <span class="loss-label">Total Epochs:</span>
                        <span class="loss-value">${lossHistory.epochs || 'N/A'}</span>
                    </div>
                    <div class="loss-item">
                        <span class="loss-label">Convergence:</span>
                        <span class="loss-value ${lossHistory.converged ? 'text-success' : 'text-warning'}">
                            ${lossHistory.converged ? 'Converged' : 'Not Converged'}
                        </span>
                    </div>
                </div>
                <div class="chart-placeholder">
                    <p><i class="fas fa-chart-line"></i> Loss history visualization would appear here</p>
                    <small class="text-muted">Chart.js or similar library would render the actual plot</small>
                </div>
            </div>
        </div>
    `;
}

function displaySolutionChart(solutionData) {
    const container = document.getElementById('solution-chart');
    if (!container) return;
    
    container.innerHTML = `
        <div class="chart-content">
            <div class="chart-header">
                <h5>Solution Comparison</h5>
            </div>
            <div class="chart-body">
                <div class="solution-summary">
                    <div class="solution-item">
                        <span class="solution-label">PINN Solution:</span>
                        <span class="solution-value text-primary">Generated</span>
                    </div>
                    <div class="solution-item">
                        <span class="solution-label">Reference:</span>
                        <span class="solution-value text-success">Available</span>
                    </div>
                    <div class="solution-item">
                        <span class="solution-label">Domain:</span>
                        <span class="solution-value">${solutionData.domain || 'N/A'}</span>
                    </div>
                </div>
                <div class="chart-placeholder">
                    <p><i class="fas fa-chart-area"></i> Solution comparison plot would appear here</p>
                    <small class="text-muted">Shows PINN vs analytical/numerical solution</small>
                </div>
            </div>
        </div>
    `;
}

function displayErrorChart(errorData) {
    const container = document.getElementById('error-chart');
    if (!container) return;
    
    container.innerHTML = `
        <div class="chart-content">
            <div class="chart-header">
                <h5>Error Analysis</h5>
            </div>
            <div class="chart-body">
                <div class="error-summary">
                    <div class="error-item">
                        <span class="error-label">Max Error:</span>
                        <span class="error-value">${errorData.max_error?.toFixed(6) || 'N/A'}</span>
                    </div>
                    <div class="error-item">
                        <span class="error-label">Mean Error:</span>
                        <span class="error-value">${errorData.mean_error?.toFixed(6) || 'N/A'}</span>
                    </div>
                    <div class="error-item">
                        <span class="error-label">Error Type:</span>
                        <span class="error-value">${errorData.error_type || 'Absolute'}</span>
                    </div>
                </div>
                <div class="chart-placeholder">
                    <p><i class="fas fa-exclamation-triangle"></i> Error distribution plot would appear here</p>
                    <small class="text-muted">Shows point-wise error distribution</small>
                </div>
            </div>
        </div>
    `;
}

function displaySurfaceChart(surfaceData) {
    const container = document.getElementById('surface-chart');
    if (!container) return;
    
    container.innerHTML = `
        <div class="chart-content">
            <div class="chart-header">
                <h5>Solution Surface</h5>
            </div>
            <div class="chart-body">
                <div class="surface-summary">
                    <div class="surface-item">
                        <span class="surface-label">Dimensions:</span>
                        <span class="surface-value">${surfaceData.dimensions || '2D'}</span>
                    </div>
                    <div class="surface-item">
                        <span class="surface-label">Points:</span>
                        <span class="surface-value">${surfaceData.points || 'N/A'}</span>
                    </div>
                    <div class="surface-item">
                        <span class="surface-label">Range:</span>
                        <span class="surface-value">${surfaceData.range || 'N/A'}</span>
                    </div>
                </div>
                <div class="chart-placeholder">
                    <p><i class="fas fa-cube"></i> 3D surface visualization would appear here</p>
                    <small class="text-muted">Interactive 3D plot of solution surface</small>
                </div>
            </div>
        </div>
    `;
}

// Utility functions
function initializeSmoothScrolling() {
    const links = document.querySelectorAll('a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

function initializeLoadingAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
            }
        });
    }, observerOptions);
    
    // Observe all sections
    const sections = document.querySelectorAll('.results-summary, .results-visualization, .metrics-section, .analysis-section');
    sections.forEach(section => {
        observer.observe(section);
    });
}

function initializeCopyButtons() {
    const metricCells = document.querySelectorAll('.metrics-table td');
    
    metricCells.forEach(cell => {
        if (cell.textContent !== '-' && cell.textContent !== 'Error') {
            cell.style.cursor = 'pointer';
            cell.title = 'Click to copy value';
            
            cell.addEventListener('click', function() {
                const text = this.textContent;
                
                navigator.clipboard.writeText(text).then(() => {
                    showNotification('Value copied to clipboard!', 'success');
                }).catch(() => {
                    showNotification('Failed to copy value', 'warning');
                });
            });
        }
    });
}

function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
    notification.style.cssText = 'top: 20px; right: 20px; z-index: 9999; min-width: 300px;';
    notification.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    document.body.appendChild(notification);
    
    // Auto-dismiss after 5 seconds
    setTimeout(() => {
        if (notification.parentNode) {
            notification.remove();
        }
    }, 5000);
}

// Download results functionality
function downloadResults() {
    const purposeKey = window.purposeKey || 'forward_problems';
    const equationType = window.equationType || 'burgers';
    
    // Create a comprehensive results summary
    const results = {
        purpose: purposeKey,
        equation: equationType,
        timestamp: new Date().toISOString(),
        summary: {
            final_loss: document.getElementById('final-loss')?.textContent || 'N/A',
            training_time: document.getElementById('training-time')?.textContent || 'N/A',
            convergence_status: document.getElementById('convergence-status')?.textContent || 'N/A'
        },
        metrics: {
            l2_error: document.getElementById('l2-error')?.textContent || 'N/A',
            linf_error: document.getElementById('linf-error')?.textContent || 'N/A',
            relative_error: document.getElementById('relative-error')?.textContent || 'N/A',
            training_time: document.getElementById('training-time-metric')?.textContent || 'N/A',
            convergence_rate: document.getElementById('convergence-rate')?.textContent || 'N/A'
        }
    };
    
    // Create and download JSON file
    const dataStr = JSON.stringify(results, null, 2);
    const dataBlob = new Blob([dataStr], {type: 'application/json'});
    const url = URL.createObjectURL(dataBlob);
    
    const link = document.createElement('a');
    link.href = url;
    link.download = `${purposeKey}_${equationType}_results_${new Date().toISOString().split('T')[0]}.json`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
    
    showNotification('Results downloaded successfully!', 'success');
}

// Add keyboard shortcuts
document.addEventListener('keydown', function(e) {
    // Ctrl/Cmd + D to download results
    if ((e.ctrlKey || e.metaKey) && e.key === 'd') {
        e.preventDefault();
        downloadResults();
    }
    
    // Escape to go back
    if (e.key === 'Escape') {
        const backButton = document.querySelector('.btn-outline-secondary');
        if (backButton) {
            backButton.click();
        }
    }
});

// Add CSS for animations
const style = document.createElement('style');
style.textContent = `
    .animate-in {
        animation: fadeInUp 0.6s ease forwards;
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .loading-placeholder, .error-placeholder {
        padding: 2rem;
        border-radius: 8px;
        background: #f8f9fa;
        border: 1px solid #dee2e6;
    }
    
    .chart-content {
        background: white;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        overflow: hidden;
    }
    
    .chart-header {
        background: #f8f9fa;
        padding: 1rem;
        border-bottom: 1px solid #dee2e6;
    }
    
    .chart-body {
        padding: 1rem;
    }
    
    .chart-placeholder {
        text-align: center;
        padding: 2rem;
        color: #6c757d;
    }
    
    .loss-summary, .solution-summary, .error-summary, .surface-summary {
        margin-bottom: 1rem;
    }
    
    .loss-item, .solution-item, .error-item, .surface-item {
        display: flex;
        justify-content: space-between;
        margin-bottom: 0.5rem;
        padding: 0.25rem 0;
    }
    
    .loss-label, .solution-label, .error-label, .surface-label {
        font-weight: 500;
        color: #495057;
    }
    
    .loss-value, .solution-value, .error-value, .surface-value {
        font-weight: 600;
    }
`;
document.head.appendChild(style);
</rewritten_file>