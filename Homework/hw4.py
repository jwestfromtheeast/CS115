'''
Created on Feb 25, 2019
I pledge my honor that I have abided by the Stevens Honor System.
@author: Justin Westley
username: jwestley
'''

def next_row(lst):
    """
    Returns the next row of Pascal's triangle, excluding the leading "1". 
    Will not work for an empty list. Strictly meant to be used as 
    a helper for pascal_row() and pascal_triangle().
    
    Inputs: lst list to use to form the next row of the triangle
    """
    if lst[0] == 1 and not lst[1:]:
        return [1]
    return [lst[0] + lst[1]] + next_row(lst[1:])

def pascal_row(row_number):
    """
    Returns the list of elements found in a row of Pascal's triangle.
    
    Inputs: row_number row of the triangle to calculate
    """
    def pascal_row_helper(rownum, nextrow):
        if rownum == row_number:
            return nextrow
        return pascal_row_helper(rownum + 1, [1] + next_row(nextrow))
    return pascal_row_helper(0, [1])    

def pascal_triangle(row_number):
    """
    Outputs the list of elements found in a row of Pascal's triangle.
    
    Inputs: row_number row of the triangle to calculate
    """
    def pascal_triangle_helper(rownum, rows):
        if rownum == row_number:
            return rows
        return pascal_triangle_helper(rownum + 1, rows + [[1] + next_row(rows[-1])])
    return pascal_triangle_helper(0, [[1]])