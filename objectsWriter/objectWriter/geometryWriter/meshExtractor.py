import bpy

class MeshExtractor:
    def getMesh(self, obj):
        # copy the object so it does not transform original
        obj_copy = obj.copy()
        obj_copy.data = obj.data.copy()
        bpy.context.collection.objects.link(obj_copy)
        # apply modifiers
        self.applyModifiers(obj_copy)
        # get mesh data from obj
        mesh = obj_copy.data
        bpy.data.objects.remove(obj_copy)
        # apply transforms
        if hasattr(mesh, "transform"):
            mb = obj.matrix_world
            mesh.transform(mb)
        return mesh

    def applyModifiers(self, obj):
        bpy.context.view_layer.objects.active = obj
        for modifier in obj.modifiers:
            bpy.ops.object.modifier_apply(modifier=modifier.name)