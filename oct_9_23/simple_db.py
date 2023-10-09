import sqlite3

conn = sqlite3.connect('contacts.sqlite3') # step 1 - connect to database
curr = conn.cursor() # step 2 - get cursor to execute queries
# contacts table
curr.execute("create table if not exists contacts (name text, phone text)") # step 3 - create table
curr.commit()
# insert into contacts
curr.execute("insert into contacts values ('John', '1234567890')")
curr.commit()
# select from contacts
results = curr.execute("select * from contacts")
results = results.fetchall()
print(results)