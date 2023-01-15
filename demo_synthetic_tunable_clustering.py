import networkx as nx
import numpy as np

from cluster_synthetic_powerLaw import cluster_synthetic_powerLaw
from synthetic_powerLaw import synthetic_powerLaw
from powerLaw_exponent import powerLaw_exponent

cc = []
for i in range(10):
    G1, _ = synthetic_powerLaw(1000, a=2)
    G2, _ = cluster_synthetic_powerLaw(1000, a=4, Pt=1)

    degrees_1 = [node_degree_pair[1] for node_degree_pair in G1.degree]
    degrees_2 = [node_degree_pair[1] for node_degree_pair in G2.degree]

    cc.append(nx.average_clustering(G2))

print(np.mean(cc))
