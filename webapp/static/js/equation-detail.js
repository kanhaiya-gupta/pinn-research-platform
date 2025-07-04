// Equation Detail Page JavaScript

document.addEventListener('DOMContentLoaded', function() {
    console.log('Equation detail page loaded');
    
    // Initialize interactive features
    initializeParameterCards();
    initializeApplicationCards();
    initializeMathDisplay();
    initializeSmoothScrolling();
});

function initializeParameterCards() {
    // Add hover effects and click interactions for parameter cards
    const parameterCards = document.querySelectorAll('.parameter-card');
    
    parameterCards.forEach(card => {
        card.addEventListener('click', function() {
            // Add a subtle animation when clicked
            this.style.transform = 'scale(0.98)';
            setTimeout(() => {
                this.style.transform = '';
            }, 150);
        });
    });
}

function initializeApplicationCards() {
    // Add interactive features for application cards
    const applicationCards = document.querySelectorAll('.application-card');
    
    applicationCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            // Add a subtle glow effect
            this.style.boxShadow = '0 8px 25px rgba(0, 0, 0, 0.2)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.boxShadow = '';
        });
    });
}

function initializeMathDisplay() {
    // Enhance math formula display
    const equationDisplays = document.querySelectorAll('.equation-display');
    
    equationDisplays.forEach(display => {
        // Add a subtle animation when the element comes into view
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '0';
                    entry.target.style.transform = 'translateY(20px)';
                    
                    setTimeout(() => {
                        entry.target.style.transition = 'all 0.6s ease';
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'translateY(0)';
                    }, 100);
                    
                    observer.unobserve(entry.target);
                }
            });
        });
        
        observer.observe(display);
    });
}

function initializeSmoothScrolling() {
    // Add smooth scrolling for anchor links
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

// Add loading states for action buttons
function addLoadingState(button) {
    const originalText = button.innerHTML;
    button.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Loading...';
    button.disabled = true;
    
    return function() {
        button.innerHTML = originalText;
        button.disabled = false;
    };
}

// Utility function to show notifications
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} alert-dismissible fade show`;
    notification.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    // Insert at the top of the page
    const container = document.querySelector('.equation-detail-container');
    container.insertBefore(notification, container.firstChild);
    
    // Auto-dismiss after 5 seconds
    setTimeout(() => {
        if (notification.parentNode) {
            notification.remove();
        }
    }, 5000);
}

// Add copy functionality for mathematical formulas
function initializeCopyButtons() {
    const equationDisplays = document.querySelectorAll('.equation-display');
    
    equationDisplays.forEach(display => {
        display.style.cursor = 'pointer';
        display.title = 'Click to copy formula';
        
        display.addEventListener('click', function() {
            const text = this.textContent;
            
            navigator.clipboard.writeText(text).then(() => {
                showNotification('Formula copied to clipboard!', 'success');
            }).catch(() => {
                showNotification('Failed to copy formula', 'warning');
            });
        });
    });
}

// Initialize copy functionality when page loads
document.addEventListener('DOMContentLoaded', function() {
    initializeCopyButtons();
});

// Add keyboard shortcuts
document.addEventListener('keydown', function(e) {
    // Ctrl/Cmd + Enter to start training
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
        const startButton = document.querySelector('.btn-primary');
        if (startButton) {
            startButton.click();
        }
    }
    
    // Escape to go back
    if (e.key === 'Escape') {
        const backButton = document.querySelector('.btn-outline-primary');
        if (backButton) {
            backButton.click();
        }
    }
});

// Add scroll-based animations
function initializeScrollAnimations() {
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
    const sections = document.querySelectorAll('.applications-section, .real-world-section, .math-section, .parameters-section, .impact-section');
    sections.forEach(section => {
        observer.observe(section);
    });
}

// Initialize scroll animations
document.addEventListener('DOMContentLoaded', function() {
    initializeScrollAnimations();
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
    
    .equation-display:hover {
        background: rgba(52, 152, 219, 0.15) !important;
        transform: scale(1.02);
        transition: all 0.3s ease;
    }
`;
document.head.appendChild(style);

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
    document.getElementById('final-loss').textContent = 'Loading...';
    document.getElementById('training-time').textContent = 'Loading...';
    document.getElementById('convergence-status').textContent = 'Loading...';
    
    // Show loading spinners in chart containers
    const chartContainers = document.querySelectorAll('.chart-container');
    chartContainers.forEach(container => {
        container.innerHTML = '<div class="text-center"><i class="fas fa-spinner fa-spin fa-2x"></i><p>Loading chart...</p></div>';
    });
}

