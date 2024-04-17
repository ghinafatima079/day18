"""Define a Python class BankAccount with private attributes __balance and __account_number.
Implement public methods get_balance() and deposit(amount) to retrieve the balance and deposit money into the account respectively. 
Ensure that the __balance attribute cannot be accessed directly from outside the class."""

class BankAccount:
    def __init__(self,account_number):
        self.__balance=0
        self.__account_number=account_number
    def get_balance(self):
        return self.__balance
    def deposit(self,amount):
        if amount>0:
            self.__balance=self.__balance+amount
            print(f"Deposited: {amount}   New Balance:{self.__balance}")
        else:
            print("Invalid input")
account1=BankAccount("ABC123")
account1.deposit(10000)
print(f"Your current balance is {account1.get_balance()}")
account1.deposit(5000)
print(f"Your current balance is {account1.get_balance()}")
