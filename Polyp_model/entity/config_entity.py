import os
from dataclasses import dataclass
from torch import device
from Polyp_model.constant.training_pipeline import *


@dataclass
class DataIngestionConfig:
    def __init__(self):
        self.data_folder:str = DATA_FOLDER
        #self.artifact_dir:str = os.path.join(ARTIFACT_DIR, TIMESTAMP)
        self.data_path:str = os.path.join(
            self.data_folder
        )
        self.train_data_path:str = os.path.join(self.data_path, "TrainDataset")
        self.test_data_path:str = os.path.join(self.data_path, "TestDataset")