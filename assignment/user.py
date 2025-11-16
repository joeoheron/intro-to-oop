import random


# User Class
class User:
    # The constructor for the User class
    def __init__(self):
        # Found this idea for a random number at a specified digit length here:
        # https://python-forum.io/thread-27756.html
        self.id = format(random.randint(0, 9999999999999999), "016d")

        # The user's name, email, password and country are all inputted by them at time of registration
        self.name = input("\nPlease enter your name:\t\t\t")
        self.email = input("Please enter your email address:\t")
        self.password = input("Please enter a password:\t\t")
        self.country = input("Please enter your country of residnce:\t")

        # The user should automatically be logged in upon registration
        self.session = True

        # The user can have multiple bank accounts, but starts without any
        self.bank_accounts = []

        # Upon successful registration, we let the user know
        print(
            "\nRegistration successful! You can now use CUBS Banking's online services.\n"
        )

    # Log out the user
    def log_out(self):
        self.session = False

    # Show the user's bank accounts
    def show_bank_accounts(self):
        # Display bank accounts if the user has any
        if self.bank_accounts:
            # Set an index and increment through user's bank accounts, showing them an overview of each
            account_index = 1
            for bank_account in self.bank_accounts:
                bank_account.show_overview(account_index)
                account_index += 1

        # Display that there are no accounts yet if the user doesn't have any
        else:
            print("\n      _______________________________________________________")
            print("     |\t\t\t\t\t\t\t     |")
            print("     |\t\t\tNo open accounts yet.\t\t     |")
            print("     |\t\t\t\t\t\t\t     |")
            print("      ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")


# Define the log in function outside of the User class because if there's no user logged in, we
# wouldn't be able to work with a user instance. Pass in email, password and list of users
# parameters
def log_in(email, password, users=[]):
    # Look over each user in our app's users
    for user in users:
        # If no matching email is found, reprompt the user for an email and password
        while email != user.email:
            print("\nNo user found. Are you sure you've entered the right email?")
            user.session = False
            email = input("\nPlease enter your email address:\t")
            password = input("Please enter your password:\t\t")

        # If an existing user is found, check that the password provided matches
        # that of the existing user's password
        else:
            while password != user.password:
                user.session = False
                password = input("\nIncorrect password. Please try again:\t")
            else:
                print(f"\nLogged in successfully.\n\nWelcome back, {user.name}")
                user.session = True
                return user
