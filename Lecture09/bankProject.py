class BankAccount:
    def __init__(self,acc_no,balance):
        self.acc_no=acc_no
        self.__balance=balance#__ double underscore used to make it private
        self.history=[]

    def credit(self,amount):
        self.__balance+=amount
        self.history.append(f"Credited:{amount}")
        print("Amount credited:",amount)

    def debit(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            self.history.append(f"Amount debited:{amount}")
            print("Amount debited:",amount)

    def show_balance(self):
        print("Balance is:",self.__balance)

    def show_history(self):
        print("Transaction history:",self.history )


obj1=BankAccount("PUNSBI909",2000)
obj1.credit(1000)
obj1.debit(500)
obj1.show_balance()
obj1.show_history()