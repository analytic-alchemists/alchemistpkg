# Building Research Software Assignment
# January 2024

import matplotlib
import matplotlib.pyplot as plt
import yaml
import requests
import time
from typing import Any, Optional
from datetime import datetime
import os

class Analysis:
    def __init__(self, analysis_config:Optional[str] = None):
        """ Analysis class constructor, loads configuration files.

        Load system-wide configuration from 'configs/system_config.yml', 
        user configuration from 'configs/user_config.yml', 
        the specified analysis configuration file 'configs/user_config.yml',
        and the given analysis_config file location (optional, default value None)

        Parameters
        ----------
        analysis_config : Optional[str] = None
            Path to the analysis/job-specific configuration file, default value is None

        Returns
        -------
        config : dict
            Analysis object containing consolidated parameters from the configuration files
        """
        # The base config path is the installed location of the package
        base_config_path = os.path.dirname(__file__)

        # list of config layer files - order by general to specific
        CONFIG_PATHS = [ 'system_config.yml',
                        'user_config.yml',
                        'analysis_config.yml']

        # add analysis config to list of paths to load
        paths_to_load = [os.path.join(base_config_path, path) for path in CONFIG_PATHS]
        if analysis_config is not None:
            paths_to_load.append(analysis_config)

        # empty dictionary to add the parameters from the config files
        config = {}

        for path in paths_to_load:
            print('Loading ' + path)
            with open(path, 'r') as file:
                configure = yaml.safe_load(file)
            # method that updates/overwrites the 'configure' file 
            # as loop iterates through config files
            # config dictionary has parameters read from the config files
            config.update(configure)
            print(config)
        
        # save instance of config for use within the Analysis Class using 'self'
        self.config = config
        self.articles_by_date = {}

    # end __init__

    def load_data(self):
        """ Retrieve data from the New York Times API.

        This function makes an HTTPS request to the New York Times API
        and retrieves data for all Articles where Pokemon is on 1st Page and or on the 1st Column of Article. The data is
        stored in the Analysis object.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        # set api_key
        api_key = self.config['api_token']

        max_pages = 100  # Maximum 100 pages for 1000 results (as per API limits)
        api_data = []  # List to store fetched articles

        # Fetch the first page to get total number of records (hits)
        first_page_data = self.get_articles(api_key=api_key, page=0)

        if first_page_data and 'response' in first_page_data:
            total_hits = first_page_data['response']['meta']['hits']
            #print(f"Total number of records: {total_hits}")

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
            print("Error fetching data from the API.")

        # Call the function with the fetched articles data to get dates to be used for plotting
        organized_articles = self.organize_articles_by_date(api_data)

        # Assign the data to articles_by_date to be accessible in the class
        self.articles_by_date = organized_articles

    # end load_data

    def compute_analysis(self) -> tuple[float, float]:
        """ Analyze previously-loaded data.

        This function runs an analytical measure of your choice 
        (mean, median, linear regression, etc...)
        and returns the data in a format of your choice.

        Parameters
        --------
        None

        Returns
        -------
        analysis_output : Any
        """
        pass
    # end compute_analysis

    def plot_data(self, save_path:Optional[str] = None) -> plt.Figure:
        """ Analyze and plot data.

        Generates a plot, display it to screen, and save it to the path
        in the parameter 'save_path', or the path from the configuration file 
        if not specified.

        Parameters
        ----------
        save_path : str, optional
            Save path for the generated figure

        Returns
        -------
        fig : matplotlib.Figure
        """
        pass
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
