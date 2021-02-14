import sys
import json
import time
import RPi.GPIO as GPIO


def main(path_to_config: str):
    config_data = get_config_data(path_to_config=path_to_config)

    initialize_gpio_settings()

    for data in config_data:
        _, _, gpio_index = data.values()
        test_gpio_pint(pin_index=gpio_index)


def test_gpio_pint(pin_index: int):
    print(f"----Running test for gpio index '{pin_index}'----")
    GPIO.setup(pin_index, GPIO.OUT)
    print('GPIO on')
    GPIO.output(pin_index, GPIO.HIGH)
    time.sleep(3)
    print('GPIO off')
    GPIO.output(pin_index, GPIO.LOW)


def initialize_gpio_settings():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)


def get_config_data(path_to_config: str) -> dict:
    try:
        with open(path_to_config, 'r') as file:
            return json.loads(file.read())
    except Exception as err:
        print(f"Unable to parse '{path_to_config}'... ErrorMsg: {err}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Script requires station config file as argument to test...')
        sys.exit()

    config_path = sys.argv[1]
    main(path_to_config=config_path)
