def hike_calculator(miles: float):
    return int(miles * 5280)


def main():
    print("Hike Calculator\n")

    miles = float(input("How many miles did you walk?\t"))

    feet = hike_calculator(miles)

    print(f"\nYou walked {feet} feet.")


if __name__ == "__main__":
    main()
