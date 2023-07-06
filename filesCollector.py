import os
import bpy

class FilesCollector:
    def __init__(self, file_path = None):
        if (file_path is not None):
            self.set_main_file_path(file_path)
        
    def set_main_file_path(self, file_path):
        self.geomety_file_name = 'Geometry.xaml'
        self.material_file_name = 'Material.xaml'
        self.main_file_path = file_path
        self.set_folder_path()
        self.set_main_file_name()
        self.set_geometry_file_path()
        self.set_material_file_path()
        
    def set_folder_path(self):
        self.folder_path = os.path.dirname(self.main_file_path)
        
    def set_main_file_name(self):
        self.main_file_name = f'{os.path.splitext(os.path.basename(bpy.data.filepath))[0]}.xaml'
        
    def set_geometry_file_path(self):
        self.geometry_file_path = f'{self.folder_path}/{self.geomety_file_name}'
        
    def set_material_file_path(self):
        self.material_file_path = f'{self.folder_path}/{self.material_file_name}'