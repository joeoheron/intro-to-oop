import feet_meter_conversions as fmc


def display_title():
    print("Feet and Meters Converter")


def display_menu():
    choice = input(
        "Conversions Menu:\na. Feet to Meters\nb. Meters to Feet\n\nSelect a Conversion (a/b):\t\t"
    )
    return choice


def main():
    display_title()

    again = "y"

    while again.lower() == "y":
        choice = display_menu()

        if choice == "a":
            feet = float(input("\nEnter feet:\t\t\t\t"))
            meters = fmc.feet_to_meters(feet)
            print(f"\n\t\t\t\t\t{meters} meters")

        elif choice == "b":
            meters = float(input("\nEnter meters:\t\t\t\t"))
            feet = fmc.meters_to_feet(meters)
            print(f"\n\t\t\t\t\t{feet} feet")

        else:
            print("You must enter a valid option.")

        again = input("\nWould you like to go again? (y/n):\t")
        print()

    print("Thanks, bye!")


if __name__ == "__main__":
    main()
