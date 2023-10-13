import tkinter as tk
from tkinter import messagebox


# step 1 - create root window
root = tk.Tk()

def create_contact():
    # save contact function handler for save_button, to display a gui message box
    def save_contact():
        # get the contact name and number
        contact_name = name_entry.get()
        contact_number = number_entry.get()
        print(contact_name, contact_number)


    # open a new window
    create_contact_window = tk.Toplevel(root)
    create_contact_window.title("Create Contact")
    create_contact_window.geometry("250x250")
    # two labels and two entry fields for contact_name and contact_number
    name_label = tk.Label(create_contact_window, text="Contact Name")
    name_label.pack()
    name_entry = tk.Entry(create_contact_window)
    name_entry.pack()
    number_label = tk.Label(create_contact_window, text="Contact Number")
    number_label.pack()
    number_entry = tk.Entry(create_contact_window)
    number_entry.pack()
    # create a button to save the contact
    save_button = tk.Button(create_contact_window, text="Save Contact", command=save_contact)
    save_button.pack()



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


# step 2 - create mainloop
root.mainloop()