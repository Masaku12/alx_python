# Tasks

Write a function that adds two integers and returns the result.

- Prototype: `def add(a, b):`
- Returns the value of `a + b`
- You are not allowed to import any module

You don’t need to understand `__import__`

```
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/env python3
add = __import__('0-sum').add

print(add(1, 2))
print(add(98, 0))
print(add(100, -2))

guillaume@ubuntu:~/$ ./0-main.py
3
98
98
guillaume@ubuntu:~/$ 
```

**Repo:**

- GitHub repository: alx_python
- Directory: python-functions
- File: 0-sum.py

