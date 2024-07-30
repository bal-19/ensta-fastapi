import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Logging:
    @staticmethod
    def info(message: str):
        logging.info(message)

    @staticmethod
    def error(message: str):
        logging.error(message)
        
    @staticmethod
    def warning(message: str):
        logging.warning(message)