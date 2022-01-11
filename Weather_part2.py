rate = []

import json
with open ('result1.json') as file:
    data = json.load(file)
print(data)
yearly_rain = sum(data)
print(yearly_rain)
for x in data:
   relativerain = (x/yearly_rain)
   relativerain = round(relativerain,2)
   rate.append(relativerain)
print(rate)

with open('result2.json', 'w') as relativerain_file:
        json.dump( rate, relativerain_file)