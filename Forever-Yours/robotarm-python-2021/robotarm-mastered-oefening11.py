from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')

# Jouw python insructies zet je vanaf hier:
robotArm.speed = 5
for rij in range(10):
    robotArm.grab()
    color = robotArm.scan()
    if color =="white":
        robotArm.moveRight()
        robotArm.drop()
    robotArm.moveRight()
   





# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()