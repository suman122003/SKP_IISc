import numpy as np
import matplotlib.pyplot as plt

# parameter
C = 1.0

T1 = np.linspace(0.01, 5, 200)

mu0 = lambda T: T * np.log(3/T**(3/2))
mu1 = lambda T: T * np.log(1/T**(3/2))

plt.figure(figsize=(7,5))
plt.plot(T1, mu0(T1), label="Spin-0")
plt.plot(T1, mu1(T1), label="Spin-1", linestyle="--")

plt.axhline(0, color="gray", linewidth=1)
plt.axvline(0, color="gray", linewidth=1)
plt.xlabel(r"$T$")
plt.ylabel(r"$\mu(T)$")
plt.title("Chemical Potential vs Temperature")
plt.legend()
plt.grid()
plt.savefig('fig5b.png', dpi=100)
plt.show()
