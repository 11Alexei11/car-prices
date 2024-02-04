import pickle as pkl
import os
from typing import Any, Dict, ByteString

from sklearn.preprocessing import MinMaxScaler
import numpy as np
from xgboost import XGBRegressor

# TModel = TypeVar("TModel", XGBRegressor)

def save_bin(artifact: ByteString, path_to_save: str) -> None:
    """Function to save bin

    Args:
        artifact (Bytestring): object to save
        path_to_save (str): Path to save
    """
    if not os.path.exists(os.path.dirname(path_to_save)):
        os.mkdir(os.path.dirname(path_to_save))

    with open(path_to_save, 'wb') as f:
        pkl.dump(artifact, f)


def load_bin(path_to_load: str) -> ByteString:
    """Function to load artifact

    Args:
        path_to_load (str): Path to string

    Returns:
        ByteString: Artifact
    """
    if os.path.exists(path_to_load):
        with open(path_to_load, 'rb') as f:
            return pkl.load(f)


def get_artifact(mode, artifact_class, artifact_path, params_dict: Dict[str, Any]):
    if mode == "train":
        artifact = artifact_class(**params_dict)
    else:
        artifact = load_bin(artifact_path)

    return artifact


def scale(y: np.ndarray):
    return np.log1p(y)


def descale(y_scaled: np.ndarray, scaler: MinMaxScaler) -> np.ndarray:
    return scaler.inverse_transform(y_scaled)

class ColumnNames:
    MILEAGE = "mileage"


class LaunchMode:
    TRAIN = "train"
    TEST = "test"