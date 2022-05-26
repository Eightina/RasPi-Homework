import RPi.GPIO as GPIO
import time
'''
2021-r2
2722-r1
1926-l1
613-l2
'''
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#l1
GPIO.setup(19,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
#l2
GPIO.setup(6,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
#r1
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
#r2
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)

time.sleep(0.2)

lm1a = gpio.PWM(19, 100)
lm1b = gpio.PWM(26, 100)
lm2a = gpio.PWM(6, 100)
lm2b = gpio.PWM(13, 100)
rm1a = gpio.PWM(27, 100)
rm1b = gpio.PWM(22, 100)
rm2a = gpio.PWM(20, 100)
rm2b = gpio.PWM(21, 100)

pwm1.start(0)
pwm2.start(0)
pwm3.start(0)
pwm4.start(0)

def fwd():
    lm1a.ChangeDutyCycle(100)
    lm1b.ChangeDutyCycle(50)
    lm2a.ChangeDutyCycle(100)
    lm2b.ChangeDutyCycle(50)
    rm1a.ChangeDutyCycle(100)
    rm1b.ChangeDutyCycle(50)
    rm2a.ChangeDutyCycle(100)
    rm2b.ChangeDutyCycle(50)
def bk():
    lm1a.ChangeDutyCycle(0)
    lm1b.ChangeDutyCycle(0)
    lm2a.ChangeDutyCycle(0)
    lm2b.ChangeDutyCycle(0)
    rm1a.ChangeDutyCycle(0)
    rm1b.ChangeDutyCycle(0)
    rm2a.ChangeDutyCycle(0)
    rm2b.ChangeDutyCycle(0)
