from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')

# Jouw python instructies zet je vanaf hier:
robotArm.moveRight()
for rij in range(1):
    for blok in range(7):
        robotArm.grab()
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()