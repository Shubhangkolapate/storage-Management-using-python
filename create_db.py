import sqlite3
def create_db():
    con=sqlite3.connect(database=r'shu.db')
    cur=con.cursor()
    cur.execute("Create Table if not exists student(pid INTEGER PRIMARY KEY AUTOINCREMENT,Name text,Branch text,Email text,password text,Utype text)")
    con.commit()
    #cur.execute()

    cur.execute("Create Table if not exists category(cid INTEGER PRIMARY KEY AUTOINCREMENT,Name text)")
    con.commit()
   
    cur.execute("Create Table if not exists supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT,Name text,Contact text)")
    con.commit()
    
    cur.execute("Create Table if not exists product(pid INTEGER PRIMARY KEY AUTOINCREMENT,category text,supplier text,name text,price text,qty text,status text)")
    con.commit()
create_db()