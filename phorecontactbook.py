contact_book = {}

def contact_logger():
    """Interactive contact logger that stores entries in the module-level contact_book dict."""
    print("----Welcome to the Call Logger----")

    while True:
        phone_number = input("Enter the phone number (or 'q' to quit) ---> ").strip()
        if phone_number.lower() in ("q", "quit", "exit", ""):
            print("Exiting logger.")
            break

        name = input("Enter the name of the contact ---> ").strip()
        if not name:
            print("Name cannot be empty. Try again.")
            continue

        key = name.lower()
        contact_book[key] = {
            "display_name": name,
            "phone": phone_number,
        }

        print(f"successfully saved {phone_number} {name}")

        print("What you'd like to do next?")
        print("would you like to add more number? ----> 1.")
        print("would you like to go to the search by name option? ----> 2.")
        choice = input("what you would like to choose (1. or 2.)? : ").strip()

        if choice == '2':
            break
        elif choice !=1:
             print("invalid input! but i gues you would like to add more number!!")
    

    print("moved toward the search by name option")
    new_input = input("what is the name you looking for? : ").strip()

    if new_input.lower() in contact_book:
        contact = contact_book[new_input.lower()]
        print("found the number!")
        print(f" name: {contact['display_name']}")
        print(f"number: {contact['phone']}")

    else:
        print("you gave an invalid name! name isnt in datalog")



     


        
        
   
    

