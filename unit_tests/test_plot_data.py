#This test plot data
import sys
import os

# Add the directory containing Analysis.py to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'alchemistpkg')))

import pytest
from Analysis import Analysis
import matplotlib.pyplot as plt

def test_plot_data():
    analysis = Analysis()
    analysis.load_data()
    fig = analysis.plot_data()
    assert isinstance(fig, plt.Figure)
