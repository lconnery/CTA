import RPi.GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2,GPIO.OUT)
print('GPIO 2 on')
GPIO.output(21,GPIO.HIGH)
time.sleep(10)
print('GPIO 2 off')
GPIO.output(21,GPIO.LOW)