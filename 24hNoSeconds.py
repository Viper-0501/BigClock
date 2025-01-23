import assets, sys, time, os
monthList = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def convertTime24(unixTimestamp):
    valueList = {}
    valueList["time"] = time.strftime("%H:%M", time.localtime(unixTimestamp))
    dateStr = time.strftime("%a, %B %d, %Y", time.localtime(unixTimestamp))
    offsetVal = assets.getLength(valueList["time"]) - len(dateStr)
    for x in range(offsetVal):
        dateStr = f" {dateStr}"
    valueList["date"] = dateStr
    return valueList



def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        formattedTime = convertTime24(time.time())
        assets.printBig(formattedTime["time"])
        print(formattedTime["date"])
        nextMin = 60 - int(str(time.time()%60)[:str(time.time()%60).find(".")])
        time.sleep(nextMin)
main()