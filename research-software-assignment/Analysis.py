# Building Research Software Assignment
# January 2024

import matplotlib
import matplotlib.pyplot as plt
import yaml


class Analysis():
    def __init__(self, analysis_config:str):
        """ Analysis class constructor, loads configuration files.

        Load system-wide configuration from 'configs/system_config.yml', 
        user configuration from 'configs/user_config.yml', 
        and the specified analysis configuration file

        Parameters
        ----------
        analysis_config : str
            Path to the analysis/job-specific configuration file

        Returns
        -------
        analysis_obj : Analysis
            Analysis object containing consolidated parameters from the configuration files

        Notes
        -----
        The configuration files should include parameters for:
            * GitHub API token
            * Plot color
            * Plot title
            * Plot x and y axis titles
            * Figure size
            * Default save path
        """

        # Define member variables
        self.config = {}
    # end __init__

    def load_data(self):
        """ Retrieve data from the GitHub API.

        This function makes an HTTPS request to the GitHub API 
        and retrieves your selected data. The data is
        stored in the Analysis object.

        Parameters
        ----------
        None
    
        Returns
        -------
        None
        """
        pass
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

