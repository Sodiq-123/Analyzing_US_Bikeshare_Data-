import pandas as pd
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january','february','march','april','may','june']
days = ['sun','mon','tue','wed','thu','fri','sat']

num = 1999.0
int_num = int(num)
print(int_num)

df = pd.read_csv('chicago.csv')
print(type(df))

stations = []
stations.extend(df['Start Station'].to_list())
stations.extend(df['End Station'].to_list())

stations_dict = dict(zip(stations, [stations.count(i) for i in stations]))
print(stations_dict)