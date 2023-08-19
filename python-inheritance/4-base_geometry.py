"""
This module defines the base class
"""

class BaseGeometry:
    """
    This is a base class for geometry-related base classes
    """
    def area(self):
        """
        Calculate the area of the geometry and raise an exception
        """
        raise Exception("area() is not implemented")