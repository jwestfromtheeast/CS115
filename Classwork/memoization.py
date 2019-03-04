'''
Created on Feb 27, 2019
I pledge my honor that I have abided by the Stevens Honor System.
@author: Justin Westley
username: jwestley
'''
# Memoization
# 0) Create a nested helper function that does the work. Pass
# an empty dictionary as a parameter.
# 1) Check if the key is in the memo. If so, return the value
# associated with the key.
# 2) Use recursion to do work, but put the result in a local variable.
# 3) Store the result in the memo and return the result.
import time

def fib(n):
    """Returns the nth keyword of the Fibonacci number."""
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

def fib_memo(n):
    """Returns the nth keyword of the fib number using memoization"""
    def fib_helper(n, memo):
        if n in memo:
            return memo[n]
        if n <= 1:
            result = n
        else:
            result = fib_helper(n - 1, memo) + fib_helper(n - 2, memo)
        memo[n] = result
        return result
    return fib_helper(n, {})

# start_time = time.time()
# print(fib(36))
# print('Computation time without memoization: %.2f ms' % ((time.time() - start_time) * 1000))
# 
# start_time = time.time()
# print(fib_memo(36))
# print('Computation time without memoization: %.2f ms' % ((time.time() - start_time) * 1000))

def LCS(s1, s2):
    """
    Returns the length of the longest common subsequence
    """
    if not s1 or not s2:
        return 0;
    if s1[0] == s2[0]:
        return 1 + LCS(s1[1:], s2[1:])
    return max(LCS(s1[1:], s2), LCS(s1, s2[1:])) 

def LCS_memo(s1, s2):
    """
    Returns the length of the longest common subsequence
    """
    def LCS_helper(s1, s2, memo):
        if (s1, s2) in memo:
            return memo[(s1, s2)]
        if not s1 or not s2:
            result = 0
        elif s1[0] == s2[0]:
            result = 1 + LCS_helper(s1[1:], s2[1:], memo)
        else:
            result = max(LCS_helper(s1, s2[1:], memo),
                         LCS_helper(s1[1:], s2, memo))
        memo[(s1, s2)] = result
        return result
    return LCS_helper(s1, s2, {})

# start_time = time.time()
# print(LCS_memo('lkjfljsdsdsafsddslajfdlskjflskffsafdsfsfsfafsfdlkf', 'dasfslerwqrrwrwerrjiojklijliklkfdsfdsafsdffsjklfs'))
# print('Computation time without memoization: %.2f ms' % ((time.time() - start_time) * 1000))

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

def LCS_with_values_memo(s1, s2):
    """
    Returns a tuple with the length of the longest common subsequence
    in strings s1 and s2 as well as the LCS itself.
    """
    def LCS_with_values_helper(s1, s2, memo):
        if (s1, s2) in memo:
            return memo[(s1, s2)]
        if not s1 or not s2:
            result = (0, '')
        elif s1[0] == s2[0]:
            lose_both = LCS_with_values_helper(s1[1:], s2[1:], memo)
            result = (1 + lose_both[0], s1[0] + lose_both[1])
        else:
            use_s1 = LCS_with_values_helper(s1, s2[1:], memo)
            use_s2 = LCS_with_values_helper(s1[1:], s2, memo)
            if use_s1[0] > use_s2[0]:
                result = use_s1
            else:
                result = use_s2
        memo[(s1, s2)] = result
        return result
    return LCS_with_values_helper(s1, s2, {})

# start_time = time.time()
# print(LCS_with_values_memo('lkjfljsdsdsafsddslajfdlskjflskffsafdsfsfsfafsfdlkf', 'dasfslerwqrrwrwerrjiojklijliklkfdsfdsafsdffsjklfs'))
# print('Computation time without memoization: %.2f ms' % ((time.time() - start_time) * 1000))

def subset_with_values_memo(target, lst):
    """
    Determines whether or not it is possible to create the target sum using values in the list.
    Can be positive, negative, or zero. Returns a tuple where the first element is True or
    False for if it is possible to create the second list. The second element of the tuple is
    a list of the elements necessary if it is possible.
    """
    last = len(lst) - 1
    def subset_helper(target, current, memo):
        if(target, current) in memo:
            return memo[(target, current)]
        if not target:
            result = (True, [])
        elif current > last:
            result = (False, [])
        else:
            use_it = subset_helper(target - lst[current], current + 1, memo)
            if use_it[0]:
                result = (True, [lst[current]] + use_it[1])
            else:
                result = subset_helper(target, current + 1, memo)
        memo[(target, current)] = result
        return result
    return subset_helper(target, 0, {})

print(subset_with_values_memo(12, [5,1,2,2,3,4,5,5,3,4,3,2,7]))
