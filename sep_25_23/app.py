import tkinter as tk

contacts = []

root_window = tk.Tk()

def add_contact_hadnler():
    conact_number_value = contact_number_entry.get()
    contacts.append(conact_number_value)

def view_contact_handler():
    contact_text_box.delete(1.0, tk.END)
    for contact in contacts:
        contact_text_box.insert(tk.END, contact + "\n")

root_window.geometry("1250x500")
root_window.minsize(500, 150)
root_window.title("My First GUI Program")

contact_label = tk.Label(root_window, text="Enter Contact Number")
contact_label.pack()

contact_number_entry = tk.Entry(root_window)
contact_number_entry.pack()

contact_button = tk.Button(root_window, text="Add Contact", command=add_contact_hadnler)
contact_button.pack()

view_contact_button = tk.Button(root_window, text="View Contact", command=view_contact_handler)
view_contact_button.pack()


contact_text_box = tk.Text(root_window, height=10, width=50)
contact_text_box.pack()

root_window.mainloop()