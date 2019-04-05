'''
Created on Apr 1, 2019
I pledge my honor that I have abided by the Stevens Honor System.
@author: Justin Westley
username: jwestley
'''

def TcToNum(S):
    """
    Returns the integer value of a two's complement 8-bit string
    """
    def binaryToNumTcHelper(S, val):
        if not S:
            return val
        # If there's a 1 leading, add value
        if S[0] == '1':
            return binaryToNumTcHelper(S[1:], val + (2 ** (len(S) - 1)))
        # Else, continue since 0 adds no value
        return binaryToNumTcHelper(S[1:], val)
    return binaryToNumTcHelper(S[1:], -128 if S[0] == '1' else 0)

def NumToTc(N):
    """
    Returns the 8-bit two's complement value of an integer
    """
    if N < -128 or N > 127:
        return 'Error'
    def NumToTcHelper(N, accum):
        if not N:
            return accum + '0' * (8 - len(accum))
        # If adding a 1 will be valid, then add a 1 to the number
        if N - 2 ** (7 - len(accum)) >= 0:
            return NumToTcHelper(N - 2 ** (7 - len(accum)), accum + '1')
        # Else, add a 0 and continue along
        return  NumToTcHelper(N, accum + '0')
    return NumToTcHelper(N + 128 if N < 0 else N, '1' if N < 0 else '0')