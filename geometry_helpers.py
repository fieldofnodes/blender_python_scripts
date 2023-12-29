##############################################################
# Filename  : geometry_helpers.py
# Author    : Jonathan Miller
# Date      : 20231228
# Aim       : Create a list of functions to assist math 
#           : operations in blender
#           :
#           :
#           :
#           :
##############################################################
from math import pi,sin,cos


def spherical_to_cartesian(initial_position, radial_magnitude, azimuth_angle, zenith_angle):
    """
    Take the position of a point, the radius, and angles
    Returns the new position in x, y, z format
    """
    if len(initial_position) != 3:
        raise Exception("Coordinates need to be length 3 to represent (x, y, z) point in R3.")
        
    x = radial_magnitude * cos(azimuth_angle) * sin(zenith_angle)
    y = radial_magnitude * sin(azimuth_angle) * sin(zenith_angle)
    z = radial_magnitude * cos(zenith_angle)

    x_n = initial_position[0] + x
    y_n = initial_position[1] + y
    z_n = initial_position[2] + z

    return [x_n, y_n, z_n]
