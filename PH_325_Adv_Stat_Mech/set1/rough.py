import numpy as np
import matplotlib.pyplot as plt

def draw_periodic_ising_circle(spins, title="Periodic Ising Chain"):
    """
    Draws a periodic Ising chain as a circle.

    Args:
        spins (np.array or list): A 1D array or list of spin states (1 for up, -1 for down).
        title (str): The title for the plot.
    """
    N = len(spins)
    radius = 1 # Radius of the circle

    # Calculate angles for each spin position
    # We want to go from 0 to 2*pi, distributing N spins evenly
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False)

    # Calculate (x, y) coordinates for each spin
    x_coords = radius * np.cos(angles)
    y_coords = radius * np.sin(angles)

    plt.figure(figsize=(7, 7))
    ax = plt.gca()

    # Plot each spin
    for i in range(N):
        if spins[i] == 1:
            # Spin Up: Red circle
            ax.plot(x_coords[i], y_coords[i], 'ro', markersize=15, zorder=2)
        else:
            # Spin Down: Blue circle
            ax.plot(x_coords[i], y_coords[i], 'bo', markersize=15, zorder=2)

        # Optionally, label the spins
        # ax.text(x_coords[i] * 1.1, y_coords[i] * 1.1, str(i), fontsize=8, ha='center', va='center')

    # Draw a faint circle to outline the chain
    circle_outline = plt.Circle((0, 0), radius, color='gray', fill=False, linestyle='--', linewidth=1, alpha=0.5)
    ax.add_artist(circle_outline)

    # Add lines connecting adjacent spins
    # For periodic boundary, connect last to first
    for i in range(N):
        next_i = (i + 1) % N # Handles the periodic wrap-around
        ax.plot([x_coords[i], x_coords[next_i]],
                [y_coords[i], y_coords[next_i]],
                color='black', linestyle='-', linewidth=0.8, alpha=0.6, zorder=1)

    ax.set_aspect('equal', adjustable='box') # Ensures the circle isn't elliptical
    plt.title(title)
    plt.axis('off') # Hide axes for a cleaner look
    plt.show()

# --- Example Usage ---
# A sample periodic Ising chain
N_chain = 12
sample_spins = np.array([1, 1, -1, -1, 1, -1, 1, 1, -1, -1, 1, -1])
draw_periodic_ising_circle(sample_spins, "My Circular Ising Chain (N=12)")

# Another example with random spins
random_spins = np.random.choice([1, -1], size=20)
draw_periodic_ising_circle(random_spins, "Random Circular Ising Chain (N=20)")