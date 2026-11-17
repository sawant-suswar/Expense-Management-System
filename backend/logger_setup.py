import logging


def setup_logger(name,file_name="app.log",log_level=logging.DEBUG):
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    file_Handler = logging.FileHandler(file_name)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_Handler.setFormatter(formatter)
    logger.addHandler(file_Handler)
    return logger

