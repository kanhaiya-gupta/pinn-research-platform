"""
Shared Physics Functions Module for PINN Research Platform.

This module provides common physics functions and differential equation implementations.
"""

import torch
import torch.nn as nn
import numpy as np
from typing import Callable, Dict, Any, Optional, Tuple
import math

from utils.loggers import get_general_logger


class PhysicsFunctions:
    """Collection of physics functions for different differential equations."""

    @staticmethod
    def heat_equation_residual(x: torch.Tensor, t: torch.Tensor, u: torch.Tensor, 
                              alpha: float = 1.0) -> torch.Tensor:
        """Compute residual for heat equation: u_t - α∇²u = 0.

        Args:
            x (torch.Tensor): Spatial coordinates.
            t (torch.Tensor): Temporal coordinates.
            u (torch.Tensor): Solution values.
            alpha (float): Thermal diffusivity.

        Returns:
            torch.Tensor: Residual values.
        """
        # Enable gradients for automatic differentiation
        x.requires_grad_(True)
        t.requires_grad_(True)
        
        # Compute gradients
        u_t = torch.autograd.grad(u, t, grad_outputs=torch.ones_like(u), 
                                 create_graph=True)[0]
        u_x = torch.autograd.grad(u, x, grad_outputs=torch.ones_like(u), 
                                 create_graph=True)[0]
        u_xx = torch.autograd.grad(u_x, x, grad_outputs=torch.ones_like(u_x), 
                                  create_graph=True)[0]
        
        # Heat equation residual: u_t - αu_xx = 0
        residual = u_t - alpha * u_xx
        
        return residual

    @staticmethod
    def wave_equation_residual(x: torch.Tensor, t: torch.Tensor, u: torch.Tensor, 
                              c: float = 1.0) -> torch.Tensor:
        """Compute residual for wave equation: u_tt - c²∇²u = 0.

        Args:
            x (torch.Tensor): Spatial coordinates.
            t (torch.Tensor): Temporal coordinates.
            u (torch.Tensor): Solution values.
            c (float): Wave speed.

        Returns:
            torch.Tensor: Residual values.
        """
        # Enable gradients for automatic differentiation
        x.requires_grad_(True)
        t.requires_grad_(True)
        
        # Compute gradients
        u_t = torch.autograd.grad(u, t, grad_outputs=torch.ones_like(u), 
                                 create_graph=True)[0]
        u_tt = torch.autograd.grad(u_t, t, grad_outputs=torch.ones_like(u_t), 
                                  create_graph=True)[0]
        u_x = torch.autograd.grad(u, x, grad_outputs=torch.ones_like(u), 
                                 create_graph=True)[0]
        u_xx = torch.autograd.grad(u_x, x, grad_outputs=torch.ones_like(u_x), 
                                  create_graph=True)[0]
        
        # Wave equation residual: u_tt - c²u_xx = 0
        residual = u_tt - c**2 * u_xx
        
        return residual

    @staticmethod
    def burgers_equation_residual(x: torch.Tensor, t: torch.Tensor, u: torch.Tensor, 
                                 nu: float = 0.01) -> torch.Tensor:
        """Compute residual for Burgers equation: u_t + uu_x - νu_xx = 0.

        Args:
            x (torch.Tensor): Spatial coordinates.
            t (torch.Tensor): Temporal coordinates.
            u (torch.Tensor): Solution values.
            nu (float): Viscosity coefficient.

        Returns:
            torch.Tensor: Residual values.
        """
        # Compute gradients (x and t should already have gradients enabled)
        u_t = torch.autograd.grad(u, t, grad_outputs=torch.ones_like(u), 
                                 create_graph=True, retain_graph=True, allow_unused=True)[0]
        u_x = torch.autograd.grad(u, x, grad_outputs=torch.ones_like(u), 
                                 create_graph=True, retain_graph=True, allow_unused=True)[0]
        u_xx = torch.autograd.grad(u_x, x, grad_outputs=torch.ones_like(u_x), 
                                  create_graph=True, retain_graph=True, allow_unused=True)[0]
        
        # Burgers equation residual: u_t + uu_x - νu_xx = 0
        residual = u_t + u * u_x - nu * u_xx
        
        return residual

    @staticmethod
    def advection_equation_residual(x: torch.Tensor, t: torch.Tensor, u: torch.Tensor, 
                                   c: float = 1.0) -> torch.Tensor:
        """Compute residual for advection equation: u_t + cu_x = 0.

        Args:
            x (torch.Tensor): Spatial coordinates.
            t (torch.Tensor): Temporal coordinates.
            u (torch.Tensor): Solution values.
            c (float): Advection speed.

        Returns:
            torch.Tensor: Residual values.
        """
        # Enable gradients for automatic differentiation
        x.requires_grad_(True)
        t.requires_grad_(True)
        
        # Compute gradients
        u_t = torch.autograd.grad(u, t, grad_outputs=torch.ones_like(u), 
                                 create_graph=True)[0]
        u_x = torch.autograd.grad(u, x, grad_outputs=torch.ones_like(u), 
                                 create_graph=True)[0]
        
        # Advection equation residual: u_t + cu_x = 0
        residual = u_t + c * u_x
        
        return residual

    @staticmethod
    def reaction_diffusion_residual(x: torch.Tensor, t: torch.Tensor, u: torch.Tensor, 
                                   D: float = 1.0, k: float = 1.0) -> torch.Tensor:
        """Compute residual for reaction-diffusion equation: u_t - D∇²u + ku = 0.

        Args:
            x (torch.Tensor): Spatial coordinates.
            t (torch.Tensor): Temporal coordinates.
            u (torch.Tensor): Solution values.
            D (float): Diffusion coefficient.
            k (float): Reaction rate.

        Returns:
            torch.Tensor: Residual values.
        """
        # Enable gradients for automatic differentiation
        x.requires_grad_(True)
        t.requires_grad_(True)
        
        # Compute gradients
        u_t = torch.autograd.grad(u, t, grad_outputs=torch.ones_like(u), 
                                 create_graph=True)[0]
        u_x = torch.autograd.grad(u, x, grad_outputs=torch.ones_like(u), 
                                 create_graph=True)[0]
        u_xx = torch.autograd.grad(u_x, x, grad_outputs=torch.ones_like(u_x), 
                                  create_graph=True)[0]
        
        # Reaction-diffusion equation residual: u_t - Du_xx + ku = 0
        residual = u_t - D * u_xx + k * u
        
        return residual


