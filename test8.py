class BankAccount:
    def __init__(self, change):
        self.money = 0
        self.money = change

    def withdraw(self, minus):
        self.money =  self.money - minus 

    def desposit(self,amount):
        self.money = self.money + amount

    def balance(self):
        print(self.money)
        

x = BankAccount(700)
x.balance()
x.withdraw(70)
x.balance()
x.desposit(7)
x.balance()