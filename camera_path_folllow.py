import os
import sys
script_directory = "/Users/jmille15/Projects/blender_projects"
sys.path.append(os.path.abspath(script_directory))

# Function to reset work all loaded items in session
import reset_script_work

import bpy

reset_script_work.reset_current_script()

# Add a camera
bpy.ops.object.camera_add(location=(0, -10, 0), rotation=(1.5708, 0, 0))
camera = bpy.context.active_object



# Add a Bezier circle
bpy.ops.curve.primitive_bezier_circle_add(radius=5, location=(0, 0, 0))
path = bpy.context.active_object


# Add Follow Path constraint to the camera
constraint = camera.constraints.new(type='FOLLOW_PATH')
constraint.target = path
constraint.use_fixed_location = True
constraint.use_curve_follow = True
constraint.forward_axis = 'FORWARD_X'

# Animate the camera along the path
bpy.context.scene.frame_start = 1
bpy.context.scene.frame_end = 100
bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')


# Add a UV sphere to the scene
bpy.ops.mesh.primitive_uv_sphere_add(radius=1.0, location=(0, 0, 0))


# Set interpolation to linear for constant speed
for fcurve in bpy.data.cameras["Camera"].animation_data.action.fcurves:
    for keyframe_point in fcurve.keyframe_points:
        keyframe_point.interpolation = 'LINEAR'