class BoundaryConditions:
    """Collection of boundary condition functions."""

    @staticmethod
    def dirichlet_bc(x: torch.Tensor, t: torch.Tensor, 
                    boundary_value: Callable[[torch.Tensor, torch.Tensor], torch.Tensor]) -> torch.Tensor:
        """Dirichlet boundary condition: u(x,t) = g(x,t).

        Args:
            x (torch.Tensor): Spatial coordinates.
            t (torch.Tensor): Temporal coordinates.
            boundary_value (Callable): Function that computes boundary values.

        Returns:
            torch.Tensor: Boundary condition values.
        """
        return boundary_value(x, t)

    @staticmethod
    def neumann_bc(x: torch.Tensor, t: torch.Tensor, u: torch.Tensor,
                   boundary_derivative: Callable[[torch.Tensor, torch.Tensor], torch.Tensor]) -> torch.Tensor:
        """Neumann boundary condition: ∂u/∂n = h(x,t).

        Args:
            x (torch.Tensor): Spatial coordinates.
            t (torch.Tensor): Temporal coordinates.
            u (torch.Tensor): Solution values.
            boundary_derivative (Callable): Function that computes boundary derivatives.

        Returns:
            torch.Tensor: Boundary condition values.
        """
        x.requires_grad_(True)
        u_x = torch.autograd.grad(u, x, grad_outputs=torch.ones_like(u), 
                                 create_graph=True)[0]
        return u_x - boundary_derivative(x, t)

    @staticmethod
    def periodic_bc(x: torch.Tensor, t: torch.Tensor, u: torch.Tensor, 
                   period: float = 2 * math.pi) -> torch.Tensor:
        """Periodic boundary condition: u(x,t) = u(x+L,t).

        Args:
            x (torch.Tensor): Spatial coordinates.
            t (torch.Tensor): Temporal coordinates.
            u (torch.Tensor): Solution values.
            period (float): Period of the domain.

        Returns:
            torch.Tensor: Boundary condition values.
        """
        # This is a simplified version - in practice, you'd need to handle
        # the specific boundary points and their periodic counterparts
        return u


