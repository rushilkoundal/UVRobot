import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)

p = GPIO.PWM(18, 50)

p.start(2.5)

def servoMotorAction(action):
    if action == "OPEN":
        print("OPEN")
        time.sleep(0.1)
        p.ChangeDutyCycle(2.5)  # turn towards 0 degree
        time.sleep(0.25) # sleep 1 second
        p.ChangeDutyCycle(7.5)  # turn towards 90 degree
        time.sleep(0.25) # sleep 1 second
        p.ChangeDutyCycle(12.5) # turn towards 180 degree
        time.sleep(0.25) # sleep 1 second
        #p.stop()
        #GPIO.cleanup()
        
    
    elif action == "CLOSE":
          print("CLOSE action")
          time.sleep(0.1)
          p.ChangeDutyCycle(12.5)  # turn towards 180 degree
          time.sleep(0.25) # sleep 1 second
          p.ChangeDutyCycle(7.5)  # turn towards 90 degree
          time.sleep(0.25) # sleep 1 second
          p.ChangeDutyCycle(2.5) # turn towards 0 degree
          time.sleep(0.25) # sleep 1 second
          #p.stop()
          #GPIO.cleanup()

   