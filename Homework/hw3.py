'''
Created on Feb 18, 2019
@author:   Justin Westley
@username: jwestley
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 3
'''
from cs115 import map
# Be sure to submit hw3.py.  Remove the '_template' from the file name.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def giveChange(amount, coins):
    """
    Returns a list whose first item is the minimum number of coins from the input
    list to make the given input amount, and whose second item is a list of the 
    coin values needed to make such a list.
    
    Inputs: amount total amount of change to reach, coins list of coin values to use
    """
    if amount <= 0:
        return [0, []]
    if not coins:
        return [float("inf"), []]
    elif coins[0] > amount:
        return giveChange(amount, coins[1:])
    else:
        use_it = giveChange(amount - coins[0], coins)
        lose_it = giveChange(amount, coins[1:])
        if use_it[0] < lose_it[0]:
            return [1 + use_it[0], [coins[0]] + use_it[1]]
        return lose_it

# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

def letterScore(letter, scoreList):
    """
    Returns the value associated with the given letter.
    
    Inputs: letter to be scored, scoreList to find the value
    """
    if not scoreList:
        return -1
    if scoreList[0][0] == letter:
        return scoreList[0][1]
    return letterScore(letter, scoreList[1:])

def wordScore(S, scoreList):
    """
    Returns the value for the given word.
    
    Inputs: S word to be scored, scoreList to find the values
    """
    def wordScoreHelper(S, scoreList, accum):
        if not S:
            return accum
        return wordScoreHelper(S[1:], scoreList, accum + letterScore(S[0], scoreList))
    return wordScoreHelper(S, scoreList, 0)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    return map(lambda x: [x, wordScore(x, scores)], dct)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n].'''
    if n < 1:
        return []
    if not L:
        return []
    return [L[0]] + take(n - 1, L[1:])
    
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:].'''
    if not L:
        return []
    if n < 1:
        return [L[0]] + drop(n - 1, L[1:])
    return drop(n - 1, L[1:])
