# Búsqueda del tesoro con sonar

import random
import sys
import math

def obtenerNuevoTablero():
    # Crea una nueva estructura de datos para un tablero de 60x15.
    tablero = []
    for x in range(60): # La lista principal es una lista de 60 listas.
        tablero.append([])
        for y in range(15): # Cada lista en la lista principal tiene 15 cadenas de un solo caracter.
            # Usa diferentes caracteres para el oceáno para hacerlo más fácil de leer.
            if random.randint(0, 1) == 0:
                tablero[x].append('~')
            else:
                tablero[x].append('`')
    return tablero

def dibujarTablero(tablero):
    # Dibuja la estructura de datos del tablero
    lineaDigitosDecenas = '    ' # Espacio inicial para los números a lo largo del lado izquierdo del tablero
    for i in range(1, 6):
        lineaDigitosDecenas += (' ' * 9) + str(i)

    # Imprime los númerosa lo largo del borde superior del tablero.
    print(lineaDigitosDecenas)
    print('   ' + ('0123456789' * 6))
    print()

    # Imprimir cada una de las 15 líneas
    for fila in range(15):
        # Números de un solo dígito deben ser precedidos por un espacio extra
        if fila < 10:
            espacioExtra = ' '
        else:
            espacioExtra = ''

        # Crea la cadena para esta cadena en el tablero.
        filaTablero = ''
        for columna in range(60):
            filaTablero += tablero[columna][fila]

        print('%s%s %s %s' % (espacioExtra, fila, filaTablero, fila))

    # Imprime los números a lo largo del borde inferior del tablero.
    print()
    print(' ' + ('0123456789' * 6))
    print(lineaDigitosDecenas)

def obtenerCofresAleatorios(numCofres):
    # Crea una lista de estructuras de datos de cofre (listas de dos elementos enteros con coordenadas x, y)
    cofres = []
    while len(cofres) < numCofres:
        nuevoCofre = [random.randint(0, 59), random.randint(0, 14)]
        if nuevoCofre not in cofres: # Asegúrese que el cofre no esté ya incluido ahí.
            cofres.append(nuevoCofre)
    return cofres

def estaEnTablero(x, y):
    # Retorna verdadero (True) si las coordenadas están en el tablero; de lo contrario falso (False).
    return x >= 0 and x <= 59 and y >= 0 and y <= 14

def realizarMovida(tablero, cofres, x, y):
    # Cambia la estructura de datos tablero agregándole un caracter de dispositivo sonar. Elimina los cofres de la lista de cofres a medida que son encontrados.
    # Retorna falso si este es un movimiento inválido.
    # En caso contrario, retorna la cadena con el resultado de esta movida
    menorDistancia = 100 # Cualquier cofre estará a una distancia menor que 100.
    for cx, cy in cofres:
        distancia = math.sqrt((cx - x) * (cx - x) + (cy - y) * (cy - y))

        if distancia < menorDistancia: # Queremos el cofre más cercano.
            menorDistancia = distancia

    menorDistancia = round(menorDistancia)

    if menorDistancia == 0:
        # ¡xy está directametne sobre un cofre!
        cofres.remove([x, y])
        return '¡Ha encontrado un cofre de tesoro hundido!'
    else:
        if menorDistancia < 10:
            tablero[x][y] = str(menorDistancia)
            return 'Tesoro detectado a una distancia de %s del dispositivo de sonar.' % (menorDistancia)
        else:
            tablero[x][y] = 'X'
            return 'El sonar no ha detectado nada. Todos los cofres de tesoro están fuera del alcance del dispositivo.'

def ingresarMovidaJugadora(movidasPrevias):
    # Permite a la jugadora ingresr su movida. Retorna una lista con dos elementos enteros con las coordenadas xy.
    print('¿Dónde quiere dejar caer el siguiente dispositivo sonar? (0-59 0-14) (o ingrese salir)')
    while True:
        movida = input()
        if movida.lower() == 'salir':
            print('¡Gracias por jugar!')
            sys.exit()

        movida = movida.split()
        if len(movida) == 2 and movida[0].isdigit() and movida[1].isdigit() and estaEnTablero(int(movida[0]), int(movida[1])):
            if [int(movida[0]), int(movida[1])] in movidasPrevias:
                print('Ya usted se movió ahí.')
                continue
            return [int(movida[0]), int(movida[1])]

        print('Ingrese un número del 0 al 59, un espacio, luego un número del 0 al 14.')

