class BankDetails:

    # constructor
    def __init__(self,name,account_no,balance):
        self.name = name
        self._account_no =account_no # protected
        self.__balance = balance # private
    def display_name(self):
        print(f"{self.name}")
    def deposit(self,amount):
        if amount >0:
            self.__balance+=amount
        else:
            print("Can't add Zero rupees to account")
    def withdrawal(self,amount):
        if amount <self.__balance:
            self.__balance-=amount
        else:
            print("insufficient funds")
        # Getter method for balance
    def get_balance(self):
        return self.__balance

        # Setter method for balance
    def set_balance(self, balance):
        if balance >= 0:
             self.__balance = balance
        else:
            print("Balance cannot be negative.")

class Account(BankDetails):
    def display_info(self):
        print(f"name : {self.name}")
        print(f"account_no : {self._account_no}")
        # Accessing private member using getter method
        balance = self.get_balance()
        print(f"balance: {balance}")

# object Creation
account = Account("Ram Singh","90289484",60000)
account.deposit(5000)
account.withdrawal(2000)
account.display_info()



