import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

from synthetic_powerLaw import synthetic_powerLaw

f = open("facebook_combined.txt")
G_fb = nx.read_edgelist(f)
f.close()

fb_degrees =  [node_degree_pair[1] for node_degree_pair in G_fb.degree]

# get sorted degree distribution
fb_degrees_set = list(set(fb_degrees))
fb_degrees_set.sort()
fb_degrees_proportion = [fb_degrees.count(degree)/len(fb_degrees) for degree in fb_degrees_set]

plt.scatter(fb_degrees_set, fb_degrees_proportion, label='facebook')

G,_ = synthetic_powerLaw(4039, a=2.3)
degrees = [node_degree_pair[1] for node_degree_pair in G.degree]

degrees_set = list(set(degrees))
degrees_set.sort()
degrees_proportion = [degrees.count(degree)/len(degrees) for degree in degrees_set]

plt.scatter(degrees_set, degrees_proportion, label='synthetic')

G = nx.barabasi_albert_graph(4039, 20)
degrees = [node_degree_pair[1] for node_degree_pair in G.degree]

degrees_set = list(set(degrees))
degrees_set.sort()
degrees_proportion = [degrees.count(degree)/len(degrees) for degree in degrees_set]

plt.scatter(degrees_set, degrees_proportion, label='BA_model')

plt.title("Power-law Degree Distribution on a log-log scale")
plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.xlabel("Degree")
plt.ylabel("Proportion")
plt.show()