class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")


guido = User("Guido","guido@gmail.com")
monty = User("Monty","monty@gmail.com")
sara = User("Sara","sara@gmail.com")

guido.make_deposit(500)
guido.make_deposit(300)
guido.make_deposit(600)
guido.make_withdrawal(800)
guido.display_user_balance()

monty.make_deposit(200)
monty.make_deposit(500)
monty.make_withdrawal(100)
monty.make_withdrawal(350)
monty.display_user_balance()

sara.make_deposit(500)
sara.make_deposit(50)
sara.make_withdrawal(100)
sara.make_withdrawal(300)
sara.display_user_balance()

guido.transfer_money(sara,300)
guido.display_user_balance()
sara.display_user_balance()
