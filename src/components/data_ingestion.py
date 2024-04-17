import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    # Specify the full path to the directory where 'artifacts' should be created
    base_directory: str = r'C:\Users\user\OneDrive\Desktop\ML_pipeline'
    train_data_path: str = os.path.join(base_directory, 'artifacts', 'train.csv')
    test_data_path: str = os.path.join(base_directory, 'artifacts', 'test.csv')
    raw_data_path: str = os.path.join(base_directory, 'artifacts', 'raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        print("Base directory:", self.ingestion_config.base_directory)
        logging.info('Data Ingestion methods Starts')
        try:
            df = pd.read_csv(os.path.join(self.ingestion_config.base_directory, 'housing.csv'))
            logging.info('Dataset read as pandas Dataframe')

            # Create 'artifacts' directory if it doesn't exist
            artifacts_directory = os.path.join(self.ingestion_config.base_directory, 'artifacts')
            print("Artifacts directory path:", artifacts_directory)
            if not os.path.exists(artifacts_directory):
                os.makedirs(artifacts_directory)
                print("Artifacts directory created successfully")
            else:
                print("Artifacts directory already exists")

            df.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info('Raw data saved')

            logging.info('Train test split')
            train_set, test_set = train_test_split(df, test_size=0.30, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info('Ingestion of Data is completed')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.error('Exception occurred at Data Ingestion stage')
            raise CustomException(e, sys)

# Instantiate the DataIngestion class and call the initiate_data_ingestion method
data_ingestion = DataIngestion()
data_ingestion.initiate_data_ingestion()
