from tkinter import *

window = Tk()  # instantiate an instance of a window
window.geometry("420x420")
window.title("Tkinter project")


icon = PhotoImage(file="Images/icon.png")  # creation of photo
window.iconphoto(True, icon)  # for icon
window.config(background="white")

# label = an area widget that holds text and/or image within a window
label = Label(window,
              text="Hello World!",
              font=('Arial', 40, 'bold'),
              fg='#00FF00',  # color of text
              bg='white',  # color of background
              relief=RAISED,  # border style
              bd=10,  # border size
              padx=20,  # padding for x-axis
              pady=20  # padding for y-axis
              # image=icon,  # import of image
              # compound='bottom'  # placement of image
              )
label.pack()
# label.place(x=0, y=0)  # for placing it to where ever you like

window.mainloop()  # place window on computer screen, listen for events
