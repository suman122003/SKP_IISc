import numpy as np
import matplotlib.pyplot as plt

B = 1
T1 = np.linspace(0.01, 5, 200)
T2 = np.linspace(0.5, 5, 200)
T3 = np.linspace(0.5, 5, 200)
T4 = np.linspace(1., 5, 200)

def fn(n, T):
    return 1 + 2*np.cosh(n*B/T)


mu0 = lambda T: T * np.log(3/T**(3/2))
mu1 = lambda T: T * np.log(1/T**(3/2))
mu1b = lambda T: T * np.log(1/(T**(3/2)*fn(1, T)))

K0 = lambda T: (1/T) * (1 - (5/8 - 1/3**(3/2))*9/T**3)
K1 = lambda T: (10/T)*(1 - (5/8 - 1/3**(3/2))/T**3)
K1b = lambda T: (1/T) * (1 - ((5/8)*(fn(2, T))**2 - 
                        (1/3**(3/2))*(fn(3, T))**2)/(T**3 * fn(1, T)))

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(T1, mu0(T1), label="Spin-0 with B")
plt.plot(T1, mu1b(T1), label="Spin-1 with B")
plt.plot(T1, mu0(T1), label="Spin-0", linestyle="--")
plt.plot(T1, mu1(T1), label="Spin-1", linestyle="--")
plt.axhline(0, color="gray", linewidth=1)
plt.axvline(0, color="gray", linewidth=1)
plt.xlabel(r"$T$")
plt.ylabel(r"$\mu(T)$")
plt.title("Chemical Potential vs Temperature")
plt.legend()
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(T2, K0(T2), label="Spin-0 with B")
plt.plot(T4, K1b(T4), label="Spin-1 with B")
plt.plot(T2, K0(T2), label="Spin-0", linestyle="--")
plt.plot(T3, K1(T3), label="Spin-1", linestyle="--")
plt.ylim(-10, 10)
plt.axhline(0, color="gray", linewidth=1)
plt.axvline(0, color="gray", linewidth=1)
plt.xlabel(r"$T$")
plt.ylabel(r"$\kappa(T)$")
plt.title("Compressibility vs Temperature")
plt.legend()
plt.grid()

plt.tight_layout()
plt.savefig('fig5d.png', dpi=100)
plt.show()
