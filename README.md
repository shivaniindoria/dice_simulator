# dice_simulator
Dice Roll Simulation Using Python - Tkinter GUI Python Project

import tkinter as tk
from PIL import Image, ImageTk
import random
# import the tkinter by using "pip install tkinter" that helps people using GUI interface |import pillow uising pillow helps usig photos ad images in python |import a random number,integer

dice=["diceimg/dice1.png","diceimg/dice2.png","diceimg/dice3.png","diceimg/dice4.png","diceimg/dice5.png","diceimg/dice6.png"] ## create a list of dice image to select random image for display
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
label1 = tk.Label(window,image=image1)
label1.image = image1
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
label2 = tk.Label(window,image=image2)
label2.image = image2
# image obj is created which get random image by choise from dice dictionary -- labels created in gui window which which contains dice image inside it .

def dice_roll():
    image1= ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image = image1)
    label1.image = image1
    image2= ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image = image2)
    label2.image = image2
button = tk.Button(window,text = "Roll" , bg= "white", fg="black" ,font="times 20 bold",command=dice_roll)

# function is created to perform the action of dice rolling dice again and again as clicked on given ROLL button 
obj.place(x= 350,y=50)
# place is a funtion that helps to adjust object's location on screen x and y are coordinates .
