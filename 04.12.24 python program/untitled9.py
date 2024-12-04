class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0  # Initialize balance to zero

    def deposit(self, amount):
        """Adds the specified amount to the balance."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Subtracts the specified amount from the balance if sufficient funds are available."""
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Withdrawal amount must be positive.")

    def view_balance(self):
        """Displays the current balance."""
        print(f"Current balance is {self.balance}.")

# Example usage
def bank_account_simulation():
    # Create a new bank account
    account = BankAccount("Alice")

    # Deposit money
    account.deposit(1000)
    
    # View balance
    account.view_balance()

    # Withdraw money
    account.withdraw(500)
    
    # View balance again
    account.view_balance()
    
    # Attempt to withdraw more than the balance
    account.withdraw(600)

    # View balance again
    account.view_balance()

# Execute the task
bank_account_simulation()
