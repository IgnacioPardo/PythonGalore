from bs4 import BeautifulSoup

text = 'Para protegerte del coronavirus, hay algunas acciones básicas que te pueden ayudar:\n1.<strong style="color:#f2674a"> Lavate las manos a menudo</strong> con agua y jabón durante al menos 20 segundos</div><div class="divider"></div><center> <div class="emoji" style="font-size: 70px">💧 🧼 👏</div></center>\n2. <strong style="color:#f2674a">Evita tocarte</strong> la cara con las manos sin lavar🚫🤦\n3. #QuedateEnCasa🏠\n4. Al toser o estornudar, <strong style="color:#f2674a">cubrite la boca y la nariz con el codo flexionado🤧💪</strong> y lávate las manos con agua y jabón o con un desinfectante de manos a base de alcohol\nhttps://fpp.org.pe/wp-content/uploads/2019/08/Lavado-de-manos-1200x768.jpg'

import re

print(re.sub(r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))", '', BeautifulSoup(text, 'html.parser').text))
