import logging
import os
from datetime import datetime

LOGFILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
LOGS_PATH = os.path.join(os.getcwd(), "logs")
os.makedirs(LOGS_PATH, exist_ok=True)
LOGFILE_PATH = os.path.join(LOGS_PATH, LOGFILE) 

logging.basicConfig(
    filename=LOGFILE_PATH,
    format="[%(asctime)s] %(lineno)d - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)   

if __name__ == "__main__":
    logging.info("Logging has started.")