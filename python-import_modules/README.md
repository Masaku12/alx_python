# Tasks

## 0. Import a simple function from a simple file

Write a program that imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`

- You have to use `print` function with string format to display integers
- You have to assign:
  - the value `1` to a variable called `a`
  - the value `2` to a variable called `b`
  - and use those two variables as arguments when calling the functions `add` and `print`
- `a` and `b` must be defined in 2 different lines: `a = 1` and another `b = 2`
- Your program should print: `<a value> + <b value> = <add(a, b) value>` followed with a new line
- You can only use the word `add_0` once in your code
- You are not allowed to use `*` for importing or `__import__`
- Your code should not be executed when imported - by using `__import__`, like the example below

```
guillaume@ubuntu:~/$ cat add_0.py
#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)

guillaume@ubuntu:~/$ ./0-add.py
1 + 2 = 3
guillaume@ubuntu:~/$ cat 0-import_add.py
__import__("0-add")
guillaume@ubuntu:~/$ python3 0-import_add.py 
guillaume@ubuntu:~/$ 
```

**Repo:**

- GitHub repository: `alx_python`
- Directory: `python-import_modules`
- File: `0-add.py`

## 1. How to make a script dynamic!

Write a program that prints the number of and the list of its arguments.

- The output should be:
  - Number of argument(s) followed by argument (if number is one) or arguments (otherwise), followed by
  - : (or . if no arguments were passed) followed by
  - a new line, followed by (if at least one argument),
  - one line per argument:
    - the position of the argument (starting at 1) followed by :, followed by the argument value and a new line
- Your code should not be executed when imported
- The number of elements of argv can be retrieved by using: len(argv)
- You do not have to fully understand lists yet, but imagine that argv can be used just like a C array: you can use an index to walk through it. There are other ways (which will be preferred for future project tasks), if you know them you can use them.

```
guillaume@ubuntu:~/$ ./1-args.py 
0 arguments.
guillaume@ubuntu:~/$ ./1-args.py Hello
1 argument:
1: Hello
guillaume@ubuntu:~/$ ./1-args.py Hello Holberton School 98 Battery street
6 arguments:
1: Hello
2: Holberton
3: School
4: 98
5: Battery
6: street
guillaume@ubuntu:~/$ 
```

**Repo:**

- GitHub repository: `alx_python`
- Directory: `python-import_modules`
- File: `1-args.py`

## 2. Everything can be imported

Write a program that imports the variable a from the file variable_load_2.py and prints its value.

- You are not allowed to use * for importing or `__import__`
- Your code should not be executed when imported

```
guillaume@ubuntu:~/$ cat variable_load_2.py
#!/usr/bin/python3
a = 98
"""Simple variable
"""

guillaume@ubuntu:~/$ ./2-variable_load.py
98
guillaume@ubuntu:~/$
```

**Repo:**

- GitHub repository: `alx_python`
- Directory: `python-import_modules`
- File: `2-variable_load.py`
