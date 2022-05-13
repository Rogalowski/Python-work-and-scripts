import urllib.request

resp = urllib.request.urlopen('https://www.alx.pl')
print(resp.read().decode('utf-8')[:200])


url = 'http://psobolewski.students.alx.pl/tylko_mozilla.php'
#resp = urllib.request.urlopen(url)
#print(resp.read().decode('utf-8'))

req = urllib.request.Request(url, headers={'user-agent': 'Mozilla/4.0 (compatible; MSIE5.5; Windows NT)'})
resp = urllib.request.urlopen(req)
print(resp.read().decode('utf-8')[:200])

####### requests #####

import requests

resp = requests.get("https://alx.pl/nie-ma-takiej-strony")
# print(resp.text)
print(resp.status_code)
# resp.raise_for_status()

resp = requests.get("http://wttr.in/Detroit?format=j1")
weather = resp.json()
print("Aktualna temperatura:", weather['current_condition'][0]['FeelsLikeC'])