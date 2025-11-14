from ascii import Ascii
from bank_account import Bank_Account
from user import User, log_in

# Instantiate the Ascii class for nice design throughout menus
ascii = Ascii()


# Begin with an authentication flow
def display_authentication(users):
    print(ascii.cubs)

    # Currently displays choice, regardless of any users existing or not
    auth_choice = int(
        input(
            f"Welcome to CUBS Banking Limited's online services!\n{ascii.auth}\nPlease log in or register to continue.\n\n[1] Log In\n[2] Register\n\n"
        )
    )

    # If the user chooses to log in, start the flow
    if auth_choice == 1:
        print(f"{ascii.log_in}\nEnter your email and password to log in.")

        # Input user credentials
        email = input("\nPlease enter your email address:\t")
        password = input("Please enter your password:\t\t")

        # Set the user object to be the returned user from log in function
        user = log_in(email, password, users)

        # Display the main dashboard to the user, passing in the logged in user and the users list
        display_dashboard(user, users)

    # If the user chooses to register a new account, start the flow
    elif auth_choice == 2:
        print(
            f"{ascii.register}\nPlease provide your name, email and a unique password to create an account."
        )

        # Create a new user
        new_user = User()

        # Add the new user to the list of app's users
        users.append(new_user)

        # Prompt the user for beginning their journey by opening a bank account
        open_bank_account_choice = int(
            input(
                "Would you like to get started by opening a bank account with CUBS Banking Limited?\n\n[1] Yes\n[2] No\n\n"
            )
        )

        # If the user would like to open a new bank account, start the flow
        if open_bank_account_choice == 1:
            # Create a new bank account for this new user
            Bank_Account(new_user)

            # Send the user to the dashboard when done creating a bank account
            display_dashboard(new_user, users)

        # If the user does not want to open an account yet, send them straight to the dashboard
        elif open_bank_account_choice == 2:
            display_dashboard(new_user, users)

    # except:
    #     print("Invalid choice. Please try again.")


# Display the main
def display_dashboard(user, users):
    # Only display the menu options if there's an active user session
    while user.session:
        print(
            "\n======================================================================"
        )
        print(ascii.cubs)
        print(ascii.dashboard)
        print("[n] Open a New Bank Account\t[l] Log Out\t[x] Exit Program")
        print(ascii.my_accounts)
        print("Enter account's corner number to perform account-specific operations.")
        user.show_bank_accounts()
        main_menu_choice = input()

        # Use an input() for the user to choose an action they'd like to perform

        # Check which choice the user made and proceed accordingly
        if (
            main_menu_choice.lower() == "n"
            or main_menu_choice.lower() == "l"
            or main_menu_choice.lower() == "x"
        ):
            if main_menu_choice.lower() == "n":
                # If the user would like to open a new bank account, instantiate the Bank_Account class with user passed in
                Bank_Account(user)
            elif main_menu_choice.lower() == "l":
                # If the user wants to log out but not end the program, call the user.log_out() method
                print(f"{ascii.see_you_soon}")
                user.log_out()
                # display_authentication(users)
            elif main_menu_choice.lower() == "x":
                # If the user would like to exit the program, call the exit() function
                print(f"\n{ascii.goodbye}\n")
                exit()
            else:
                return
        else:
            main_menu_choice = int(main_menu_choice)
            user.bank_accounts[main_menu_choice - 1].perform_actions()

    else:
        print(
            "\n======================================================================"
        )
        display_authentication(users)
