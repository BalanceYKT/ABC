import matplotlib.pyplot as plt
import numpy as np


fruits = ["apple", "peach", "orange", "bannana", "melon"]
bees = [10, 20, 30, 40, 50]
counts = [10, 20, 43, 31, 17]


color_rectangle = [[0.12667976, 0.24576586, 0.20662157],
 [0.10393054,0.73387493,0.26943051],
 [0.82215833,0.52483819,0.08072223],
 [0.65688829,0.0405407, 0.5929251 ],
 [0.84813705,0.71782068,0.78441227],
 [0.95170892,0.3300486, 0.13282495],
 [0.73559197,0.48829551,0.60693618]]

#color_rectangle = np.random.rand(7, 3)

plt.bar(bees, counts, color = color_rectangle, width=10)
#plt.title("Fruits!")
plt.xlabel("Число агентов-разведчиков")
plt.ylabel("Число итераций")
plt.show()

"""
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 8)
y = np.random.randint(1, 10, size = 7)


fig, ax = plt.subplots()

ax.bar(x, y, color = 'red')


fig.set_figwidth(12)    #  ширина и
fig.set_figheight(6)    #  высота "Figure"
fig.set_facecolor('floralwhite')
ax.set_facecolor('seashell')

plt.show()

"""
