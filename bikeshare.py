import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january','february','march','april','may','june'] # list of months
days = [] # list of days
for i in range(1,32): # loop 31 times
    if i <= 9: # 
        days.append('0'+str(i))
    else:
        days.append(str(i))
months_dict = dict(zip(months, days)) # a dictionary of month names as keys and 01,02,03,04,05,06 as keys 
months_dict_reversed = dict(zip(days, months)) # a dictionary of days 01,02,03,04,05,06 as keys and month names as values
def get_filters():
    month = '' # variable to hold the value for month
    day = '' # variable to hold the value for day    
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
    df = ''
    #CHICAGO
    if city.lower() == 'chicago': # if the city chosen by the user is chicago
        df = pd.read_csv('chicago.csv') # read the chicago data set
        df['Gender'].replace(np.nan,'Male',inplace=True) # replace the missing values in the gender column using mode since its a categorically represented
        df['Birth Year'].replace(np.nan,df['Birth Year'].mean(),inplace=True) # replace the missing values in the birth year column using mean since it contains contionous values 
        df['Birth Year'] = df['Birth Year'].astype(int) # convert the entire birth year column to integer data type
        if month != '' and day == '': # if month is not empty and day is empty means we are filtering by MONTH
            df = df.loc[df['Start Time'].str[5:7] == months_dict.get(month)] # return a dataframe where the slice of every value in the the Start time column at index 5 and 6 (month) is equal to the month entered by the user
        elif month == '' and day != '': # if month is empty and day is not empty means we are filtering by DAY
            df = df.loc[df['Start Time'].str[8:10] == day]
        elif month != '' and day != '': # if month is not empty and day is not empty means we are filtering BOTH
            df = df.loc[(df['Start Time'].str[5:7] == months_dict.get(month)) & (df['Start Time'].str[8:10] == day)]
        elif month == '' and day == '': # if month and day is empty it means we are NOT filtering  
            df = df.copy()
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
            df = df.loc[(df['Start Time'].str[5:7] == months_dict.get(month)) & (df['Start Time'].str[8:10] == day)]
        elif month == '' and day == '': # if month and day is empty it means we are NOT filtering  
            df = df.copy()
        else:
            pass
    # WASHINGTON
    elif city.lower() == 'washington':
        df = pd.read_csv('washington.csv')
        if month != '' and day == '': # if month is not empty and day is empty means we are filtering by MONTH
            df = df.loc[df['Start Time'].str[5:7] == months_dict.get(month)]
        elif month == '' and day != '': # if month is empty and day is not empty means we are filtering by DAY
            df = df.loc[df['Start Time'].str[8:10] == day]
        elif month != '' and day != '': # if month is not empty and day is not empty means we are filtering BOTH
            df = df.loc[(df['Start Time'].str[5:7] == months_dict.get(month)) & (df['Start Time'].str[8:10] == day)]
        elif month == '' and day == '': # if month and day is empty it means we are NOT filtering  
            df = df.copy()
        else:
            pass
    return df

def time_stats(df, city, month, day):
    """Displays statistics on the most frequent times of travel."""
    print('Calculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    if month == '': # if month is empty it means there is the dataframe is not month-filtered, so most common month can be displayed
        # display the most common month: Since the dataframe to be used within this function is filtered, most common month will only be calculated for a dataframe which is not month-filtered.
        m_series = df['Start Time'].str[5:7].value_counts() # slice every value in the start time column to extract the month number, group them by the number of occurences using value_counts, a series will be returned
        m = m_series[m_series == np.max(m_series)].index[0] # the series contains the month number as index and number of occurences as value, get the maximum value and return the index(month number)
        print("The most common month in the {} data is {}".format(city.upper(),months_dict_reversed.get(m)))
    if day == '':
        # display the most common day of week: the most common day will only be calculated for a dataframe which is not day-filtered.
        d_series = df['Start Time'].str[8:10].value_counts()
        d = d_series[d_series == np.max(d_series)].index[0]
        print("The most common day in the {} data is {}".format(city.upper(), d))
    # display the most common start hour
    h_series = df['Start Time'].str[11:13].value_counts()
    h = h_series[h_series == np.max(h_series)].index[0]
    print("The most common start hour in the {} data is {} with a count of: {}".format(city.upper(), h, np.max(h_series)))        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('Calculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # display most commonly used start station
    S_stations = df['Start Station'].value_counts()
    S_max_station = S_stations[S_stations == np.max(S_stations)].index[0]
    print("The most used start station is '{}' with the count of '{}' uses.".format(S_max_station, np.max(S_stations)))
    # display most commonly used end station
    E_stations = df['End Station'].value_counts()
    E_max_station = E_stations[E_stations == np.max(E_stations)].index[0]
    print("The most used end station is '{}' with the count of '{}' uses.".format(E_max_station, np.max(E_stations)))    
    # display most frequent combination of start station and end station trip
    start = df[['Start Station']] # create a dataframe of only the Start Stations   
    end = df[['End Station']] # create a dataframe of only the End Stations 
    start.columns = ['Stations'] # rename the column name to Stations
    end.columns = ['Stations'] # rename the column name to Stations
    start.append(end) # append the end data frame to the start data frame
    startend_series = start['Stations'].value_counts() # returns a series of stations as indexes and count as values
    start_end = startend_series[startend_series == np.max(startend_series)].index[0]
    print("The most frequent combination of start station and end station trip is '{}' with the count of '{}' uses.".format(start_end, np.max(startend_series)))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('Calculating Trip Duration...\n')
    start_time = time.time()
    def time_data(seconds):
        seconds = int(seconds)
        seconds = seconds % (24 * 3600) 
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        return hour, minutes, seconds
    # display total travel time
    total = time_data(np.sum(df['Trip Duration']))
    print("The Total travel time is {} hours {} minutes and {} seconds.".format(total[0],total[1],total[2]))
    # display mean travel time
    mean = time_data(np.mean(df['Trip Duration']))
    print("The Average travel time is {} hours {} minutes and {} seconds.".format(mean[0],mean[1],mean[2]))    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)

def user_stats(df, city):
    """Displays statistics on bikeshare users."""
    print('Calculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    subscribers = len(df.loc[df['User Type'] == 'Subscriber'])
    customers = len(df.loc[df['User Type'] == 'Customer'])
    dependents = len(df.loc[df['User Type'] == 'Dependent'])
    print("There are {} Subscribers, {} Customers and {} Dependents within the {} Data".format(subscribers, customers, dependents, city))    
    
    if city.lower() == 'chicago' or city.lower() == 'new york':
        # Display counts of gender
        male = len(df.loc[df['Gender'] == 'Male'])
        female = len(df.loc[df['Gender'] == 'Female'])   
        print("There are {} Males and {} Females within the {} Data".format(male, female, city)) 
        # Display earliest, most recent, and most common year of birth
        year = df['Birth Year']
        print('\nIn the {} Data, the earliest year of birth is {},\nthe most recent is {} and the most common is {}.'.\
              format(city, str(np.min(year)), str(np.max(year)), str(np.bincount(year).argmax())))
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, city, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
