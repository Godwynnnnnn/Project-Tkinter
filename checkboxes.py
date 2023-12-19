from tkinter import *

window = Tk()  # instantiate an instance of a window
window.title("Tkinter project")

icon = PhotoImage(file="Images/icon.png")
window.iconphoto(True, icon)
window.config(background="white")


def display():
    if x.get():  # if they check the checkbox,
        print("Yes it is a checkbox")
    else:
        print("It is not a checkbox")


x = BooleanVar()

check_button = Checkbutton(window,
                           text="I am a checkbox",
                           variable=x,
                           onvalue=True,
                           offvalue=False,
                           command=display,
                           font=("Comic Sans", 20),
                           fg="white",
                           bg="#a3842c",
                           activeforeground="white",
                           activebackground="#a3842c",
                           padx=25,
                           pady=10
                           )
check_button.pack()

window.mainloop()  # place window on computer screen, listen for events
