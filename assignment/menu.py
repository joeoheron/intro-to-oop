from ascii import Ascii
from bank_account import Bank_Account
from client import Client, log_in

ascii = Ascii()


def display_welcome(clients):
    # If no clients exist yet, then we need to start by creating one
    if not clients:
        # ACSII Art Generated at https://patorjk.com/software/taag
        print(ascii.cubs)
        print(
            "Welcome to CUBS Banking Limited's online services!\n\nLet's get you started by creating an online banking account...\n"
        )

        # Create a new instance of Client() and add it to our list of clients
        client = Client()

        clients.append(client)

        print("Let's get you started by opening a bank account.")

        Bank_Account(client)

        display_main_menu(client, clients)
    else:
        print(ascii.cubs)
        print(
            "Welcome to CUBS Banking Limited's online services!\n\nPlease log in to continue.\n"
        )

        email = input("Please enter your email address:\t")
        password = input("Please enter your password:\t\t")

        client = log_in(email, password, clients)

        display_main_menu(client, clients)


def display_main_menu(client, clients):
    print(f"{ascii.dashboard}\nHow can we help you today?")

    while client.session:
        main_menu_choice = int(
            input(
                "\n[1] Show My Bank Accounts\n[2] Open a New Bank Account\n[3] Log Out\n[4] Exit Program\n\n"
            )
        )
        print()

        if main_menu_choice == 1:
            client.show_user_bank_accounts()
            print("\nIs there anything else that we can help you with today?")
        elif main_menu_choice == 2:
            Bank_Account(client)
            print("\nIs there anything else that we can help you with today?")
        elif main_menu_choice == 3:
            client.log_out()
            display_welcome(clients)
        elif main_menu_choice == 4:
            exit()
        else:
            return
