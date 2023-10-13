import sys
import tkinter as tk
import sqlite3

conn = sqlite3.connect('students.sqlite3')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS students (name TexT, Phone Text, age INTEGER)")






root = tk.Tk()
def InsertContact():

    c.execute("insert into students (name, Phone, age) values (?, ?, ?) ", (Name_Input.get(), PhoneNumber_Input.get(), Age_Input.get()))
    print("Insert Successfully")
    conn.commit()

def Exit():
    conn.close()
    sys.exit()

def viewrecord():
    results = c.execute(("Select * from students"))
    row = results.fetchall()
    for i in row:
        print(i)
def delete():
    c.execute("delete from students")
    conn.commit()

root.title("This is my first APP")
root.geometry("750x250")

Name = tk.Label(root,text="Name").place(x=40,y=60)
Name_Input = tk.Entry(root,width = 30)
Name_Input.place(x = 110,y = 60)


PhoneNumber = tk.Label(root,text="Phone #").place(x=40,y=100)
PhoneNumber_Input = tk.Entry(root,width = 30)
PhoneNumber_Input.place(x = 110,y = 100)

Age = tk.Label(root,text="Age").place(x=40,y=140)
Age_Input = tk.Entry(root,width = 30)
Age_Input.place(x = 110,y = 140)


submit_button = tk.Button(root,text = "Insert", command=InsertContact).place(x = 110,y = 180)
view_button = tk.Button(root,text = "View", command=viewrecord).place(x = 150,y = 180)
update_button = tk.Button(root,text = "Update").place(x = 190,y = 180)
delete_button = tk.Button(root,text = "Delete", command=delete).place(x = 230,y = 180)
Exit_button = tk.Button(root,text = "Exit", command=Exit).place(x = 280,y = 180)



root.mainloop()