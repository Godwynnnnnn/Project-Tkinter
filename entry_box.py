from tkinter import *

window = Tk()  # instantiate an instance of a window
window.title("Tkinter project")

icon = PhotoImage(file="Images/icon.png")
window.iconphoto(True, icon)
window.config(background="white")

# entry = textbox that accepts a single line of user input


def submit():
    username = entry.get()  # store the values of entry
    print("Hello " + username)
    entry.config(state=DISABLED)


def delete():
    entry.delete(0, END)  # delete all


def backspace():
    entry.delete(len(entry.get())-1, END)  # delete 1 character


entry = Entry(window,
              font=("Comic Sans", 50),
              fg="white",
              bg="#a3842c"
              # show="*"  # for passwords
              )
# entry.insert(0,"Type here...")
entry.pack(side=LEFT)

submit_button = Button(window,
                       text="Submit",
                       command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window,
                       text="Delete",
                       command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window,
                          text="Backspace",
                          command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()  # place window on computer screen, listen for events
