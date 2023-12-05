import pyfirmata
import time

# board = pyfirmata.Arduino('/dev/cu.usbmodem1101')

# it = pyfirmata.util.Iterator(board)
# it.start()

# input_1 = board.get_pin("a:0:i")

# while True:
#     voltage = input_1.read()
#     if voltage:
#         print(f"{voltage*5} V")
#     else: print(None)
#     time.sleep(1)

# Flicker when there is current in pin 10
# board = pyfirmata.Arduino('/dev/cu.usbmodem1101')

# it = pyfirmata.util.Iterator(board)
# it.start()

# board.digital[10].mode = pyfirmata.INPUT

# while True:
#     sw = board.digital[10].read()
#     if sw is True:
#         board.digital[13].write(1)
#     else:
#         board.digital[13].write(0)
#     time.sleep(0.1)



# Keep the name of a pin

board = pyfirmata.Arduino('/dev/cu.usbmodem1101')

it = pyfirmata.util.Iterator(board)
it.start()

digital_input = board.get_pin('d:10:i')
led = board.get_pin('d:13:o')

while True:
    # sw = digital_input.read()
    # if sw is True:
    led.write(1)
    # else:
    #     led.write(0)
    time.sleep(0.1)







# print("allo")
# print("\033[1;31;40mAnanananannanannanan not equal.\033[0m")
# print("allo")

