import random

DIGITOSNUM = 3
MAXINTENTOS = 10

def obtenerNumSecreto(DIGITOSNUM):
   	#Devuelve una cadena con digitos únicos de longitud DIGITOSNUM
	numeros = list(range(10))
	random.shuffle(numeros)
	numSecreto = ''
	for i in range(DIGITOSNUM):
		numSecreto += str(numeros[i])		
	return numSecreto

def obtenerPistas(intento, numSecreto):
	#Devuelve una cadena con las pistas Pico, Fermi y Panecillo
	if intento == numSecreto:
		return '¡Lo has adivinado!'
	
	pistas = []
	for i in range(len(intento)):
		if intento[i] == numSecreto[i]:				
			pistas.append('Fermi')
		elif intento[i] in numSecreto:
				pistas.append('Pico')
		if len(pistas) == 0:
			return 'Panecillos'

		pista.sort()
		return ' '.join(pista)

def esSoloDigitos(num):
	#Devuelve True si num es una cadena de solamente números, sino retorna False
	if num == '':
		return False
	
	for i in num:
		if i not in '0 1 2 3 4 5 6 7 8 9'.split():
			return False
		
	return True


print('Estoy pensando en un número de %s dígitos. Intenta adivinar cuál es.' % (DIGITOSNUM))
print('Aquí hay algunas pistas:')
print('Cuando digo:    Eso significa:')
print('  Pico          Un dígito es correcto pero está en la posición incorrecta.')
print('  Fermi         Un dígito es correcto y está en la posición correcta.')
print('  Panecillos    Ningún dígito es correcto.')

while True:
		numSecreto = obtenerNumSecreto(DIGITOSNUM)		
		print('He pensado un número. Tienes %s intentos para adivinarlo.' % (MAXINTETOS))

		numIntentos = 1
		while numIntentos <= MAXINTETOS:
			intento = ''
			while len(intento) != DIGITOSNUM or not esSoloDigitos(intento):
				print('Intento #%s: ' % (numIntentos))
				intento = input()
		
			print(obtenerPistas(intento, numSecreto))			
			numIntentos += 1

			if intento == numSecreto:
				break
			if numIntentos > MAXINTETOS:
				print('Te has quedado sin intentos. La respuesta era %s.' % (numSecreto))

		print('¿Deseas volver a jugar? (sí o no)')
		if not input.lower().startswith('s')
			break