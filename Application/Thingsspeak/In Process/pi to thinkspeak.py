import requests
import time

api="82849K01N103YE00"
def sender():
		payload = {'api_key': api, 'field1' : str(10)}
		
   		requests.post("https://api.thingspeak.com/update"+payload)
		
		for x in range(3):
			print(x)

sender()

if __name__ == '__main__':
	main()

