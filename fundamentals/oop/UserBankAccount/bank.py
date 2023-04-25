class BankAccount:
	def __init__(self, account, int_rate, balance): # don't forget to add some default values for these parameters!
		self.account = account
		self.int_rate = 0.002
		self.balance = 0

	def deposit(self, amount):
		self.balance += amount
		return self

	def withdraw(self, amount):
		if amount <= self.balance:
			self.balance -= amount
			return self
		else: 
			amount > self.balance
			self.balance = self.balance - 5
			return print('Insufficient funds: Charging a $5 fee')

	def display_account_info(self):
		return self.balance

	def yield_interest(self, amount):
		self.balance = amount*0.02 + amount
		return self

jimmy = BankAccount('Jimmy\'s Account',0,0)
jenny = BankAccount('Jenny\'s Account',0,0)
poor = BankAccount('Poor\'s Account',0,0)
Rich = BankAccount('Rich\'s Account',0,0)

jimmy.deposit(100).deposit(200).deposit(300).withdraw(600/2).display_account_info()

jenny.deposit(200).deposit(100).withdraw(50).withdraw(25).withdraw(25).withdraw(100).display_account_info()

poor.withdraw(5) # poor has nothing but still withdraw 10 therefore he was charged $5 fee.

Rich.yield_interest(100)

print(jimmy.balance)
print(jenny.balance)
print(poor.balance)
print(Rich.balance)