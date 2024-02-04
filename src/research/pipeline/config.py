from typing import Optional
import os

import yaml


class Config:
    """Class implements logic of configuration for pipeline training and inference"""

    def __init__(self, path_to_config: str = "/home/ares/work/car-price/configs/pipeline-config.yml"):
        """Method initializer

        Args:
            path_to_config (str): Path to configuration.yml file
        """
        if path_to_config is not None and os.path.exists(path_to_config):
            self._load_configuration(path_to_config)
        else:
            self._load_configuration()

        self.path_to_train: str = self._config_file["preprocess"]["dataset"]["path_to_train"]
        self.path_to_test: str = self._config_file["preprocess"]["dataset"]["path_to_test"]

        self.string_encoders_path: str = self._config_file["preprocess"]["string_encoders"]["path"]
        self.scalers_path: str = self._config_file["preprocess"]["scalers"]["path"]

        self.train_model_path: str = self._config_file["train"]["regressor"]["model_path"]
        self.train_train_share: str = self._config_file["train"]["train_share"]

        self.preprocess_x_train_preprocessed_path: str = self._config_file["preprocess"]["dataset"]["x_train_preprocessed_path"]
        self.preprocess_y_train_preprocessed_path: str = self._config_file["preprocess"]["dataset"]["y_train_preprocessed_path"]
        self.preprocess_x_test_preprocessed_path: str = self._config_file["preprocess"]["dataset"]["x_test_preprocessed_path"]
        self.preprocess_y_test_preprocessed_path: str = self._config_file["preprocess"]["dataset"]["y_test_preprocessed_path"]

        self.preprocess_target_col_name: str = self._config_file["preprocess"]["dataset"]["target_col_name"]

        self.evaluate_metrics_dir: str = self._config_file["evaluate"]["metrics_dir"]
        self.evaluate_plots_dir: str = self._config_file["evaluate"]["plots_dir"]

    def _load_configuration(self, path_to_config: Optional[str] = "/home/ares/work/car-price/configs/pipeline-config.yml") -> None:
        """Method for load configuration file

        Args:
            path_to_config (Optional[str], optional): Default path of configuration file. Defaults to "/home/ares/work/car-price/configs/pipeline-config.yml".
        """
        with open(path_to_config, 'r') as f:
            self._config_file = yaml.safe_load(f)