'''
Created on Feb 21, 2019
I pledge my honor that I have abided by the Stevens Honor System.
@author: Justin Westley
username: jwestley
'''

def knapsack(capacity, itemList):
    """
    Function that aims to collect the maximum value of items
    while still being within the given capacity.
    Returns the maximum value and a list of the items.
    
    Inputs: capacity maximum capacity, itemList list of items,
    each entry is a list with weight and value.
    """
    # Base cases
    if capacity <= 0:
        return [0, []]
    if not itemList:
        return [0, []]
    # Don't want an oversized element
    if itemList[0][0] > capacity:
        return knapsack(capacity, itemList[1:])
    # typical use it
    use_it = knapsack(capacity - itemList[0][0], itemList[1:])
    # need a sum holder. remember this function returns a list of [sum, [itemWeight, itemValue]].
    # so, our sum is the current value of the itemList plus the total.
    new_sum = itemList[0][1] + use_it[0]
    # typical lose it
    lose_it = knapsack(capacity, itemList[1:])
    # return the answer in proper format
    if new_sum > lose_it[0]:
        return [new_sum, [itemList[0]] + use_it[1]]
    return lose_it  
    