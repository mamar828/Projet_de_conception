import pyfirmata
import time

board = pyfirmata.Arduino('/dev/cu.usbmodem1101')

it = pyfirmata.util.Iterator(board)
it.start()

# analog_input = board.get_pin('a:0:i')
led = board.get_pin('d:13:o')

while True:
    led.write(1)
    time.sleep(0.5)
    led.write(0)
    time.sleep(0.5)
#     analog_value = analog_input.read()
#     if analog_value is not None:
#         led.write(analog_value)
#     time.sleep(0.1)