import random

from ascii import Ascii

ascii = Ascii()


# Account Class
class Bank_Account:
    def __init__(self, user):
        # Found this idea for a random number at a specified digit length here:
        # https://python-forum.io/thread-27756.html
        # Combined string array knowledge gained here:
        # https://www.w3schools.com/python/python_strings.asp
        self.id = f"{user.country[0:2].upper()}{format(random.randint(0, 99999999999999), '014d')}"
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

        self.balance = 0.00
        available_currencies = {"€": "eur", "$": "usd", "£": "gbp"}
        chosen_currency = int(
            input(
                f"\nWhat currency would you like this account hold?\n\n[1] {list(available_currencies.keys())[0].upper()} ({list(available_currencies.values())[0].upper()})\n[2] {list(available_currencies.keys())[1].upper()} ({list(available_currencies.values())[1].upper()})\n[3] {list(available_currencies.keys())[2].upper()} ({list(available_currencies.values())[2].upper()})\n\n"
            )
        )

        if chosen_currency == 1:
            self.currency = list(available_currencies.keys())[0]
        elif chosen_currency == 2:
            self.currency = list(available_currencies.keys())[1]
        elif chosen_currency == 3:
            self.currency = list(available_currencies.keys())[2]

        currency_counter = 0
        for bank_account in self.user.bank_accounts:
            if bank_account.currency == self.currency:
                currency_counter += 1

        if currency_counter == 0:
            self.nickname = f"Primary {available_currencies[self.currency].upper()}"
        elif currency_counter == 1:
            self.nickname = f"Secondary {available_currencies[self.currency].upper()}"
        else:
            self.nickname = f"Other {available_currencies[self.currency].upper()}"

        self.user.bank_accounts.append(self)
        self.transactions = []

        print("\nNew account created successfully!\n")
        self.show_overview()

    # Show bank account overview
    def show_overview(self, index=1):
        print("\t _______________________________________________________")
        print(f"\t| {index} |\t\t\t\t\t\t\t|\n\t|‾‾‾\t\t\t\t\t\t\t|")
        print(f"\t|\tAccount Nickname:\t{self.nickname}\t\t|")
        print(f"\t|\tAccount ID:\t\t{self.id}\t|")
        print(f"\t|\tAccount Type:\t\t{self.type.capitalize()}\t\t|")
        # Printing the account balance, rounding nicely with .2f:
        # https://www.datacamp.com/tutorial/python-round-to-two-decimal-places
        if self.balance < 1000:
            print(f"\t|\tBalance:\t\t{self.currency}{self.balance:.2f}\t\t\t|")
        elif self.balance >= 1000 and self.balance < 10000000000:
            print(f"\t|\tBalance:\t\t{self.currency}{self.balance:.2f}\t\t|")
        else:
            print(f"\t|\tBalance:\t\t{self.currency}{self.balance:.2f}\t|")
        print("\t|\t\t\t\t\t\t\t|")
        print("\t ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

    def perform_actions(self):
        print(ascii.account)
        print("[d] Return to Dashboard\t\t[l] Log Out\t[x] Exit Program\n")

        account_menu_choice = input()

        # Check which choice the user made and proceed accordingly
        if (
            account_menu_choice.lower() == "r"
            or account_menu_choice.lower() == "l"
            or account_menu_choice.lower() == "x"
        ):
            if account_menu_choice.lower() == "r":
                # If the user would like to open a new bank account, instantiate the Bank_Account class with user passed in
                return
            elif account_menu_choice.lower() == "l":
                # If the user wants to log out but not end the program, call the user.log_out() method
                print(f"\n{ascii.see_you_soon}")
                self.user.log_out()
            elif account_menu_choice.lower() == "x":
                # If the user would like to exit the program, call the exit() function
                print(f"\n{ascii.goodbye}\n")
                exit()
            else:
                return
        else:
            account_menu_choice = int(account_menu_choice)
