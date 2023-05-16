from tkinter import *
from tkinter import ttk

root = Tk()

entry = ttk.Entry(root, width=30)
entry2 = ttk.Entry(root, width=30)
entry.insert(0, "WHAT IS YOUR NAME")

entry2.config(show='*')

entry.pack()
entry2.pack()

root.geometry("400x400")

root.mainloop