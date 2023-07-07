import sqlite3

def create_db():
    con = sqlite3.connect(database = r'win.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT, name text, email text, gender text, contact text, dob text, doj text, pass text, utype text, address text, salary text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS employee_backup(eid INTEGER PRIMARY KEY AUTOINCREMENT, name text, email text, gender text, contact text, dob text, doj text, pass text, utype text, address text, salary text)")
    con.commit()



    cur.execute("CREATE TABLE IF NOT EXISTS customer(invoice INTEGER PRIMARY KEY AUTOINCREMENT, name text, contact text, desc text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS customer_backup(invoice INTEGER PRIMARY KEY AUTOINCREMENT, name text, contact text, desc text)")
    con.commit()



    cur.execute("CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT, name text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS category_backup(cid INTEGER PRIMARY KEY AUTOINCREMENT, name text)")
    con.commit()



    cur.execute("CREATE TABLE IF NOT EXISTS project(pid INTEGER PRIMARY KEY AUTOINCREMENT, Customer text, Category text, name text, stipend text, length text, status text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS project_backup(pid INTEGER PRIMARY KEY AUTOINCREMENT, Customer text, Category text, name text, stipend text, length text, status text)")
    con.commit()


create_db()