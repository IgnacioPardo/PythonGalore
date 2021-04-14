import requests
from bs4 import BeautifulSoup

def covidHoy(prov=None):
	url = "https://www.google.com/search?sxsrf=ALeKk015GHbvnmtTxCU5GgP7gYBNe5d3Mw%3A1594126137498&ei=OW8EX435HeGz5OUP-q6E4A8&q=casos+de+covid+hoy+san+juan&oq=casos+de+covid+hoy+san+juan&gs_lcp=CgZwc3ktYWIQAzIGCAAQFhAeOgQIIxAnOgcIABAUEIcCOgIIADoFCCEQoAFQgm5YvnZgtXhoAHAAeACAAY8BiAG_CJIBAzEuOJgBAKABAaoBB2d3cy13aXo&sclient=psy-ab&ved=0ahUKEwjN-ZvRlrvqAhXhGbkGHXoXAfwQ4dUDCAw&uact=5"

	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')

	table = soup.find_all("table", class_="qyEGdc")
	table = list(set(table))
	results = {'world':{}, 'arg':{}, 'prov':{}}
	order = ['prov', 'arg', 'world']
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
			results[order[i]][contenido] = cantidad
		i+=1
	return str(results)

url = "https://www.google.com/search?sxsrf=ALeKk015GHbvnmtTxCU5GgP7gYBNe5d3Mw%3A1594126137498&ei=OW8EX435HeGz5OUP-q6E4A8&q=casos+de+covid+hoy+san+juan&oq=casos+de+covid+hoy+san+juan&gs_lcp=CgZwc3ktYWIQAzIGCAAQFhAeOgQIIxAnOgcIABAUEIcCOgIIADoFCCEQoAFQgm5YvnZgtXhoAHAAeACAAY8BiAG_CJIBAzEuOJgBAKABAaoBB2d3cy13aXo&sclient=psy-ab&ved=0ahUKEwjN-ZvRlrvqAhXhGbkGHXoXAfwQ4dUDCAw&uact=5"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)

#print(covidHoy())