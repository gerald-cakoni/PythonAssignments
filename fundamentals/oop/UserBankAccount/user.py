class User: 
    def __init__(self, name):
        self.name = name
        self.account = BankAccount (int_rate = 0.02, balance = 0)

    def make_deposit(self, amount):
        self.account += amount
        return self

    def make_withdrawal(self, amount):
        if amount <= self.account:
            self.account -= amount
            return self

    def display_user_balance(self):
        return self.account

user1 = User('Jimmy')
user2 = User('John')
user3 = User('Jenny')

user1.make_deposit(100).make_deposit(250).make_deposit(300).make_withdrawal(147).display_user_balance()

user2.make_deposit(500).make_deposit(200).make_withdrawal(600).make_withdrawal(50)

user3.make_deposit(603).make_withdrawal(402).make_withdrawal(102).make_withdrawal(22).transfer_money(user2, 20) 

print(user1.user_balance)
print(user2.user_balance)
print(user3.user_balance)