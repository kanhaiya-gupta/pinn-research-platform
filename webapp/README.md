# Physics-Informed Neural Network (PINN) Frontend

A comprehensive web interface for exploring and experimenting with Physics-Informed Neural Networks across a wide range of scientific and engineering applications.

## 🌟 Overview

This frontend provides an intuitive, interactive platform for PINN research and applications, showcasing the revolutionary potential of combining deep learning with physical laws. The platform supports multiple differential equations and demonstrates various PINN purposes including forward problems, inverse problems, scientific discovery, and more.

## 🎯 PINN Applications & Purposes

The platform showcases the wide scope of PINN applications:

### 🔄 Forward Problems
- Simulate physical systems by solving known PDEs with given initial and boundary conditions
- Examples: Heat conduction, Wave propagation, Fluid dynamics

### 🔍 Inverse Problems
- Infer unknown parameters, source terms, or boundary conditions from observed data
- Examples: Parameter identification, Source reconstruction, Boundary condition estimation

### ⚡ Simulation Efficiency
- Provide faster, differentiable, and real-time alternatives to traditional numerical solvers
- Examples: Real-time simulation, Differentiable physics, Fast surrogate models

### 📊 Sparse/Noisy Data Learning
- Use physical laws to guide learning, reducing dependence on large labeled datasets
- Examples: Limited data scenarios, Noisy measurements, Data augmentation

### 🔄 Data Assimilation
- Combine observational data with governing physics to improve state estimation
- Examples: Weather forecasting, Ocean modeling, Climate prediction

### ⚙️ Multiphysics Systems
- Handle systems involving multiple interacting physical phenomena or scales
- Examples: Fluid-structure interaction, Thermo-mechanical coupling, Electromagnetic-thermal

### 🔬 Scientific Discovery
- Discover or validate new physical laws, constitutive relations, or hidden dynamics
- Examples: New constitutive laws, Hidden dynamics, Physical validation

### 📈 Uncertainty Quantification
- Extend PINNs to probabilistic frameworks to model and quantify uncertainties
- Examples: Probabilistic predictions, Confidence intervals, Risk assessment

### 🛡️ Generalization & Robustness
- Physics constraints act as regularizers, leading to better generalization
- Examples: Out-of-distribution, Domain adaptation, Robust predictions

### 🎛️ Control & Optimization
- Use PINNs in design, control, or optimization tasks with physics constraints
- Examples: Optimal control, Design optimization, Parameter tuning

## 🧮 Supported Equations

The platform currently supports the following differential equations:

| Equation | Type | Applications | PINN Purposes |
|----------|------|--------------|---------------|
| **Burgers Equation** | Nonlinear PDE | Shock waves, Traffic flow, Gas dynamics | Forward/Inverse problems, Efficiency |
| **Heat Equation** | Parabolic PDE | Thermal analysis, Material processing, Climate modeling | Forward/Inverse problems, Efficiency, Sparse data |
| **Wave Equation** | Hyperbolic PDE | Acoustic waves, Electromagnetic waves, Seismic waves | Forward/Inverse problems, Efficiency, Multiphysics |
| **Simple Harmonic Motion** | ODE | Mechanical vibrations, Electrical circuits, Molecular dynamics | Forward problems, Control optimization, Generalization |
| **Helmholtz Equation** | Elliptic PDE | Acoustic scattering, Electromagnetic fields, Quantum mechanics | Forward/Inverse problems, Multiphysics |
| **Navier-Stokes** | System of PDEs | Aerodynamics, Oceanography, Blood flow modeling | Forward/Inverse problems, Multiphysics, Efficiency |
| **Schrödinger Equation** | Quantum PDE | Quantum chemistry, Material properties, Quantum computing | Forward problems, Scientific discovery, Uncertainty |
| **Maxwell Equations** | System of PDEs | Antenna design, Optical systems, Electromagnetic compatibility | Forward problems, Multiphysics, Efficiency |

## 🚀 Features

### Interactive Dashboard
- **PINN Purposes Overview**: Visual cards showcasing different PINN applications
- **Equation Explorer**: Browse supported differential equations with detailed information
- **Research Impact**: Learn about the transformative potential of PINNs in various fields
- **Quick Start Guide**: Step-by-step instructions for getting started

### Equation Detail Pages
- **Comprehensive Information**: Mathematical background, applications, and parameters
- **PINN Applications**: Specific use cases for each equation
- **Real-world Applications**: Practical examples and industry use cases
- **Interactive Elements**: Clickable formulas, parameter explanations, and animations

### Simulation Interface
- **Parameter Configuration**: Intuitive forms for setting equation parameters
- **Training Controls**: Start, monitor, and control PINN training
- **Real-time Feedback**: Live updates on training progress and results
- **Visualization**: Interactive plots and solution comparisons

### Research Tools
- **Result Analysis**: Comprehensive analysis of training results
- **Performance Metrics**: Loss curves, convergence analysis, and accuracy measures
- **Comparison Tools**: Compare PINN solutions with analytical or numerical solutions
- **Export Capabilities**: Download results, plots, and model parameters

## 🛠️ Technology Stack

- **Frontend Framework**: FastAPI with Jinja2 templates
- **Styling**: Custom CSS with Bootstrap 5 integration
- **JavaScript**: Vanilla JS with modern ES6+ features
- **Icons**: Font Awesome for comprehensive iconography
- **Charts**: Chart.js for interactive visualizations
- **Backend Integration**: RESTful API communication with main.py backend

## 📦 Installation

### Prerequisites
- Python 3.8+
- FastAPI
- Uvicorn
- Jinja2
- httpx

### Setup
1. **Clone the repository** (if not already done):
   ```bash
   git clone <repository-url>
   cd physics-informed-neural-network
   ```

