import random


# Account Class
class Bank_Account:
    def __init__(self, user):
        # Found this idea for a random number at a specified digit length here: https://python-forum.io/thread-27756.html
        self.id = format(random.randint(0, 9999999999999999), "016d")
        self.user = user
        type = int(
            input(
                "\nWhat type of account would you like to open?\n\n[1] Personal Current Account\n[2] Business Current Account\n\n"
            )
        )
        if type == 1:
            self.type = "personal"
        elif type == 2:
            self.type = "business"
        else:
            print(
                "Invalid option. Please only enter a [1] for a personal account or a [2] for a business account."
            )

        self.balance = 100000.00
        available_currencies = {"eur": "€", "usd": "$", "gbp": "£"}
        chosen_currency = int(
            input(
                f"\nWhat will be the primary currency for this account?\n\n[1] {list(available_currencies.keys())[0].upper()} ({list(available_currencies.values())[0].upper()})\n[2] {list(available_currencies.keys())[1].upper()} ({list(available_currencies.values())[1].upper()})\n[3] {list(available_currencies.keys())[2].upper()} ({list(available_currencies.values())[2].upper()})\n\n"
            )
        )
        if chosen_currency == 1:
            self.currency = list(available_currencies.values())[0]
        elif chosen_currency == 2:
            self.currency = list(available_currencies.values())[1]
        elif chosen_currency == 3:
            self.currency = list(available_currencies.values())[2]

        self.user.bank_accounts.append(self)
        self.transactions = []

        print(
            "\nNew account created successfully!\n\n _______________________________________________"
        )
        print("|\t\t\t\t\t\t|\n|\t\t\t\t\t\t|")
        self.show_overview()
        print("|\t\t\t\t\t\t|\n|\t\t\t\t\t\t|")
        print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

    # Show bank account overview
    def show_overview(self):
        print(f"|\tAccount ID:\t{self.id}\t|")
        # print(f"Account ID: {self.id}") rounding nicely with .2f:
        # https://www.datacamp.com/tutorial/python-round-to-two-decimal-places
        print(f"|\tBalance:\t{self.currency}{self.balance:.2f}\t\t|")
