import os
import sys
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder, StandardScaler
from src.exception import CustomException
from src.logger import logging
from src.utils import save_function
from dataclasses import dataclass

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformation_object(self):
        try:
            logging.info('Data Transformation initiated')

            # Define which columns should be ordinal-encoded and which should be scaled
            categorical_cols = ['ocean_proximity']
            numerical_cols = ['housing_median_age', 'total_rooms', 'total_bedrooms',
                              'population', 'households', 'median_income']

            # Define the custom ranking for each ordinal variable
            ocean_proximity_categories = ['<1H OCEAN', 'INLAND', 'NEAR OCEAN', 'NEAR BAY', 'ISLAND']

            logging.info('Pipeline Initiated')

            # Numerical Pipeline
            num_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='median')),
                ('scaler', StandardScaler())
            ])

            # Categorical Pipeline (No need for scaling)
            cat_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='most_frequent')),
                ('ordinalencoder', OrdinalEncoder(categories=[ocean_proximity_categories]))
            ])

            preprocessor = ColumnTransformer([
                ('num_pipeline', num_pipeline, numerical_cols),
                ('cat_pipeline', cat_pipeline, categorical_cols)
            ])

            logging.info('Pipeline Completed')

            return preprocessor

        except Exception as e:
            logging.error("Error in Data Transformation")
            raise CustomException(e, sys)

    def initiate_data_transformation(self, raw_data_path):
        try:
            # Read raw data
            raw_df = pd.read_csv(raw_data_path)
            logging.info('Raw data read successfully')

            # Obtain preprocessing object
            preprocessing_obj = self.get_data_transformation_object()

            # Separate features and target
            X = raw_df.drop(columns=['median_house_value', 'latitude', 'longitude'], axis=1)  # Exclude latitude and longitude
            y = raw_df['median_house_value']

            # Transform data
            X_transformed = preprocessing_obj.fit_transform(X)

            # Save preprocessing object
            save_function(self.data_transformation_config.preprocessor_obj_file_path, preprocessing_obj)
            logging.info('Preprocessor object saved')

            return X_transformed, np.array(y), self.data_transformation_config.preprocessor_obj_file_path

        except Exception as e:
            logging.error("Error in initiating data transformation")
            raise CustomException(e, sys)

# Instantiate the DataTransformation class and call the initiate_data_transformation method
data_transformation = DataTransformation()
data_transformation.initiate_data_transformation('artifacts/raw.csv')
