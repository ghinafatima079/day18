"""Create a Python class Point to represent a point in 2D space with attributes x and y. 
Implement the __add__() method to allow adding two Point objects together, where addition is performed element-wise (i.e., adding the x values together and the y values together). 
Then, demonstrate the use of the overloaded + operator by adding two Point objects."""
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return f"{self.x},{self.y}"
    def __add__(self,p):
        return Point(self.x+p.x , self.y+p.y)
p1=Point(3,5)
print(f"({p1})")
p2=Point(4,6)
print(f"({p2})")
print(f"({p1+p2})")