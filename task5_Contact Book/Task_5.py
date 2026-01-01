Contacts = {}

while True:
    print("\nContact Book")
    print("1.Add Contact")
    print("2.View Contact")
    print("3.Update Contact")
    print("4.Delete Contact")
    print("5.Search Contact")
    print("6.View All Contacts")
    print("7.Exit")

    try:
     choice = int(input("Enter Your Choice: "))
    except ValueError:
        print("Please enter a number!")
        continue

    if choice == 1:
        name = input("Enter name: ")
        if name in Contacts:
            print(f"{name} exists in Contacts")

        else:
            age = int(input("Enter Your Age: "))
            phone = input("Enter Phone Number: ")
            email = input("Enter Email Address: ")
            address = input("Enter Address: ")
            Contacts[name] = {"Age": int(age), "Phone Number": phone, "Email":email , "Address":address}
            print(f"{name} has been added!")

    elif choice == 2:
        sContact = input("Enter Contact name: ")
        if sContact in Contacts:
            contact = Contacts[sContact]
            print(f"\nName: {sContact}")
            print(f"Age: {contact['Age']}")
            print(f"Phone Number: {contact['Phone Number']}")
            print(f"Email Address: {contact['Email']}")
            print(f"Address: {contact['Address']}")

        else:
            print("Contact not found!")

    elif choice == 3:
        name = input("Enter name to update Contact =")
        if name in Contacts:
            age = int(input("Enter Your Age: "))
            phone = input("Enter Phone Number: ")
            email = input("Enter Email Address: ")
            address = input("Enter Address: ")
            Contacts[name] = {"Age": int(age), "Phone Number": phone , "Email":email , "Address":address}
        else:
            print("Contact not found!")

    elif choice == 4:
        name = input("Enter contact name to be deleted =")
        if name in Contacts:
            del Contacts[name]
            print(f"{name} has be deleted! ")
        else:
            print("Contact not found!")
    elif choice == 5:
        searchname = input("Enter contact name to search = ")
        found = False
        for name, contact in Contacts.items():
            if searchname.lower() in name.lower():
                print(f"Name = {name}, Age = {contact['Age']} , Phone = {contact['Phone Number']}")

                found = True
        if not found:
            print("No Conatct Found! ")

    elif choice == 6:
        if not Contacts:
            print("No contacts available.")
        else:
            for name, contact in Contacts.items():
                print(f"{name} - {contact['Phone Number']}")

    
    elif choice == 7:
        print("Goodbye.. Have a Good Day!")
        break

    else:
        print("Invalid choice!")



    
