"""
Shared Models Module for PINN Research Platform.

This module provides common PINN model architectures that can be used across all purposes.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
from typing import List, Tuple, Optional, Dict, Any
import math

from utils.loggers import get_general_logger


class MLP(nn.Module):
    """Multi-Layer Perceptron with customizable architecture."""

    def __init__(self, input_dim: int, output_dim: int, hidden_dims: List[int],
                 activation: str = "tanh", output_activation: str = "linear", dropout: float = 0.0):
        """Initialize MLP.

        Args:
            input_dim (int): Input dimension.
            output_dim (int): Output dimension.
            hidden_dims (List[int]): List of hidden layer dimensions.
            activation (str): Activation function for hidden layers ('tanh', 'relu', 'sigmoid', 'swish').
            output_activation (str): Activation function for output layer ('linear', 'tanh', 'sigmoid').
            dropout (float): Dropout rate.
        """
        super(MLP, self).__init__()
        
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.hidden_dims = hidden_dims
        self.activation_name = activation
        self.output_activation_name = output_activation
        self.dropout = dropout
        
        # Build layers
        layers = []
        prev_dim = input_dim
        
        for hidden_dim in hidden_dims:
            layers.append(nn.Linear(prev_dim, hidden_dim))
            layers.append(self._get_activation(activation))
            if dropout > 0:
                layers.append(nn.Dropout(dropout))
            prev_dim = hidden_dim
        
        # Output layer
        layers.append(nn.Linear(prev_dim, output_dim))
        
        # Add output activation if not linear
        if output_activation.lower() != "linear":
            layers.append(self._get_activation(output_activation))
        
        self.network = nn.Sequential(*layers)
        
        # Initialize weights
        self._initialize_weights()

    def _get_activation(self, activation: str) -> nn.Module:
        """Get activation function.

        Args:
            activation (str): Activation function name.

        Returns:
            nn.Module: Activation function.
        """
        if activation.lower() == "tanh":
            return nn.Tanh()
        elif activation.lower() == "relu":
            return nn.ReLU()
        elif activation.lower() == "sigmoid":
            return nn.Sigmoid()
        elif activation.lower() == "swish":
            return nn.SiLU()
        elif activation.lower() == "gelu":
            return nn.GELU()
        else:
            raise ValueError(f"Unsupported activation: {activation}")

    def _initialize_weights(self):
        """Initialize network weights."""
        for m in self.modules():
            if isinstance(m, nn.Linear):
                nn.init.xavier_normal_(m.weight)
                if m.bias is not None:
                    nn.init.zeros_(m.bias)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Forward pass.

        Args:
            x (torch.Tensor): Input tensor.

        Returns:
            torch.Tensor: Output tensor.
        """
        return self.network(x)


class FourierFeatureMLP(nn.Module):
    """MLP with Fourier feature embedding for better approximation of high-frequency functions."""

    def __init__(self, input_dim: int, output_dim: int, hidden_dims: List[int],
                 fourier_dim: int = 256, sigma: float = 10.0, activation: str = "tanh"):
        """Initialize Fourier Feature MLP.

        Args:
            input_dim (int): Input dimension.
            output_dim (int): Output dimension.
            hidden_dims (List[int]): List of hidden layer dimensions.
            fourier_dim (int): Dimension of Fourier features.
            sigma (float): Standard deviation for Fourier feature sampling.
            activation (str): Activation function.
        """
        super(FourierFeatureMLP, self).__init__()
        
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.fourier_dim = fourier_dim
        self.sigma = sigma
        
        # Fourier feature projection
        self.fourier_projection = nn.Linear(input_dim, fourier_dim, bias=False)
        
        # Initialize Fourier features
        with torch.no_grad():
            self.fourier_projection.weight.data = torch.randn(fourier_dim, input_dim) * sigma
        
        # MLP after Fourier features
        self.mlp = MLP(fourier_dim, output_dim, hidden_dims, activation)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Forward pass.

        Args:
            x (torch.Tensor): Input tensor.

        Returns:
            torch.Tensor: Output tensor.
        """
        # Apply Fourier feature transformation
        fourier_features = torch.cos(2 * math.pi * self.fourier_projection(x))
        
        # Pass through MLP
        return self.mlp(fourier_features)


class AdaptivePINN(nn.Module):
    """Adaptive PINN with dynamic loss weighting."""

    def __init__(self, input_dim: int = 2, output_dim: int = 1,
                 hidden_dims: List[int] = [50, 50, 50, 50],
                 activation: str = "tanh", num_loss_components: int = 3):
        """Initialize Adaptive PINN.

        Args:
            input_dim (int): Input dimension.
            output_dim (int): Output dimension.
            hidden_dims (List[int]): Hidden layer dimensions.
            activation (str): Activation function.
            num_loss_components (int): Number of loss components.
        """
        super(AdaptivePINN, self).__init__()
        
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.hidden_dims = hidden_dims
        self.activation = activation
        self.num_loss_components = num_loss_components
        
        # Main network
        self.network = MLP(input_dim, output_dim, hidden_dims, activation)
        
        # Adaptive loss weights (learnable)
        self.loss_weights = nn.Parameter(torch.ones(num_loss_components))
        
        # Softmax to ensure weights sum to 1
        self.softmax = nn.Softmax(dim=0)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Forward pass.

        Args:
            x (torch.Tensor): Input tensor.

        Returns:
            torch.Tensor: Output tensor.
        """
        return self.network(x)

    def get_loss_weights(self) -> torch.Tensor:
        """Get normalized loss weights.

        Returns:
            torch.Tensor: Normalized loss weights.
        """
        return self.softmax(self.loss_weights)

    def predict(self, x: torch.Tensor, t: torch.Tensor) -> torch.Tensor:
        """Make predictions.

        Args:
            x (torch.Tensor): Spatial coordinates.
            t (torch.Tensor): Temporal coordinates.

        Returns:
            torch.Tensor: Predicted solution values.
        """
        inputs = torch.cat([x, t], dim=1)
        return self.forward(inputs)


