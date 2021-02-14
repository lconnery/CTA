import logging


class StationNode(object):

    def __init__(self, station_id: str, station_name: str):
        self.station_id = station_id
        self.station_name = station_name
        self.has_train = False

    def train_has_arrived(self):
        self.has_train = True

    def train_has_left(self):
        self.has_train = False

    def print(self):
        if self.has_train:
            output_figure = "*"
        else:
            output_figure = ""

        x = ' '
        logging.info(f"{self.station_id}-{self.station_name}"+ self.__print_spacing*x + output_figure)

    @property
    def __print_spacing(self) -> int:
        return 25 - (len(self.station_id) + len(self.station_name))

