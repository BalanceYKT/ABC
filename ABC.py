import numpy as np
import matplotlib.pyplot as plt


class Bee:
    x = None
    y = None
    F = None


# ---------------------- CONST ---------------------------
X = 10
Y = 10
TAU = 5
Tau = TAU
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
    return 20 - 20 * np.exp(-0.2 * np.sqrt(1.0 / 2 * sum(x ** 2 for x in individual))) + np.e - np.exp(1.0 / 2 * sum(np.cos(2 * np.pi * x) for x in individual))

def Rosenbrock(x, y):
        return 100 * (y - x**2)**2 + (x - 1) ** 2

def Rastrigin(x, y):
    return x**2 - 10 * np.cos(2*np.pi*(x)) + 10 + y**2 - 10 * np.cos(2*np.pi*(y)) + 10


def Sphere(x, y):
    return x**2 + y**2



def printBeeData(bee):
    s = "x = " + str(bee.x) + "; y = " + str(bee.y) + "; F = " + str(bee.F)

def isOnSquare(bee_one, bee_two):
    if np.sqrt((bee_one.x - bee_two.x) ** 2 + (bee_one.y - bee_two.y) ** 2) <= Radius:
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
        Bees.x = np.random.uniform(BeePoint.x - Radius, BeePoint.x + Radius)
        Bees.y = np.random.uniform(BeePoint.y - Radius, BeePoint.y + Radius)
        Bees.F = Sphere(Bees.x, Bees.y)
        Bee_arr.append(Bees)


def get_F(Bee):
    return Bee.F


# ---------------------- INIT ----------------------------
Bee_arr = []
Iterations = []
Areas = []
BestArea_arr = []
PotentialArea_arr = []
MIN_arr = []
MAX_arr = []


# ---------------------------------------------------------
for i in range(BeeCount):
    Bees = Bee()
    Bees.x = np.random.uniform(-X_Rastrigin, X_Rastrigin)
    Bees.y = np.random.uniform(-Y_Rastrigin, Y_Rastrigin)
    Bees.F = Sphere(Bees.x, Bees.y)
    Bee_arr.append(Bees)

# reverse = True

Bee_arr.sort(key=get_F)
MIN = Bee_arr[0].F
Extr = Bee_arr[0].F
count = 1
otr = []

while (Tau > 0):
    newIteration = []
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
        newIteration.append(newArea)
        if temp >= AreaCount:
            break
    Bee_arr = []

    if (MIN == Areas[0][0].F):
        Tau -= 1
        if Radius == 0.1:
            Radius = 0.1
        else:
            Radius -= 0.3
    else:
        Radius = 1
        Tau = 5

    MIN = Areas[0][0].F


    for i in range(len(Areas)):
        generate(Areas[i][0])
        # MIN_arr.append(Areas[i][0].F)

    Areas.sort(key= lambda X: X[0].F)
    Extr = Areas[0][0].F
    Iterations.append(newIteration)





# ---------------------- OUTPUT ----------------------

print("EXTREMUM : " + str(Extr))
print("COUNT : " + str(count))

x = []
y = []

iter_num = len(Iterations)
iter_show_num = 5

for i in range(0, iter_num, int(iter_num / iter_show_num)):

    iteration = Iterations[i]
    area_count = len(iteration)
    area_colors = np.random.rand(area_count)
    print("iteration " + str(i) + " have " + str(area_count) + " areas")

    colors = []
    x = []
    y = []
    for j in range(area_count):
        area = iteration[j]
        bee_in_area_count = len(area)
        print("area " + str(j) + " have " + str(bee_in_area_count) + " bees")
        for k in range(bee_in_area_count):
            bee = area[k]
            x.append(bee.x)
            y.append(bee.y)
            colors.append(area_colors[j])

    plt.scatter(x, y, c=colors, alpha=0.5)
    plt.savefig('plot' + str(i))
