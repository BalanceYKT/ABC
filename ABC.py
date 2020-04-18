import numpy as np

class Bee:

    x = 0
    y = 0
    F = 0


# ---------------------- CONST ---------------------------
X = 1000
Y = 1000
Tau = 5
BeeCount = 100
BestBeeCount = 50
PotentialBeeCount = 30
MIN = 0
MAX = 0
Radius = 5
AreaCount = 7
BestAreaCount = 5
PotentialAreaCount = 2


# ---------------------- FUNCTIONS ----------------------------
def Sphere(x, y):
    return x**2 + y**2

def printBeeData(bee):
  print("x = " + str(bee.x) + "; y = " + str(bee.y)+ "; F = " + str(bee.F))

def isOnSquare(bee_one, bee_two):
    if abs(bee_one.x - bee_two.x) <= Radius and abs(bee_one.y - bee_two.y) <= Radius:
        return True
    else:
        return False


# ---------------------- INIT ----------------------------
SETKA = np.zeros((X, Y))
Bee_arr = []
Areas = []
Area_arr = []
BestArea_arr = []
PotentialArea_arr = []

#---------------------------------------------------------
for i in range(BeeCount):
    Bees = Bee()
    Bees.x = np.random.randint(0, 20)
    Bees.y = np.random.randint(0, 20)
    Bees.F = Sphere(Bees.x, Bees.y)
    Bee_arr.append(Bees)


def get_F(Bee):
    return Bee.F

Bee_arr.sort(key=get_F)

rest = Bee_arr
while (len(rest) > 0):
  newRest = []
  main_bee = rest[0]
  newArea = [main_bee]
  for i in range(1, len(rest)):
      if isOnSquare(main_bee, rest[i]):
        newArea.append(rest[i])
      else:
        newRest.append(rest[i])
  rest = newRest
  Areas.append(newArea)


for i in range(len(Areas)):
  print(str(i) + " area")
  for j in range(len(Areas[i])):
    printBeeData(Areas[i][j])
  print()