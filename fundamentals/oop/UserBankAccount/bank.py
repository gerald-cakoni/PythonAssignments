class BankAccount:



    def __init__(self):
        self.account_balance = 0
        self.interest = 0.02 


    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdraw(self, amount):
        if (amount-self.account_balance)>0:
            print("Insuficient Founds")
            self.account_balance -= 5
        else:
            self.account_balance -= amount
        return self

    def yield_interest(self):
        self.account_balance += self.account_balance*self.interest
        return self