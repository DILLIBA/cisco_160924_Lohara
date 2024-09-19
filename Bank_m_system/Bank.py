from Bank_Account import  BankAccount


class Bank:
    
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        account_number = input("Enter Account Number: ")
        account_name = input("Enter Account Name: ")
        initial_balance = float(input("Enter Initial Balance: "))
        address = input("Enter Address: ")
        phone_number = input("Enter Phone Number: ")
        email = input("Enter Email: ")

        if account_number in self.accounts:
            print("--------Account already exists.----------------")
           
        else:
            self.accounts[account_number] = BankAccount(account_number, account_name, initial_balance, address, phone_number, email)
            
            print("Account created successfully.")
            print("-------------------------------------Thank You------------------------------------------\n\n\n")

    
       
    def display_account(self):
        account_number = input("Enter Account Number: ")

        if account_number in self.accounts:
            self.accounts[account_number].display_details()
        else:
            print("Account does not exist.")  
    
    def find_account(self, account_number):
        return self.accounts.get(account_number, None)

    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.deposit(amount)
        else:
            print("Account not found.")
    def withdraw(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found.")

    def close_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print(f"Account {account_number} has been closed.")
        else:
            print("Account not found.")

    def display_all_accounts(self):
        if not self.accounts:
            print("No accounts found.")
        else:
            print("\nAll Accounts:")
            for account in self.accounts.values():
                account.display() 