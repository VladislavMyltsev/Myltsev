import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)


p = GPIO.PWM(22, 1000)
p.start(0)


try:
    while True:
        inputStr = input("Put a dutycycle (in percents) <'q' to exit>:")
        if inputStr.isdigit():
            dc = int(inputStr)
            if dc > 100:
                print("Enter value in percents (0-100):")
                continue
            else:
                p.ChangeDutyCycle(dc)
                print("Final voltage =",3.3*dc/100)
        elif inputStr == 'q':
            break
        else:
            print("Enter a positive integer:")
            continue
except KeyboardInterrupt:
    print("The program was stoped by the keyboard")
else:
    print("No exceptions")
finally:
    p.stop()
    GPIO.cleanup()
    print("GPIO cleanup completed")