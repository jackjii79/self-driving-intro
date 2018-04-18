#!/usr/bin/python3.5
import matplotlib.pyplot as plt

def bar_heights(intervals, relative_probabilities, total_probability):
    heights = []
    #TODO: sum the relative probabilities
    total_relative_prob = sum(relative_probabilities)
    heights = [(total_probability/total_relative_prob)*relative_probabilities[i-1]/(intervals[i]-intervals[i-1]) for i in range(1,len(intervals))]
    return heights

hour_intervals = [0, 5, 10, 16, 21, 24]
probability_intervals = [1, 5, 3, 6, 1/2]
accident_probability = 0.05

heights = bar_heights(hour_intervals, probability_intervals, accident_probability)

for i in range(len(probability_intervals)):
    plt.plot([hour_intervals[i], hour_intervals[i+1]], [heights[i], heights[i]], color='blue') 
    plt.plot([hour_intervals[i], hour_intervals[i]], [0, heights[i]], '--', color='blue')
    plt.plot([hour_intervals[i+1], hour_intervals[i+1]], [0, heights[i]], '--', color='blue')

plt.xticks(range(0,25,1))
plt.xlabel('hours')
plt.ylabel('probability density function')
plt.title('Probability Density Function \n for Car Accidents During the Day')
plt.show()
