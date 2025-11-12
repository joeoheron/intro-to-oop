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
        # This desired currencies setup is proving to be some of the most difficult logic to me so far.
        available_currencies = {1: "EUR (€)", 2: "USD ($)", 3: "GBP (£)"}
        self.currencies = {}
        primary_currency = int(
            input(
                f"\nWhat will be the primary currency for this account?\n\n[1] {available_currencies[1]}\n[2] {available_currencies[2]}\n[3] {available_currencies[3]}\n\n"
            )
        )
        if primary_currency == 1:
            self.currencies.update({1: "EUR"})
        elif primary_currency == 2:
            self.currencies.update({2: "USD"})
        elif primary_currency == 3:
            self.currencies.update({3: "GBP"})
        add_another_currency = True
        while add_another_currency:
            add_another_currency = int(
                input(
                    "\nWould you like to add another currency to your account?\n\n[1] Yes\n[2] No\n\n"
                )
            )
            if add_another_currency == 1:
                # Found this way to compare two dictionaries here: https://stackoverflow.com/a/32815681
                still_available_currencies = {
                    currency_key: available_currencies[currency_key]
                    for currency_key in set(available_currencies) - set(self.currencies)
                }
                if not still_available_currencies:
                    print(
                        "\nYou already hold balances for the available currency options for your account."
                    )
                else:
                    print(
                        "\nWhich additional currency would you like to add to your account?"
                    )
                    for still_available_currency in still_available_currencies.values():
                        print(f"{still_available_currency}")
                    additional_currency = int(input("\n"))

        self.balances = []
        self.user.bank_accounts.append(self)
        self.transactions = []
        self.show_details()

    # Show Balance Method
    def show_details(self):
        print(self.id)
        return
