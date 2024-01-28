from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures, LabelEncoder
from sklearn.decomposition import PCA

from sklearn.metrics import r2_score, mean_squared_error as mse, mean_absolute_percentage_error as mape

import os

from preprocess import Preprocess
from utils import save_bin


def train(
        model,
        X_train,
        y,
        path_to_save_model: str = None):
    cat_columns = [col for col in X_train.columns if X_train[col].dtype == 'object']

    encoders = []
    for _ in range(len(cat_columns)):
        encoders.append(LabelEncoder())

    encoders = {col.lower().replace(' ', '_'): encoder for col, encoder in zip(cat_columns, encoders)}
    pca = PCA()
    fp = PolynomialFeatures(degree=3)

    preprocessor = Preprocess(
        pca_converter=pca,
        string_encoders=encoders,
        feature_extender=fp
    )

    X_train_preprocessed, y_preprocessed = preprocessor.preprocess(X_train, y, is_train=True)

    model.fit(X_train_preprocessed, y_preprocessed)

    if os.path.exists(path_to_save_model):
        save_bin(model, path_to_save_model)

    return model