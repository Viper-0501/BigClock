import assets, sys, time, os

def convertTime(timestamp):
    valueList = {}
    valueList["year"] = 1970
    while timestamp > 31536000:
        timestamp = timestamp - 31536000
        valueList["year"] = valueList["year"] + 1
    return valueList

def getMode():
    valid = ["-24", "-12"]
    try: 
        clockMode = sys.argv[1]
        if clockMode not in valid:
            raise ValueError("first arg must be '', '-12', or '-24'")
    except:
        print("clockMode not specified, defaulting to 24h")
        
        for x in range(5):
            y = 5 - x
            print(f"Continuing in {y}", end="\r")
            time.sleep(1)
    return clockMode





    
