# Local imports
from .tabs.tabChange import TabChange

class FootersWriter:
    def __init__(self, writersManager):
        self.writersManager = writersManager
    
    def write(self):
        self.write_main_footer()
        self.write_geometry_footer()
        self.write_material_footer()
        
    def write_main_footer(self):
        self.writersManager.main_writer.write_with_tabs('</Viewport3D>', TabChange.Remove)
        
    def write_geometry_footer(self):
        self.writersManager.geometry_writer.write_with_tabs('</ResourceDictionary>', TabChange.Remove)
        
    def write_material_footer(self):
        self.writersManager.material_writer.write_with_tabs('</ResourceDictionary>', TabChange.Remove)