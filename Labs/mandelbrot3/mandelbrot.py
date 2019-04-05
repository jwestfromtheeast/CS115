# mandelbrot.py
# Lab 9
#
# Name:

# keep this import line...
from cs5png import *

# start your Lab 9 functions here:
def mult(c, n):
    """
    Returns the product of c times n without multiplication.
    Holds a result value and uses a for loop.
    """
    result = 0
    for x in range(n):
        result += c
    return result

def update(c, n):
    """
    Starts a new value, z, at zero, and repeatedly updates it using the
    assignment statement z = z**2 + c for a total of n times.
    Returns the final value of z.
    """
    z = 0
    for x in range(n):
        z = z**2 + c
    return z

def inMSet(c, n):
    """ inMSet takes in: 
            c for the update step of z = z**2+c             
            n, the maximum number of times to run that step         
        Then, it should return:              
            False as soon as abs(z) gets larger than 2             
            True if abs(z) never gets larger than 2 (for n iterations)     
    """ 
    z = 0
    for x in range(n):
        z = z**2 + c
        if abs(z) > 2:
            return False
    return True

def weWantThisPixel(col, row):
    """
    A function that returns True if we want the pixel
    at col, row, and False otherwise
    """
    if not col % 10 or not row % 10:
        return True
    return False

def test():
    """
    A function to demonstrate how to create and save a png image
    """
    width = 300
    height = 200
    image = PNGImage(width, height)
    
    # create a loop in order to draw some pixels
    
    for col in range(width):
        for row in range(height):
            if weWantThisPixel(col, row):
                image.plotPoint(col, row)
    
    # done iterating through pixels
    image.saveFile()
# How the image would change: it would "connect the dots"

def scale(pix, pixMax, floatMin, floatMax):
    """ scale takes in:
            pix, the current pixel value column or row
            pixMax, the total # of pixel columns
            floatMin, the min floating-point value
            floatMax, the max floating-point value that
                corresponds to pix
    """
    q1 = 1.0 * pix / pixMax
    q2 = floatMax - floatMin
    return q1 * q2 + floatMin    

def mset():
    """
    Creates a 300x200 image of the Mandelbrot set
    """
    width = 300
    height = 200
    image = PNGImage(width, height)
    
    # create a loop to draw some pixels
    
    for col in range(width):
        for row in range(height):
            x = scale(col, width, -2.0, 1.0)
            y = scale(row, height, -1.0, 1.0)
            c = x + y * 1j
            # Change n as desired
            if inMSet(c, 25):
                image.plotPoint(col, row)
    
    image.saveFile()
    
mset()