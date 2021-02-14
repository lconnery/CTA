import sys
import logging

from src.data import CtaTrain
from src.data import StationNode


class DisplayManager(object):

    def __init__(self, station_data: [dict]):
        self.station_data = station_data

        self.stations: [StationNode] = list()
        self.__initialize_station_nodes()

    def __initialize_station_nodes(self):
        for node_data in self.station_data:
            self.__add_new_station_node(node_data=node_data)

    def __add_new_station_node(self, node_data: dict):
        try:
            station_id, station_name = node_data.values()
            station_node = StationNode(station_id=station_id,
                                       station_name=station_name)
            self.stations.append(station_node)
        except Exception as err:
            logging.error(f"Unable to create station node with '{node_data}'...errMsg: {err}")
            sys.exit(1)

    def update_locations(self, current_trains: [CtaTrain]):
        arrival_ids: [str] = self.__get_ids_from_current_trains(current_trains=current_trains)
        for station in self.stations:
            if station.station_id in arrival_ids:
                station.train_has_arrived()
            else:
                station.train_has_left()

    def print_stations(self):
        logging.info(f"----Printing Stations----")
        for station in self.stations:
            station.print()

    @staticmethod
    def __get_ids_from_current_trains(current_trains: [CtaTrain]) -> [str]:
        return list(map(lambda train: train.next_parent_stop_id, current_trains))
