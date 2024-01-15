![analytic-alchemists-header](https://github.com/analytic-alchemists/alchemistpkg/assets/3884360/306b0521-2aa1-4cb4-b90b-58a7177fead1)
# Building Research Software Assignment
Assignment for the Building Research Software Course, January 2024

## Team Members and Accounts

(alphabetical)
- Nourin Aman: https://github.com/nourinaman
- Milan Bhakta: https://github.com/milanbhakta
- Raymond Fong: https://github.com/rfong1
- Suzanne Michie: https://github.com/suzannemichie
- Siti Nurfaezah Binti Zahari https://github.com/faezahari
- Michael Schumaker: https://github.com/mschumak

# Project Name: Alchemist Data Analysis

## Description

Alchemist Data Analysis is a Python package designed to fetch, analyze, and visualize data from the New York Times API, focusing on the occurrence of specific keywords (e.g., "Pokemon") in news articles. It loads various configuration settings and uses them to control aspects of data retrieval and plot generation. The package is capable of processing API responses, performing basic analytical computations, and generating visual plots to represent trends over time.

## Installation

To install the Alchemist Data Analysis package directly from GitHub, use the following command:

```bash
pip install git+https://github.com/analytic-alchemists/alchemistpkg.git
```
This command will fetch and install the latest version of the Alchemist Data Analysis package from the GitHub repository. Ensure you have Git installed on your system to use this method.

## Post-Installation Steps

1) Download Configuration Files: Download the configs folder, which includes system_config.yml, user_config.yml, analysis_config.yml, to your working directory. These configuration files are essential for the package to function correctly.
2) Configuration: Ensure the configuration files are set up according to your requirements and are accessible to your Python script.

## Usage
To use the Alchemist Data Analysis package, follow these steps:

1) Initialize the Analysis Class:
```python
    from alchemistpkg import Analysis
    analysis = Analysis()   
```
2) Load Data
This fetches data from the New York Times API based on the configured parameters.
```python
analysis.load_data()
```
3) Perform Analysis
Analyze the frequency of articles mentioning "Pokemon" over time. This could involve calculating the number of articles per year and identifying trends.

4) Generate and View Plot
Create a plot based on the analysis. You can specify a filename to save the plot.
```python
analysis.plot_data("filename.jpg")
```

