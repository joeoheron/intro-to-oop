import random

LIMIT = 6


def roll_die():
    roll = random.randint(1, LIMIT)

    return roll


def roll_dice():
    die_1 = roll_die()
    die_2 = roll_die()

    print(f"Die 1:\t{die_1}")
    print(f"Die 2:\t{die_2}")


def main():
    roll_dice()


if __name__ == "__main__":
    main()
