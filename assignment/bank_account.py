import random

from ascii import Ascii
from transaction import Transaction

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

        # Using this loop for exception handling:
        # https://stackoverflow.com/a/2244307
        while True:
            try:
                type = int(
                    input(
                        "\nWhat type of account would you like to open?\n\n[1] Personal Current Account\n[2] Business Current Account\n\n"
                    )
                )
                if type == 1:
                    self.type = "personal"
                    break
                elif type == 2:
                    self.type = "business"
                    break
            except ValueError:
                pass

            print(
                "\nInvalid option. Please only enter either a 1 for a personal bank account or a 2 for a business bank account."
            )

        self.balance = 0.00
        available_currencies = {"€": "eur", "$": "usd", "£": "gbp"}

        while True:
            try:
                chosen_currency = int(
                    input(
                        f"\nWhat currency would you like this account hold?\n\n[1] {list(available_currencies.keys())[0].upper()} ({list(available_currencies.values())[0].upper()})\n[2] {list(available_currencies.keys())[1].upper()} ({list(available_currencies.values())[1].upper()})\n[3] {list(available_currencies.keys())[2].upper()} ({list(available_currencies.values())[2].upper()})\n\n"
                    )
                )

                if chosen_currency == 1:
                    self.currency = list(available_currencies.keys())[0]
                    break
                elif chosen_currency == 2:
                    self.currency = list(available_currencies.keys())[1]
                    break
                elif chosen_currency == 3:
                    self.currency = list(available_currencies.keys())[2]
                    break

            except ValueError:
                pass

            print(
                "\nInvalid option. Please only enter either a 1 for EUR, a 2 for USD, or a 3 for GBP."
            )

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
        self.show_detailed()

    # Show bank account overview
    def show_overview(self, index=1):
        print("      _______________________________________________________")
        print(f"     | {index} |\t\t\t\t\t\t     |\n     |‾‾‾\t\t\t\t\t\t     |")
        print(f"     |\t    Account Nickname:\t{self.nickname}\t\t     |")
        print(f"     |\t    Account ID:\t\t{self.id}\t     |")
        print(f"     |\t    Account Type:\t{self.type.capitalize()}\t\t     |")
        # Printing the account balance, rounding nicely with .2f:
        # https://www.datacamp.com/tutorial/python-round-to-two-decimal-places
        if self.balance < 1000:
            print(
                f"     |\t    Balance:\t\t{self.currency}{self.balance:.2f}\t\t\t     |"
            )
        elif self.balance >= 1000 and self.balance < 10000000000:
            print(
                f"     |\t    Balance:\t\t{self.currency}{self.balance:.2f}\t\t     |"
            )
        else:
            print(f"     |\t    Balance:\t\t{self.currency}{self.balance:.2f}\t     |")
        print("     |\t\t\t\t\t\t\t     |")
        print("      ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

    def show_detailed(self):
        print(ascii.account_details)
        print("[g] Go to Dashboard\t[l] Log Out\t[x] Exit Program\n")
        print(" _____________________________________________________________________")
        print(
            f"| {self.nickname} |\t\t\t\t\t\t\t      |\n|‾‾‾‾‾‾‾‾‾‾‾‾‾\t\t\t\t\t\t\t      |"
        )
        print(f"| Account ID:\t{self.id}\t\t\t\t      |")
        print(f"| Account Type:\t{self.type.capitalize()}\t\t\t\t\t      |")
        # Printing the account balance, rounding nicely with .2f:
        # https://www.datacamp.com/tutorial/python-round-to-two-decimal-places
        if self.balance < 1000:
            print(f"| Balance:\t{self.currency}{self.balance:.2f}\t\t\t\t\t\t      |")
        else:
            print(f"| Balance:\t{self.currency}{self.balance:.2f}\t\t\t\t\t      |")
        print("|\t\t\t\t\t\t\t\t      |")
        print("|     [d] Deposit           [w] Withdraw           [t] Transfer       |")
        print("|‾‾‾‾‾‾‾‾‾‾‾‾|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|‾‾‾‾‾‾‾‾‾‾|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
        print("| Date\t     | Description\t\t   |  Amount  | Balance After |")
        print("|____________|_____________________________|__________|_______________|")

        if self.transactions:
            for transaction in self.transactions:
                print(
                    f"|{transaction.timestamp.strftime(' %d.%m.%Y ')}| {transaction.type.capitalize()} | {self.currency}{transaction.amount} | {self.currency}{transaction.balance_after} |"
                )

        account_menu_choice = input("\n")

        # Check which choice the user made and proceed accordingly
        if account_menu_choice.lower() == "g":
            # If the user would like to open a new bank account, instantiate the Bank_Account class with user passed in
            return
        elif account_menu_choice.lower() == "l":
            # If the user wants to log out but not end the program, call the user.log_out() method
            print(f"\n{ascii.see_you_soon}")
            self.user.log_out()
            return
        elif account_menu_choice.lower() == "x":
            # If the user would like to exit the program, call the exit() function
            print(f"\n{ascii.goodbye}\n")
            raise SystemExit
        elif account_menu_choice.lower() == "d":
            print(ascii.deposit)
            print("How much would you like to deposit into your account?")
            Transaction(self).deposit_funds()

        elif account_menu_choice.lower() == "w":
            print(ascii.withdraw)
            print("How much would you like to withdraw from your account?")
            Transaction(self).withdraw_funds()
        elif account_menu_choice.lower() == "t":
            print(ascii.transfer)
            print("Which account would you like to transfer money into?")
            account_index = 1
            for bank_account in self.user.bank_accounts:
                if bank_account.id != self.id:
                    bank_account.show_overview(account_index)
                    account_index += 1

            chosen_bank_account = int(input())

            Transaction(self).transfer_funds(chosen_bank_account - 1)

        else:
            return
