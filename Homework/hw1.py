'''
Created on Feb 6, 2019
I pledge my honor that I have abided by the Stevens Honor System.
@author: Justin Westley
username: jwestley
'''
from cs115 import map, reduce

def mult(x, y):
    """Returns the product of x and y"""
    return x * y

def add(x, y):
    """Returns the sum of x and y"""
    return x + y

def factorial(n):
    """Returns the factorial of the given positive integer n"""
    if n == 0:
        return 1
    return reduce(mult, range(1, n + 1))

def mean(L):
    """Returns the mean of the given list of numbers"""
    return reduce(add, L) / len(L)

def divides(n):
    """Returns a function that takes in k and checks if it divides n"""
    def div(k):
        return n % k == 0
    return div

def prime(n):
    """Returns true if n is prime or false if n is composite"""
    # Optimally, only go to the sqrt of n
    if n < 2:
        return False
    return not sum(map(divides(n), range(2, n // 2 + 1)))    