from bank import *


class User:
    all_accounts = []
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.bank = BankAccount() #Connect the class user with the class bank
        User.all_accounts.append(self)

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.bank.account_balance}")

    @classmethod
    def all_balances(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += account.bank.account_balance
        return sum

guido = User("Guido", "guido@gmail.com")
monty = User("Monty","monty@gmail.com")

guido.bank.deposit(200).deposit(300).deposit(150).withdraw(400).yield_interest()
monty.bank.deposit(200).deposit(300).withdraw(150).withdraw(430).withdraw(230).withdraw(130).yield_interest()

guido.display_user_balance()
monty.display_user_balance()

print(f"The total amount of all users is: {User.all_balances()}")
