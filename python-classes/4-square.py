"""
This module defines a class square
"""

class Square:
    """
    This class defines a square by a private instance attribute 'size' and provides methods
    for retrieving the size, calculating the area, and printing the square pattern.
    
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
        self.size = size
        
    @property
    def size(self):
        """
        Retrieves the current size of the square.
        
        Returns:
            int: The size of the square.
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """
        Sets the size of the square.
        
        Args:
            value (int): The new size to set.
        
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        
    def area(self):
        """
        Calculates and returns the current square area.
        
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
    
    def my_print(self):
        """
        Prints the square pattern using '#'.
        """
        if self.__size == 0:
            print()
            return
        
        for _ in range(self.__size):
            print("#" * self.__size)
