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

month = "march"
months.insert(0,'december')
print(months)