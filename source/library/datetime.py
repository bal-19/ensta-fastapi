from datetime import datetime


class Datetime:
    @staticmethod
    def now():
        return datetime.now()
    
    @staticmethod
    def timestamp():
        return datetime.now().timestamp()
    
    @staticmethod
    def formatted_date():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")