def repite(n):
	reps = [0 for _ in range(max_e(n)+1)]

	for i in range(len(n)-2):
		reps[int(n[i])] += 1
		if n[i] in n[:i] + n[i+1:]:
			reps[int(n[i])] += 1
			n = n[:i] + n[i+1:]

	print(reps)

def rep(n):
	reps = [0 for _ in range(max_e(n)+1)]
	for i in range(len(n)):
		reps[int(n[i])] += 1
	print(reps)

def max_e(s):
	m = 0
	for e in s:
		if int(e) > m:
			m = int(e)
	return m
