'''
Created on Apr 4, 2019
I pledge my honor that I have abided by the Stevens Honor System.
@author: Justin Westley
username: jwestley
'''
def mult(c, n):
    """
    Returns the product of c times n without multiplication.
    Holds a result value and uses a for loop.
    """
    result = 0
    for x in range(n):
        result += c
    return result

def update(c, n):
    """
    Starts a new value, z, at zero, and repeatedly updates it using the
    assignment statement z = z**2 + c for a total of n times.
    Returns the final value of z.
    """
    z = 0
    for x in range(n):
        z = z**2 + c
    return z

def inMSet(c, n):
    """ inMSet takes in: 
            c for the update step of z = z**2+c             
            n, the maximum number of times to run that step         
        Then, it should return:              
            False as soon as abs(z) gets larger than 2             
            True if abs(z) never gets larger than 2 (for n iterations)     
    """ 
    z = 0
    for x in range(n):
        z = z**2 + c
        if abs(z) > 2:
            return False
    return True
    
c = 0.42 + 0.2j
print(inMSet(c, 50))