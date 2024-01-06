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
<u>ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '<enter password>';</u>
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


### _Syntax related to tables in Database_

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


### CRUD Operation
C: Create: INSERT statements \
R: Read: SELECT statements \
U: UPDATE statements \
D: DELETE statements


Create a table in database
```
CREATE TABLE <name_of_table>
(
    col_name1 datatype1 CONSTRAINT1,
    col_name2 datatype2 CONSTRAINT2,
    col_name3 datatype3 CONSTRAINT3
);
```

Inserting values in tables
```
INSERT INTO <table_name(colName1, colName2, colName3)> VALUES (colValue1, colValue2, colValue3),
(colValue1, colValue2, colValue3),
(colValue1, colValue2, colValue3);
```

Read all columns from table
```
SELECT * FROM <table_name>;
```

Read specified columns from table
```
SELECT <colName1>, <colName2> FROM <tableName>;
```

Check current database
```
SELECT database();
```

List all the schemas
```
SELECT schema();
```

Filter clause
<!-- Filter clause on strings are case insensitive !-->
```
SELECT 
    <colName1>, 
    <colName2> 
FROM <tableName>
WHERE 
    <colName1> = <value1>
```

Case sensitive filter clause
```
SELECT 
    <colName1>, 
    <colName2> 
FROM <tableName>
WHERE 
    BINARY <colName1> = <value1>
```

ALIAS in SQL
```
SELECT
    firstname AS fname,
    lastname AS lname
FROM
    <tableName>
```

UPDATE STATEMENTS IN SQL
```
UPDATE <tableName>
SET
    <colName> = <colValue>
WHERE
    <colName2> = <colValue2>
```

DELETE STATEMENT IN SQL
```
DELETE * FROM <tableName>
```

ALTER COMMANDS IN SQL
USECASES: \
1. Add a new column \
```
    ALTER TABLE <tableName>
    ADD COLUMN
        <colNametoAdd> <datatype>
```

    2. DROP a column \
        ```
        ALTER TABLE <tableName>
        DROP COLUMN
            <coltoDrop>
        ```
    
    3. Modify the column \
        ```
        ALTER TABLE <tableName>
        MODIFY COLUMN
	        <colName> datatype;
        ```

DDL vs DML \
DDL: Data Definition Language: Changes the table structure \
Ex: CREATE, ALTER, DROP, TRUNCATE \

DML: Data Manipulation Language \
Ex: INSERT, UPDATE, DELETE \


Difference between TRUNCATE and DELETE \
TRUNCATE (DDL): Remove all the records from table and recreate it \
DELETE (DML): Deletes records one by one hence inefficient \



DISTINCT Command
```
SELECT DISTINCT 
    colName1, 
    colName2
FROM
    tableName
```

ORDER BY Command
```
SELECT
    *
FROM
    tableName
ORDER BY colName1 DESC;
```

LIMIT Command
```
SELECT
    *
FROM tableName
ORDER BY
    colName1 ASC,
    colName2 DESC
LIMIT 10;
```

```
SELECT
    *
FROM tableName
ORDER BY
    colName1 ASC,
    colName2 DESC
LIMIT <startOfRow>, <numOfRows>;
```

REGEXP in SQL
```
SELECT 
    *
FROM
    employee2
WHERE
    colName REGEXP 'regexp_pattern';
```

LOGICAL Operator in SQL \
    1. _=_ : Equal to \
    2. _!=_ or _<>_ : Not equal to \
    3. _LIKE <keyword>_  \
    4, _NOT LIKE <keyword>_ \
    5. _AND_ \
    6. _OR_ \
    7. _IN ('word1', 'word2')_ \
    8. _NOT IN ('word1', 'word2')_ \


CASE STATEMENTS 
```
SELECT
    col1,
    col2,
    CASE
        WHEN <condition1> THEN <value1>
        WHEN <condition2> THEN <value2>
        ELSE value3
    END AS col3
FROM
    <table_name>
```


JOINS in SQL
```
SELECT
    a.col1,
    b.col2,
    a.vcol3
FROM
    table1 AS a
        <TYPE OF JOIN> JOIN
    table2 AS b
    ON a.common_col1 = b.common_col2
```

TYPES of JOINS
1. DEFAULT is INNER join
2. LEFT JOIN or LEFT OUTER JOIN: Same
3. RIGHT JOIN
4. OUTER JOIN: can also be UNION between LEFT and RIGHT outer JOIN
5. CROSS JOIN: Multiply the table, DEFAULT if no condition for JOIN is provided


DIfference between WHERE and HAVING Clause \
WHERE: Is used to filter individual records before GROUPBY clause \
HAVING: is used after aggregation to filter out \



Create new table from existing table
```
CREATE
    TABLE new_table
    AS
    SELECT
        * 
    FROM
        existing_table
```

OVER and PARTITION BY Clause
```
SELECT
    col1,
    col2,
    COUNT(agg_col) OVER (PARTITION BY part_col)
FROM
    table1
```

ROW NUMBER
```
SELECT
    col1,
    col2,
    ROW_NUMBER() OVER (ORDER BY order_col DESC)
FROM
    table
```

RANK and DENSE Rank \
Rank: Gives same number to same value and continues like row_number \
Ex: \
|Name    |class   |Rank|
|:------:|:------:|---:|
|Abhi    |1       |1   |
|Rahul   |1       |1   |
|Pathak  |2       |3   |

DENSE RANK: Gives same number to same value and resumes from latest rank \
Ex: \
|Name    |class   |Rank|
|:------:|:------:|---:|
|Abhi    |1       |1   |
|Rahul   |1       |1   |
|Pathak  |2       |2   |


INDEXES and ORDER OF EXECUTION \
There are two ways SQL search for data: \
1. SEEK: Based on index
         Generally Primary keys are inserted in order and search can happen faster using indexes

         INDEX are of 2 types:
            1. Clustered Index
                There can be only one clustered index.
                It can be from single column or multiple column

            2. Non Clustered Index
                a. Creates a index table, where column in   kept in sorted order
                b. First it retrieves information from index and search in the main table
                c. It is 2 step process
2. SCAN: Search the entire table
         SQL searches the entire data


<b>Way to read a plan: \
It is read from Right to LEFT and Top to Bottom </b>



Common Table Expression (CTE)
1. It is used to simplify queries
2. It improves readability of queries

```
WITH
    new_table1 (req_col1, req_col2) AS (
        SELECT
            col1,
            col2
        FROM    
            table1
    )

    new_table2 AS (
        SELECT
            req_col1
        FROM 
            new_table1
    )

SELECT req_col1 FROM new_table2
```

a. From WITH till SELECT it is a single query \
b. CTE stores table in memory \
c. CTE defines a temporary result set that can be referred in \
    SELECT, INSERT, UPDATE, DELETE statements, immediately followed by CTE expressions \
d. CTE can improve the performance (Not always) \
e. On CTE indexes are non performant \
















































































### Questions
1. Create a note about datatype, constraint  and Keys in SQL
2. Understand all usecase of ALTER command
3. Understand the difference between DELETE, TRUNCATE and DROP 
4. Understand LIKE operator in SQL


