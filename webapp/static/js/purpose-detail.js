// Purpose Detail Page JavaScript

document.addEventListener('DOMContentLoaded', function() {
    console.log('Purpose detail page loaded');
    
    // Initialize interactive features
    initializeEquationCards();
    initializeResearchCards();
    initializeAdvantageCards();
    initializeSmoothScrolling();
    initializeCopyFunctionality();
});

function initializeEquationCards() {
    // Add hover effects and click interactions for equation cards
    const equationCards = document.querySelectorAll('.equation-card');
    
    equationCards.forEach(card => {
        card.addEventListener('click', function() {
            // Add a subtle animation when clicked
            this.style.transform = 'scale(0.98)';
            setTimeout(() => {
                this.style.transform = '';
            }, 150);
        });
        
        // Add hover effects
        card.addEventListener('mouseenter', function() {
            this.style.boxShadow = '0 8px 25px rgba(0, 0, 0, 0.2)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.boxShadow = '';
        });
    });
}

function initializeResearchCards() {
    // Add interactive features for research cards
    const researchCards = document.querySelectorAll('.research-card');
    
    researchCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
            this.style.boxShadow = '0 8px 25px rgba(0, 0, 0, 0.15)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = '';
            this.style.boxShadow = '';
        });
    });
}

function initializeAdvantageCards() {
    // Add interactive features for advantage cards
    const advantageCards = document.querySelectorAll('.advantage-card');
    
    advantageCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
            this.style.boxShadow = '0 8px 25px rgba(0, 0, 0, 0.15)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = '';
            this.style.boxShadow = '';
        });
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

function initializeCopyFunctionality() {
    // Add copy functionality for mathematical formulas
    const formulas = document.querySelectorAll('.equation-formula');
    
    formulas.forEach(formula => {
        formula.style.cursor = 'pointer';
        formula.title = 'Click to copy formula';
        
        formula.addEventListener('click', function() {
            const text = this.textContent;
            
            navigator.clipboard.writeText(text).then(() => {
                showNotification('Formula copied to clipboard!', 'success');
            }).catch(() => {
                showNotification('Failed to copy formula', 'warning');
            });
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
    const container = document.querySelector('.purpose-detail-container');
    container.insertBefore(notification, container.firstChild);
    
    // Auto-dismiss after 5 seconds
    setTimeout(() => {
        if (notification.parentNode) {
            notification.remove();
        }
    }, 5000);
}

// Add keyboard shortcuts
document.addEventListener('keydown', function(e) {
    // Ctrl/Cmd + Enter to start simulation
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
    const sections = document.querySelectorAll('.overview-section, .equations-section, .research-section, .advantages-section');
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
    
    .equation-formula:hover {
        background: rgba(52, 152, 219, 0.15) !important;
        transform: scale(1.02);
        transition: all 0.3s ease;
    }
    
    .purpose-header-section {
        animation: slideInDown 0.8s ease;
    }
    
    @keyframes slideInDown {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
`;
document.head.appendChild(style);

// Add purpose-specific functionality
function initializePurposeSpecificFeatures() {
    const purposeKey = window.location.pathname.split('/')[2]; // Extract purpose key from URL
    
    // Add purpose-specific color theming
    const purposeColors = {
        'forward_problems': '#3498db',
        'inverse_problems': '#e74c3c',
        'efficiency': '#27ae60',
        'sparse_data': '#f39c12',
        'data_assimilation': '#9b59b6',
        'multiphysics': '#1abc9c',
        'scientific_discovery': '#34495e',
        'uncertainty': '#e67e22',
        'generalization': '#16a085',
        'control_optimization': '#8e44ad'
    };
    
    if (purposeColors[purposeKey]) {
        const color = purposeColors[purposeKey];
        document.documentElement.style.setProperty('--purpose-color', color);
        
        // Update header border color
        const headerSection = document.querySelector('.purpose-header-section');
        if (headerSection) {
            headerSection.style.borderLeftColor = color;
        }
    }
}

// Initialize purpose-specific features
document.addEventListener('DOMContentLoaded', function() {
    initializePurposeSpecificFeatures();
}); 