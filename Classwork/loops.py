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
# L = [1, 2, 3]
# M = shallow_copy(L)
# L[0] = 11
# print(L)
# print(M)
# print(id(L[1]), id(M[1]))
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

def sequential_search(lst, key):
    """
    Returns the index at which a particular key is found in a list. If it is not found,
    will return -1.
    """
    for i in range(len(lst)):
        if lst[i] == key:
            return i
    return -1

def binary_search(lst, key):
    """
    
    """
    low = 0
    high = len(lst) - 1
    while low <= high:
        # prevents bug of integer overflow on huge numbers
        mid = low + (high - low) // 2
        if lst[mid] == key:
            return mid
        if lst[mid] < key:
            low = mid + 1
        else:
            high = mid + 1
    return -low - 1

board = [
    [3,0,1],
    [2,5,6],
    [-9,8,7],
    [1,2,3],
]

def swap(lst, a, b):
    """
    swaps the elements in lst at indexes a and b
    """
    temp = lst[a]
    lst[a] = lst[b]
    lst[b] = temp
    
def selection_sort(lst):
    """
    
    """
    n = len(lst)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        if min_index != i:
            swap(lst, i, min_index)

