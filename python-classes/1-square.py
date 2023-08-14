"""
This module defines the square class
"""

class square:
    """
    This class defines a square by a private instance attribute 'size' and provides methods for retrieving and setting the size.
    
    Attributes:
        __size (int): The size of the square.
    """
    
    def __init__(self, size=0):
        """
        Initializes a new Square instance with the given size.
    
        Args:
        size (int, optional): The size of the square. Defaults to 0.
        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        