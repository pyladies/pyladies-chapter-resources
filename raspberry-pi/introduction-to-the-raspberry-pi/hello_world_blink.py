# The Rpi.GPIO library makes it easy for your programs to read from and write to
# the Raspberry Pi's GPIO (General Purpose Input/Output) pins
import RPi.GPIO as GPIO
import time

# GPIO.BCM mode selects the pin numbering system of GPIO pin channels
# as opposed to GPIO.BOARD mode which uses P1 connector pin numbers
GPIO.setmode(GPIO.BCM)
# Any Raspberry Pi pin you use needs to be set as either an input or an output
# Here we are setting pin GPIO 20 as an output to control the LED
GPIO.setup(20, GPIO.OUT)

# Blink the LED 20 times
for i in range(20):
    # Output high (3.3 volts) on pin 20, to turn the LED on
    GPIO.output(20, 1)
    # Leave the LED on for one second
    time.sleep(1)
    # Output low (0 volts) on pin 20, to turn the LED off
    GPIO.output(20, 0)
    # Leave the LED off for one second
    time.sleep(1)

# This resets any ports used in your program
GPIO.cleanup()

# Why not? :-)
print("Hello World!")
# This will print some general info about your Raspberry Pi
print("Raspberry Pi stats: {}".format(GPIO.RPI_INFO))
