"""Write a function that computes the volume of a sphere given its radius"""
import math 
def vol(radius):
    volume =  (4/2) * math.pi * (radius**3)
    return volume

#check
vol(2)

