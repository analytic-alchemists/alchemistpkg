#This test will check if "load_data" methods works as expected 
import sys
import os

# Add the directory containing Analysis.py to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'alchemistpkg')))

import pytest
from Analysis import Analysis

def test_load_data():
    analysis = Analysis()
    analysis.load_data()
    assert analysis.articles_by_date
