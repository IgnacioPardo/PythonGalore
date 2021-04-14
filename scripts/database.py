import os, psutil, pickle, codecs

class DB():

	db_loc = ""
	ram_size = 500 * 1024
	disk_size = 500 * 1024
	defaults = {}
	data = {}

	def __init__(self, loc, defaults={}):
		self.db_loc = loc
		self.defaults = defaults
		if os.path.isfile(loc):
			self.data = self.l_db()
		else:
			f = open(loc, "w")
			f.close()
			self.u_db(db={"main_db":{}, "defaults":self.defaults})

	def __str__(self):
		return str(self.l_db())

	def size_to_str(self):
		return str(os.stat(self.db_loc).st_size / 1024) + ' KB | ' + str(len(self.l_db())) + ' keys'

	def db_size(self):
		return os.stat(self.db_loc).st_size / 1024

	def keys_size(self):
		return len(self.l_db())

	def clear(self):
		self.u_db(db={"main_db":{}, "defaults":self.defaults})

	def l_db(self):
		pk = pickle.load(open(self.db_loc, 'rb'))
		self.data = pk["main_db"]
		self.defaults = pk["defaults"]
		return self.data

	def u_db(self, db=None):
		pickle.dump(db if db else {"main_db":self.data, "defaults":self.defaults}, open(self.db_loc, 'wb'))

	def ram_usage(self):
		process = psutil.Process(os.getpid())
		return process.memory_info().rss / 1024

	def disk_usage(self):
		disk = 0
		start_path = '.'
		for path, dirs, files in os.walk(start_path):
			for f in files:
				fp = os.path.join(path, f)
				disk += os.path.getsize(fp)
		return disk / 1024

	def ram_usage_p(self):
		return self.ram_usage() / self.ram_size

	def disk_usage_p(self):
		return self.disk_usage() / self.disk_size

	def db_disk_p(self):
		return self.db_size() / self.disk_size

	def html_circle(self, size, big='', color=''):
		return '<div class="dark '+big+' '+color+' c100 pPSIZE center"><span>PSIZE%</span><div class="slice"><div class="bar"></div><div class="fill"></div></div></div>'.replace('PSIZE', str(size)[:5])

	def html_stats(self, mobile):
		s = codecs.open('web/stats_header.html', 'r', 'utf-8').read()
		if mobile:
			return s + '<center><br><br><table style=" width:75%;margin-top:10%;"><tr>RAM</tr><tr>'+self.html_circle(self.ram_usage_p()*100)+'</tr><br><tr>DISK</tr><tr>'+self.html_.circle(self.disk_usage_p()*100, 'green')+'</tr><br><tr>DB: '+str(len(self.l_db())) + ' keys'+'</tr><tr>'+self.html_.circle(self.db_disk_p()*100, 'orange')+'</tr></table></center>'
		else:
			return s + '<center><table style=" width:75%;margin-top:10%;"><tr><th>RAM</th><th>DISK</th><th>DB: '+str(len(self.l_db())) + ' keys'+'</th></tr><tr><td>'+self.html_.circle(self.ram_usage_p()*100, big='big')+'</td><td>'+self.html_circle(self.disk_usage_p()*100, big='big', color='green')+'</td><td>'+self.html_circle(self.db_disk_p()*100, big='big', color='orange')+'</td></tr></table></center>'

	def delete(self, _id):
		del self.data[_id]
		self.u_db()

	def new(self, nData):
		for d in self.defaults:
			if d not in nData.keys():
				nData[d] = self.defaults[d]
		new_id = max(list(self.data.keys()))+1 if len(self.data) else 0
		self.data[new_id] = nData
		self.u_db()

	def get(self, _id):
		return self.data[_id]

	def getAll(self):
		return self.data

class UsersDB(DB):

	def addFav(self, _id, fav_id):
		if type(fav_id) is list:
			ids = set(fav_id)
		elif type(fav_id) is int:
			ids = {fav_id}
		self.data[_id]["Favs"] = self.data[_id]["Favs"].union(ids)

	def removeFav(self, _id, fav_id):
		if type(fav_id) is list:
			ids = set(fav_id)
		elif type(fav_id) is int:
			ids = {fav_id}
		self.data[_id]["Favs"] = self.data[_id]["Favs"].difference(ids)

	def getFavs(self, _id):
		return self.data[_id]["Favs"]


class BarsDB(DB):

	def compare(self, i1, i2):
		return i2.lower().startswith(i1.lower()) or i2.lower().startswith(i1[:-1].lower())

	def search(self, _input):
		return {k:self.data[k] for k in self.data if compare(_input, self.data[k]["Name"])}