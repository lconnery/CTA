import logging

from src.gpio import PinManger


class StationNode(object):

    def __init__(self, station_id: str, station_name: str, gpio_index: int):
        self.station_id = station_id
        self.station_name = station_name
        self.pin_manager = PinManger(gpio_index=gpio_index)
        self.has_train = False

    def train_has_arrived(self):
        self.has_train = True
        self.pin_manager.turn_on_power()

    def train_has_left(self):
        self.has_train = False
        self.pin_manager.turn_off_power()

    def print(self):
        if self.has_train:
            output_figure = "*"
        else:
            output_figure = ""

        x = ' '
        logging.info(f"{self.station_id}-{self.station_name}" + self.__print_spacing*x + output_figure)

    @property
    def __print_spacing(self) -> int:
        return 25 - (len(self.station_id) + len(self.station_name))

