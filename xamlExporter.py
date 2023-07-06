# Local imports
from .filesCollector import FilesCollector
from .writersManager import WritersManager
from .filesManager import FilesManager
from .headersWriter import HeadersWriter
from .mainResourcesWriter import MainResourcesWriter
from .camerasWriter import CamerasWriter
from .objectsWriter import ObjectsWriter
from .footersWriter import FootersWriter

class XamlExporter:
    def __init__(self):
        self.filesCollector = FilesCollector()
        self.writersManager = WritersManager()
        self.filesManager = FilesManager(self.filesCollector, self.writersManager)
        self.headersWriter = HeadersWriter(self.writersManager)
        self.mainResourcesWriter = MainResourcesWriter(self.writersManager, self.filesCollector)
        self.mainCamerasWriter = CamerasWriter(self.writersManager)
        self.objectsWriter = ObjectsWriter(self.writersManager)
        self.footersWriter = FootersWriter(self.writersManager)
    
    def export(self, filepath, include_only_selected_ones, include_only_visible_ones, objects_settings):
        self.filesCollector.set_main_file_path(filepath)
        self.filesManager.set_files()
        self.objectsWriter.set_top_level_objects(include_only_selected_ones, include_only_visible_ones)
        
        self.headersWriter.write()
        self.mainResourcesWriter.write()
        self.mainCamerasWriter.write()
        self.objectsWriter.write()
        self.footersWriter.write()
        self.filesManager.writeFiles()
        return True