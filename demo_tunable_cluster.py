import networkx as nx

from KH_model import KH_model
from powerLaw_exponent import powerLaw_exponent

G = nx.barabasi_albert_graph(1000, 3)
print(nx.average_clustering(G))
G_degree = [node_degree_pair[1] for node_degree_pair in G.degree]
print(powerLaw_exponent(G_degree))

for Pt in [0, 0.2, 0.4, 0.6, 0.8, 1]:
    G1 = nx.powerlaw_cluster_graph(1000, 3, Pt)
    G2 = KH_model(1000, 3, Pt)

    print(nx.average_clustering(G1))
    print(nx.average_clustering(G2))

    G1_degree = [node_degree_pair[1] for node_degree_pair in G1.degree]
    G2_degree = [node_degree_pair[1] for node_degree_pair in G2.degree]
    print(powerLaw_exponent(G1_degree))
    print(powerLaw_exponent(G2_degree))