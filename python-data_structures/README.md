# Tasks

## 0. Can you C me now?

Write a function that removes all characters c and C from a string.

- Prototype: `def no_c(my_string):`
- The function should return the new string
- You are not allowed to import any module
- You are not allowed to use `str.replace()`

```
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/env python3
no_c = __import__('0-no_c').no_c

print(no_c("Holberton School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))

guillaume@ubuntu:~/$ ./0-main.py
Holberton Shool
hiago
 is fun!
guillaume@ubuntu:~/$ 
```

**Repo:**

- GitHub repository: `alx_python`
- Directory: `python-data_structures`
- File: `0-no_c.py`

## 1. Lists of lists = Matrix

Write a function that prints a matrix of integers.

- Prototype: `def print_matrix_integer(matrix=[[]]):`
- Format: see example
- You are not allowed to import any module
- You can assume that the list only contains integers
- You are not allowed to cast integers into strings
- You have to use `str.format()` to print integers

```
guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
print_matrix_integer = __import__('1-print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()

guillaume@ubuntu:~/$ ./1-main.py | cat -e
1 2 3$
4 5 6$
7 8 9$
--$
$
guillaume@ubuntu:~/$ 
```

**Repo:**

- GitHub repository: `alx_python`
- Directory: `python-data_structures`
- File: `1-print_matrix_integer.py`

## 2. More returns!

Write a function that returns a tuple with the length of a string and its first character.

- Prototype: `def multiple_returns(sentence):`
- If the sentence is empty, the first character should be equal to None
- You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
multiple_returns = __import__('2-multiple_returns').multiple_returns

sentence = "At Holberton school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))

guillaume@ubuntu:~/$ ./2-main.py
Length: 32 - First character: A
guillaume@ubuntu:~/$ 
```

**Repo:**

- GitHub repository: `alx_python`
- Directory: `python-data_structures`
- File: `2-multiple_returns.py`