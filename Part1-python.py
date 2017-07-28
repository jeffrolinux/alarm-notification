import time
import RPi.GPIO as io
import subprocess

#this set GPIO to use pin number instead of GPIO number
io.setmode(io.BCM)

#enter number for pin using
door_pin = 23

io.setup(door_pin, io.IN, pull_up_down=io.PUD_UP)  #active input with pullup

#initialize door
door=0

while True:
        if (io.input(door_pin)==True and door!=2):
            print ("The window and or circuit is open")
            door=2
            subprocess.call("./mailer", shell=True)
            #time.sleep(30)
        if (io.input(door_pin)==False and door!=1):
            print ("The window and or circuit is once again closed")
            door=1
            #time.sleep(30)
#I went with door instead of sleep so interation would run once until door variable changed            
