#This test will check if the configurations are loaded correctly
import sys
import os

# Add the directory containing Analysis.py to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'alchemistpkg')))

import unittest
from Analysis import Analysis

class TestAnalysisConfig(unittest.TestCase):

    def test_config_loading(self):
        analysis = Analysis()
        # Here you can check if configuration is loaded correctly
        # For example, check if some config parameters are set
        self.assertIn('api_token', analysis.config)

if __name__ == '__main__':
    unittest.main()