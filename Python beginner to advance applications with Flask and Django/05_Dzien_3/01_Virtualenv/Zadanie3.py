import requests

r = requests.get('https://www.x-kom.pl')

#print(r.content)
#print(r.status_code)
print(r.text)