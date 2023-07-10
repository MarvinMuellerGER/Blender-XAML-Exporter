import bpy

class ObjectsCollector:
    def get_objects_to_export(self, include_only_selected_ones, include_only_visible_ones):
        if include_only_selected_ones and bpy.context.selected_objects:
            objects = bpy.context.selected_objects
        else:
            objects = bpy.context.scene.objects
        
        if include_only_visible_ones:
            return self.get_visible_objects(objects)
        return objects
    
    def get_visible_objects(self, objects):
        for obj in objects:
            if obj.visible_get():
                yield obj
        
    def get_top_level_objects(self, include_only_selected_ones, include_only_visible_ones):
        objects = self.get_objects_to_export(include_only_selected_ones, include_only_visible_ones)
        return [obj for obj in objects if obj.parent is None]