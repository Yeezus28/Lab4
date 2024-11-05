from hal import hal_input_switch as switch
from hal import hal_led as led
import time

def blink_led(frequency, duration=None):
    period = 1.0 / frequency
    delay = period / 2
    
    start_time = time.time()
    while True:
        # Check duration if specified
        if duration and (time.time() - start_time) >= duration:
            break
            
        led.set_output(0, 1)  #LED ON
        time.sleep(delay)
        led.set_output(0, 0)  #LED OFF
        time.sleep(delay)

def main():
    led.init()
    switch.init()
    
    while True:
        switch_position = switch.read_slide_switch()
        
        if switch_position == 0:  #Left position
            blink_led(5)
        else:  #Right position
            blink_led(10, 5)
            led.set_output(0, 0)  # Ensure LED is off after blinking

if __name__ == "__main__":
    main()