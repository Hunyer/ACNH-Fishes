import goody
import prompt
from collections import defaultdict
import json

from datetime import datetime
import pytz

def isWithinTime(fishTime) -> bool:
    currentHour = currentTime.hour

    if(currentHour in fishTime):        
        return True
    return False

def isWithinMonths(fishMonths) -> bool:
    currentMonth = currentDate.month    
    if(currentMonth in fishMonths):
        return True
    return False
    
def addFish(loaded, fishDict, fishJson):
    isAllDay = loaded['availability']['isAllDay'] #bool value
    location = loaded['availability']['location'] #location of the fish
    shadow = loaded['shadow'] #size of the shadow
    name = loaded['name']['name-USen'] #name of the fish in english
    rarity = loaded['availability']['rarity']
    
    if(isAllDay):
        fishDict[name] = '\n' + 'All Day' + '\n' + location + '\n' + shadow + '\n' + rarity + '\n' #store fish into the dict

    else:
        time = loaded['availability']['time']
        fishDict[name] = '\n' + time + '\n' + location + '\n' + shadow + '\n' + rarity + '\n'#store fish into the dict

    fishJson.append(loaded)

        
def calcFishes(loadedFish, fishDict, fishJson):
    isAllYear = loadedFish['availability']['isAllYear']
    isAllDay = loadedFish['availability']['isAllDay']
    fishTime = loadedFish['availability']['time-array']
    fishMonths = loadedFish['availability']['month-array-northern']
        
    if(isAllYear and isAllDay):
        addFish(loadedFish, fishDict, fishJson)

    elif(isAllYear and isAllDay == False):
        if(isWithinTime(fishTime)):
            addFish(loadedFish, fishDict, fishJson)

    elif(isAllYear == False and isAllDay == False):        
        if(isWithinTime(fishTime) and isWithinMonths(fishMonths)):
            addFish(loadedFish, fishDict, fishJson)

    elif(isAllYear == False and isAllDay):
         if(isWithinMonths(fishMonths)):
             addFish(loadedFish, fishDict, fishJson)
    
        
def availableFish(currentTime, currentDate) -> dict:

    fishDict = defaultdict(str)
    fishJson = []
    
    with open('fish.txt') as fishFile:
        allFishes = json.load(fishFile)        
        
        for x in allFishes.values():
            calcFishes(x, fishDict, fishJson)
                        
        fishFile.close()
    
    return fishDict, fishJson


if __name__ == '__main__':
    pst = pytz.timezone('America/Los_Angeles')
    currentTime = datetime.time(datetime.now(tz=pst))
    currentDate = datetime.date(datetime.now(tz=pst))

    fishDict, fishJson = availableFish(currentTime, currentDate)

    with open('available_fish.json', 'w') as af:
        json.dump(fishJson, af)

    for x in fishDict:
        print(x, fishDict[x])
