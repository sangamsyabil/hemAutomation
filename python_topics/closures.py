"""
The technique by which some data gets attached to the code is called closure in python.
When do we have a closure?
- We must have a nested function (function inside a function)
- The nested function must refer to a value defined in the enclosing function.
- The enclosing function must return the nested function.

When to use Closures?
- Closures can avoid the use of global values and provides some form of data hiding.
- When there are few methods (one method in most cases) to be implemented in a class, closures can provide an alternate
  and more elegant solutions. But when the number of attributes and methods get larger, better implement a class.

Concept/Code: Hem Raj Regmi (sangamsyabil@gmail.com)
github repository: https://github.com/sangamsyabil/hemAutomation

Happy coding !!!
"""


# Before getting into closure, let's first understand nested function.
def print_msg(msg):  # This is the outer enclosing function
    def printer():  # This is the nested function
        print(msg)

    printer()


print_msg('Hello-world')

#########################################################################
# We can see that the nested function printer() was able to access the non-local variable msg of the enclosing function

# Let's change function print_msg()
def print_msg(msg):
    def printer():
        print(msg)

    return printer


another = print_msg("Hello again")
another()
# The print_msg() function was called with the string and returned function was bound to the name another.
# On calling another(), the message was still remembered although we had already finished executing the print_msg()

# This technique by which some data 'hello again' gets attached to the code is called closure in Python.

##############################################################################


# A simple example of closure
def make_multiplier_of(n):
    def multiplier(x):
        return x * n

    return multiplier


times3 = make_multiplier_of(3)
print(times3(9))  # 27

##############################################################################
