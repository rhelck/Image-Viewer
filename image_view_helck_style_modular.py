from tkinter import *
import time
from time import strftime
from PIL import ImageTk,Image
from random import *
import os

root = Tk()
root.iconbitmap('C:\\Users\\User\\desktop_clock_folder\\favicon.ico')

# this allows the user to access files (presumably JPGs, but I beleive that most picture formats will be accepted) in the folder
path = 'C:\\Users\\User\\desktop_clock_folder\\image viewer pics'
directory = os.listdir(path)
image_list = []
image_name_list = []

# this generates a list of image files using Pillow, and a list of corresponding names
for f in directory:
    f_path = path + '\\' + f
    image_name_list.append(f)
    image_list.append(ImageTk.PhotoImage(Image.open(f_path)))
print(image_list)
print(image_name_list)

position = 1

# this is where the image itself is displayed on the GUI
img_label = Label(root, image = image_list[position])
img_label.grid(column = 0, row = 0, columnspan = 3)

# this corresponds to the button_forward widget located far below. It modulates the position varialble by +1, thus displaying the "next" picture
def forward():
    
    global img_label
    global position 
    global name_label

    if position < (len(image_list) - 1):
        position = position + 1
        img_label.grid_forget()
        img_label = Label(image = image_list[position])
        img_label.grid(column = 0, row = 0, columnspan = 3)
        name_label.grid_forget()
        name_label = Label(text = image_name_list[position])
        name_label.grid(column = 0, row = 3, columnspan = 3)

#this corresponds to the button_backward widget found far below, and modulates the position variable by -1, thus bringing up the "previous" image
def backward():

    global img_label
    global position
    global name_label

    if position > 0:
        position = position - 1
        img_label.grid_forget()
        img_label = Label(image = image_list[position])
        img_label.grid(column = 0, row = 0, columnspan = 3)
        name_label.grid_forget()
        name_label = Label(text = image_name_list[position])
        name_label.grid(column = 0, row = 3, columnspan = 3)

# this corresponds to the random_button widget, and brings up a random image from the list
def random_func():

    global img_label
    global position
    global name_label

    position = randint(0, (len(image_list)-1))
    img_label.grid_forget()
    img_label = Label(image = image_list[position])
    img_label.grid(column = 0, row = 0, columnspan = 3)
    name_label.grid_forget()
    name_label = Label(text = image_name_list[position])
    name_label.grid(column = 0, row = 3, columnspan = 3)

name_label = Label(root, width = 10, text = '')
name_label.grid(column = 0, row = 3, columnspan = 3)
time_label = Label(root, width = 10)
time_label.grid(column = 0, row = 4, columnspan = 3)

#this runs a clock on the widget. It's not necessay, but it seems a nice touch.
def count():
    time_now = time.strftime('%H %M %S %p')
    time_label.configure(text = time_now)
    time_label.after(1000, count)

count()

back_button = Button(root, text = '<', command = backward)
back_button.grid(column = 0, row = 1)
random_button = Button(root, text = 'random', command = random_func)
random_button.grid(column = 1, row = 1)
forward_button = Button(root, text = '>', command = forward)
forward_button.grid(column = 2, row = 1)

root.mainloop()
