import tkinter as tk
from tkinter import messagebox


# step 1 - create root window
root = tk.Tk()

def create_contact():
    print("Create Contact")



root.title("My First GUI App")
root.geometry("750x250")

# step 3 - create widgets
label = tk.Label(root, text="Contact App")
label.pack()

create_button = tk.Button(root, text="Create Contact", command=create_contact)
create_button.pack()
view_button = tk.Button(root, text="View Contact")
view_button.pack()
update_button = tk.Button(root, text="Update Contact")
update_button.pack()
# delete_button with styles
delete_button = tk.Button(root, text="Delete Contact")
delete_button.pack()

# big text box
text_box = tk.Text(root, height=5, width=50)
text_box.pack()


# step 2 - create mainloop
root.mainloop()