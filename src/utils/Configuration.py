import sys
import json


class Configuration(object):

    def __init__(self, path_to_config: str, api_key: str):
        self.__config_file = path_to_config
        self.__api_key = api_key

        self.__load_config_data()
        self.__set_props()

    def __load_config_data(self):
        try:
            with open(self.__config_file, 'r') as file:
                self.__data = json.loads(file.read())
        except Exception as err:
            print(f"Issue loading config file. err_msg: {err}")
            sys.exit(1)

    def __set_props(self):
        self.__app_name = self.__load_value(key='app_name', default_val='CTA_Tracker')
        self.__logging_directory = self.__load_value(key='logging_directory', default_val='/sitelogs/CTA')
        self.__cta_line = self.__load_value(key='cta_line', default_val='red')
        self.__update_interval_seconds = self.__load_value(key="update_interval_seconds", default_val=60)
        self.__request_url = self.__load_value(key="request_url", default_val=None)
        self.__path_to_station_config = self.__load_value(key="path_to_station_config", default_val=None)

    def __load_value(self, key: str, default_val: any):
        if key in self.__data:
            return self.__data[key]

        print(f"Config: {key} not found, using default value {default_val}")
        return default_val

    @property
    def api_key(self) -> str:
        return self.__api_key

    @property
    def app_name(self) -> str:
        return self.__app_name

    @property
    def logging_directory(self) -> str:
        return self.__logging_directory

    @property
    def cta_line(self) -> str:
        return self.__cta_line

    @property
    def update_interval_seconds(self) -> int:
        return self.__update_interval_seconds

    @property
    def request_url(self) -> str:
        return self.__request_url

    @property
    def path_to_station_config(self) -> str:
        return self.__path_to_station_config
