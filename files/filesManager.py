# Local imports
from .fileWriter import FileWriter

class FilesManager:
    def __init__(self, files_collector, writers_manager):
        self.files_collector = files_collector
        self.writers_manager = writers_manager
        self.mainFileWriter = FileWriter()
        self.geometryFileWriter = FileWriter()
        self.materialFileWriter = FileWriter()
        
    def set_files(self):
        self.mainFileWriter.set_filepath_and_writer(self.files_collector.main_file_path, self.writers_manager.main_writer)
        self.geometryFileWriter.set_filepath_and_writer(self.files_collector.geometry_file_path, self.writers_manager.geometry_writer)
        self.materialFileWriter.set_filepath_and_writer(self.files_collector.material_file_path, self.writers_manager.material_writer)

    def writeFiles(self):
        self.mainFileWriter.WriteAll()
        self.geometryFileWriter.WriteAll()
        self.materialFileWriter.WriteAll()