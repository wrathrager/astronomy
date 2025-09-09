# Plotting functions (matplotlib, plotly)
"""Plotting helpers for Matplotlib / Plotly (demo stubs).
"""
import matplotlib.pyplot as plt
import os




def demo_plot():
    os.makedirs('results/figures', exist_ok=True)
    print('Plot demo: creating a sample figure...')
    plt.figure(figsize=(5,3))
    plt.plot([0,1,2,3,4],[0,1,0,1,0])
    plt.title('Demo plot')
    plt.savefig('results/figures/demo_plot.png')
    print('Saved results/figures/demo_plot.png')




def plot_lensed_image(image, output_path='results/figures/lensed.png'):
    """Simple imshow wrapper to save images."""
    plt.figure(figsize=(4,4))
    plt.imshow(image, origin='lower')
    plt.colorbar()
    plt.savefig(output_path)
    plt.close()
    print('Saved', output_path)