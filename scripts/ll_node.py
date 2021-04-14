def lprint(l):
	for a in l:
		if type(a) is tuple:
			print(a[0], a[1])
		else:
			print(a, end= ", ")
	print()

class Node:
	nexus = []
	used = []
	name = 0
	def __init__(self, nex=None, n=0):
		if nex:
			self.append(nex)
		self.name = n
	def append(self, nex):
		self.nexus.append(nex)
	def get(self):
		if len(self.nexus) == 0:
			return False
		self.used.append(self.nexus[0])
		self.nexus = self.nexus[1:]
		return self.used[-1]
	def __str__(self):
		return str(self.name)


n = []
for i in range(10):
	n.append(Node(n=i))

"""
n[0].append(n[1])
n[0].append(n[9])

n[1].append(n[0])
n[1].append(n[2])
n[1].append(n[8])

n[2].append(n[1])
n[2].append(n[3])
n[2].append(n[7])

n[3].append(n[2])
n[3].append(n[4])
n[3].append(n[6])

n[4].append(n[3])
n[4].append(n[5])

n[5].append(n[4])
n[5].append(n[6])

n[6].append(n[5])
n[6].append(n[7])
n[6].append(n[3])

n[7].append(n[6])
n[7].append(n[8])
n[7].append(n[2])

n[8].append(n[7])
n[8].append(n[9])
n[8].append(n[1])

n[9].append(n[8])
n[9].append(n[1])
"""

def single(l):
	l_ = []
	for a, b in l:
		if (b, a) not in l:
			l_.append((a,b))
	return l_

paths = single([(0, 1), (0, 9), (1, 0), (1, 2), (1, 8), (2, 1), (2, 3), (2, 7), (3, 2), (3, 4), (3, 6), (4, 3), (4, 5), (5, 4), (5, 6), (6, 5), (6, 7), (6, 3), (7, 6), (7, 8), (7, 2), (8, 7), (8, 9), (8, 1), (9, 8), (9, 1)])

for p in paths:
	n[p[0]].append(n[p[1]])
	n[p[1]].append(n[p[0]])
"""
for s in n:
	i = s
	w = []
	while i.get():
		w.append((i, i := i.get()))
	
	lprint(w)
	print()
"""
lprint(n)
