# Background Context

The AirBnB project is a big part of the Higher level curriculum. This project will help you be ready for it.

In this project, you will review everything about Python:

- Import
- Exceptions
- Class
- Private attribute
- Getter/Setter
- Class method
- Static method
- Inheritance
- Unittest
- Read/Write file

You will also learn about:

- args and kwargs
- Serialization/Deserialization
- JSON

## Tasks

### 0. Base class

Write the first class `Base:`

Create a folder named models with an empty file `__init__.py` inside - with this file, the folder will become a Python package

Create a file named `models/base.py:`

- Class Base:
  - private class attribute `__nb_objects = 0`
  - class constructor: `def __init__(self, id=None):`:
    - if id is not None, assign the public instance attribute id with this argument value - you can assume id is an integer and you don’t need to test the type of it
    - otherwise, `increment __nb_objects` and assign the new value to the public instance attribute id

This class will be the “base” of all other classes in this project. The goal of it is to manage id attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)

```
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
""" 0-main """
from models.base import Base

if __name__ == "__main__":

    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)

guillaume@ubuntu:~/$ ./0-main.py
1
2
3
12
4
guillaume@ubuntu:~/$ 
```

**Repo:**

- GitHub repository: `alx_python`
- Directory: `python-almost_a_circle`
- File: `models/base.py`, `models/__init__.py`

### 1. First Rectangle

Write the class `Rectangle` that inherits from `Base`:

- In the file models/rectangle.py
- Class Rectangle inherits from Base
- Private instance attributes, each with its own public getter and setter:
  - `__width` -> `width`
  - `__height` -> `height`
  - `__x` -> `x`
  - `__y` -> `y`
- Class constructor: `def __init__(self, width, height, x=0, y=0, id=None)`:
  - Call the super class with id - this super call with use the logic of the `__init__` of the Base class
  - Assign each argument width, height, x and y to the right attribute
Why private attributes with getter/setter? Why not directly public attribute?

Because we want to protect attributes of our class. With a setter, you are able to validate what a developer is trying to assign to a variable. So after, in your class you can “trust” these attributes.

```
guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)

guillaume@ubuntu:~/$ ./1-main.py
1
2
12
guillaume@ubuntu:~/$ 
```

**Repo:**

- GitHub repository: `alx_python`
- Directory: `python-almost_a_circle`
- File: `models/rectangle.py`

