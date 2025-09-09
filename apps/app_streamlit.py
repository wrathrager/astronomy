"""Streamlit app: now with user input for any Hubble target."""
import streamlit as st
from src import mirapy_models, preprocessing, relativity, visualization, data_fetchers
import numpy as np
from PIL import Image

st.set_page_config(page_title='Astro Sim Demo', layout='wide')
st.title('Astro-Simulations — Demo Dashboard')
st.sidebar.header('Load Data')
uploaded = st.sidebar.file_uploader('Upload a FITS or PNG image', type=['fits','png','jpg','jpeg'])


if uploaded is not None:
    if uploaded.name.lower().endswith('.fits'):
        from astropy.io import fits
        hdul = fits.open(uploaded)
        arr = hdul[0].data
        arr = np.nan_to_num(arr)
        arr = arr / (arr.max() or 1)
        st.image(arr, caption='Uploaded FITS (normalized)', use_column_width=True)
    else:
        img = Image.open(uploaded).convert('L')
        st.image(img, caption='Uploaded image', use_column_width=True)


st.sidebar.header('Run demo')
if st.sidebar.button('Run full demo pipeline'):
    st.info('Running demo pipeline...')
    preprocessing.demo_preprocess()
    mirapy_models.demo_train()
    relativity.demo_simulation()
    visualization.demo_plot()
    st.success('Demo completed. Check results/figures for outputs.')

st.sidebar.header("Real Telescope Data")
target = st.sidebar.text_input("Target name (e.g., M31, M87, Orion Nebula)", value="M31")


if st.sidebar.button("Fetch Hubble & Display"):
    st.info(f"Querying Hubble for {target}... this may take time on first run.")
    path = data_fetchers.fetch_hubble_images(target, max_records=1)
    if path:
        from astropy.io import fits
        with fits.open(path) as hdul:
            arr = np.nan_to_num(hdul[0].data.astype(float))
            arr = arr / (arr.max() or 1)
        st.image(arr, caption=f'Hubble FITS for {target}', use_column_width=True)
        st.success(f"Hubble image for {target} fetched and displayed.")
    else:
        st.error(f"No Hubble data found for {target}.")


if st.sidebar.button("Fetch Gaia sample (around M31)"):
    gaia = data_fetchers.fetch_gaia_sources()
    st.write(gaia)


st.markdown('---')
st.header('Demo Outputs')
col1, col2 = st.columns(2)
with col1:
    try:
        st.image('results/figures/demo_input.png', caption='Demo input')
    except Exception:
        st.write('No demo input image yet')
with col2:
    try:
        st.image('results/figures/demo_orbit.png', caption='Demo orbit')
    except Exception:
        st.write('No demo orbit image yet')


st.markdown('---')
st.write('This Streamlit app now supports fetching & displaying Hubble FITS data for any target specified by the user, plus Gaia samples.')