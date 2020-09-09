import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

month = '' # variable to hold the value for month
day = '' # variable to hold the value for day
months = ['january','february','march','april','may','june'] # list of months
days = [] # list of days
for i in range(1,32): # loop 31 times
    if i <= 9: # 
        days.append('0'+str(i))
    else:
        days.append(str(i))
        
def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        city = input("Enter the city you like to view data on between Chicago, New york, or Washington\n") # Get city of choice from user
        if city.lower() == 'chicago' or city.lower() == 'new york' or city.lower() == 'washington': # If the city entered is either of the cities provided
            while True:
                choice = input("For the "+city.upper()+" dataset enter data filter type by month, day, both or not at all Type 'none' for no filter.\n") # Get the filter choice from user
                if choice.lower() == 'month': # if the filter choice by the user is MONTH
                    while True:
                        month = input("Enter Month: January, February, March, April, May or June\n") # Get the month to filter from user
                        if month in months: # if month entered by user is in the months list break the loop
                            break
                        else: # else continue looping until the right input is entered
                            print('Invalid month, try again!')
                            continue
                    break #break the loop
                elif choice.lower() == 'day': # if the filter choice by the user is DAY
                    while True:
                        day = input("Enter Day(Date): 01,02,03,....,31\n") # Get the day to filter from user
                        if day in days: # if day entered by user is in the days list break the loop
                            break
                        else: # else continue looping until the right input is entered
                            print('Invalid date, try again!')
                            continue                            
                    break #break the loop
                elif choice.lower() == 'both': # if the filter choice by the user is BOTH
                    while True:
                        both = input("Enter Month (space) day(date): January 05\n")
                        if both.split(' ')[0] in months and both.split(' ')[1] in days:
                            month = both.split(' ')[0] # assign the month variable to first value in both
                            day = both.split(' ')[1] # assign the day variable to second value in both                             
                            break
                        else:
                            print("Invalid month or day, try again!")
                            continue
                    break #break the loop
                elif choice.lower() == 'none': # if the filter choice by the user is NONE
                    month = ''
                    day = ''
                    break #break the loop, month and day will remain empty
                else: # Invalid input continue running the loop
                    print('Invalid filter input, try again!') 
                    continue 
            break # break the external loop
        else:
            print("Invalid city name, try again")
            continue
    print('-'*50)
    return city, month, day

def load_data(city, month, day):
    months_dict = dict(zip(months, days))    
    #CHICAGO
    if city.lower() == 'chicago': # if the city chosen by the user is chicago
        df = pd.read_csv('chicago.csv') # read the chicago data set
        df['Gender'].replace(np.nan,'Male',inplace=True) # replace the missing values in the gender column using mode since its a categorically represented
        df['Birth Year'].replace(np.nan,df['Birth Year'].mean(),inplace=True) # replace the missing values in the birth year column using mean since it contains contionous values 
        df['Birth Year'] = df['Birth Year'].astype(int) # convert the entire birth year column to integer data type
        if month != '' and day == '': # if month is not empty and day is empty means we are filtering by MONTH
            df = df.loc[df['Start Time'].str[5:7] == months_dict.get(month)]
        elif month == '' and day != '': # if month is empty and day is not empty means we are filtering by DAY
            df = df.loc[df['Start Time'].str[8:10] == day]
        elif month != '' and day != '': # if month is not empty and day is not empty means we are filtering BOTH
            df = df.loc[df['Start Time'].str[5:7] == months_dict.get(month) & df['Start Time'].str[8:10] == day]
        elif month == '' and day == '': # if month and day is empty it means we are NOT filtering  
            df
        else:
            pass
    # NEW YORK
    elif city.lower() == 'new york':
        df = pd.read_csv('new_york_city.csv')
        df['User Type'].replace(np.nan,'Subscriber',inplace=True) # replace the missing values in the user type column using mode since its a categorically represented
        df['Gender'].replace(np.nan,'Male',inplace=True) # replace the missing values in the gender column using mode since its a categorically represented
        df['Birth Year'].replace(np.nan,df['Birth Year'].mean(),inplace=True) # replace the missing values in the birth year column using mean since it contains contionous values         
        df['Birth Year'] = df['Birth Year'].astype(int) # convert the entire birth year column to integer data type
        if month != '' and day == '': # if month is not empty and day is empty means we are filtering by MONTH
            df = df.loc[df['Start Time'].str[5:7] == months_dict.get(month)]
        elif month == '' and day != '': # if month is empty and day is not empty means we are filtering by DAY
            df = df.loc[df['Start Time'].str[8:10] == day]
        elif month != '' and day != '': # if month is not empty and day is not empty means we are filtering BOTH
            df = df.loc[df['Start Time'].str[5:7] == months_dict.get(month) & df['Start Time'].str[8:10] == day]
        elif month == '' and day == '': # if month and day is empty it means we are NOT filtering  
            df
        else:
            pass
    elif city.lower == 'washington':
        df = pd,read_csv('washington.csv')
        
    return df
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
