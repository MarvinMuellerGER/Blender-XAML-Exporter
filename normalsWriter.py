# Local imports
from .convertedPointWriter import ConvertedPointWriter

class NormalsWriter:
    def __init__(self, writer):
        self.writer = writer
        self.convertedPointWriter = ConvertedPointWriter(writer)

    def write(self, mesh):
        self.writer.write('Normals="')
        first = True
        for polygon in mesh.polygons:
            if first:
                first = False
            else:
                self.writer.write(' ')
            self.convertedPointWriter.write(polygon.normal)
        self.writer.write('" ')