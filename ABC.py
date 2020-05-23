import numpy as np
#

class Bee:
    x1 = None
    x2 = None
    x3 = None
    x4 = None
    x5 = None
    x6 = None
    x7 = None
    x8 = None
    x9 = None
    x10 = None
    F = None


# ---------------------- CONST ---------------------------
X = 100
Y = 100
TAU = 10
Tau = TAU
NUJ = 0.1
BeeCount = 50
BestBeeCount = 50
PotentialBeeCount = 30
MIN = None
MAX = None
Extr = None
Radius = 1
AreaCount = 7
BestAreaCount = 5
PotentialAreaCount = 2
Repeat = 0
X_Rastrigin = 5
Y_Rastrigin = 5


# ---------------------- FUNCTIONS ----------------------------
def Griewank(x, y):
    return (x**2 + y**2)/4000 - ((np.cos(x)) * (np.cos(y / np.sqrt(2)))) + 1

def Ackley(x, individual):
    return 20 - 20 * np.exp(-0.2 * np.sqrt(1.0 / N * sum(x ** 2 for x in individual))) + np.e - np.exp(1.0 / N * sum(np.cos(2 * np.pi * x) for x in individual))

def Rosenbrock(x, y):
        return 100 * (y - x**22)**2 + (x - 1) ** 2

def Rastrigin(x, y):
    return x**2 - 10 * np.cos(2*np.pi*(x)) + 10 + y**2 - 10 * np.cos(2*np.pi*(y)) + 10


def Sphere(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10):
    return x1**2 + x2**2 + x3**2 + x4**2 + x5**2 +x6**2 +x7**2 + x8**2 + x9**2 + x10**2



def printBeeData(bee):
    print("x = " + str(bee.x) + "; y = " + str(bee.y) + "; F = " + str(bee.F))

def isOnSquare(bee_one, bee_two):
    if np.sqrt((bee_one.x1 - bee_two.x1) ** 2 + (bee_one.x2 - bee_two.x2) ** 2 + (bee_one.x3 - bee_two.x3) ** 2 + (bee_one.x4 - bee_two.x4) ** 2 + (bee_one.x5 - bee_two.x5) ** 2 + (bee_one.x6 - bee_two.x6) ** 2 + (bee_one.x7 - bee_two.x7) ** 2 + (bee_one.x8 - bee_two.x8) ** 2 + (bee_one.x9 - bee_two.x9) ** 2 + (bee_one.x10 - bee_two.x10) ** 2) <= Radius:
        return True
    else:
        return False

"""
def isOnSquare(bee_one, bee_two):
    if abs(bee_one.x - bee_two.x) <= Radius and abs(bee_one.y - bee_two.y) <= Radius:
        return True
    else:
        return False
"""


def generate(BeePoint):
    for i in range(BeeCount):
        Bees = Bee()
        Bees.x1 = np.random.uniform(BeePoint.x1 - Radius, BeePoint.x1 + Radius)
        Bees.x2 = np.random.uniform(BeePoint.x2 - Radius, BeePoint.x2 + Radius)
        Bees.x3 = np.random.uniform(BeePoint.x3 - Radius, BeePoint.x3 + Radius)
        Bees.x4 = np.random.uniform(BeePoint.x4 - Radius, BeePoint.x4 + Radius)
        Bees.x5 = np.random.uniform(BeePoint.x5 - Radius, BeePoint.x5 + Radius)
        Bees.x6 = np.random.uniform(BeePoint.x6 - Radius, BeePoint.x6 + Radius)
        Bees.x7 = np.random.uniform(BeePoint.x7 - Radius, BeePoint.x7 + Radius)
        Bees.x8 = np.random.uniform(BeePoint.x8 - Radius, BeePoint.x8 + Radius)
        Bees.x9 = np.random.uniform(BeePoint.x9 - Radius, BeePoint.x9 + Radius)
        Bees.x10 = np.random.uniform(BeePoint.x10 - Radius, BeePoint.x10 + Radius)
        Bees.F = Sphere(Bees.x1, Bees.x2, Bees.x3, Bees.x4, Bees.x5, Bees.x6, Bees.x7, Bees.x8, Bees.x9, Bees.x10)
        Bee_arr.append(Bees)


def get_F(Bee):
    return Bee.F


# ---------------------- INIT ----------------------------
Bee_arr = []
Areas = []
BestArea_arr = []
PotentialArea_arr = []
MIN_arr = []
MAX_arr = []


# ---------------------------------------------------------
for i in range(BeeCount):
    Bees = Bee()
    Bees.x1 = np.random.uniform(-X, X)
    Bees.x2 = np.random.uniform(-X, X)
    Bees.x3 = np.random.uniform(-X, X)
    Bees.x4 = np.random.uniform(-X, X)
    Bees.x5 = np.random.uniform(-X, X)
    Bees.x6 = np.random.uniform(-X, X)
    Bees.x7 = np.random.uniform(-X, X)
    Bees.x8 = np.random.uniform(-X, X)
    Bees.x9 = np.random.uniform(-X, X)
    Bees.x10 = np.random.uniform(-X, X)
    Bees.F = Sphere(Bees.x1, Bees.x2, Bees.x3, Bees.x4, Bees.x5, Bees.x6, Bees.x7, Bees.x8, Bees.x9, Bees.x10,)
    Bee_arr.append(Bees)

# reverse = True

Bee_arr.sort(key=get_F)
MIN = Bee_arr[0].F
Extr = Bee_arr[0].F
count = 1

while (Tau > 0):
        count += 1
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
        Bee_arr = []

        if (MIN == Areas[0][0].F):
            Tau -= 1
            if Radius == 0.1:
                NUJ *= NUJ
            else:
                Radius -= NUJ
        else:
            Radius = 1
            Tau = 10

        MIN = Areas[0][0].F


        for i in range(len(Areas)):
            generate(Areas[i][0])
            # MIN_arr.append(Areas[i][0].F)

        Areas.sort(key= lambda X: X[0].F)
        Extr = Areas[0][0].F





# ---------------------- OUTPUT ----------------------
print("Global min: " + str(MIN))

"""for i in range(len(Areas)):
    print(str(i + 1) + " area")
    # print("min in area: " + str(MIN_arr[i]))
    for j in range(len(Areas[i])):
        printBeeData(Areas[i][j])
"""
print("EXTREMUM : " + str(Extr))
print("COUNT : " + str(count))
