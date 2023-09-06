# Before you start…

Please make sure your MySQL server is in 5.7 -> [How to install MySQL 5.7 in Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-14-04)

## Background Context

In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module `MySQLdb` to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module `SQLAlchemy` (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

Without ORM:

```conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```

With an ORM:

```engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```

Do you see the difference? Cool, right?

The biggest difficulty with ORM is: The syntax!

Indeed, all of them have the same type of syntax, but not always. Please read tutorials and don’t read the entire documentation before starting, just jump on it if you don’t get something.

## Tasks

### 0. Get all states

Write a script that lists all `states` from the database `hbtn_0e_0_usa`:

- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation needed)
- You must use the module `MySQLdb` (`import MySQLdb`)
- Your script should connect to a MySQL server running on `localhost` at `port 3306`
- Results must be sorted in ascending order by `states.id`
- Results must be displayed as they are in the example below
- Your code should not be executed when imported

```guillaume@ubuntu:~/$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/$ python3 0-select_states.py root root hbtn_0e_0_usa
(1, 'California')
(2, 'Arizona')
(3, 'Texas')
(4, 'New York')
(5, 'Nevada')
guillaume@ubuntu:~/$
```

**Click here to show/hide hint**
To be able to solve this task correctly, you will need to know how to use command line arguments in python and also you would have to pay particular attention to how the results is to be printed out.
The example given above can help you to get it right. To follow the example and test your code locally:

You need to locally execute the SQL script (`0-select_states.sql`) whose content was given in the example
After fetching the results from the database, you will need to figure out how to arrange them like it has been shown in the example above

**Repo:**

- GitHub repository: `alx_python`
- Directory: `python-object_relational_mapping`
- File: `0-select_states.py`

### 1. Filter states

Write a script that lists all states with a name starting with N (upper N) from the database `hbtn_0e_0_usa`:

- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation needed)
- You must use the module `MySQLdb` (`import MySQLdb`)
- Your script should connect to a MySQL server running on `localhost` at `port 3306`
- Results must be sorted in ascending order by `states.id`
- Results must be displayed as they are in the example below
- Your code should not be executed when imported

```guillaume@ubuntu:~/$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/$ ./1-filter_states.py root root hbtn_0e_0_usa
(4, 'New York')
(5, 'Nevada')
guillaume@ubuntu:~/$
```

**Repo:**

- GitHub repository: `alx_python`
- Directory: `python-object_relational_mapping`
- File: `1-filter_states.py`

### 2. Filter states by user input

Write a script that takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument.

- Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name searched` (no argument validation needed)
- You must use the module `MySQLdb` (`import MySQLdb`)
- Your script should connect to a MySQL server running on `localhost` at `port 3306`
- You must use `format` to create the SQL query with the user input
- Results must be sorted in ascending order by `states.id`
- Results must be displayed as they are in the example below
- Your code should not be executed when imported

```guillaume@ubuntu:~/$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/$ ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
guillaume@ubuntu:~/$
```

**Repo:**

- GitHub repository: `alx_python`
- Directory: `python-object_relational_mapping`
- File: `2-my_filter_states.py`

### 3. SQL Injection

Wait, do you remember the previous task? Did you test `"Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"` as an input?

```guillaume@ubuntu:~/$ ./2-my_filter_states.py root root hbtn_0e_0_usa "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"
(2, 'Arizona')
guillaume@ubuntu:~/$ ./0-select_states.py root root hbtn_0e_0_usa
guillaume@ubuntu:~/$
```

What? Empty?

Yes, it’s an [SQL injection](https://en.wikipedia.org/wiki/SQL_injection) to delete all records of a table…

Once again, write a script that takes in arguments and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument. But this time, write one that is safe from MySQL injections!

- Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name` searched (safe from MySQL injection)
- You must use the module `MySQLdb` (`import MySQLdb`)
- Your script should connect to a MySQL server running on `localhost` at `port 3306`
- Results must be sorted in ascending order by `states.id`
- Results must be displayed as they are in the example below
- Your code should not be executed when imported

```guillaume@ubuntu:~/$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/$ ./3-my_safe_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
guillaume@ubuntu:~/$
```

