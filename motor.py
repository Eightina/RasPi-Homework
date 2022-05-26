import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)

GPIO.setup(17,GPIO.IN)
GPIO.setup(5,GPIO.IN)
GPIO.setup(18,GPIO.IN)

GPIO.setup(12,GPIO.OUT)
GPIO.setup(23,GPIO.IN)
GPIO.setup(24,GPIO.IN)
GPIO.setup(25,GPIO.IN)
time.sleep(0.2)

GPIO.output(20,False)
GPIO.output(21,False)
GPIO.output(19,False)
GPIO.output(26,False)
GPIO.output(27,False)
GPIO.output(22,False)
GPIO.output(6,False)
GPIO.output(13,False)
GPIO.output(12,False)



def fwd():
    GPIO.output(20,True)
    GPIO.output(21,False)
    GPIO.output(19,True)
    GPIO.output(26,False)
    GPIO.output(27,True)
    GPIO.output(22,False)
    GPIO.output(6,True)
    GPIO.output(13,False)
    time.sleep(2000)

def bwd():
    GPIO.output(20,False)
    GPIO.output(21,True)
    GPIO.output(19,False)
    GPIO.output(26,True)
    GPIO.output(27,False)
    GPIO.output(22,True)
    GPIO.output(6,False)
    GPIO.output(13,True)
    time.sleep(2000)

def end():
    GPIO.output(20,False)
    GPIO.output(21,True)
    GPIO.output(19,False)
    GPIO.output(26,True)
    GPIO.output(27,False)
    GPIO.output(22,True)
    GPIO.output(6,False)
    GPIO.output(13,True)
    time.sleep(1500)
    GPIO.output(20,False)
    GPIO.output(21,False)
    GPIO.output(19,False)
    GPIO.output(26,False)
    GPIO.output(27,False)
    GPIO.output(22,False)
    GPIO.output(6,False)
    GPIO.output(13,False)
    
'''
2021-r2
2722-r1
1926-l1
613-l2
'''

def lft():
    GPIO.output(19,False)
    GPIO.output(26,True)
    GPIO.output(6,False)
    GPIO.output(13,False)
    GPIO.output(20,False)
    GPIO.output(21,False)
    GPIO.output(27,True)
    GPIO.output(22,False)
    time.sleep(2000)

def rht():
    GPIO.output(20,False)
    GPIO.output(21,False)
    GPIO.output(27,False)
    GPIO.output(22,True)
    GPIO.output(19,True)
    GPIO.output(26,False)
    GPIO.output(6,False)
    GPIO.output(13,False)
    time.sleep(2000)

def brk():
    GPIO.output(20,False)
    GPIO.output(21,False)
    GPIO.output(19,False)
    GPIO.output(26,False)
    GPIO.output(27,False)
    GPIO.output(22,False)
    GPIO.output(6,False)
    GPIO.output(13,False)
    time.sleep(2000)
