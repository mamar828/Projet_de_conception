import pyfirmata
import time

# Initialize board and input updating
board = pyfirmata.Arduino('/dev/cu.usbmodem1101')
it = pyfirmata.util.Iterator(board)
it.start()

# Setup pins
input_0 = board.get_pin("a:0:i")
output = board.get_pin("d:11:p")

while True:
    try:
        # Get voltage values
        v_1 = input_0.read()
        v_2 = 0
        v_0 = 9

        # Check the validity of every voltage
        if v_0 is not None:
            v_1 *= 5        # Convert 0-1 V to 0-5 V
            R_1 = 1000
            R_2 = 10000

            current = (v_1 - v_2) / 1000
            r_photo = (v_0 - v_1) / current
            # print(f"v_1 : {v_1:.5f}, current : {current:.5f}, r_photo : {r_photo:.5f}")

            # Set ratio of resistance between 1 and 0 (1 is brightest, 0 is darkest) to control voltage output
            max_ratio = 1 - (r_photo - 5000) / 15000
            # max_ratio = 1 - (r_photo - 1000) / 199000
            if max_ratio < 0: max_ratio = 0 
            elif max_ratio > 1: max_ratio = 1 
            print(f"ai_0: {v_0:.3f}, ai_1: {v_1:.3f}, ai_2: {v_2:.3f}, current: {current:.3f}, r_photo: {r_photo:.3f}, max_ratio: {max_ratio:.3f}")

            output.write(max_ratio)
        else:
            print(f"\033[1;31;40mVoltage input missing. ai_0: {v_0}, ai_1: {v_1}, ai_2: {v_2}\033[0m")
        
    except:
        print("ERROR")
    
    time.sleep(0.1)
