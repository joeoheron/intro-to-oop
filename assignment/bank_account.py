import random


# Account Class
class Bank_Account:
    def __init__(self, client):
        # Found this idea for a random number at a specified digit length here: https://python-forum.io/thread-27756.html
        self.id = format(random.randint(0, 9999999999999999), "016d")
        self.client = client
        self.type = ""
        self.balances = []
        self.currencies = []
        self.client.bank_accounts.append(self)
        self.transactions = []
        self.show_details()

    # Open Individual Account Method
    # def open_individual_account(self):
    # Found this idea for a random number at a specified digit length here: https://python-forum.io/thread-27756.html
    # self.id = format(random.randint(0, 9999999999999999), "016d")
    # self.client.bank_accounts.insert(0, self)
    # self.show_details()
    # return

    # Open Business Account
    # def open_business_account(self):
    #     return

    # Show Balance Method
    def show_details(self):
        print(self.id)
        return
