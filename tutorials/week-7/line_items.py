def line_calculator():
    print("ENTER ITEMS (ENTER 0 TO END)")

    total = 0.0
    cost = float(input("Cost of item:\t\t\t\t"))

    while cost != 0:
        total += cost
        cost = float(input("Cost of item:\t\t\t\t"))

    print(f"Total:\t\t\t\t\t{round(total, 2)}")

    return round(total, 2)
