import qrcode
import sys
import zlib
import os
# Create qr code instance
qr = qrcode.QRCode(
    version = None,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border = 4,
)

# The data that you want to store
#data = input('Ingresar Texto:')
data = "Ragoût D'escargots à L'émulsion D'herbes Fraîches,14.0\nJambon Persillé Du Morvan Et Oignons Confits Aux Condiments,14.0\nCannelons De Langoustines, Concombres Farcis Aux Choux Fleurs, Bisque De Crustacés,14.0\nMosaïque De Chèvre Frais à L'artichaut Et Aux Aubergines, Vinaigrette De Quinoa Aux Appétits (Saveur Légère),14.0\nPressé De Tomate Au Crabe, à L'avocat Et Pomme Verte, Salade De Betteraves 'Shoggia',14.0\nFilet De Dorade Vapeur, Tian De Légumes Provençal, émulsion De Lait Végétal Au Thé D'agrumes (Saveur Légère),28.0\nBar Rôti à La Farigoulette Et Spaghettis De Courgettes Au Thym En Feuilletté,28.0\nCroustillant De Caille Au Foie Gras, Oignon Farci Au Chou Et Piments Doux,28.0\nFilet De Canette Rôtie Aux épices Douces, Bayaldi De Courgettes Et Aubergines, Frites De Polenta,28.0\nPanaché De Quasi Et De Ris De Veau, Aux Blettes Et Artichauts Poivrades,35.0\nAmandine, Compotée De Fruits Rouge, Sorbet Serpolet Et Citron,10.0\nMoelleux Au 'Cœur De Chocolat Guanaja' Glace Vanille,10.0\nMousse De Calisson En Millefeuille, Sorbet Verveine,10.0\nTarte Brisée à La Rhubarbe, Sorbet Fraises Des Bois,10.0\nVacherin à L'abricot, Jus Acidulé Au Romarin,10.0\nMousse De Haddock, Vierge D'agrumes,17.0\nThon Rôti, Risotto D'épeautres,28.0\nFaux Filet De Charolais, Cromesquis De Queue De Bœuf, Mitonnée De Pois Gourmands, Douceur De Brocolis,35.0\nMillefeuille Aux Mirabelles, Glace Pistache,10.0\nSaint Bris,4.5\nPouilly Fuissé,9.0\nPuligny Montrachet '1er Cru',12.0\nMercurey 'Clos De Touches',6.0\nSantenay '1er Cru Gravières',8.0\nLa Parde De Haut Bailly,9.0"
print(sys.getsizeof(data))

def comp(data):
	return zlib.compress(data.encode())

def decomp(data):
	return zlib.decompress(data).decode()

cData = comp(data)
print(sys.getsizeof(cData))

dData = decomp(cData)
print(sys.getsizeof(dData))


# Add data
qr.add_data(cData)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image()

# Save it somewhere, change the extension as needed:
# img.save('image.png')
# img.save('image.bmp')
# img.save('image.jpeg')
img.save('image.jpg')
os.system('open image.jpg')