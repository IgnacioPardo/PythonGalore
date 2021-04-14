from pattern.text.es import parsetree, Text
from parse import parse
import feedparser
import spacy
import csv
from googletrans import Translator
translator = Translator()



Infobae = feedparser.parse("https://www.infobae.com/argentina-rss.xml")
#Clarin = feedparser.parse("https://www.clarin.com/rss/lo-ultimo/")
titulos_clarin = feedparser.parse("https://www.clarin.com/rss/lo-ultimo/").entries + feedparser.parse("https://www.clarin.com/rss/politica/").entries + feedparser.parse("https://www.clarin.com/rss/sociedad/").entries + feedparser.parse("https://www.clarin.com/rss/policiales/").entries + feedparser.parse("https://www.clarin.com/rss/ciudades/").entries + feedparser.parse("https://www.clarin.com/rss/opinion/").entries + feedparser.parse("https://www.clarin.com/rss/cultura/").entries + feedparser.parse("https://www.clarin.com/rss/rural/").entries + feedparser.parse("https://www.clarin.com/rss/economia/").entries + feedparser.parse("https://www.clarin.com/rss/tecnologia/").entries
titulos_infobae = Infobae.entries


traducciones_clarin = translator.translate([t.title for t in titulos_clarin], dest='en')
traducciones_infobae = translator.translate([t.title for t in titulos_infobae], dest='en')


#print([(t.origin, t.text) for t in translations])

nlp = spacy.load('en_vectors_web_lg')

def llWrite(txt, wrti):
	wrti.writerow(txt)
	return txt

f = open('comparisons.csv', 'w')

with f:

	writer = csv.writer(f)

	for tC in traducciones_clarin:
		[llWrite(txt, writer) for txt in [[nlp(tC.text).similarity(nlp(tI.text)), tC.origin, tI.origin] for tI in traducciones_infobae]]

f.close()
#print(len(titulos_clarin), len(titulos_infobae))