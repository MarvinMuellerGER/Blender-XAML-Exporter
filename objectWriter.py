# Local imports
from .geometryWriter import GeomeryWriter
from .materialWriter import MaterialWriter
from .mainObjectWriter import MainObjectWriter
from .tabChange import TabChange

class ObjectWriter:
    def __init__(self, writersManager, namesCollector):
        self.writer = writersManager.main_writer
        self.namesCollector = namesCollector
        self.geomeryWriter = GeomeryWriter(writersManager, namesCollector)
        self.materialWriter = MaterialWriter(writersManager, namesCollector)
        self.mainObjectWriter = MainObjectWriter(writersManager, namesCollector)
    
    def write(self, obj):
        if obj.type != "MESH":
            return
        groupName = self.namesCollector.getGroupName(obj)
        
        self.geomeryWriter.write(obj)
        self.materialWriter.write(obj)
        
        # write Main XAML
        if obj.children:
            self.writer.write_line(f'<Model3DGroup x:Name="{groupName}">', TabChange.Add, False)
        self.mainObjectWriter.write(obj)
        if obj.children:
            for child in obj.children:
                self.write(child)
            self.writer.write_line(f'</Model3DGroup>', TabChange.Remove)