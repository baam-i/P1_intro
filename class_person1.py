"""
    In object-oriented programming, public, private, and protected are access 
    modifiers that define the level of accessibility of class members (attributes 
    and methods) from outside the class. These modifiers control how these members 
    can be accessed or modified by other parts of the code.

    Public:
        Public members are accessible from outside the class without any restrictions.
        In Python, all attributes and methods are public by default.
        They can be accessed directly from outside the class.

    Protected:
        Protected members are accessible within the class itself and its subclasses.
        In Python, conventionally, attributes and methods are marked as protected by prefixing an underscore _ to their names.
        They can still be accessed from outside the class, but it's a convention to discourage direct access.

    Private:
        Private members are only accessible within the class itself.
        In Python, to define private attributes and methods, their names are prefixed with double underscores __.
        Accessing private members directly from outside the class raises an 'AttributeError'.
"""
class Person:
    def __init__(self, name, age):
        self.name = name                # Public attribute
        self._age = age                 # Protected attribute

    def display_info(self):
        print(f"Name: {self.name}, Age: {self._age}")


class Worker(Person):
    def __init__(self, name, age, company):
        super().__init__(name, age)
        self.company = company          # Public attribute

    def display_info(self):
        super().display_info()
        print(f"Works at: {self.company}")


class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.__school = school          # Private attribute

    def display_info(self):
        super().display_info()
        print(f"School: {self.__school}")


class Manager(Worker):
    def __init__(self, name, age, company, department):
        super().__init__(name, age, company)
        self._department = department   # Protected attribute

    def display_info(self):
        super().display_info()
        print(f"Department: {self._department}")


# Example Usage
person1 = Person("Alice", 30)
person1.display_info()

print()

worker1 = Worker("Bob", 35, "XYZ Corporation")
worker1.display_info()

print()

student1 = Student("Eve", 20, "ABC University")
student1.display_info()

# Trying to access private attribute directly (will result in an AttributeError)
# print(student1.__school)

print()

manager1 = Manager("Charlie", 40, "XYZ Corporation", "HR")
manager1.display_info()
