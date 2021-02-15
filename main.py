import sys
import os


from src.utils import Configuration
from src.utils.log import initialize_logging
from src.cta import CtaTracker


def main(path_to_config_file: str):
    api_key = load_api_key()
    config = Configuration(path_to_config=path_to_config_file, api_key=api_key)
    initialize_logging(config=config)

    cta_tracker = CtaTracker(config=config)
    cta_tracker.run()


def load_api_key() -> str:
    app_env = get_app_env()
    if app_env == "dev":
        from dotenv import load_dotenv
        load_dotenv(dotenv_path='./.env')

        return os.environ['API_KEY']
    elif app_env == "prod":
        from dotenv import Dotenv
        return Dotenv('.env')['API_KEY']


def get_app_env() -> str:
    try:
        return os.environ['APP_ENV']
    except Exception as err:
        print(f"Unable to determine environment. Set 'APP_ENV' as 'dev' or 'prod' in run script..."
              f"errMsg: {err}")
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Missing config file...\nUsage: ./main.py ./config.json")

    path_to_config = sys.argv[1]

    print(f"Running CTA Tracker with {path_to_config}...")
    main(path_to_config_file=path_to_config)