2. **Install frontend dependencies**:
   ```bash
   cd webapp
   pip install -r requirements.txt
   ```

3. **Start the backend** (in a separate terminal):
   ```bash
   # From the root directory
   python main.py
   ```

4. **Start the frontend**:
   ```bash
   # From the root directory
   python run_frontend.py
   ```

5. **Access the application**:
   - Frontend: http://localhost:5000
   - Backend API: http://localhost:8000

## 🎮 Usage

### Getting Started
1. **Explore the Dashboard**: Visit the main page to see PINN purposes and supported equations
2. **Choose an Application**: Select from forward problems, inverse problems, or other PINN purposes
3. **Select an Equation**: Pick the differential equation that models your physical system
4. **Configure Parameters**: Set equation parameters and training configuration
5. **Start Training**: Launch PINN training and monitor progress
6. **Analyze Results**: View interactive visualizations and performance metrics

### Navigation
- **Dashboard** (`/`): Overview of PINN applications and equations
- **Equation Info** (`/equation/{type}`): Detailed information about specific equations
- **Simulation** (`/simulation/{type}`): Training interface for PINN models
- **Results** (`/results/{type}`): Analysis and visualization of training results

### Interactive Features
- **Clickable Formulas**: Click on mathematical formulas to copy them
- **Hover Effects**: Interactive cards with hover animations
- **Keyboard Shortcuts**: 
  - `Ctrl/Cmd + Enter`: Start training
  - `Escape`: Go back
- **Responsive Design**: Works on desktop, tablet, and mobile devices

## 🔧 Configuration

### Environment Variables
- `API_BASE_URL`: Backend API URL (default: http://localhost:8000)

### Customization
- **Adding New Equations**: Update `config.py` with equation definitions
- **Modifying Parameters**: Edit default parameters in the configuration
- **Styling**: Customize CSS variables in `static/css/main.css`
- **Templates**: Modify Jinja2 templates in the `templates/` directory

## 📊 API Integration

The frontend communicates with the backend API through the following endpoints:

### Training Endpoints
- `POST /api/{equation_type}/train`: Submit training requests
- `POST /api/{equation_type}/predict`: Make predictions with trained models
- `GET /api/results/{equation_type}`: Retrieve training results

### Parameter Mapping
The frontend automatically maps user-friendly parameter names to backend API formats for each equation type.

## 🎨 Design Philosophy

### User Experience
- **Intuitive Interface**: Clean, modern design with clear navigation
- **Educational Focus**: Comprehensive explanations and examples
- **Interactive Learning**: Hands-on exploration of PINN concepts
- **Professional Presentation**: Research-grade visualization and analysis

### Accessibility
- **Responsive Design**: Works across all device sizes
- **Keyboard Navigation**: Full keyboard accessibility
- **Clear Typography**: Readable fonts and proper contrast
- **Loading States**: Clear feedback during operations

## 🔬 Research Applications

### Academic Research
- **Methodology Development**: Test new PINN architectures and training strategies
- **Benchmarking**: Compare PINN performance with traditional methods
- **Parameter Studies**: Systematic exploration of equation parameters
- **Educational Tool**: Teach PINN concepts to students and researchers

### Industry Applications
- **Engineering Design**: Optimize designs using physics-informed AI
- **Process Optimization**: Improve manufacturing and industrial processes
- **Risk Assessment**: Quantify uncertainties in physical predictions
- **Real-time Control**: Deploy PINNs for real-time system control

## 🚧 Development

### Project Structure
```
webapp/
├── app.py                 # FastAPI application
├── config.py             # Configuration and equation definitions
├── requirements.txt      # Python dependencies
├── static/              # Static assets
│   ├── css/            # Stylesheets
│   ├── js/             # JavaScript files
│   └── reports/        # Generated reports
├── templates/           # Jinja2 templates
│   ├── base.html       # Base template
│   ├── index.html      # Dashboard
│   └── equations/      # Equation-specific templates
└── README.md           # This file
```

### Contributing
1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/new-equation`
3. **Make changes**: Add new equations, improve UI, or enhance functionality
4. **Test thoroughly**: Ensure all features work correctly
5. **Submit a pull request**: Include detailed description of changes

### Adding New Equations
1. **Update `config.py`**: Add equation definition with parameters
2. **Create templates**: Add equation-specific HTML templates
3. **Add styling**: Include any custom CSS if needed
4. **Test integration**: Ensure backend API compatibility
5. **Update documentation**: Add equation to README and help text

## 📚 Educational Resources

### Learning PINNs
- **Mathematical Background**: Understanding the theory behind PINNs
- **Implementation Details**: How PINNs are implemented and trained
- **Best Practices**: Guidelines for effective PINN development
- **Case Studies**: Real-world examples and applications

### Advanced Topics
- **Multi-scale Problems**: Handling problems with multiple spatial/temporal scales
- **Uncertainty Quantification**: Probabilistic PINN frameworks
- **Inverse Problems**: Parameter identification and system identification
- **Optimization**: Using PINNs for design and control optimization

## 🤝 Community

### Getting Help
- **Documentation**: Comprehensive guides and tutorials
- **Examples**: Working examples for all supported equations
- **Troubleshooting**: Common issues and solutions
- **Support**: Community forums and discussion groups

### Contributing to Research
- **Open Source**: All code is open source and available for research
- **Collaboration**: Connect with other researchers and developers
- **Publications**: Cite the platform in your research papers
- **Feedback**: Share suggestions for improvements and new features

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Research Community**: Thanks to the PINN research community for foundational work
- **Open Source**: Built on excellent open source libraries and frameworks
- **Contributors**: All contributors who have helped improve the platform
- **Users**: Researchers and students who use the platform for their work

---

**Transform your scientific computing with Physics-Informed Neural Networks!** 🚀 