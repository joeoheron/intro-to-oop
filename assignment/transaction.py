import datetime

from ascii import Ascii

ascii = Ascii()


class Transaction:
    # The constructor for the Transaction class
    def __init__(self, bank_account):
        # Date and time for when a transaction is created
        self.timestamp = datetime.datetime.now()
        # Bank account associated with a transaction
        self.bank_account = bank_account
        # The type of transaction: transfer, withdrawal or deposit
        self.type = ""
        # The amount of a transaction
        self.amount = 0.0
        # The balance 'stamp' after making a transaction
        self.balance_after = 0.0
        # Add the transaction to the list of transactions associated with a bank account
        self.bank_account.transactions.append(self)

    # Deposit Funds Method
    def deposit_funds(self):
        # Loop to handle exception by incorrect input
        while True:
            try:
                self.type = "deposit"
                self.amount = float(input(self.bank_account.currency))
                self.bank_account.balance += self.amount
                self.balance_after = self.bank_account.balance

                return

            # Handle exception if float isn't entered and inform user to retry
            except ValueError:
                pass

            print(
                "\nThat's not a valid amount. Please enter a valid financial amount.\n"
            )

    # Withdraw Funds Method
    def withdraw_funds(self):
        # Loop to handle exception by incorrect input
        while True:
            try:
                self.type = "withdrawal"
                amount = float(input(self.bank_account.currency))
                # Check if the bank account has enough funds to withdraw the desired amount
                while amount > self.bank_account.balance:
                    amount = round(
                        float(
                            input(
                                f"\nInsufficient funds available. Please enter an amount that your account can cover.\n\n{self.bank_account.currency}"
                            )
                        ),
                        2,
                    )

                self.amount = -amount
                self.bank_account.balance += self.amount
                self.balance_after = self.bank_account.balance

                return

            # Handle exception if float isn't entered and inform user to retry
            except ValueError:
                pass

            print(
                "\nThat's not a valid amount. Please enter a valid financial amount.\n"
            )

    # Convert Funds Method
    def transfer_funds(self, target_account):
        # Dictionary of conversion rates to a base currency of Euro
        conversion_rate = {"€": 1, "$": 1.1, "£": 0.9}
        # Empty fee rate variable initialised
        fee_rate = ""
        # Conversion fee of 0 initialised
        conversion_fee = 0

        self.type = "transfer"

        # Ask user how much of the target currency they'd like to transfer to the target account
        target_amount = float(
            input(
                f"\nHow much {target_account.currency} would you like to transfer into this account?\n\n{target_account.currency}"
            )
        )

        # Currency conversion flow begins
        while self.bank_account.currency != target_account.currency:
            # Convert the targeted amount to Euro, using the dictionary above
            target_amount_in_euro = (
                target_amount / conversion_rate[target_account.currency]
            )

            # Convert amount deducted from transfering account in its own currency
            deducted_amount = (
                target_amount_in_euro * conversion_rate[self.bank_account.currency]
            )

            # Check the value of the deducted amount and apply fee brackets
            if deducted_amount < 100:
                fee_rate = "1%"
                conversion_fee = deducted_amount * 0.01
            elif deducted_amount >= 100 and deducted_amount < 500:
                fee_rate = "2%"
                conversion_fee = deducted_amount * 0.02
            else:
                fee_rate = "3%"
                conversion_fee = deducted_amount * 0.03

            # Deducted amount with appropriate conversion fee
            deducted_amount += conversion_fee

            # Check if the amount deducted will overdraw account and reprompt if so
            if deducted_amount >= self.bank_account.balance:
                target_amount = float(
                    input(
                        f"\nInsufficient funds available. Please enter an amount that your account can cover.\n\n{target_account.currency}"
                    )
                )

                continue

            # Loop to handle exceptions from incorrect user input
            while True:
                try:
                    # Provide user with fee info and choice to proceed with transaction or not
                    proceed_choice = int(
                        input(
                            f"A {fee_rate} currency conversion fee of {self.bank_account.currency}{'{:,.2f}'.format(conversion_fee)} will be applied to this transfer.\nA total of {self.bank_account.currency}{'{:,.2f}'.format(deducted_amount)} would be charged to your account.\n\nWould you like to proceed?\n\n[1] Yes\n[2] No\n\n"
                        )
                    )

                    # Process transfer if the user chooses yes
                    if proceed_choice == 1:
                        self.amount = round(-deducted_amount, 2)

                        self.bank_account.balance += self.amount
                        self.balance_after = round(self.bank_account.balance, 2)

                        return target_amount

                    # Return a zeroed out transaction if the user chooses no
                    else:
                        print("Cancelling transaction...")

                        return 0

                except:
                    pass

        # If the currencies are the same, check that the transfering account has sufficient
        # balance to complete transfer and process transfer accordingly.
        else:
            while target_amount > self.bank_account.balance:
                target_amount = float(
                    input(
                        f"\nInsufficient funds available. Please enter an amount that your account can cover.\n\n{self.bank_account.currency}"
                    )
                )

            self.amount = -target_amount

            self.bank_account.balance += self.amount
            self.balance_after = round(self.bank_account.balance, 2)

            return target_amount
