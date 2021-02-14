from typing import Optional
from copy import deepcopy

from src.data.CtaTrain import CtaTrain


class CtaLocation(object):

    def __init__(self, request_data: dict):
        if request_data is not None:
            self.request_data = request_data['ctatt']
        else:
            self.request_data = None

        self.__trains = []
        self.__construct_trains()

    @property
    def is_loaded(self) -> bool:
        """
        Checks to see if data is not None and error code is '0'
        :return: boolean
        """
        if self.request_data is None:
            return False

        return self.request_data['errCd'] == "0"

    @property
    def error_description(self) -> Optional[str]:
        if self.request_data is None:
            return "Request Data is None"

        if not self.is_loaded:
            return self.request_data['errNm']

        return None

    @property
    def route_title(self) -> str:
        return self.__route['@name']

    @property
    def __route(self) -> dict:
        return self.request_data['route'][0]

    @property
    def trains(self) -> [CtaTrain]:
        return deepcopy(self.__trains)

    def __construct_trains(self):
        if self.is_loaded:
            for train_data in self.__route['train']:
                self.__trains.append(CtaTrain(data=train_data.copy()))
