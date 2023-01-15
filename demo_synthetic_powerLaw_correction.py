import numpy as np

from synthetic_powerLaw import synthetic_powerLaw

Ns = [100, 1000, 10000]

for N in Ns:
    corrections = []
    for i in range(10):
        G, correction = synthetic_powerLaw(N)
        #print(G.number_of_edges())
        #print(correction)
        corrections.append(correction)

    print(np.mean(corrections))