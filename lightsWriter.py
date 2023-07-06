import bpy
import mathutils

# Local imports
from .colorHexConverter import ColorHexConverter

class LightsWriter:
    def __init__(self, writersManager):
        self.colorHexConverter = ColorHexConverter()
        self.writer = writersManager.main_writer
        
    def write(self):
        light_objects = self.getLights()
        for light_object in light_objects:
            light_type = self.getLightType(light_object)
            name = self.getNameString(light_object)
            color = self.getColorString(light_object)
            if light_type == 'PointLight' or light_type == 'SpotLight':
                position = self.getPositionString(light_object)
            else:
                position = ''
            if light_type == 'SpotLight':
                direction = self.getDirectionString(light_object)
                cone_angle = self.getConeAngleString(light_object)
                direction_and_cone_angle = ' ' + direction + cone_angle
            else:
                direction_and_cone_angle = ''
            self.writer.write_line(f'<{light_type} {name} {color} {position}{direction_and_cone_angle} />')

    def getNameString(self, light_object):
        return f'x:Name="{light_object.name}"'
    
    def getColorString(self, light_object):
        colorHex = self.getColorHex(light_object)
        return f'Color="{colorHex}"'

    def getPositionString(self, light_object):
        return self.getMatrixString('Position', self.getPosition(light_object))

    def getDirectionString(self, light_object):
        return self.getMatrixString('Direction', self.getDirection(light_object))

    def getMatrixString(self, name, matrix):
        x, y, z = matrix
        return f'{name}="{x:.2f},{y:.2f},{z:.2f}"'

    def getConeAngleString(self, light_object):
        outer = self.getOuterConeAngleString(light_object)
        inner = self.getInnerConeAngleString()
        return f'{outer} {inner}'

    def getOuterConeAngleString(self, light_object):
        angle = self.getOuterConeAngle(light_object)
        return f'OuterConeAngle="{angle}"'

    def getInnerConeAngleString(self):
        return f'InnerConeAngle="0"'
        
    def getLights(self):
        return [obj for obj in bpy.context.scene.objects if obj.type == 'LIGHT']

    def getLightType(self, light):
        light_type = light.data.type
        if light_type == 'POINT':
            return 'PointLight'
        if light_type == 'SUN':
            return 'AmbientLight'
        if light_type == 'SPOT':
            return 'SpotLight'
        if light_type == 'AREA':
            return 'AmbientLight'

    def getColorHex(self, light_object):
        color = light_object.data.color
        return self.colorHexConverter.getColorHex(color)
    
    def getPosition(self, light_object):
        x, y, z = light_object.location
        return x, y, z

    def getDirection(self, light_object):
        x, y, z = light_object.rotation_euler.to_quaternion() @ mathutils.Vector((0, 0, -1))
        return x, y, z

    def getOuterConeAngle(self, light_object):
        return light_object.data.spot_size