from requests_html import HTMLSession
import pyppdf.patch_pyppeteer
from bs4 import BeautifulSoup


def covidHoy(prov=None):
	url = 'https://www.google.com/search?q=casos+de+covid+hoy'
	session = HTMLSession()
	resp = session.get(url)
	resp.html.render()
	html = resp.html.html
	soup = BeautifulSoup(html, 'html.parser')

	table = soup.find_all("table", class_="qyEGdc")
	table = list(set(table))
	world = {}
	arg = {}
	prov = {}
	results = [world, arg, prov]
	i = 0
	from pprint import pprint
	for t in table:
		tds = t.find_all("td")
		for td in tds:
			div =  td.find("div", class_="amyZLb")
			span = td.find("span")
			contenido = div.text
			cantidad = span.text

			if "\\" in contenido:
				contenido = contenido.split("\\")[0]
			if "\\" in cantidad:
				cantidad = cantidad.replace("\\xa0", " ")
			results[i][contenido] = cantidad
		i+=1
	return results