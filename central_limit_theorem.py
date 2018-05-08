#!/usr/bin/python3.5

#following function will randomly choose a sample list of sample_size from population_data set
def random_sample(population_data, sample_size):
    return np.random.choice(population_data, size = sample_size)

#calculate the sample mean
def sample_mean(sample):
    return np.mean(sample)

#we randomly choose #iterations number of samples of size n
def central_limit_theorem(population, n, iterations):
    sample_means_results = []
    for i in range(iterations):
        # get a random sample from the population of size n
        sample = random_sample(population, n)
        
        # calculate the mean of the random sample 
        # and append the mean to the results list
        sample_means_results.append(sample_mean(sample))
    return sample_means_results

#visualize the results
import matplotlib.pyplot as plt
def visualize_results(sample_means):
    plt.hist(sample_means, bins = 30)
    plt.title('Histogram of the Sample Means')
    plt.xlabel('Mean Value')
    plt.ylabel('Count')
