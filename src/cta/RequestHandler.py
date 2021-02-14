import os
import logging
import requests
from typing import Optional

from src.utils import Configuration
from src.data import CtaLocation


class RequestHandler(object):

    def __init__(self, config: Configuration):
        self.config = config

    def get_cta_locations(self) -> CtaLocation:
        data = self.__make_request()
        return CtaLocation(request_data=data)

    def __make_request(self) -> Optional[dict]:
        try:
            result = requests.request(method="GET", url=self.__generate_url())
            return result.json()
        except Exception as err:
            logging.error(f"Error getting data with url: {self.__generate_url()}\nerr_msg: {err}")
            return None

    def __generate_url(self) -> str:
        return f"{self.config.request_url}{self.__add_api_key()}{self.__add_route()}&outputType=JSON"

    def __add_route(self) -> str:
        return f"&rt={self.config.cta_line}"

    @staticmethod
    def __add_api_key() -> str:
        return f"?key={os.environ['API_KEY']}"
