import tkinter as tk

root_window = tk.Tk()
def handle_submit():
    name = name_entry.get()
    print("Hello " + name)


# enter name label with big font
enter_name_label = tk.Label(root_window, text = "Enter Name", font = ("Arial", 20))
# place the label on the window
enter_name_label.pack()

# entry widget to enter name
name_entry = tk.Entry(root_window)
# place the entry widget on the window
name_entry.pack()

# button widget to submit name
submit_button = tk.Button(root_window, text = "Submit", command=handle_submit)
# place the button on the window
submit_button.pack()


root_window.mainloop()