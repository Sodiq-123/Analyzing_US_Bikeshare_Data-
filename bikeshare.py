import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
month = ''
day = ''
def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        city = input("Enter the city you like to view data on between Chicago, New york, or Washington\n") # Get city of choice from user
        if city.lower() == 'chicago' or city.lower() == 'new york' or city.lower() == 'washington': # If the city entered is either of the cities provided
            while True:
                choice = input("Enter data filter type by month, day, both or not at all Type 'none' for no filter.\n") # Get the filter choice from user
                if choice.lower() == 'month': # if the filter choice by the user is MONTH
                    month = choice # assign the month variable to choice('month')
                    break #break the loop
                elif choice.lower() == 'day': # if the filter choice by the user is DAY
                    day = choice # assign the day variable to choice('day')
                    break #break the loop
                elif choice.lower() == 'both': # if the filter choice by the user is BOTH
                    month = 'yes' # assign the month variable to yes
                    day = 'yes' # assign the day variable to yes
                    break #break the loop
                elif choice.lower() == 'none': # if the filter choice by the user is NONE
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
    """Chicago"""
    if city == chicago
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
