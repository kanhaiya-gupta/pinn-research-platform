"""
ControlOptimization Evaluator for PINN Research Platform.

This module provides evaluation functionality for control optimization using PINNs.
"""

import torch
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, Any, Tuple, Optional, List
import json
from pathlib import Path
import seaborn as sns
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

from utils.loggers import get_purpose_logger


class ControlOptimizationEvaluator:
    """Evaluator class for control optimization using PINNs."""

    def __init__(self, model: torch.nn.Module, purpose: str, equation: str):
        """Initialize the control optimization evaluator.

        Args:
            model (torch.nn.Module): Trained PINN model.
            purpose (str): PINN purpose (e.g., 'control_optimization').
            equation (str): Equation type (e.g., 'heat', 'wave', 'burgers').
        """
        self.model = model
        self.purpose = purpose
        self.equation = equation
        self.logger = get_purpose_logger(purpose, equation)
        
        self.model.eval()  # Set model to evaluation mode
        
        self.logger.log_purpose_specific_info("ControlOptimization Evaluator initialized")

    def predict(self, x: torch.Tensor, t: torch.Tensor) -> torch.Tensor:
        """Make predictions using the trained model.

        Args:
            x (torch.Tensor): Spatial coordinates.
            t (torch.Tensor): Temporal coordinates.

        Returns:
            torch.Tensor: Predicted solution values.
        """
        with torch.no_grad():
            inputs = torch.cat([x, t], dim=1)
            predictions = self.model(inputs)
        return predictions

    def compute_metrics(self, y_true: np.ndarray, y_pred: np.ndarray) -> Dict[str, float]:
        """Compute evaluation metrics.

        Args:
            y_true (np.ndarray): True values.
            y_pred (np.ndarray): Predicted values.

        Returns:
            Dict[str, float]: Dictionary of metrics.
        """
        mse = mean_squared_error(y_true, y_pred)
        mae = mean_absolute_error(y_true, y_pred)
        r2 = r2_score(y_true, y_pred)
        rmse = np.sqrt(mse)
        
        # Relative L2 error
        relative_l2 = np.linalg.norm(y_true - y_pred) / np.linalg.norm(y_true)
        
        # Maximum absolute error
        max_error = np.max(np.abs(y_true - y_pred))
        
        metrics = {
            'mse': mse,
            'mae': mae,
            'r2': r2,
            'rmse': rmse,
            'relative_l2': relative_l2,
            'max_error': max_error
        }
        
        return metrics

    def evaluate_on_grid(self, x_grid: np.ndarray, t_grid: np.ndarray,
                        u_true: np.ndarray) -> Dict[str, Any]:
        """Evaluate model on a regular grid.

        Args:
            x_grid (np.ndarray): Spatial grid.
            t_grid (np.ndarray): Temporal grid.
            u_true (np.ndarray): True solution on grid.

        Returns:
            Dict[str, Any]: Evaluation results.
        """
        # Convert to tensors
        x_tensor = torch.FloatTensor(x_grid.flatten().reshape(-1, 1))
        t_tensor = torch.FloatTensor(t_grid.flatten().reshape(-1, 1))
        
        # Make predictions
        u_pred_tensor = self.predict(x_tensor, t_tensor)
        u_pred = u_pred_tensor.numpy().reshape(x_grid.shape)
        
        # Compute metrics
        metrics = self.compute_metrics(u_true.flatten(), u_pred.flatten())
        
        # Store results
        results = {
            'predictions': u_pred,
            'true_values': u_true,
            'metrics': metrics,
            'x_grid': x_grid,
            't_grid': t_grid
        }
        
        self.logger.log_equation_specific_info(f"Grid evaluation completed - R²: {metrics['r2']:.4f}")
        
        return results

    def save_evaluation_results(self, results: Dict[str, Any], 
                              save_path: str) -> None:
        """Save evaluation results to file.

        Args:
            results (Dict[str, Any]): Evaluation results.
            save_path (str): Path to save results.
        """
        # Prepare data for saving
        save_data = {
            'metrics': results['metrics'],
            'equation': self.equation,
            'purpose': self.purpose,
            'evaluation_timestamp': str(np.datetime64('now'))
        }
        
        # Save as JSON
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        with open(save_path, 'w') as f:
            json.dump(save_data, f, indent=2)
        
        self.logger.log_equation_specific_info(f"Evaluation results saved to {save_path}")

    def generate_evaluation_report(self, results: Dict[str, Any], 
                                 save_dir: str) -> str:
        """Generate comprehensive evaluation report.

        Args:
            results (Dict[str, Any]): Evaluation results.
            save_dir (str): Directory to save report.

        Returns:
            str: Path to the generated report.
        """
        Path(save_dir).mkdir(parents=True, exist_ok=True)
        
        # Save results
        results_path = Path(save_dir) / f"{self.equation}_evaluation_results.json"
        self.save_evaluation_results(results, str(results_path))
        
        # Generate text report
        report_path = Path(save_dir) / f"{self.equation}_evaluation_report.txt"
        
        with open(report_path, 'w') as f:
            f.write("=" * 60 + "\n")
            f.write(f"PINN EVALUATION REPORT - {self.equation.upper()}\n")
            f.write("=" * 60 + "\n\n")
            
            f.write(f"Equation: {self.equation}\n")
            f.write(f"Purpose: {self.purpose}\n")
            f.write(f"Evaluation Date: {np.datetime64('now')}\n\n")
            
            f.write("EVALUATION METRICS:\n")
            f.write("-" * 20 + "\n")
            for metric, value in results['metrics'].items():
                f.write(f"{metric.upper()}: {value:.6f}\n")
            
            f.write(f"\nReport generated by: {self.__class__.__name__}\n")
        
        self.logger.log_equation_specific_info(f"Evaluation report generated in {save_dir}")
        
        return str(report_path)
