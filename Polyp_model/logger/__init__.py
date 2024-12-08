import logging
import os

from Polyp_model.constant.training_pipeline import TIMESTAMP

LOG_FILE:str = f"{TIMESTAMP}.log"

logs_path = os.path.join(os.getcwd(), "Logs", TIMESTAMP)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Cấu hình định dạng thông báo bên trong file.log
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    # [ 2024-12-02 16:59:43,395 ] 17 root - INFO - Building the bento from bentofile.yaml
    level=logging.INFO
)