from ascii import Ascii
from bank_account import Bank_Account
from user import User, log_in

ascii = Ascii()


def display_authentication(users):
    print(ascii.cubs)

    auth_choice = int(
        input(
            f"Welcome to CUBS Banking Limited's online services!\n{ascii.auth}\nPlease log in or register to continue.\n\n[1] Log In\n[2] Register\n\n"
        )
    )

    # try:
    if auth_choice == 1:
        print(f"{ascii.log_in}\nEnter your email and password to log in.")
        email = input("\nPlease enter your email address:\t")
        password = input("Please enter your password:\t\t")

        user = log_in(email, password, users)

        display_dashboard(user, users)

    elif auth_choice == 2:
        print(
            f"{ascii.register}\nPlease provide your name, email and a unique password to create an account."
        )

        new_user = User()
        users.append(new_user)

        open_bank_account_choice = int(
            input(
                "Would you like to get started by opening a bank account with CUBS Banking Limited?\n\n[1] Yes\n[2] No\n\n"
            )
        )

        if open_bank_account_choice == 1:
            Bank_Account(new_user)

            display_dashboard(new_user, users)
        elif open_bank_account_choice == 2:
            display_dashboard(new_user, users)
    # except:
    #     print("Invalid choice. Please try again.")


def display_dashboard(user, users):
    print(f"{ascii.dashboard}\nHow can we help you today?")

    while user.session:
        main_menu_choice = int(
            input(
                "\n[1] Show My Bank Accounts\n[2] Open a New Bank Account\n[3] Log Out\n[4] Exit Program\n\n"
            )
        )
        print()

        if main_menu_choice == 1:
            user.show_user_bank_accounts()
            print("\nIs there anything else that we can help you with today?")
        elif main_menu_choice == 2:
            Bank_Account(user)
            print("\nIs there anything else that we can help you with today?")
        elif main_menu_choice == 3:
            print(ascii.goodbye)
            user.log_out()
            display_authentication(users)
        elif main_menu_choice == 4:
            exit()
        else:
            return
