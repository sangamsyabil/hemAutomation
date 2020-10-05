"""
There are lot of overhead in building an iterator in Python; we need to keep track of internal states,
raise StopIteration when there was no values to be returned etc.

Python generators are a simple way of creating iterators.
A generator is a function that returns an object (iterator) which we can iterate over (one value at a time)

It is fairly simple to create a generator in Python. It is as easy as defining a normal function with yield statement
instead of a return statement.

The difference is that, while a return statement terminates a function entirely, yield statement pauses the function
saving all its states and later continues from there on successive calls.

Concept/Code: Hem Raj Regmi (sangamsyabil@gmail.com)
github repository: https://github.com/sangamsyabil/hemAutomation

Happy coding !!!
"""


def pow_two_gen(maximum=0):
    n = 0
    while n < maximum:
        yield 2 ** n
        n += 1


# Infinite Stream
def all_even():
    n = 0
    while True:
        yield n
        n += 2


if __name__ == '__main__':
    gen_value = pow_two_gen(4)  # <generator object pow_two_gen at 0x7fafffed0c50>

    print(gen_value.__next__())
    print(gen_value.__next__())

    for num in all_even():
        if num < 10:  # don't forget to put any kind of stopper or this will run forever.
            print(num)
