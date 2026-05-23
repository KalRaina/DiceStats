
from scipy.stats import chisquare

import numpy as np
import matplotlib.pyplot as plt

arr = []

for i in range (1,1000):
  randNum = np.random.randint(1,11)
  arr.append(randNum)
arr = np.array(arr)

plt.hist(arr, bins = np.arange(1,12)-0.5,
         edgecolor = "black",
         ) # bins is how many intervals

plt.xticks(range(1,11))
plt.yticks(np.arange(0,140,10))
plt.title("Random Distribution of a 10 sided dice")

sampleMean = np.mean(arr) # mean of all values, theoretically 5.5
print("Sample mean: ",sampleMean)

sample_Var = np.var(arr) # variance of distribution, theoretically 8.25, average squared distance from the mean
print("Sample variance: ",sample_Var)
sample_StandardDeviation = np.sqrt(sample_Var) # standard deviation - average distance from mean in original units

print("Sample standard deviation:", sample_StandardDeviation)
print("Theoretical mean: ",5.5)
print("Theoretical variance: ",8.25)
print("Theoretical standard deviation (to 2d.p): ",2.87)

unique, counts = np.unique(arr, return_counts=True)
experimental = counts / len(arr)

for face, prob in zip(unique, experimental):
    print(face, prob) # experimental probability of each number appearing, based on results

chi_stat, p_value = chisquare(counts)  

print("\nChi-square statistic:", chi_stat) # chi square -> a measure of how far values deviate from expected
print("p-value:", p_value) # probability of seeing this uneveness in stats by chance

plt.show()