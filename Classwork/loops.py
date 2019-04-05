'''
Created on Apr 1, 2019
I pledge my honor that I have abided by the Stevens Honor System.
@author: Justin Westley
username: jwestley
'''
def find_max(lst):
    if not lst:
        return None
    maxi = lst[0];
    for x in lst:
        if x > maxi:
            maxi = x
    return maxi

def find_min_max(lst):
    if not lst:
        return None
    mini = maxi = lst[0]
    for x in lst:
        if x > maxi:
            maxi = x
        elif x < mini:
            mini = x
    return [mini, maxi]

# Sub-lists would only be aliases, need a deep copy for that
def shallow_copy(lst):
    new_list = []
    for x in lst:
        new_list.append(x)
    return new_list

def shallow_copy_list_comp(lst):
    return [x for x in lst]

# Aliasing: if L = [1, 2, 3], and M = L, point to same thing.
# What would happen?
L = [1, 2, 3]
M = shallow_copy(L)
L[0] = 11
print(L)
print(M)
print(id(L[1]), id(M[1]))
# Different lists, but since index 1 holds the same value, points to same place.

def deep_copy(lst):
    new_list = []
    for x in lst:
        if type(x) is list:
            new_list.append(deep_copy(x))
        else:
            new_list.append(x)
    return new_list

def addall(board):
    """
    Sums the values of a 2d array
    """
    total = 0
    for row in board:
        for val in row:
            total += val
    return total

def addall2(board):
    """
    Sums the values of a 2d array with range
    """
    total = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            total += board[i][j]
    return total

board = [
    [3,0,1],
    [2,5,6],
    [-9,8,7],
    [1,2,3],
]
print(addall2(board))