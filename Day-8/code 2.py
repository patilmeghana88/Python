class BankAccount:
    def __init__(self,balance):
        self._balance = balance #Private variable

    def deposit(self,amount):
        self._balance += amount

    def get_balance(self):
        return self._balance
    
#creating an object
account = BankAccount(2000)
account.deposit(300)
print(account.get_balance())
    