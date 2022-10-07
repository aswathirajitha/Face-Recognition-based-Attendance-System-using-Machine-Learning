import urllib,json
import urllib.request

baseURL = 'https://api.thingspeak.com/update?api_key=X85HZ2NEYA5L19LI&field1='
#b="temp=32"
    

b='new'


urllib.request.urlopen(baseURL +str(b))
	

	
print ("Program has ended")