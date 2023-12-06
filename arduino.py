import pyfirmata
import time

# Initialize board and input updating
board = pyfirmata.Arduino('/dev/cu.usbmodem1101')
it = pyfirmata.util.Iterator(board)
it.start()

# Setup name for used pins
input_0 = board.get_pin("a:0:i")
output = board.get_pin("d:11:p")

# The following ratios are used to limit the arduino PWM output (a ratio of 1 would mean 5V, 0 would be 0V)
max_v_ratio = 0.55
min_v_ratio = 0.32

while True:
    try:
        # Get voltage values at different points in the circuit (v_2 and v_0 are hard-coded)
        v_0 = 9                         # Battery voltage
        v_1 = input_0.read()            # Between photoresistance and 1000 ohms resistance
        v_2 = 0                         # Ground

        # Check the validity of the voltage read
        if v_1 is not None:
            v_1 *= 5            # Convert 0-1 V to 0-5 V
            current = (v_1 - v_2) / 1000
            r_photo = (v_0 - v_1) / current

            # Set ratio of resistance between 1 and 0 (1 is brightest, 0 is darkest) to control voltage output
            max_ratio = 1 - (r_photo - 5000) / 15000
            if max_ratio < 0: max_ratio = 0
            elif max_ratio > 1: max_ratio = 1

            print((f"ai_0: {v_0:.3f}, ai_1: {v_1:.3f}, ai_2: {v_2:.3f}, current: {current:.3f},") + 
                   (f"r_photo: {r_photo:.3f}, max_ratio: {max_ratio:.3f}"))

            output.write(max_ratio * (max_v_ratio - min_v_ratio) + min_v_ratio)
        else:
            print(f"\033[1;31;40mVoltage input missing. ai_0: {v_0}, ai_1: {v_1}, ai_2: {v_2}\033[0m")
        
    except:
        print("ERROR")
    
    # Set updating delay to prevent CPU overloading
    time.sleep(0.1)
