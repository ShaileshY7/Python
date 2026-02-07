# Task:​
# Create an Account class with:
# ●​ Attributes → balance, account number​
# ●​ Methods → debit, credit, print balance​

class Account:

    def __init__(self,accno,balance):
        self.accno=accno
        self.balance=balance

    def  credit(self,amount):
        self.balance+=amount
        print("Amount is created:",amount)
    
    def debit(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print("Amount is debited:",amount)
        else:
            print("Insufficient balance")
    
    def printbalance(self):
        print("Balance:",self.balance)

account=Account("PUNB099",5000)
account.credit(500)
account.debit(10000)
account.printbalance()