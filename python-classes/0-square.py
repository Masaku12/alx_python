class Square:
    """
    This class defines a square by a private instance attribute 'size'.
    
    Attributes:
        __size (int): The size of the square.
    """
    
    def __init__(self, size):
        """
        Initializes a new Square instance with the given size.
        
        Args:
            size (int): The size of the new square.
        """
        self.__size = size
        
    def get_size(self):
        """
        Retrieves the current size of the square.
        
        Returns:
            int: The size of the square
        """
        return self.__size
    
    def set_size(self, new_size):
        """
        Sets a new size for the square.
        
        Args:
            new_size (int): The new size to set.
        """
        self.__size = new_size