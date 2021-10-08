import time

print("de raket wordt gelanceerd over 30 seconden")
time.sleep(1)

lancering = 0
for lancering in range(29,-1,-1):

 while lancering >=0:
    time.sleep(1)
    print(lancering)
    
if lancering == 0:
    print("raket is gelanceerd")