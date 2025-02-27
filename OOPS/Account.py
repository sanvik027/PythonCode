class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance # private attribute

    def deposit(self,amount):
        self.__balance+=amount

    def withdrawal(self, amount):
        if amount <=self.__balance:
            self.__balance-=amount
        else:
            return "insufficient balance"

    def display_balance(self):
        return self.__balance

# Creating object of account class
account = Account("Ram",45000)
account.deposit(50000)
account.withdrawal(20000)
print(account.display_balance())

