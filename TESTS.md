# Description of Manual Testing Procedures for Analysis Package

## Overview
This document outlines the procedures for manually testing the Analysis package. The package is designed to load, compute, and plot data related to articles from the New York Times API. The following instructions ensure that each component of the package functions as intended when installed and run in a Colab environment.

## Running the Analysis Package in Colab
To use the Analysis package in a Colab environment, follow these steps:

### 1) Installation
First, install the package using pip:

```python
!pip install git+https://github.com/user/alchemistpkg
```

### 2) Get Configuration Files
Download the configs folder, which includes system_config.yml, user_config.yml, and analysis_config.yml. 
The fastest way to accomplish this is with git:
```python
!git clone https://github.com/analytic-alchemists/alchemistpkg.git
```

Copy the alchemistpkg/configs folder to your working space:
```python
!cp ./alchemistpkg/configs .
```

### 3) Configuration
The 'Analysis' class uses configuration files in the configs folder of the repository. Make sure that these files are present in the configs folder in the working directory. The `Analysis` class will automatically load `system_config.yml` and `user_config.yml`.
The analysis configuration file can be customized, but it is easier to begin from a pre-existing file.
`analysis_config.yml` is the primary configuration file, and its path or the path of a custom file should be provided when creating an instance of the `Analysis` class.

### 4) Importing and Using the Package
After installation, import and use the 'Analysis' class as follows: 

```python
from alchemistpkg import Analysis
# Create an instance of the Analysis class
# Make sure that the configuration file path is correct and accessible
analysis_obj = Analysis.Analysis('configs/analysis_config.yml')
```

### 5) Load data from the New York Times API
```python
analysis_obj.load_data()
```
### 6) Compute analysis
```python
analysis_output = analysis_obj.compute_analysis()
print(analysis_output)
```
### 7) Generate and display a plot
```python
analysis_figure = analysis_obj.plot_data("filename.jpg")
```
If no file name is specified, the image will be saved to the location in the configuration file.
```python
analysis.plot_data()
```
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
- `test_load_config_step.py`: 
  Tests for the configuration handling in `analysis_config.py`. It checks if configurations can load correctly. 

## Running the Test for Single Test Data
Perform the following steps to manually test each functionality of the Analysis package:

### 1)Test Data Loading
```python
pytest test_load_data.py
```

###Note: This command should load the data from the New York Times API based on the configuration provided. Verify that data is loaded correctly without errors.

### 2)Test Compute Analysis
```python
pytest test_compute_analysis.py
```

###Note: This command should provide the analytical results.

### 3)Test Configuration File Handling
```python
pytest test_load_config_step.py
```

###Note: This command tests if configurations are loaded correctly. Verify that the required configuration parameters are present in the analysis.config object.

### 4) Test Plot Data
```python
pytest test_plot.py
```

####Note: This command should generate a plot based on the loaded data. Verify that the plot is displayed or saved correctly, as implemented in your `plot_data()` method.

## Running All Tests in the Directory
To run the all tests in the directory, navigate to the project directory and execute the following command:

```bash
pytest
```

or 

```bash
pytest -v 
# To see a more detailed output, including print statements from tests or the full traceback for failures or errors)
```

## Additional Notes

- Before running the tests, ensure that all dependencies required by the Analysis package are installed in your environment. These should be handled by the package setup.
- The `load_data()` function requires interaction with an external API. The New York Times API has a request rate limit. To accommodate this, the load_data function has a time delay between requests to obtain the full dataset.
- Review `analysis_config.yml` or your custom file to ensure that it contains the correct settings and API keys needed for the package to function properly.

By following these procedures, you can manually test the Analysis package's functionality in a Colab environment or any other Python environment where the package is installed.

---
