import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory, send_file, Response
from werkzeug.utils import secure_filename
import csv
from csv import DictReader
from pprint import pprint
from imdbpie import ImdbFacade
import analize

def analizeFile(outfile):
	dic = {}

	with open('NetflixViewingHistory.csv', newline='') as csvfile:
		reader = DictReader(csvfile)
		for row in reader:
			#Es una serie?
			if row['Title'].count(":") == 2:
				title = row['Title'].split(':')[0]
				date = row['Date']
				if title in dic.keys():
					#Ya me habia aparecido en la lista?
					dic[title][1] += 1
					#dic[title][2].append(date)
				else:
					#Agregala a la lista
					dic[title] = [[], 1]#,[date]]


	imdb = ImdbFacade()

	for tvseries in list(dic.keys()):
		#Por cada serie, me fijo en IMDB cuantas series hay con nombre parecido
		titles = imdb.search_for_title(tvseries)
		#titles es una lista con la cantidad de matches
		if (len(titles)) > 0:
			#Si la lista tiene mas de 0 registros entonces existen registros de esa serie
			for i in range(len(titles)):
				if tvseries.lower() == titles[i].title.lower():
					#Si alguno de los resultados se llama igual que la que esta en mi archivo de netflix
					#Lo guardo en la variable title
					title = imdb.get_title(imdb_id=titles[0].imdb_id)
					#title contiene ahora toda la informacion sobre esta serie
				else:
					if i == len(titles):
						#Si ninguno se llama igual (capaz esta en otro idioma)
						print(tvseries + ' not found. Choose:')
						#Muestro todas las opciones
						pprint([show.title for show in titles])
						#Y pregunto por consola a ver cual es
						index = input('Number:')
						if index == '*':
							#Si tipeo el caracter '*' el titulo el codigo entiende que el titulo no se encontro y pasamos al siguiente
							break
						#Si figura el titulo, lo guardamos en la variable title
						title = imdb.get_title(imdb_id=titles[int(index)].imdb_id)
				break
			#Agregamos a nuestra lista las caracteristicas del titulo que nos interesen
			#imdb_id, title, year, rating, type, release_date, releases, plot_outline, rating_count, writers, directors, creators, genres, credits, certification, image, stars
			dic[tvseries][0] = [title.certification, title.genres, title.year]
			print(tvseries)
			pprint(dic[tvseries])
			

	rows = [[key, dic[key][1], dic[key][0][0], dic[key][0][2]]+list(dic[key][0][1]) for key in dic.keys() if len(dic[key][0]) > 1]
	max_genres = max(map(len, rows))
	first_row = ['Title', 'Ammount', 'Certification', 'Year']+ ['Genre_' + str(i+1) for i in range(max_genres-4)]
	rows.insert(0, first_row)

	import csv

	with open(outfile+".csv", "w", newline="") as f:
	    writer = csv.writer(f)
	    writer.writerows(rows)





UPLOAD_FOLDER = ''
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #os.system('python3 netflix_series.py')
            analize.analizeFile(str(request.form['name']))
            return send_from_directory(directory='', filename=str(request.form['name'])+'.csv', as_attachment=True)
            
    return '''
    <!doctype html>
    <title>Subir Archivo</title>
    <h1>Subir Archivo</h1>
    <form method=post enctype=multipart/form-data>
      <input type=text name="name" placeholder="Nombre">
      <br>
      <input type=file name=file>
      <br>
      <input type=submit value=Subir>
    </form>
    '''