# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 16:57:35 2023
Python Unit Test cases to test the implementation of classifying triangles 
@author: Vishwesh
"""
import unittest
from Triangle import classifyTriangle,my_brand
class TestTriangleClassification(unittest.TestCase):
    #function to test if triangle is equilateral
    def test_equilateral(self):
        test_result = classifyTriangle(5, 5, 5)
        self.assertEqual(test_result, "Equilateral Triangle")
        test_result = classifyTriangle(4, 4, 4)
        self.assertEqual(test_result, "Equilateral Triangle")
        test_result = classifyTriangle(12, 12, 12)
        self.assertEqual(test_result, "Equilateral Triangle")
        test_result = classifyTriangle(33, 33, 33)
        self.assertEqual(test_result, "Equilateral Triangle")
        test_result = classifyTriangle(2, 2, 2)
        self.assertEqual(test_result, "Equilateral Triangle")

    #function to test if triangle is isoscles
    def test_isosceles(self):
        test_result = classifyTriangle(8, 10, 10)
        self.assertEqual(test_result, "Isosceles Triangle")
        test_result = classifyTriangle(12, 14, 14)
        self.assertEqual(test_result, "Isosceles Triangle")
        test_result = classifyTriangle(9, 6, 9)
        self.assertEqual(test_result, "Isosceles Triangle")
        test_result = classifyTriangle(10, 12, 12)
        self.assertEqual(test_result, "Isosceles Triangle")
        test_result = classifyTriangle(5, 7, 7)
        self.assertEqual(test_result, "Isosceles Triangle")

    #function to test if triangle is scalene
    def test_scalene(self):
        test_result = classifyTriangle(4, 5, 6)
        self.assertEqual(test_result, "Scalene Triangle")
        test_result = classifyTriangle(7, 9, 11)
        self.assertEqual(test_result, "Scalene Triangle")
        test_result = classifyTriangle(12, 15, 20)
        self.assertEqual(test_result, "Scalene Triangle")
        test_result = classifyTriangle(25, 30, 35)
        self.assertEqual(test_result, "Scalene Triangle")
        test_result = classifyTriangle(40, 45, 55)
        self.assertEqual(test_result, "Scalene Triangle")
        
    #function to test if triangle is right angled
    def test_right(self):
        test_result = classifyTriangle(6, 8, 10)
        self.assertEqual(test_result, "Right Triangle")
        test_result = classifyTriangle(3, 4, 5)
        self.assertEqual(test_result, "Right Triangle")
        test_result = classifyTriangle(9, 12, 15)
        self.assertEqual(test_result, "Right Triangle")
        test_result = classifyTriangle(5, 12, 13)
        self.assertEqual(test_result, "Right Triangle")
        test_result = classifyTriangle(8, 15, 17)
        self.assertEqual(test_result, "Right Triangle")

    #function to test if parameters doesnot form a triangle
    def test_NotATriangle(self):
        test_result = classifyTriangle(2,3,7)
        self.assertEqual(test_result, "Not a Triangle")
        test_result = classifyTriangle(4,5,12)
        self.assertEqual(test_result, "Not a Triangle")
        test_result = classifyTriangle(6,8,15)
        self.assertEqual(test_result, "Not a Triangle")
        test_result = classifyTriangle(10,11,21)
        self.assertEqual(test_result, "Not a Triangle")
        test_result = classifyTriangle(9,13,22)
        self.assertEqual(test_result, "Not a Triangle")
        
    #function to test for invalid inputs
    def test_Invalid(self):
        test_result = classifyTriangle(-1, 2, 3)
        self.assertEqual(test_result, "Invalid Input")
        test_result = classifyTriangle(1.1, 2, 3)
        self.assertEqual(test_result, "Invalid Input")
        test_result = classifyTriangle(0, 0, 1)
        self.assertEqual(test_result, "Invalid Input")
        test_result = classifyTriangle("3", 3, 6)
        self.assertEqual(test_result, "Invalid Input")
        test_result = classifyTriangle(2.0, 2.0, 2.0)
        self.assertEqual(test_result, "Invalid Input")

if __name__ == '__main__':
    my_brand("HW 01")
    unittest.main()
    print('Starting Unit Tests')
    my_brand("HW 01")
