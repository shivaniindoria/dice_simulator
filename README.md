# dice_simulator
Dice Roll Simulation Using Python - Tkinter GUI Python Project

<h2> import_needed__libraries</h2>
import tkinter as tk</br>
from PIL import Image, ImageTk</br>
import random</br> 
<h4>import the tkinter by using "pip install tkinter" that helps people using GUI interface || import pillow by pip helps using photos and images in python || import a random number,integer</h4><hr>

<h2> create a list of dice image to select random image for display</h2>
dice=["diceimg/dice1.png","diceimg/dice2.png","diceimg/dice3.png","diceimg/dice4.png","diceimg/dice5.png","diceimg/dice6.png"]<hr>
<h2> Create _objects</h2>
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))</br>
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))</br>
<h3> image obj is created which get random image by choise from dice list</h3>
label1 = tk.Label(window,image=image1)</br>
label1.image = image1</br>
label2 = tk.Label(window,image=image2)</br>
label2.image = image2</br>
<h3>labels created in GUI window which contains dice image inside it .</h3><hr>

<h2>function -- actions on ROLL button </h2>
<b>def dice_roll():</b></br>
    image1= ImageTk.PhotoImage(Image.open(random.choice(dice)))</br>
    label1.configure(image = image1)</br>
    label1.image = image1</br>
    image2= ImageTk.PhotoImage(Image.open(random.choice(dice)))</br>
    label2.configure(image = image2)</br>
    label2.image = image2</br>
button = tk.Button(window,text = "Roll" , bg= "white", fg="black" ,font="times 20 bold",command=dice_roll)</br>
<h3> function is created to perform the action of dice rolling dice again and again as clicked on given ROLL button </h3>
obj.place(x= 350,y=50)
<h3> place is a funtion that helps to adjust object's location on screen x and y are coordinates .</h3>
