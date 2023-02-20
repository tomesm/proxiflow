import yaml
from typing import Dict


class Config:
    """
    A class for loading configuration data from a YAML file.

    Parameters:
    file_path (str): The path to the YAML configuration file.
    """

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.config = self.load_config(file_path)

    @staticmethod
    def load_config(file_path: str) -> Dict:
        """
        Load a YAML configuration file from the specified file path.

        Parameters:
        file_path (str): The path to the YAML configuration file.

        Returns:
        dict: A dictionary containing the configuration values.

        Raises:
        FileNotFoundError: If the specified file path does not exist.
        ValueError: If the specified file is empty or cannot be parsed as YAML.
        """
        try:
            with open(file_path, "r") as f:
                config = yaml.safe_load(f)
            if config is None:
                raise ValueError("Config file is empty")
            return config
        except FileNotFoundError:
            raise FileNotFoundError("Config file not found")
        except yaml.YAMLError as e:
            raise ValueError(f"Error parsing config file: {str(e)}")

    @property
    def cleaning_config(self) -> Dict:
        """
        Get the data cleaning configuration values from the configuration dictionary.

        Returns:
        dict: A dictionary containing the data cleaning configuration values.

        Raises:
        ValueError: If the "data_cleaning" key is not present in the configuration dictionary.
        """
        try:
            return self.config["data_cleaning"]
        except KeyError:
            raise ValueError("data_cleaning config not found in config file")

    @property
    def normalization_config(self) -> Dict:
        """
        Get the data normalization configuration values from the configuration dictionary.

        Returns:
        dict: A dictionary containing the data normalization configuration values.

        Raises:
        ValueError: If the "data_normalization" key is not present in the configuration dictionary.
        """
        try:
            return self.config["data_normalization"]
        except KeyError:
            raise ValueError("data_normalization config not found in config file")

    @property
    def feature_engineering_config(self) -> Dict:
        """
        Get the feature engineering configuration values from the configuration dictionary.

        Returns:
        dict: A dictionary containing the feature engineering configuration values.

        Raises:
        ValueError: If the "feature_engineering" key is not present in the configuration dictionary.
        """
        try:
            return self.config["feature_engineering"]
        except KeyError:
            raise ValueError("feature_engineering config not found in config file")