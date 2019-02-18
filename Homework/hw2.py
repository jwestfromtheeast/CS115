'''
Created on Feb 12, 2019
@author:   Justin Westley
Pledge:    I pledge my honor that I have abided by the Stevens Honor System
username: jwestley

CS115 - Hw 2
'''
import sys
from cs115 import map, reduce, filter
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.
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

def ind(e, L):
    """
    Returns the index at which element e is found in sequence L.
    If it does not exist in the sequence, returns the length of L.
    
    Inputs: element e to be searched for, and sequence L, a string or list
    """
    def ind_helper(e, L, index):
        if not L:
            return index
        if L[0] == e:
            return index
        return ind_helper(e, L[1:], index + 1)
    return ind_helper(e, L, 0)

def clearLetter(e, Rack):
    """
    Returns a new Rack that is the same as the old hut with a letter removed.
    
    Inputs: e letter to remove, Rack list of lowercase letter
    """
    return Rack[:ind(e, Rack)] + Rack[ind(e, Rack) + 1:]

def exists(S, Rack):
    """
    Returns True if the given string can be made from the given Rack.
    If not, returns false.
    
    Inputs: str string to check, Rack list of lowercase letters
    """
    if not S:
        return True
    if S[0] in Rack:
        return exists(S[1:], clearLetter(S[0], Rack))          
    return False

def getWords(Rack):
    """
    Returns a list of all the words that can be made from the given Rack.
     
    Inputs: Rack list of lowercase letters
    """
    return filter(lambda x: exists(x, Rack), Dictionary)

def getScores(Rack):
    """
    Returns a list of all the scores that can be made from the given Rack.
     
    Inputs: Rack list of lowercase letters
    """
    return map(lambda x: wordScore(x, scrabbleScores), getWords(Rack))


def scoreList(Rack):
    """
    Returns a list of lists, each two elements long. The first is the
    word that can be made from the given Rack and the second is the
    score for that word.
    
    Inputs: Rack list of lowercase letters
    """
    def scoreListComb(words, scores, accum):
        if not words:
            return accum
        return scoreListComb(words[1:], scores[1:], accum + [[words[0], scores[0]]])
    return scoreListComb(getWords(Rack), getScores(Rack), [])

def bestWord(Rack):
    """
    Returns a list with two elements: the highest possible scoring word
    and the score for that word.
    
    Inputs: Rack list of lowercase letters
    """
    # Check for bad input
    if not getScores(Rack):
        return ['', 0]
    maxScore = reduce(max, getScores(Rack))
    scoreLst = scoreList(Rack)
    # Helper function to find the best word from the max score
    def bestWordHelper(mx, sclst):
        if sclst[0][1] == mx:
            return  sclst[0][0]
        return bestWordHelper(mx, sclst[1:])
    return [bestWordHelper(maxScore, scoreLst), maxScore]