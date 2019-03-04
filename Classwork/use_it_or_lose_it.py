'''
Created on Feb 11, 2019
I pledge my honor that I have abided by the Stevens Honor System.
@author: Justin Westley
username: jwestley
'''
from cs115 import map

def powerset(lst):
    """
    Returns the power set of the list, that is, the
    set of all subsets of the list
    """
    # trace this!
    if not lst:
        return [[]]
    lose_it = powerset(lst[1:])
    use_it = map(lambda subset: [lst[0]] + subset, lose_it)
    return lose_it + use_it

def subset(target, lst):
    """
    Determines whether or not it is possible to create the target
    sum using the values in the list. Can be positive, negative, or zero
    """
    if not target:
        return True
    if not lst:
        return False
    lose_it = subset(target, lst[1:])
    use_it = subset(target - lst[0], lst[1:])
    return use_it or lose_it

def subset2(capacity, items):
    """Given a suitcase capacity and a list of items
       consisting of positive numbers, returns a number
       indicating the largest sum that can be made from a
       subset of the items without exceeding the capacity."""
    # Think about each case. Base cases easiest first.
    # If either input is empty or invalid, we can't make a subset.
    if capacity <= 0 or not items:
        return 0
    # If the first item is too large to fit, we can toss it.
    elif items[0] > capacity:
        return subset2(capacity, items[1:])
    # Else, we need to make a choice between two things here.
    # Should we use the first item or lose it? Well, try both.
    # Let's find the best solution that uses the first item and
    # the best solution that loses the first item.
    else:
        # Easy, just find the full capacity and lose items[0]
        lose_it = subset(capacity, items[1:])
        # Keep items 0, subtract it from capacity to find the
        # rest of the set you can make
        use_it = items[0] + subset(capacity - items[0], items[1:])
        return max(lose_it, use_it)

def subsetBetter(target, lst):
    if not target:
        return True
    if not lst:
        return False
    return subsetBetter(target - lst[0], lst[1:]) or subsetBetter(target, lst[1:])

def LCS(s1, s2):
    """
    Returns the length of the longest common subsequence
    """
    if not s1 or not s2:
        return 0;
    if s1[0] == s2[0]:
        return 1 + LCS(s1[1:], s2[1:])
    return max(LCS(s1[1:], s2), LCS(s1, s2[1:])) 

def subset_with_values(target, lst):
    """
    Determines whether or not it is possible to create the target
    sum using the values in the list. Can be positive, negative, or zero.
    The function returns a tuple of exactly two items. The first
    is a Boolean that indicates True if the sum is possible, and false
    if it not. The second element in the tuple is a list of all the
    values that add up to make the target sum
    """
    # order matters. if you reach target == 0 at the bottom of a tree,
    # you have found the answer!
    if not target:
        return (True, [])
    # if you didnt reach true, but list is empty, its not the right answer.
    if not lst:
        return (False, [])
    use_it = subset_with_values(target - lst[0], lst[1:])
    if use_it[0]:
        return (True, [lst[0]] + use_it[1])
    # lose it. only executes if the use it side is false.
    return subset_with_values(target, lst[1:])

def LCS_with_values(s1, s2):
    """
    Returns a tuple with the length of the longest common subsequence
    in strings s1 and s2 as well as the LCS itself.
    """
    if not s1 or not s2:
        return (0, '')
    if s1[0] == s2[0]:
        result = LCS_with_values(s1[1:], s2[1:])
        return (1 + result[0], s1[0] + result[1])
    use_s1 = LCS_with_values(s1, s2[1:])
    use_s2 = LCS_with_values(s1[1:], s2)
    if use_s1[0] > use_s2[0]:
        return use_s1
    return use_s2

def coin_row(lst):
    """Returns max amount of money with no two adjacent coins
       being picked up"""
    if not lst:
        return 0
    return max(lst[0] + coin_row(lst[2:]), coin_row(lst[1:]))

def coin_row_with_values(lst):
    """Same as above but returns a list of the coin values as well"""
    if not lst:
        return [0, []]
    # as always, trace if necessary
    use_it = coin_row_with_values(lst[2:])
    # store our sum. This confused me, but remember, we arrive home
    # from our recursion before going to new_sum. so lst[0] uses it.
    new_sum = lst[0] + use_it[0]
    lose_it = coin_row_with_values(lst[1:])
    if new_sum > lose_it[0]:
        return [new_sum, [lst[0]] + use_it[1]]
    return lose_it
    
# print(coin_row_with_values([5, 1, 2, 10, 6, 2]))

def distance(first, second):
    """
    Returns the edit distance between the first and second string.
    """
    if not first:
        return len(second)
    if not second:
        return len(first)
    if first[0] == second[0]:
        return distance(first[1:], second[1:])
    # Optimization: originally added "1 +" to each of the next three.
    # Instead, move it to the min. Also, you could move all three recursive
    # calls to the min(), but this is easier to read, so leaving it.
    substitution = distance(first[1:], second[1:])
    deletion = distance(first[1:], second)
    insertion = distance(first, second[1:])
    return 1 + min(substitution, deletion, insertion)
        
    