"""
This module defines the base class
"""

class BaseGeometry:
    """
    This is a base class for geometry-related base classes
    """
    def area(self):
        """
        Calculate the area of the geometry
        
        Raises:
            Exception: This method is not implemented
        """
        
        raise Exception("area() is not implemented")

# Create an instance of the class
bg = BaseGeometry()
    
try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))