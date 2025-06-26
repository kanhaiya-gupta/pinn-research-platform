"""
Generalization Parameters
Parameters for improving model generalization and transfer learning.
"""

GENERALIZATION_PARAMETERS_DICT = {
    # Regularization Parameters
    'l1_regularization': {
        'name': 'L1 Regularization',
        'description': 'L1 regularization coefficient',
        'unit': 'dimensionless',
        'default': 0.0,
        'range': [0.0, 1.0],
        'category': 'regularization_parameters',
        'generalization_method': 'sparsity'
    },
    'l2_regularization': {
        'name': 'L2 Regularization',
        'description': 'L2 regularization coefficient',
        'unit': 'dimensionless',
        'default': 1e-6,
        'range': [0.0, 1e-3],
        'category': 'regularization_parameters',
        'generalization_method': 'weight_decay'
    },
    'dropout_rate': {
        'name': 'Dropout Rate',
        'description': 'Dropout rate for regularization',
        'unit': 'dimensionless',
        'default': 0.1,
        'range': [0.0, 0.5],
        'category': 'regularization_parameters',
        'generalization_method': 'dropout'
    },
    'batch_normalization': {
        'name': 'Batch Normalization',
        'description': 'Whether to use batch normalization',
        'unit': 'dimensionless',
        'default': True,
        'range': [True, False],
        'category': 'regularization_parameters',
        'generalization_method': 'normalization'
    },
    
    # Data Augmentation Parameters
    'noise_level': {
        'name': 'Noise Level',
        'description': 'Level of noise for data augmentation',
        'unit': 'dimensionless',
        'default': 0.01,
        'range': [0.0, 0.1],
        'category': 'data_augmentation_parameters',
        'generalization_method': 'noise_injection'
    },
    'scaling_factor': {
        'name': 'Scaling Factor',
        'description': 'Scaling factor for data augmentation',
        'unit': 'dimensionless',
        'default': 0.1,
        'range': [0.0, 1.0],
        'category': 'data_augmentation_parameters',
        'generalization_method': 'scaling'
    },
    'rotation_angle': {
        'name': 'Rotation Angle',
        'description': 'Rotation angle for data augmentation',
        'unit': 'degrees',
        'default': 5.0,
        'range': [0.0, 45.0],
        'category': 'data_augmentation_parameters',
        'generalization_method': 'rotation'
    },
    'translation_range': {
        'name': 'Translation Range',
        'description': 'Translation range for data augmentation',
        'unit': 'dimensionless',
        'default': 0.1,
        'range': [0.0, 1.0],
        'category': 'data_augmentation_parameters',
        'generalization_method': 'translation'
    },
    
    # Cross-Validation Parameters
    'cross_validation_folds': {
        'name': 'Cross Validation Folds',
        'description': 'Number of folds for cross validation',
        'unit': 'dimensionless',
        'default': 5,
        'range': [2, 10],
        'category': 'cross_validation_parameters',
        'generalization_method': 'cross_validation'
    },
    'stratified_sampling': {
        'name': 'Stratified Sampling',
        'description': 'Whether to use stratified sampling',
        'unit': 'dimensionless',
        'default': True,
        'range': [True, False],
        'category': 'cross_validation_parameters',
        'generalization_method': 'cross_validation'
    },
    'leave_one_out': {
        'name': 'Leave One Out',
        'description': 'Whether to use leave-one-out validation',
        'unit': 'dimensionless',
        'default': False,
        'range': [True, False],
        'category': 'cross_validation_parameters',
        'generalization_method': 'cross_validation'
    },
    
    # Transfer Learning Parameters
    'transfer_learning': {
        'name': 'Transfer Learning',
        'description': 'Whether to use transfer learning',
        'unit': 'dimensionless',
        'default': False,
        'range': [True, False],
        'category': 'transfer_learning_parameters',
        'generalization_method': 'transfer_learning'
    },
    'pretrained_model': {
        'name': 'Pretrained Model',
        'description': 'Path to pretrained model',
        'unit': 'dimensionless',
        'default': '',
        'range': ['', 'path_to_model'],
        'category': 'transfer_learning_parameters',
        'generalization_method': 'transfer_learning'
    },
    'fine_tuning_layers': {
        'name': 'Fine Tuning Layers',
        'description': 'Number of layers to fine-tune',
        'unit': 'dimensionless',
        'default': 2,
        'range': [0, 10],
        'category': 'transfer_learning_parameters',
        'generalization_method': 'transfer_learning'
    },
    'freeze_layers': {
        'name': 'Freeze Layers',
        'description': 'Whether to freeze pretrained layers',
        'unit': 'dimensionless',
        'default': True,
        'range': [True, False],
        'category': 'transfer_learning_parameters',
        'generalization_method': 'transfer_learning'
    },
    
    # Domain Adaptation Parameters
    'domain_adaptation': {
        'name': 'Domain Adaptation',
        'description': 'Whether to use domain adaptation',
        'unit': 'dimensionless',
        'default': False,
        'range': [True, False],
        'category': 'domain_adaptation_parameters',
        'generalization_method': 'domain_adaptation'
    },
    'domain_loss_weight': {
        'name': 'Domain Loss Weight',
        'description': 'Weight for domain adaptation loss',
        'unit': 'dimensionless',
        'default': 1.0,
        'range': [0.0, 10.0],
        'category': 'domain_adaptation_parameters',
        'generalization_method': 'domain_adaptation'
    },
    'adversarial_training': {
        'name': 'Adversarial Training',
        'description': 'Whether to use adversarial training',
        'unit': 'dimensionless',
        'default': False,
        'range': [True, False],
        'category': 'domain_adaptation_parameters',
        'generalization_method': 'domain_adaptation'
    },
    
    # Ensemble Parameters
    'ensemble_size': {
        'name': 'Ensemble Size',
        'description': 'Number of models in ensemble',
        'unit': 'dimensionless',
        'default': 5,
        'range': [2, 20],
        'category': 'ensemble_parameters',
        'generalization_method': 'ensemble_learning'
    },
    'ensemble_method': {
        'name': 'Ensemble Method',
        'description': 'Method for ensemble combination',
        'unit': 'dimensionless',
        'default': 'average',
        'range': ['average', 'weighted', 'stacking', 'boosting'],
        'category': 'ensemble_parameters',
        'generalization_method': 'ensemble_learning'
    },
    'bootstrap_sampling': {
        'name': 'Bootstrap Sampling',
        'description': 'Whether to use bootstrap sampling',
        'unit': 'dimensionless',
        'default': True,
        'range': [True, False],
        'category': 'ensemble_parameters',
        'generalization_method': 'ensemble_learning'
    },
    
    # Physics-Informed Parameters
    'physics_weight': {
        'name': 'Physics Weight',
        'description': 'Weight for physics-informed terms',
        'unit': 'dimensionless',
        'default': 1.0,
        'range': [0.0, 10.0],
        'category': 'physics_informed_parameters',
        'generalization_method': 'physics_informed'
    },
    'boundary_weight': {
        'name': 'Boundary Weight',
        'description': 'Weight for boundary conditions',
        'unit': 'dimensionless',
        'default': 1.0,
        'range': [0.0, 10.0],
        'category': 'physics_informed_parameters',
        'generalization_method': 'physics_informed'
    },
    'initial_weight': {
        'name': 'Initial Weight',
        'description': 'Weight for initial conditions',
        'unit': 'dimensionless',
        'default': 1.0,
        'range': [0.0, 10.0],
        'category': 'physics_informed_parameters',
        'generalization_method': 'physics_informed'
    },
    'data_weight': {
        'name': 'Data Weight',
        'description': 'Weight for observational data',
        'unit': 'dimensionless',
        'default': 1.0,
        'range': [0.0, 10.0],
        'category': 'physics_informed_parameters',
        'generalization_method': 'physics_informed'
    },
    
    # Multi-Scale Parameters
    'multi_scale_training': {
        'name': 'Multi-Scale Training',
        'description': 'Whether to use multi-scale training',
        'unit': 'dimensionless',
        'default': False,
        'range': [True, False],
        'category': 'multi_scale_parameters',
        'generalization_method': 'multi_scale'
    },
    'scale_factors': {
        'name': 'Scale Factors',
        'description': 'Scale factors for multi-scale training',
        'unit': 'dimensionless',
        'default': [0.5, 1.0, 2.0],
        'range': [0.1, 10.0],
        'category': 'multi_scale_parameters',
        'generalization_method': 'multi_scale'
    },
    'scale_weights': {
        'name': 'Scale Weights',
        'description': 'Weights for different scales',
        'unit': 'dimensionless',
        'default': [1.0, 1.0, 1.0],
        'range': [0.0, 10.0],
        'category': 'multi_scale_parameters',
        'generalization_method': 'multi_scale'
    },
    
    # Curriculum Learning Parameters
    'curriculum_learning': {
        'name': 'Curriculum Learning',
        'description': 'Whether to use curriculum learning',
        'unit': 'dimensionless',
        'default': False,
        'range': [True, False],
        'category': 'curriculum_parameters',
        'generalization_method': 'curriculum_learning'
    },
    'difficulty_metric': {
        'name': 'Difficulty Metric',
        'description': 'Metric for measuring sample difficulty',
        'unit': 'dimensionless',
        'default': 'loss',
        'range': ['loss', 'gradient', 'uncertainty'],
        'category': 'curriculum_parameters',
        'generalization_method': 'curriculum_learning'
    },
    'curriculum_schedule': {
        'name': 'Curriculum Schedule',
        'description': 'Schedule for curriculum progression',
        'unit': 'dimensionless',
        'default': 'linear',
        'range': ['linear', 'exponential', 'step'],
        'category': 'curriculum_parameters',
        'generalization_method': 'curriculum_learning'
    },
    
    # Validation Parameters
    'validation_frequency': {
        'name': 'Validation Frequency',
        'description': 'Frequency of validation during training',
        'unit': 'dimensionless',
        'default': 100,
        'range': [10, 1000],
        'category': 'validation_parameters',
        'generalization_method': 'validation'
    },
    'early_stopping': {
        'name': 'Early Stopping',
        'description': 'Whether to use early stopping',
        'unit': 'dimensionless',
        'default': True,
        'range': [True, False],
        'category': 'validation_parameters',
        'generalization_method': 'validation'
    },
    'patience': {
        'name': 'Patience',
        'description': 'Patience for early stopping',
        'unit': 'dimensionless',
        'default': 100,
        'range': [10, 1000],
        'category': 'validation_parameters',
        'generalization_method': 'validation'
    },
    
    # Model Selection Parameters
    'model_selection': {
        'name': 'Model Selection',
        'description': 'Method for model selection',
        'unit': 'dimensionless',
        'default': 'validation_loss',
        'range': ['validation_loss', 'aic', 'bic', 'cross_validation'],
        'category': 'model_selection_parameters',
        'generalization_method': 'model_selection'
    },
    'hyperparameter_tuning': {
        'name': 'Hyperparameter Tuning',
        'description': 'Method for hyperparameter tuning',
        'unit': 'dimensionless',
        'default': 'grid_search',
        'range': ['grid_search', 'random_search', 'bayesian', 'genetic'],
        'category': 'model_selection_parameters',
        'generalization_method': 'model_selection'
    }
} 