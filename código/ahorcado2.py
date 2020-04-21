import random
IMÁGENES_AHORCADO = ['''		
  +---+
      |		
      |		
      |		
     ===''', '''		
  +---+		
  O   |
      |		
      |		
     ===''', '''		
  +---+		
  O   |		
  |   |		
      |		
     ===''', '''		
  +---+		
  O   |		
 /|   |		
      |		
     ===''', '''		
  +---+		
  O   |		
 /|\  |		
      |		
     ===''', '''		
  +---+		
  O   |		
 /|\  |		
 /    |		
     ===''', '''		
  +---+		
  O   |		
 /|\  |		
 / \  |		
     ===''', '''
  +---+
 [O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O]  |
 /|\  |
 / \  |
     ===''']
palabras = {'Colores':'rojo naranja amarillo verde azul añil violeta blanco negro marron'.split(),
            'Formas':'cuadrado triangulo rectangulo circulo elipse rombo trapezoide chevron pentágono hexágono heptágono octágono'.split(),
            'Frutas':'manzana naranja limon lima pera sandia uva pomelo cereza banana melon mango fresa tomate'.split(),
            'Animales':'murcielago oso castor gato pantera cangrejo ciervo perro burro pato aguila pez rana cabra sanguijuela leon lagarto mono alce raton nutria buho panda piton conejo rata tiburon oveja mofeta calamar tigre pavo tortuga comadreja ballena lobo wombat cebra'.split()}

def obtenerPalabraAlAzar(diccionarioDePalabras):
    # Esta función devuelve una cadena al azar del diccionario de listas de cadenas y sus claves
    # Primero, elige una clave al azar del diccionario:
    claveDePalabra = random.choice(list(diccionarioDePalabras.keys()))
    
    # Segundo, elige una palabra aleatoria de la lista de claves en el diccionario:
    índiceDePalabra = random.randint(0, len(diccionarioDePalabras[claveDePalabra]) - 1)
    
    return [diccionarioDePalabras[claveDePalabra][índiceDePalabra], claveDePalabra]

def mostrarTablero(letrasIncorrectas, letrasCorrectas, palabraSecreta):
    print(IMÁGENES_AHORCADO[len(letrasIncorrectas)])
    print()

    print('Letras incorrectas:', end=' ')
    for letra in letrasIncorrectas:
        print(letra, end=' ')
    print()

    espaciosVacíos = '_' * len(palabraSecreta)

    for i in range(len(palabraSecreta)): # completar los espacios vacíos con las letras adivinadas
        if palabraSecreta[i] in letrasCorrectas:
            espaciosVacíos = espaciosVacíos[:i] + palabraSecreta[i] + espaciosVacíos[i+1:]

    for letra in espaciosVacíos: # mostrar la palabra secreta con espacios entre cada letra
        print(letra, end=' ')
    print()

def obtenerIntento(letrasProbadas):
    # Devuelve la letra ingresada por la jugadora. Verifica que la jugadora ha ingresado sólo una letra, y no otra cosa.
    while True:
        print('Adivina una letra.')
        intento = input()
        intento = intento.lower()
        if len(intento) != 1:
            print('Por favor, introduce una letra.')
        elif intento in letrasProbadas:
            print('Ya has probado esa letra. Elige otra.')
        elif intento not in 'abcdefghijklmnñopqrstuvwxyz':
            print('Por favor ingresa una LETRA.')
        else:
            return intento

def jugarDeNuevo():
    # Esta función devuelve True si la jugadora quiere volver a jugar, en caso contrario devuelve False.
    print('¿Quieres jugar de nuevo? (sí o no)')
    return input().lower().startswith('s')


print('A H O R C A D O')

dificultad = 'X'
while dificultad not in ['F', 'M', 'D']:
    print('Ingrese la dificultad: F - Fácil, M - Medio, D - Difícil')
    dificultad = input().upper()
if dificultad == 'M':
    del IMÁGENES_AHORCADO[8]
    del IMÁGENES_AHORCADO[7]
if dificultad == 'D':
    del IMÁGENES_AHORCADO[8]
    del IMÁGENES_AHORCADO[7]
    del IMÁGENES_AHORCADO[5]
    del IMÁGENES_AHORCADO[3]

letrasIncorrectas = ''
letrasCorrectas = ''
palabraSecreta, conjuntoSecreto = obtenerPalabraAlAzar(palabras)
juegoTerminado = False

while True:
    print('La palabra secreta pertenece al conjunto: ' + conjuntoSecreto)
    mostrarTablero(letrasIncorrectas, letrasCorrectas, palabraSecreta)

    # Permite a la jugadora escribir una letra.
    intento = obtenerIntento(letrasIncorrectas + letrasCorrectas)

    if intento in palabraSecreta:
        letrasCorrectas = letrasCorrectas + intento

        # Verifica si la jugadora ha ganado.
        encontradoTodasLasLetras = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letrasCorrectas:
                encontradoTodasLasLetras = False
                break
        if encontradoTodasLasLetras:
            print('¡Sí! ¡La palabra secreta es "' + palabraSecreta + '"! ¡Has ganado!')
            juegoTerminado = True
    else:
        letrasIncorrectas = letrasIncorrectas + intento
        # Comprobar si la jugadora ha agotado sus intentos y ha perdido.
        if len(letrasIncorrectas) == len(IMÁGENES_AHORCADO) - 1:
            mostrarTablero(letrasIncorrectas, letrasCorrectas, palabraSecreta)
            print('¡Te has quedado sin intentos!\nDespués de ' +
                  str(len(letrasIncorrectas)) + ' intentos fallidos y ' +
                  str(len(letrasCorrectas)) + ' aciertos, ' + 
                  'la palabra era "' + palabraSecreta + '"')
            juegoTerminado = True

    # Preguntar a la jugadora si quiere volver a jugar (pero sólo si el juego ha terminado).
    if juegoTerminado:
        if jugarDeNuevo():
            letrasIncorrectas = ''
            letrasCorrectas = ''
            juegoTerminado = False
            palabraSecreta, conjuntoSecreto = obtenerPalabraAlAzar(palabras)
        else:
            break
