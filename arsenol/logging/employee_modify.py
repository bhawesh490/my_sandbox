import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler = logging.FileHandler("employee_modify.log")
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        logger.info("Employee created: %s", self.name)

    @property
    def email(self):
        return f"{self.name}@gmail.com"


emp1 = Employee("bhawesh", 28)
emp2 = Employee("saumya", 25)
logger.info(emp1.email)
logger.info(emp2.email)
