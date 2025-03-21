import logging
import os
import inspect

def custom_logger(log_level=logging.DEBUG):
    # Set class/method name from where it's called
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)

    # Ensure the logs directory exists
    log_dir = "../logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Create file handler
    try:
        fh = logging.FileHandler(os.path.join(log_dir, "automation.log"), mode='a')
    except Exception as e:
        print(f"Failed to create log file: {e}")
        return None

    # Create log formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    fh.setFormatter(formatter)

    # Add handler
    if not logger.hasHandlers():
        logger.addHandler(fh)

    logger.propagate = False
    return logger

# Test the logger
logger = custom_logger()
if logger:
    logger.info("This is an info log for testing.")
    logger.error("This is an error log for testing.")
