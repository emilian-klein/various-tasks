"""
Task:
    Create class called Point, it's constructor accepts two arguments (x and y respectively), both default to zero.
    All the properties should be private. The class contains two parameterless methods called getx() and gety(),
    which return each of the two coordinates. The class provides a method called distance_from_xy(x,y), which calculates
    and returns the distance between the point stored inside the object and the other point given as a pair of floats.
    The class provides a method called distance_from_point(point), which calculates the distance
    (like the previous method), but the other point's location is given as another Point class object.
"""
import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.sqrt(((self.__x - x) ** 2) + ((self.__y - y) ** 2))

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())


if __name__ == "__main__":
    point1 = Point(10, 0)
    point2 = Point(1, -23)
    print(point1.distance_from_point(point2))
    print(point2.distance_from_xy(23, 0))
