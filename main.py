import assets, sys, time, os

try: 
    clockMode = sys.argv[1]
except:
    print("clockMode not specified, defaulting to 24h")
    for x in range(5):
        y = 5 - x
        print(f"Continuing in {y}", end="\r")
        time.sleep(1)


while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    time = time.time()
    
