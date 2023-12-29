import bpy

bpy.ops.mesh.primitive_ico_sphere_add(radius=1, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

bpy.ops.object.empty_add(type='SPHERE', align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))


bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(0, 0, 0), rotation=(1.07687, 1.51294e-07, -0.0209395), scale=(1, 1, 1))

bpy.context.space_data.context = 'DATA'
bpy.context.space_data.context = 'CONSTRAINT'
bpy.ops.object.constraint_add(type='TRACK_TO')
bpy.context.object.constraints["Track To"].name = "Track To"
bpy.context.object.constraints["Track To"].target = bpy.data.objects["Empty"]

bpy.context.object.constraints["Track To"].target = bpy.data.objects["Empty"]




# Get references to the camera and curve objects
camera_obj = bpy.data.objects['Camera']  # Replace 'Camera' with your camera's name
curve_obj = bpy.data.objects['BezierCircle']  # Replace 'BezierCurve' with your curve's name

# Create a Follow Path constraint for the camera
constraint = camera_obj.constraints.new('FOLLOW_PATH')
constraint.target = curve_obj
constraint.use_curve_follow = True

# Set the offset factor to start the camera at the beginning of the curve
constraint.offset_factor = 0.0

# Animate the offset factor to move the camera along the curve
bpy.context.scene.frame_start = 1
bpy.context.scene.frame_end = 250  # Adjust the end frame as needed

# Add a keyframe for the offset factor at frame 1
constraint.offset_factor = 0.0
constraint.keyframe_insert("offset_factor",frame=1)  # index=0 for X location

# Add a keyframe for the offset factor at the end frame
constraint.offset_factor = 1.0
constraint.keyframe_insert("offset_factor", frame=bpy.context.scene.frame_end)

camera_obj.animation_data_create()
# Optional: Set the interpolation to linear for constant speed
for fcurve in camera_obj.animation_data.action.fcurves:
    for keyframe_point in fcurve.keyframe_points:
        keyframe_point.interpolation = 'LINEAR'
