'''
Created on Feb 4, 2019
I pledge my honor that I have abided by the Stevens Honor System.
@author: Justin Westley
username: jwestley
'''
from cs115 import map, reduce, filter
import math

def factorial(n):
    """Computes n!"""
    if n == 0:
        return 1;
    return n * factorial(n - 1)

def tower(n):
    """Computes 2^(2^(2...)) with n 2's, using recursion"""
    if n == 0:
        return 1
    return 2 ** tower(n - 1)

def length(lst):
    """Returns the length of the list"""
    # In class, tend to use if list == []. But this is better practice; empty list is false.
    if not lst:
        return 0
    return 1 + length(lst[1:])

def reverse(lst):
    """Takes as input a list of elements and returns the list in reverse order."""
    if not lst:
        return []
    return lst[-1:] + reverse(lst[:-1])

def member(x, lst):
    """Returns true if x is contained in the list and false otherwise."""
    # Different than the previous, a tail recursion rather than linear.
    if not lst:
        return False
    if x == lst[0]:
        return True
    return member(x, lst[1:])
    
def collapse(lst):
    """Collapses a list of possibly nested lists into a single list of values"""
    # Tree recursion
    # Base case: return empty list if list is empty
    if not lst:
        return []
    # If you currently are at a list: collapse it then collapse the rest later
    if isinstance(lst[0], list):
        return collapse(lst[0]) + collapse(lst[1:])
    # If you are not in a list, concatenate the index you're at and move on
    return lst[:1] + collapse(lst[1:])

def my_map(f, lst):
    """
    Returns a new list where the function f has been applied to every element
    in the original list.
    """
    if not lst:
        return []
    return [f(lst[0])] + my_map(f, lst[1:])

def tower_reduce(n):
    """Computes 2^(2^(2...)) with n 2's, using reduce"""
    def power(x, y):
        return y ** x
    return reduce(power, [2] * n)

def power(x, y):
    """Computes x^y using recursion"""
    if not y:
        return 1
    return x * power(x, y - 1)

def power_tail(x, y):
    """Computes x^y using tail recursion"""
    def power_tail_helper(x, y, accum):
        if not y:
            return accum
        return power_tail_helper(x, y - 1, x * accum)
    # Trace it from here, ends up just calling this with x y and 1
    # Accumulator ends up saving your squared value as you go, so don't go back up the stack
    return power_tail_helper(x, y, 1)

def my_reduce(f, lst):
    """
    Operates a function f and reduces the list to a single value as dictated
    by the predicate f.
       
    Inputs: function f to operate, list lst to operate on   
    """
    # Trace this
    def my_reduce_helper(f, lst, accum):
        if not lst:
            return accum
        return my_reduce_helper(f, lst[1:], f(accum, lst[0]))
    if not lst:
        raise TypeError("my_reduce() of empty sequence with no initial value")
    return my_reduce_helper(f, lst[1:], lst[0])

def prime(n):
    """
    Returns whether or not the integer is prime
    """
    possible_divisors = range(2, int(math.sqrt(n)))
    divisors = filter(lambda x: n % x == 0, possible_divisors)
    return len(divisors) == 0

def primes(n):
    """
    Returns a list of primes in the range [2, n] computed via the sieve of Erotosthenes
    """
    def sieve(lst):
        if not lst:
            return []
        return [lst[0]] + sieve(filter(lambda x: x % lst[0] != 0, lst[1:]))
    return sieve(range(2, n + 1))

def add(x,y):
    return x+y

def fib(n):
    """Returns the fibonacci value at the given index"""
    if n <= 1:
        return n;
    return fib(n - 1) + fib(n - 2)
       
# trace this for [1, 2, 3]
print(fib(5))

print(primes(5))