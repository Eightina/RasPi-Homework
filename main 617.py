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
lm1a = GPIO.PWM(19, 1000)
lm1b = GPIO.PWM(26, 1000)
lm2a = GPIO.PWM(6, 1000)
lm2b = GPIO.PWM(13, 1000)
rm1a = GPIO.PWM(27, 1000)
rm1b = GPIO.PWM(22, 1000)
rm2a = GPIO.PWM(20, 1000)
rm2b = GPIO.PWM(21, 1000)
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
    lm1b.ChangeDutyCycle(0)
    lm2a.ChangeDutyCycle(100)
    lm2b.ChangeDutyCycle(0)
    rm1a.ChangeDutyCycle(100)
    rm1b.ChangeDutyCycle(0)
    rm2a.ChangeDutyCycle(100)
    rm2b.ChangeDutyCycle(0)
    time.sleep(0.0005)  
    lm1a.ChangeDutyCycle(100)
    lm1b.ChangeDutyCycle(35)
    lm2a.ChangeDutyCycle(100)
    lm2b.ChangeDutyCycle(35)
    rm1a.ChangeDutyCycle(100)
    rm1b.ChangeDutyCycle(35)
    rm2a.ChangeDutyCycle(100)
    rm2b.ChangeDutyCycle(35)
    time.sleep(0.0005)

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
    lm1a.ChangeDutyCycle(0)
    lm1b.ChangeDutyCycle(100)
    lm2a.ChangeDutyCycle(0)
    lm2b.ChangeDutyCycle(100)
    rm1a.ChangeDutyCycle(0)
    rm1b.ChangeDutyCycle(100)
    rm2a.ChangeDutyCycle(0)
    rm2b.ChangeDutyCycle(100)
    time.sleep(0.05)

def Rbwd():
    lm1a.ChangeDutyCycle(0)
    lm1b.ChangeDutyCycle(100)
    lm2a.ChangeDutyCycle(0)
    lm2b.ChangeDutyCycle(100)
    rm1a.ChangeDutyCycle(0)
    rm1b.ChangeDutyCycle(100)
    rm2a.ChangeDutyCycle(0)
    rm2b.ChangeDutyCycle(100)
    time.sleep(0.0005)
    lm1a.ChangeDutyCycle(35)
    lm1b.ChangeDutyCycle(100)
    lm2a.ChangeDutyCycle(35)
    lm2b.ChangeDutyCycle(100)
    rm1a.ChangeDutyCycle(35)
    rm1b.ChangeDutyCycle(100)
    rm2a.ChangeDutyCycle(35)
    rm2b.ChangeDutyCycle(100)
    time.sleep(0.0005)
    
def lft():
    lm1a.ChangeDutyCycle(100)
    lm1b.ChangeDutyCycle(0)
    lm2a.ChangeDutyCycle(100)
    lm2b.ChangeDutyCycle(0)
    rm1a.ChangeDutyCycle(100)
    rm1b.ChangeDutyCycle(0)
    rm2a.ChangeDutyCycle(100)
    rm2b.ChangeDutyCycle(0)
    time.sleep(0.003)
    lm1a.ChangeDutyCycle(0)
    lm1b.ChangeDutyCycle(0)
    rm1a.ChangeDutyCycle(100)
    rm1b.ChangeDutyCycle(0)
    lm2a.ChangeDutyCycle(0)
    lm2b.ChangeDutyCycle(100)
    rm2a.ChangeDutyCycle(100)
    rm2b.ChangeDutyCycle(0)
    time.sleep(0.005)
       
def Rlft():
    lm1a.ChangeDutyCycle(0)
    lm1b.ChangeDutyCycle(100)
    lm2a.ChangeDutyCycle(0)
    lm2b.ChangeDutyCycle(100)
    rm1a.ChangeDutyCycle(0)
    rm1b.ChangeDutyCycle(100)
    rm2a.ChangeDutyCycle(0)
    rm2b.ChangeDutyCycle(100)
    time.sleep(0.003)
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
    lm1b.ChangeDutyCycle(0)
    lm2a.ChangeDutyCycle(100)
    lm2b.ChangeDutyCycle(0)
    rm1a.ChangeDutyCycle(100)
    rm1b.ChangeDutyCycle(0)
    rm2a.ChangeDutyCycle(100)
    rm2b.ChangeDutyCycle(0)
    time.sleep(0.003)
    lm1a.ChangeDutyCycle(100)
    lm1b.ChangeDutyCycle(0)
    rm1a.ChangeDutyCycle(0)
    rm1b.ChangeDutyCycle(0)
    lm2a.ChangeDutyCycle(100)
    lm2b.ChangeDutyCycle(0)
    rm2a.ChangeDutyCycle(0)
    rm2b.ChangeDutyCycle(100)
    time.sleep(0.005)
    
def Rrht():
    lm1a.ChangeDutyCycle(0)
    lm1b.ChangeDutyCycle(100)
    lm2a.ChangeDutyCycle(0)
    lm2b.ChangeDutyCycle(100)
    rm1a.ChangeDutyCycle(0)
    rm1b.ChangeDutyCycle(100)
    rm2a.ChangeDutyCycle(0)
    rm2b.ChangeDutyCycle(100)
    time.sleep(0.003)
    lm1a.ChangeDutyCycle(100)
    lm1b.ChangeDutyCycle(0)
    lm2a.ChangeDutyCycle(0)
    lm2b.ChangeDutyCycle(0)
    rm1a.ChangeDutyCycle(0)
    rm1b.ChangeDutyCycle(100)
    rm2a.ChangeDutyCycle(0)
    rm2b.ChangeDutyCycle(100)
    time.sleep(0.005)

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

