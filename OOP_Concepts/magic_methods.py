#!/usr/bin/python3
#definning Class Rectangle
class Rectangle:
    def __init__(self,length,width):
        self.width=width
        self.lenght=length

        #defining property method called area for calculating 
    @property
    def area(self):

        return (self.lenght * self.width)
    #Using the perimeter property to find the perimeter of the Rectangle
    @property
    def perimeter(self):
        #calculating the perimeter of the Rectangle
        return 2*self.width + self.lenght
    
    def __str__(self):
        #returning a string representation of the rectangle
        return "Rectangle({length ,with})"
    
    # definning a method to compare the two rectangles and check whether their areas are the same
    def __eq__(self,other):
        if isinstance(other,Rectangle):
            return self.area == other.area
        return False

rectangle1 = Rectangle(4,7) 
rectangle2 =Rectangle(8,7)
#printing the area and perimeter
print(f"{rectangle1}-> Area:{rectangle1.area},Perimeter{rectangle1.perimeter}")
print(f"{rectangle2}-> Area:{rectangle2.area},Perimeter{rectangle2.perimeter}")


    