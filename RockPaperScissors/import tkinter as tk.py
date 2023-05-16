import tkinter as tk
from tkinter import ttk

root = tk.Tk()
my_boolean_var = tk.BooleanVar()

root.geometry("300x300")

my_checkbutton = ttk.Checkbutton(
    text="Check when the option True",
    variable=my_boolean_var
)
my_checkbutton.pack()
root.mainloop