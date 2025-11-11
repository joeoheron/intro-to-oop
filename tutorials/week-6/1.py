print("Letter Grade Converter")


def calculate_grade():
    choice = "y"

    while choice.lower() == "y":
        num_grade = float(input("\nEnter numerical grade: "))

        letter_grade = ""

        if num_grade >= 88 and num_grade <= 100:
            letter_grade = "A"
        elif num_grade >= 80:
            letter_grade = "B"
        elif num_grade >= 67:
            letter_grade = "C"
        elif num_grade >= 60:
            letter_grade = "D"
        else:
            letter_grade = "F"

        print("Letter grade:", letter_grade)

        choice = input("\nContinue? (y/n): ")

    print("\nBye!")


print(calculate_grade())
