#Aastha Sangani
#U73625733

#polygons module

import math

class regularPolygon:
    def __init__(self):
        self.__sides = 0
        self.__length = 0.0

    def setSides(self,num_side):
        self.__sides = num_side

    def setLength(self,length_size):
        self.__length = length_size

    def getSides(self):
        return self.__sides

    def getLength(self):
        return self.__length

    def perimeter(self):
        p = self.__sides * self.__length
        return p

    def area(self):
        a = (self.__sides * self.__length) **2/(4*math.tan(math.pi/self.__sides))
        return a
    
