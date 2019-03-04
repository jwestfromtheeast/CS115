'''
Created on Feb 27, 2019
I pledge my honor that I have abided by the Stevens Honor System.
@author: Justin Westley
username: jwestley
'''
import unittest
import hw4

# Test hw4
class Test(unittest.TestCase):
    # Test pascal_row()
    def test01(self):
        self.assertEqual(hw4.pascal_row(0), [1])
    
    def test02(self):
        self.assertEqual(hw4.pascal_row(1), [1,1])

    def test03(self):
        self.assertEqual(hw4.pascal_row(2), [1,2,1])
    
    def test04(self):
        self.assertEqual(hw4.pascal_row(7), [1, 7, 21, 35, 35, 21, 7, 1])
    
    def test05(self):
        self.assertEqual(hw4.pascal_row(15), [1, 15, 105, 455, 1365, 3003, 5005, 6435, 6435, 5005, 3003, 1365, 455, 105, 15, 1])
    
    # Test pascal_triangle()
    def test06(self):
        self.assertEqual(hw4.pascal_triangle(0), [[1]])
    
    def test07(self):
        self.assertEqual(hw4.pascal_triangle(1), [[1], [1,1]])
    
    def test08(self):
        self.assertEqual(hw4.pascal_triangle(2), [[1], [1, 1], [1, 2, 1]])
    
    def test09(self):
        self.assertEqual(hw4.pascal_triangle(11), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1], [1, 8, 28, 56, 70, 56, 28, 8, 1], [1, 9, 36, 84, 126, 126, 84, 36, 9, 1], [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1], [1, 11, 55, 165, 330, 462, 462, 330, 165, 55, 11, 1]])
    
    def test10(self):
        self.assertEqual(hw4.pascal_triangle(14), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1], [1, 8, 28, 56, 70, 56, 28, 8, 1], [1, 9, 36, 84, 126, 126, 84, 36, 9, 1], [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1], [1, 11, 55, 165, 330, 462, 462, 330, 165, 55, 11, 1], [1, 12, 66, 220, 495, 792, 924, 792, 495, 220, 66, 12, 1], [1, 13, 78, 286, 715, 1287, 1716, 1716, 1287, 715, 286, 78, 13, 1], [1, 14, 91, 364, 1001, 2002, 3003, 3432, 3003, 2002, 1001, 364, 91, 14, 1]])
    
if __name__ == "__main__":
    unittest.main()