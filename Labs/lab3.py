'''
Created on Feb 14, 2019
I pledge my honor that I have abided by the Stevens Honor System.
@author: Justin Westley
username: jwestley
'''

def change(amount, coins):
    """
    Find the least amount of coins needed to give the given amount of change.
    
    Inputs: amount integer of the total amount of change to add up to
            coins list of integers of values of the coins
    """    
    if amount <= 0:
        return 0
    if not coins:
        return float("inf")
    elif coins[0] > amount:
        return change(amount, coins[1:])
    else:
        lose_it = change(amount, coins[1:])
        use_it = 1 + change(amount - coins[0], coins)
        return min(use_it, lose_it)