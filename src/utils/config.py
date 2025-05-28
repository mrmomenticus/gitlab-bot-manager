import logging
import yaml
import argparse
from typing import Dict, Any


class Config:
    """Класс для хранения и управления конфигурацией"""

    def __init__(self, config_path: str):
        self._config = self._load_config(config_path)

    def _load_config(self, path: str) -> Dict[str, Any]:
        """Загружает конфигурацию из YAML файла"""
        try:
            with open(path, "r") as file:
                config = yaml.safe_load(file)
            return config
        except Exception as e:
            logging.critical(f"Error loading config: {e}")
            raise e

    def get(self) -> Dict[str, Any]:
        return self._config


def get_config_from_args() -> Config:
    """Создает объект конфигурации из аргументов командной строки"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", help="path to config file", required=True)
    args = parser.parse_args()
    return Config(args.config)
