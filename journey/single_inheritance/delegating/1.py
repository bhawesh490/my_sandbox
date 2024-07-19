# Example1
class Person:
    def work(self):
        return "Person works..."


class Student(Person):
    def work(self):
        result = super().work()
        return f"Student works... and {result}"


print("Example1")
s = Student()
print(s.work())


# Example 2
class Person:
    def work(self):
        return "Person works..."


class Student(Person):
    pass


class PythonStudent(Student):
    def work(self):
        result = super().work()
        return f"Python student works... and {result}"


print("Example2")
ps = PythonStudent()
ps.work()
print(ps.work())


# Example 3
class Person:
    def work(self):
        return "Person works..."


class Student(Person):
    def work(self):
        return "Student works..."


class PythonStudent(Student):
    def work(self):
        result = super().work()
        return f"Python student works... and {result}"


print("Example3")
ps = PythonStudent()
ps.work()
print(ps.work())


# Example 4
class Person:
    def work(self):
        return "Person works..."


class Student(Person):
    def work(self):
        result = super().work()
        return f"Student works...{result}"


class PythonStudent(Student):
    def work(self):
        result = super().work()
        return f"Python student works... and {result}"


print("Example4")
ps = PythonStudent()
ps.work()
print(ps.work())


# Example 5
class Person:
    def work(self):
        return "Person Works..."


class Student(Person):
    def study(self):
        return "Student studies"


class PythonStudent(Student):
    def code(self):
        result_1 = self.work()
        # could have used super().work() but since we dont have any work method defined
        # in our subclass so there is no abiguity
        # if there was a work method here in this class we should use super().work() to
        # tell python that to fetch from parent class
        result_2 = self.study()
        return f"{result_1} and {result_2} and Python student codes"


print("Example5")
ps = PythonStudent()
print(ps.code())


# Example 6
class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age


print("Example6")
s = Student("John", 23)
print(s.__dict__)

# Example 7
from math import pi
from numbers import Real


class Circle:
    def __init__(self, r):
        # self._r = r
        self.radius = r
        self._area = None
        self._perimeter = None

    @property
    def radius(self):
        return self._r

    @radius.setter
    def radius(self, value):
        if isinstance(value, Real) and value > 0:
            self._r = value
            self._area = None
            self._perimeter = None
        else:
            raise ValueError("Radius must be a positive real number..")

    @property
    def area(self):
        if self._area is None:
            self._area = pi * self.radius**2
        return self._area

    @property
    def perimeter(self):
        if self._perimeter is None:
            self._perimeter = 2 * pi * self.radius
        return self._perimeter


class UnitCircle(Circle):
    def __init__(self):

        super().__init__(1)


print("Example7")
u = UnitCircle()
print(u.radius)
print(u.area)
print(u.perimeter)
# but we can change the radius values
u.radius = 10
print(u.radius)
# so what i want is that radius property to be settable from Circle Class but not from UnitCircle class
# so we are going to override the radius settable proprty in the unit circle class and we will make this proprty read only


class UnitCircle(Circle):
    def __init__(self):
        super().__init__(1)

    @property
    def radius(self):
        return super().radius


# u = UnitCircle()
# why is this happening?
# becuase we dont have a setter property in the unit circle class


# Example 8 to fix the above issue
class Circle:
    def __init__(self, r):
        # self._r = r
        self.set_radius(r)
        self._area = None
        self._perimeter = None

    @property
    def radius(self):
        return self._r

    def set_radius(self, value):
        if isinstance(value, Real) and value > 0:
            self._r = value
            self._area = None
            self._perimeter = None
        else:
            raise ValueError("Radius must be a positive real number..")

    @radius.setter
    def radius(self, value):
        self.set_radius(value)

    @property
    def area(self):
        if self._area is None:
            self._area = pi * self.radius**2
        return self._area

    @property
    def perimeter(self):
        if self._perimeter is None:
            self._perimeter = 2 * pi * self.radius
        return self._perimeter


class UnitCircle(Circle):
    def __init__(self):
        super().__init__(1)

    @property
    def radius(self):
        return super().radius


u = UnitCircle()
print(u.radius)
# u.radius = 10  # can't set attribute 'radius'
# offcouse we can do this
u.set_radius(10)
print(u.radius)
# so to avoid this lets make it private then


# Example 9 to fix the above issue
class Circle:
    def __init__(self, r):
        # self._r = r
        self._set_radius(r)
        self._area = None
        self._perimeter = None

    @property
    def radius(self):
        return self._r

    def _set_radius(self, value):
        if isinstance(value, Real) and value > 0:
            self._r = value
            self._area = None
            self._perimeter = None
        else:
            raise ValueError("Radius must be a positive real number..")

    @radius.setter
    def radius(self, value):
        self._set_radius(value)

    @property
    def area(self):
        if self._area is None:
            self._area = pi * self.radius**2
        return self._area

    @property
    def perimeter(self):
        if self._perimeter is None:
            self._perimeter = 2 * pi * self.radius
        return self._perimeter


class UnitCircle(Circle):
    def __init__(self):
        super().__init__(1)

    @property
    def radius(self):
        return super().radius


u = UnitCircle()
print(u.radius)
# u.radius = 10  # can't set attribute 'radius'
# offcouse we can do this
# so now you cannot use this u.set_radius(10)
# print(u.radius)
