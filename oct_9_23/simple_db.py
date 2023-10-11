import sqlite3


# step 1 - create a connection to the database
connection = sqlite3.connect('./oct_9_23/simple_db.sqlite3')
# step 2 - create a cursor object
curr = connection.cursor()
# step 3 - create a table if it doesn't exist
curr.execute("CREATE TABLE IF NOT EXISTS users (NAME TEXT, AGE INT)")
# # step - insert some static data
# curr.execute("INSERT INTO users VALUES ('John', 25)")
# # step - insert some dynamic data
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# curr.execute("INSERT INTO users VALUES (?, ?)", (name, age))
# # step - commit the changes
# connection.commit()
# step - select all the data from the table
result = curr.execute("SELECT * FROM users")
# step - print the result
for row in result:
    print(row)

# step - see specific data
result = curr.execute("SELECT * FROM users WHERE AGE > 30")
for row in result:
    print(row)

# step - update data
curr.execute("UPDATE users SET AGE = 30 WHERE NAME = 'John'")

# step - delete data
curr.execute("DELETE FROM users WHERE NAME = 'John'")

# last step - close the connection
connection.close()