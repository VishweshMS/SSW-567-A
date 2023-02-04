# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 16:57:35 2023

@author: Vishwesh
"""
import datetime
"""
classifyTriangle function takes three parameters a,b,c 
which are sides of triangle and determines if it is 
scalene, Equilateral, Right, Not a triangle, Invalid Input 
"""
def classifyTriangle(a, b, c):
    #check if input parameters are integers and have value greater than 0
    if (type(a) == int and type(b) == int and type(c) == int) and (a > 0 and b > 0 and c > 0):
        #check if triangle can be formed with given parameters
        if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
            return 'Not a Triangle'
        #if two sides are equal it forms equilateral triangle
        elif a == b and b == c:
            return 'Equilateral Triangle'
        #condition to check for right angled triangle
        elif ((b ** 2) + (c ** 2)) == (a ** 2) or ((a ** 2) + (b ** 2)) == (c ** 2) or ((a ** 2) + (c ** 2)) == (b ** 2) :
            return 'Right Triangle'
        #condition to check for scalene triangle
        elif (a != c) and (b != c) and (a != b) :
            return 'Scalene Triangle'
        else:
            return 'Isosceles Triangle'
    
    else:
        return 'Invalid Input'
    
def my_brand(assignment_name):
    print("=*=*=*= Vishwesh Malur Somashekar =*=*=*=")
    print("=*=*=*= Course 2023S-SSW567-WS =*=*=*=")
    print("=*=*=*= " + assignment_name + " =*=*=*=")
    print("=*=*=*= " + str(datetime.datetime.now()) + " =*=*=*=")


