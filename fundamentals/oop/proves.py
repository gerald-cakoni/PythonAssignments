class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received

guido = User("Guido","guido@gmail.com")
monty = User("Monty","monty@gmail.com")

guido.make_deposit(100)
guido.make_deposit(500)
guido.make_deposit(500)
monty.make_deposit(50)
print(guido.account_balance)	# output: 300
print(monty.account_balance)	# output: 50
