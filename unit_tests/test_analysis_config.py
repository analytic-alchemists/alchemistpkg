#This test will check if the configurations are loaded correctly
import sys
import os

# Add the directory containing Analysis.py to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'alchemistpkg')))

import pytest
from Analysis import Analysis

def test_config_loading():
    analysis = Analysis()
    assert 'api_token' in analysis.config