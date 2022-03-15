import RPi.GPIO as GPIO

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
        inputStr = input ("Enter a value between 0 and 255 ('q' to exit) >")

        if inputStr.isdigit():
            value = int(inputStr)

            if value >= lvls:
                print("The value is too large, try again")
                continue
                
            signal = bin2dac(value)
            voltage = value/lvls * maxVoltage
            print("Entered value = {} -> {}, output voltage = {:.2f}".format(value,signal,voltage))
        elif inputStr == 'q':
            break
        else:
            print("Enter a positive integer")
            continue
except KeyboardInterrupt:
    print("The program was stoped by the keyboard")
else:
    print("No exceptions")
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    print("GPIO cleanup completed")