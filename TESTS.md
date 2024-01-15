# Description of Manual Testing Procedures for Analysis Package

## Overview
This document outlines the procedures for manually testing the Analysis package. The package is designed to load, compute, and plot data related to articles from the New York Times API. The following instructions ensure that each component of the package functions as intended when installed and run in a Colab environment.

## Running the Analysis Package in Colab
To use the Analysis package in a Colab environment, follow these steps:

### 1) Installation
First, install the package using pip:

```python
!pip install git+https://github.com/user/alchemistpkg

### 2)Importing and Using the Package
After installation, import and use the 'Analysis' class as follows: 

```python
from alchemistpkg import Analysis
# Create an instance of the Analysis class
# Make sure that the configuration file path is correct and accessible
analysis_obj = Analysis('path/to/config.yml')

### 3)Configuration Files and Uploading Files to Colab
The 'Analysis' class uses three configuration files:
1. `analysis_config.yml`: This is the primary configuration file, and its path should be provided when creating an instance of the `Analysis` class.
2. `system_config.yml`: Contains system-wide configuration settings. The `Analysis` class expects to find this file in a specific directory (e.g., the same directory as `analysis_config.yml` or a 'configs' directory).
3. `user_config.yml`: Contains user-specific settings. Similar to `system_config.yml`, the `Analysis` class will look for this file in a predefined location.

Make sure that these files are present in the expected locations and are correctly configured. The `Analysis` class will automatically load `system_config.yml` and `user_config.yml` based on the location of `analysis_config.yml`.

When using the package in Colab, upload `analysis_config.yml`, `system_config.yml`, and `user_config.yml` to the Colab environment. Ensure that the `Analysis` class is instantiated with the correct path to `analysis_config.yml`. The class will automatically load the other configuration files if they are in the same directory.

### 4)Load data from the New York Times API
analysis_obj.load_data()

### 5)Compute analysis
analysis_output = analysis_obj.compute_analysis()
print(analysis_output)

### 6)Generate and display a plot
analysis_figure = analysis_obj.plot_data()

## Summary
In the above code: 
- The Analysis class is imported from the alchemistpkg package.
- The instance analysis_obj is created with a path to a configuration file. Make sure this file is available in your Colab environment.
- The load_data method fetches data from the API.
- The compute_analysis method performs the analysis and its output is printed.
- The plot_data method generates and displays a plot. Ensure that your Colab environment supports plot display.

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

## Running the Test for Single Test Data
Perform the following steps to manually test each functionality of the Analysis package:

### 1)Test Data Loading
```python
pytest test_load_data.py

###Note: This command should load the data from the New York Times API based on the configuration provided. Verify that data is loaded correctly without errors.

### 2)Test Compute Analysis
```python
pytest test_compute_analysis.py

###Note: This command should provide the analytical results.

### 3)Test Analysis Configuration
'''python
pytest test_analysis_config.py

###Note: This command tests if configurations are loaded correctly. Verify that the required configuration parameters are present in the analysis.config object.

### 4) Test Plot Data
pytest test_plot.py

####Note: This command should generate a plot based on the loaded data. Verify that the plot is displayed or saved correctly, as implemented in your `plot_data()` method.

## Running All Tests in the Directory
To run the all tests in the directory, navigate to the project directory and execute the following command:

```bash
pytest 

or 

```bash
pytest -v 

(To see a more detailed output, including print statements from tests or the full traceback for failures or errors)

## Additional Notes

- Before running the tests, ensure that all dependencies required by the Analysis package are installed in your environment.
- Some methods, such as `load_data()`, may require internet access as they interact with external APIs. Make sure that your Colab environment has network access.
- Review the `config.yml` file to ensure that it contains the correct settings and API keys needed for the package to function properly.
- The Analysis package's methods should be tested in an isolated environment to ensure that they do not depend on external variables or states.

By following these procedures, you can manually test the Analysis package's functionality in a Colab environment or any other Python environment where the package is installed.

---
