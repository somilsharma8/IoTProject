import requests
import time

api="82849K01N103YE00"
def sender():
	for i in range(10,20):
		payload = {'api_key': api, 'field1' : str(i)}
		requests.post("https://api.thingspeak.com/update",payload)
		print("in")
		time.sleep(2)
		print("out")
		
		

sender()

#if __name__ == '__main__':
#	main()

