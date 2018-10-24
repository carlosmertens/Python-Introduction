""" Cylinder volume.

The volume of a cylinder is calculated by multiplying its height by the square of its radius
    and by pi
"""


def cylinder_volume(height, radius):
    """ Function to calculate the volume of the cylinder

    """
    pi = 3.14159
    return height * pi * (radius ** 2)


# Get values and storage into variables
cylinder_height = int(input("Cylinder's height: "))
cylinder_radius = int(input("Cylinder's radius: "))

# Call the function
volume = cylinder_volume(cylinder_height, cylinder_radius)

# Display the result

print(volume)
