import tkinter as tk
from PIL import ImageTk, Image
import pygame

root = tk.Tk()
root.geometry("400x400")
root.resizable(False, False)

image_path = "C:\\Users\\lyand\\OneDrive\\Documents\\codes\\Johns-Code-that-I-stolen\\Assets\\Tigr.png"
img = Image.open(image_path)
img = img.resize((400, 400))  # Resize the image to your desired dimensions
image = ImageTk.PhotoImage(img)

image_label = tk.Label(root, image=image)
image_label.pack()

def RockClick():
    print("Rock")

Rock = tk.Button(root, text="Rock", width=10, height=2, command=RockClick)
Rock.pack()
Rock.place(x=30, y=300)

def PaperClick():
    print("Paper")

Paper = tk.Button(root, text="Paper", width=10, height=2, command=PaperClick)
Paper.pack()
Paper.place(x=170, y=300)

def ScissorsClick():
    print("Scissors")

Scissors = tk.Button(root, text="Scissors", width=10, height=2, command=ScissorsClick)
Scissors.pack()
Scissors.place(x=290, y=300)

root.mainloop()
