'''
Created on Mar 26, 2019
@author:   Brendan Lee
username:  blee9
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 7
'''

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
    """Takes as input a non-negative (0 or larger)integer N and a base B 
        (between 2 and 10 inclusive) and returns a string representing the number 
        N in base B"""
    if N == 0:
        return "0"
    return str(int(numToBaseB(int(N / B), B) + str(N % B)))

def baseBToNum(S, B):
    """Takes as input a string S and a base B where S represents a number 
    in base B where B is between 2 and 10 inclusive"""
    if S == "":
        return 0
    return baseBToNum(S[:-1], B) * B + int(S[-1])

def baseToBase(B1, B2, SinB1):
    """Takes a base B1, a base B2 (both of which are between 2 and 10, inclusive) and 
    SinB1, which is a string representing a number in base B1"""
    return numToBaseB(baseBToNum(SinB1, B1), B2)

def add(S,T):
    """Takes two binary strings S and T as input and returns their sum, 
        also in binary"""
    return numToBaseB(baseBToNum(S, 2) + baseBToNum(T, 2), 2)

def addB(S, T):
    """Return a new string representing the sum of the two input strings"""
    length = len(S) - len(T)
    if length > 0:
        T = "0" * length + T
    if length < 0:
        S = "0" * length + S
    def addBHelper(X, S, T):
        if S == "":
            if X == "0":
                return ""
            else:
                return "1"
        return addBHelper(FullAdder[(X, S[-1], T[-1])][1], S[:-1], T[:-1]) + FullAdder[(X, S[-1], T[-1])][0]
    return addBHelper("0", S, T)