import os
import sys
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_train import ModelTrainer
from src.logger import logging
from src.exception import CustomException

if __name__ == "__main__":
    try:
        # Initialize DataIngestion and ingest data
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

        # Initialize DataTransformation and transform data
        data_transformation = DataTransformation()
        train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data_path)

        # Initialize ModelTrainer and train the model
        model_trainer = ModelTrainer()
        model_trainer.initiate_model_training(train_arr, test_arr)

        logging.info("Training pipeline completed successfully.")

    except CustomException as e:
        logging.error(f"Error occurred: {e}")
        sys.exit(1)
