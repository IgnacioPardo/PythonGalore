from random import randint

modo = input("Modo de juego (Dificil/Medio/Facil): ")

d = (modo == "Dificil")*4 + (modo == "Medio")*3 + (modo == "Facil")*3  
attempts = (modo == "Dificil")*4 + (modo == "Medio")*5 + (modo == "Facil")*8  

contra = randint(10**(d-1), 10**d-1)

for a in range(attempts):
	attempt = input("Ingrese la clave de " + str(d) + " digitos: ")
	if str(contra) == attempt:
		print("Ganaste")
		quit()
	else:
		count = 0
		digs = 0
		posiciones = [0 for _ in range(d)]
		for i in range(len(attempt)):
			count += 1*(attempt[i] == str(contra)[i])
			digs += 1*(attempt[i] in str(contra))
			posiciones[i] = (attempt[i] == str(contra)[i])

		print(count, " posiciones correctas.")
		if modo == "Medio" or modo == "Facil":
			print(digs, " numeros correctos.")
			if modo == "Facil":
				print(["✓" if a else "X" for a in posiciones])
		print("Quedan ", attempts - a - 1, " intentos. \n")
print("Perdiste, la contraseña era: ", contra)