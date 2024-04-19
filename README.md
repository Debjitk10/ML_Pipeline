# House Price Prediction Project

This project aims to develop an end-to-end machine learning solution for predicting house prices based on various features such as housing median age, total rooms, total bedrooms, population, households, median income, and ocean proximity.

## Project Structure

The project is structured as follows:


## Description

- **README.md**: Contains information about the project, how to set it up, and usage instructions.
- **requirements.txt**: Lists all the dependencies required to run the project.
- **setup.py**: Defines the project as a package and specifies its dependencies.
- **.gitignore**: Specifies files and directories to be ignored by Git.
- **src**: Source directory containing all the Python code.
    - **__init__.py**: Initializes the src directory as a Python package.
    - **exception.py**: Defines custom exception classes.
    - **logger.py**: Defines logging configuration and utilities.
    - **utils.py**: Contains utility functions used across the project.
    - **components**: Subdirectory containing modular components of the pipeline.
        - **__init__.py**: Initializes the components package.
        - **data_ingestion.py**: Module for data ingestion functionality.
        - **data_transformation.py**: Module for data transformation functionality.
        - **model_trainer.py**: Module for training machine learning models.
    - **pipeline**: Subdirectory containing pipeline scripts.
        - **__init__.py**: Initializes the pipeline package.
        - **train_pipeline.py**: Script to initiate the training pipeline.
        - **prediction_pipeline.py**: Script to initiate the prediction pipeline.


## Getting Started

### Prerequisites
- Python 3.10
- Anaconda or Miniconda (optional)

### Setup
1. Clone this repository to your local machine.
2. Create a new virtual environment:
    ```bash
    conda create -p venv python=3.10
    conda activate venv
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Create Source Directory
Create a directory named src at the root of your project. This directory will contain all the source code for your project.

5. Create Subdirectories
Within the src directory, create the following subdirectories:

5.1. components
This directory will include the following components: data_ingestion, data_transformation, model_trainer, and init.py. These components are interconnected for future use.

5.2. pipeline
Create a folder named pipeline within the src directory. This folder will contain two Python files: training_pipeline.py and prediction_pipeline.py, along with an init.py file.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue if you encounter any problems or have suggestions for improvement.

## Acknowledgements
Special thanks to the contributors and developers of the libraries and tools used in this project.

## Authors
- [Debjit Kundu](https://github.com/Debjitk10)
