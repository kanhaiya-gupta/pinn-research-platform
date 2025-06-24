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