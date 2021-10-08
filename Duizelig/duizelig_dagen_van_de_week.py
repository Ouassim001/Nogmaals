weekMaandag = ["dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]
weekDinsdag = ["woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]
weekWoensdag = ["donderdag", "vrijdag", "zaterdag", "zondag"]
weekDonderdag = ["vrijdag", "zaterdag", "zondag"]
weekVrijdag = ["zaterdag", "zondag"]
weekZaterdag = ["zondag"]
weekZondag = ["zondag"]





ma = "maandag"
di = "dinsdag"
wo = "woensdag"
do = "donderdag"
vr = "vrijdag" 
za = "zaterdag"
zo = "zondag"

dag = input("kies een dag.")
while True:
    if ma == dag:
        break
    else:
        print(weekMaandag)

    if di == dag:
        break
    else:
        print(weekDinsdag)

    if wo == dag:
        break
    else:
        print(weekWoensdag)

    if do == dag:
        break
    else:
        print(weekDonderdag)

    if vr == dag:
        break
    else:
        print(weekVrijdag)

    if za == dag:
        break
    else:
        print(weekZaterdag)

    if zo == dag:
        break
    else:
        print(weekZondag)
    

