import logging
import os
from datetime import datetime


def get_logger():
    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger("assignment5_logger")
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger

    log_file = os.path.join("logs", f"test_run_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger
