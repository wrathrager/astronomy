"""
Data fetchers for telescope archives (Gaia, Hubble/MAST, Rubin/LSST).
"""
from astroquery.mast import Observations
from astroquery.gaia import Gaia

def fetch_hubble_images(target="M31", max_records=3):
    """
    Query MAST for Hubble Space Telescope observations of a target.
    """
    obs_table = Observations.query_criteria(
        obs_collection="HST",
        target_name=target,
        dataproduct_type="image"
    )
    obs_ids = obs_table[:max_records]["obsid"]
    print("Found HST obs IDs:", obs_ids)
    return obs_ids

def fetch_gaia_sources(ra=10.684, dec=41.269, radius=0.1):
    """
    Query Gaia DR3 around given coordinates (default: M31 center).
    """
    query = f"""
    SELECT TOP 10 *
    FROM gaiadr3.gaia_source
    WHERE CONTAINS(
        POINT('ICRS',ra,dec),
        CIRCLE('ICRS',{ra},{dec},{radius})
    )=1
    """
    job = Gaia.launch_job(query)
    results = job.get_results()
    print("Gaia query results:", results[:5])
    return results
