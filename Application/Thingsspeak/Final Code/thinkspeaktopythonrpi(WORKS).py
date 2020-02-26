from urllib import request
import json
READ_API_KEY='KT1CQ2Q0V9G4JZPN'
CHANNEL_ID=218929
FIELD_ID=1
conn = request.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.txt"% (CHANNEL_ID))
print(conn)
print("It worked")
def main():
        conn = request.urlopen("http://api.thingspeak.com/channels/%s/fields/%s/last.txt"% (CHANNEL_ID, FIELD_ID))
        response = conn.read().decode('utf 8')
        #data=json.loads(response)
        #print(data['field1'],data['created_at'])
        print(response)
        conn.close()
                #conn.request("POST", "/update", params, headers)
                #response = conn.getresponse()
                #print temp
                #print response.status, response.reason
                #data = response.read()
                #conn.close()
'''
        except:
                print("connection failed")
                #break
'''
#print "http status code=%s" % (conn.getcode())
    
if __name__ == '__main__':
        main()
