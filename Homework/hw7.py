'''
Created on Mar 27, 2019
I pledge my honor that I have abided by the Stevens Honor System.
@author: Justin Westley
username: jwestley
'''

# constant needed for the last part
FullAdder = {
('0','0','0') : ('0','0'),
('0','0','1') : ('1','0'),
('0','1','0') : ('1','0'),
('0','1','1') : ('0','1'),
('1','0','0') : ('1','0'),
('1','0','1') : ('0','1'),
('1','1','0') : ('0','1'),
('1','1','1') : ('1','1')
}

def numToBaseB(N, B):
    """
    Takes as input a non-negative integer N and base B between 2 and 10.
    Returns a string representing integer N in base B.
    """
    # "Reversal" of baseBToNum()
    if not N:
        return "0"
    return str(int(numToBaseB(int(N / B), B) + str(N % B)))

def baseBToNum(S, B):
    """
    Takes as input a string S and base B the string is in, between 2 and 10.
    Returns the integer representing this number in base 10.
    """
    # Modified from previous assignment + today's exam :)
    if not S:
        return 0
    return B * baseBToNum(S[:-1], B) + int(S[-1])

def baseToBase(B1, B2, SinB1):
    """
    Takes three inputs: B1, the base you are in, B2, the base you convert to,
    (both between 2 and 10) and SinB1, the base of B1. Returns a string
    representing the number SinB1 in base B2.
    """
    # convert the input to a number, then that number to the new base
    return numToBaseB(baseBToNum(SinB1, B1), B2)

def add(S, T):
    """
    Adds the binary numbers S and T together (strings). Returns a string 
    representing this binary number, by converting to num, add, then back.
    """
    # Convert both numbers to decimal, add normally, and convert back to binary
    return numToBaseB(baseBToNum(S, 2) + baseBToNum(T, 2), 2)

def addB(S, T):
    """
    Adds the binary numbers S and T together (strings). Returns a string
    representing the binary number. Uses the binary addition algorithm.
    Uses a helper function to hold the binary number.
    """
    length = len(S) - len(T)
    if length > 0:
        T = length * "0" + T
    if length < 0:
        S = length * "0" + S
    def addB_helper(X, S, T):
        if not S:
            if X == "0":
                return ""
            else:
                return "1"
        return addB_helper(FullAdder[(X, S[-1], T[-1])][1], S[:-1], T[:-1]) + FullAdder[(X, S[-1], T[-1])][0]
    return addB_helper("0", S, T)