class MultiScalePINN(nn.Module):
    """Multi-scale PINN with different resolution networks."""

    def __init__(self, input_dim: int = 2, output_dim: int = 1,
                 hidden_dims: List[int] = [50, 50, 50, 50],
                 activation: str = "tanh", num_scales: int = 3):
        """Initialize Multi-scale PINN.

        Args:
            input_dim (int): Input dimension.
            output_dim (int): Output dimension.
            hidden_dims (List[int]): Hidden layer dimensions.
            activation (str): Activation function.
            num_scales (int): Number of scales.
        """
        super(MultiScalePINN, self).__init__()
        
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.hidden_dims = hidden_dims
        self.activation = activation
        self.num_scales = num_scales
        
        # Networks for different scales
        self.scale_networks = nn.ModuleList([
            MLP(input_dim, output_dim, hidden_dims, activation)
            for _ in range(num_scales)
        ])
        
        # Scale weights
        self.scale_weights = nn.Parameter(torch.ones(num_scales))
        self.softmax = nn.Softmax(dim=0)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Forward pass.

        Args:
            x (torch.Tensor): Input tensor.

        Returns:
            torch.Tensor: Output tensor.
        """
        outputs = []
        weights = self.softmax(self.scale_weights)
        
        for i, network in enumerate(self.scale_networks):
            output = network(x)
            outputs.append(weights[i] * output)
        
        return torch.sum(torch.stack(outputs), dim=0)

    def predict(self, x: torch.Tensor, t: torch.Tensor) -> torch.Tensor:
        """Make predictions.

        Args:
            x (torch.Tensor): Spatial coordinates.
            t (torch.Tensor): Temporal coordinates.

        Returns:
            torch.Tensor: Predicted solution values.
        """
        inputs = torch.cat([x, t], dim=1)
        return self.forward(inputs)


class ResNetPINN(nn.Module):
    """ResNet-style PINN with residual connections."""

    def __init__(self, input_dim: int = 2, output_dim: int = 1,
                 hidden_dims: List[int] = [50, 50, 50, 50],
                 activation: str = "tanh"):
        """Initialize ResNet PINN.

        Args:
            input_dim (int): Input dimension.
            output_dim (int): Output dimension.
            hidden_dims (List[int]): Hidden layer dimensions.
            activation (str): Activation function.
        """
        super(ResNetPINN, self).__init__()
        
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.hidden_dims = hidden_dims
        self.activation = activation
        
        # Input layer
        self.input_layer = nn.Linear(input_dim, hidden_dims[0])
        
        # Residual blocks
        self.residual_blocks = nn.ModuleList()
        for i in range(len(hidden_dims) - 1):
            self.residual_blocks.append(
                ResidualBlock(hidden_dims[i], hidden_dims[i+1], activation)
            )
        
        # Output layer
        self.output_layer = nn.Linear(hidden_dims[-1], output_dim)
        
        # Activation function
        self.activation_fn = self._get_activation(activation)

    def _get_activation(self, activation: str) -> nn.Module:
        """Get activation function."""
        if activation.lower() == "tanh":
            return nn.Tanh()
        elif activation.lower() == "relu":
            return nn.ReLU()
        elif activation.lower() == "sigmoid":
            return nn.Sigmoid()
        elif activation.lower() == "swish":
            return nn.SiLU()
        elif activation.lower() == "gelu":
            return nn.GELU()
        else:
            raise ValueError(f"Unsupported activation: {activation}")

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Forward pass.

        Args:
            x (torch.Tensor): Input tensor.

        Returns:
            torch.Tensor: Output tensor.
        """
        # Input layer
        x = self.activation_fn(self.input_layer(x))
        
        # Residual blocks
        for block in self.residual_blocks:
            x = block(x)
        
        # Output layer
        x = self.output_layer(x)
        
        return x

    def predict(self, x: torch.Tensor, t: torch.Tensor) -> torch.Tensor:
        """Make predictions.

        Args:
            x (torch.Tensor): Spatial coordinates.
            t (torch.Tensor): Temporal coordinates.

        Returns:
            torch.Tensor: Predicted solution values.
        """
        inputs = torch.cat([x, t], dim=1)
        return self.forward(inputs)


