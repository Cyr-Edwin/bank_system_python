# import modules
import sqlite3
import bcrypt
import random

# create Bank class
class Bank:
    
    # create constructor
    def __init__(self, db_name = "bank.db"):
        self.con = sqlite3.connect(db_name)
        self.cursor = self.con.cursor()
        self.create_tables()
    def create_tables(self):
        self.cursor.execute('''
             CREATE TABLE IF NOT EXISTS branches(
                            id_branch INTEGER PRIMARY KEY,
                            name TEXT,
                            location TEXT
             )
''')
        self.cursor.execute('''
              CREATE TABLE IF NOT EXISTS customers(
                            id_cus INTEGER PRIMARY KEY,
                            name TEXT,
                            password TEXT,
                            account_number INTEGER,
                            id_br INTEGER,
                            FOREIGN KEY(id_br) REFERENCES branches(id)

                            
              )
''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts(
                            account_number INTEGER PRIMARY KEY,
                            balance REAL,
                            credit_limit REAL

            )
''')
        self.con.commit()

    def branches_table(self, name , location):
        self.cursor.execute('INSERT INTO branches(name , location) VALUES(?,?)',(name , location))
        rows = self.cursor.execute('SELECT * FROM branches')
        print(rows)
        self.con.commit()
        


p = Bank("db")
p.branches_table("12","123")