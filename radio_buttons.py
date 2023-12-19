from tkinter import *

window = Tk()  # instantiate an instance of a window
window.title("Tkinter project")

icon = PhotoImage(file="Images/icon.png")
window.iconphoto(True, icon)
window.config(background="white")

# Radio buttons = a checkboxes, but you can only select one

food = ["pizza", "hamburger", "hotdog"]

pizzaImage = PhotoImage(file='Images/pizza.png')
smallPizzaImage = pizzaImage.subsample(3, 3)  # resizing image
hamburgerImage = PhotoImage(file='Images/hamburger.png')
smallHamburgerImage = hamburgerImage.subsample(3, 3)
hotdogImage = PhotoImage(file='Images/hotdog.png')
smallHotdogImage = hotdogImage.subsample(3, 3)
foodImages = [smallPizzaImage, smallHamburgerImage, smallHotdogImage]


def order():
    if x.get() == 0:
        print("You ordered pizza!")
    elif x.get() == 1:
        print("You ordered a hamburger!")
    elif x.get() == 2:
        print("You ordered a hotdog!")
    else:
        print("Sorry, we don't have that...")


x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],  # adds text to radio buttons
                              variable=x,  # groups radio buttons together if they share the same variable
                              value=index,  # assigns each radio button a different value
                              padx=25,
                              font=("Comic Sans", 20),
                              image=foodImages[index],
                              compound='left',
                              indicatoron=False,  # removing the circle thing
                              width=375,
                              command=order
                              )
    radiobutton.pack(anchor=W)

window.mainloop()  # place window on computer screen, listen for events
