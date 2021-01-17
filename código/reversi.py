# Reversi: un clone de Othello/Reversegam
import random
import sys
ANCHO = 8 # El tablero tiene 8 espacios de ancho.
ALTO = 8 # El tablero tiene 8 espacios de alto.
def dibujarTablero(tablero):
    # Imprime el tablero pasado a esta función. Retorna None.
    print('  12345678')
    print(' +--------+')
    for y in range(ALTO):
        print('%s|' % (y+1), end='')
        for x in range(ANCHO):
            print(tablero[x][y], end='')
        print('|%s' % (y+1))
    print(' +--------+')
    print('  12345678')

def obtenerNuevoTablero():
    # Crea un nuevo tablero, una estructura de datos de tablero vacío.
    tablero = []
    for i in range(ANCHO):
        tablero.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    return tablero

def esJugadaVálida(tablero, ficha, iniciox, inicioy):
    # Retorna False si la jugada de la jugadora en iniciox, inicioy es inválida.
    # Si es una jugada válida, retorna una lista de espacios que pasarían a ser de la jugadora si moviera ahí.
    if tablero[iniciox][inicioy] != ' ' or not estáEnTablero(iniciox, inicioy):
        return False

    if ficha == 'X':
        otraFicha = 'O'
    else:
        otraFicha = 'X'

    fichasAVoltear = []
    for direcciónx, direccióny in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = iniciox, inicioy
        x += direcciónx # Primer paso en la dirección x
        y += direccióny # Primer paso en la dirección y
        while estáEnTablero(x, y) and tablero[x][y] == otraFicha:
            # Se mantienen moviendose en esa dirección x & y.
            x += direcciónx
            y += direccióny
            if estáEnTablero(x, y) and tablero[x][y] == ficha:
                # Hay fichas para voltear. Vaya en la dirección opuesta hasta que alcance el espacio original, registrando todas las fichas en el camino.
                while True:
                    x -= direcciónx
                    y -= direccióny
                    if x == iniciox and y == inicioy:
                        break
                    fichasAVoltear.append([x, y])

    if len(fichasAVoltear) == 0: # Si no se voltearon fichas, este no es un movimiento válido.
        return False
    return fichasAVoltear

def estáEnTablero(x, y):
    # Devuelve True si las coordenadas se encuentran dentro del tablero.
    return x >= 0 and x <= ANCHO - 1 and y >= 0 and y <= ALTO - 1

def obtenerTableroConJugadasVálidas(tablero, ficha):
    # Retorna un nuevo tablero con puntos marcando las movidas válidas que la jugadora puede realizar.
    copiaDeTablero = obtenerCopiaTablero(tablero)

    for x, y in obtenerJugadasVálidas(copiaDeTablero, ficha):
        copiaDeTablero[x][y] = '.'
    return copiaDeTablero

def obtenerJugadasVálidas(tablero, ficha):
    # Retorna una lista de listas [x,y] de jugadas válidas para la jugadora y tablero dades.
    jugadasVálidas = []
    for x in range(ANCHO):
        for y in range(ALTO):
            if esJugadaVálida(tablero, ficha, x, y) != False:
                jugadasVálidas.append([x, y])
    return jugadasVálidas

def obtenerPuntajeTablero(tablero):
    # Determina el puntaje contando las fichsa. Retorna un diccionario con las llaves 'X' y 'O'.
    puntajex = 0
    puntajeo = 0
    for x in range(ANCHO):
        for y in range(ALTO):
            if tablero[x][y] == 'X':
                puntajex += 1
            if tablero[x][y] == 'O':
                puntajeo += 1
    return {'X':puntajex, 'O':puntajeo}

def ingresarFichaDeJugadora():
    # Permite a la juadora elegir qué ficha quiere mover.
    # Retorna una lista con la ficha de la jugadora como primer elemento y la de la computadora como segundo.
    ficha = ''
    while not (ficha == 'X' or ficha == 'O'):
        print('¿Desea ser las fichas X o O?')
        ficha = input().upper()

    # El primer elemento en la lista es la ficha de la jugadora, el segundo elemento es la de la computadora.
    if ficha == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def quiénComienza():
    # Al azar elige qué jugadora inicia.
    if random.randint(0, 1) == 0:
        return 'computadora'
    else:
        return 'jugadora'

def hacerJugada(tablero, ficha, iniciox, inicioy):
    # Coloca la ficha sobre el tablero en iniciox, inicioy y convierte cualquier ficha de la oponente.
    # Retorna False si esta movida es inválida; True si es válida.
    fichasAVoltear = esJugadaVálida(tablero, ficha, iniciox, inicioy)

    if fichasAVoltear == False:
        return False

    tablero[iniciox][inicioy] = ficha
    for x, y in fichasAVoltear:
        tablero[x][y] = ficha
    return True

def obtenerCopiaTablero(tablero):
    # Crea un duplicado de la lista del tablero y la retorna.
    copiaDeTablero = obtenerNuevoTablero()

    for x in range(ANCHO):
        for y in range(ALTO):
            copiaDeTablero[x][y] = tablero[x][y]

    return copiaDeTablero

def esEsquina(x, y):
    # Retorna True si la posición está en una de las cuatro esquinas.
    return (x == 0 or x == ANCHO - 1) and (y == 0 or y == ALTO - 1)

