class BankAccount:

    all_accounts = []

    def __init__(self, account_balance, interest):
        self.account_balance = account_balance
        self.interest = interest
        BankAccount.all_accounts.append(self)


    def deposit(self, amount):
        self.account_balance += amount
        return self


    def withdraw(self, amount):
        if (self.account_balance-amount>0):
            self.account_balance -= amount
        else:
            print("Issufficient Funds")
            self.account_balance -= 5
        return self


    def yield_interest(self):
        self.account_balance += self.account_balance*self.interest


    def display_account_info(self):
        print(f"Balance: ${self.account_balance}")

    @classmethod
    def all_balances(cls):
        sum = 0
        # we use cls to refer to the class
        for account in cls.all_accounts:
            sum += account.account_balance
        return sum

guido = BankAccount(0,0.05)
monty = BankAccount(200,0.033)

guido.deposit(200).deposit(300).deposit(150).withdraw(430).yield_interest()
monty.deposit(200).deposit(300).withdraw(150).withdraw(430).withdraw(230).withdraw(130).yield_interest()

guido.display_account_info()
monty.display_account_info()

BankAccount.all_balances()