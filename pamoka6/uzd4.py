contacts = {}

while True:
    action = input("Chooce: Add, Find, Delete, or end:")
    if action.lower() == "add":
        name = input("Enter name:")
        number = input("Enter number:")
        contacts[name] = number
        print(f"contact {name} add.")
        
    elif action.lower() == "find":
        name = input("Enter name to find: ")
        
        if name in contacts:
            print(f"{name} number is: {contacts[name]}")
        else:
            print(f"Contact {name} not found.")

    elif action.lower() == "delete":
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"Contact {name} deleted.")
        else:
            print(f"Contact {name} not found.")

    elif action.lower() == "end":
        print("Ending the program.")
        break
    else:
        print("Invalid option. Please choose Add, Find, Delete, (or 'end'.)")

print ("All contacks:", contacts) 