def fololin():
    global cnt
    global n
    rir=GPIO.input(17)
    mir=GPIO.input(5)
    lir=GPIO.input(18)
    print(lir,mir,rir)
    if lir==0 and mir==1 and rir==0:
        fwd()
        n=0
    elif lir==0 and mir==0 and rir==0:     
        bwd()          
    elif lir==0 and mir==0 and rir==1:
        rht()
        n=0  
    elif lir==1 and mir==0 and rir==0:
        lft()
        n=0
    elif lir==1 and mir==1 and rir==0:
        lft()
        n=0
    elif lir==0 and mir==1 and rir==1:
        rht()
        n=0
    elif lir==1 and rir==1:
        print('detected!')
        cnt+=1
        if cnt==2:
            brk()
            bwd()
            time.sleep(0.5)
            reverse()
            
        elif cnt==4:
            brk()
            while True:
                rir=GPIO.input(17)
                mir=GPIO.input(5)
                lir=GPIO.input(18)
                bwd()
                if (mir==1 and rir==1)or(rir==1 and mir==1):
                    longbrk() 
        time.sleep(0.2)
        fwd()
       

def Rfololin():
    global cnt
    global n
    rir=GPIO.input(17)
    mir=GPIO.input(5)
    lir=GPIO.input(18)
    print('r',lir,mir,rir)
    if lir==0 and mir==1 and rir==0:
        Rbwd()
        n=0
    elif lir==0 and mir==0 and rir==0:      
        Rfwd()          
    elif lir==0 and mir==0 and rir==1:
        Rrht()
        n=0  
    elif lir==1 and mir==0 and rir==0:
        Rlft()
        n=0
    elif lir==1 and mir==1 and rir==0:
        Rlft()
        n=0
    elif lir==0 and mir==1 and rir==1:
        Rrht()
        n=0
    elif lir==1 and rir==1:
        print('detected!')
        cnt+=1
        brk()
       




def reverse():
    global cnt
    global n
    print('reversing')
    while True:
        Rfololin()
        if lir==1 and rir==1:
            lm1a.ChangeDutyCycle(100)
            lm1b.ChangeDutyCycle(0)
            rm1a.ChangeDutyCycle(0)
            rm1b.ChangeDutyCycle(0)
            lm2a.ChangeDutyCycle(100)
            lm2b.ChangeDutyCycle(0)
            rm2a.ChangeDutyCycle(0)
            rm2b.ChangeDutyCycle(100)
            time.sleep(0.5)
            break
    while True:
        rir=GPIO.input(17)
        mir=GPIO.input(5)
        lir=GPIO.input(18)
        rht()
        print(lir,mir,rir)
        if  mir==1:
            break


def mainfolo():
    global cnt
    while True:
        fololin()
    while True:
        rir=GPIO.input(17)
        mir=GPIO.input(5)
        lir=GPIO.input(18)
        print(lir,mir,rir)
        bwd()
        if lir==1 and rir==1:
            print('detected!')
            cnt+=1
            if cnt==6:
                break
            time.sleep(0.5)
    longbrk()    

def main():
    while True:
        
        rir=GPIO.input(17)
        mir=GPIO.input(5)
        lir=GPIO.input(18)
        '''
        GPIO.output(12,True)
        time.sleep(0.00001)
        GPIO.output(12,False)
        while GPIO.input(23)==0:
            st1=time.time()
        while GPIO.input(23)==1:
            et1=time.time()
        '''
        

        
        
        GPIO.output(12,True)
        time.sleep(0.00001)
        GPIO.output(12,False)
        while GPIO.input(24)==0:
            st2=time.time()
        while GPIO.input(24)==1:
            et2=time.time()
            
        '''    
        GPIO.output(12,True)
        time.sleep(0.00001)
        GPIO.output(12,False)
        while GPIO.input(25)==0:
            st3=time.time()
        while GPIO.input(25)==1:
            et3=time.time()
        '''
    
        #d1=17150*(et1-st1)
        d2=17150*(et2-st2)
        #d3=17150*(et3-st3)
    
        if d2<=35:
            brk()
            lft()
            time.sleep(1.5)
            fwd()
            time.sleep(2)
            rht()
            time.sleep(2)
            while True:
                fwd()
                if mir==1:
                    break
        '''
        elif d2<=15 and d3<=15:
            brk()
            rht()
            time.sleep(2)
            fwd()
            time.sleep(2)
            lft()
            time.sleep(3.5)
            while True:
                fwd()
                if mir==1:
                    break
        '''
            
        else:
            global cnt
            global n
            rir=GPIO.input(17)
            mir=GPIO.input(5)
            lir=GPIO.input(18)
            print(lir,mir,rir)
            if lir==0 and mir==1 and rir==0:
                fwd()
                n=0
            elif lir==0 and mir==0 and rir==0:     
                bwd()          
            elif lir==0 and mir==0 and rir==1:
                rht()
                n=0  
            elif lir==1 and mir==0 and rir==0:
                lft()
                n=0
            elif lir==1 and mir==1 and rir==0:
                lft()
                n=0
            elif lir==0 and mir==1 and rir==1:
                rht()
                n=0
            elif lir==1 and rir==1:
                print('detected!')
                cnt+=1
                if cnt==2:
                    brk()
                    bwd()
                    time.sleep(0.5)
                    reverse()
                    continue
                elif cnt==4:
                    brk()
                    while True:
                        rir=GPIO.input(17)
                        mir=GPIO.input(5)
                        lir=GPIO.input(18)
                        bwd()
                        if (mir==1 and rir==1)or(rir==1 and mir==1):
                            longbrk() 
                time.sleep(0.2)
                fwd()
       

        
cnt=0
n=0
main()
            


    










