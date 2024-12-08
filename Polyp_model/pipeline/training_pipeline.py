import sys

from Polyp_model.logger import logging
from Polyp_model.exception import PolypException

from Polyp_model.components.data_ingestion import DataIngestion

from Polyp_model.entity.config_entity import (
    DataIngestionConfig,
)

from Polyp_model.entity.artifacts_entity import (
    DataIngestionArtifact,
)

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
    
    def start_data_ingestion(self)->DataIngestionArtifact:
        logging.info("Entered the start_data_ingestion method of TrainPipeline class.")
        try:
            logging.info("Getting the data.")
            data_ingestion = DataIngestion(
                data_ingestion_config=self.data_ingestion_config,
            )
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the train-dataset and test-dataset.")
            logging.info("Excited the start_data_ingestion method of TrainPipeline class.")
            return data_ingestion_artifact
        except Exception as e:
            raise PolypException(e, sys)
        
    def run_pipeline(self)->None:
        logging.info("Entered the run_pipeline method of TrainPipeline class.")
        try:
            data_ingestion_artifact:DataIngestionArtifact = self.start_data_ingestion()
            logging.info("Exited the run_pipeline method of TrainPipeline class.")
        except Exception as e:
            raise PolypException(e, sys)