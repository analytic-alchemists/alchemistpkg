# Description of Manual Testing Procedures for Analysis Package

## Overview
This document provides details on the unit tests implemented for the Analysis package. The Analysis package is designed to load, compute, and plot data, and these tests ensure that each component functions as expected.

## Test Files
The unit tests are divided into the following files:

- `test_load_data.py`: 
  Tests for the `load_data()` function. It tests if the data loading functionality works correctly.
- `test_compute_analysis.py`: 
  Tests for the `compute_analysis()` function. It tests the data analysis computations.
- `test_plot_data.py`: 
  Tests for the `plot_data()` function. It ensures that the plot data function creates a plot. 
- `test_analysis_config.py`: 
  Tests for the configuration handling in `analysis_config.py`. It checks if configurations are loaded correctly. 

## Running the Tests
To run the tests, navigate to the project directory and execute the following command:

```bash
python -m unittest discover -s unit_tests

or 

```bash
python -m unittest discover -s unit_tests -v


Additional Notes

Make sure all dependencies are installed before running the tests.
Some tests may require internet access if they interact with external APIs.