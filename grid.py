from tkinter import *

window = Tk()  # instantiate an instance of a window
window.title("Tkinter project")

icon = PhotoImage(file="Images/icon.png")
window.iconphoto(True, icon)
window.config(background="white")

titleLabel = (Label(window,
                    text="Enter Your Information",
                    font=("Comic Sans", 25)).
              grid(row=0, column=0, columnspan=2))

firstNameLabel = (Label(window,
                        text="First name: ",
                        width=20,
                        bg="red").
                  grid(row=1, column=0))
firstNameEntry = (Entry(window).
                  grid(row=1, column=1))

lastNameLabel = (Label(window, text="Last name: ",
                       width=20,
                       bg="green").
                 grid(row=2, column=0))
lastNameEntry = (Entry(window).
                 grid(row=2, column=1))

emailLabel = (Label(window, text="Email: ",
                    width=20,
                    bg="blue").
              grid(row=3, column=0))
emailEntry = (Entry(window).
              grid(row=3, column=1))

submitButton = (Button(window, text="Submit").
                grid(row=4, column=0, columnspan=2))

window.mainloop()  # place window on computer screen, listen for events
