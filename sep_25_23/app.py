import tkinter as tk

contacts = []

root_window = tk.Tk()

def add_contact_hadnler():
    conact_number_value = contact_number_entry.get()
    contacts.append(conact_number_value)

root_window.geometry("1250x500")
root_window.minsize(500, 150)
root_window.title("My First GUI Program")

contact_label = tk.Label(root_window, text="Enter Contact Number")
contact_label.pack()

contact_number_entry = tk.Entry(root_window)
contact_number_entry.pack()

contact_button = tk.Button(root_window, text="Add Contact", command=add_contact_hadnler)
contact_button.pack()

root_window.mainloop()