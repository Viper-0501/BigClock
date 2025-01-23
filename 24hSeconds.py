import assets, time, os
monthList = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def convertTime12(unixTimestamp):
    valueList = {}
    valueList["time"], valueList["sec"] = time.strftime("%H:%M %S", time.localtime(unixTimestamp)).split()
    dateStr = time.strftime("%a, %B %d, %Y", time.localtime(unixTimestamp))
    offsetVal = assets.getLength(valueList["time"]) - len(dateStr)
    for x in range(offsetVal-2):
        dateStr = f" {dateStr}"
    dateStr = f"{valueList["sec"]}{dateStr}"
    valueList["date"] = dateStr
    return valueList



def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        formattedTime = convertTime12(time.time())
        assets.printBig(formattedTime["time"], formattedTime["date"])
        time.sleep(1)


main()

