# Tasks

## 0. Squared simple

Write a function that computes the square value of all integers of a matrix.

- Prototype: `def square_matrix_simple(matrix=[]):`
- matrix is a 2 dimensional array
- Returns a new matrix:
  - Same size as matrix
  - Each value should be the square of the value of the input
- Initial matrix should not be modified
- You are not allowed to import any module
- You are allowed to use regular loops, map, etc.

```
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)

guillaume@ubuntu:~/$ ./0-main.py
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
guillaume@ubuntu:~/$ 
```

**Repo:**

- GitHub repository: `alx_python`
- Directory: `python-more_data_structures`
- File: `0-square_matrix_simple.py`

## 1. Present in both

Write a function that returns a set of common elements in two sets.

- Prototype: `def common_elements(set_1, set_2):`
- You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
common_elements = __import__('1-common_elements').common_elements

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))

guillaume@ubuntu:~/$ ./1-main.py
['C']
guillaume@ubuntu:~/$ 
```

**Repo:**

- GitHub repository: `alx_python`
- Directory: `python-more_data_structures`
- File: `1-common_elements.py`

## 2. Update dictionary

Write a function that replaces or adds key/value in a dictionary.

- Prototype: def update_dictionary(a_dictionary, key, value):
- key argument will be always a string
- value argument will be any type
- If a key exists in the dictionary, the value will be replaced
- If a key doesn’t exist in the dictionary, it will be created
- You are not allowed to import any module

```
guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
update_dictionary = __import__('2-update_dictionary').update_dictionary

def print_sorted_dictionary(my_dict):
    """ Print sorted dictionary """
    keys = sorted(my_dict.keys())
    for k in keys:
        print("{}: {}".format(k, my_dict[k]))

a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
new_dict = update_dictionary(a_dictionary, 'language', "Python")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

print("--")
print("--")

new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

guillaume@ubuntu:~/$ ./2-main.py
language: Python
number: 89
track: Low level
--
language: Python
number: 89
track: Low level
--
--
city: San Francisco
language: Python
number: 89
track: Low level
--
city: San Francisco
language: Python
number: 89
track: Low level
guillaume@ubuntu:~/$ 
```

**Repo:**

- GitHub repository: `alx_python`
- Directory: `python-more_data_structures`
- File: `2-update_dictionary.py`
