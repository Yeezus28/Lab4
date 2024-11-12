from hal import hal_input_switch as switch
from hal import hal_led as led
import time

flag = False  # Tracks if the 5-second blink has already been performed

def blink_led(delay):
    led.set_output(0, 1)
    time.sleep(delay)
    led.set_output(0, 0)
    time.sleep(delay)

def main():
    led.init()
    switch.init()

    while True:
        if switch.read_slide_switch() == 0:
            if not flag:
                start_time = time.time()
                while (time.time() - start_time) < 5:  # Blink for 5 seconds
                    blink_led(0.05)  # 10 Hz (0.05s on, 0.05s off)
                led.set_output(0, 0)  # Turn off LED after 5 seconds
                flag = True  # Set flag to avoid repeating the 5-second blink
        else:
            flag = False  # Reset flag to allow 5-second blink when switch is off
            blink_led(0.1)  # Continuous 5 Hz blinking when switch is on

# Run the main function
if __name__ == "__main__":
    main()
