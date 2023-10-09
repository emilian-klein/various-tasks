"""
Task:
    Create classes called Triangle and Point. The constructor of Triangle class accepts three arguments - all of them
    are objects of the Point class. The points are stored inside the object as a private list, the class provides a
    parameterless method called perimeter(), which calculates the perimeter of the triangle described by the three points.
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


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__triangle_points = [vertice1, vertice2, vertice3]

    def perimeter(self):
        side1 = self.__triangle_points[0].distance_from_point(self.__triangle_points[1])
        side2 = self.__triangle_points[1].distance_from_point(self.__triangle_points[2])
        side3 = self.__triangle_points[2].distance_from_point(self.__triangle_points[0])
        return side1 + side2 + side3


if __name__ == "__main__":
    triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
    print(triangle.perimeter())
