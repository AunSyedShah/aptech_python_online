import sqlite3

conn = sqlite3.connect('students.sqlite3')
curr = conn.cursor()
# contacts table
curr.execute("create table if not exists contacts (name text, phone text)")

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
        results = results.fetchall()
        print("Name\tPhone")
        for result in results:
            print(result)
    elif choice == "5":
        conn.close()
        break