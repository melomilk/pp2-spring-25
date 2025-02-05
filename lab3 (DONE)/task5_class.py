class Account:
    def __init__(self):
        self.owner = input("Enter your name: ")  
        self.balance = float(input("Enter your initial balance: "))  

    def deposit(self):
        amount = float(input("Enter the amount of money to add to bank acc: "))  
        self.balance += amount
        print(f"Your new balance: {self.balance}")

    def withdraw(self):
        amount = float(input("How much do you wanna withdraw?: "))  
        if amount > self.balance:
            print("You don't have enough funds.")
        else:
            self.balance -= amount
            print(f"Withdrawn successful! Your new balance: {self.balance}")

    def show_balance(self):
        print(f"Owner: {self.owner}, Current balance: {self.balance}")

account = Account()
account.show_balance()

account.deposit()

account.withdraw()

account.show_balance()