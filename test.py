import pandas as pd
import numpy as np
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january','february','march','april','may','june']
days = ['sun','mon','tue','wed','thu','fri','sat']

num = 1999.0
int_num = int(num)
print(int_num)

df = pd.read_csv('chicago.csv')

def time_data(seconds):
    seconds = seconds % (24 * 3600) 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return ("The total travel time is {} hours {} minutes and {} seconds.".format(hour, minutes, seconds))

print(np.sum(df['Trip Duration']))
print(time_data(np.sum(df['Trip Duration'])))