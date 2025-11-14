import datetime

from ascii import Ascii

ascii = Ascii()


class Transaction:
    # The constructor for the Transaction class
    def __init__(self, bank_account):
        self.timestamp = datetime.datetime.now()
        self.bank_account = bank_account
        self.type = ""
        self.amount = 0.0
        self.fee = 0.0
        self.balance_after = 0.0
        self.bank_account.transactions.append(self)

    # Deposit Funds Method
    def deposit_funds(self):
        self.type = "deposit"
        self.amount = round(float(input()), 2)
        self.bank_account.balance += self.amount
        self.balance_after = self.bank_account.balance

    # Withdraw Funds Method
    def withdraw_funds(self):
        self.type = "withdraw"
        self.amount = round(float(input()), 2)
        self.bank_account.balance -= self.amount
        self.balance_after = self.bank_account.balance

    # Convert Funds Method
    def transfer_funds(self, to_account):
        self.type = "transfer"
        self.amount = round(
            float(input("How much would you like to transfer into this account?\n"))
        )
