# Local imports
from .xamlWriter import XamlWriter

class XamlWriters:
    def __init__(self):
        self.main_writer = XamlWriter()
        self.geomety_writer = XamlWriter()
        self.material_writer = XamlWriter()