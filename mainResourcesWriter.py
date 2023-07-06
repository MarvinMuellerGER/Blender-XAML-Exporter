# Local imports
from .tabChange import TabChange

class MainResourcesWriter:
    def __init__(self, writersManager, files_collector):
        self.writer = writersManager.main_writer
        self.files_collector = files_collector
        
    def write(self):
        self.writer.write_line('<Viewport3D.Resources>')
        self.writer.write_line('<ResourceDictionary>', TabChange.Add)
        self.writer.write_line('<ResourceDictionary.MergedDictionaries>', TabChange.Add)
        self.writer.write_line(f'<ResourceDictionary Source="{self.files_collector.geomety_file_name}" />', TabChange.Add)
        self.writer.write_line(f'<ResourceDictionary Source="{self.files_collector.material_file_name}" />')
        self.writer.write_line('</ResourceDictionary.MergedDictionaries>', TabChange.Remove)
        self.writer.write_line('</ResourceDictionary>', TabChange.Remove)
        self.writer.write_line('</Viewport3D.Resources>', TabChange.Remove)