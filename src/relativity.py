"""EinsteinPy demo stubs for geodesics and lensing.
Replace stubs with full EinsteinPy geodesic calls and lensing ray-tracing code.
"""
import numpy as np




def demo_simulation():
    print('Running demo EinsteinPy simulation (stub).')
    # A tiny fake trajectory: circular orbit points
    theta = np.linspace(0, 2 * np.pi, 200)
    x = 10 * np.cos(theta)
    y = 10 * np.sin(theta)
    import matplotlib.pyplot as plt
    plt.figure(figsize=(4,4))
    plt.plot(x, y)
    plt.scatter([0],[0], c='k')
    plt.title('Demo circular orbit (replace with EinsteinPy geodesic)')
    plt.savefig('results/figures/demo_orbit.png')
    print('Saved results/figures/demo_orbit.png')




# Example placeholder for a function you will replace with EinsteinPy calls
def compute_geodesic_schwarzschild(mass, init_coords, init_momenta, steps=100):
    """Compute a fake geodesic. Replace with einsteinpy.geodesic usage."""
    # return Nx4 array of coordinates (t, x, y, z)
    t = np.linspace(0, 100, steps)
    coords = np.vstack([t, np.sin(t), np.cos(t), np.zeros_like(t)]).T
    return coords