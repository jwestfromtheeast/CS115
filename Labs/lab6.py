'''
Created on Mar 7 2019
@author:   Justin Westley
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return not not n % 2
# 42 base 10 to base 2: 101010
# An odd base 2 number will have a rightmost value of 1
# An even base 2 number will have a rightmost value of 0
# When you remove the LSB, the value of the number is halved (rounded down)
# If N is odd: add an LSB of 1. If N is even: add an LSB of 0

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if not n:
        return ''
    if isOdd(n):
        return numToBinary(n // 2) + '1'
    return numToBinary(n // 2) + '0'

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if not s:
        return 0
    if isOdd(int(s[-1])):
        return binaryToNum(s[:-1]) * 2 + 1
    return binaryToNum(s[:-1]) * 2

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    if s == '1' * 8:
        return '0' * 8
    numb = numToBinary((binaryToNum(s) + 1))
    return ((8 - len(numb)) * '0') + numb

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n < 0:
        return
    print(s)
    count(increment(s), n - 1)

# 59 base 10 to ternary: 2012
def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if not n:
        return ''
    if not n % 3:
        return numToTernary(n // 3) + '0'
    if n % 3 == 1:
        return numToTernary(n // 3) + '1'
    return numToTernary(n // 3) + '2'

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if not s:
        return 0
    if int(s[-1]) == 2:
        return ternaryToNum(s[:-1]) * 3 + 2
    if int(s[-1]) == 1:
        return ternaryToNum(s[:-1]) * 3 + 1
    return ternaryToNum(s[:-1]) * 3
