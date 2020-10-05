"""
Difference between Regular Methods, Class Methods and Static Methods.
Regular method are retular functions inside the class
Class Method can also be used as decorator, takes class as variable
Static Method don't take any parameter, If we need a method that is not associated with the whole class we can use
    static method.

Concept/Code: Hem Raj Regmi (sangamsyabil@gmail.com)
github repository: https://github.com/sangamsyabil/hemAutomation

Happy coding !!!
"""


# Let's take an example
class Employee:
    num_of_employee = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        self.email = '{}_{}@gmail.com'.format(self.first, self.last)

        Employee.num_of_employee += 1

    # This is a regular method which takes class instance (self) as an argument.
    def full_name(self):
        return '{} {}'.format(self.first, self.last).title()

    # Class method takes whole class as argument not instances.
    @classmethod
    def apply_raise(cls, amount):
        cls.raise_amount = amount

    # This class method basically takes string, splits into pieces, construct a class with those variables
    # and finally returns that new employee object
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # static method don't take any argument.
    # this method just returns if today is workday or not. weekday() [0-6 from Monday to Sunday]
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True



emp_1 = Employee('test', 'user', 5000)
print(emp_1.email)  # test_user@gmail.com

Employee.apply_raise(1.05)
print(Employee.raise_amount)  # 1.05

# this also can be use from instances
emp_1.apply_raise(1.06)
print(emp_1.raise_amount)  # 1.06

# we can use classmethod as decorator
emp_str_1 = 'john-doe-4000'
new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)

# Finally, static method don't pass anythig as argument unlike 'self' on regular method and 'cls' on classmethod
import datetime
my_date = datetime.date(2019, 8, 1)
print(Employee.is_workday(my_date))
