from ast import Invert
from distutils.util import execute
import sqlite3

def connect():
    conn=sqlite3.connect("Stock_list.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Stock (id INTEGER PRIMARY KEY, description text, code integer, quantity integer, supplier text)")
    conn.commit()
    conn.close()

    def insert(): ("description, code, quantity, supplier")
    conn: sqlite3.connect("Stock_list.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO Stock VALUES (NULL,?,?,?,?)",("description","code","quantity","supplier"))
    conn.commit()
    conn.close()
    
def view():
    conn=sqlite3.connect("Stock_list.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM Stock")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(description="",code="",quantity="",supplier=""):
    conn=sqlite3.connect("Stock_list.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM Stock_list.db WHERE description=? OR code=? OR quantity=? OR supplier=?", (description,code,quantity,supplier))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("Stock_list.db")
    cur=conn.cursor()
    cur.execute("DELETE * FROM Stock WHERE id=?",(id,))
    conn.commit()
    conn.close()
    
#def total_out():
    #conn=sqlite3.connect("Stock_list.db")
    #cur=conn.cursor()
    #cur.execute("COUNT * FROM Stock WHERE id=?",(id,))
    #conn.commit()
    #conn.close()

    connect()
