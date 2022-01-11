
#created an empty list called Seattle
Seattle = []

import json
with open ('precipitation.json') as file:
    data = json.load(file)
    # created 12 different indexes with the value zero called sum
    sum = [0]*12
for x in data: 
    # sorted by station name - to filter for location Seattle
    stationname = (x['station'])
    if stationname == 'GHCND:US1WAKG0038':
        # split the date and indexed the second value to acess the month
        date = (x['date'])
        month = (date.split('-'))
        month = (month[1])
        #the index of the monthly sum in the list is month - 1
        index = (int(month)) - 1
        rain = (x['value'])
        #running sum total of precipitation values of a specific month
        sum[index] = sum[index] + rain
Seattle = sum
print(Seattle)

# list Seattle is saved as a Json file
with open('result1.json', 'w') as seattle_file:
        json.dump( Seattle, seattle_file)

            
    
        

    
    

