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
# Timing
import threading
import time


#====================================Main Application Class====================================
class Bikeshare:
    def __init__(self, master):
        #243447
        background = '#ffffff' 
        background2 = 'gray98'
        foreground = '#050716'
        master.iconbitmap("icon.ico") #window icon
        self.master = master #root window
        self.master.title("Bikeshare") #window title
        self.master.configure(background=background) #window background color
        self.master.geometry('800x600') #window geometry(size)
        self.master.resizable(False,False) # resize window -> false
        
        self.image1 = PhotoImage(file='bg.png')
        self.image2 = PhotoImage(file='bg2.png')
        self.image3 = PhotoImage(file='load.png')        
        
        self.label = Label(self.master, image=self.image1,bg=background)
        self.label.place(x=0,y=0)
        
        text2 = "Exploring data related to bike share systems for\nChicago, New York City, and Washington in the United States Of America."
        self.info = Label(self.master,text='Exploratory Data Analaysis',font=('arial',25,'bold'),fg=foreground,bg=background)
        self.info.place(x=185,y=5)
        self.info2 = Label(self.master,text=text2,font=('arial',11),fg=foreground,bg=background)
        self.info2.place(x=150,y=50)
        
        def _continue():
            self.label.configure(image=self.image2)
            self.info.place_forget()
            self.info2.place_forget()
            self.continue_btn.place_forget()
            
            self.info3 = Label(self.master,text='Select country to perform analysis',font=('arial',13,'bold'),fg=foreground,bg=background)
            self.info3.place(x=245,y=15)
            
            self.status_frame = Frame(self.master,width=800,height=50,bg=background,bd=1,relief='sunken')
            self.status_frame.place(x=0,y=580)
            self.status = Label(self.status_frame,text='',font=('normal',8),fg=foreground,bg=background)
            self.status.place(x=0,y=0)            
            def choice():
                self.info3.place_forget()
                self.chicago.place_forget()
                self.washington.place_forget()
                self.new_york.place_forget()
                
                if i.get() == 1:
                    country = 'Chicago'
                    
                def loop():
                    self.canvas = Canvas(self.master,width=80,height=20,bg=background,highlightbackground=background)
                    self.canvas.place(x=350,y=260)
                    
                    self.load1 = self.canvas.create_image(7,10,image=self.image3)
                    self.load2 = self.canvas.create_image(7,10,image=self.image3)
                    self.load3 = self.canvas.create_image(7,10,image=self.image3)  
                    self.status.configure(text='Establishing link to database...')
                    while True:
                        for i in range(0,25):
                            self.canvas.move(self.load1,2,0)                  
                            self.canvas.update()
                            time.sleep(0.02)       
                            self.status.configure(text='Connecting to '+country+' database...')
                        for i in range(0,25):
                            self.canvas.move(self.load2,2,0)                  
                            self.canvas.update()
                            time.sleep(0.02) 
                            self.status.configure(text='Checking for missing values...')
                        for i in range(0,25):
                            self.canvas.move(self.load3,2,0)                  
                            self.canvas.update()
                            time.sleep(0.02)         
                        for i in range(0,25):
                            self.canvas.move(self.load1,-2,0)                  
                            self.canvas.update()
                            time.sleep(0.02)       
                            self.status.configure(text='Handling missing values...')
                        for i in range(0,25):
                            self.canvas.move(self.load2,-2,0)                  
                            self.canvas.update()
                            time.sleep(0.02) 
                        for i in range(0,25):
                            self.canvas.move(self.load3,-2,0)                  
                            self.canvas.update()
                            time.sleep(0.02)   
                            self.status.configure(text='Finishing up...')
                thread = threading.Thread(target=loop)
                thread.start()                   
                
            i = IntVar()
            self.chicago = Checkbutton(self.master,text='Chicago',bg=background,fg=foreground,activebackground=background,font=("arial",11),onvalue=1,offvalue=0,variable=i,command=choice)
            self.washington = Checkbutton(self.master,text='Washington',bg=background,fg=foreground,activebackground=background,font=("arial",11),onvalue=2,offvalue=0,variable=i,command=choice)
            self.new_york = Checkbutton(self.master,text='New York City',bg=background,fg=foreground,activebackground=background,font=("arial",11),onvalue=3,offvalue=0,variable=i,command=choice)
            self.chicago.place(x=210,y=60) 
            self.washington.place(x=331,y=60)  
            self.new_york.place(x=470,y=60)
            
        self.continue_btn = Button(self.master,text='Continue',font=('arial',12),bg='#afc3df',fg=background,bd=1,relief='ridge',activebackground=background,command=_continue)
        self.continue_btn.place(x=320,y=100,width=150,height=45)
               
        
        
if __name__=='__main__':
    root = Tk()
    App = Bikeshare(root)
    root.mainloop()