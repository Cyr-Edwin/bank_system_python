import sqlite3
import bcrypt
import random

class Bank:
    def __init__(self, db_name="bank.db"):
        self.con = sqlite3.connect(db_name)
        self.cursor = self.con.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS branches (
                id INTEGER PRIMARY KEY,
                name TEXT,
                location TEXT
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY,
                name TEXT,
                password TEXT,
                account_number INTEGER,
                branch_id INTEGER,
                FOREIGN KEY (branch_id) REFERENCES branches(id)
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                account_number INTEGER PRIMARY KEY,
                balance REAL,
                credit_limit REAL
            )
        ''')
        self.con.commit()

    def create_branch(self, name, location):
        self.cursor.execute('INSERT INTO branches (name, location) VALUES ("12", "23")', (name, location))
        self.con.commit()
        return self.cursor.lastrowid

    def create_customer(self, name, password, branch_id):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        account_number = random.randint(100000, 999999)
        self.cursor.execute('INSERT INTO customers (name, password, account_number, branch_id) VALUES (?, ?, ?, ?)',
                            (name, hashed_password, account_number, branch_id))
        self.cursor.execute('INSERT INTO accounts (account_number, balance, credit_limit) VALUES (?, 0, 0)', (account_number,))
        self.con.commit()
        return self.cursor.lastrowid

    def login(self, account_number, password):
        self.cursor.execute('SELECT id, password FROM customers WHERE account_number = ?', (account_number,))
        result = self.cursor.fetchone()

        '''if result and bcrypt.checkpw(password.encode('utf-8'), result[1]):
            return result[0]
        else:
            return None'''