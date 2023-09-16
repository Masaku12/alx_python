# Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General

- What is a Web Framework
- How to build a web framework with Flask
- How to define routes in Flask
- What is a route
- How to handle variables in a route
- What is a template
- How to create a HTML response in Flask by using a template
- How to create a dynamic template (loops, conditions…)
- How to display in HTML data from a MySQL database

# Requirements

## Python Scripts

- Recommended editors: Visual studio code
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7)
- The length of your files will be tested using wc
- All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## HTML/CSS Files

- Recommended editors: Visual studio code
- All your files should end with a new line
- A README.md file at the root of the folder of the project is mandatory
- Your code should be W3C compliant and validate with W3C-Validator (except for jinja template)
- All your CSS files should be in the styles folder
- All your images should be in the images folder
- You are not allowed to use !important or id (#... in the CSS file)
- All tags must be in uppercase
- Current screenshots have been done on Chrome 56.0.2924.87.
- No cross browsers

## Install flask
```$ pip3 install Flask```

# Tasks

## 0. Hello Flask!

Write a script that starts a Flask web application:

- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
  - /: display “Hello HBNB!”
- You must use the option strict_slashes=False in your route definition

```guillaume@ubuntu:~/AirBnB_v2$ python3 0-hello_route.py
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```

in another tab

```guillaume@ubuntu:~$ curl 0.0.0.0:5000 ; echo "" | cat -e
Hello HBNB!$
guillaume@ubuntu:~$
```

**Repo:**

- GitHub repository: `alx_python`
- Directory: `python-web_framework`
- File: `0-hello_route.py`
