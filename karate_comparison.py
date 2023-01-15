import networkx as nx
import numpy as np

from KH_model import KH_model
from powerLaw_exponent import powerLaw_exponent


# import Karate club dataset and get statistics
G_karate = nx.karate_club_graph()
print(G_karate.number_of_nodes())
print(G_karate.number_of_edges())
print(nx.average_clustering(G_karate))
karate_degree = [node_degree_pair[1] for node_degree_pair in G_karate.degree]
print(powerLaw_exponent(karate_degree))

ccs, exponents = [], []

for i in range(10):
    G_BA = nx.barabasi_albert_graph(34, 2)
    ccs.append(nx.average_clustering(G_BA))
    BA_degree = [node_degree_pair[1] for node_degree_pair in G_BA.degree]
    exponents.append(powerLaw_exponent(BA_degree))

print(np.mean(ccs))
print(np.mean(exponents))

ccs.clear()
exponents.clear()


for i in range(10):
    G_KH1 = nx.powerlaw_cluster_graph(34, 2, 0.6)
    ccs.append(nx.average_clustering(G_KH1))
    KH1_degree = [node_degree_pair[1] for node_degree_pair in G_KH1.degree]
    exponents.append(powerLaw_exponent(KH1_degree))

print(np.mean(ccs))
print(np.mean(exponents))

ccs.clear()
exponents.clear()

for i in range(10):
    G_KH1 = KH_model(34, 2, 0.6)
    ccs.append(nx.average_clustering(G_KH1))
    KH1_degree = [node_degree_pair[1] for node_degree_pair in G_KH1.degree]
    exponents.append(powerLaw_exponent(KH1_degree))

print(np.mean(ccs))
print(np.mean(exponents))
