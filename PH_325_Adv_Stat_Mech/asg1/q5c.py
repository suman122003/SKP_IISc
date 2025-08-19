import numpy as np
import matplotlib.pyplot as plt

T1 = np.linspace(1.1, 5, 200)
T2 = np.linspace(0.6, 5, 200)

K0 = lambda T: (10/T)*(1 - (5/8 - 1/3**(3/2))*9/T**3)
K1 = lambda T: (10/T)*(1 - (5/8 - 1/3**(3/2))/T**3)

plt.figure(figsize=(7,5))
plt.plot(T1, K0(T1), label="Spin-0")
plt.plot(T2, K1(T2), label="Spin-1", linestyle="--")

plt.axhline(0, color="gray", linewidth=1)
plt.axvline(0, color="gray", linewidth=1)
plt.xlabel(r"$T$")
plt.ylabel(r"$\kappa(T)$")
plt.title("Compressibility vs Temperature")
plt.legend()
plt.grid()
plt.savefig('fig5c.png', dpi=100)
plt.show()
