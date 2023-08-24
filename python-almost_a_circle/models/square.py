"""
Module: Square, which inherits from the Rectangle class
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Class Square, which inherits from Rectangle class
    
    Attributes:
        size: The size of the Square
        x: The x-coordinate in the Square
        y: The y-coordinate in the Square
        id: The id of the square
        
    Methods:
        __init__(self, size, x=0, y=0, id=None): A constructor that initializes a Squrare object
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square object
        
        Args:
            size: The size of the square
            x: The x-coordinate of the square
            y: The y-coordinate of the square
            id: The id of the square
            
        Returns:
            None
        """
        super().__init__(size, size, x, y, id)
        self.size = size
        
    @property
    def size(self):
        """Getter method for the size attribute"""
        return self.width
    
    @size.setter
    def size(self, value):
        """Setter method for the size attribute"""
        self.width = value
        self.height = value
        
    def __str__(self):
        """
        Return a string(str) that represents the Square instance
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x, self.y, self.size)