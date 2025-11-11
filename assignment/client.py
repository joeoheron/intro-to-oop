from account import Account


# Client Class
class Client:
    def __init__(self):
        self.name = ""
        self.email = ""
        self.password = ""
        self.country = ""
        self.accounts = [Account]

    # Create User Method
    def create_user(self):
        self.name = input("Please type your name:\t\t\t")
        self.email = input("Please type your email address:\t\t")
        self.password = input("Please type a password:\t\t\t")
        print(f"Hi {self.name}, welcome to CUBS Banking!")

    # Log In User
    def log_in(self):
        return

    # Log Out User
    def log_out(self):
        return

    # Show Account Balances Method
    def show_account_balances(self):
        return
