import argparse
import sqlite3

def setup_db():
    con = sqlite3.connect("my_db.sqlite3")
    cur = con.cursor()
    cur.execute("CREATE TABLE students(name, grade)")
    cur.execute("INSERT INTO students VALUES('Alice', 'A')")
    cur.execute("INSERT INTO students VALUES('Bob', 'B')")
    cur.execute("INSERT INTO students VALUES('Charlie', 'C')")
    con.commit()
    con.close()

def list_students():
    con = sqlite3.connect("my_db.sqlite3")
    cur = con.cursor()
    cur.execute("SELECT * FROM students")
    for row in cur.fetchall():
        print(row)
    con.close()

# THIS IS BAD
def unsafe_insert():
    name = input("Enter name: ")
    grade = input("Enter grade: ")
    con = sqlite3.connect("my_db.sqlite3")
    cur = con.cursor()
    cur.execute("insert into students (name, grade) values" +
        "('" + name + "', '" + grade + "')")
    con.commit()
    con.close()

if __name__ == "__main__":
    arguments = argparse.ArgumentParser()
    arguments.add_argument("action", choices=["setup", "list", "insert"])
    args = arguments.parse_args()
    if args.action == "setup":
        setup_db()
    elif args.action == "list":
        list_students()
    elif args.action == "insert":
        unsafe_insert()