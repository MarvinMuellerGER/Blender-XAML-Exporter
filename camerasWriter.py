import bpy
import mathutils

# Local imports
from .tabs.tabChange import TabChange

class CamerasWriter:
    def __init__(self, writersManager):
        self.writer = writersManager.main_writer
        
    def write(self):
        camera_objects = self.getCameras()
        for camera in camera_objects:
            self.writeCamera(camera)

    def writeCamera(self, camera):
        camera_type = self.getCameraType(camera)
        name = self.getNameString(camera)
        if camera_type == 'OrthographicCamera':
            width = self.getWidthString(camera) + ' '
        else:
            width = ''
        position = self.getPositionString(camera)
        upDirection = self.getUpDirectionString(camera)
        lookDirection = self.getLookDirectionString(camera)
        self.writer.write_line('<Viewport3D.Camera>')
        self.writer.write_line(f'<{camera_type} {name} {width}{position} {upDirection} {lookDirection} />', TabChange.Add)
        self.writer.write_line('</Viewport3D.Camera>', TabChange.Remove)

    def getNameString(self, camera):
        return f'x:Name="{camera.name}"'

    def getWidthString(self, camera):
        width = self.getWidth(camera)
        return f'Width="{width:.2f}"'

    def getPositionString(self, camera):
        return self.getMatrixString('Position', self.getPosition(camera))

    def getUpDirectionString(self, camera):
        return self.getMatrixString('UpDirection', self.getUpDirection(camera))

    def getLookDirectionString(self, camera):
        return self.getMatrixString('LookDirection', self.getLookDirection(camera))

    def getMatrixString(self, name, matrix):
        x, y, z = matrix
        return f'{name}="{x:.2f},{y:.2f},{z:.2f}"'
        
    def getCameras(self):
        return [obj for obj in bpy.context.scene.objects if obj.type == 'CAMERA']

    def getCameraType(self, camera):
        camera_type = camera.data.type
        if camera_type == 'PERSP':
            return 'PerspectiveCamera'
        if camera_type == 'ORTHO':
            return 'OrthographicCamera'
        if camera_type == 'PANO':
            return 'PerspectiveCamera'
    
    def getPosition(self, camera):
        x, y, z = camera.location
        return x, y, z
    
    def getUpDirection(self, camera):
        x, y, z = camera.matrix_world.to_quaternion() @ mathutils.Vector((0.0, 1.0, 0.0))
        return x, y, z
    
    def getLookDirection(self, camera):
        x, y, z = -camera.matrix_world.to_quaternion() @ mathutils.Vector((0.0, 0.0, -1.0))
        return x, y, z
    
    def getWidth(self, camera):
        return camera.data.ortho_scale * 2.0