
Seattle = []

import json
with open ('precipitation.json') as file:
    data = json.load(file)
    sum = [0]*12
for x in data: 
    stationname = (x['station'])
    if stationname == 'GHCND:US1WAKG0038':
        date = (x['date'])
        month = (date.split('-'))
        month = (month[1])
        index = (int(month)) - 1
        rain = (x['value'])
        sum[index] = sum[index] + rain
Seattle = sum
print(Seattle)

with open('result1.json', 'w') as seattle_file:
        json.dump( Seattle, seattle_file)

            
    
        

    
    

