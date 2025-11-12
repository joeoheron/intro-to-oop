import random


# User Class
class User:
    # The constructor for the User class
    def __init__(self):
        # Found this idea for a random number at a specified digit length here: https://python-forum.io/thread-27756.html
        self.id = format(random.randint(0, 9999999999999999), "016d")

        # The user's name, email, password and country are all inputted by them at time of registration
        self.name = input("\nPlease type your name:\t\t\t")
        self.email = input("Please type your email address:\t\t")
        self.password = input("Please type a password:\t\t\t")
        self.country = ""

        # The user should automatically be logged in upon registration
        self.session = True

        # The user can have multiple bank accounts, but starts without any
        self.bank_accounts = []

        # Upon successful registration, we let the user know
        print(
            "\nRegistration successful! You can now use CUBS Banking's online services.\n"
        )

        # log_in(self.email, self.password)

    # Log Out User
    def log_out(self):
        self.session = False

    # Show Bank Accounts Method
    def show_user_bank_accounts(self):
        account_index = 0
        for bank_account in self.bank_accounts:
            account_index += 1
            print(f"[{account_index}] Account ID: {bank_account.id}")

        chosen_account = int(input("\nWhich account would you like to work with?"))

        if chosen_account == account_index:
            print(f"Account Balance: {bank_account.balance}")


def log_in(email, password, users=[]):
    if email and password:
        for user in users:
            while email != user.email:
                print("\nNo user found. Are you sure you've entered the right email?")
                user.session = False
                email = input("\nPlease enter your email address:\t")
                password = input("Please enter your password:\t\t")

            else:
                while password != user.password:
                    user.session = False
                    password = input("\nIncorrect password. Please try again:\t")
                else:
                    print(f"\nLogged in successfully.\n\nWelcome back, {user.name}")
                    user.session = True
                    return user
