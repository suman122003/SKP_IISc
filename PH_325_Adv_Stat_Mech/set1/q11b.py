import numpy as np
import matplotlib.pyplot as plt
from q11 import Ising_1D

N = 10

# Ising_1D(N, T=1.0, BC='periodic', config=None, plot_=True)
Ising_1D(N, T=1.0, BC='open', config=None, plot_=True)
