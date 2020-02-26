from urllib import request
from json import *
READ_API_KEY='KT1CQ2Q0V9G4JZPN'
CHANNEL_ID=218929
conn = request.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s"% (CHANNEL_ID,READ_API_KEY))

def main():
        try:
                conn = request.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s"% (CHANNEL_ID,READ_API_KEY))
                response = conn.read()
                data=json.loads(response)
                print(data['field1'],data['created_at'])
                conn.close()
                #conn.request("POST", "/update", params, headers)
                #response = conn.getresponse()
                #print temp
                #print response.status, response.reason
                #data = response.read()
                #conn.close()
        except:
                print("connection failed")
                #break
#print "http status code=%s" % (conn.getcode())
    
if __name__ == '__main__':
        main()
