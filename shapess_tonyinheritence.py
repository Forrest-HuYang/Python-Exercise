import easygui
import math
from math import pi


#########################################


class Rectangle():

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def getArea(self):
        area = self.height * self.width
        return (area)

    def getCircum(self):
        circum = (self.height + self.width) * 2
        return circum


class Triangle():

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

    
class Circle():

    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        area = ((self.radius))**2 * pi
        return (area)

    def getCircum(self):
        circum = self.radius * 2 * pi
        return circum

class Pillar:
    
    def __init__(self , myShape , height):
        self.bottom = myShape
        self.height = height

    def getVolume(self):
        volume = self.bottom.getArea() * self.height 
        return volume

    def getSuperficialArea(self):
        SuperficialArea = (self.bottom.getCircum() * self.height) + self.bottom.getArea() * 2
        return SuperficialArea


#########################################


choice = easygui.enterbox( "If you want a Triangle, please type 1; Rectangle, type 2; Circle, type 3.")
height = float(easygui.enterbox("Enter height of the pillar (type zero if you don't want a three dimensional object)"))
if choice == "1":
    sideA_tri = float(easygui.enterbox("Enter first side of triangle"))
    sideB_tri = float(easygui.enterbox("Enter second side of triangle"))
    sideC_tri = float(easygui.enterbox("Enter third side of triangle"))
    if (sideA_tri + sideB_tri <= sideC_tri) or (sideA_tri + sideC_tri <= sideB_tri) or (sideC_tri + sideB_tri <= sideA_tri):
        easygui.msgbox ("Such a triangle doesn't exist. the following are hypothetical statistics.")
        myShape = Triangle(sideA_tri , sideB_tri , sideC_tri)
            
if choice == "2":
    length_rect = float(easygui.enterbox("Enter length of rectangle"))
    width_rect = float(easygui.enterbox("Enter width of rectangle"))
    myShape = Rectangle(length_rect, width_rect)
        
if choice == "3":
    radius_circle = float(easygui.enterbox("Enter radius of circle"))
    myShape = Circle(radius_circle)
    
area_display = str(myShape.getArea())
circum_display = str(myShape.getCircum())
    
if height != 0:
    myPillar = Pillar(myShape , height)
    volume_display = str(myPillar.getVolume())
    SuperficialArea_display = str(myPillar.getSuperficialArea())
        

#######################################


easygui.msgbox("the volume of the 3D object is " + volume_display + "\n" + "\n" + "the superficial area of the 3D object is " + SuperficialArea_display)
easygui.msgbox("The area of that 2D shape is " + area_display + "\n" + "\n" + "The circumference of that 2D shape is " + circum_display)