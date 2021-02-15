import sys
from dotenv import load_dotenv

from src.utils import Configuration
from src.utils.log import initialize_logging
from src.cta import CtaTracker

load_dotenv(dotenv_path='./.env')


def main(path_to_config_file: str):
    config = Configuration(path_to_config=path_to_config_file)
    initialize_logging(config=config)

    cta_tracker = CtaTracker(config=config)
    cta_tracker.run()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Missing config file...\nUsage: ./main.py ./config.json")

    path_to_config = sys.argv[1]

    print(f"Running CTA Tracker with {path_to_config}...")
    main(path_to_config_file=path_to_config)
