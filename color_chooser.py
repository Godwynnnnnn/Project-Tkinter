from tkinter import *
from tkinter import colorchooser

window = Tk()  # instantiate an instance of a window
window.geometry('420x420')
window.title("Tkinter project")

icon = PhotoImage(file="Images/icon.png")
window.iconphoto(True, icon)
window.config(background="white")


def click():
    color = colorchooser.askcolor()
    print(color)
    hex_color = color[1]
    print(hex_color)
    window.config(bg=hex_color)


button = Button(text='Change color', command=click)
button.pack()

window.mainloop()  # place window on computer screen, listen for events
