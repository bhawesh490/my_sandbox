class Person:
    pass


class Student(Person):
    def study(self):
        return "Study...." * 3


p = Person()
# p.study() # AttributeError: 'Person' object has no attribute 'study'
s = Student()
print(isinstance(s, Person))  # True
print(s.study())


class Person:
    def routine(self):
        return self.eat() + self.study() + self.sleep()

    def eat(self):
        return "Person eats.."

    def sleep(self):
        return "Person sleeps.."


p = Person()
# p.routine()  # AttributeError: 'Person' object has no attribute 'study'


class Student(Person):
    def study(self):
        return "Student studies.."


s = Student()
print(s.routine())

# but the problem still exists we cannot call routine method from the person object


class Person:
    def routine(self):
        result = self.eat()
        if hasattr(self, "study"):
            result = result + self.study()
        result = result + self.sleep()
        return result

    def eat(self):
        return "Person eats.."

    def sleep(self):
        return "Person sleeps.."


p = Person()
print(p.routine())  # 'Person eats..Person sleeps..'


class Student(Person):
    def study(self):
        return "Student studies.."


s = Student()
print(s.routine())


########################
class Account:
    apr = 3.0

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        self.account_type = "Generic Account"

    def calc_interest(self):
        return f"Calc interest on {self.account_type} with APR = {self.__class__.apr} or {type(self).apr}"
        # we could have used self.apr but it would have been a problem if we had an instance variable with the same name
        # or somebody changed the attribute apr from outside


class Savings(Account):
    apr = 5.0

    def __init__(self, account_number, balance):
        self.account_type = "Savings Account"
        super().__init__(account_number, balance)


s = Savings(123, 10)
s.calc_interest()  # 'Calc interest on Savings Account with APR = 5.0 or 5.0'
print(s.calc_interest())
