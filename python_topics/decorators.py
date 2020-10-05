"""
Before decorator - check higher_order_function.py
Functions and methods are callable as they can be called.

Basically, a decorator takes in a function, adds some functionality and returns it.
NOTE: Dynamically alter the functionality of your functions

Why we need decorators?
- We easily can modify the functionality of original function without changing the function itself.

Concept/Code: Hem Raj Regmi (sangamsyabil@gmail.com)
github repository: https://github.com/sangamsyabil/hemAutomation

Happy coding !!!
"""


# basic example explaining decorator
def decorator_function(original_function):
    def wrapper_function():
        print('Wrapper executed before {}'.format(original_function.__name__))
        return original_function()

    return wrapper_function


def display():
    print('Display function ran')


decorated_display = decorator_function(display)
# decorated_display variable is actually a wrapper_function; waiting to be executed.
decorated_display()  # Wrapper executed before display \n Display function ran

#####################################################################
# same program but modifying new look
def decorator_function(original_function):
    def wrapper_function():
        print('Wrapper executed before {}'.format(original_function.__name__))
        return original_function()

    return wrapper_function


@decorator_function
def display():
    print('Display function ran')


display()  # Wrapper executed before display \n Display function ran

###################################################################
# Now passing and not passing (arguments and kewword arguments)
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('Wrapper function executed before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print('Display function ran')

@decorator_function
def display_info(name, age):
    print('Display_info function ran with {0}, {1}'.format(name, age))

display()
display_info('Hem Raj Regmi', 30)

#######################################################################
# let's create decorator class (less useful)
class Decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('Call method called before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)

@Decorator_class
def display():
    print('Display function ran')

@Decorator_class
def display_info(name, age):
    print('Display_info function ran with {0}, {1}'.format(name, age))

display()
display_info('Hem', 29)


# One practical example
# in addition of displaying display_info(), we can keep track of arguments passsed to it.
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    def wrapper_func(*args, **kwargs):
        logging.info('Ram with args: {}, and kwargs {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)
    return wrapper_func

@my_logger
def display_info(place, code):
    print('Display_info function ran with {0}, {1}'.format(place, code))

display()
display_info('Ottawa, Canada', 999)