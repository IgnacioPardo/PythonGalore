from time import sleep
import os

from random import randint


os.system("clear")

text = "VICKY PARDO"
top = 80
lines = 320

out = text
for i in range(1, lines):
	cant = (1//i) * 10
	out = " "*cant + out
	if len(out) == top or randint(0, 10) > 9:
		for i in range(top):
			out = out[1:]
			sleep(0.04)
			print(out)
			if len(out) == len(text) or randint(0, 10) > 9:
				i = 0
				break

	sleep(0.04)
	print(out)
