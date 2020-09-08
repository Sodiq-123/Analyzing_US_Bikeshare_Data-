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
        if city.lower() == 'chicago' or city.lower() == 'new york' or city.lower() == 'washington':
            while True:
                choice = input("Enter data filter type by month, day, both or not at all Type 'none' for no filter.\n") # Get the filter choice from user
                if choice.lower() == 'month':
                    month = choice
                    break
                elif choice.lower() == 'day':
                    day = choice
                    break
                elif choice.lower() == 'both':
                    month = 'yes'
                    day = 'yes'
                    break
                elif choice.lower() == 'none':
                    break
                else:
                    print('Invalid filter input, try again!') 
                    continue
            break
        else:
            print("Invalid city name, try again")
            continue
    print('-'*40)
    return city, month, day

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
