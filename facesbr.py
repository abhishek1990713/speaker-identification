from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from train import *
from test import *

root = Tk()
root.title("Speaker Recognition")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
root.state('zoomed')
