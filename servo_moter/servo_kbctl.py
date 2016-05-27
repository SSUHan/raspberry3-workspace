import RPi.GPIO as GPIO
import time

pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

p = GPIO.PWM(pin, 50)
p.start(0)
def doAngle(angle):
    p.ChangeDutyCycle(angle)
    print "Angle: %d" % angle
    time.sleep(0.5)




var = 1
try:

    while True:
        var = float(raw_input("dutyCycle value : "))
        doAngle(var)
#        var = raw_input("Enter L/R/C : ")
#        if var == 'R' or var == 'r' :
#            print "Right"
#            doAngle(2.5)
#        elif var == 'L' or var == 'l':
#            print "Left"
#            doAngle(12.5)
#        elif var == 'C' or var == 'c':
#            print "Center"
#            doAngle(7.5)
except KeyboardInterrupt:
    p.stop()
GPIO.cleanup()

