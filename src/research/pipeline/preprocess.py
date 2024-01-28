from typing import Dict, List
import re

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, PolynomialFeatures
from sklearn.decomposition import PCA


class Preprocess:
    def __init__(self,
                 pca_converter: PCA,
                 string_encoders: Dict[str, LabelEncoder],
                 feature_extender: PolynomialFeatures) -> None:
        self._string_encoders = string_encoders
        self._pca_converter = pca_converter
        self._feature_extender = feature_extender

    def __preprocess_mileage(self, mileage_string):
        return int(re.search("\d+", mileage_string).group(0))

    def __preprocess_string(self, x: pd.DataFrame, is_train: bool):
        encoded_df = x.copy()
        for col in encoded_df.columns:
            encoded_df.rename(columns={col: col.lower()}, inplace=True)

        col_name = 'levy'
        encoded_df[col_name] = encoded_df[col_name].replace({'-': '0'}).astype(np.uint16)

        col_name = 'mileage'
        encoded_df[col_name] = encoded_df[col_name].apply(self.__preprocess_mileage)

        for col_name, encoder in self._string_encoders.items():
            print(col_name)
            if is_train:
                encoded_df[col_name] = encoder.fit_transform(encoded_df[col_name])
            else:
                encoded_df[col_name] = encoder.transform(encoded_df[col_name])

        return encoded_df

    def __pca_convert(self, x_df: pd.DataFrame, is_train: bool):
        x_np = x_df.values
        if is_train:
            pca_transformed = self._pca_converter.fit_transform(x_np)[:, :3]   
        else:
            pca_transformed = self._pca_converter.transform(x_np)[:, :3]

        return pca_transformed

    def __feature_extend(self, x_pca_transformed: List):
        x_features_extended = self._feature_extender.transform(x_pca_transformed)

        return x_features_extended
    
    def __preprocess_targets(self, y):
        return np.log1p(y)
    
    def deconvert_target(self, predicted_y):
        return np.expm1(predicted_y)
    
    def preprocess(self, x: pd.DataFrame, y: pd.DataFrame, is_train: bool = False):
        x_encoded_strings = self.__preprocess_string(x, is_train)
        x_pca_transformed = self.__pca_convert(x_encoded_strings, is_train)
        x_extended = self.__feature_extend(x_pca_transformed)
        y = self.__preprocess_targets(y)

        return x_extended, y