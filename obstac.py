import RPi.GPIO as R
import time
R.setwarnings(False)
R.setmode(R.BOARD)
R.setup(3,R.IN)
R.setup(5,R.IN)
R.setup(8,R.OUT)
R.setup(10,R.OUT)
R.setup(7,R.OUT)
R.setup(12,R.OUT)
R.setup(11,R.IN)
h=0
l=1
while 1:
    ir1=R.input(3)
    ir2=R.input(5)
    ir3=R.input(11)
    print ('i1: ',ir1,'i2: ',ir2,'i3: ',ir3)
    time.sleep(1)
    if(ir1==0 and ir2==1 and ir3==0):
#making the car to move forward
        R.output(8,h)
        R.output(10,l)
        R.output(7,h)
        R.output(12,l)
    elif(ir1==1 and ir2==1 and ir3==0):
#to reverse the left motor
        R.output(8,l)
        R.output(10,h)
        R.output(7,l)
        R.output(12,h)
            
        time.sleep(1)
        R.output(8,l)
        R.output(10,h)
        R.output(7,l)
        R.output(12,h)

        R.output(8,h)
        R.output(10,l)
        R.output(7,l)
        R.output(12,l)
    elif(ir1==0 and ir2==1 and ir3==1):
#to reverse the right motor
        R.output(8,l)
        R.output(10,h)
        R.output(7,l)
        R.output(12,h)
            
        time.sleep(1)
        R.output(8,l)
        R.output(10,h)
        R.output(7,l)
        R.output(12,h)

        R.output(8,l)
        R.output(10,l)
        R.output(7,h)
        R.output(12,l)
#stop motor
    elif(ir1==0 and ir2==0 and ir3==0):
        R.output(8,l)
        R.output(10,l)
        R.output(7,l)
        R.output(12,l)
        

                
#to full stop the car
    elif(ir1==1 and ir2==1 and ir3==1):
        R.output(8,l)
        R.output(10,l)
        R.output(7,l)
        R.output(12,l)
