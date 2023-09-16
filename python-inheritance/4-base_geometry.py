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
    
# Create an instance of BaseGeometry
bg = BaseGeometry()

# Filter the dir(bg) result to exclude unwanted attributes
filtered_dir = [item for item in dir(bg) if not item.startswith('__')]

# Print the filtered item
print(filtered_dir)