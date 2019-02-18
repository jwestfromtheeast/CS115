'''
Created on Feb 7, 2019
I pledge my honor that I have abided by the Stevens Honor System.
@author: Justin Westley
username: jwestley
'''

def dot(L, K):
    """
    Outputs the dot products of the input lists L and K
    
    Inputs: Lists L and K, for operation L.K
    """
    if not L or not K:
        return 0.0
    return L[0] * K[0] + dot(L[1:], K[1:])

def explode(S):
    """Returns a list of the characters of the input
    
    Input: String S to be exploded
    """
    if not S:
        return []
    return [S[0]] + explode(S[1:])

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
        
def removeAll(e, L):
    """
    Returns a list identical to L but with all elements identical to e removed.
    
    Inputs: element e to be removed, list L
    """
    if not L:
        return [];
    if L[0] == e:
        return removeAll(e, L[1:])
    return L[:1] + removeAll(e, L[1:])

def myFilter(f, L):
    """
    Performs the function f that returns True or False on each element of list L.
    Then returns a new list with only the elements that returned True.
    
    Inputs: function f that operates on a single element and returns True or False.
            list L that will be operated on
    """
    if not L:
        return [];
    if f(L[0]):
        return L[:1] + myFilter(f, L[1:])
    return myFilter(f, L[1:])
    
def deepReverse(L):
    """
    Returns the reversal of a list L. If there are nested lists, they will also
    be reversed.
    
    Input: list L to be reversed. May have nested lists
    """
    if not L:
        return [];
    if isinstance(L[-1], list):
        return [deepReverse(L[-1])] + deepReverse(L[:-1])
    return L[-1:] + deepReverse(L[:-1])

print(deepReverse([1,2,3,[2,1],4]))