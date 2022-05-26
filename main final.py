import RPi.GPIO as GPIO
import time
#===================================
print('resetting GPIO...')
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

GPIO.setup(17,GPIO.IN)
GPIO.setup(5,GPIO.IN)
GPIO.setup(18,GPIO.IN)

GPIO.setup(12,GPIO.OUT)
GPIO.setup(23,GPIO.IN)
GPIO.setup(24,GPIO.IN)
GPIO.setup(25,GPIO.IN)
time.sleep(0.2)


GPIO.output(12,False)
#=====================================
print('adjusting PWM')
lm1a = GPIO.PWM(19, 500)
lm1b = GPIO.PWM(26, 500)
lm2a = GPIO.PWM(6, 500)
lm2b = GPIO.PWM(13, 500)
rm1a = GPIO.PWM(27, 500)
rm1b = GPIO.PWM(22, 500)
rm2a = GPIO.PWM(20, 500)
rm2b = GPIO.PWM(21, 500)
lm1a.start(0)
lm1b.start(0)
lm2a.start(0)
lm2b.start(0)
rm1a.start(0)
rm1b.start(0)
rm2a.start(0)
rm2b.start(0)


#===============================
'''
2021-r2
2722-r1
1926-l1
613-l2
'''
def fwd():
    lm1a.ChangeDutyCycle(100)
    lm1b.ChangeDutyCycle(60)
    lm2a.ChangeDutyCycle(100)
    lm2b.ChangeDutyCycle(60)
    rm1a.ChangeDutyCycle(100)
    rm1b.ChangeDutyCycle(60)
    rm2a.ChangeDutyCycle(100)
    rm2b.ChangeDutyCycle(60)
    time.sleep(0.0000001)
    lm1a.ChangeDutyCycle(100)
    lm1b.ChangeDutyCycle(65)
    lm2a.ChangeDutyCycle(100)
    lm2b.ChangeDutyCycle(65)
    rm1a.ChangeDutyCycle(100)
    rm1b.ChangeDutyCycle(65)
    rm2a.ChangeDutyCycle(100)
    rm2b.ChangeDutyCycle(65)
    time.sleep(0.0000001)

def Rfwd():
    lm1a.ChangeDutyCycle(100)
    lm1b.ChangeDutyCycle(0)
    lm2a.ChangeDutyCycle(100)
    lm2b.ChangeDutyCycle(0)
    rm1a.ChangeDutyCycle(100)
    rm1b.ChangeDutyCycle(0)
    rm2a.ChangeDutyCycle(100)
    rm2b.ChangeDutyCycle(0)
    time.sleep(0.01) 
        
def bwd():
    lm1a.ChangeDutyCycle(65)
    lm1b.ChangeDutyCycle(100)
    lm2a.ChangeDutyCycle(65)
    lm2b.ChangeDutyCycle(100)
    rm1a.ChangeDutyCycle(65)
    rm1b.ChangeDutyCycle(100)
    rm2a.ChangeDutyCycle(65)
    rm2b.ChangeDutyCycle(100)
    time.sleep(0.000001)

def Rbwd():
    lm1a.ChangeDutyCycle(50)
    lm1b.ChangeDutyCycle(100)
    lm2a.ChangeDutyCycle(50)
    lm2b.ChangeDutyCycle(100)
    rm1a.ChangeDutyCycle(50)
    rm1b.ChangeDutyCycle(100)
    rm2a.ChangeDutyCycle(50)
    rm2b.ChangeDutyCycle(100)
    time.sleep(0.00001)
    lm1a.ChangeDutyCycle(75)
    lm1b.ChangeDutyCycle(100)
    lm2a.ChangeDutyCycle(75)
    lm2b.ChangeDutyCycle(100)
    rm1a.ChangeDutyCycle(75)
    rm1b.ChangeDutyCycle(100)
    rm2a.ChangeDutyCycle(75)
    rm2b.ChangeDutyCycle(100)
    time.sleep(0.00005)
    
def lft():
    lm1a.ChangeDutyCycle(100)
    lm1b.ChangeDutyCycle(100)
    rm1a.ChangeDutyCycle(100)
    rm1b.ChangeDutyCycle(20)
    lm2a.ChangeDutyCycle(20)
    lm2b.ChangeDutyCycle(100)
    rm2a.ChangeDutyCycle(100)
    rm2b.ChangeDutyCycle(20)
    time.sleep(0.00001)
def slft():
    lm1a.ChangeDutyCycle(100)
    lm1b.ChangeDutyCycle(100)
    rm1a.ChangeDutyCycle(100)
    rm1b.ChangeDutyCycle(35)
    lm2a.ChangeDutyCycle(35)
    lm2b.ChangeDutyCycle(100)
    rm2a.ChangeDutyCycle(100)
    rm2b.ChangeDutyCycle(35)
    time.sleep(0.00001)


