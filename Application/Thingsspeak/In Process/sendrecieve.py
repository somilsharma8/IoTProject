#!/usr/bin/env python
#__author__ = 'pankaj'
# This program logs a Raspberry Pi's CPU temperature to a Thingspeak Channel
# To use, get a Thingspeak.com account, set up a channel, and capture the Channel Key at https://thingspeak.com/docs/tutorials/ 
# Then paste your channel ID in the code for the value of "key" below.
# Then run as sudo python pitemp.py (access to the CPU temp requires sudo access)
# You can see my channel at https://thingspeak.com/channels/41518

import http.client as httplib
import urllib
import time
sleep = 10 # how many seconds to sleep between posts to the channel
#key = 'Put your Thingspeak Channel Key here'  # Thingspeak channel to update
key = '82849K01N103YE00'

#Report Raspberry Pi internal temperature to Thingspeak Channel
#def thermometer():
#    while True:
        #Calculate CPU temperature of Raspberry Pi in Degrees C
#        temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 # Get Raspberry Pi CPU temp
def dump():
	for i in range(41,50):
		print(int(i))
		#time.sleep(15)
		#print(int(50))



		params = urllib.parse.urlencode({'field1': i, 'key':key }) 
		headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept":"text/plain"}
		conn = httplib.HTTPConnection("api.thingspeak.com:80")
		try:
			time.sleep(15)
			conn.request("POST", "/update", params, headers)
			response = conn.getresponse()
			print(i)
			print([response.status, response.reason])
			data = response.read()
			conn.close()
		except:
			print("connection failed")
		
#sleep for desired amount of time
if __name__ == "__main__":
	dump()
        #time.sleep(sleep)
