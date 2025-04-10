import logging
from http import HTTPStatus

import yaml
import os

from exception.generic_exception import GenericException


class ConfigLoader:
    config_path = 'C:\\Users\\ThinkPad\\Documents\\Projects\\conf\\config.yml'

    def __init__(self):
        # Load the configuration when the class is instantiated
        self.config = self.load_config()

    """
        Load the YAML configuration file.
        Raises an exception if the file cannot be read or parsed.
    """
    @staticmethod
    def load_config():

        if not os.path.exists(ConfigLoader.config_path):
            logging.error(f"Configuration file not found: {ConfigLoader.config_path}")
            raise FileNotFoundError(f"Configuration file not found: {ConfigLoader.config_path}")

        try:
            with open(ConfigLoader.config_path, "r") as file:
                return yaml.safe_load(file)
        except Exception as e:
            logging.error(f"Error loading configuration file: {e}")
            raise GenericException(HTTPStatus.SERVICE_UNAVAILABLE,
                                   f"Error loading configuration file: {ConfigLoader.config_path}",
                                   "Service is currently unavailable")

    @staticmethod
    def get_config():
        # Get loaded configuration
        return ConfigLoader().config

        # def get_property(self, key: str):
    #     Get a property from the loaded configuration.
    #     keys = key.split(".")
    #     value = self.config
    #     for k in keys:
    #         value = value.get(k)
    #         if value is None:
    #             raise KeyError(f"Configuration key not found: {key}")
    #     return value
