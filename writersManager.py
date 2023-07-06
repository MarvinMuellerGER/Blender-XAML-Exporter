# Local imports
from .writerWithTabs import WriterWithTabs

class WritersManager:
    def __init__(self):
        self.main_writer = WriterWithTabs()
        self.geometry_writer = WriterWithTabs()
        self.material_writer = WriterWithTabs()