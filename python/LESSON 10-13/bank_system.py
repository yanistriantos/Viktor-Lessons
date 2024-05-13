class BankAccount:
    # Class attribute to keep track of the total number of bank accounts
    total_accounts = 0  # this attribute is static -> doesn't belong to a single object but is rather a SHARED STATE

    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder
        self.balance = initial_balance
        BankAccount.total_accounts += 1

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        # python's and operator == C++'s && operator
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            # self.balance = self.balance - amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid amount for withdrawal.")

    def check_balance(self):

        print(f"Account balance for {self.account_holder}: ${self.balance}")

    # 'dunder', 'special', 'magic' methods
    def __str__(self):
        return f"random stuff"
