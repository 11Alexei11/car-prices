import numpy as np
import pandas as pd
import re
from typing import Dict, List
from sklearn.ensemble import VotingRegressor
from sklearn.preprocessing import LabelEncoder, PolynomialFeatures
from sklearn.decomposition import PCA


class ColumnNames:
    LEVY = "levy"
    PROD_YEAR = "prod_year" 
    LEATHER_INTERIOR = "leather_interior"
    MILEAGE = "mileage"
    CYLINDERS = "cylinders"
    AIRBUGS = "airbugs"
    ID = "id"
    USER_ID = "user_id"
    LEVY = "levy"
    MANUFACTURER = "manufacturer"
    MODEL = "model"
    PROD_YEAR = "prod_year"
    CATEGORY = "category"
    LEATHER_INTERIOR = "leather_interior"
    FUEL_TYPE = "fuel_type"
    ENGINE_VOLUME = "engine_volume"
    MILEAGE = "mileage"
    CYLINDERS = "cylinders"
    GEAR_BOX_TYPE = "gear_box_type"
    DRIVE_WHEELS = "drive_wheels"
    DOORS = "doors"
    WHEEL = "wheel"
    COLOR = "color"
    AIRBUGS = "airbugs"
    PRICE = "price"

    @classmethod
    def numeric_column_names(cls):
        return [
            cls.LEVY,
            cls.PROD_YEAR, 
            cls.LEATHER_INTERIOR,
            cls.MILEAGE,
            cls.CYLINDERS,
            cls.AIRBUGS
        ]

    @classmethod
    def string_column_names(cls):
        return [
            cls.MANUFACTURER,
            cls.MODEL,
            cls.CATEGORY,
            cls.FUEL_TYPE,
            cls.ENGINE_VOLUME,
            cls.GEAR_BOX_TYPE,
            cls.DRIVE_WHEELS,
            cls.DOORS,
            cls.WHEEL,
            cls.COLOR
        ]


class FullPipelineRegressor:
    def __init__(self, 
                 model: VotingRegressor,
                 pca_converter: PCA,
                 string_encoders: Dict[str, LabelEncoder],
                 feature_extender: PolynomialFeatures):

        self._model = model
        self._pca_converter = pca_converter
        self._string_encoders = string_encoders
        self._feature_extender = feature_extender

    def __preprocess_mileage(self, mileage_string):
        return int(re.search("\d+", mileage_string).group(0))

    def __preprocess_strings(self, x: pd.DataFrame):
        encoded_df = x.copy()
        for col in encoded_df.columns:
            encoded_df.rename(columns={col: col.lower().replace(' ', '_')}, inplace=True)

        col_name = 'levy'
        encoded_df[col_name] = encoded_df[col_name].replace({'-': '0'}).astype(np.uint16)

        col_name = 'mileage'
        encoded_df[col_name] = encoded_df[col_name].apply(self.__preprocess_mileage)

        for col_name, encoder in self._string_encoders.items():
            print(col_name)
            encoded_df[col_name] = encoder.transform(encoded_df[col_name])

        return encoded_df
    
    def __pca_convert(self, x_df: pd.DataFrame):
        x_np = x_df.values
        pca_transformed = self._pca_converter.transform(x_np)[:, :3]

        return pca_transformed
    
    def __feature_extend(self, x_pca_transformed: List):
        x_features_extended = self._feature_extender.transform(x_pca_transformed)
        
        return x_features_extended
        
    def __preprocess(self, x: pd.DataFrame):
        x_encoded_strings = self.__preprocess_strings(x)
        x_pca_transformed = self.__pca_convert(x_encoded_strings)
        x_extended = self.__feature_extend(x_pca_transformed)

        return x_extended

    def __denorm_predict(self, x_preprocessed):
        return np.expm1(self._model.predict(x_preprocessed))

    def predict(self, x):
        x_preprocessed = self.__preprocess(x)

        return self.__denorm_predict(x_preprocessed)
