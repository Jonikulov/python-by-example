import sqlite3

con = sqlite3.connect('company.db')
cur = con.cursor()

# List the tables in a database
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
# See the properties of a table in a database
cur.execute("SELECT sql FROM sqlite_master " \
            "WHERE type='table' AND name='MY_TABLE_NAME'")
# metadata = cur.fetchone()[0]

cur.execute("""CREATE TABLE IF NOT EXISTS employees(
    id integer PRIMARY KEY,
    name text NOT NULL,
    dept text NOT NULL,
    salary integer);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS dept(
    dept text PRIMARY KEY,
    manager text NOT NULL);
""")

# cur.execute("""INSERT INTO employees(id,name,dept,salary)
#     VALUES("1","Bob","Sales","25000")
# """)

# newID = input("Enter ID number: ")
# newName = input("Enter name: ")
# newDept = input("Enter department: ")
# newSalary = input("Enter salary: ")
# cur.execute("""INSERT INTO employees(id,name,dept,salary)
#     VALUES(?,?,?,?)""",(newID,newName,newDept,newSalary)
# )

cur.execute("SELECT * FROM employees")
# cur.execute("SELECT * FROM employees ORDER BY name")
# cur.execute("SELECT * FROM employees WHERE salary>20000")
# cur.execute("SELECT * FROM employees WHERE dept='Sales'")
# cur.execute("SELECT name, salary FROM employees")

# cur.execute("""SELECT employees.id, employees.name, dept.manager
#     FROM employees, dept
#     WHERE employees.dept=dept.dept
#     AND employees.salary > 20000
# """)

# whichDept = input("Enter a department: ")
# cur.execute("SELECT * FROM employees WHERE dept=?", [whichDept])

# cur.execute("UPDATE employees SET name='Tony' WHERE id=1")
# cur.execute("DELETE FROM employees WHERE id=1")

for x in cur.fetchall():
    print(x)

# con.commit()
con.close()