import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()

n = 1000
kmin = 1
a = 1.1
degrees_2 = []
# generate power-law degrees
for i in range(n):
    u = rng.uniform()
    k = round(np.e ** (np.log(u * (kmin ** (1 - a))) / (1 - a)))
    while(k > n):
        u = rng.uniform()
        k = round(np.e ** (np.log(u * (kmin ** (1 - a))) / (1 - a)))
    degrees_2.append(k)

degrees_2_set = list(set(degrees_2))
degrees_proportion = [degrees_2.count(degree)/len(degrees_2) for degree in degrees_2_set]

plt.scatter(degrees_2_set, degrees_proportion, label="a=1.1")

n = 1000
kmin = 1
a = 2
degrees_2 = []
# generate power-law degrees
for i in range(n):
    u = rng.uniform()
    k = round(np.e ** (np.log(u * (kmin ** (1 - a))) / (1 - a)))
    while(k > n):
        u = rng.uniform()
        k = round(np.e ** (np.log(u * (kmin ** (1 - a))) / (1 - a)))
    degrees_2.append(k)

degrees_2_set = list(set(degrees_2))
degrees_proportion = [degrees_2.count(degree)/len(degrees_2) for degree in degrees_2_set]

plt.scatter(degrees_2_set, degrees_proportion, label="a=2")

n = 1000
kmin = 1
a = 3
degrees_2 = []
# generate power-law degrees
for i in range(n):
    u = rng.uniform()
    k = round(np.e ** (np.log(u * (kmin ** (1 - a))) / (1 - a)))
    while(k > n):
        u = rng.uniform()
        k = round(np.e ** (np.log(u * (kmin ** (1 - a))) / (1 - a)))
    degrees_2.append(k)

degrees_2_set = list(set(degrees_2))
degrees_proportion = [degrees_2.count(degree)/len(degrees_2) for degree in degrees_2_set]

plt.scatter(degrees_2_set, degrees_proportion, label="a=3")

n = 1000
kmin = 1
a = 4
degrees_2 = []
# generate power-law degrees
for i in range(n):
    u = rng.uniform()
    k = round(np.e ** (np.log(u * (kmin ** (1 - a))) / (1 - a)))
    while(k > n):
        u = rng.uniform()
        k = round(np.e ** (np.log(u * (kmin ** (1 - a))) / (1 - a)))
    degrees_2.append(k)

degrees_2_set = list(set(degrees_2))
degrees_proportion = [degrees_2.count(degree)/len(degrees_2) for degree in degrees_2_set]

plt.scatter(degrees_2_set, degrees_proportion, label="a=4")



plt.title("Power-law Degree Distribution on a log-log scale")
plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.xlabel("Degree")
plt.ylabel("Proportion")
plt.show()