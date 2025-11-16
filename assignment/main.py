# from client import
from menu import display_authentication


def main():
    users = []
    display_authentication(users)


if __name__ == "__main__":
    main()

# TODO: [x] Create a User class with name, email and country properties
# TODO: [x] Create a Bank_Account class with id, currencies and balances properties
# TODO: [x] Create a new user and set balances as needed
# TODO: [x] Deposit funds into the appropriate account
# TODO: [x] Transfer and convert funds and deduct fee where appropriate
# TODO: [x] Withdraw funds from an account
# TODO: [x] Include a minimum of 3 available currencies
# TODO: [x] Use table or realtime currency info to convert currencies
# TODO: [x] Project is well-commented
# TODO: [x] Project free of errors and exceptions handled gracefully
# TODO: [x] Match indexes between currencies and balances to maintain a link
# TODO: [x] Add advanced functionality and demonstrate coding skills
# authentication flow, multi-user setup, multiple accounts per user,
# multiple balances per account, multiple transactions per balance, ascii for looks
# datetime stamps for transactions, fake country code + random number for bank account id
