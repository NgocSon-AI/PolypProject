import sys

from Polyp_model.exception import PolypException
from Polyp_model.pipeline.training_pipeline import TrainPipeline


def start_model():
    try:
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()
    except Exception as e:
        raise PolypException(e, sys)
    
if __name__ == '__main__':
    start_model()
