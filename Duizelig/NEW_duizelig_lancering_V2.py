import time
count=int(input("set the count : "))

while count >= 0:
    time.sleep(1)
    print(count)
    count-=1
    
    if count == -1:
        print("de raket is gelanceerd")