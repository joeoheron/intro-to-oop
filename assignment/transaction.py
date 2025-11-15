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
        self.amount = round(float(input(f"{self.bank_account.currency}")), 2)
        self.bank_account.balance += self.amount
        self.balance_after = self.bank_account.balance

    # Withdraw Funds Method
    def withdraw_funds(self):
        self.type = "withdrawal"
        amount = round(float(input(f"{self.bank_account.currency}")), 2)
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

    # Convert Funds Method
    def transfer_funds(self, to_account):
        conversion_rate = {"€": 1, "$": 1.2, "£": 0.8}

        self.type = "transfer"

        chosen_amount = float(
            input(
                f"\nHow much {to_account.currency} would you like to transfer into this account?\n\n{to_account.currency}"
            )
        )

        # Currency conversion flow begins
        if self.bank_account.currency != to_account.currency:
            chosen_amount_in_euro = chosen_amount / conversion_rate[to_account.currency]

            print(f"Chosen amount in euro: {chosen_amount_in_euro}")

            available_balance_in_euro = (
                self.bank_account.balance / conversion_rate[self.bank_account.currency]
            )

            print(f"Available balance in euro: {available_balance_in_euro}")

            while chosen_amount_in_euro >= available_balance_in_euro:
                chosen_amount = round(
                    float(
                        input(
                            f"\nInsufficient funds available. Please enter an amount that your account can cover.\n\n{to_account.currency}"
                        )
                    ),
                    2,
                )

                chosen_amount_in_euro = (
                    chosen_amount * conversion_rate[to_account.currency]
                )

            self.amount = round(-chosen_amount_in_euro, 2)

            self.bank_account.balance += self.amount
            self.balance_after = round(self.bank_account.balance, 2)

            return chosen_amount

        else:
            while chosen_amount > self.bank_account.balance:
                chosen_amount = round(
                    float(
                        input(
                            f"\nInsufficient funds available. Please enter an amount that your account can cover.\n\n{self.bank_account.currency}"
                        )
                    ),
                    2,
                )

            self.amount = -chosen_amount

            self.bank_account.balance += self.amount
            self.balance_after = round(self.bank_account.balance, 2)

            return chosen_amount