def obtenerJugadaJugadora(tablero, fichaJugadora):
    # Permite a la jugadora ingresar su movimiento.
    # Retorna la movida como [x, y] (o retorna la cadena 'pistas' o 'salir').
    CIFRAS1A8 = '1 2 3 4 5 6 7 8'.split()
    while True:
        print('Ingrese su jugada, "salir" para finalizar el juego, o "pistas" para activar/desactivar las pistas.')
        movida = input().lower()
        if movida == 'salir' or movida == 'pistas':
            return movida

        if len(movida) == 2 and movida[0] in CIFRAS1A8 and movida[1] in CIFRAS1A8:
            x = int(movida[0]) - 1
            y = int(movida[1]) - 1
            if esJugadaVálida(tablero, fichaJugadora, x, y) == False:
                continue
            else:
                break
        else:
            print('Esa no es una jugada válida. Ingrese la columna (1-8) y luego la fila (1-8).')
            print('Por ejemplo, 81 coresponde a la esquina superior derecha.')

    return [x, y]

def obtenerJugadaComputadora(tablero, fichaComputadora):
    # Dado un tbalero y una ficha de la computadora, determina dónde
    # jugar y retorna la movida como una lista [x, y].
    movidasPosibles = obtenerJugadasVálidas(tablero, fichaComputadora)
    random.shuffle(movidasPosibles) # Ordena al azar el orden de las jugadras posibles.

    # Siempre juega en una esquna si está disponible.
    for x, y in movidasPosibles:
        if esEsquina(x, y):
            return [x, y]

    # Busca la movida de mayor puntaje posible.
    mejorPuntaje = -1
    for x, y in movidasPosibles:
        copiaDeTablero = obtenerCopiaTablero(tablero)
        hacerJugada(copiaDeTablero, fichaComputadora, x, y)
        puntaje = obtenerPuntajeTablero(copiaDeTablero)[fichaComputadora]
        if puntaje > mejorPuntaje:
            mejorJugada = [x, y]
            mejorPuntaje = puntaje
    return mejorJugada

def mostrarPuntajes(tablero, fichaJugadora, fichaComputadora):
    puntajes = obtenerPuntajeTablero(tablero)
    print('Usted: %s puntos. Computadora: %s puntos.' % (puntajes[fichaJugadora], puntajes[fichaComputadora]))

def jugarJuego(fichaJugadora, fichaComputadora):
    mostrarPistas = False
    turno = quiénComienza()
    print('Las fichas de la ' + turno + ' comenzarán.')

    # Limpia el tablero y coloca la piezas iniciales.
    tablero = obtenerNuevoTablero()
    tablero[3][3] = 'X'
    tablero[3][4] = 'O'
    tablero[4][3] = 'O'
    tablero[4][4] = 'X'

    while True:
        jugadasVálidasJugadora = obtenerJugadasVálidas(tablero, fichaJugadora)
        jugadasVálidasComputadora = obtenerJugadasVálidas(tablero, fichaComputadora)

        if jugadasVálidasJugadora == [] and jugadasVálidasComputadora == []:
            return tablero # Nadie se puede mover, así que el juego terminará.

        elif turno == 'jugadora': # Turno de la jugadora
            if jugadasVálidasJugadora != []:
                if mostrarPistas:
                    tableroJugadasVálida = obtenerTableroConJugadasVálidas(tablero, fichaJugadora)
                    dibujarTablero(tableroJugadasVálida)
                else:
                    dibujarTablero(tablero)
                mostrarPuntajes(tablero, fichaJugadora, fichaComputadora)

                movida = obtenerJugadaJugadora(tablero, fichaJugadora)
                if movida == 'salir':
                    print('¡Gracias por jugar!')
                    sys.exit() # Termina el programa.
                elif movida == 'pistas':
                    mostrarPistas = not mostrarPistas
                    continue
                else:
                    hacerJugada(tablero, fichaJugadora, movida[0], movida[1])
            turno = 'computadora'

        elif turno == 'computadora': # turno de la computadora
            if jugadasVálidasComputadora != []:
                dibujarTablero(tablero)
                mostrarPuntajes(tablero, fichaJugadora, fichaComputadora)

                input('Presione ENTER para ver la jugada de la computadora.')
                movida = obtenerJugadaComputadora(tablero, fichaComputadora)
                hacerJugada(tablero, fichaComputadora, movida[0], movida[1])
            turno = 'jugadora'



print('¡Bienvenida a Reversi!')

fichaJugadora, fichaComputadora = ingresarFichaDeJugadora()

while True:
    tableroFinal = jugarJuego(fichaJugadora, fichaComputadora)

    # Muestra el puntaje final.
    dibujarTablero(tableroFinal)
    puntajes = obtenerPuntajeTablero(tableroFinal)
    print('X obtuvo %s puntos. O obtuvo %s puntos.' % (puntajes['X'], puntajes['O']))
    if puntajes[fichaJugadora] > puntajes[fichaComputadora]:
        print('¡Usted venció la computadora por %s puntos! ¡Felicidades!' % (puntajes[fichaJugadora] - puntajes[fichaComputadora]))
    elif puntajes[fichaJugadora] < puntajes[fichaComputadora]:
        print('Usted perdió. La computadora la venció por %s puntos.' % (puntajes[fichaComputadora] - puntajes[fichaJugadora]))
    else:
        print('¡El juego finalizó empatado!')

    print('¿Quiere jugar de nuevo? (si o no)')
    if not input().lower().startswith('s'):
        break
