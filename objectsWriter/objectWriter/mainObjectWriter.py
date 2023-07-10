# Local imports
from ...tabs.tabChange import TabChange

class MainObjectWriter:
    def __init__(self, writersManager, namesCollector):
        self.writer = writersManager.main_writer
        self.namesCollector = namesCollector
        
    def write(self, obj):
        objectName = self.namesCollector.getObjectName(obj)
        nestedObjectName = self.namesCollector.getNestedObjectName(obj)
        geometryName = self.namesCollector.getGeometryName(obj)
        materialName = self.namesCollector.getMaterialName(obj)
        self.writer.write_line(f'<Model3DGroup x:Name="{objectName}">')
        self.writer.write_line(f'<Model3DGroup x:Name="{nestedObjectName}">', TabChange.Add)
        self.writer.write_line(f'<GeometryModel3D Geometry="{{StaticResource {geometryName}}}" Material="{{StaticResource {materialName}}}" BackMaterial="{{StaticResource {materialName}}}" />', TabChange.Add)
        self.writer.write_line(f'</Model3DGroup>', TabChange.Remove)
        self.writer.write_line(f'</Model3DGroup>', TabChange.Remove)