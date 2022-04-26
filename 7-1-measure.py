import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt


dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21,20,16,12,7,8,25,24]
bits = len(dac)
lvls = 2**bits
maxVoltage = 3.3
Troyka = 17
comparator = 4

def dec2bin(value):
    return[int(bit) for bit in bin(value)[2:].zfill(bits)]
def bin2dac(value):
    signal = dec2bin(value)
    GPIO.output(dac,signal)
    return signal
def bin2leds(value):
    signal = dec2bin(value)
    GPIO.output(leds,signal)
    return signal
def TroVal():
    for value in range(256):
            signal = bin2dac(value)
            voltage = value / lvls * maxVoltage
            time.sleep(0.0007)
            comparatorValue = GPIO.input(4)
            if comparatorValue == 0:
                bin2leds(value)
                break
    return value
        

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(Troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comparator, GPIO.IN)

data = []

try:
    while True:
        GPIO.output(Troyka, GPIO.HIGH)
        print("Charging...")
        tstart = time.time()

        while TroVal() <= 0.96 * 256:
            data.append(TroVal())
        GPIO.output(Troyka, 0)
        print("Discharging...")
        while TroVal() >= 0.02 * 256:
            data.append(TroVal())
        tfinish = time.time()

        measured_data_str = [str(item) for item in data]

        with open("data.txt", "w") as outfile:
            outfile.write("\n".join(measured_data_str))
        with open("settings.txt", "w") as outfile:
           outfile.write(str((tfinish-tstart)/len(data)))
           outfile.write("\n")
           outfile.write(str(maxVoltage/256))
        print("Time of experiment = {:.2f} sec; Time of one measurement = {:.4f} sec; Dec frequency = {:.2f} Hz; Quantization step = {:.3f} V".format(tfinish - tstart,(tfinish-tstart)/len(data),len(data)/(tfinish-tstart), maxVoltage/256))
        plt.plot(data)
        plt.show()
        break

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