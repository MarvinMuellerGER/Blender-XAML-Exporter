# Local imports
from .colorHexConverter import ColorHexConverter

class ColorsCollector:
    def __init__(self):
        self.colorHexConverter = ColorHexConverter()
    
    def setObject(self, object):
        self.object = object
        self.setMaterial(object)
    
    def setMaterial(self, object):
        self.material = object.active_material

    def getDiffuseHex(self):
        diffuse_color = self.getDiffuseColor()
        return self.colorHexConverter.getColorHex(diffuse_color)
    
    def getDiffuseColor(self):
        if self.material is None:
            return self.object.color
        else:
            return self.material.diffuse_color
        
    def getSpecularHex(self):
        if self.material is None:
            return None
        specular_color = self.material.specular_color
        return self.colorHexConverter.getColorHex(specular_color)