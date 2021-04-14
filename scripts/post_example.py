import requests
import json

#url = 'https://RAIDNODE.ignaciopardo.repl.co/set/0'
#params = {'somekey': {"a": 124}}

#myobj = {'request':  json.dumps(params) }
#x = requests.post(url, data = myobj)

#print the response text (the content of the requested file):

#print(x.text)


#print(requests.get('https://RAIDNODE.ignaciopardo.repl.co/get/0').text)

url = "https://RAIDHUB.ignaciopardo.repl.co/set"

params = {5: "chona", "pass": "12345" }

myobj = {'request':  json.dumps(params) }
x = requests.post(url, data = myobj)

print(x.text)