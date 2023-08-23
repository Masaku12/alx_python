"""
base_module: Defines the base class, which will manage id attributes in child classes
"""

class Base:
    """
    Manages id attributes in subclasses
    
    Attributes:
        __nb_objects: A private class that records created number of instances
        
    Methods:
        __init__(self, id=None): Constructor that initializes the id attribute
    """
    __nb_objects = 0 # private class attribute
    
    def __init__(self, id=None):
        """
        Initialized the id attribute based on provided id or incremented __nb_objects
        
        Args:
            id: The value assigned to the id attribute
            
        Returns:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects