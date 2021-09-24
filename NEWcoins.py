# name of student: 
# number of student:
# purpose of program: 
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) #hoeveelheid om te betalen
payed = int(float(input('Payed amount: ')) * 100) #hoeveelheid betaalt
change = payed - toPay #wisselgeld
if change > 0: #als het groter is dan 0 dan 500 cent wisselgeld
  coinValue = 500
  while change > 0 and coinValue > 0: #
    nrCoins = change // coinValue #

    if nrCoins > 0: #
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #hoeveelheid coins terug
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #hoeveel coins heb je teruggegeven
      change -= nrCoinsReturned * coinValue #wisselgeld is coins teruggegeven maal de waarde van de coins
      print(nrCoinsReturned, 'of ', coinValue )
# comment on code below: 
    if coinValue == 500:
      coinValue = 300
    elif coinValue == 300:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 100
    elif coinValue == 100:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    else:
      coinValue = 0

if change > 0: #als wisselgeld groter is dan 0 print onderstaande
  print('Change not returned: ', str(change) + ' cents')
elif change < 0:
  print("not enough")
else:
  print('done')