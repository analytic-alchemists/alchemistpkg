# Building Research Software Assignment
# January 2024

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import yaml
import requests
import time
from typing import Any, Optional
from datetime import datetime
import os
import logging

class Analysis:
    def __init__(self, analysis_config:Optional[str] = None):
        """ Analysis class constructor, loads configuration files.

        Load system-wide configuration from 'configs/system_config.yml',
        user configuration from 'configs/user_config.yml',
        and the given analysis_config file location (optional, default value None)

        Parameters
        ----------
        analysis_config : Optional[str] = None
            Path to the analysis/job-specific configuration file, default value is None

        Returns
        -------
        None

        Notes
        -----
        Defines the value of the class member variable
        self.config : dict
            Analysis object containing consolidated parameters from the configuration files
        """
        # Set up logging configuration
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        # The base config path is the installed location of the package
        base_config_path = os.path.dirname(__file__)

        # list of config layer files - order by general to specific
        CONFIG_PATHS = [ 'system_config.yml',
                        'user_config.yml',
                        'analysis_config.yml']

        # Test if user added optional analysis_config to list of paths to load
        paths_to_load = [os.path.join(base_config_path, path) for path in CONFIG_PATHS]
        if analysis_config is not None:
            try:
                if os.path.exists(analysis_config):
                    paths_to_load.append(analysis_config)
                    self.logger.info(f'User provided file path is valid.')
                else:
                    raise FileNotFoundError(f'User file path does not exist.')
            except ValueError as e:
                raise TypeError(f'{analysis_config} is not a string.')

        # empty dictionary to add the parameters from the config files
        config = {}

        for path in paths_to_load:
            self.logger.info('Loading ' + path)
            with open(path, 'r') as file:
                configure = yaml.safe_load(file)
            # method that updates/overwrites the 'configure' file
            # as loop iterates through config files
            # config dictionary has parameters read from the config files
            config.update(configure)
            #print(config)

        # save instance of config for use within the Analysis Class using 'self'
        self.config = config
        self.articles_by_date = {}

    # end __init__

    def load_data(self):
        """ Retrieve data from the New York Times API.

        This function makes an HTTPS request to the New York Times API
        and retrieves data for all Articles where Pokemon is on 1st Page 
        and or on the 1st Column of Article. The retrieved records are
        stored in a member variable of the Analysis object.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.logger.info("Retrieving data from the New York Times API.")

        # set api_key
        api_key = self.config['api_token']

        max_pages = 1  # Maximum 100 pages for 1000 results (as per API limits)
        api_data = []  # List to store fetched articles

        # Fetch the first page to get total number of records (hits)
        first_page_data = self.get_articles(api_key=api_key, page=0)

        if first_page_data and 'response' in first_page_data:
            total_hits = first_page_data['response']['meta']['hits']

            # Calculate the number of pages required to fetch all records
            num_pages_required = min((total_hits // 10) + 1, max_pages)

            # Iterate through the calculated number of pages
            for page_number in range(1, num_pages_required + 1):
                articles_page = self.get_articles(api_key=api_key, page=page_number)
                if articles_page and 'response' in articles_page:
                    docs = articles_page['response']['docs']
                    api_data.extend(docs)

                # Introduce a delay of 12 seconds between requests to avoid rate limiting.
                # NY TIMES HAS RATE LIMIT OF FIVE PER MINUTE
                time.sleep(12)
        else:
            self.logger.error("Error fetching data from the API.")


        # Call the function with the fetched articles data to get dates to be used for plotting
        organized_articles = self.organize_articles_by_date(api_data)

        # Assign the data to articles_by_date to be accessible in the class
        self.articles_by_date = organized_articles


    # end load_data

    def compute_analysis(self) -> tuple[float, float, float]:
        """ Analyze previously-loaded data.

        This function calculates the mean and linear regression of the loaded data.

        Parameters
        --------
        None

        Returns
        -------
        analysis_output : tuple[float, float, float]
            A tuple containing the mean, linear regression slope, and linear reg. intercept.
        """
        # Create a dictionary to store the count of records for each year
        records_by_year = {}
        # Iterate through articles and count records for each year
        for article_list in self.articles_by_date.values():
            pub_date = article_list[0].get('pub_date', '')
            if pub_date:
                year = datetime.strptime(pub_date, '%Y-%m-%dT%H:%M:%S%z').strftime('%Y')
                if year in records_by_year:
                    records_by_year[year] += 1
                else:
                    records_by_year[year] = 1
        # Extract years and corresponding record counts
        years = list(records_by_year.keys())
        record_counts = list(records_by_year.values())
        # Calculate the mean
        mean_articles_per_year = np.mean(record_counts)
        # Linear regression
        x_values = np.arange(len(years))
        slope, intercept = np.polyfit(x_values, record_counts, 1)
        return (mean_articles_per_year, slope, intercept)
    # end compute_analysis

    def display_analysis(self):
        """ Print the mean and linear regression slope and intercept to standard output.

        This function computes and prints the mean and linear regression
        values to the screen.

        Parameters
        --------
        None

        Returns
        -------
        None
        """
        mean_value, slope, intercept = self.compute_analysis()
        print(f"Mean Number of Articles per Year: {mean_value}")
        print(f"Linear Regression Slope and Intercept: {slope}, {intercept}")
    # end display_analysis

    def plot_data(self, save_path: Optional[str] = None) -> plt.Figure:
        """ Analyze and plot a line graph of the number of articles by year.

        Generates a plot, displays it on the screen, and saves it to the path
        specified by 'save_path', or to the default path from the configuration file
        if 'save_path' is not provided.

        Parameters
        ----------
        save_path : str, optional
            Save path for the generated figure.

        Returns
        -------
        fig : matplotlib.Figure
        """

        # Create a dictionary to store the count of records for each year
        records_by_year = {}

        # Iterate through articles and count records for each year
        for article_list in self.articles_by_date.values():
            pub_date = article_list[0].get('pub_date', '')
            if pub_date:
                year = datetime.strptime(pub_date, '%Y-%m-%dT%H:%M:%S%z').strftime('%Y')
                if year in records_by_year:
                    records_by_year[year] += 1
                else:
                    records_by_year[year] = 1

        # Extract years and corresponding record counts
        years = list(records_by_year.keys())
        record_counts = list(records_by_year.values())

        # Sort years chronologically
        years.sort()

        # Plotting
        plt.figure(figsize=(12, 6))
        plt.plot(years, record_counts, marker='o', linestyle='-', color='green', label='Records')
        plt.title('Number of Articles per Year')
        plt.xlabel('Year')
        plt.ylabel('Number of Articles')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.legend()

        # Save the plot to the specified path or the default path from the configuration file
        if save_path is None:
            save_path = self.config.get('save_path', 'default_plot.png')

        plt.savefig(save_path)
        print(f"Plot saved to: {save_path}")
        
        #Debugging output
        print(years)
        print(record_counts)    


        # Display the plot to screen
        plt.show()

        return plt.gcf()
    # end plot_data

    def get_articles(self, api_key: str, page=0):
        base_url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
        params = {
            "api-key": api_key,
            "page": page,
            "q": 'Pokemon',
            'print_page': 1,
            "print_section": ' ("A", "1") OR (!_exists_:print_section)'
        }

        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            self.logger.error(f'Error fetching data from the API. Status code: {response.status_code}')
            self.logger.debug(f'Response text: {response.text}')
            return None

    def organize_articles_by_date(self, articles_data) -> dict:
        # Create a dictionary to store articles by date
        articles_date = {}

        # Iterate through articles and organize them by date
        for article in articles_data:
            pub_date = article.get('pub_date', '')

            # Check if pub_date is not empty
            if pub_date:
                # Convert pub_date to datetime for better sorting
                pub_date_datetime = datetime.strptime(pub_date, '%Y-%m-%dT%H:%M:%S%z')

                # Check if the date is already a key in the dictionary
                if pub_date_datetime in articles_date:
                    articles_date[pub_date_datetime].append(article)
                else:
                    articles_date[pub_date_datetime] = [article]

        return articles_date

# This block will only execute when the script is run directly, not when imported as a module
if __name__ == "__main__":
    # Create an instance of the Analysis class
    analysis = Analysis()

    # Call the methods to load data, perform analysis, and plot data
    analysis.load_data()         # Load data from the API
    analysis.compute_analysis()  # Perform analysis on the loaded data
    analysis.plot_data()         # Plot the data and save the figure

