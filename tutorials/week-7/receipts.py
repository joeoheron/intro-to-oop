import line_items as li
import sales_tax_calculator as stc


def display_title():
    print("Sales Tax Calculator\n")


def receipt_generator():
    display_title()

    again = "y"

    while again.lower() == "y":
        total = li.line_calculator()

        stc.calculate_tax(total)

        again = input("\nWould you like to go again? (y/n):\t")
        print()

    print("Thanks, bye!")
