import os
import sys
import pandas as pd
from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from src.utils import save_function, load_obj  # Corrected import statement
from dataclasses import dataclass

@dataclass
class ModelTrainerConfig:
    trained_model_file_path: str = os.path.join('artifacts', 'model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_training(self, train_data_path, preprocessor_obj_file_path):
        try:
            logging.info('Model training initiated')

            # Load preprocessor object
            preprocessor = load_obj(preprocessor_obj_file_path)  # Corrected function name
            logging.info('Preprocessor object loaded')

            # Read train data
            train_df = pd.read_csv(train_data_path)
            X_train = train_df.drop(columns=['median_house_value'], axis=1)
            y_train = train_df['median_house_value']

            # Transform features using preprocessor
            X_train_transformed = preprocessor.transform(X_train)
            logging.info('Features transformed using preprocessor')

            # Split data into train and validation sets
            X_train_final, X_val, y_train_final, y_val = train_test_split(X_train_transformed, y_train, test_size=0.2, random_state=42)
            logging.info('Data split into train and validation sets')

            # Initialize and train the model
            model = LinearRegression()
            model.fit(X_train_final, y_train_final)
            logging.info('Model trained successfully')

            # Save the trained model
            save_function(self.model_trainer_config.trained_model_file_path, model)
            logging.info('Trained model saved')

            return self.model_trainer_config.trained_model_file_path

        except Exception as e:
            logging.error('Error occurred during model training')
            raise CustomException(e, sys)

# Instantiate the ModelTrainer class and call the initiate_model_training method
model_trainer = ModelTrainer()
model_trainer.initiate_model_training(train_data_path='artifacts/train.csv', preprocessor_obj_file_path='artifacts/preprocessor.pkl')
