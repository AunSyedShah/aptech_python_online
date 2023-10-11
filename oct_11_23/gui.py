import tkinter as tk


# step 1 - create root window
root = tk.Tk()
root.title("My First GUI App")
root.geometry("750x250")

# step 3 - create widgets
label = tk.Label(root, text="Hello, World!")
label.pack()
login_button = tk.Button(root, text="Login")
login_button.pack()


# step 2 - create mainloop
root.mainloop()