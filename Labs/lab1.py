'''
Created on Jan 31, 2019
I pledge my honor that I have abided by the Stevens Honor System.
@author: Justin Westley
username: jwestley
'''
from cs115 import map, reduce
import math

def inverse(n):
    """
    Takes a number n and returns its reciprocal as a floating point number
    
    input n: an int or float
    """
    return 1 / n

def e(n):
    """
    Approximates the mathematical value e using a Taylor expansion to the first n terms
    
    input n: a positive int
    """
    return 1 + sum(map(inverse, (map(math.factorial, range(1, n + 1)))))

def error(n):
    """
    Returns the absolute value of the difference between the actual value of e and my approximation to n terms
    
    input n: a positive int
    """
    return abs(math.e - e(n))