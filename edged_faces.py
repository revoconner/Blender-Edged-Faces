bl_info = {
    "name": "Selected Mesh Edged Faces",
    "author": "Rév",
    "version": (1, 0),
    "blender": (4, 0, 0),
    "location": "Viewport",
    "description": "Automatically toggles wireframe display when selecting/deselecting mesh objects, mimicks 3ds Max edged faces",
    "category": "3D View",
}

import bpy
from bpy.app.handlers import persistent

class WireframeTogglePreferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    def draw(self, context):
        layout = self.layout
        layout.label(text="No additional preferences available.")

@persistent
def selection_change_handler(scene):
    # Get the active object
    active_obj = bpy.context.active_object
    
    # First, turn off wireframe for all mesh objects
    for obj in bpy.data.objects:
        if obj.type == 'MESH':
            obj.show_wire = False
    
    # Then, turn on wireframe for selected mesh objects
    if bpy.context.selected_objects:
        for obj in bpy.context.selected_objects:
            if obj.type == 'MESH':
                obj.show_wire = True

def register():
    bpy.utils.register_class(WireframeTogglePreferences)
    if selection_change_handler in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.remove(selection_change_handler)
    bpy.app.handlers.depsgraph_update_post.append(selection_change_handler)

def unregister():
    bpy.utils.unregister_class(WireframeTogglePreferences)
    if selection_change_handler in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.remove(selection_change_handler)

if __name__ == "__main__":
    register()