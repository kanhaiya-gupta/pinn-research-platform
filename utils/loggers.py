"""Enhanced LoggerFactory: A comprehensive logging utility for PINN research platform."""

from datetime import datetime
import logging
import os
import sys
from typing import Optional, Dict, Any
import json


class LoggerFactory:
    """Create and configure a logger with file and console output for PINN research."""

    def __init__(self, logger_name: str, log_dir: str, log_file_base: str, 
                 purpose: Optional[str] = None, equation: Optional[str] = None):
        """Initialize the logger factory.

        Args:
            logger_name (str): Unique name for the logger.
            log_dir (str): Directory where the log file will be stored.
            log_file_base (str): Base name of the log file (without timestamp).
            purpose (str, optional): PINN purpose (e.g., 'forward_problems', 'inverse_problems').
            equation (str, optional): Equation type (e.g., 'heat', 'wave', 'burgers').
        """
        self.logger_name = logger_name
        self.log_dir = log_dir
        self.log_file_base = log_file_base
        self.purpose = purpose
        self.equation = equation
        self.logger = logging.getLogger(logger_name)

    def get_logger(self, level: str = "INFO") -> logging.Logger:
        """Set up and return a logger instance.

        Args:
            level (str): Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL).

        Returns:
            logging.Logger: Configured logger instance.
        """
        if self.logger.handlers:
            return self.logger

        # Set log level
        log_level = getattr(logging, level.upper(), logging.INFO)
        self.logger.setLevel(log_level)
        self.logger.propagate = False

        # Create log directory
        os.makedirs(self.log_dir, exist_ok=True)

        # Create timestamped log file
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        log_filename = f"{self.log_file_base}_{timestamp}.log"
        file_path = os.path.join(self.log_dir, log_filename)

        # File handler with detailed formatting
        file_handler = logging.FileHandler(file_path, mode="w", encoding="utf-8")
        file_formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s"
        )
        file_handler.setFormatter(file_formatter)
        file_handler.setLevel(logging.DEBUG)  # File gets all logs
        self.logger.addHandler(file_handler)

        # Console handler with cleaner formatting
        console_handler = logging.StreamHandler(sys.stdout)
        console_formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        console_handler.setFormatter(console_formatter)
        console_handler.setLevel(log_level)  # Console respects the specified level
        self.logger.addHandler(console_handler)

        # Log initial setup information
        self.logger.info(f"Logger '{self.logger_name}' initialized")
        if self.purpose:
            self.logger.info(f"PINN Purpose: {self.purpose}")
        if self.equation:
            self.logger.info(f"Equation: {self.equation}")
        self.logger.info(f"Log file: {file_path}")

        return self.logger

    def log_training_start(self, params: Dict[str, Any]) -> None:
        """Log training start with parameters.

        Args:
            params (Dict[str, Any]): Training parameters.
        """
        self.logger.info("=" * 60)
        self.logger.info("PINN TRAINING STARTED")
        self.logger.info("=" * 60)
        self.logger.info(f"Training Parameters: {json.dumps(params, indent=2)}")

    def log_training_progress(self, epoch: int, total_epochs: int, 
                            physics_loss: float, total_loss: float) -> None:
        """Log training progress.

        Args:
            epoch (int): Current epoch.
            total_epochs (int): Total number of epochs.
            physics_loss (float): Physics loss value.
            total_loss (float): Total loss value.
        """
        progress = (epoch / total_epochs) * 100
        self.logger.info(f"Epoch {epoch}/{total_epochs} ({progress:.1f}%) - "
                        f"Physics Loss: {physics_loss:.6f}, Total Loss: {total_loss:.6f}")

    def log_training_complete(self, final_loss: float, training_time: float) -> None:
        """Log training completion.

        Args:
            final_loss (float): Final loss value.
            training_time (float): Total training time in seconds.
        """
        self.logger.info("=" * 60)
        self.logger.info("PINN TRAINING COMPLETED")
        self.logger.info(f"Final Loss: {final_loss:.6f}")
        self.logger.info(f"Training Time: {training_time:.2f} seconds")
        self.logger.info("=" * 60)

    def log_error(self, error: Exception, context: str = "") -> None:
        """Log error with context.

        Args:
            error (Exception): The error that occurred.
            context (str): Additional context about the error.
        """
        self.logger.error(f"ERROR in {context}: {str(error)}")
        self.logger.error(f"Error type: {type(error).__name__}")


