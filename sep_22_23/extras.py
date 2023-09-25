import os
contact_list = []

while True:
    os.system("cls")
    print("Welcome to Contact List App")
    print("=====================================")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Delete Contact")
    choice = input("Enter your choice: ")
    if choice == '1':
        os.system("cls")
        print("Please use this format: 'Name - Contact Number'")
        user_detail = input("Enter Your Name and Contact Number: ")
        # check if user_detail is empty
        if user_detail == "":
            print("Please Enter Some Value")
            os.system("pause")
            continue
        contact_list.append(user_detail)
        print("Contact Added Successfully")
        os.system("pause")
    if choice == '2':
        os.system("cls")
        if contact_list == []:
            print("No Contact Found")
        else:
            for contact in contact_list:
                print(contact)
        os.system("pause")
    if choice == '3':
        contact_number = input("Enter Contact Number To Delete: ")
        for i in contact_list:
            if contact_number in i:
                contact_list.remove(i)
                print("Contact Deleted Successfully")
        os.system("pause")