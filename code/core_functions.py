# core_functions.py
"""Functions to be imported across multiple notebooks for easier transerability"""

from sklearn import metrics


def evaluate_model(binary_preds, continuous_preds, observations, scaling, name,
                   binary_metrics=None, continuous_metrics=None):
    """Evaluate model predictions

    :param binary_preds: array of binary model predictions
    :param continuous_preds: array of continuous model predictions e.g. probabilities
    :param observations: array of observed binary values
    :param scaling: array of scaling factor for each observation
    :param name: name of model, to be output with performance_dict
    :param eval_metrics: dictionary of metrics from sklearn to evaluate. If None,
    function will use accuracy, f1, precision, recall, and roc-auc
    :return: dict of model performance
    """
    if binary_metrics is None:
        binary_metrics = {'accuracy': metrics.accuracy_score,
                          'f1': metrics.f1_score,
                          'precision': metrics.precision_score,
                          'recall': metrics.recall_score}
    if continuous_metrics is None:
        continuous_metrics = {'roc-auc': metrics.roc_auc_score,
                              'avg_precision': metrics.average_precision_score}
    performance_dict = {}
    for metric_name, metric in binary_metrics.items():
        performance_dict[metric_name] = metric(observations, binary_preds,
                                               sample_weight=scaling)
    for metric_name, metric in continuous_metrics.items():
        performance_dict[metric_name] = metric(observations, continuous_preds,
                                               sample_weight=scaling)

    performance_dict['name'] = name
    return performance_dict