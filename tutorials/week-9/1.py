import prime_numbers as pm


def main():
    again = "y"

    while again.lower() == "y":
        pm.prime_number_checker()

        again = input("\nTry again? (y/n):\t\t\t\t")
        print()

    print("Bye!")


if __name__ == "__main__":
    main()
