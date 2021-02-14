import os
import logging
from datetime import datetime

from src.utils import Configuration


def initialize_logging(config: Configuration):
      logging.basicConfig(filename=get_log_file_name(config=config),
                        format="%(asctime)s:%(levelname)s   %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S",
                        level=logging.INFO)


def get_log_file_name(config: Configuration) -> str:
    return f'{config.logging_directory}/{config.app_name}.{datetime.now().strftime("%Y-%m-%d.%H:%M:%S")}.log'