def Rlft():
    lm1a.ChangeDutyCycle(0)
    lm1b.ChangeDutyCycle(100)
    lm2a.ChangeDutyCycle(0)
    lm2b.ChangeDutyCycle(100)
    rm1a.ChangeDutyCycle(0)
    rm1b.ChangeDutyCycle(100)
    rm2a.ChangeDutyCycle(0)
    rm2b.ChangeDutyCycle(100)
    time.sleep(0.0008)
    lm1a.ChangeDutyCycle(0)
    lm1b.ChangeDutyCycle(100)
    lm2a.ChangeDutyCycle(0)
    lm2b.ChangeDutyCycle(100)
    rm1a.ChangeDutyCycle(100)
    rm1b.ChangeDutyCycle(0)
    rm2a.ChangeDutyCycle(0)
    rm2b.ChangeDutyCycle(0)
    time.sleep(0.005)
'''
2021-r2
2722-r1
1926-l1
613-l2
'''
def rht():
    
    lm1a.ChangeDutyCycle(100)
    lm1b.ChangeDutyCycle(20)
    rm1a.ChangeDutyCycle(100)
    rm1b.ChangeDutyCycle(100)
    lm2a.ChangeDutyCycle(100)
    lm2b.ChangeDutyCycle(20)
    rm2a.ChangeDutyCycle(20)
    rm2b.ChangeDutyCycle(100)
    time.sleep(0.00001)
def srht():
    
    lm1a.ChangeDutyCycle(100)
    lm1b.ChangeDutyCycle(35)
    rm1a.ChangeDutyCycle(100)
    rm1b.ChangeDutyCycle(100)
    lm2a.ChangeDutyCycle(100)
    lm2b.ChangeDutyCycle(35)
    rm2a.ChangeDutyCycle(35)
    rm2b.ChangeDutyCycle(100)
    time.sleep(0.00001)
    
    


def brk():
    lm1a.ChangeDutyCycle(0)
    lm1b.ChangeDutyCycle(0)
    lm2a.ChangeDutyCycle(0)
    lm2b.ChangeDutyCycle(0)
    rm1a.ChangeDutyCycle(0)
    rm1b.ChangeDutyCycle(0)
    rm2a.ChangeDutyCycle(0)
    rm2b.ChangeDutyCycle(0)
    time.sleep(0.01)

def longbrk():
    lm1a.ChangeDutyCycle(0)
    lm1b.ChangeDutyCycle(0)
    lm2a.ChangeDutyCycle(0)
    lm2b.ChangeDutyCycle(0)
    rm1a.ChangeDutyCycle(0)
    rm1b.ChangeDutyCycle(0)
    rm2a.ChangeDutyCycle(0)
    rm2b.ChangeDutyCycle(0)
    time.sleep(9999)





def main():
    global st1,st2,st3
    global cnt
    
    while True:
        rir=GPIO.input(17)
        mir=GPIO.input(5)
        lir=GPIO.input(18)
        '''
        GPIO.output(12,True)
        time.sleep(0.0001)
        GPIO.output(12,False)
        while GPIO.input(23)==0:
            st1=time.time()
        while GPIO.input(23)==1:
            et1=time.time()
            '''
        
        GPIO.output(12,True)
        time.sleep(0.0001)
        GPIO.output(12,False)
        while GPIO.input(24)==0:
            st2=time.time()
        while GPIO.input(24)==1:
            et2=time.time()
        '''    
        GPIO.output(12,True)
        time.sleep(0.0001)
        GPIO.output(12,False)
        while GPIO.input(25)==0:
            st3=time.time()
        while GPIO.input(25)==1:
            et3=time.time()
            '''
    
        #d1=17150*(et1-st1)
        d2=17150*(et2-st2)
        #d3=17150*(et3-st3)

        time.sleep(0.1)
        
        
    
        if d2<=40:
            brk()
            time.sleep(0.05)
            lft()
            time.sleep(0.5)
            fwd()
            time.sleep(1)
            rht()
            time.sleep(0.8)

            while True:
                
                rir=GPIO.input(17)
                mir=GPIO.input(5)
                lir=GPIO.input(18)
                print('reentering..')
                fwd()
                if rir==1:
                    main()
                    
            brk()
            time.sleep(0.3)

            
                
        else:
            global cnt
            global n
            rir=GPIO.input(17)
            mir=GPIO.input(5)
            lir=GPIO.input(18)
            if lir==1 and rir==1:
                cnt+=1   
                if cnt==1:
                    print('11111111111111111111')
                    fwd()
                    time.sleep(0.28)
                    rht()
                    time.sleep(0.5)
                    while True:
                        rir=GPIO.input(17)
                        mir=GPIO.input(5)
                        lir=GPIO.input(18)
                        if mir==1:
                            break
                        rht()
                elif cnt==2:
                        fwd()
                        time.sleep(0.8)
                        while True:
                            rir=GPIO.input(17)
                            mir=GPIO.input(5)
                            lir=GPIO.input(18)
                            print('reversing')
                            bwd()                            
                            if lir==1 and rir==1:
                                n+=1
                                time.sleep(0.1)
                                print(n)
                                if n==3:   
                                    longbrk() 
               
                fwd()
            elif lir==0 and mir==1 and rir==0:
                fwd()
            elif lir==0 and mir==0 and rir==0:     
                bwd()          
            elif lir==0 and mir==0 and rir==1:
                rht()
            elif lir==1 and mir==0 and rir==0:
                lft()      
            elif lir==1 and mir==1 and rir==0:
                slft()                
            elif lir==0 and mir==1 and rir==1:
                srht()
            


st1=0
st2=0
st3=0
cnt=0
n=0
main()
            


    










