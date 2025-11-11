print("Even or Odd Checker\n")


def even_or_odd_checker():
    choice = int((input("Enter an integer:\t")))

    if choice % 2 == 0:
        print("\nThis is an even number.")
    else:
        print("\nThis is an odd number.")


even_or_odd_checker()
