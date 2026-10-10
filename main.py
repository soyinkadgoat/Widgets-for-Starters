from tkinter import *
from datetime import date

window = Tk()
window.title("My First App")
window.geometry("400x300")
window.configure(bg="yellow")

Lbl1 = Label(window, text="Hey there!", bg="red", fg="white", height=1, width=300)
Lbl1.pack()

name_lbl = Label(window, text="Full Name")
name_entry = Entry(window)

name_lbl.pack()
name_entry.pack()

def Display():
    name = name_entry.get()
    global message
    message = " Welcome to the Application.\nToday's date is: "
    greeting = "Hello " + name + "!"

    text_box.insert(END, greeting)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

btn = Button(window, text="Begin", bg="blue", fg="white", height=1, width=5, command=Display)
btn.pack()

text_box = Text(window, height=3)
text_box.pack()


window.mainloop()