from tkinter import *
from tkinter import filedialog

window = Tk()  # instantiate an instance of a window
window.title("Tkinter project")

icon = PhotoImage(file="Images/icon.png")
window.iconphoto(True, icon)
window.config(background="white")


def save_file():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\Godwyn\\PycharmProjects\\Project-Tkinter",
                                    defaultextension='.json',
                                    filetypes=[
                                        ("JSON file", ".json"),
                                        ("Text file", ".txt")
                                    ])
    if file is None:
        return
    file_text = str(text.get(1.0, END))
    file.write(file_text)
    file.close()


button = Button(text="save", command=save_file)
button.pack()
text = Text(window)
text.pack()

window.mainloop()  # place window on computer screen, listen for events
