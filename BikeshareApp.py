# Data wrangling and analysis
import pandas as pd
import numpy as np
# Data Visualization
#import matplotlib.pyplot as plt
#import seaborn as sns
# Graphical user interface
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

#====================================Main Application Class====================================
class Bikeshare:
    def __init__(self, master):
        background = '#ffffff' 
        background2 = 'gray98'
        foreground = '#050716'
        #master.iconbitmap("GPA.ico") #window icon
        self.master = master #root window
        self.master.title("Bikeshare") #window title
        self.master.configure(background=background) #window background color
        self.master.geometry('800x600') #window geometry(size)
        self.master.resizable(False,False) # resize window -> false
        



if __name__=='__main__':
    root = Tk()
    App = Bikeshare(root)
    root.mainloop()