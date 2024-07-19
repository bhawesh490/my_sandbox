import set_log

logger = set_log.setup_logging(__name__, "employee_modify_v1.log")


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
