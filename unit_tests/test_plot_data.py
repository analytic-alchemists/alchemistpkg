#This test plot data
import sys
import os

# Add the directory containing Analysis.py to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'alchemistpkg')))

import unittest
from Analysis import Analysis
import matplotlib.pyplot as plt

class TestPlotData(unittest.TestCase):

    def test_plot_data(self):
        analysis = Analysis()
        analysis.load_data()
        fig = analysis.plot_data()
        self.assertIsInstance(fig, plt.Figure)

if __name__ == '__main__':
    unittest.main()