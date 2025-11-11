def command_menu():
    print(
        "\nCOMMAND MENU\nshow - Show all items\ngrab - Grab an item\nedit - Edit an item\ndrop - Drop an item\nexit - Exit program"
    )


def show_items(items):
    for item in items:
        print(f"{items.index(item) + 1}. {item}")


def grab_item(items):
    if len(items) >= 4:
        print("You can't carry any more items. Drop something first.")
    else:
        new_item = input("\nName: ")
        items.append(new_item)
        print(f"\n{new_item} was added.\n")


def edit_item(items):
    item_number = int(input("Number: "))
    for item in items:
        if item_number - 1 == items.index(item):
            index = items.index(item)
            print(f"Editing item {item} at {index}")
            items[index] = input(f"Updated name: ")
            print(f"Item number {index + 1} was updated.")


def drop_item(items):
    item_number = int(input("Number: "))
    for item in items:
        if item_number - 1 == items.index(item):
            items.remove(item)
            print(f"{item} was dropped.")
