from cProfile import label
from email.mime import image
from secrets import choice
import tkinter as tk
from PIL import Image, ImageTk 
import random

window = tk.Tk()
window.geometry("750x500")
window.title("Dice Roll")

dice=["diceimg/dice1.png","diceimg/dice2.png","diceimg/dice3.png","diceimg/dice4.png","diceimg/dice5.png","diceimg/dice6.png"]
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = tk.Label(window,image=image1)
label2 = tk.Label(window,image=image2)

label1.image = image1
label2.image = image2
label1.place(x=100,y=150)
label2.place(x=400,y=150)

def dice_roll():
    image1= ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image = image1)
    label1.image = image1

    image2= ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image = image2)
    label2.image = image2


button = tk.Button(window,text = "Roll" , bg= "white", fg="black" ,font="times 20 bold",command=dice_roll)
button.place(x= 350,y=50)
window.mainloop()


# def roll_dice():
#     a = random.randint(1,6)
#     label = tk.Label(window,text= a).pack()
# button.pack()