import os
import bpy

class NamesCollector:
    def __init__(self):
        self.setNameExtensions('1', 'Group', 'Geometry', 'Material')
        self.charactarsToRemove = [' ', '.', '_']
        
    def setNameExtensions(self, nestedObjectName, groupNameExtension, geometryNameExtension, materialNameExtension):
        self.setNestedObjectNameExtension(nestedObjectName)
        self.setGroupNameExtension(groupNameExtension)
        self.setGeometryNameExtension(geometryNameExtension)
        self.setMaterialNameExtension(materialNameExtension)
    
    def setNestedObjectNameExtension(self, extensionString):
        self.nestedObject_nameExtension = extensionString
        
    def setGroupNameExtension(self, extensionString):
        self.group_nameExtension = extensionString
        
    def setGeometryNameExtension(self, extensionString):
        self.geometry_nameExtension = extensionString
        
    def setMaterialNameExtension(self, extensionString):
        self.material_nameExtension = extensionString
        
    def getObjectName(self, obj):
        objName = obj.name
        for charactar in self.charactarsToRemove:
            objName = objName.replace(charactar, '')
        return objName
        
    def getNestedObjectName(self, obj):
        objName = self.getObjectName(obj)
        return f'{objName}{self.nestedObject_nameExtension}'
    
    def getGroupName(self, obj):
        objName = self.getObjectName(obj)
        return f'{objName}{self.group_nameExtension}'
    
    def getGeometryName(self, obj):
        objName = self.getObjectName(obj)
        return f'{objName}{self.geometry_nameExtension}'
    
    def getMaterialName(self, obj):
        objName = self.getObjectName(obj)
        return f'{objName}{self.material_nameExtension}'
    
    def getProjectName(self):
        project_name = f'{os.path.splitext(os.path.basename(bpy.data.filepath))[0]}'
        if project_name is '':
            project_name = 'Untitled'
        return project_name