import inventory as inventory


def main():
    print("\nThe Wizard Inventory Program\n\n")

    inventory.command_menu()
    items = []

    while True:
        command = input("\nCommand: ")
        if command == "exit":
            break
        elif command == "show":
            inventory.show_items(items)
        elif command == "grab":
            inventory.grab_item(items)
        elif command == "edit"
            inventory.edit_item(items)
        elif command == "drop":
            inventory.drop_item(items)
        else:
            print("Please provide a valid command.")

    print("Bye!")


if __name__ == "__main__":
    main()
