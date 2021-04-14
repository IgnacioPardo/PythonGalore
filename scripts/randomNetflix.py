import requests
from bs4 import BeautifulSoup
from random import choice


def random_netflix():
	url = 'https://www.ennetflix.com.ar/tipo/programa'
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	titles = soup.findAll("div", class_="mtitle")
	from pprint import pprint

	content = []

	for title in titles:
		try:
			content.append(title.find('a').text)
		except:
			pass
	chosen = choice(content)

	ases = soup.find("a", {"title" : chosen})

	image = 'https://www.ennetflix.com.ar' + ases.find('img')['src']

	return chosen, image


apis = {'netflix' : random_netflix}

print(apis['netflix']())