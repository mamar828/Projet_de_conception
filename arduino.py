import pyfirmata
import time

# Initialize board and input updating
board = pyfirmata.Arduino('/dev/cu.usbmodem1101')
it = pyfirmata.util.Iterator(board)
it.start()

# Setup pins
input_0 = board.get_pin("a:0:i")
input_1 = board.get_pin("a:1:i")
input_2 = board.get_pin("a:2:i")
output = board.get_pin("d:11:p")

while True:
    # Get voltage values
    v_0 = input_0.read()
    v_1 = input_1.read()
    v_2 = input_2.read()

    # Check the validity of every voltage
    if v_0 is not None and v_1 is not None and v_2 is not None:
        current = (v_1 - v_2) / 1000
        r_photo = (v_0 - v_1) / current

        # Set ratio of resistance between 1 and 0 (1 is brightest, 0 is darkest) to control voltage output
        max_ratio = 1 - (r_photo - 1000) / 199000
        if max_ratio < 0: max_ratio = 0 
        elif max_ratio > 1: max_ratio = 1 
        print(f"ai_0: {v_0}, ai_1: {v_1}, ai_2: {v_2}, current: {current}, r_photo: {r_photo}, max_ratio: {max_ratio}")

        output.write(max_ratio)
    else:
        print(f"\033[1;31;40mVoltage input missing. ai_0: {v_0}, ai_1: {v_1}, ai_2: {v_2}\033[0m")
    
    time.sleep(1)
