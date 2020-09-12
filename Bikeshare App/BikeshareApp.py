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
        background = '#243447' 
        background2 = 'gray98'
        foreground = '#ffffff'
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
                
                if c.get() == 1:
                    city = 'Chicago'
                elif c.get() == 2:
                    city = 'Washington'
                elif c.get() == 3:
                    city = 'New York City'
                else:
                    pass

                #def loop():
                self.canvas = Canvas(self.master,width=80,height=20,bg=background,highlightbackground=background)
                self.canvas.place(x=350,y=260)
                
                self.load1 = self.canvas.create_image(7,10,image=self.image3)
                self.load2 = self.canvas.create_image(7,10,image=self.image3)
                self.load3 = self.canvas.create_image(7,10,image=self.image3)  
                self.status.configure(text='Connecting to '+city+' database...')
                count = 0
                """while True:
                    for i in range(0,25):
                    self.canvas.move(self.load1,2,0)                  
                        self.canvas.update()
                        time.sleep(0.02)       
                    for i in range(0,25):
                        self.canvas.move(self.load2,2,0)                  
                        self.canvas.update()
                        time.sleep(0.02) 
                    for i in range(0,25):
                        self.canvas.move(self.load3,2,0)                  
                        self.canvas.update()
                        time.sleep(0.02)         
                    for i in range(0,25):
                        self.canvas.move(self.load1,-2,0)                  
                        self.canvas.update()
                        time.sleep(0.02)       
                    for i in range(0,25):
                        self.canvas.move(self.load2,-2,0)                  
                        self.canvas.update()
                        time.sleep(0.02) 
                    for i in range(0,25):
                        self.canvas.move(self.load3,-2,0)                  
                        self.canvas.update()
                        time.sleep(0.02)   
                        self.status.configure(text='Finishing up...')
                    count += 1
                    if count == 1:    """
                self.canvas.place_forget()
                self.status.configure(text='')
                #==========================Filter Options==========================
                self.info4 = Label(self.master,text='Filter Option',font=('arial',13,'bold'),fg=foreground,bg=background)
                self.info4.place(x=350,y=15)                            
                def check_box():
                    if m.get() == 1:
                        self.month_box.configure(state=NORMAL)
                    else:
                        self.month_box.configure(state=DISABLED)
                    if d.get() == 1:
                        self.day_box.configure(state=NORMAL)
                    else:
                        self.day_box.configure(state=DISABLED)                       
                m = IntVar()
                d = IntVar()
                self.month_btn = Checkbutton(self.master,text='Month',bg=background,fg=foreground,activebackground=background,font=("arial",11),onvalue=1,offvalue=0,variable=m,command=check_box)
                self.day_btn = Checkbutton(self.master,text='Day',bg=background,fg=foreground,activebackground=background,font=("arial",11),onvalue=1,offvalue=0,variable=d,command=check_box)                
                self.month_btn.place(x=290,y=60) 
                self.day_btn.place(x=420,y=60)  
                
                self.month_box = ttk.Combobox(self.master,width=10,font=("normal",10),state=DISABLED)
                self.month_box.insert(0,'')
                self.month_box['values'] = ("January","Ferbuary","March","April","May","June")
                self.month_box.place(x=295,y=90)
                
                self.day_box = ttk.Combobox(self.master,width=10,font=("normal",10),state=DISABLED)
                self.day_box.insert(0,'')
                self.day_box['values'] = [str(i) for i in range(1,32)]
                self.day_box.place(x=425,y=90)                            
                             
                self.continue_btn.place(x=350,y=130,width=100,height=28)
                self.continue_btn.configure(command=None)                
                #thread = threading.Thread(target=loop)
                #thread.start()                   
                
                
            c = IntVar()
            self.chicago = Checkbutton(self.master,text='Chicago',bg=background,fg=foreground,activebackground=background,font=("arial",11),onvalue=1,offvalue=0,variable=c,command=choice)
            self.washington = Checkbutton(self.master,text='Washington',bg=background,fg=foreground,activebackground=background,font=("arial",11),onvalue=2,offvalue=0,variable=c,command=choice)
            self.new_york = Checkbutton(self.master,text='New York City',bg=background,fg=foreground,activebackground=background,font=("arial",11),onvalue=3,offvalue=0,variable=c,command=choice)
            self.chicago.place(x=210,y=60) 
            self.washington.place(x=331,y=60)  
            self.new_york.place(x=470,y=60)
            
        self.continue_btn = Button(self.master,text='Continue',font=('arial',12),bg='#afc3df',fg=background,bd=1,relief='ridge',activebackground=background,command=_continue)
        self.continue_btn.place(x=320,y=100,width=150,height=45)
               
        
        
if __name__=='__main__':
    root = Tk()
    App = Bikeshare(root)
    root.mainloop()