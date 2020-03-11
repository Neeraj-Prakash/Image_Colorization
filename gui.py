
from tkinter import * 
from tkinter.ttk import *
from PIL import ImageTk, Image
import os
import cv2
import numpy 
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfile 

imgpath = "" 
root = Tk() 
root.geometry('1000x1000') 


def open_file(): 
	global imgpath
	file = askopenfile(mode ='r', filetypes =[('Image Files', '*.jpg')]) 
	img = ImageTk.PhotoImage(Image.open(file.name))
	imgpath += file.name
	panel = Label(root, image = img)
	panel.img = img
	panel.pack(side = "left", fill = "none", expand = "yes") 
	btn1.after(0000, btn1.destroy)

def load_file():
	img = ImageTk.PhotoImage(Image.open(imgpath))
	panel = Label(root, image = img)
	panel.img = img
	panel.pack(side = "bottom", fill = "x=500,y=500", expand = "yes") 



btn1 = Button(root, text ='Open', command = open_file) 
btn2 = Button(root, text ='Convert', command = load_file) 

btn1.pack(side = TOP, pady = 40) 
btn2.pack(side = BOTTOM, pady = 100) 

mainloop() 
