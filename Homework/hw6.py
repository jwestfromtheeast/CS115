'''
Created on Mar 12 2019
@author:   Justin Westley
@username: jwestley
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

def count_white(S):
    """
    Counts a sequence of 0's, or white pixels. Returns when string ends or a 1 is found
    """
    if not S:
        return 0
    if S[0] == '1':
        return 0
    return 1 + count_white(S[1:])

def count_black(S):
    """
    Counts a sequence of 1's, or black pixels. Returns when string ends or a 0 is found
    """
    if not S:
        return 0
    if S[0] == '0':
        return 0
    return 1 + count_black(S[1:])

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if not n:
        return ''
    if n % 2:
        return numToBinary(n // 2) + '1'
    return numToBinary(n // 2) + '0'

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if not s:
        return 0
    if int(s[-1]) % 2:
        return binaryToNum(s[:-1]) * 2 + 1
    return binaryToNum(s[:-1]) * 2

def pad(S):
    """
    Pads a binary number with leading 0's for compression
    """
    return '0' * (COMPRESSED_BLOCK_SIZE - len(S)) + S

def compress(S):
    """
    Takes a binary string S of length 64 as input and returns another
    binary string with a run-length encoding as output.
    """
    # To compress a string of length 64, the worst case would be the checkerboard
    # starting with black. By convention, we start with 0, for white, so that's 5 bits.
    # But, at the end of each row, the color carries to the next row. So, this ends
    # up having 58 sequences needed, or 58 * COMPRESSED_BLOCK_SIZE. Here, 58*5=290.
    if S == '':
        return ''
    wsum = count_white(S[:MAX_RUN_LENGTH])
    if S[wsum:] == '':
        return pad(numToBinary(wsum)) + compress(S[wsum:])
    bsum = count_black(S[wsum:wsum+MAX_RUN_LENGTH])
    return pad(numToBinary(wsum)) + pad(numToBinary(bsum)) + compress(S[wsum+bsum:])

def uncompress(S):
    """
    Takes a binary string S with a run-length encoding as input and inverts
    the compression done. Returns the inverted binary string.
    """
    if not S:
        return ''
    white = binaryToNum(S[:5]) * '0'
    black = binaryToNum(S[5:10]) * '1'
    return white + black + uncompress(S[10:])

def compression(S):
    """
    Returns the ratio of the compressed size to original size for string S.
    """
    return len(compress(S)) / len(S)

# Professor Lai: You cannot represent a full set of bits with a number smaller
# than the original bit number. For example, if you are compressing any file of
# size 3 bits, there are 2^3 = 8 possible combos. If your compression always reduces
# the size of any file, it will be two bits long in the worst case. There are only
# 2^2 = 4 possible combinations of 2 bits, and you cannot represent 8 combinations
# with only 4 values. Therefore, decompression is impossible without data loss.
