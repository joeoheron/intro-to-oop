import datetime


class Transaction:
    def __init__(self, bank_account):
        self.timestamp = datetime.datetime.now()
        self.bank_account = bank_account
        self.amount = 0
        self.fee = 0
        self.bank_account.transactions.append(self)

    # Deposit Funds Method
    def deposit_funds(self):
        return

    # Withdraw Funds Method
    def withdraw_funds(self):
        return

    # Convert Funds Method
    def convert_funds(self):
        return
