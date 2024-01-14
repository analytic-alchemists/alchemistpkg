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

# Installation

To install Alchemist Data Analysis, follow these steps:

1) Clone the Repository:

```bash
git clone https://github.com/your-username/alchemist-data-analysis.git

Note:Replace 'your-username' with the appropriate Github username or organization.

2) Navigate to the Project Directory:

```bash
cd alchemist-data-analysis

3) Install Dependencies:

Ensure you have Python installed on your system. Then, install the required packages:

```bash
pip install -r requirements.txt
Note: You might want to create a virtual environment before installing the dependencies.

4) Configuration:
Before running the analysis, ensure the configuration files ('system_config.yml' ,'user_config.yml','analysis_config.yml') are set up according to your requirements.

# Usage
To use the Alchemist Data Analysis package, follow these steps:

1) Initialize the Analysis Class:

```python
from alchemistpkg import Analysis
analysis = Analysis()

2) Load Data:
This fecthes data from the New York Times API based on the configured parameters.

```python
analysis.load_data()

3) Perform Analysis:
Trend Analysis - Analyze the frequency of articles mentioning "Pokemon" over time. This could involve calculating the number of articles per year and identifying trends, such as increases or decreases in mentions.

4) Generate and View Plot:
This will create a plot based on the analysis and save it to a specified location.
```python
analysis.plot_data()