class InitialConditions:
    """Collection of initial condition functions."""

    @staticmethod
    def gaussian_ic(x: torch.Tensor, t: torch.Tensor, 
                   mu: float = 0.0, sigma: float = 0.1) -> torch.Tensor:
        """Gaussian initial condition.

        Args:
            x (torch.Tensor): Spatial coordinates.
            t (torch.Tensor): Temporal coordinates.
            mu (float): Mean of the Gaussian.
            sigma (float): Standard deviation of the Gaussian.

        Returns:
            torch.Tensor: Initial condition values.
        """
        return torch.exp(-0.5 * ((x - mu) / sigma) ** 2)

    @staticmethod
    def sine_ic(x: torch.Tensor, t: torch.Tensor, 
                frequency: float = 1.0, amplitude: float = 1.0) -> torch.Tensor:
        """Sine initial condition.

        Args:
            x (torch.Tensor): Spatial coordinates.
            t (torch.Tensor): Temporal coordinates.
            frequency (float): Frequency of the sine wave.
            amplitude (float): Amplitude of the sine wave.

        Returns:
            torch.Tensor: Initial condition values.
        """
        return amplitude * torch.sin(frequency * x)

    @staticmethod
    def step_ic(x: torch.Tensor, t: torch.Tensor, 
                threshold: float = 0.0) -> torch.Tensor:
        """Step function initial condition.

        Args:
            x (torch.Tensor): Spatial coordinates.
            t (torch.Tensor): Temporal coordinates.
            threshold (float): Threshold for the step function.

        Returns:
            torch.Tensor: Initial condition values.
        """
        return torch.where(x > threshold, torch.ones_like(x), torch.zeros_like(x))


def get_physics_function(equation_type: str) -> Callable:
    """Get physics function for a given equation type.

    Args:
        equation_type (str): Type of differential equation.

    Returns:
        Callable: Physics function.
    """
    physics_functions = {
        'heat': PhysicsFunctions.heat_equation_residual,
        'wave': PhysicsFunctions.wave_equation_residual,
        'burgers': PhysicsFunctions.burgers_equation_residual,
        'advection': PhysicsFunctions.advection_equation_residual,
        'reaction_diffusion': PhysicsFunctions.reaction_diffusion_residual
    }
    
    if equation_type.lower() not in physics_functions:
        raise ValueError(f"Unsupported equation type: {equation_type}")
    
    return physics_functions[equation_type.lower()]


def get_boundary_condition(bc_type: str) -> Callable:
    """Get boundary condition function for a given type.

    Args:
        bc_type (str): Type of boundary condition.

    Returns:
        Callable: Boundary condition function.
    """
    bc_functions = {
        'dirichlet': BoundaryConditions.dirichlet_bc,
        'neumann': BoundaryConditions.neumann_bc,
        'periodic': BoundaryConditions.periodic_bc
    }
    
    if bc_type.lower() not in bc_functions:
        raise ValueError(f"Unsupported boundary condition type: {bc_type}")
    
    return bc_functions[bc_type.lower()]


def get_initial_condition(ic_type: str) -> Callable:
    """Get initial condition function for a given type.

    Args:
        ic_type (str): Type of initial condition.

    Returns:
        Callable: Initial condition function.
    """
    ic_functions = {
        'gaussian': InitialConditions.gaussian_ic,
        'sine': InitialConditions.sine_ic,
        'step': InitialConditions.step_ic
    }
    
    if ic_type.lower() not in ic_functions:
        raise ValueError(f"Unsupported initial condition type: {ic_type}")
    
    return ic_functions[ic_type.lower()] 