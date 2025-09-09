"""Data loading & preprocessing helpers.
This file contains small demo functions to load FITS images and sample lightcurves,
and to perform basic normalization and augmentation stubs.
"""
from astropy.io import fits
import numpy as np
import os


def load_fits(path):
    """Load a FITS file and return a normalized numpy array."""
    with fits.open(path) as hdul:
        data = hdul[0].data.astype(float)
    # Handle NaNs
    data = np.nan_to_num(data)
    # Normalize
    mx = np.max(np.abs(data))
    if mx == 0:
        return data
    return data / mx




def demo_preprocess():
    """Demo stub: generate or load small example(s) and save to results/."""
    print("Demo preprocessing: creating a fake image array and saving to results/")
    arr = np.random.randn(128, 128)
    os.makedirs('results/figures', exist_ok=True)
    # save a simple image using imageio if available
    try:
        import imageio
        imageio.imwrite('results/figures/demo_input.png', (255 * (arr - arr.min()) / (arr.ptp())).astype('uint8'))
        print('Saved results/figures/demo_input.png')
    except Exception as e:
        print('Install imageio to save demo images:', e)