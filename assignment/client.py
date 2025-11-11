from bank_account import Bank_Account


# Client Class
class Client:
    def __init__(self):
        self.name = ""
        self.email = ""
        self.password = ""
        self.country = ""
        self.session = False
        self.bank_accounts = []

    # Create User Method
    def create_user(self):
        self.name = input("Please type your name:\t\t\t")
        self.email = input("Please type your email address:\t\t")
        self.password = input("Please type a password:\t\t\t")
        print("\nYou've successfully created an account!\n")
        self.log_in()

    # Log In User
    def log_in(self):
        if self.email and self.password:
            self.session = True
            print(f"Hi {self.name}, welcome to CUBS Banking!")
        else:
            email = input("Please enter your email address:")
            if self.email == email:
                print("User found. Checking your password.")
            else:
                print("No user found. Are you sure you've entered the right email?")
            password = input("Please enter your password:")
            if self.password == password:
                self.session = True
                print("Logging you in...")
            else:
                print("Incorrect password. Please try again.")

    # Log Out User
    def log_out(self):
        return

    # Show Account Balances Method
    def show_account_balances(self):
        return
