"""
This module provides a function that checks if an object is an instance or inherited
"""

def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited (directly or indirectly)
    from the specified class.
    
    Args:
        obj: The object to be checked.
        a_class: The class to compare against.
        
    Returns:
        True if obj is an instance of a subclass of a_class, otherwise False.
    """
    return issubclass(type(obj), a_class)