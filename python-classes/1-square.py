"""
This module defines the square class
"""

class square:
    """
    This class defines a square by a private instance attribute 'size'
    and provides methods for retrieving and setting the size.
    
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
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    def get_size(self):
        """
        Retrieves the current size of the square.
        
        Returns:
            int: The size of the square.
        """
        return self.__size
    
    def set_size(self, new_size):
        """
        Sets a new size for the square.
        
        Args:
            new_size (int): The new size to set.
            
        Raises:
            TypeError: If new_size is not an integer.
            ValueError: If new_size is less than 0.
        """
        if not isinstance(new_size, int):
            raise TypeError("size must be an integer")
        if new_size < 0:
            raise ValueError("size must be >= 0")
        self.__size = new_size