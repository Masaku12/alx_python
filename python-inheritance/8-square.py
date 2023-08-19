"""
Module: GeometryModule
"""

class BaseGeometry:
    """
    Base class for geometry-related classes
    """
    def area(self):
        """
        Calculate the area of the geometry
        
        Raises:
            Exception: This method is not implemented
        """
        
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate an integer value
        
        Args:
            name: The name of the value being validated
            value: The value to be validated
            
        Raises:
            TypeError: If the value is not an integer
            ValueError: If the value is less than or equal to 0
        """
        
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """
    Rectangle class, inheriting from BaseGeometry
    """
    
    def __init__(self, width, height):
        """
        Initialize a Rectangle instance with width and height
        
        Args:
            width: The width of the rectangle
            height: The height of the rectangle
        """
        
        self.__width = 0  # Initialize to 0 for now
        self.__height = 0  # Initialize to 0 for now
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate the area of the rectangle
        
        Returns:
            int: The area of the rectangle
        """
        
        return self.__width * self.__height

    def __str__(self):
        """
        Get a string representation of the rectangle
        
        Returns:
            str: A formatted string describing the rectangle
        """
        
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

class Square(Rectangle):
    """
    Square class, inheriting from Rectangle
    """
    
    def __init__(self, size):
        """
        Initialize a Square instance with size
        
        Args:
            size: The size of the square
        """
        
        self.__size = 0  # Initialize to 0 for now
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculate the area of the square.
        
        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
