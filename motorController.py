import RPi.GPIO as GPIO
import time


DC_MOTOR_1 = 24
DC_MOTOR_2 = 25

#BCM Mode
GPIO.setmode(GPIO.BCM)
#motor driver output pins
GPIO.setup(DC_MOTOR_1,GPIO.OUT)
GPIO.setup(DC_MOTOR_2,GPIO.OUT)

motorRight = GPIO.PWM(DC_MOTOR_1, 20000)
motorLeft = GPIO.PWM(DC_MOTOR_2, 20000)

motorRight.start(50)
motorLeft.start(50)

ForwardDirection=100
BackwardDirection=0
StopCommand=50

def motorAction(action):
    if action == "FORWARD":
        print("FORWARD")
        #time.sleep(0.1)
        motorRight.ChangeDutyCycle(ForwardDirection)
        motorLeft.ChangeDutyCycle(ForwardDirection)           
    
    elif action == "BACKWARD":
          print("BACKWARD")
          motorRight.ChangeDutyCycle(BackwardDirection)
          motorLeft.ChangeDutyCycle(BackwardDirection)   
          
    elif action == "LEFT":
          print("LEFT")
          #time.sleep(0.1)
          motorRight.ChangeDutyCycle(BackwardDirection)
          motorLeft.ChangeDutyCycle(ForwardDirection)           
           
          
    elif action == "RIGHT":
          print("RIGHT")
          #time.sleep(0.1)
          motorRight.ChangeDutyCycle(ForwardDirection)
          motorLeft.ChangeDutyCycle(BackwardDirection)           
 

    elif action == "STRAIGHT":
          print("STRAIGHT")
         
    elif action == "STOPDRIVE":
          print("STOPDRIVE")          
         
          
    elif action == "STOPALL":
          print("STOPALL")
          motorRight.ChangeDutyCycle(StopCommand)
          motorLeft.ChangeDutyCycle(StopCommand)           
 
          
    elif action == "STOPSTEERING":
          print("STOPSTEERING")          
          
          

        
        
   
        
        
