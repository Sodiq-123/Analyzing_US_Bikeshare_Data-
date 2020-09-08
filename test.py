CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january','february','march','april','may','june']
days = ['sun','mon','tue','wed','thu','fri','sat']

num = 1999.0
int_num = int(num)
print(int_num)

days = []
for i in range(1,32):
    if i <= 9:
        days.append('0'+str(i))
    else:
        days.append(str(i))
print(days)