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
    def transfer_funds(self, target_account):
        conversion_rate = {"€": 1, "$": 1.1, "£": 0.9}
        fee_rate = ""
        conversion_fee = 0

        self.type = "transfer"

        target_amount = float(
            input(
                f"\nHow much {target_account.currency} would you like to transfer into this account?\n\n{target_account.currency}"
            )
        )

        # Currency conversion flow begins
        while self.bank_account.currency != target_account.currency:
            target_amount_in_euro = (
                target_amount / conversion_rate[target_account.currency]
            )

            available_balance_in_euro = (
                self.bank_account.balance / conversion_rate[self.bank_account.currency]
            )

            deducted_amount = (
                target_amount_in_euro * conversion_rate[self.bank_account.currency]
            )

            if deducted_amount < 100:
                fee_rate = "1%"
                conversion_fee = deducted_amount * 0.01
            elif deducted_amount >= 100 and deducted_amount < 500:
                fee_rate = "2%"
                conversion_fee = deducted_amount * 0.02
            else:
                fee_rate = "3%"
                conversion_fee = deducted_amount * 0.03

            deducted_amount += conversion_fee

            if deducted_amount >= available_balance_in_euro:
                target_amount = float(
                    input(
                        f"\nInsufficient funds available. Please enter an amount that your account can cover.\n\n{target_account.currency}"
                    )
                )

                continue

            proceed_choice = int(
                input(
                    f"A {fee_rate} currency conversion fee of {self.bank_account.currency}{'{:,.2f}'.format(conversion_fee)} will be applied to this transfer.\nA total of {self.bank_account.currency}{'{:,.2f}'.format(deducted_amount)} would be charged to your account.\n\nWould you like to proceed?\n\n[1] Yes\n[2] No\n\n"
                )
            )

            if proceed_choice == 1:
                self.amount = round(-deducted_amount, 2)

                self.bank_account.balance += self.amount
                self.balance_after = round(self.bank_account.balance, 2)

                return target_amount

            else:
                print("Cancelling transaction...")
                break

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
