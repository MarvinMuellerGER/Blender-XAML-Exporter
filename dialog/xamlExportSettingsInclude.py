from bpy.types import Panel

class XamlExportSettingsInclude(Panel):
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'TOOL_PROPS'
    bl_label = "Einschließen"
#   bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        sfile = context.space_data
        operator = sfile.active_operator
        return operator.bl_idname == "EXPORT_OT_xaml"

    def draw(self, context):
        layout = self.layout
        #layout.use_property_split = True
        #layout.use_property_decorate = False  # No animation.

        sfile = context.space_data
        operator = sfile.active_operator

        layout.label(text="Auswahl der zu exportierenden Objekte")
        layout.prop(operator, 'include_only_selected_ones')
        layout.prop(operator, 'include_only_visible_ones')