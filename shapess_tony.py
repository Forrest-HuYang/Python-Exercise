import easygui
import math
from math import pi

class Rectangle:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def getArea(self):
        area = self.height * self.width
        return (area)

    def getCircum(self):
        circum = (self.height + self.width) * 2
        return circum

class Cuboid:
    
    def __init__(self , myRect , height):
        self.bottom = myRect
        self.height = height

    def getVolume(self):
        volume = self.bottom.getArea() * self.height 
        return volume


class Triangle:

    def __init__(self, sideA, sideB , sideC):
        self.sideA = sideA
        self.sideB = sideB
        self.sideC = sideC
        
        

    def getArea(self):
        p = (self.sideA + self.sideB +self.sideC)/2
        area = (p * (p - self.sideA) * (p - self.sideB) * (p - self.sideC))**(1/2)
        return area
    
    def getCircum(self):
        circum = self.sideA + self.sideB +self.sideC
        return circum
    


class Triangular_prism:
    
    def __init__(self , myTriangle , height):
        self.bottom = myTriangle
        self.height = height

    def getVolume(self):
        volume = self.bottom.getArea() * self.height 
        return volume

    



class Circle:

    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        area = ((self.radius))**2 * pi
        return (area)

    def getCircum(self):
        circum = self.radius * 2 * pi
        return circum

class Cylinder:
    
    def __init__(self , myCircle , height):
        self.bottom = myCircle
        self.height = height

    def getVolume(self):
        volume = self.bottom.getArea() * self.height 
        return volume
#########################################

choice = easygui.enterbox( "If you want a Triangle, please type 1; Rectangle, type 2; Circle, type 3.")

if choice == "1":
    sideA_tri = float(easygui.enterbox("Enter first side of triangle"))
    sideB_tri = float(easygui.enterbox("Enter second side of triangle"))
    sideC_tri = float(easygui.enterbox("Enter third side of triangle"))
    height_tri = float(easygui.enterbox("Enter height of triangular prism (type zero if you don't want a three dimensional object)"))
    if (sideA_tri + sideB_tri <= sideC_tri) or (sideA_tri + sideC_tri <= sideB_tri) or (sideC_tri + sideB_tri <= sideA_tri):
        easygui.msgbox ("Such a triangle doesn't exist")
    else:
        myTriangle = Triangle(sideA_tri , sideB_tri , sideC_tri)
        area_display = str(myTriangle.getArea())
        circum_display = str(myTriangle.getCircum())
        if height_tri != 0:
            myTriangularPrism = Triangular_prism(myTriangle , height_tri)
            volume_display = str(myTriangularPrism.getVolume())
            easygui.msgbox("the volume of the 3D object is " + volume_display)



    

if choice == "2":
    length_rect = float(easygui.enterbox("Enter length of rectangle"))
    width_rect = float(easygui.enterbox("Enter width of rectangle"))
    height_rect = float(easygui.enterbox("Enter height of cuboid (type zero if you don't want a three dimensional object)"))
    myRect = Rectangle(length_rect, width_rect)
    area_display = str(myRect.getArea())
    circum_display = str(myRect.getCircum())
    if height_rect != 0:
        myCuboid = Cuboid(myRect , height_rect)
        volume_display = str(myCuboid.getVolume())
        easygui.msgbox("the volume of the 3D object is " + volume_display)

if choice == "3":
    radius_circle = float(easygui.enterbox("Enter radius of circle"))
    myCircle = Circle(radius_circle)
    area_display = str(myCircle.getArea())
    circum_display = str(myCircle.getCircum())
    height_circle = float(easygui.enterbox("Enter height of cuboid (type zero if you don't want a three dimensional object)"))
    if height_circle != 0:
        myCylinder = Cylinder(myCircle , height_circle)
        volume_display = str(myCylinder.getVolume())
        easygui.msgbox("the volume of the 3D object is " + volume_display)



easygui.msgbox("The area of that 2D shape is " + area_display + "\n" + "\n" + "The circumference of that 2D shape is " + circum_display)

   


#######################################
