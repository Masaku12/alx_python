"""
Module: Rectangle

This module defines the Rectangle class, which inherits from the Base class
"""

from models.base import Base

class Rectangle(Base):
    """
    Class Rectangle, inherited from the Base class
    
    Attributes:
        width (int): Rectangle width
        height (int): Rectangle height
        x (int): x-coordinate of the rectangle's position
        y (int): y-coordinate of the rectangle's position
        id (int): The id of the rectangle
        
    Methods:
        __init__(self, width, height, x=0, y=0, id=None): Constructor that initializes a rectangle object
        width (property): Getter and setter methods for the width attribute
        height (property): Getter and setter methods for the height attribute
        x (property): Getter and setter methods for the x attribute
        y (property): Getter and setter methods for the y attribute
    """
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a rectangle object
        
        Args:
            width (int): Rectangle width
            height (int): Rectangle height
            x (int): x-coordinate of the rectangle's position
            y (int): y-coordinate of the rectangle's position
            id (int): The id of the rectangle
            
        Returns:
            None
        """
        super().__init__(id) # Calls the Base class constructor with id
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        
    @property
    def width(self):
        """Getter method for width attribute"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Setter method for width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        
    @property
    def height(self):
        """Getter method for height attribute"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Setter method for height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
        
    @property
    def x(self):
        """Getter method for x attribute"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """Setter method for x attribute"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
        
    @property
    def y(self):
        """Getter method for y attribute"""
        return self.__y
    
    @y.setter
    def y(self, value):
        """Setter method for y attribute"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    
    def area(self):
        """
        Calculates and returns the area of the Rectangle public instance
        
        Returns:
            The area value of the Rectangle instance
        """
        return self.__width * self.__height