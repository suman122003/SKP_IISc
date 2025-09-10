import numpy as np
import matplotlib.pyplot as plt
from q11 import Ising_1D

N = 12      # INPUT
ferro_spins = np.zeros(N, dtype=int)
for i in range(N):
    if i % 2 == 0:
        ferro_spins[i] = 1
    else:
        ferro_spins[i] = -1

# Ising_1D(N, T=1.0, BC='periodic', config=ferro_spins, plot_=True)
Ising_1D(N, T=1.0, BC='open', config=ferro_spins, plot_=True)

