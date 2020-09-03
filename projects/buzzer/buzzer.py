import explorerhat as eh
import RPi.GPIO as GPIO


# Sets up GPIO pin 18 as a PWM output with freq. of 400 Hz.
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
buzzer = GPIO.PWM(18, 400)

while True:
    if eh.touch.one.is_pressed():
        buzzer.start(50)
    else:
        buzzer.stop()




