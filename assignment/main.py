# from client import
from menu import display_authentication


def main():
    users = []
    display_authentication(users)


if __name__ == "__main__":
    main()

# TODO: Create a User class with name, email and country properties [x]
# TODO: Create a Bank_Account class with id, currencies and balances properties [x]
# TODO: Create a new user and set balances as needed [x]
# TODO: Deposit funds into the appropriate account []
# TODO: Convert funds in an account and deduct fee where appropriate []
# TODO: Withdraw funds from an account []
# TODO: Include a minimum of 3 available currencies [x]
# TODO: Use table or realtime currency info to convert currencies []
# TODO: Project is well-commented []
# TODO: Project free of errors and exceptions handled gracefully []
# TODO: Match indexes between currencies and balances to maintain a link [x]
# TODO: Add advanced functionality and demonstrate coding skills
# authentication flow, multi-user setup, multiple accounts per user,
# multiple balances per account, multiple transactions per balance, ascii for looks
