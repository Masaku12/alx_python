"""
This module defines the base class
"""

class BaseGeometry:
    """
    This base class contains geometry-related classes
    """
    
    def area(self):
        """
        Calculates the area of the provided geometry
        
        Raises:
            Exception: This method is not implemented
        """
        
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