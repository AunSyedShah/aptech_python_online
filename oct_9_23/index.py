import sqlite3

conn = sqlite3.connect('students.sqlite3') # step 1 - connect to database
curr = conn.cursor() # step 2 - get cursor to execute queries
# contacts table
curr.execute("create table if not exists contacts (name text, phone text)") # step 3 - create table

while True:
    print("Welcome to the contacts app")
    print("1. Add a contact")
    print("2. View all contacts")
    print("3. Delete a contact")
    print("4. Update a contact")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        curr.execute("insert into contacts values (?, ?)", (name, phone))
        conn.commit()
        print("Contact added successfully")
    elif choice == "2":
        results = curr.execute("select * from contacts")
        for result in results:
            print(result)
    elif choice == "3":
        name = input("Enter name: ")
        curr.execute("delete from contacts where name = ?", (name,))
        conn.commit()
        print("Contact deleted successfully")
    elif choice == "4":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        curr.execute("update contacts set phone = ? where name = ?", (phone, name))
        conn.commit()
        print("Contact updated successfully")
    elif choice == "5":
        conn.close()
        break