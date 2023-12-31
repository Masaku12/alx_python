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
    
    def display(self):
        """
        Display the Rectangle instance by printing it to stdout using the # character
        
        Returns:
            None
        """
        for _ in range(self.__height):
            print("#" * self.__width)
            
    def __str__(self):
        """
        Return a string representation of the Rectangle instance
        
        Returns:
            str: A string that represents the rectangle instance
        """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id, self.x, self.y, self.width, self.height)
    
    def display(self):
        """
        Displays the Rectangle instance by printing to stdout the # character and takes care of x and y attributes
        
        Returns:
            None
        """
        
        for _ in range(self.__y):
            print()
            
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)
            
    def update(self, *args, **kwargs):
        """
        Updates the Rectangular instance attributes using available arguments.
        
        Args:
            *args: Variable number of arguments
                - if not empty:
                    - 1st argument updates the id attribute
                    - 2nd argument updates the width attribute
                    - 3rd argument updates the height attribute
                    - 4th argument updates the x attribute
                    - 5th argument updates the y attribute
            **kwargs: Variable number of keyword arguments
                - Every key-value pair updates the next attribute of the instance
                
            If both *args and **kwargs are available, **kwargs is avoided
        """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
            else:
                for key, value in kwargs.items():
                    setattr(self, key, value)