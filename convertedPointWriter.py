# Local imports
from .pointWriter import PointWriter

class ConvertedPointWriter:
    def __init__(self, writer):
        self.pointWriter = PointWriter(writer)

    def write(self, point):
        x, y, z = self.convertPoint(point)
        self.pointWriter.write(x, y, z)

    def convertPoint(self, point):
        x = self.convertPointAxis(point.x)
        y = self.convertPointAxis(point.y)
        z = self.convertPointAxis(point.z)
        return x, y, z

    def convertPointAxis(self, axis):
        return self.compactFloat(round(axis, 6))

    def compactFloat(self, number):
        str = "%.6f" % number
        if len(str) == 0 : return str
        backStr = str[-5:]
        frontStr = str[:-5]
        str = frontStr + backStr.rstrip("0")
        return str