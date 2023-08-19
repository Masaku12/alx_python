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
    def __init__(self, width, height):
        """
        Initializes a rectangle instance with width and height
        
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
        
    def area(self):
        """
        Calculate area of the rectangle
        
        Returns:
            int: Area of the rectangle
        """
        
        return self.__width * self.__height
    
    def __str__(self):
        """
        Obtain a string that represents the rectangle
        
        Returns:
            str: a formated string
        """
        
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
        
class Square(Rectangle):
    """
    A square class that inherits from the Rectangle class
    """
    
    def __init__(self, size):
        """
        Initialize a square instance with size
        
        Args:
            size: The size of the square
        """
        
        self.__size = 0 # Initialized to 0
        self.integer.validator("size", size)
        self.__size = size
        super().__init(size, size)
        
    def area(self):
        """
        Calculate the area of the square
        
        Returns:
            int: The area of the square
        """
        
        return self.__size * self.__size