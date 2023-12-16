from tkinter import *

window = Tk()  # instantiate an instance of a window
window.title("Tkinter project")

icon = PhotoImage(file="Images/icon.png")
window.iconphoto(True, icon)
window.config(background="white")

photo = PhotoImage(file="Images/click.png")

# button = clicking it do stuff

count = 0


def click():
    global count
    count += 1
    print(count)


button = Button(window,
                text="A button",
                command=click,
                font=("Comic Sans", 30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",  # to change the button color when you click it
                activebackground="black",
                state=ACTIVE,  # to make it usable or not (ACTIVE/DISABLE)
                image=photo,
                compound='bottom'
                )
button.pack()

window.mainloop()  # place window on computer screen, listen for events
