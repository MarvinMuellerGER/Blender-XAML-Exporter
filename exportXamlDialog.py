import bpy
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, BoolProperty
from bpy.types import Operator

# Local imports
from .xamlExporter import XamlExporter

# Saves 3 XAML files (one main file, one for geometries and one for materials)
class ExportXamlDialog(Operator, ExportHelper):
    """Speichern von 3 XAML-Dateien (eine Hauptdatei sowie eine für die Geometrien und eine für die Materialien"""
    bl_idname = "export.xaml"
    bl_label = "XAML exportieren"

    filename_ext = ".xaml"

    filter_glob: StringProperty(
        default="*.xaml",
        options={'HIDDEN'},
        maxlen=255,
    )

    include_only_selected_ones: BoolProperty(
        name="Ausgewählte Objekte",
        description="Nur ausgewählte Objekte exportieren.",
        default=False,
    )
    
    include_only_visible_ones: BoolProperty(
        name="Sichtbare Objekte",
        description="Nur sichtbare Objekte exportieren.",
        default=False,
    )
    
    use_scale: BoolProperty(
        name="",
        description="ScaleTransform für dieses Objekt anlegen.",
        default=True,
    )
    
    use_rotate: BoolProperty(
        name="",
        description="RotateTransform für dieses Objekt anlegen.",
        default=True,
    )
    
    use_move: BoolProperty(
        name="",
        description="TranslateTransform für dieses Objekt anlegen.",
        default=True,
    )
    
    def __init__(self):
        self.xamlExporter = XamlExporter()
        self.objects_settings = []

    def execute(self, context):
        filepath = self.filepath
        filepath = bpy.path.ensure_ext(filepath, self.filename_ext)
        exported = self.xamlExporter.export(filepath, self.include_only_selected_ones, self.include_only_visible_ones, self.objects_settings)
        return {'FINISHED'}
    
    def draw(self, context):
        pass
        
# class XamlObjectSetting:
    # use_scale: BoolProperty(
        # name="",
        # description="ScaleTransform für dieses Objekt anlegen.",
        # default=True,
    # )
    
    # use_rotate: BoolProperty(
        # name="",
        # description="RotateTransform für dieses Objekt anlegen.",
        # default=True,
    # )
    
    # use_move: BoolProperty(
        # name="",
        # description="TranslateTransform für dieses Objekt anlegen.",
        # default=True,
    # )