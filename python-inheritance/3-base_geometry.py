"""
This module defines the base class
"""

class BaseGeometry:
    """
    This is a base class for geometry-related classes
    """
    pass # an empty block

bg = BaseGeometry()
print(repr(bg))
print(sorted(dir(bg)))
print(sorted(dir(BaseGeometry)))