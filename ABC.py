import numpy as np


class Bee:
    x = None
    y = None
    F = None


# ---------------------- CONST ---------------------------
X = 1000
Y = 1000
TAU = 5
Tau = TAU
BeeCount = 100
BestBeeCount = 50
PotentialBeeCount = 30
MIN = 0
MAX = 0
Radius = 3
AreaCount = 7
BestAreaCount = 5
PotentialAreaCount = 2


# ---------------------- FUNCTIONS ----------------------------
def Sphere(x, y):
    return x ** 2 + y ** 2


def printBeeData(bee):
    print("x = " + str(bee.x) + "; y = " + str(bee.y) + "; F = " + str(bee.F))


def isOnSquare(bee_one, bee_two):
    if abs(bee_one.x - bee_two.x) <= Radius and abs(bee_one.y - bee_two.y) <= Radius:
        return True
    else:
        return False


# ---------------------- INIT ----------------------------
SETKA = np.zeros((X, Y))
Bee_arr = []
Areas = []
BestArea_arr = []
PotentialArea_arr = []
ALL = []
MIN_arr = []
MAX_arr = []


# ---------------------------------------------------------
for i in range(BeeCount):
    Bees = Bee()
    Bees.x = np.random.randint(0, 20)
    Bees.y = np.random.randint(0, 20)
    Bees.F = Sphere(Bees.x, Bees.y)
    Bee_arr.append(Bees)


def get_F(Bee):
    return Bee.F


Bee_arr.sort(key=get_F)

temp = 0
rest = Bee_arr
while (len(rest) > 0):
    temp += 1
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
    if temp >= AreaCount:
        break

MIN = Areas[0][0].F
for i in range(AreaCount):
    MIN_arr.append(Areas[i][0].F)

while (Tau != 0):
    if Tau > 0:

        Tau -= 1
    else:
        Tau = TAU


# ---------------------- OUTPUT ----------------------
print("Global min: " + str(MIN))
for i in range(len(Areas)):
    print(str(i + 1) + " area")
    print("min in area: " + str(MIN_arr[i]))
    for j in range(len(Areas[i])):
        printBeeData(Areas[i][j])
