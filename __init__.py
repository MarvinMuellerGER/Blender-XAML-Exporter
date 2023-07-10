bl_info = {
    "name": "XAML format (.xaml)",
    "author": "Marvin Mueller",
    "version": (0, 1, 0),
    "blender": (3, 4, 0),
    "location": "File > Export > XAML",
    "description": "Export scene or object(s) to XAML",
    "warning": "",
    "wiki_url": "",
    "category": "Import-Export"}


##########################################
# REGISTER
##########################################

import bpy

# Local imports
from .dialog.exportXamlDialog import ExportXamlDialog
from .dialog.xamlExportSettingsInclude import XamlExportSettingsInclude
from .dialog.xamlExportSettingsTransform import XamlExportSettingsTransform

def menu_func_export(self, context):
    self.layout.operator(ExportXamlDialog.bl_idname, text="XAML Viewport3D (.xaml)")

def register():
    bpy.utils.register_class(ExportXamlDialog)
    bpy.utils.register_class(XamlExportSettingsInclude)
    bpy.utils.register_class(XamlExportSettingsTransform)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)

def unregister():
    bpy.utils.unregister_class(XamlExportSettingsTransform)
    bpy.utils.unregister_class(XamlExportSettingsInclude)
    bpy.utils.unregister_class(ExportXamlDialog)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)

if __name__ == "__main__":
    register()