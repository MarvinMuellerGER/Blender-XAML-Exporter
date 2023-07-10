# Local imports
from ....collectors.colorsCollector import ColorsCollector
from ....tabs.tabChange import TabChange

class MaterialWriter:
    def __init__(self, writersManager, namesCollector):
        self.writer = writersManager.material_writer
        self.namesCollector = namesCollector
        self.colorsCollector = ColorsCollector()
    
    def write(self, object):
        self.colorsCollector.setObject(object)
        self.write_header(object)
        self.write_diffuse_material()
        self.write_specular_material()
        self.write_footer()
        
    def write_header(self, object):
        materialName = self.namesCollector.getMaterialName(object)
        self.writer.write_line(f'<MaterialGroup x:Key="{materialName}">')
        
    def write_diffuse_material(self):
        diffuse_hex = self.colorsCollector.getDiffuseHex()
        self.writer.write_line('<DiffuseMaterial>', TabChange.Add)
        self.writer.write_line('<DiffuseMaterial.Brush>', TabChange.Add)
        self.writer.write_line(f'<SolidColorBrush Color="{diffuse_hex}"/>', TabChange.Add)
        self.writer.write_line('</DiffuseMaterial.Brush>', TabChange.Remove)
        self.writer.write_line('</DiffuseMaterial>', TabChange.Remove)
        
    def write_specular_material(self):
        specular_hex = self.colorsCollector.getSpecularHex()
        if specular_hex is None:
            return
        self.writer.write_line('<SpecularMaterial>')
        self.writer.write_line('<SpecularMaterial.Brush>', TabChange.Add)
        self.writer.write_line(f'<SolidColorBrush Color="{specular_hex}"/>', TabChange.Add)
        self.writer.write_line(f'</SpecularMaterial.Brush>', TabChange.Remove)
        self.writer.write_line('</SpecularMaterial>', TabChange.Remove)
        
    def write_footer(self):
        self.writer.write_line('</MaterialGroup>', TabChange.Remove)