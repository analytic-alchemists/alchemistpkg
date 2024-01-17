![analytic-alchemists-header](https://github.com/analytic-alchemists/alchemistpkg/assets/3884360/306b0521-2aa1-4cb4-b90b-58a7177fead1)
# Building Research Software Assignment
Assignment for the Building Research Software Course, January 2024

## Team Members and Accounts
(alphabetical)
- Nourin Aman: https://github.com/nourinaman
- Milan Bhakta: https://github.com/milanbhakta
- Suzanne M Chalambalacis: https://github.com/suzannemichie
- Raymond Fong: https://github.com/rfong1
- Michael Schumaker: https://github.com/mschumak
- Siti Nurfaezah Binti Zahari https://github.com/faezahari

# Project Name: Alchemist Data Analysis

## Description

Alchemist Data Analysis is a Python package designed to fetch, analyze, and visualize data from the New York Times API, focusing on the occurrence of specific keywords (e.g., "Pokemon") in news articles. It loads configuration settings from YAML files. These settings include the API key for the New York Times and plot features. The package is capable of processing API responses, performing computations on the article dates retrieved, and generating plots of article counts with respect to time.

## Installation

To install the Alchemist Data Analysis package directly from GitHub, use the following command:
```bash
pip install git+https://github.com/analytic-alchemists/alchemistpkg.git
```
This command will fetch and install the latest version of the Alchemist Data Analysis package from the GitHub repository. Ensure you have Git installed on your system to use this method.

## Post-Installation Steps

### Download Configuration Files

Download the configs folder, which includes system_config.yml, user_config.yml, and analysis_config.yml, to your working directory. 
The fastest way to accomplish this is with git:
```bash
git clone https://github.com/analytic-alchemists/alchemistpkg.git
```

Copy the alchemistpkg/configs folder to your working directory:
```bash
cp -R ./alchemistpkg/configs .
```

### Configuration

You may make a custom config file to be read by the Alchemist package, or use the configs/analysis_config.yml file. Ensure your configuration file is accessible from your working directory.

## Usage
To use the Alchemist Data Analysis package, follow these steps:

1. Initialize the Analysis Class
```python
    from alchemistpkg import Analysis
    analysis = Analysis.Analysis("configs/analysis_config.yml")   
```

2. Load Data
This fetches data from the New York Times API. The query searches for articles on the front page
of the New York Times that contain a specific word. In this case, "Pokemon".
```python
analysis.load_data()
```
The function stores the publication dates of the articles for the following steps.

3. Perform Analysis
This analyzes the number of articles as a function of year. It calculates the mean value over
the full time period, and performs linear regression.
The function returns the mean, slope, and intercept values.
```python
mean_val, slope, intercept = analysis.compute_analysis()
```

4. Generate and View Plot
Create a plot displaying the number of articles as a function of year.
If a file name is specified, the image will be saved to that location. If no file name
is given, the save location will be retrieved from the configuration file.
```python
analysis.plot_data("filename.jpg")
```
or
```python
analysis.plot_data()
```
