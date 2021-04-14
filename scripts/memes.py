from random import choice
import json
import requests

animalsImages = ['dog', 'cat', 'panda', 'red_panda', 'birb', 'fox', 'koala']
r = requests.get("https://some-random-api.ml/img/" + choice(animalsImages))
r = r.json()
print(r["link"])