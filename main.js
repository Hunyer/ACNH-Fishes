
function isWithinTime(fishTime)
{
    let d = new Date();
    let hour = d.getHours();    
    if(fishTime.includes(hour))
    {        
        return true;
    }
    return false;
}

function isWithinMonths(fishMonths)
{
    let d = new Date();
    let month = d.getMonth() + 1;
        
    if(fishMonths.includes(month))
    {        
        return true;
    }
    return false;
}

function calcFishes(fishName, loadedFish, fishDict)
{
    isAllYear = loadedFish["availability"]["isAllYear"];
    isAllDay = loadedFish['availability']['isAllDay'];
    fishTime = loadedFish['availability']['time-array'];
    fishMonths = loadedFish['availability']['month-array-northern'];        

    if(isAllYear && isAllDay)
    {
        fishDict[fishName] = loadedFish;
    }
    else if(isAllYear && isAllDay == false)
    {
        if(isWithinTime(fishTime))
        {
            fishDict[fishName] = loadedFish;            
        }
    }
    else if(isAllYear == false && isAllDay == false)
    {
        if(isWithinTime(fishTime) && isWithinMonths(fishMonths))
        {
            fishDict[fishName] = loadedFish;
        }
    }
    else if(isAllYear == false && isAllDay)
    {
        if(isWithinMonths(fishMonths))
        {
            fishDict[fishName] = loadedFish;
        }
    }
}

function availableFish() 
{
    fishDict = {};
    let fishFile = require("./fishes.json");

    for(let x in fishFile) //x is every k of fishFile
    {
        let fishValue = fishFile[x]; 
        calcFishes(x, fishValue, fishDict);
    }
    return fishDict;
}

function main() 
{    
    fishDict = availableFish();        
    console.log(Object.keys(fishDict));
}

main();