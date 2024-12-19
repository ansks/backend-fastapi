def add(num1: int, num2: int):
    return num1 + num2


def subtract(num1: int, num2: int):
    return num1 - num2


def multiply(num1: int, num2: int):
    return num1 * num2


def divide(num1: int, num2: int):
    return num1 / num2


class InsufficientBalance(Exception):
    """Custom Exception class"""
    pass
    

class BankAccount():

    def __init__(self, balance = 0):
        self.balance = balance
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalance("Not enough balance")
            # raise ZeroDivisionError
        
        self.balance = self.balance - amount
        
    def interest(self):
        self.balance = self.balance*1.1
