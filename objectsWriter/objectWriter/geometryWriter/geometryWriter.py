# Local imports
from .meshExtractor import MeshExtractor
from .positionsAndTriangleIndicesWriter import PositionsAndTriangleIndicesWriter
# from .normalsWriter import NormalsWriter

class GeomeryWriter:
    def __init__(self, writersManager, namesCollector):
        self.writer = writersManager.geometry_writer
        self.namesCollector = namesCollector
        self.meshExtractor = MeshExtractor()
        self.positionsAndTriangleIndicesWriter = PositionsAndTriangleIndicesWriter(self.writer)
        # self.normalsWriter = NormalsWriter(self.writer)
        
    def write(self, obj):
        mesh = self.meshExtractor.getMesh(obj)
        geometryName = self.namesCollector.getGeometryName(obj)
        self.writer.write_with_tabs(f'<MeshGeometry3D x:Key="{geometryName}" ')
        self.positionsAndTriangleIndicesWriter.write(mesh)
        # self.normalsWriter.write(mesh)
        self.writer.write('/>\n')