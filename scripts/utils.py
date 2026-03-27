import logging
from typing import Callable, Dict, List, Optional

class Utils:
    @staticmethod
    def is_valid_email(email: str) -> bool:
        import re
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return bool(re.match(pattern, email))

    @staticmethod
    def is_valid_password(password: str) -> bool:
        import re
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"
        return bool(re.match(pattern, password))

    @staticmethod
    def validate_input(input_dict: Dict[str, str]) -> Dict[str, str]:
        errors = {}
        for field, value in input_dict.items():
            if not value:
                errors[field] = f"{field} is required"
        return errors

    @staticmethod
    def convert_to_dict(data: List[Dict[str, str]]) -> Dict[str, List[Dict[str, str]]]:
        result = {}
        for item in data:
            key = item.get("id")
            if key not in result:
                result[key] = []
            result[key].append(item)
        return result

    @staticmethod
    def format_datetime(date_time: str) -> str:
        import datetime
        return datetime.datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M")

    @staticmethod
    def format_date(date: str) -> str:
        import datetime
        return datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d")

    @staticmethod
    def get_logger() -> logging.Logger:
        return logging.getLogger(__name__)

    @staticmethod
    def get_logger_instance(logger_name: str) -> logging.Logger:
        return logging.getLogger(logger_name)

    @staticmethod
    def format_phone_number(phone_number: str) -> str:
        return phone_number.replace(" ", "")

    @staticmethod
    def get_current_time() -> float:
        return Utils.format_datetime("1970-01-01 00:00:00")