def repite(n):
	reps = [0] * max_e(n)
	for i in n:
		for j in n:
			if int(i)-int(j) == 0:
				reps[int(i)-1] += 1
	return (4 in reps and len(n) == 3) or (9 in reps and len(n) == 4)

def max_e(s):
	m = 0
	for e in s:
		if int(e) > m:
			m = int(e)
	return m