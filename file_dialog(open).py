from tkinter import *
from tkinter import filedialog

window = Tk()  # instantiate an instance of a window
window.title("Tkinter project")

icon = PhotoImage(file="Images/icon.png")
window.iconphoto(True, icon)
window.config(background="white")


def open_file():
    filepath = filedialog.askopenfile(initialdir="C:\\Users\\Godwyn\\PycharmProjects\\Project-Tkinter",
                                      filetypes=(("json file", "*.json"), ("all files", "*.*")))
    file = open(filepath, 'r')
    print(file.read())
    file.close()


button = Button(text="Open", command=open_file)
button.pack()

window.mainloop()  # place window on computer screen, listen for events
