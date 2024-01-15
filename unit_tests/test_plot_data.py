#This test plot data
import sys
import os

# Add the directory containing Analysis.py to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'alchemistpkg')))

import pytest
from Analysis import Analysis
import matplotlib.pyplot as plt

def test_plot_data():
    # Create an instance of the Analysis class
    analysis = Analysis()

    # Adjust fake data to match the expected structure
    # Each article should be a dictionary with a 'pub_date' key
    fake_articles_by_date = {
    '2018-01-01': [{'pub_date': '2018-01-01T00:00:00+0000'}, {'pub_date': '2018-01-01T00:00:00+0000'}],
    '2018-06-15': [{'pub_date': '2018-06-15T00:00:00+0000'}],
    '2019-02-20': [{'pub_date': '2019-02-20T00:00:00+0000'}, {'pub_date': '2019-02-20T00:00:00+0000'}],
    '2019-11-25': [{'pub_date': '2019-11-25T00:00:00+0000'}],
    '2020-03-30': [{'pub_date': '2020-03-30T00:00:00+0000'}, {'pub_date': '2020-03-30T00:00:00+0000'}],
    '2020-12-10': [{'pub_date': '2020-12-10T00:00:00+0000'}],
    '2021-01-01': [{'pub_date': '2021-01-01T00:00:00+0000'}, {'pub_date': '2021-01-01T00:00:00+0000'}, {'pub_date': '2021-01-01T00:00:'}],
    '2021-01-01': [{'pub_date': '2021-01-01T00:00:00+0000'}, {'pub_date': '2021-01-01T00:00:00+0000'}, {'pub_date': '2021-01-01T00:00:00+0000'}],
    '2021-01-02': [{'pub_date': '2021-01-02T00:00:00+0000'}],
    '2021-01-03': [{'pub_date': '2021-01-03T00:00:00+0000'}, {'pub_date': '2021-01-03T00:00:00+0000'}]
    }

    # Manually set the articles_by_date attribute
    analysis.articles_by_date = fake_articles_by_date

    # Call the plot_data method
    fig = analysis.plot_data()

    # Assert that the result is a matplotlib Figure instance
    assert isinstance(fig, plt.Figure), "plot_data should return a matplotlib figure."