'''
Created on Jan 30, 2019

@author: justi
'''
from cs115 import map, reduce

def span(lst):
    """Returns the difference between the maximum and minimum numbers in a list."""
    return reduce(max, lst) - reduce(min, lst)

def add(a, b):
    """Returns the sum of a and b."""
    return a + b

def sqr(x):
    """Returns the square of x."""
    return x * x

def mult(a, b):
    """Returns the product of a and b."""
    return a * b

def gauss(n):
    """Takes as input a positive integer n and returns the sum of 1+2+...+n"""
    return reduce(add, range(1, n + 1))

def gauss2(n):
    """Takes as input a positive integer n and returns the sum of 1+2+...+n"""
    if n == 0:
        return 0
    return n + gauss(n - 1)

def sum_of_squares(n):
    """Takes as input a positive integer n and returns the sum 1^2 + 2^2 + ... + n^2"""
    return reduce(add, map(sqr, range(1, n + 1)))

print(sum_of_squares(10))

list_of_strings = ['hello', 'my', 'name', 'is', 'brian']
print(map(len, list_of_strings))

list_of_ints = [1, 2, 3, 4, 5]
print(reduce(mult, list_of_ints))