from client import Client


def display_menu():
    client = Client()

    # If no bank accounts exist, then we need to start by creating a user
    if not client.bank_accounts:
        print("""
      ___ _   _ ___ ___   ___            _   _
     / __| | | | _ ) __| | _ ) __ _ _ _ | |_(_)_ _  __ _
    | (__| |_| | _ \\__ \\ | _ \\/ _` | ' \\| / / | ' \\/ _` |
     \\___|\\___/|___/___/ |___/\\__,_|_||_|_\\_\\_|_||_\\__, |
                                                   |___/
            """)
        print(
            "Welcome to CUBS Banking Limited's online services!\n\nLet's get you started by creating an account...\n"
        )

        client = Client()
        client.create_user()

        create_account_choice = int(
            input(
                "\nWould you like to get started by creating an account?\n\n[1] Yes\n[2] No\n\n"
            )
        )

        if create_account_choice == 1:
            print("\nGreat")
    else:
        client.log_in()