function displayResults(data) {
    // Update summary statistics
    if (data.final_loss !== undefined) {
        document.getElementById('final-loss').textContent = data.final_loss.toFixed(6);
    }
    
    if (data.training_time !== undefined) {
        document.getElementById('training-time').textContent = `${data.training_time.toFixed(2)}s`;
    }
    
    if (data.convergence_status !== undefined) {
        document.getElementById('convergence-status').textContent = data.convergence_status;
    }
    
    // Update metrics table
    if (data.metrics) {
        if (data.metrics.l2_error !== undefined) {
            document.getElementById('l2-error').textContent = data.metrics.l2_error.toFixed(6);
        }
        if (data.metrics.linf_error !== undefined) {
            document.getElementById('linf-error').textContent = data.metrics.linf_error.toFixed(6);
        }
        if (data.metrics.relative_error !== undefined) {
            document.getElementById('relative-error').textContent = `${(data.metrics.relative_error * 100).toFixed(2)}%`;
        }
        if (data.training_time !== undefined) {
            document.getElementById('training-time-metric').textContent = `${data.training_time.toFixed(2)}s`;
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
}

function showErrorState(errorMessage) {
    // Show error message
    showNotification(`Failed to load results: ${errorMessage}`, 'danger');
    
    // Update summary stats with error indicators
    document.getElementById('final-loss').textContent = 'Error';
    document.getElementById('training-time').textContent = 'Error';
    document.getElementById('convergence-status').textContent = 'Error';
    
    // Show error message in chart containers
    const chartContainers = document.querySelectorAll('.chart-container');
    chartContainers.forEach(container => {
        container.innerHTML = '<div class="text-center text-danger"><i class="fas fa-exclamation-triangle fa-2x"></i><p>Failed to load chart data</p></div>';
    });
}

function displayLossChart(lossHistory) {
    const container = document.getElementById('loss-chart');
    if (!container) return;
    
    // Simple chart display - in a real implementation, you'd use Chart.js or similar
    container.innerHTML = `
        <div class="chart-placeholder">
            <h4>Loss History</h4>
            <p>Training completed successfully!</p>
            <p>Final Loss: ${lossHistory.final_loss?.toFixed(6) || 'N/A'}</p>
            <p>Epochs: ${lossHistory.epochs || 'N/A'}</p>
        </div>
    `;
}

function displaySolutionChart(solutionData) {
    const container = document.getElementById('solution-chart');
    if (!container) return;
    
    container.innerHTML = `
        <div class="chart-placeholder">
            <h4>Solution Comparison</h4>
            <p>PINN solution generated successfully!</p>
            <p>Domain: ${solutionData.domain || 'N/A'}</p>
        </div>
    `;
}

function displayErrorChart(errorData) {
    const container = document.getElementById('error-chart');
    if (!container) return;
    
    container.innerHTML = `
        <div class="chart-placeholder">
            <h4>Error Analysis</h4>
            <p>Error analysis completed!</p>
            <p>Max Error: ${errorData.max_error?.toFixed(6) || 'N/A'}</p>
        </div>
    `;
}

function displaySurfaceChart(surfaceData) {
    const container = document.getElementById('surface-chart');
    if (!container) return;
    
    container.innerHTML = `
        <div class="chart-placeholder">
            <h4>Solution Surface</h4>
            <p>3D surface visualization ready!</p>
            <p>Points: ${surfaceData.points || 'N/A'}</p>
        </div>
    `;
}

// Download results functionality
function downloadResults() {
    const purposeKey = window.purposeKey || 'forward_problems';
    const equationType = window.equationType || 'burgers';
    
    // Create a simple results summary
    const results = {
        purpose: purposeKey,
        equation: equationType,
        timestamp: new Date().toISOString(),
        summary: {
            final_loss: document.getElementById('final-loss').textContent,
            training_time: document.getElementById('training-time').textContent,
            convergence_status: document.getElementById('convergence-status').textContent
        }
    };
    
    // Create and download JSON file
    const dataStr = JSON.stringify(results, null, 2);
    const dataBlob = new Blob([dataStr], {type: 'application/json'});
    const url = URL.createObjectURL(dataBlob);
    
    const link = document.createElement('a');
    link.href = url;
    link.download = `${purposeKey}_${equationType}_results.json`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
    
    showNotification('Results downloaded successfully!', 'success');
} 