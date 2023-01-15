import numpy as np
import matplotlib.pyplot as plt

from powerLaw_exponent import powerLaw_exponent
from synthetic_powerLaw import synthetic_powerLaw

alpha = [1.5, 2, 3, 4]
actual_a = []

for a in alpha:

    G,_ = synthetic_powerLaw(10000, a)
    degrees = [node_degree_pair[1] for node_degree_pair in G.degree]

    degrees_set = list(set(degrees))
    degrees_proportion = [degrees.count(degree)/len(degrees) for degree in degrees_set]
    plt.scatter(degrees_set, degrees_proportion, label=f"a={a}")

plt.title("Power-law Degree Distribution on a log-log scale")
plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.xlabel("Degree")
plt.ylabel("Proportion")
plt.show()




