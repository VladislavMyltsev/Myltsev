import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt


dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21,20,16,12,7,8,25,24]
bits = len(dac)
lvls = 2**bits
maxVoltage = 3.3

def dec2bin(value):
    return[int(bit) for bit in bin(value)[2:].zfill(bits)]
def bin2dac(value):
    signal = dec2bin(value)
    GPIO.output(dac,signal)
    return signal
def TroVal():
    value = 0
    while GPIO.input(4) != 0 and value <= 256:
           bin2dac(value)
           value += 1
    return value
def TroLeds(value):
    signal = dec2bin(value)
    GPIO.output(leds,signal)
    return signal
        

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(4, GPIO.IN)

data = []

try:
        GPIO.output(17, GPIO.HIGH)
        tstart = time.time()
        while TroVal() < 250:
            data.append(TroVal() / lvls * maxVoltage)
            TroLeds(TroVal())
            print(TroVal())
        GPIO.output(17,1)
        while TroVal() > 10:
            data.append(TroVal() / lvls * maxVoltage)
            TroLeds(TroVal())
            print(TroVal())
        tfinish = time.time()

        measured_data_str = [str(item) for item in data]

        with open("data.txt", "w") as outfile:
            outfile.write("\n".join(measured_data_str))
        with open("settings.txt", "w") as outfile:
           outfile.write("Dec frequency =",len(data)/(tfinish-tstart),"sec")
    
        plt.plot(data)
        plt.show()

except KeyboardInterrupt:
    print("The program was stoped by the keyboard")
else:
    print("No exceptions")
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.output(leds, GPIO.LOW)
    GPIO.cleanup(dac)
    GPIO.output(leds, GPIO.LOW)
    print("GPIO cleanup completed")