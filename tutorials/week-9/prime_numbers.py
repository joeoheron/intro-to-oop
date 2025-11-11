def prime_number_checker():
    print("\nPrime Number Checker\n")

    number = int(input("Please enter an integer between 1 and 5000:\t"))
    factors = []

    if number < 1 or number > 5000:
        print("Please enter a valid number.")
    else:
        for i in range(2, int(0.5 * number) + 1):
            if number % i == 0:
                factors.append(i)

    if len(factors) > 0:
        print(f"\n{number} is NOT a prime number.")
        print(f"\nIt has {len(factors)} factors:\t\t\t\t{factors}")
    else:
        print(f"\n{number} is a prime number.")
