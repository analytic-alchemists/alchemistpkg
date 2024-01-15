#This test will depend on how we implement "compute_analysis". Assuming it returns some kind of results
import sys
import os

# Add the directory containing Analysis.py to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'alchemistpkg')))

import pytest
from Analysis import Analysis

def test_compute_analysis():
    analysis = Analysis()
    analysis.load_data()
    result = analysis.compute_analysis()
    assert result is not None