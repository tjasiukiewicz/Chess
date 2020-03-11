#!/usr/bin/env python3.4

class Point2D(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point2D: x = " + str(self.x) + " y = " + str(self.y)

class Vector2D(object):

    def __init__(self, azimuth, module):
        self.azimuth = azimuth
        self.module = module

class Space2D(object):
    
    @staticmethod
    def translate(point, vector):
        # FIXME: Tu obciczenia nie są prawidłowe.
        # Oczywiście należy użyć sin/cos itp...
        p1 = Point2D(0,0)
        p1.x += vector.azimuth + vector.module
        p1.y += vector.azimuth + vector.module
        return p1

if __name__ == '__main__':
    p1 = Point2D(2, 4)
    p2 = Space2D.translate(p1, Vector2D(10,20))
    print(p1)
    print(p2)

