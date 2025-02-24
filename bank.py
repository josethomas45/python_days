class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount

    def display_balance(self):
        print(f"Current balance: {self.balance}")

alice_account = BankAccount("Alice", 500)
alice_account.deposit(200)

alice_account.withdraw(100)


alice_account.display_balance()