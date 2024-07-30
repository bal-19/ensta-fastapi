from datetime import datetime


class Datetime:
    @staticmethod
    def now():
        """
        Get current datetime

        Returns:
            datetime: current datetime
        """
        return datetime.now()
    
    @staticmethod
    def timestamp():
        """
        Get current timestamp

        Returns:
            int: current timestamp
        """
        return datetime.now().timestamp()
    
    @staticmethod
    def formatted_date():
        """
        Get current formatted date

        Returns:
            str: current formatted date
        """
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")