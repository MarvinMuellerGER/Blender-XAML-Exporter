import bpy
from bpy.types import Panel

class XamlExportSettingsTransform(Panel):
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'TOOL_PROPS'
    bl_label = "Transformieren"
    bl_options = {'DEFAULT_CLOSED'}
    
    @classmethod
    def poll(cls, context):
        sfile = context.space_data
        operator = sfile.active_operator
        return operator.bl_idname == "EXPORT_OT_xaml"

    def draw(self, context):
        layout = self.layout
        
        sfile = context.space_data
        operator = sfile.active_operator

        # Get all objects in the scene
        objects = bpy.context.scene.objects
        
        # Create a table
        # Split the layout into 4 columns
        row = layout.row()
        split = row.split(factor=0.25)
        # First column
        col1 = split.column()
        col1.label(text="Objekt")
        # Second column
        split = split.split(factor=0.333)
        col2 = split.column()
        col2.label(text="Skalieren")
        # Third column
        split = split.split(factor=0.5)
        col3 = split.column()
        col3.label(text="Rotieren")
        # Fourth column
        split = split.split(factor=0.667)
        col4 = split.column()
        col4.label(text="Bewegen")

        # Create a row for each object
        for obj in objects:
            col1.row().label(text=obj.name)
            col2.row().prop(operator, 'use_scale')
            col3.row().prop(operator, 'use_rotate')
            col4.row().prop(operator, 'use_move')