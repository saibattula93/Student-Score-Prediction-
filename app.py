import sys
from src.student_score_prediction.logger import logging
from src.student_score_prediction.exception import CustomException
from src.student_score_prediction.components.data_ingestion import DataIngestion
from src.student_score_prediction.components.data_ingestion import DataIngestionConfig
from src.student_score_prediction.components.data_transformation import DataTransformationConfig,DataTransformation
from src.student_score_prediction.components.model_tranier import ModelTrainerConfig,ModelTrainer



if __name__ == '__main__':
    logging.info("The execution has started")
    
    try:
        #data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        train_data_path,test_data_path = data_ingestion.initiate_data_ingestion()

        data_transformation = DataTransformation()
        train_arr,test_arr,_=data_transformation.initiate_data_transormation(train_data_path,test_data_path)


        model_trainer=ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr,test_arr))
        
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)
        