"""
Iterator in Python is simply an object that can be iterated upon.
An object which will return data, one element at a time.

Technically, Python 'iterator object' must implement two special methods, __iter__(), and __next__(),
collectively called the iterator protocol.

Most of built-in containers in python like list, tuple, string etc. are iterables.

The advantage of using iterators is that they save resources.
For example we could get all the odd numbers without storing the entire number system in memory

Concept/Code: Hem Raj Regmi (sangamsyabil@gmail.com)
github repository: https://github.com/sangamsyabil/hemAutomation

Happy coding !!!
"""

print('#' * 50)

# define a list
my_list = [4, 3, 5, 4]

# get an iterator using iter()
my_iter = iter(my_list)

print(type(my_iter))  # <class 'list_iterator'>

# iterate through it using next()
print(next(my_iter))  # 4

# next(job) is same as obj.__next__()

print(my_iter.__next__())  # 3

print('#' * 50)


# An example that will give us next power of 2 in each iteration. Power exponent starts from zero upto a user set num.
class PowOfTwo:
    """
    Class to implement an iterator of power of two
    """

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


# We can create an iterator and iterate through it
a = PowOfTwo(4)
i = iter(a)
print(next(i))  # 1
print(next(i))  # 2
print(next(i))  # 4

print('\n')

# We also can use a for lop to iterate over our iterator class
for i in PowOfTwo(4):
    print(i)
