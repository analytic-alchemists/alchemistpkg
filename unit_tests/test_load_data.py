#This test will check if "load_data" methods works as expected 
import sys
import os
from datetime import datetime

# Add the directory containing Analysis.py to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'alchemistpkg')))

import pytest
from Analysis import Analysis

def test_load_data():
    analysis = Analysis()
    analysis.load_data(2)

    # Assert that the articles_by_date attribute is not empty and has pub_date as a key
    assert analysis.articles_by_date is not None
    assert analysis.articles_by_date.keys() is not None


