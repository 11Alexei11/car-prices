import os
import pickle as pkl
import json

from xgboost import XGBRegressor
from sklearn.metrics import r2_score as r2, mean_absolute_percentage_error as mape, mean_absolute_error as mae
from dvclive import Live
from sklearn.preprocessing import MinMaxScaler

import numpy as np

from src.research.pipeline.config import Config
from src.research.pipeline.utils import save_bin, load_bin, descale


def main() -> None:
    config = Config()
    model: XGBRegressor = load_bin(path_to_load=config.train_model_path)

    x_test_preprocessed: np.ndarray = load_bin(config.preprocess_x_test_preprocessed_path)
    y_test_scaled: np.ndarray = load_bin(config.preprocess_y_test_preprocessed_path)
    target_scaler: MinMaxScaler = load_bin(config.scalers_path)[config.preprocess_target_col_name]

    predictions = descale(model.predict(x_test_preprocessed).reshape(-1, 1), target_scaler)
    y_test = descale(y_test_scaled.reshape(-1, 1), target_scaler)

    metrics = {
        "mae": mae(y_test, predictions),
        "mape": mape(y_test, predictions),
        "r2": r2(y_test, predictions)
    }

    print(f"evaluate metrics directory: {config.evaluate_metrics_dir}")
    os.makedirs(config.evaluate_metrics_dir, exist_ok=True)
    with open(os.path.join(config.evaluate_metrics_dir, "metrics.json"), 'w') as f:
        json.dump(metrics, f)

    with Live(dir=config.evaluate_metrics_dir) as live:
        for metric_name, value in metrics.items():
            live.log_metric(name=metric_name, val=value)

    with open(os.path.join(config.evaluate_metrics_dir, "predictions.json"), "w") as f:
        json.dump({"predictions": [(str(prediction), str(target)) for prediction, target in zip(predictions.flatten(),
                                                                                      y_test.flatten())]}, f, indent=4)


if __name__=="__main__":
    main()
