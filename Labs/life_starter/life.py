#
# life.py - Game of Life lab
#
# Name: Justin Westley
# Pledge: I pledge my honor that I have abided by the Stevens Honor System
#

import random, sys

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """
    Creates and returns a new list of height rows and width column.
    All elements are initialized to zero
    """
    A = []
    for row in range(height):
        A += [createOneRow(width)]
    return A

def printBoard(A):
    """
    This function prints the 2D list of lists A without spaces
    """
    for row in A:
        for col in row:
            sys.stdout.write(str(col))
        sys.stdout.write('\n')

def diagonalize(width, height):
    """
    Creates an empty board and then modifies it so that it has a diagonal
    strip of "on" cells
    """
    A = createBoard(width, height)
    # always go row, col, where row goes "down", col goes "right"
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

def innerCells(w, h):
    """
    Creates a board of cells, where all are living, except a 1-wide
    border around the edges
    """
    A = createBoard(w, h)
    for row in range(1, h - 1):
        for col in range(1, w - 1):
            A[row][col] = 1
            
    return A

def randomCells(w, h):
    """
    Creates a board of cells, with each being random whether it is
    living or not. The outer 1-wide edge will be 0, as above.
    """
    A = createBoard(w, h)
    for row in range(1, h - 1):
        for col in range(1, w - 1):
            A[row][col] = random.choice([0, 1])
    return A

def copy(A):
    """
    Creates a deep copy of the 2D array A
    """
    B = createBoard(len(A[0]), len(A))
    for row in range(len(A)):
        for col in range(len(A[0])):
            B[row][col] = A[row][col]
    return B

def innerReverse(A):
    """
    Creates a new array with all cells, besides those on the outer edge,
    flipped (that is, 0 to 1, or 1 to 0)
    """
    B = copy(A)
    for row in range(1, len(B) - 1):
        for col in range(1, len(B[0]) - 1):
            if B[row][col]:
                B[row][col] = 0
            else:
                B[row][col] = 1
    return B

def countNeighbors(row, col, A):
    """
    Returns the number of neighbors a particular cell has (at row, col)
    """
    count = 0
    if A[row-1][col-1]:
        count += 1
    if A[row-1][col]:
        count += 1    
    if A[row][col-1]:
        count += 1
    if A[row+1][col-1]:
        count += 1
    if A[row-1][col+1]:
        count += 1
    if A[row+1][col]:
        count += 1
    if A[row][col+1]:
        count += 1
    if A[row+1][col+1]:
        count += 1
    return count

def next_life_generation(A):
    """
    makes a copy of A and then advanced one         
    generation of Conway's game of life within        
    the *inner cells* of that copy.         
    The outer edge always stays 0. 
    """
    newA = copy(A)
    for row in range(1, len(A) - 1):
        for col in range(1, len(A[0]) - 1):
            cnt = countNeighbors(row, col, A)
            if cnt < 2 or cnt > 3:
                newA[row][col] = 0
            elif cnt == 3:
                newA[row][col] = 1
    return newA

                