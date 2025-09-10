import numpy as np
import matplotlib.pyplot as plt

def Ising_1D(N: int, T: float, BC: str, config, plot_=False):
    """
    1D Ising model with either periodic or open boundary conditions.
    Arguments:
        N (int): Number of spins in the chain.
        T (float): Temperature of the system.
        BC (str): Boundary condition, either 'periodic' or 'open'.
        config (int, np.ndarray, list, or None): Initial configuration of spins.
            - If int or None: Random configuration with given seed.
            - If np.ndarray or list: Use as the initial spin configuration.
        plot_ (bool): Whether to plot the spin configuration.
    Returns:
        spins (np.ndarray): The spin configuration.
        E_config (float): The energy of the configuration.
        """
    if type(config) == int or config is None:
        rand_seed = config
        np.random.seed(rand_seed)
        spins = np.random.choice([-1, 1], size=(N,))
    elif type(config) == np.ndarray or type(config) == list:
        spins = config
    J = 1.0     # INPUT
    bt = 1.0 / T     # Natural units
    E_config = 0
    for i in range(N):
        if i == 0:
            if BC == 'periodic':
                E_config += -J * spins[i] * (spins[i+1] + spins[-1])
            elif BC == 'open':
                E_config += -J * spins[i] * spins[i+1]
        elif i == N-1:
            if BC == 'periodic':
                E_config += -J * spins[i] * (spins[i-1] + spins[0])
            elif BC == 'open':
                E_config += -J * spins[i] * spins[i-1]
        else:
            E_config += -J * spins[i] * (spins[i-1] + spins[i+1])
    
    if plot_ == True and BC == 'periodic':
        r_cir = 1
        th_cir = np.linspace(0, 2*np.pi, N, endpoint=False)
        x_cir, y_cir = r_cir*np.cos(th_cir), r_cir*np.sin(th_cir)
        ax = plt.gca()
        for i in range(N):
            if spins[i] == 1:
                ax.plot(x_cir[i], y_cir[i], 'ro')
            if spins[i] == -1:
                ax.plot(x_cir[i], y_cir[i], 'bo')
            ax.text(x_cir[i]*1.1, y_cir[i]*1.1, str(i), ha='center', va='center')
        cir_plot = plt.Circle((0, 0), r_cir, color='gray', fill=False, linestyle='--', alpha=0.5)
        ax.add_artist(cir_plot)
        plt.title(f'1D Ising Chain with Periodic BC (N={N}, T={T}, E={E_config})\n')
        plt.axis('off')
        plt.savefig('set1q11.png')
        plt.show()
    if plot_ == True and BC == 'open':
        ax = plt.gca()
        for i in range(N):
            if spins[i] == 1:
                ax.plot(i, 0, 'ro')
            if spins[i] == -1:
                ax.plot(i, 0, 'bo')
            ax.text(i, 0.1, str(i), ha='center', va='center')
        ax.plot([-1, N], [0, 0], color='gray', linestyle='--', alpha=0.5)
        plt.title(f'1D Ising Chain with Open BC (N={N}, T={T}, E={E_config})\n')
        plt.axis('off')
        plt.savefig('set1q11.png')
        plt.show()

    return spins, E_config

if __name__ == "__main__":
    # Ising_1D(N = 12, T = 1.0, BC = 'periodic', config = 42, plot_ = True)
    # Ising_1D(N = 12, T = 1.0, BC = 'open', config = 42, plot_ = True)
    # Ising_1D(N = 13, T = 1.0, BC = 'periodic', config = None, plot_ = True)
    Ising_1D(N = 13, T = 1.0, BC = 'open', config = None, plot_ = True)

