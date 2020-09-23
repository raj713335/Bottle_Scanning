from tkinter import *
from tkinter import messagebox

t = Tk()

def button1_click():
    messagebox.showinfo("Message", "Bang!")

def button2_click():
    button1.invoke()

button1 = Button(t, text="Button 1", command=button1_click)
button1.pack()

button2 = Button(t, text="Button 2", command=button2_click)
button2.pack()

mainloop()