import sys
import logging
import json


class StationConfigReader(object):

    @staticmethod
    def read_station_data(path_to_config: str) -> [dict]:
        try:
            with open(path_to_config, 'r') as file:
                return json.loads(file.read())
        except Exception as err:
            logging.error(f"Unable to load station config file '{path_to_config}', ErrMsg: {err}")
            sys.exit(1)
