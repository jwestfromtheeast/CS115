'''
Created on Feb 25, 2019
I pledge my honor that I have abided by the Stevens Honor System.
@author: Justin Westley
username: jwestley
'''
import turtle

def square_spiral(walls):
    def square_spiral_helper(distance, initial, count):
        if count == walls:
            turtle.done()
        turtle.left(90)
        turtle.forward(distance)
        # Only increases distance every other time
        square_spiral_helper(distance + initial * (count % 2), initial, count + 1)
    square_spiral_helper(20, 20, 0)
    
def oct_spiral(walls):
    def oct_spiral_helper(distance, initial, count):
        if count == walls:
            turtle.done()
        turtle.left(45)
        turtle.forward(distance)
        # Only increases distance every other time
        oct_spiral_helper(distance + initial * (count % 2), initial, count + 1)
    oct_spiral_helper(20, 5, 0)
oct_spiral(15)