# Local imports
from .pointWriters.pointWriter import PointWriter
from .pointWriters.convertedPointWriter import ConvertedPointWriter

class PositionsAndTriangleIndicesWriter:
    def __init__(self, writer):
        self.writer = writer
        self.pointWriter = PointWriter(self.writer)
        self.convertedPointWriter = ConvertedPointWriter(self.writer)

    def write(self, mesh):
        vertices, polygons = self.getVerticesAndPolygons(mesh)
        self.writer.write('Positions="')
        first = True
        for vertice in vertices:
            if first:
                first = False
            else:
                self.writer.write(' ')
            self.convertedPointWriter.write(vertice.co)
        self.writer.write('" ')
        self.writer.write('TriangleIndices="')
        first = True
        for polygon in polygons:
            if first:
                first = False
            else:
                self.writer.write(' ')
            self.writeVertice(polygon)
        self.writer.write('" ')

    def writeVertice(self, polygon):
        vertices = polygon
        i = 2
        while i < len(vertices):
            if i > 2:
                self.writer.write(' ')
            self.writeTriangleIndice(vertices, i)
            i += 1
    
    def writeTriangleIndice(self, vertices, index):
        x, y, z = self.getTriangleIndice(vertices, index)
        self.pointWriter.write(x, y, z)

    def getVerticesAndPolygons(self, mesh):
        originalVertices = mesh.vertices
        originalPolygons = mesh.polygons
        newVertices = []
        newPolygons = []
        index = 0
        for polygon in originalPolygons:
            vertices = polygon.vertices
            newPolygon = []
            for vertice in vertices:
                newVertice = originalVertices[vertice]
                newVertices.append(newVertice)
                newPolygon.append(index)
                index += 1
            newPolygons.append(newPolygon)
        return newVertices, newPolygons

    def getTriangleIndice(self, vertices, index):
        x = vertices[0]
        y = vertices[index-1]
        z = vertices[index]
        return x, y, z