##############################################################
# Filename  : filename.py
# Author    : author
# Date      : date
# Aim       : script aim
#           :
#           :
#           :
#           :
#           :
##############################################################
import bpy
import os
import sys
home_directory = os.path.expanduser("~")
helper_script_directory = "Projects/blender_projects"
helper_path = os.path.join(home_directory, helper_script_directory)
sys.path.append(os.path.abspath(helper_path))

# Import file to reset session
import reset_script_work

# Function to reset work all loaded items in sessio
reset_script_work.reset_current_script()