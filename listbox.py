from tkinter import *

window = Tk()  # instantiate an instance of a window
window.title("Tkinter project")

icon = PhotoImage(file="Images/icon.png")
window.iconphoto(True, icon)
window.config(background="white")

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Comic Sans", 20)
                  )
listbox.pack()

listbox.insert(1, "yuichi")

entryBox = Entry(window)
entryBox.pack()


def submit():
    listbox.get(listbox.curselection())


submitButton = Button(window, text="submit", command=submit)
submitButton.pack()


def add():
    listbox.insert(listbox.size(), entryBox.get())


addButton = Button(window, text="add", command=add)
addButton.pack()


def delete():
    listbox.delete(listbox.curselection())


deleteButton = Button(window, text="delete", command=delete)
deleteButton.pack()

window.mainloop()  # place window on computer screen, listen for events
