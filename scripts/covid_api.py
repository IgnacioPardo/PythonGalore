from requests_html import HTMLSession
import pyppdf.patch_pyppeteer
from bs4 import BeautifulSoup

url = 'https://www.google.com/search?q=casos+de+covid+hoy'

url = "https://www.google.com/search?rlz=1C1DIMC_enAR838AR838&sxsrf=ALeKk03ADS8twe8zifGyV3S0eaiY0G0fsQ%3A1594073482502&ei=iqEDX7CbHsKG0AbIir-oDA&q=casos+de+covid+hoy+argentina&oq=casos+de+covid+hoy+argentina&gs_lcp=CgZwc3ktYWIQAzIFCAAQywEyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeOgoIABCxAxCDARBDOggIABCxAxCDAToCCAA6BAgAEEM6DQgAELEDEIMBEBQQhwI6BwgAEBQQhwJQ_7TQAVjfv9ABYMXB0AFoAHAAeACAAdwBiAHvCpIBBTIuOC4xmAEAoAEBqgEHZ3dzLXdpeg&sclient=psy-ab&ved=0ahUKEwiwiK690rnqAhVCA9QKHUjFD8UQ4dUDCAw&uact=5"

session = HTMLSession()


resp = session.get(url)
resp.html.render()
html = resp.html.html

soup = BeautifulSoup(html, 'html.parser')

#div = soup.find("div", class_="wsV78c")

#print(div)

div = soup.find("div", class_="o6Yscf").parent

svg = div.find("svg")

for a in svg:
	deleted = a.extract()


from pprint import pprint
pprint(div)