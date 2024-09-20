import sqlite3

from Bank_Account import BankAccount


class Bank:
    def _init_(self):
        self.connection = sqlite3.connect('bank.db')
        self.cursor = self.connection.cursor()
        self.create_account_table()

    def create_account_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                account_number TEXT PRIMARY KEY,
                account_name TEXT,
                balance REAL,
                address TEXT,
                phone_number TEXT,
                email TEXT
            )
        ''')
        self.connection.commit()

    def create_account(self):
        account_number = input("Enter Account Number: ")
        account_name = input("Enter Account Name: ")
        initial_balance = float(input("Enter Initial Balance: "))
        address = input("Enter Address: ")
        phone_number = input("Enter Phone Number: ")
        email = input("Enter Email: ")

        try:
            self.cursor.execute('''
                INSERT INTO accounts (account_number, account_name, balance, address, phone_number, email)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (account_number, account_name, initial_balance, address, phone_number, email))
            self.connection.commit()
            print("Account created successfully.")
        except sqlite3.IntegrityError:
            print("--------Account already exists.----------------")

    def display_account(self):
        account_number = input("Enter Account Number: ")
        self.cursor.execute('SELECT * FROM accounts WHERE account_number = ?', (account_number,))
        account = self.cursor.fetchone()
        if account:
            acc = BankAccount(*account)
            acc.display_details()
        else:
            print("Account does not exist.")

    def deposit(self, account_number, amount):
        self.cursor.execute('SELECT * FROM accounts WHERE account_number = ?', (account_number,))
        account = self.cursor.fetchone()
        if account:
            acc = BankAccount(*account)
            new_balance = acc.deposit(amount)
            if new_balance is not None:
                self.cursor.execute('UPDATE accounts SET balance = ? WHERE account_number = ?', (new_balance, account_number))
                self.connection.commit()
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        self.cursor.execute('SELECT * FROM accounts WHERE account_number = ?', (account_number,))
        account = self.cursor.fetchone()
        if account:
            acc = BankAccount(*account)
            new_balance = acc.withdraw(amount)
            if new_balance is not None:
                self.cursor.execute('UPDATE accounts SET balance = ? WHERE account_number = ?', (new_balance, account_number))
                self.connection.commit()
        else:
            print("Account not found.")

    def close_account(self):
        account_number = input("Enter account number: ")
        self.cursor.execute('DELETE FROM accounts WHERE account_number = ?', (account_number,))
        if self.cursor.rowcount > 0:
            self.connection.commit()
            print(f"Account {account_number} has been closed.")
        else:
            print("Account not found.")

    def display_all_accounts(self):
        self.cursor.execute('SELECT * FROM accounts')
        accounts = self.cursor.fetchall()
        if not accounts:
            print("No accounts found.")
        else:
            print("\nAll Accounts:")
            for account in accounts:
                acc = BankAccount(*account)
                acc.display_details()

    def close_connection(self):
      self.connection.close()