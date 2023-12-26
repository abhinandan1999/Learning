### Installing MySQL Server (Ubuntu)

```
<u>sudo apt update</u>
<u>sudo apt install mysql-server</u>
```

### To check the status of MySQL Server
```
<u>sudo systemctl status mysql.service</u>
```

### To start the MySQL Server
```
<u>sudo systemctl start mysql.service</u>
```

### To enter MySQL shell
```
<u>sudo mysql</u>
```

### Set up configuration 
```
<u>sudo mysql_secure_installation</u>
```

### Setup password USER using ALTER Command
```
<u>ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Qwerty2@';</u>
```

====================================================================================================
DtataBase (Make notes from leetcode)



=====================================================================================================
SQL (Structured query Langauge)
*It is used to query the data from relational database*



## SQL Syntax

### _Syntax related to Database_

Get the list of all the databases currently present.
```
SHOW DATABASES;
```

Create a database
```
CREATE DATABASE <name_of_database>;
```

Drop the database
```
DROP DATABASE <name_of_database>;
```

Connect with database
```
USE <name_of_database>;
```

Check current database
```
SELECT database();
```

_Syntax related to tables in Database_

Create a table in database
```
CREATE TABLE <name_of_table>
(
    col_name1 datatype1,
    col_name2 datatype2,
    col_name3 datatype3
);
```

Show various tables in database
```
SHOW tables;
```

See schema of table
```
DESCRIBE <name_of_table>;
DESC <name_of_table>
```

Drop the table
```
DROP table <name_of_table>
```
















































### Create a note about datatype in SQL


