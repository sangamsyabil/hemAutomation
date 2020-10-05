"""
Basics of creating and instantiating simple classes.

Method: A function that is associated with the class (An operation that we can perform with the object)
Attributes: A characteristics of an object (variables inside the class)

Example: We can create a Class caled 'Dog'. An attribute of a dog maybe its name, age.
while method of a dog maybe defined by bark() method which returns a sound.

OOP: A-PIE (Abstraction, Polymorphism, Inheritance, Encapsulation)

Concept/Code: Hem Raj Regmi (sangamsyabil@gmail.com)
github repository: https://github.com/sangamsyabil/hemAutomation

Happy coding !!!
"""


class Employee:
    def __init__(self, first, last, pay):
        self.first = first  # class variables (attributes)
        self.last = last
        self.pay = pay
        self.email = self.first + '_' + self.last + '@gmail.com'

    def full_name(self):
        return '{} {}'.format(self.first, self.last).title()


emp_1 = Employee('testing', 'user', 5000)  # instance variables

# Assessing class attribute
print(emp_1.email)  # testing_user@gmail.com

# Accessing class method
print(emp_1.full_name())  # Testing User


########################################################################
# Working more on class variables
class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + '_' + self.last + '@gmail.com'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  # raise_amount also need to referenced with instances


emp_1 = Employee('testing', 'user', 5000)  # instance variables
emp_1.apply_raise()
print(emp_1.pay)  # 5200

emp_1.raise_amount = 1.05  # we can use from common class variable or can provide from here.
emp_1.apply_raise()
print(emp_1.pay)  # 5400


#######################################################################
# Illustration of constant class variable
# No. or total employee (will be incremented by 1 when the new instance is created.)
class Employee:
    num_of_employee = 0

    def __init__(self):
        pass
        Employee.num_of_employee += 1


emp_1 = Employee()
emp_2 = Employee()
print(Employee.num_of_employee)  # 2
