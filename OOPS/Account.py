class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance # private attribute

    def deposit(self,amount):
        if amount > 0:
            self.__balance+=amount
        else:
            return "Wrong amount"

    def withdrawal(self, amount):
        if amount <=self.__balance:
            self.__balance-=amount
        else:
            return "insufficient balance"

    def display_balance(self):
        return self.__balance

# Creating object of account class
account = Account("Ram",45000)
account.deposit(70000)
account.withdrawal(15000)
print(account.display_balance())

