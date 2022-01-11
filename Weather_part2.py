# empty set called rate is created
rate = []

import json
with open ('result1.json') as file:
    data = json.load(file)
# Made a variable where the monthly precipitation values were summed
    yearly_rain = sum(data)
for x in data:
# divided each element of the list by the yearly sum of rain
   relativerain = (x/yearly_rain)
   relativerain = round(relativerain,2)
   rate.append(relativerain)
print(rate)

# Saved the list as a Json file
with open('result2.json', 'w') as relativerain_file:
        json.dump( rate, relativerain_file)