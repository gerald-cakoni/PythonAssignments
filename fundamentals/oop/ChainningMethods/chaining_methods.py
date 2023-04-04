class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")


guido = User("Guido","guido@gmail.com")
monty = User("Monty","monty@gmail.com")
sara = User("Sara","sara@gmail.com")

guido.make_deposit(500).make_deposit(300).make_deposit(600).make_withdrawal(800).display_user_balance()

monty.make_deposit(200).make_deposit(500).make_withdrawal(100).make_withdrawal(350).display_user_balance()

sara.make_deposit(500).make_deposit(50).make_withdrawal(100).make_withdrawal(300).display_user_balance()

guido.transfer_money(sara,300).display_user_balance()
sara.display_user_balance()
