import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
lvls = 2**bits
maxVoltage = 3.3

def dec2bin(value):
    return[int(bit) for bit in bin(value)[2:].zfill(bits)]
def bin2dac(value):
    signal = dec2bin(value)
    GPIO.output(dac,signal)
    return signal

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)

try:
    while True:
        inputStr = input("Put a time of one period (in seconds):")
        if inputStr.isdigit():
            decfreq = int(inputStr)/512
            for i in range(256):
                bin2dac(i)
                time.sleep(decfreq)
                GPIO.output(dac,0)
            for i in range(255,0,-1):
                bin2dac(i)
                time.sleep(decfreq)
                GPIO.output(dac,0)
        else:
            print("Enter a positive integer:")
            continue
except KeyboardInterrupt:
    print("The program was stoped by the keyboard")
else:
    print("No exceptions")
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    print("GPIO cleanup completed")