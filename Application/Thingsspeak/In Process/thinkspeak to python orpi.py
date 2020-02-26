'''
#this program uses urllib2, which only works with python2 not python 3
#python3 can be used with urllib3, but then changes have to be made to this code
import urllib2,json
READ_API_KEY='KT1CQ2Q0V9G4JZPN'
CHANNEL_ID=218929
def main():
    conn = urllib2.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s"% (CHANNEL_ID,READ_API_KEY))
    response = conn.read()
    #print "http status code=%s" % (conn.getcode())
    data=json.loads(response)
    print(data['field1'],data['created_at'])
    conn.close()
if __name__ == '__main__':
    main()
'''

#Here's the python3 version of above code:
import urllib3, json

def main():
	http= urllib3.PoolManager()
	response=http.request('GET', "http://api.thingspeak.com/channels/218929/feeds/last.json?api_key='KT1CQ2Q0V9G4JZPN'")
	txt=response.data()
	data=json.load(txt)
	print(data['field1'],data['created_at'])
	
if __name__ == '__main__':
    main()
