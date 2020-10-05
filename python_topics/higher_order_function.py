"""
Everything in Python are object (class, functions and all)
Functions can be passed as arguments to another function. For example: map, filter and reduce in Python.
    Such function that take another functions as arguments are also called Higher order functions.

Concept/Code: Hem Raj Regmi (sangamsyabil@gmail.com)
github repository: https://github.com/sangamsyabil/hemAutomation

Happy coding !!!
"""

def inc(x):
    return x + 1


def dec(x):
    return x - 1


def operate(func, x):
    return func(x)


# We invoke the function as follows.
print(operate(inc, 3))  # 4
print(operate(dec, 3))  # 2


# Furthermore, a function can return another function
def is_called():
    def is_returned():
        print('Hello')

    return is_returned


new = is_called()
new()  # Hello
# Here, is_returned() is a nested function which is defined and returned, each time we call is_called()
