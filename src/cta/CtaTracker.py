import sys
import time
import logging

from src.utils import Configuration, StationConfigReader
from src.data import CtaLocation
from src.data import CtaTrain
from src.cta.RequestHandler import RequestHandler
from src.cta.DisplayManager import DisplayManager


class CtaTracker(object):

    def __init__(self, config: Configuration):
        self.config = config
        self.request_handler = RequestHandler(config=self.config)

        stations = StationConfigReader.read_station_data(path_to_config=config.path_to_station_config)
        self.display_manager = DisplayManager(station_data=stations)

    def run(self):
        while True:
            cta_location: CtaLocation = self.request_handler.get_cta_locations()
            if cta_location.is_loaded:
                trains: [CtaTrain] = cta_location.trains
                self.display_manager.update_locations(current_trains=trains)
                self.display_manager.print_stations()
            else:
                logging.error(f"cta_location not loaded. err_msg: {cta_location.error_description}")
            self.__timeout()

    def __timeout(self):
        time.sleep(self.config.update_interval_seconds)
