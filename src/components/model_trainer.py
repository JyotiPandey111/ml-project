

import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging

# importing the defined functions from utils.py
from src.utils import save_object,evaluate_models

logging.info("All the required libraries are successfully imported in training model")


@dataclass

# creating class to set the file path for the saving model
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")

logging.info("trained_model_file_path successfully created model.pkl")


# creating class for model trainig
class ModelTrainer:
    def __init__(self):
        # inheriting the model file 
        self.model_trainer_config=ModelTrainerConfig()


    def initiate_model_trainer(self,train_array,test_array):
        """
        to perform training of the model
        """
        try:
            logging.info("Split training and test input data")
            # splitting the data
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            # creating the dic of the models
            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "K-Neighbors Classifier": KNeighborsRegressor(),
                "XGBClassifier": XGBRegressor(),
                "CatBoosting Classifier": CatBoostRegressor(verbose=False),
                "AdaBoost Classifier": AdaBoostRegressor(),
            }

            # calling a function from utils.py to evaluate the model and creating a dic
            model_report:dict=evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,
                                             models=models)
            

            ## To get best model score from dict
            best_model_score = max(sorted(model_report.values()))


            ## To get best model name from dict
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]


            if best_model_score<0.6:
                raise CustomException("No best model found")
            logging.info(f"Best found model on both training and testing dataset,{best_model_name}")

            # calling a function from utils.py to save the model in defined path in config class
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted=best_model.predict(X_test)

            r2_square = r2_score(y_test, predicted)
            return r2_square, best_model_name
            



            
        except Exception as e:
            raise CustomException(e,sys)