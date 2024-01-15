import pytest
import load_config_step

required_keys = ['api_token', 'plot_title', 'plot_xaxis_title', 'plot_yaxis_title', 'save_path']

def test_load_config():
  '''
  This script will test the output of the __init__ function.

  The output of the __init_ function is a dictionary containing the config items as
  keys: values as a self-parameter to be referenced by subsequent functions defined 
  in the Class.

  To test the __init__ function, follow the steps below:
  A) Preparing __init__ function for testing:
    1) Copy/paste the __init__() function to a new python file.
      Include lines from 'def __init__()' to 'self.config'
    2) Remove 'self,' from within the parentheses in '__init__()'.
    3) Rename the function from '__init__' to 'load_config'.
    4) Replace 'self.config' line with 'return config'.
      This will set the output of this function to return the [config] dictionary.
    5) Save this python file as load_config_step.py
  B) Run test_load_config_file.py
    1) Open bash shell.
      If using Google Colab, run the following code in two separate cells:
        !pip install google_colab.shell
        from google_colab_shell import getshell

        getshell()
    2) In shell type: pytest test_load_config_step.py
    3) Output from shell will show results of the test.
        For example:
        █$ colab>>  pytest Test_Analysis.py
          ============================= test session starts =========================
          platform linux -- Python 3.10.12, pytest-7.4.4, pluggy-1.3.0
          rootdir: /content
          plugins: anyio-3.7.1
          collected 1 item

          Test_Analysis.py . [100%]

          ============================= 1 passed in 0.03s ===========================
  C) This test function is testing the entries taken from the config files,
     to determine of all five of the necessary items are present to proceed forward
     with the analysis. To test further, go back to the original config files and
     edit/remove items.


  PARAMETERS:
  -----------
  required_keys : this is list of keys that are required/expected.

  RESULT:
  -------
  actual_outputs : this is the dictionary (keys:values) outputted from load_config().
  
  EXAMPLE:
  After edits, load_config_step.py should look like this:

  ###Edited version of load config step from Class###
  import yaml
  import os

  def load_config(analysis_config:Optional[str] = None):
    # The base config path is the installed location of the package
    base_config_path = os.path.dirname(__file__)

    # list of config layer files - order by general to specific
    CONFIG_PATHS = [ 'system_config.yml',
                    'user_config.yml',
                    'analysis_config.yml']

    # add analysis config to list of paths to load
    paths_to_load = [os.path.join(base_config_path, path) for path in CONFIG_PATHS]
    if analysis_config is not None:
      try:
        if os.path.exists(analysis_config):
          paths_to_load.append(analysis_config)
          print(f'User provided file path is valid.')
        else:
          raise FileNotFoundError(f'User file path does not exist.')
      except ValueError as e:
        raise TypeError(f'{analysis_config} is not a string.')

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
    #self.config = config
    #self.articles_by_date = {}
    return config

  '''

  expected_output = {'plot_color': 'yellow', 
                     'font_size': 16, 
                     'api_token': 'AGKIVke1cHUkTIe8C8L8lI7DYnXQJaPJ', 
                     'plot_title': 'Number of Mentions of the Word "Pokemon" on New York Times Front Page by Year', 
                     'plot_xaxis_title': 'Years', 
                     'plot_yaxis_title': 'Number of Article Mentions', 
                     'save_path': 'image.png'}

  actual_output = {}
  actual_output = load_config_step.load_config()
  
  assert all(key in actual_output for key in required_keys), "Not all required keys contained in config files."