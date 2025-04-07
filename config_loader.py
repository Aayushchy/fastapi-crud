import yaml
import os

class ConfigLoader:
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.config = self._load_config()

    def _load_config(self):
        """
        Load the YAML configuration file.
        Raises an exception if the file cannot be read or parsed.
        """
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")

        try:
            with open(self.config_path, "r") as file:
                return yaml.safe_load(file)
        except yaml.YAMLError as e:
            raise Exception(f"Error parsing YAML file: {e}")
        except Exception as e:
            raise Exception(f"Error loading configuration file: {e}")

    def get_property(self, key: str):
        """
        Get a property from the loaded configuration.
        Raises an exception if the key is not found.
        """
        keys = key.split(".")
        value = self.config
        for k in keys:
            value = value.get(k)
            if value is None:
                raise KeyError(f"Configuration key not found: {key}")
        return value