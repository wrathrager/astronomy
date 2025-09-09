# Main script to execute pipeline
"""Main runner for simple pipeline demos.
Usage: python run.py [--stage preprocess|train|simulate|all]
"""
import argparse
from src import preprocessing, mirapy_models, relativity, visualization




def main(stage):
    if stage in ("preprocess", "all"):
        print("[1/4] Preprocessing data...")
        preprocessing.demo_preprocess()
    if stage in ("train", "all"):
        print("[2/4] Training MiraPy model (stub)...")
        mirapy_models.demo_train()
    if stage in ("simulate", "all"):
        print("[3/4] Running EinsteinPy simulations (stub)...")
        relativity.demo_simulation()
    if stage in ("visualize", "all"):
        print("[4/4] Generating visualizations...")
        visualization.demo_plot()




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--stage', default='all', help='Stage to run')
    args = parser.parse_args()
    main(args.stage)