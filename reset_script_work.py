###############################################################################################
# Filename  : reset_script_work.py
# Author    : author
# Date      : date
# Aim       : script aim
#           :
#           :
#           :
#           :
#           :
###############################################################################################
import bpy
def reset_current_script():
    # Deselect all objects
    bpy.ops.object.select_all(action='DESELECT')

    # Select and remove all objects
    for obj in bpy.data.objects:
        bpy.data.objects.remove(obj, do_unlink=True)

    # Optionally, remove meshes, curves, etc.
    for mesh in bpy.data.meshes:
        bpy.data.meshes.remove(mesh)

    for curve in bpy.data.curves:
        bpy.data.curves.remove(curve)

    # Optionally, remove materials, textures, etc.
    for material in bpy.data.materials:
        bpy.data.materials.remove(material)

    for texture in bpy.data.textures:
        bpy.data.textures.remove(texture)
