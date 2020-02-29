import re,urllib 
import urllib.request
sites="google rediff".split() #sites name
print(sites)
for s in sites: 
	print("Searching...",s)
	u=urllib.request.urlopen("http://"+s+".com")
text=u.read()
title=re.findall("<title>.*</title>",str(text),re.I)
print(title[0])  # return title tag at [0] position