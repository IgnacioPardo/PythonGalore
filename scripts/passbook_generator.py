import requests
from bs4 import BeautifulSoup

url = "https://www.passsource.com/pass/register.php?templateId=3"

payload = {'psForm_0_structure_primaryFields_event_value': 'Recorrido de Museos',
'psForm_0_structure_secondaryFields_loc_value': 'Recoleta',
'psForm_0_barcode_altText': 'Recorrido de Museos por Recoleta',
'psForm_0_barcode_format': 'PKBarcodeFormatQR',
'psForm_0_barcode_message': '123456',
'psForm_0_submit': 'Register',
'psForm': '0'}
files = [
  ('background', None),
  ('background@2x', None),
  ('thumbnail', None),
  ('thumbnail@2x', None)
]
headers = {
  'Cookie': '__cfduid=d235b3bbf4efd1762c68cc467326594ce1597786713; PHPSESSID=df85d94d95b3bb967de4675f52a445bc'
}

page = requests.request("POST", url, headers=headers, data = payload, files = files)

#print(page.text.encode('utf8'))

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.find('p', class_="downloadButton").find('a')['href'])