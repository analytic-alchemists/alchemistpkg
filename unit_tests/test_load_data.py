#This test will check if "load_data" methods works as expected 
import sys
import os

# Add the directory containing Analysis.py to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'alchemistpkg')))


import unittest
from Analysis import Analysis

class TestLoadData(unittest.TestCase):

    def test_load_data(self):
        analysis = Analysis()  # Add parameters if necessary
        analysis.load_data()
        # Here you can check if data is loaded properly
        # For example, check if `analysis.articles_by_date` is not empty
        self.assertTrue(analysis.articles_by_date)

if __name__ == '__main__':
    unittest.main()
