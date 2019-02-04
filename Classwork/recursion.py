'''
Created on Feb 4, 2019
I pledge my honor that I have abided by the Stevens Honor System.
@author: Justin Westley
username: jwestley
'''
from cs115 import map

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
    #In class, tend to use if list == []. But this is better practice; empty list is false.
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
    #Different than the previous, a tail recursion rather than linear.
    if not lst:
        return False
    if x == lst[0]:
        return True
    return member(x, lst[1:])
    
print(map(tower, range(5)))
myList = [1,2,3]
print(reverse(myList))
print(member(3, myList))