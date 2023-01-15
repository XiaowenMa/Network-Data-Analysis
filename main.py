import matplotlib.pyplot as plt
import networkx as nx
import time
import numpy as np
import itertools

from powerLaw_exponent import powerLaw_exponent
from KH_model import KH_model
from synthetic_powerLaw import synthetic_powerLaw

G,_ = synthetic_powerLaw(10000, a=2.6)

degrees = [node_degree_pair[1] for node_degree_pair in G.degree]

print(powerLaw_exponent(degrees))

# get sorted degree distribution
degrees_set = list(set(degrees))
degrees_set.sort()
degrees_proportion = [degrees.count(degree)/len(degrees) for degree in degrees_set]


# get CCDF
culmulative_density = degrees_proportion[:] # copy by value, not reference
culmulative_density.reverse()

culmulative_density = list(itertools.accumulate(culmulative_density))
culmulative_density.reverse()

plt.scatter(degrees_set, degrees_proportion)
plt.xscale('log')
plt.yscale('log')
plt.show()


'''
num_trials = 10
lst1, lst2 = [], []
cc1, cc2 = [], []

for i in range(10):

    G = KH_model(100, 3, Pt=0.3)
    G2 = nx.barabasi_albert_graph(100, 3)

    # get degree count
    G_degrees = [node_degree_pair[1] for node_degree_pair in G.degree]
    G2_degrees = [node_degree_pair[1] for node_degree_pair in G2.degree]

    lst1.append(powerLaw_exponent(G_degrees))
    lst2.append(powerLaw_exponent(G2_degrees))

    cc1.append(nx.average_clustering(G))
    cc2.append(nx.average_clustering(G2))

print(f'KH model a: {np.mean(lst1)}, std: {np.std(lst1)}, cc: {np.mean(cc1)}')
print(f'BA model a: {np.mean(lst2)}, std: {np.std(lst2)}, cc: {np.mean(cc2)}')
'''