# Data wrangling and analysis
import pandas as pd
import numpy as np
# Data Visualization
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
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
        #==============================Second Page=================================
        def _continue():
            self.label.configure(image=self.image2)
            self.info.place_forget()
            self.info2.place_forget()
            self.continue_btn.place_forget()
            
            self.info3 = Label(self.master,text='Select country to perform analysis',font=('arial',13,'bold'),fg=foreground,bg=background)
            self.info3.place(x=245,y=15)
            
            self.plot_frame = Frame(self.master,bg=background,bd=0,relief='flat')
            self.plot_info = Label(self.plot_frame,text='',font=('arial',12),bg=background,fg=foreground)
            
            self.status_frame = Frame(self.master,width=800,height=50,bg=background,bd=1,relief='sunken')
            self.status_frame.place(x=0,y=580)
            self.status = Label(self.status_frame,text='',font=('normal',8),fg=foreground,bg=background)
            self.status.place(x=0,y=0)     
            #==============================Third Page=================================
            def choice():
                self.info3.place_forget()
                self.chicago.place_forget()
                self.washington.place_forget()
                self.new_york.place_forget()
                
                if c.get() == 1:
                    city = 'chicago'
                elif c.get() == 2:
                    city = 'washington'
                elif c.get() == 3:
                    city = 'new york'
                else:
                    pass

                #==========================Filter Options==========================
                self.info4 = Label(self.master,text='Filter Option',font=('arial',15,'bold'),fg=foreground,bg=background)
                self.info4.place(x=290,y=15)                            
                def check_box():
                    if m.get() == 1:
                        self.month_box.configure(state=NORMAL)
                    else:
                        self.month_box.configure(state=DISABLED)
                    if d.get() == 1:
                        self.day_box.configure(state=NORMAL)
                    else:
                        self.day_box.configure(state=DISABLED)                       
                months = ["January","Ferbuary","March","April","May","June"]
                days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
                m = IntVar()
                d = IntVar()
                
                self.month_btn = Checkbutton(self.master,text='Month',bg=background,fg=foreground,activebackground=background,font=("arial",11),onvalue=1,offvalue=0,variable=m,command=check_box)
                self.day_btn = Checkbutton(self.master,text='Day',bg=background,fg=foreground,activebackground=background,font=("arial",11),onvalue=1,offvalue=0,variable=d,command=check_box)                
                self.month_btn.place(x=290,y=60) 
                self.day_btn.place(x=420,y=60)  
                
                self.month_box = ttk.Combobox(self.master,width=10,font=("normal",10),state=DISABLED)
                self.month_box.insert(0,'')
                self.month_box['values'] = months
                self.month_box.place(x=295,y=90)
                
                self.day_box = ttk.Combobox(self.master,width=10,font=("normal",10),state=DISABLED)
                self.day_box.insert(0,'')
                self.day_box['values'] = days
                self.day_box.place(x=425,y=90)                            
                #=========================Fourth Page==========================
                def _continue2():
                    #===================Loading Loop========================
                    def loop(b):
                        self.canvas = Canvas(self.master,width=80,height=20,bg=background,highlightbackground=background)
                        self.canvas.place(x=350,y=260)
                        
                        self.load1 = self.canvas.create_image(7,10,image=self.image3)
                        self.load2 = self.canvas.create_image(7,10,image=self.image3)
                        self.load3 = self.canvas.create_image(7,10,image=self.image3)  
                        
                        while True:
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
                            if b == 'no':
                                continue
                            else:
                                break                        
                    #=============Handle and assign values for month and day==================
                    month = '' # variable to hold the value for month
                    day = '' # variable to hold the value for day    
                    if m.get() == 0 and d.get() == 0: # IF the two checkbuttons are not checked the filter is NONE
                        month = ''
                        day = ''
                    elif m.get() == 1 and d.get() == 0: #IF the month checkbutton is 1 and the day checkbutton is 0 the filter is MONTH
                        if self.month_box.get() not in months:
                            tkinter.messagebox.showerror("Error","Invalid month, Try again!")
                            _continue()
                        else:
                            month = self.month_box.get()                         
                    elif m.get() == 0 and d.get() == 1: #IF the month checkbutton is 0 and the day checkbutton is 1 the filter is DAY
                        if self.day_box.get() not in days:
                            tkinter.messagebox.showerror("Error","Invalid day, Try again!")
                            _continue()
                        else:
                            day = self.day_box.get()                               
                    elif m.get() == 1 and d.get() == 1: #IF the month checkbutton is 1 and the day checkbutton is 1 the filter is BOTH
                        if self.month_box.get() not in months or self.day_box.get() not in days:
                            tkinter.messagebox.showerror("Error","Invalid month or day, Try again!")
                            _continue()
                        else:
                            month = self.month_box.get()
                            day = self.day_box.get()                                
                    else:
                        pass
         
                    # ========Delete this widgets from the window===============
                    self.info4.place_forget()
                    self.month_btn.place_forget()
                    self.day_btn.place_forget()
                    self.month_box.place_forget()
                    self.day_box.place_forget()                    
                    self.continue_btn.place_forget()
                    
                    #=============================Load Data=============================
                    df = ''
                    #CHICAGO
                    if city == 'chicago': # if the city chosen by the user is chicago
                        self.status.configure(text="Fetching Chicago data...")
                        df = pd.read_csv('../chicago.csv') # read the chicago data set
                        df['Gender'].replace(np.nan,'Male',inplace=True) # replace the missing values in the gender column using mode since its a categorically represented
                        df['Birth Year'].replace(np.nan,df['Birth Year'].mean(),inplace=True) # replace the missing values in the birth year column using mean since it contains contionous values 
                        df['Birth Year'] = df['Birth Year'].astype(int) # convert the birth year column to integer data type
                        df['Start Time'] = pd.to_datetime(df['Start Time']) # convert the start time column to datetime data type
                        
                        if month != '' and day == '': # if month is not empty and day is empty means we are filtering by MONTH
                            df = df.loc[df['Start Time'].dt.month_name() == month.capitalize()] # return a dataframe where the month name equal to the month entered by the user
                        elif month == '' and day != '': # if month is empty and day is not empty means we are filtering by DAY
                            df = df.loc[df['Start Time'].dt.day_name() == day.capitalize()]
                        elif month != '' and day != '': # if month is not empty and day is not empty means we are filtering BOTH
                            df = df.loc[(df['Start Time'].dt.month_name() == month.capitalize()) & (df['Start Time'].dt.day_name() == day.capitalize())]
                        elif month == '' and day == '': # if month and day is empty it means we are NOT filtering  
                            df = df.copy()
                        else:
                            pass
                    # NEW YORK
                    elif city == 'new york':
                        self.status.configure(text="Fetching New York City data...")
                        df = pd.read_csv('../new_york_city.csv')
                        df['User Type'].replace(np.nan,'Subscriber',inplace=True) # replace the missing values in the user type column using mode since its a categorically represented
                        df['Gender'].replace(np.nan,'Male',inplace=True) # replace the missing values in the gender column using mode since its a categorically represented
                        df['Birth Year'].replace(np.nan,df['Birth Year'].mean(),inplace=True) # replace the missing values in the birth year column using mean since it contains contionous values         
                        df['Birth Year'] = df['Birth Year'].astype(int) # convert the birth year column to integer data type
                        df['Start Time'] = pd.to_datetime(df['Start Time']) # convert the start time column to datetime data type

                        if month != '' and day == '': # if month is not empty and day is empty means we are filtering by MONTH
                            df = df.loc[df['Start Time'].dt.month_name() == month.capitalize()] # return a dataframe where the month name equal to the month entered by the user
                        elif month == '' and day != '': # if month is empty and day is not empty means we are filtering by DAY
                            df = df.loc[df['Start Time'].dt.day_name() == day.capitalize()]
                        elif month != '' and day != '': # if month is not empty and day is not empty means we are filtering BOTH
                            df = df.loc[(df['Start Time'].dt.month_name() == month.capitalize()) & (df['Start Time'].dt.day_name() == day.capitalize())]
                        elif month == '' and day == '': # if month and day is empty it means we are NOT filtering  
                            df = df.copy()
                        else:
                            pass
                    # WASHINGTON
                    elif city == 'washington':
                        self.status.configure(text="Fetching Washington data...")
                        df = pd.read_csv('../washington.csv')
                        df['Start Time'] = pd.to_datetime(df['Start Time']) # convert the start time column to datetime data type
                        
                        if month != '' and day == '': # if month is not empty and day is empty means we are filtering by MONTH
                            df = df.loc[df['Start Time'].dt.month_name() == month.capitalize()] # return a dataframe where the month name equal to the month entered by the user
                        elif month == '' and day != '': # if month is empty and day is not empty means we are filtering by DAY
                            df = df.loc[df['Start Time'].dt.day_name() == day.capitalize()]
                        elif month != '' and day != '': # if month is not empty and day is not empty means we are filtering BOTH
                            df = df.loc[(df['Start Time'].dt.month_name() == month.capitalize()) & (df['Start Time'].dt.day_name() == day.capitalize())]
                        elif month == '' and day == '': # if month and day is empty it means we are NOT filtering  
                            df = df.copy()
                        else:
                            pass                    
                        
                    
                    
                    #==========================Statistics and plots==========================
                    plots = []
                    labels = []
                    #=======Time Stats========
                    self.plot_frame.place(x=0,y=20,width=800,height=490)
                    def time_stats():   
                        """Displays statistics on the most frequent times of travel."""
                        self.status.configure(text='Calculating The Most Frequent Times of Travel...')
                        if month == '': # if month is empty it means there is the dataframe is not month-filtered, so most common month can be displayed
                            # display the most common month: Since the dataframe to be used within this function is filtered, most common month will only be calculated for a dataframe which is not month-filtered.
                            m_series = df['Start Time'].dt.month_name().value_counts() # return month names, group them by the number of occurences using value_counts, a series will be returned
                            m = m_series[m_series == np.max(m_series)].index[0] # the series contains the month as index and number of occurences as value, get the maximum value and return the index(month)
                            label1 = "The most common month in the {} data is {}".format(city.upper(),m)
                            #======Plot======
                            m_figure1 = Figure(figsize=(8,6), dpi=70)
                            m_figure1.suptitle("Monthly count of the {} data".format(city.upper()))
                            m_plot1 = m_figure1.add_subplot(111)
                            m_plot1.bar(df['Start Time'].dt.month_name().unique(), m_series.values, color=background)
                            
                            self.canvas_plot1 = FigureCanvasTkAgg(m_figure1, self.plot_frame)
                            self.canvas_plot1.draw()
                            plots.append(self.canvas_plot1)
                            labels.append(label1)
                            #self.canvas_plot1.get_tk_widget().pack(side=TOP)
                        if day == '':
                            # display the most common day of week: the most common day will only be calculated for a dataframe which is not day-filtered.
                            d_series = df['Start Time'].dt.day_name().value_counts()
                            d = d_series[d_series == np.max(d_series)].index[0]
                            label2 = "The most common day in the {} data is {}".format(city.upper(), d)
                            #=====Plot======
                            m_figure2 = Figure(figsize=(8,6), dpi=70)
                            m_figure2.suptitle("Daily count of the {} data".format(city.upper()))
                            m_plot2 = m_figure2.add_subplot(111)
                            m_plot2.bar(df['Start Time'].dt.day_name().unique(), d_series.values, color=background)
                            
                            self.canvas_plot2 = FigureCanvasTkAgg(m_figure2, self.plot_frame)
                            self.canvas_plot2.draw()
                            plots.append(self.canvas_plot2)           
                            labels.append(label2)
                        # display the most common start hour
                        h_series = df['Start Time'].dt.hour.value_counts()
                        h = h_series[h_series == np.max(h_series)].index[0]
                        label3 = "The most common start hour in the {} data is {} with a count of: {}".format(city.upper(), h, np.max(h_series))
                        #=====Plot======
                        m_figure3 = Figure(figsize=(8,6), dpi=70)
                        m_figure3.suptitle("Daily count of the {} data".format(city.upper()))
                        m_plot3 = m_figure3.add_subplot(111)
                        m_plot3.bar(df['Start Time'].dt.hour.unique(), h_series.values, color=background)
                        
                        self.canvas_plot3 = FigureCanvasTkAgg(m_figure3, self.plot_frame)
                        self.canvas_plot3.draw()
                        plots.append(self.canvas_plot3)  
                        labels.append(label3)
                    
                    #==========Start Loading========== 
                    #thread = threading.Thread(target=loop('no'))
                    #thread.start()    
                    
                    
                    time_stats()
                    plots[0].get_tk_widget().pack(side=TOP)
                    self.plot_info.pack(side=BOTTOM)
                    self.plot_info.configure(text=labels[0])
                    index = 1
                    def _next():
                        for plot in self.plot_frame.winfo_children():
                            plot.pack_forget()
                        plots[index].get_tk_widget().pack(side=TOP)    
                        self.plot_info.configure(text=labels[index])
                        #index += 1
                    
                    self.next_btn = Button(self.master,text='>',font=('normal',35),fg=foreground,bd=0,relief='flat',bg=background,activebackground=background,command=_next)
                    self.next_btn.place(x=733,y=240)
                self.continue_btn.place(x=357,y=130,width=100,height=28)
                self.continue_btn.configure(command=_continue2)                
                                  
                
                
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