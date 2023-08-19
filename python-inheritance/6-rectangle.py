"""
This module defines the base class
"""

class BaseGeometry:
    """
    This is a base class for all geometry related classes
    """
    
    def area(self):
        """
        Calculates the area of the provided geometry
        
        Raises:
            Exception: This method is not implemented
        """
        
        raise Exception("Area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        Validates an integer value
        
        Args:
            name: The name of the value being validated
            value: The value being validated
            
        Raises:
            TypeError: If value is not an int
            ValueError: If value is <= 0
        """
        
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        
class Rectangle(BaseGeometry):
    """
    Rectangle class being inherited from class BaseGeometry
    
    Args:
        width: The width of the rectangle
        height: The height of the rectangle
    """
    
    self.__width = 0 # initialized to 0
    self.__height = 0 # initialized to 0
    self.integer_validator("width", width)
    self.integer_validator("height", height)
    self.__width = width
    self.__height = height