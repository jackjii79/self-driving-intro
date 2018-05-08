#!/usr/bin/python3.5
import matplotlib.pyplot as plt
from scipy.stats import norm

### 
# The plot_fill function plots a probability density function and also
# shades the area under the curve between x_prob_min and x_prob_max.
# INPUTS:
# x: x-axis values for plotting
# x_prob_min: minimum x-value for shading the visualization
# x_prob_max: maximum x-value for shading the visualization
# y_lim: the highest y-value to show on the y-axis
# title: visualization title
#
# OUTPUTS:
# prints out a visualization
### 

def plot_fill(x, x_prob_min, x_prob_max, y_lim, title):
    # Calculate y values of the probability density function
    # Note that the pdf method can accept an array of values from numpy linspace.
    y = norm(loc = 50, scale = 10).pdf(x) #we can also calculate the corresponding cdf by norm(loc=..,scale=..).cdf(x) where loc is mean and scale is stdev
    
    # Calculate values for filling the area under the curve
    x_fill = np.linspace(x_prob_min, x_prob_max, 1000)
    y_fill = norm(loc = 50, scale = 10).pdf(x_fill)
    
    # Plot the results
    plt.plot(x, y)
    plt.fill_between(x_fill, y_fill)
    plt.title(title)
    plt.ylim(0, y_lim)#we set the limits of y ,ylim(ymin,ymax) here ymin is 0 and ymax is 0.05
    plt.xticks(np.linspace(0, 100, 21))
    plt.xlabel('Temperature (Fahrenheit)')
    plt.ylabel('probability density function')
    plt.show()

average = 50
stdev = 10
y_lim = 0.05
x = np.linspace(0, 100, 1000)

plot_fill(x, 0, 50, y_lim,
          'Gaussian Distribution, Average = ' + str(average) + ', Stdev ' + str(stdev))
