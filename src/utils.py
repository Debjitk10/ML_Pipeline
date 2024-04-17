import os
import csv
import mysql.connector
import sys 
import pickle 
from src.exception import CustomException
from sklearn.metrics import r2_score
from src.logger import logging

def save_function(file_path, obj): 
    dir_path = os.path.dirname(file_path)
    os.makedirs(dir_path, exist_ok= True)
    with open (file_path, "wb") as file_obj: 
        pickle.dump(obj, file_obj)

def model_performance(X_train, y_train, X_test, y_test, models): 
    try: 
        report = {}
        for i in range(len(models)): 
            model = list(models.values())[i]
# Train models
            model.fit(X_train, y_train)
# Test data
            y_test_pred = model.predict(X_test)
            #R2 Score 
            test_model_score = r2_score(y_test, y_test_pred)
            report[list(models.keys())[i]] = test_model_score
        return report

    except Exception as e: 
        raise CustomException(e,sys)

# Function to load a particular object 
def load_obj(file_path):
    try: 
        with open(file_path, 'rb') as file_obj: 
            return pickle.load(file_obj)
    except Exception as e: 
        logging.info("Error in load_object fuction in utils")
        raise CustomException(e,sys)

def fetch_table_data(table_name):
    try:
        # Establish connection to MySQL server
        cnx = mysql.connector.connect(
            host='localhost',
            database='housingdb',
            user='root',
            password='Debjit@2002',
            auth_plugin='mysql_native_password'
        )
        cursor = cnx.cursor()
        
        # Execute query to fetch data from the specified table
        cursor.execute(f'SELECT * FROM {table_name}')
        
        # Get column names (header)
        header = [row[0] for row in cursor.description]
        
        # Fetch all rows
        rows = cursor.fetchall()
        
        # Closing connection
        cnx.close()
        
        return header, rows
    except mysql.connector.Error as err:
        print("Error:", err)
        return None, None

def export(table_name):
    header, rows = fetch_table_data(table_name)
    if header and rows:
        # Define CSV filename
        csv_filename = f'{table_name}.csv'
        # Write data to CSV file
        with open(csv_filename, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            # Write header
            csv_writer.writerow(header)
            # Write rows
            csv_writer.writerows(rows)
        print(f"{len(rows)} rows written successfully to {csv_filename}") 
    else:
        print("Failed to fetch data from the database.")

# Example usage
export('housing')
