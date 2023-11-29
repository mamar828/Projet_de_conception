import pyfirmata
import time

board = pyfirmata.Arduino('/dev/cu.usbmodem1101')

it = pyfirmata.util.Iterator(board)
it.start()

input_0 = board.get_pin("a:0:i")
input_1 = board.get_pin("a:1:i")
input_2 = board.get_pin("a:2:i")

while True:
    voltage_0 = input_0.read()
    voltage_1 = input_1.read()
    voltage_2 = input_2.read()
     
    if voltage:
        print(f"{voltage*5} V")
    else: print(None)
    time.sleep(1)