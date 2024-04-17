import sys 
import os 
import pandas as pd
from src.exception import CustomException 
from src.logger import logging 
from src.utils import load_obj

class PredictPipeline: 
    def __init__(self) -> None:
        pass

    def predict(self, features): 
        try: 
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
            model_path = os.path.join("artifacts", "model.pkl")

            preprocessor = load_obj(preprocessor_path)
            model = load_obj(model_path)

            data_scaled = preprocessor.transform(features)
            pred = model.predict(data_scaled)
            return pred
        except Exception as e: 
            logging.info("Error occurred in predict function in prediction_pipeline location")
            raise CustomException(e, sys)
        
class CustomData: 
    def __init__(self, 
                 housing_median_age: float, 
                 total_rooms: float, 
                 total_bedrooms: float, 
                 population: float, 
                 households: float, 
                 median_income: float, 
                 ocean_proximity: str): 
        self.housing_median_age = housing_median_age
        self.total_rooms = total_rooms
        self.total_bedrooms = total_bedrooms
        self.population = population
        self.households = households
        self.median_income = median_income
        self.ocean_proximity = ocean_proximity
        
    def get_data_as_dataframe(self): 
        try: 
            custom_data_input_dict = {
                'housing_median_age': [self.housing_median_age], 
                'total_rooms': [self.total_rooms],
                'total_bedrooms': [self.total_bedrooms],
                'population': [self.population], 
                'households': [self.households], 
                'median_income': [self.median_income], 
                'ocean_proximity': [self.ocean_proximity]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info("Dataframe created")
            return df
        except Exception as e:
            logging.info("Error occurred in get_data_as_dataframe function in prediction_pipeline")
            raise CustomException(e, sys) 
