#Implement a program that asks the user to input three positive integers and determines
#whether they constitute the side lengths of some right-angle triangle.

import math

side1=int(input("enter a positive integer: "))
side2=int(input("enter a positive integer: "))
side3=int(input("enter a positive integer: "))

Sides=[]
Sides= sorted([side1,side2,side3])

print(Sides)

print(Sides[0])

if ((Sides[0]**2)+(Sides[1]**2))==Sides[2]**2:
    print ("they are sides of a right angle triangle")
else:
    print("they are not sides of a right angle triangle")