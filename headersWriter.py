# Local imports
from .tabChange import TabChange

class HeadersWriter:
    def __init__(self, writersManager):
        self.writersManager = writersManager
        self.main_writer = self.writersManager.main_writer
        self.geometry_writer = self.writersManager.geometry_writer
        self.material_writer = self.writersManager.material_writer
        
    def write(self):
        self.write_main_header()
        self.write_geometry_header()
        self.write_material_header()
            
    def write_main_header(self):
        self.main_writer.write_line('<Viewport3D xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"')
        self.main_writer.write_line('xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"', TabChange.Add)
        self.main_writer.write_line('Width="800" Height="600">')
        
    def write_geometry_header(self):
        self.geometry_writer.write_line('<ResourceDictionary xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"')
        self.geometry_writer.write_line('xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">', TabChange.Add)
        
    def write_material_header(self):
        self.material_writer.write_line('<ResourceDictionary xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"')
        self.material_writer.write_line('xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">', TabChange.Add)