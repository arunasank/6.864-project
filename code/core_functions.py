# core_functions.py
"""Functions to be imported across multiple notebooks for easier transerability"""

from sklearn import metrics


def evaluate_model(predictions, observations, scaling, name, eval_metrics=None):
    """Evaluate model predictions

    :param predictions: array of binary model predictions
    :param observations: array of observed binary values
    :param scaling: array of scaling factor for each observation
    :param name: name of model, to be output with performance_dict
    :param eval_metrics: dictionary of metrics from sklearn to evaluate. If None,
    function will use accuracy, f1, precision, recall, and roc-auc
    :return: dict of model performance
    """
    if eval_metrics is None:
        eval_metrics = {'accuracy': metrics.accuracy_score,
                        'f1': metrics.f1_score,
                        'precision': metrics.precision_score,
                        'recall': metrics.recall_score,
                        'roc-auc': metrics.roc_auc_score}
        performance_dict = {}
        for metric_name, metric in eval_metrics.items():
            performance_dict[metric_name] = metric(observations, predictions,
                                                   sample_weight=scaling)
        performance_dict['name'] = name
        return performance_dict