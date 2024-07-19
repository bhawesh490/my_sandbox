import logging

logging.basicConfig(
    filename="employee.log",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        logging.info("Employee created: %s", self.name)

    @property
    def email(self):
        return f"{self.name}@gmail.com"


emp1 = Employee("bhawesh", 28)
emp2 = Employee("saumya", 25)
logging.info(emp1.email)
logging.info(emp2.email)
