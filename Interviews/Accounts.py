class Account:
    # constructor
    def __init__(self,name,acct_no,balance):
        self.name = name # public
        self._acct_no = acct_no # protected
        self.__balance = balance

    def deposit_balance(self,amount):
        if amount >0:
            self.__balance+=amount
    def withdraw_balance(self,amount):
        if self.__balance > amount:
            self.__balance-=amount

    @property
    def acct_no(self):
        return self._acct_no
    @property
    def get_bal(self):
        return self.__balance


# Creating object
account = Account("Ram Singh",12345,50000)
print(f"Name: {account.name}")
print(f"AccountNumber: {account.acct_no}")
account.deposit_balance(60000)
account.withdraw_balance(30000)
print(f"Available balance: {account.get_bal}")