No test cases needed

**Click here to show/hide hint**
To be able to solve this task correctly, you will need to understand how to use parameterized query in SQL while using MySQLdb.
Check out the example under MySQLdb in the [documentation here](https://mysqlclient.readthedocs.io/user_guide.html)

**Repo:**

- GitHub repository: `alx_python`
- Directory: `python-object_relational_mapping`
- File: `3-my_safe_filter_states.py`

### 4. Cities by states

Write a script that lists all cities from the database `hbtn_0e_4_usa`

- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
- You must use the module `MySQLdb` (`import MySQLdb`)
- Your script should connect to a MySQL server running on `localhost` at `port 3306`
- Results must be sorted in ascending order by `cities.id`
- You can use only `execute()` once
- Results must be displayed as they are in the example below
- Your code should not be executed when imported

```guillaume@ubuntu:~/$ cat 4-cities_by_state.sql
-- Create states table in hbtn_0e_4_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_4_usa;
USE hbtn_0e_4_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), (1, "Fremont"), (1, "Livermore");
INSERT INTO cities (state_id, name) VALUES (2, "Page"), (2, "Phoenix");
INSERT INTO cities (state_id, name) VALUES (3, "Dallas"), (3, "Houston"), (3, "Austin");
INSERT INTO cities (state_id, name) VALUES (4, "New York");
INSERT INTO cities (state_id, name) VALUES (5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");

guillaume@ubuntu:~/$ cat 4-cities_by_state.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/$ ./4-cities_by_state.py root root hbtn_0e_4_usa
(1, 'San Francisco', 'California')
(2, 'San Jose', 'California')
(3, 'Los Angeles', 'California')
(4, 'Fremont', 'California')
(5, 'Livermore', 'California')
(6, 'Page', 'Arizona')
(7, 'Phoenix', 'Arizona')
(8, 'Dallas', 'Texas')
(9, 'Houston', 'Texas')
(10, 'Austin', 'Texas')
(11, 'New York', 'New York')
(12, 'Las Vegas', 'Nevada')
(13, 'Reno', 'Nevada')
(14, 'Henderson', 'Nevada')
(15, 'Carson City', 'Nevada')
guillaume@ubuntu:~/$
```

No test cases needed

**Repo:**

- GitHub repository: `alx_python`
- Directory: `python-object_relational_mapping`
- File: `4-cities_by_state.py`

### 5. All cities by state

Write a script that takes in the name of a state as an argument and lists all `cities` of that state, using the database `hbtn_0e_4_usa`

- Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name` (SQL injection free!)
- You must use the module `MySQLdb` (`import MySQLdb`)
- Your script should connect to a MySQL server running on `localhost` at `port 3306`
- Results must be sorted in ascending order by `cities.id`
- You can use only `execute()` once
- The results must be displayed as they are in the example below
- Your code should not be executed when imported

```guillaume@ubuntu:~/$ cat 4-cities_by_state.sql
-- Create states table in hbtn_0e_4_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_4_usa;
USE hbtn_0e_4_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), (1, "Fremont"), (1, "Livermore");
INSERT INTO cities (state_id, name) VALUES (2, "Page"), (2, "Phoenix");
INSERT INTO cities (state_id, name) VALUES (3, "Dallas"), (3, "Houston"), (3, "Austin");
INSERT INTO cities (state_id, name) VALUES (4, "New York");
INSERT INTO cities (state_id, name) VALUES (5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");

guillaume@ubuntu:~/$ ./5-filter_cities.py root root hbtn_0e_4_usa Texas

guillaume@ubuntu:~/$ cat 4-cities_by_state.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/$ ./5-filter_cities.py root root hbtn_0e_4_usa Texas
Dallas, Houston, Austin
guillaume@ubuntu:~/$ ./5-filter_cities.py root root hbtn_0e_4_usa Hawaii

guillaume@ubuntu:~/$
```

No test cases needed

**Repo:**

- GitHub repository: `alx_python`
- Directory: `python-object_relational_mapping`
- File: `5-filter_cities.py`

### 6. First state model

Write a python file that contains the class definition of a `State` and an instance `Base = declarative_base()`:

- `State` class:
  - inherits from `Base` [Tips](https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/basic_use.html)
  - links to the MySQL table `states`
  - class attribute `id` that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
  - class attribute `name` that represents a column of a string with maximum 128 characters and can’t be null
- You must use the module `SQLAlchemy`
- Your script should connect to a MySQL server running on `localhost` at `port 3306`
- **WARNING:** all classes who inherit from `Base` must be imported before calling `Base.metadata.create_all(engine)`

```guillaume@ubuntu:~/$ cat 6-model_state.sql
-- Create database hbtn_0e_6_usa
CREATE DATABASE IF NOT EXISTS hbtn_0e_6_usa;
USE hbtn_0e_6_usa;
SHOW CREATE TABLE states;

guillaume@ubuntu:~/$ cat 6-model_state.sql | mysql -uroot -p
Enter password: 
ERROR 1146 (42S02) at line 4: Table 'hbtn_0e_6_usa.states' doesn't exist
guillaume@ubuntu:~/$ cat 6-model_state.py
#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

guillaume@ubuntu:~/$ ./6-model_state.py root root hbtn_0e_6_usa
guillaume@ubuntu:~/$ cat 6-model_state.sql | mysql -uroot -p
Enter password: 
Table   Create Table
states  CREATE TABLE `states` (\n  `id` int(11) NOT NULL AUTO_INCREMENT,\n  `name` varchar(128) NOT NULL,\n  PRIMARY KEY (`id`)\n) ENGINE=InnoDB DEFAULT CHARSET=latin1
guillaume@ubuntu:~/$
```

No test cases needed

**Repo:**

- GitHub repository: `alx_python`
- Directory: `python-object_relational_mapping`
- File: `model_state.py`

### 7. All states via SQLAlchemy

Write a script that lists all `State` objects from the database `hbtn_0e_6_usa`

- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
- You must use the module `SQLAlchemy`
- You must import `State` and `Base from model_state` - from `model_state import Base`, `State`
- Your script should connect to a MySQL server running on `localhost` at `port 3306`
- Results must be sorted in ascending order by `states.id`
- The results must be displayed as they are in the example below
- Your code should not be executed when imported

```guillaume@ubuntu:~/$ cat 7-model_state_fetch_all.sql
-- Insert states
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/$ cat 7-model_state_fetch_all.sql | mysql -uroot -p hbtn_0e_6_usa
Enter password: 
guillaume@ubuntu:~/$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
guillaume@ubuntu:~/$
```

No test cases needed

**Repo:**

- GitHub repository: `alx_python`
- Directory: `python-object_relational_mapping`
- File: `7-model_state_fetch_all.py`

### 8. First state

Write a script that prints the first `State` object from the database `hbtn_0e_6_usa`

- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
- You must use the module `SQLAlchemy`
- You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
- Your script should connect to a MySQL server running on `localhost` at `port 3306`
- The state you display must be the first in `states.id`
- You are not allowed to fetch all states from the database before displaying the result
- The results must be displayed as they are in the example below
- If the table `states` is empty, print `Nothing` followed by a new line
- Your code should not be executed when imported

```guillaume@ubuntu:~/$ ./8-model_state_fetch_first.py root root hbtn_0e_6_usa
1: California
guillaume@ubuntu:~/$
```

No test cases needed

**Repo:**

- GitHub repository: `alx_python`
- Directory: `python-object_relational_mapping`
- File: `8-model_state_fetch_first.py`

### 9. Contains `a`

Write a script that lists all `State` objects that contain the letter a from the database `hbtn_0e_6_usa`

- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
- You must use the module `SQLAlchemy`
- You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
- Your script should connect to a MySQL server running on `localhost` at `port 3306`
- Results must be sorted in ascending order by `states.id`
- The results must be displayed as they are in the example below
- Your code should not be executed when imported

```guillaume@ubuntu:~/$ ./9-model_state_filter_a.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
5: Nevada
guillaume@ubuntu:~/$
```

No test cases needed

**Repo:**

- GitHub repository: `alx_python`
- Directory: `python-object_relational_mapping`
- File: `9-model_state_filter_a.py`
