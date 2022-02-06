import urllib.request
from time import time, sleep

for i in range(1, 100):
	i = i+1	
	s = urllib.request.urlopen("https://api.thingspeak.com/update?api_key=LELS9WKJXMZ7PMKD&field1=0"+str(i))
	s = s.read()
	print(i)
	sleep(10)
