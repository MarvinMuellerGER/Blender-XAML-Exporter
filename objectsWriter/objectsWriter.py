# Local imports
from ..collectors.namesCollector import NamesCollector
from .objectWriter.objectWriter import ObjectWriter
from .lightsWriter.lightsWriter import LightsWriter
from ..collectors.objectsCollector import ObjectsCollector
from ..tabs.tabChange import TabChange

class ObjectsWriter:
    def __init__(self, writersManager):
        self.writer = writersManager.main_writer
        self.namesCollector = NamesCollector()
        self.objectWriter = ObjectWriter(writersManager, self.namesCollector)
        self.lightsWriter = LightsWriter(writersManager)
        
    def set_top_level_objects(self, include_only_selected_ones, include_only_visible_ones):
        objectsCollector = ObjectsCollector()
        self.top_level_objects = objectsCollector.get_top_level_objects(include_only_selected_ones, include_only_visible_ones)
        
    def write(self):
        self.write_header()
        for obj in self.top_level_objects:
            self.objectWriter.write(obj)
        self.write_footer()
    
    def write_header(self):
        project_name = self.namesCollector.getProjectName()
        self.writer.write_line('<ModelVisual3D>')
        self.writer.write_line('<ModelVisual3D.Content>', TabChange.Add)
        self.writer.write_line_with_2tabs('<Model3DGroup x:Name="Scene">', TabChange.Add, TabChange.Add)
        self.lightsWriter.write()
        self.writer.write_line(f'<Model3DGroup x:Name="{project_name}">')
        self.writer.tab_string_manager.edit(TabChange.Add)

    def write_footer(self):
        self.writer.write_line('</Model3DGroup>', TabChange.Remove)
        self.writer.write_line('</Model3DGroup>', TabChange.Remove)
        self.writer.write_line('</ModelVisual3D.Content>', TabChange.Remove)
        self.writer.write_line('</ModelVisual3D>', TabChange.Remove)