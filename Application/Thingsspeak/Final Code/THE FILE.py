
import RPi.GPIO as GPIO
import requests
import test13
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
#GPIO.setup(3, GPIO.OUT)         #LED output pin
api="82849K01N103YE00"
while True:
       i=GPIO.input(11)
       payload = {'api_key': api, 'field1' : str(i)}
       requests.post("https://api.thingspeak.com/update",payload)
       if i==0:                 #When output from motion sensor is LOW
             print "No intruders",i
             #GPIO.output(3, 0)  #Turn OFF LED
             time.sleep(0.1)
       elif i==1:               #When output from motion sensor is HIGH
             print "Intruder detected",i
             #GPIO.output(3, 1)  #Turn ON LED
             test13.run()                                                                         
             time.sleep(0.1)