def mostrarInstrucciones():
    print('''Instrucciones:
Usted es la capitana de El Simón, un buque cazador de tesoros. Su misión actual
es utilizar dispositivos de sonar para encontrar tres cofres con tesoros, hundidos en el
fondo del océano. Pero usted solo tiene sonares baratos que encuentran distancia, no dirección.

Ingrese las coordenadas para soltar un dispositivo de sonar. El mapa del océano será
marcado con cuán distante está el cofre más próximo, o una X si está más allá del alcance del
dispositivo de sonar. Por ejemplo las marcas C son donde están los cofres. El dispositivo de sonar
muestra un 3 porque el cofre más cercano está a 3 espacios.

                    1         2         3
          012345678901234567890123456789012

        0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
        1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
        2 `~`C``3`~~~~`C`~~~~`````~~``~~~`` 2
        3 ````````~~~`````~~~`~`````~`~``~` 3
        4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4

          012345678901234567890123456789012
                    1         2         3
(En el juego real, los cofres no serán visibles en el océano.)

Presione enter para continuar...''')
    input()

    print('''Cuando suelta un dispositivo de sonar directamente en un cofre, lo recoge y los otros
    dispositivos de sonar se actualizan para mostrar qué tan lejos está el siguiente cofre más cercano. Los cofres
    están más allá del alcance del dispositivo de sonar a la izquierda, por lo que muetra una X.

                    1         2         3
          012345678901234567890123456789012

        0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
        1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
        2 `~`X``7`~~~~`C`~~~~`````~~``~~~`` 2
        3 ````````~~~`````~~~`~`````~`~``~` 3
        4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4

          012345678901234567890123456789012
                    1         2         3

Los cofres de tesoro no se mueven. Los dispositivos de sonar pueden detectar cofres de
tesoro a una distancia de hasta 9 espacios. Intente recoger los 3 cofres antes de quedarse sin
dispositivos de sonar. ¡Buena suerte!

Presione enter para continuar...''')
    input()



print('S O N A R !')
print()
print('¿Le gustaría ver las instrucciones? (si/no)')
if input().lower().startswith('s'):
    mostrarInstrucciones()

while True:
    # Configuración del Juego
    dispositivosSonar = 20
    elTablero = obtenerNuevoTablero()
    losCofres = obtenerCofresAleatorios(3)
    dibujarTablero(elTablero)
    movidasPrevias = []

    while dispositivosSonar > 0:
        # Mostrar el estado de los dispositivos sonar y cofres
        print('Usted tiene %s dispositivo(s) de sonar restantes. %s cofre(s) de tesoro restantes.' % (dispositivosSonar, len(losCofres)))

        x, y = ingresarMovidaJugadora(movidasPrevias)
        movidasPrevias.append([x, y]) # debemos registrar todas las movidas para que los dispositivos sonar puedan ser actualizados.

        resultadoMovida = realizarMovida(elTablero, losCofres, x, y)
        if resultadoMovida == False:
            continue
        else:
            if resultadoMovida == '¡Ha encontrado un cofre de tesoro hundido!':
                # Actualiza todos los dispositivos sonar presentes en el mapa
                for x, y in movidasPrevias:
                    realizarMovida(elTablero, losCofres, x, y)
            dibujarTablero(elTablero)
            print(resultadoMovida)

        if len(losCofres) == 0:
            print('¡Ha encontrado todos los cofres del tesoro! ¡Felicitaciones y buena partida!')
            break

        dispositivosSonar -= 1

        if dispositivosSonar == 0:
            print('Nos hemos quedado sin dispositivos sonar! ¡Ahora tenemos que dar la vuelta y dirigirnos')
            print('de regreso a casa dejando tesoros en el mar! Juego terminado.')
            print('    Los cofres restantes estaban aquí:')
            for x, y in losCofres:
                print('    %s, %s' % (x, y))

print('¿Quiere jugar de nuevo? (sí o no)')
if not input().lower().startswith('s'):
    sys.exit()
