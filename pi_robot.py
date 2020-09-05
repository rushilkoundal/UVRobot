# import curses and GPIO
import curses
import time
import motorController
import RPi.GPIO as GPIO
import RFIDScanner
import servo
import os
from espeak import espeak
from subprocess import Popen, PIPE, STDOUT#set GPIO numbering mode and define output pins

Authorization_PIN = 5
MotionDetection_PIN = 6
Heatwarning_PIN = 13
UVLamp_PIN =19
#BCM Mode
GPIO.setmode(GPIO.BCM)

GPIO.setup(UVLamp_PIN,GPIO.OUT)
GPIO.setup(Authorization_PIN,GPIO.IN)
GPIO.setup(MotionDetection_PIN,GPIO.IN)
GPIO.setup(Heatwarning_PIN,GPIO.IN)
os.system(' espeak -ven+f3  --stdout "hello World , I am U V robot to disinfect Corona Virus. Please swipe your card for access" | aplay') 

#espeak -s80 "Hello Deepesh" 2>/dev/null --stdout|aplay
# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
motorController.motorAction("STOPALL")
screen.keypad(True)
id=RFIDScanner.read_rfid()
id=0
print (id)
os.system(' espeak -ven+f4 --stdout "Access Granted" | aplay') 
time.sleep(2)
last_time = time.time()
try:
        while (id==0):           
            
            print('before screen')
            char = screen.getch()
            print(char)
            if char == ord('q'):
                break
            elif char == curses.KEY_UP:               
                print("STRAIGHT")
                #motorController.motorAction("STRAIGHT")
                motorController.motorAction("FORWARD")
                #char = 's'
                
            elif char == curses.KEY_DOWN:
                print("down")
                #motorController.motorAction("STRAIGHT")              
                motorController.motorAction("BACKWARD")
                char = 's'
                
            elif char == curses.KEY_RIGHT:
                print("RIGHT")
                motorController.motorAction("RIGHT")
                char = 'f'
                
                
            elif char == curses.KEY_LEFT:
                print("LEFT")
                motorController.motorAction("LEFT")
                char = 'f'
                
                
            elif char == 10: #enter key
                print("STOPALL")
                motorController.motorAction("STOPALL")
                
            elif char == 32: # space bar key
                print("STOPSTEERING")
                motorController.motorAction("STOPSTEERING")
            
            elif char == 111: # o key open
                print("Opening chamber")
                servo.servoMotorAction("OPEN")
                
            elif char == 99: # c key oclose
                print("Closing chamber")
                servo.servoMotorAction("CLOSE")
                
                
            elif char:
                motorController.motorAction("STOPALL")

            print('char')
            print(char)
            
                        
             
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    motorController.motorAction("STOPALL")

    curses.endwin()
    GPIO.cleanup()
    
