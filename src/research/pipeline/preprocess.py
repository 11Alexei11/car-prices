from typing import Dict

import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler

from config import Config
from utils import save_bin


def load_dataset(launch_mode: str) -> pd.DataFrame:
    """Function to load dataset from file

    Returns:
        pd.DataFrame: Dataset
    """
    config = Config()

    if launch_mode == "train":
        path_to_dataset = config.path_to_train
    elif launch_mode == "test":
        path_to_dataset = config.path_to_test

    return pd.read_csv(path_to_dataset).drop_duplicates().dropna()


def preprocess_carname(string: pd.Series):
    return string.split(' ')[0].lower()


def preprocess_string(df: pd.DataFrame, encoders: Dict[str, OneHotEncoder], mode: str) -> pd.DataFrame:
    df['CarName'] = df['CarName'].apply(preprocess_carname)
    import warnings
    warnings.filterwarnings('ignore')
    for col_name in encoders:
        print(f'encoding: {col_name}')
        if mode == "train":
            df[col_name] = encoders[col_name].fit_transform(df[col_name].values.reshape(-1, 1))
        elif mode == "test":
            df[col_name] = encoders[col_name].transform(df[col_name].values.reshape(-1, 1))

    return df


def scale(df: pd.DataFrame, scalers: Dict[str, MinMaxScaler], mode: str) -> pd.DataFrame:
    for col_name in scalers:
        print(f'start scaling: {col_name}')
        if mode == "train":
            df[col_name] = scalers[col_name].fit_transform(df[col_name].values.reshape(-1, 1))
        elif mode == "test":
            df[col_name] = scalers[col_name].transform(df[col_name].values.reshape(-1, 1))

    return df


def main() -> None:
    config = Config()
    dataset = {"train": {"x": None, "y": None}, "test": {"x": None, "y": None}}

    dataset["train"]["x"] = load_dataset(launch_mode="train").set_index("car_ID")
    dataset["test"]["x"] = load_dataset(launch_mode="test").set_index("car_ID")

    scalers = {col_name: MinMaxScaler()
                          for col_name in dataset["train"]["x"].select_dtypes(include=['float64', 'int64']).columns}

    dataset["train"]["x"] = scale(dataset["train"]["x"], scalers, mode="train")
    dataset["test"]["x"] = scale(dataset["test"]["x"], scalers, mode="test")

    string_columns = [column for column in dataset["train"]["x"].select_dtypes(include=['object']).columns]
    string_encoders = {name: LabelEncoder() for name in string_columns}
    dataset["train"]["x"] = preprocess_string(dataset["train"]["x"], string_encoders, mode="train")
    dataset["test"]["x"] = preprocess_string(dataset["test"]["x"], string_encoders, mode="test")
    print('all columns were scaled')

    dataset["train"]["y"] = dataset["train"]["x"].pop(config.preprocess_target_col_name).values
    dataset["test"]["y"] = dataset["test"]["x"].pop(config.preprocess_target_col_name).values

    # save preprocessors
    save_bin(artifact=string_encoders, path_to_save=config.string_encoders_path)
    save_bin(artifact=scalers, path_to_save=config.scalers_path)

    # save dataset
    save_bin(artifact=dataset["train"]["x"], path_to_save=config.preprocess_x_train_preprocessed_path)
    save_bin(artifact=dataset["train"]["y"], path_to_save=config.preprocess_y_train_preprocessed_path)

    save_bin(artifact=dataset["test"]["x"], path_to_save=config.preprocess_x_test_preprocessed_path)
    save_bin(artifact=dataset["test"]["y"], path_to_save=config.preprocess_y_test_preprocessed_path)


if __name__ == "__main__":
    main()
