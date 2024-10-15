from bank_system import BankAccount

# Create two BankAccount objects
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 500)

# Perform operations on the accounts
account1.deposit(500)
account2.withdraw(200)
account1.check_balance()
account2.check_balance()

# Print the total number of bank accounts created
print(f"Total bank accounts created: {BankAccount.total_accounts}")
