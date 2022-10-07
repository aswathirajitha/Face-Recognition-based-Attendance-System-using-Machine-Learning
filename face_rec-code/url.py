import urllib,json
import urllib.request

def thin(data):
    baseURL='https://api.thingspeak.com/update?api_key=X85HZ2NEYA5L19LI&field1='
    b=data
    urllib.request.urlopen(baseURL+str(b))
	#print("Program has ended")