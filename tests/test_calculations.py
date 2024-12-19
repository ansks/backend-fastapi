from app.calculations import add, subtract, multiply, divide, BankAccount, InsufficientBalance
import pytest


# @pytest.fixture
# def test_zero_bank_account():
#     print("Zero Bank Account opened")
#     return BankAccount()

# def test_initial_funds_account()


# To initialise certain things: like database, email server -> rather initilizing again and again
@pytest.fixture
def zero_bank_account():
    print("Empty bank account")
    return BankAccount()


@pytest.fixture
def bank_account():
    print("Account with balance of 20")
    return BankAccount(20)


@pytest.mark.parametrize(
    "deposited, withdrew, expected",
    [(200, 100, 100), (1200, 200, 1000), (600, 500, 100)],
)
def test_bank_transactions(zero_bank_account, deposited, withdrew, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)

    assert zero_bank_account.balance == expected

def test_insufficient_funds(bank_account):
    with pytest.raises(InsufficientBalance):  # very specific exception helpful in scenarios where multiple exception can occur
        bank_account.withdraw(200)
        

def test_zero_bank_account(zero_bank_account):
    print("Testing my bank account")
    assert zero_bank_account.balance == 0


def test_deposit(bank_account):
    bank_account.deposit(20)
    assert bank_account.balance == 40


def test_withdraw(bank_account):
    bank_account.withdraw(10)
    assert bank_account.balance == 10


def test_interest(bank_account):
    bank_account.interest()
    assert round(bank_account.balance, 6) == 22


@pytest.mark.parametrize("num1, num2, expected", [(1, 2, 3), (4, 5, 9)])
def test_add(num1, num2, expected):
    print("adding two numbers")
    assert add(num1, num2) == expected


def test_subtract():
    print("subtracting two numbers")
    assert subtract(10, 5) == 5


def test_multiply():
    print("multiply two numbers")
    assert multiply(5, 2) == 10


def test_divide():
    print("divide two numbers")
    assert divide(10, 2) == 5
