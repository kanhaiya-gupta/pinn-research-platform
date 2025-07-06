class LiveTrainingVisualizer {
    constructor(purpose, equationType) {
        this.purpose = purpose;
        this.equationType = equationType;
        this.progressInterval = null;
        this.isTraining = false;
        
        // Initialize charts
        this.initializeCharts();
        
        // Start polling for progress
        this.startProgressPolling();
    }
    
    initializeCharts() {
        // Loss chart
        const lossChartDiv = document.getElementById('loss-chart');
        if (lossChartDiv) {
            this.lossChart = Plotly.newPlot(lossChartDiv, [
                {
                    name: 'Total Loss',
                    type: 'scatter',
                    mode: 'lines',
                    line: { color: '#1f77b4', width: 2 },
                    x: [],
                    y: []
                },
                {
                    name: 'Physics Loss',
                    type: 'scatter',
                    mode: 'lines',
                    line: { color: '#ff7f0e', width: 2 },
                    x: [],
                    y: []
                },
                {
                    name: 'Boundary Loss',
                    type: 'scatter',
                    mode: 'lines',
                    line: { color: '#2ca02c', width: 2 },
                    x: [],
                    y: []
                },
                {
                    name: 'Initial Loss',
                    type: 'scatter',
                    mode: 'lines',
                    line: { color: '#d62728', width: 2 },
                    x: [],
                    y: []
                }
            ], {
                title: 'Training Loss Progress',
                xaxis: { title: 'Epoch' },
                yaxis: { title: 'Loss', type: 'log' },
                height: 400,
                margin: { l: 60, r: 30, t: 60, b: 60 }
            });
        }
        
        // Progress gauge
        const progressGaugeDiv = document.getElementById('progress-gauge');
        if (progressGaugeDiv) {
            this.progressGauge = Plotly.newPlot(progressGaugeDiv, [{
                type: "indicator",
                mode: "gauge+number+delta",
                value: 0,
                domain: { x: [0, 1], y: [0, 1] },
                title: { text: "Training Progress" },
                delta: { reference: 0 },
                gauge: {
                    axis: { range: [null, 100] },
                    bar: { color: "#1f77b4" },
                    steps: [
                        { range: [0, 25], color: "#ff7f0e" },
                        { range: [25, 50], color: "#ffdd57" },
                        { range: [50, 75], color: "#2ca02c" },
                        { range: [75, 100], color: "#1f77b4" }
                    ],
                    threshold: {
                        line: { color: "red", width: 4 },
                        thickness: 0.75,
                        value: 90
                    }
                }
            }], {
                height: 300,
                margin: { l: 30, r: 30, t: 60, b: 30 }
            });
        }
        
        // Convergence rate chart
        const convergenceDiv = document.getElementById('convergence-chart');
        if (convergenceDiv) {
            this.convergenceChart = Plotly.newPlot(convergenceDiv, [{
                name: 'Convergence Rate',
                type: 'scatter',
                mode: 'lines+markers',
                line: { color: '#9467bd', width: 2 },
                x: [],
                y: []
            }], {
                title: 'Convergence Rate',
                xaxis: { title: 'Epoch' },
                yaxis: { title: 'Convergence Rate' },
                height: 300,
                margin: { l: 60, r: 30, t: 60, b: 60 }
            });
        }
    }
    
    startProgressPolling() {
        // Update progress every 500ms for real-time updates
        this.progressInterval = setInterval(() => {
            this.updateProgress();
        }, 500);
    }
    
    async updateProgress() {
        try {
            const response = await fetch(`/api/training-progress/${this.purpose}/${this.equationType}`);
            const progress = await response.json();
            
            console.log('📊 Frontend received progress:', progress);
            
            this.updateProgressDisplay(progress);
            this.updateCharts(progress);
            
            // Check if training is completed
            if (progress.status === 'completed') {
                console.log('✅ Training completed, stopping polling');
                this.onTrainingComplete();
            }
            
        } catch (error) {
            console.error('Error fetching training progress:', error);
        }
    }
    
    updateProgressDisplay(progress) {
        // Update progress text
        const progressText = document.getElementById('progress-text');
        if (progressText) {
            const percentage = Math.round((progress.current_epoch / progress.total_epochs) * 100);
            progressText.textContent = `${percentage}% Epoch ${progress.current_epoch} / ${progress.total_epochs}`;
        }
        
        // Update loss values
        const totalLossEl = document.getElementById('total-loss');
        const physicsLossEl = document.getElementById('physics-loss');
        const boundaryLossEl = document.getElementById('boundary-loss');
        const initialLossEl = document.getElementById('initial-loss');
        
        if (totalLossEl) totalLossEl.textContent = progress.total_loss.toExponential(3);
        if (physicsLossEl) physicsLossEl.textContent = progress.physics_loss.toExponential(3);
        if (boundaryLossEl) boundaryLossEl.textContent = progress.boundary_loss.toExponential(3);
        if (initialLossEl) initialLossEl.textContent = progress.initial_loss.toExponential(3);
        
        // Update status
        const statusEl = document.getElementById('training-status');
        if (statusEl) {
            statusEl.textContent = progress.status === 'completed' ? 'Training Completed' : 'Training in Progress...';
            statusEl.className = progress.status === 'completed' ? 'status-completed' : 'status-training';
        }
    }
    
    updateCharts(progress) {
        const currentEpoch = progress.current_epoch;
        const percentage = (currentEpoch / progress.total_epochs) * 100;
        
        console.log(`🔄 Updating charts - Epoch: ${currentEpoch}, Status: ${progress.status}, Last epoch: ${this.lastEpoch}`);
        
        // Update progress gauge
        if (this.progressGauge) {
            Plotly.update('progress-gauge', {
                value: percentage,
                delta: { reference: Math.max(0, percentage - 5) }
            });
        }
        
        // Update loss chart (only if we have new data or training is completed)
        if (this.lossChart && currentEpoch > 0) {
            const totalLoss = progress.total_loss;
            const physicsLoss = progress.physics_loss;
            const boundaryLoss = progress.boundary_loss;
            const initialLoss = progress.initial_loss;
            
            // Check if this is new data or if training is completed
            const shouldUpdate = progress.status === 'completed' || 
                               !this.lastEpoch || 
                               currentEpoch > this.lastEpoch;
            
            console.log(`📈 Loss chart update - Should update: ${shouldUpdate}, Epoch: ${currentEpoch}, Losses: ${totalLoss.toFixed(6)}, ${physicsLoss.toFixed(6)}, ${boundaryLoss.toFixed(6)}, ${initialLoss.toFixed(6)}`);
            
            if (shouldUpdate) {
                // Add new data points
                Plotly.extendTraces('loss-chart', {
                    x: [[currentEpoch], [currentEpoch], [currentEpoch], [currentEpoch]],
                    y: [[totalLoss], [physicsLoss], [boundaryLoss], [initialLoss]]
                }, [0, 1, 2, 3]);
                
                // Auto-scale y-axis
                Plotly.relayout('loss-chart', {
                    'yaxis.autorange': true
                });
                
                // Store the last epoch we processed
                this.lastEpoch = currentEpoch;
                console.log(`✅ Loss chart updated for epoch ${currentEpoch}`);
            }
        }
        
        // Update convergence chart
        if (this.convergenceChart && progress.convergence_rate !== undefined) {
            const shouldUpdate = progress.status === 'completed' || 
                               !this.lastConvergenceEpoch || 
                               currentEpoch > this.lastConvergenceEpoch;
            
            console.log(`📊 Convergence chart update - Should update: ${shouldUpdate}, Rate: ${progress.convergence_rate}`);
            
            if (shouldUpdate) {
                Plotly.extendTraces('convergence-chart', {
                    x: [[currentEpoch]],
                    y: [[progress.convergence_rate]]
                }, [0]);
                
                this.lastConvergenceEpoch = currentEpoch;
                console.log(`✅ Convergence chart updated for epoch ${currentEpoch}`);
            }
        }
    }
    
    onTrainingComplete() {
        // Stop polling
        if (this.progressInterval) {
            clearInterval(this.progressInterval);
            this.progressInterval = null;
        }
        
        // Show completion message
        const completionMsg = document.getElementById('completion-message');
        if (completionMsg) {
            completionMsg.style.display = 'block';
        }
        
        // Enable view results button
        const viewResultsBtn = document.getElementById('view-results-btn');
        if (viewResultsBtn) {
            viewResultsBtn.style.display = 'inline-block';
        }
    }
    
    stop() {
        if (this.progressInterval) {
            clearInterval(this.progressInterval);
            this.progressInterval = null;
        }
    }
}

// Initialize live training visualizer when page loads
document.addEventListener('DOMContentLoaded', function() {
    // Get purpose and equation type from URL or data attributes
    const purpose = document.body.dataset.purpose || 'forward_problems';
    const equationType = document.body.dataset.equationType || 'heat';
    
    // Initialize the visualizer
    window.liveTrainingVisualizer = new LiveTrainingVisualizer(purpose, equationType);
    
    // Handle page unload
    window.addEventListener('beforeunload', function() {
        if (window.liveTrainingVisualizer) {
            window.liveTrainingVisualizer.stop();
        }
    });
}); 