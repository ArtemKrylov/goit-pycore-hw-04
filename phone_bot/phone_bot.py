from colorama import Fore, just_fix_windows_console


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact {Fore.BLUE}{name}{Fore.RESET} added."


def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact {Fore.BLUE}{name}{Fore.RESET} updated."


def show_contact(name, contacts):
    if not contacts.get(name):
        return f"Contact {Fore.BLUE}{name}{Fore.RESET} does not exist."

    return f"{Fore.BLUE}{name}: {Fore.GREEN}{contacts[name]}{Fore.RESET}"


def show_all_contacts(contacts):
    showing_contacts = "Phonebook:\n"
    for name, phone in contacts.items():
        showing_contacts += f"{Fore.BLUE}{name}: {Fore.GREEN}{phone}{Fore.RESET}\n"
    return showing_contacts


def main():

    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ")
        except KeyboardInterrupt:
            print("\nGood bye!")
            break

        if not user_input or not user_input.strip():
            continue

        command, *args = parse_input(user_input)

        match command:
            case "hello":
                print("How can I help you?")
            case "add":
                if not args or len(args) != 2:
                    print("Please provide a name and phone number.")
                    continue
                if contacts.get(args[0]):
                    print("Contact already exists. Rewrite it? (y/n): ")
                    if input().lower() == "y":
                        print(change_contact(args, contacts))
                    else:
                        print("Contact not updated.")
                else:
                    print(add_contact(args, contacts))
            case "change":
                if not args or len(args) != 2:
                    print("Please provide a name and phone number.")
                    continue
                if not contacts.get(args[0]):
                    print("Contact does not exist. Add it? (y/n): ")
                    if input().lower() == "y":
                        print(add_contact(args, contacts))
                    else:
                        print("Contact not added.")
                else:
                    print(change_contact(args, contacts))
            case "phone":
                if not args or len(args) != 1:
                    print("Please provide a name.")
                    continue
                name = args[0]
                print(show_contact(name, contacts))
            case "all":
                if not contacts or len(contacts.items()) == 0:
                    print("No contacts found.")
                    continue
                print(show_all_contacts(contacts))
            case "close" | "exit":
                print("Good bye!")
                break
            case _:
                print("Unknown command")


if __name__ == "__main__":
    just_fix_windows_console()
    main()
