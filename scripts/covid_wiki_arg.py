import requests
from bs4 import BeautifulSoup
import csv
import io


url = "https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data/Argentina_medical_cases_by_province"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

noise = soup.find_all('td', attrs={'style':'padding:0px 2px;'})

for td in noise:
	td.decompose()

noise = soup.find_all('img')
for img in noise:
	img.decompose()
noise = soup.find_all('a')
for a in noise:
	a.decompose()

table = soup.find("table", class_="wikitable")
trs = table.find_all('tr', class_="")

html_table = '<table><tbody>'
for tr in trs:
	html_table += str(tr)
html_table += '</tbody></table>'
html_table.replace('<b>24</b>', '<b>Argentina</b>')

soup = BeautifulSoup(html_table, 'html.parser')
indexes = ['Provincia', 'Casos', 'Muertes', 'Recuperados',	'Poblacion', 'CasosSobre100k']
resultados = []
for table_num, table in enumerate(soup.find_all('table')):
	for tr in table.find_all('tr'):
		row = [''.join(cell.stripped_strings) for cell in tr.find_all(['td', 'th'])]
		resultados.append(row[1:])
resultados[1] = ['Argentina'] + resultados[1]

data = {}

for row in resultados:
	prov = row[0]

	data[prov] = {
					indexes[1]: row[1],
					indexes[2]: row[2],
					indexes[3]: row[3],
					indexes[4]: row[4],
					indexes[5]: row[5]
				}
