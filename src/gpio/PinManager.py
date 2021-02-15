import RPi.GPIO as GPIO


class PinManger(object):

    def __init__(self, gpio_index: int):
        self.gpio_index = gpio_index

        self.__set_gpio_props()

    def __set_gpio_props(self):
        GPIO.setup(self.gpio_index, GPIO.OUT)

    def turn_off_power(self):
        GPIO.output(self.gpio_index,GPIO.LOW)

    def turn_on_power(self):
        GPIO.output(self.gpio_index, GPIO.HIGH)

    @staticmethod
    def initialize_gpio_settings():
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