class ResidualBlock(nn.Module):
    """Residual block for ResNet PINN."""

    def __init__(self, input_dim: int, output_dim: int, activation: str = "tanh"):
        """Initialize residual block.

        Args:
            input_dim (int): Input dimension.
            output_dim (int): Output dimension.
            activation (str): Activation function.
        """
        super(ResidualBlock, self).__init__()
        
        self.input_dim = input_dim
        self.output_dim = output_dim
        
        # Layers
        self.layer1 = nn.Linear(input_dim, output_dim)
        self.layer2 = nn.Linear(output_dim, output_dim)
        
        # Activation function
        if activation.lower() == "tanh":
            self.activation = nn.Tanh()
        elif activation.lower() == "relu":
            self.activation = nn.ReLU()
        elif activation.lower() == "sigmoid":
            self.activation = nn.Sigmoid()
        elif activation.lower() == "swish":
            self.activation = nn.SiLU()
        elif activation.lower() == "gelu":
            self.activation = nn.GELU()
        else:
            raise ValueError(f"Unsupported activation: {activation}")
        
        # Skip connection (if dimensions don't match)
        if input_dim != output_dim:
            self.skip_connection = nn.Linear(input_dim, output_dim)
        else:
            self.skip_connection = nn.Identity()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Forward pass.

        Args:
            x (torch.Tensor): Input tensor.

        Returns:
            torch.Tensor: Output tensor.
        """
        identity = self.skip_connection(x)
        
        out = self.activation(self.layer1(x))
        out = self.layer2(out)
        
        return self.activation(out + identity)


def create_pinn_model(model_type: str = "standard", **kwargs) -> nn.Module:
    """Factory function to create PINN models.

    Args:
        model_type (str): Type of PINN model.
        **kwargs: Additional arguments for model initialization.

    Returns:
        nn.Module: PINN model.
    """
    # Handle separate hidden_activation and output_activation parameters
    if 'hidden_activation' in kwargs and 'output_activation' in kwargs:
        # Map to the new MLP parameters
        kwargs['activation'] = kwargs.pop('hidden_activation')
        kwargs['output_activation'] = kwargs.pop('output_activation')
    elif 'hidden_activation' in kwargs:
        kwargs['activation'] = kwargs.pop('hidden_activation')
        kwargs['output_activation'] = 'linear'  # Default output activation
    elif 'output_activation' in kwargs:
        kwargs['activation'] = 'tanh'  # Default hidden activation
        kwargs['output_activation'] = kwargs.pop('output_activation')
    
    if model_type.lower() == "standard":
        return MLP(**kwargs)
    elif model_type.lower() == "fourier":
        return FourierFeatureMLP(**kwargs)
    elif model_type.lower() == "adaptive":
        return AdaptivePINN(**kwargs)
    elif model_type.lower() == "multiscale":
        return MultiScalePINN(**kwargs)
    elif model_type.lower() == "resnet":
        return ResNetPINN(**kwargs)
    else:
        raise ValueError(f"Unsupported model type: {model_type}")


def get_model_summary(model: nn.Module) -> Dict[str, Any]:
    """Get model summary information.

    Args:
        model (nn.Module): PINN model.

    Returns:
        Dict[str, Any]: Model summary.
    """
    total_params = sum(p.numel() for p in model.parameters())
    trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    
    summary = {
        'model_type': model.__class__.__name__,
        'total_parameters': total_params,
        'trainable_parameters': trainable_params,
        'input_dim': getattr(model, 'input_dim', 'Unknown'),
        'output_dim': getattr(model, 'output_dim', 'Unknown'),
        'hidden_dims': getattr(model, 'hidden_dims', 'Unknown'),
        'activation': getattr(model, 'activation', 'Unknown')
    }
    
    return summary 