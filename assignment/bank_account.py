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

        # Exception handling loop:
        # https://stackoverflow.com/a/2244307
        while True:
            try:
                # User chooses account type
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

            # Error, print invalid option, and retry if user doesn't choose correctly
            except ValueError:
                pass

            print(
                "\nInvalid option. Please only enter either a 1 for a personal bank account or a 2 for a business bank account."
            )

        # Initialise the account balance to 0
        self.balance = 0.00

        # Dictionary with currencies and their corresponding symbols
        available_currencies = {"€": "eur", "$": "usd", "£": "gbp"}

        # Exception handling loop
        while True:
            try:
                # User chooses account's currency
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

            # Error, print invalid option, and retry if user doesn't choose correctly
            except ValueError:
                pass

            print(
                "\nInvalid option. Please only enter either a 1 for EUR, a 2 for USD, or a 3 for GBP."
            )

        # Loop through currencies and keep track of how many accounts of each
        currency_counter = 0
        for bank_account in self.user.bank_accounts:
            if bank_account.currency == self.currency:
                currency_counter += 1

        # Set account nicknames based on currency
        if currency_counter == 0:
            self.nickname = f"Primary {available_currencies[self.currency].upper()}"
        elif currency_counter == 1:
            self.nickname = f"Secondary {available_currencies[self.currency].upper()}"
        else:
            self.nickname = f"Other {available_currencies[self.currency].upper()}"

        # Add the new account to user's accounts list
        self.user.bank_accounts.append(self)

        # Create an empy transactions list
        self.transactions = []

        # Inform the user of successful account creation and display account details
        print("\nNew account created successfully!")
        self.show_detailed()

    # Show overview of bank account
    def show_overview(self, index=1):
        # Characters used with print statements for design purposes
        print("      _______________________________________________________")

        # Account index is displayed in box in top left corner
        print(f"     | {index} |\t\t\t\t\t\t     |\n     |‾‾‾\t\t\t\t\t\t     |")

        # Account nickname, id and type are displayed near centre of box
        print(f"     |\t    Account Nickname:\t{self.nickname}\t\t     |")
        print(f"     |\t    Account ID:\t\t{self.id}\t     |")
        print(f"     |\t    Account Type:\t{self.type.capitalize()}\t\t     |")

        # Account balance is displayed near centre of box, rounded nicely with .2f:
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

        # Bottom of box design
        print("     |\t\t\t\t\t\t\t     |")
        print("      ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

    # Show details of bank account
    def show_detailed(self):
        # Fancy "Account Details" displayed with nav options at top
        print(ascii.account_details)
        print("[r] Return to Dashboard\t  [l] Log Out\t[x] Exit Program\n")

        # Account box displayed next
        print(" ____________________________________________________________________")

        # Account nickname and options displayed at top of account details box
        print(
            f"| {self.nickname} |\t     [d] Deposit    [w] Withdraw    [t] Transfer     |\n|‾‾‾‾‾‾‾‾‾‾‾‾‾\t\t\t\t\t\t\t     |"
        )

        # Account id, type and balance displayed
        print(f"| Account ID:\t\t{self.id}\t\t\t     |")
        print(f"| Account Type:\t\t{self.type.capitalize()}\t\t\t\t     |")
        # Printing the account balance, rounding nicely with .2f:
        # https://www.datacamp.com/tutorial/python-round-to-two-decimal-places
        if self.balance < 1000:
            print(
                f"| Current Balance:\t{self.currency}{self.balance:.2f}\t\t\t\t\t     |"
            )
        else:
            print(
                f"| Current Balance:\t{self.currency}{self.balance:.2f}\t\t\t\t     |"
            )
        print("|\t\t\t\t\t\t\t\t     |")

        # Account transactions header and transactions displayed
        print("|               |               |               |                    |")
        print("| Date\t\t| Description\t| Amount\t| Balance After\t\t|")
        print(" ---------------|---------------|---------------|--------------------")

        # If there aren't any transactions yet, display that there aren't any
        if not self.transactions:
            print("|\t\t\t\t\t\t\t\t     |")
            print("|\t\t\tNo account activity yet.\t\t     |")
            print("|\t\t\t\t\t\t\t\t     |")
            print(
                " ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾"
            )

        # Display transactions
        else:
            # Reversing the order of transactions to display as expected in account statements:
            # https://stackoverflow.com/a/3940144
            for transaction in reversed(self.transactions):
                # Formatting time as instructed by Python docs:
                # https://docs.python.org/3/library/datetime.html#format-codes
                print(
                    f" {transaction.timestamp.strftime(' %b %d ')}\t| {transaction.type.capitalize()}\t| {self.currency}{transaction.amount:.2f}\t| {self.currency}{transaction.balance_after:.2f}"
                )
                print(
                    " ---------------|---------------|---------------|--------------------"
                )

            # Display end of activity section for nicer box design
            print("|\t\t\tEnd of account activity.\t\t     |")
            print(
                " --------------------------------------------------------------------"
            )

        while True:
            try:
                # Accept a user input on account details page
                account_menu_choice = input("\n")

                # Take user back to dashboard if "r" is entered
                if account_menu_choice.lower() == "r":
                    return

                # Log user out if "l" is entered
                elif account_menu_choice.lower() == "l":
                    print(f"\n{ascii.see_you_soon}")
                    self.user.log_out()
                    return

                # Exit the program if "x" is entered
                elif account_menu_choice.lower() == "x":
                    print(f"\n{ascii.goodbye}\n")
                    raise SystemExit

                # Begin deposit flow if "d" is entered
                elif account_menu_choice.lower() == "d":
                    print(ascii.deposit)
                    print("How much would you like to deposit into your account?\n")
                    # Create a new Transaction() instance with deposit_funds method
                    Transaction(self).deposit_funds()
                    return

                # Begin withdrawal flow if "w" is entered
                elif account_menu_choice.lower() == "w":
                    print(ascii.withdraw)
                    print("How much would you like to withdraw from your account?\n")
                    # Create a new Transaction() instance with withdraw_funds method
                    Transaction(self).withdraw_funds()
                    return

                # Begin transfer flow if "t" is entered
                elif account_menu_choice.lower() == "t":
                    print(ascii.transfer)
                    print("Which account would you like to transfer money into?\n")

                    # Set index and check if user has any other accounts in the system
                    account_index = 1
                    transferable_accounts = []

                    for bank_account in self.user.bank_accounts:
                        if bank_account.id != self.id:
                            # Show the account overview for each account using its account index
                            bank_account.show_overview(account_index)
                            # Add the account to the transferable accounts list
                            transferable_accounts.append(bank_account)
                            account_index += 1

                    # If there are transferable accounts, display them
                    if transferable_accounts:
                        # Loop on exception caused by incorrect user input
                        while True:
                            try:
                                # Accept input for user to choose account to transfer to
                                chosen_bank_account = transferable_accounts[
                                    int(input()) - 1
                                ]

                                # Transfers act as two Transaction() instances
                                # Create a Transaction() instance for the outward transfer
                                outward_transfer = Transaction(self).transfer_funds(
                                    chosen_bank_account
                                )

                                # Create a Transaction() instance for the account receiving the funds and set
                                # properties accordingly
                                inward_transfer = Transaction(chosen_bank_account)
                                inward_transfer.amount = outward_transfer
                                inward_transfer.type = "transfer"
                                inward_transfer.balance_after = (
                                    chosen_bank_account.balance + inward_transfer.amount
                                )
                                chosen_bank_account.balance += inward_transfer.amount

                                return

                            except TypeError:
                                return

                            except (IndexError, ValueError):
                                pass

                            print(
                                "\nThat's not an available account option. The accounts that you can transfer to are:\n"
                            )

                            account_index = 1
                            for transferable_account in transferable_accounts:
                                print(
                                    f"[{account_index}] {transferable_account.nickname}"
                                )
                                account_index += 1

                            print()

                    # Display that there are no currently available accounts for transfer
                    else:
                        print(
                            "      _______________________________________________________"
                        )
                        print("     |\t\t\t\t\t\t\t     |")
                        print("     |\t\tNo available accounts for transfer.\t     |")
                        print("     |\t\tPlease open another account first.\t     |")
                        print("     |\t\t\t\t\t\t\t     |")
                        print(
                            "      ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾"
                        )

                        # Input used to pause program
                        input(
                            "\nEnter any character to return to the dashboard, where you can open another account.\n\n"
                        )

                        # Take the user back to the dashboard
                        return

                else:
                    pass

            # Error, print invalid option, and retry if user doesn't choose correctly
            except ValueError:
                pass

            # Inform user that they've entered an incorrect option and display the valid options
            print("""\nInvalid option. Your options are:

Navigation Options
[r] Return to Dashboard
[l] Log Out
[x] Exit Program

Account Options
[d] Deposit
[w] Withdrawal
[t] Transfer""")
