#!/usr/bin/python3.5
import matplotlib.pyplot as plt

def uniform_distribution_height(a, b):
 return 1 / (b - a)

y = uniform_distribution_height(0, 360)

plt.plot([0, 360], [y, y], color='blue')
plt.plot([0, 0], [0, y], '--', color='blue', )
plt.plot([360, 360], [0, y], '--', color='blue', )
plt.ylim([0, y + y/2])

plt.xlabel('Degrees')
plt.ylabel('Probability Distribution')
plt.title('Uniform Probability Distribution \n for a Spinning Bottle')
plt.xticks(range(0, 361, 30))
plt.show()
