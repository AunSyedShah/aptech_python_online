import os

contacts = {}
while True:
    print("1. Add/Update Contact")
    print("2. View Contact")
    print("3. Delete Contact")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        contact_name = input("Enter Contact Name: ")
        contact_number = input("Enter Contact Number: ")
        contacts[contact_name] = contact_number
        print("Contact Added Successfully")
    elif choice == "2":
        print("Contact Name\tContact Number")
        # display dictionary
        for k, v in contacts.items():
            print(k, v)
    elif choice == "3":
        contact_name = input("Enter Contact Name: ")
        if contact_name in contacts:
            del contacts[contact_name]
            print("Contact Deleted Successfully")
        else:
            print("Contact Not Found")
    elif choice == "4":
        break