class PurposeLogger:
    """Purpose-specific logger for different PINN applications."""

    def __init__(self, purpose: str, equation: str):
        """Initialize purpose-specific logger.

        Args:
            purpose (str): PINN purpose (e.g., 'forward_problems').
            equation (str): Equation type (e.g., 'heat').
        """
        self.purpose = purpose
        self.equation = equation
        self.log_dir = f"logs/{purpose}/{equation}"
        self.logger = LoggerFactory(
            logger_name=f"{purpose}.{equation}",
            log_dir=self.log_dir,
            log_file_base=f"{purpose}_{equation}",
            purpose=purpose,
            equation=equation
        ).get_logger()

    def log_purpose_specific_info(self, info: str) -> None:
        """Log purpose-specific information.

        Args:
            info (str): Information to log.
        """
        self.logger.info(f"[{self.purpose.upper()}] {info}")

    def log_equation_specific_info(self, info: str) -> None:
        """Log equation-specific information.

        Args:
            info (str): Information to log.
        """
        self.logger.info(f"[{self.equation.upper()}] {info}")

    def log_training_start(self, params: Dict[str, Any]) -> None:
        """Log training start with parameters.

        Args:
            params (Dict[str, Any]): Training parameters.
        """
        self.logger.info("=" * 60)
        self.logger.info("PINN TRAINING STARTED")
        self.logger.info("=" * 60)
        self.logger.info(f"Training Parameters: {json.dumps(params, indent=2)}")

    def log_training_progress(self, epoch: int, total_epochs: int, 
                            physics_loss: float, total_loss: float) -> None:
        """Log training progress.

        Args:
            epoch (int): Current epoch.
            total_epochs (int): Total number of epochs.
            physics_loss (float): Physics loss value.
            total_loss (float): Total loss value.
        """
        progress = (epoch / total_epochs) * 100
        self.logger.info(f"Epoch {epoch}/{total_epochs} ({progress:.1f}%) - "
                        f"Physics Loss: {physics_loss:.6f}, Total Loss: {total_loss:.6f}")

    def log_training_complete(self, final_loss: float, training_time: float) -> None:
        """Log training completion.

        Args:
            final_loss (float): Final loss value.
            training_time (float): Total training time in seconds.
        """
        self.logger.info("=" * 60)
        self.logger.info("PINN TRAINING COMPLETED")
        self.logger.info(f"Final Loss: {final_loss:.6f}")
        self.logger.info(f"Training Time: {training_time:.2f} seconds")
        self.logger.info("=" * 60)

    def log_error(self, error: Exception, context: str = "") -> None:
        """Log error with context.

        Args:
            error (Exception): The error that occurred.
            context (str): Additional context about the error.
        """
        self.logger.error(f"ERROR in {context}: {str(error)}")
        self.logger.error(f"Error type: {type(error).__name__}")


# Convenience functions for quick logging setup
def get_purpose_logger(purpose: str, equation: str) -> PurposeLogger:
    """Get a purpose-specific logger.

    Args:
        purpose (str): PINN purpose.
        equation (str): Equation type.

    Returns:
        PurposeLogger: Configured logger for the specific purpose and equation.
    """
    return PurposeLogger(purpose, equation)


def get_general_logger(name: str, log_dir: str = "logs/general") -> logging.Logger:
    """Get a general-purpose logger.

    Args:
        name (str): Logger name.
        log_dir (str): Log directory.

    Returns:
        logging.Logger: Configured general logger.
    """
    return LoggerFactory(
        logger_name=name,
        log_dir=log_dir,
        log_file_base=name
    ).get_logger()