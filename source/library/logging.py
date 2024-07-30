import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Logging:
    @staticmethod
    def info(message: str):
        """
        Log info

        Args:
            message (str): message to log
        """
        logging.info(message)

    @staticmethod
    def error(message: str):
        """
        Log error

        Args:
            message (str): message to log
        """
        logging.error(message)
        
    @staticmethod
    def warning(message: str):
        """
        Log warning

        Args:
            message (str): message to log
        """
        logging.warning(message)