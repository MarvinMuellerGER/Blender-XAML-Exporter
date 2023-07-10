# Local imports
from .xamlWriterWithTabs import XamlWriterWithTabs

class xamlWritersManager:
    def __init__(self):
        self.main_writer = XamlWriterWithTabs()
        self.geometry_writer = XamlWriterWithTabs()
        self.material_writer = XamlWriterWithTabs()