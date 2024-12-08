import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Polyp_model.logger import logging
from Polyp_model.exception import PolypException

from Polyp_model.entity.config_entity import DataIngestionConfig
from Polyp_model.entity.artifacts_entity import DataIngestionArtifact


class DataIngestion:
    def __init__(
        self,
        data_ingestion_config: DataIngestionConfig,
    ):
        self.data_ingestion_config = data_ingestion_config
    
    def get_data(self):
        try:
            logging.info("Entered the get_data method of DataIngestion class.")
            self.data_ingestion_config.data_path
            logging.info("Exited the get data method of DataIngestion class.")
        except Exception as e:
            raise PolypException(e, sys)
        
    def initiate_data_ingestion(self)->DataIngestionArtifact:
        logging.info("Entered the initiate_data_ingestion method of DataIngestion class.")
        try:
            self.get_data()
            data_ingestion_artifact:DataIngestionArtifact = DataIngestionArtifact(
                train_file_path=self.data_ingestion_config.train_data_path,
                test_file_path=self.data_ingestion_config.test_data_path
            )
            logging.info("Exited the initiate_data_ingestion method of DataIngestion class")
            return data_ingestion_artifact
        except Exception as e:
            raise PolypException(e, sys)