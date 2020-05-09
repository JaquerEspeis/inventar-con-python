# Tres en línea

import random

def dibujarTablero(tablero):
    # Esta función dibuja el tablero recibido como argumento.

    # "tablero" es una lista de 10 cadenas representando el tablero (ignora índice 0)
    print(tablero[7] + '|' + tablero[8] + '|' + tablero[9])
    print('-+-+-')
    print(tablero[4] + '|' + tablero[5] + '|' + tablero[6])
    print('-+-+-')
    print(tablero[1] + '|' + tablero[2] + '|' + tablero[3])
    
def ingresaLetraJugador():
    # Permite a la jugadora ingresar que letra desea ser.
    # Devuelve una lista con las letras de la jugadora como primer item, y la de la computadora como segundo.
    letra = ''
    while not (letra == 'X' or letra == 'O'):
        print('¿Desea ser X o O?')
        letra = input().upper()

    # el primer elemento de la lista es la letra de la jugadora, el segundo es la letra de la computadora.
    if letra == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def quienComienza():
    # Elije al azar que jugador comienza.
    if random.randint(0, 1) == 0:
        return 'La computadora'
    else:
        return 'La jugadora'

def hacerJugada(tablero, letra, jugada):
    tablero[jugada] = letra

def esGanador(ta, le):
    # Dado un tablero y la letra de una jugadora, devuelve True (verdadero) si la misma ha ganado.
    # Utilizamos "ta" por tablero y "le" por letra para no escribir tanto.
    return ((ta[7] == le and ta[8] == le and ta[9] == le) or # horizontal superior
            (ta[4] == le and ta[5] == le and ta[6] == le) or # horizontal medio
            (ta[1] == le and ta[2] == le and ta[3] == le) or # horizontal inferior
            (ta[7] == le and ta[4] == le and ta[1] == le) or # vertical izquierda
            (ta[8] == le and ta[5] == le and ta[2] == le) or # vertical medio
            (ta[9] == le and ta[6] == le and ta[3] == le) or # vertical derecha
            (ta[7] == le and ta[5] == le and ta[3] == le) or # diagonal
            (ta[9] == le and ta[5] == le and ta[1] == le)) # diagonal

def obtenerCopiaDelTablero(tablero):
    # Hace una copia la lista del tablero y lo devuelve.
    copaDelTablero = []
    for i in tablero:
        copaDelTablero.append(i)
    return copaDelTablero

def hayEspacioLibre(tablero, jugada):
    # Devuelte true si la jugada pasada como argumento está libre en el tablero
    return tablero[jugada] == ' '

def obtenerJugadaJugadora(tablero):
    # Permite a la jugadora ingresar su jugada.
    jugada = ' '
    while jugada not in '1 2 3 4 5 6 7 8 9'.split() or not hayEspacioLibre(tablero, int(jugada)):
        print('¿Cuál es su próxima jugada? (1-9)')
        jugada = input()
    return int(jugada)

def elegirJugadaAlAzarDeLista(tablero, listaJugadas):
    # Devuelve una jugada válida del tablero recibido como argumento.
    # Devuelve None si no hay ninguna jugada válida.
    jugadasPosibles = []
    for i in listaJugadas:
        if hayEspacioLibre(tablero, i):
            jugadasPosibles.append(i)

        if len(jugadasPosibles) != 0:
            return random.choice(jugadasPosibles)
        else:
            return None

def obtenerJugadaComputadora(tablero, letraComputadora):
    # Dado un tablero y una letra de la computadora, determina dónde moverse.
    if letraComputadora == 'X':
        letraJugador = 'O'
    else:
        letraJugador = 'X'

    # Aquí está el algoritmo para nuestra IA del Tres en línea
    # Primero, verifica si podemos ganar en la próxima jugada
    for i in range(1, 10):
        copiaTablero = obtenerCopiaDelTablero(tablero)
        if hayEspacioLibre(copiaTablero, i):
            hacerJugada(copiaTablero, letraComputadora, i)
            if esGanador(copiaTablero, letraComputadora):
                return i

    # Verifica si la jugadora podría ganar en su próxima jugada, y la bloquea.
    for i in range(1, 10):
        copiaTablero = obtenerCopiaDelTablero(tablero)
        if hayEspacioLibre(copiaTablero, i):
            hacerJugada(copiaTablero, letraJugador, i)
            if esGanador(copiaTablero, letraJugador):
                return i

    # Intenta ocupar una de las esquinas de estar libre.
    jugada = elegirJugadaAlAzarDeLista(tablero, [1, 3, 7, 9])
    if jugada != None:
        return jugada

    # De estar libre, intenta ocupar el centro.
    if hayEspacioLibre(tablero, 5):
        return 5

    # Ocupa alguno de los lados.
    return elegirJugadaAlAzarDeLista(tablero, [2, 4, 6, 8])

def tableroEstaCompleto(tablero):
    # Devuelve True si cada espacio del tablero fue ocupado, caso contrario devuele False.
    for i in range(1, 10):
        if hayEspacioLibre(tablero, i):
            return False
    return True


print('¡Bienvenida al Tres en línea!')

while True:
    # Reinicia el tablero
    elTablero = [' '] * 10
    letraJugador, letraComputadora = ingresaLetraJugador()
    turno = quienComienza()
    print(turno + ' irá primero.')
    juegoEnCurso = True

    while juegoEnCurso:
        if turno == 'La jugadora':
            # Turno de la jugadora
            dibujarTablero(elTablero)
            jugada = obtenerJugadaJugadora(elTablero)
            hacerJugada(elTablero, letraJugador, jugada)

            if esGanador(elTablero, letraJugador):
                dibujarTablero(elTablero)
                print('¡Felicidades, has ganado!')
                juegoEnCurso = False
            else:
                if tableroEstaCompleto(elTablero):
                    dibujarTablero(elTablero)
                    print('¡Es un empate!')
                    break
                else:
                    turno = 'La computadora'

        else:
            # Turno de la computadora
            jugada = obtenerJugadaComputadora(elTablero, letraComputadora)
            hacerJugada(elTablero, letraComputadora, jugada)

            if esGanador(elTablero, letraComputadora):
                dibujarTablero(elTablero)
                print('¡La computadora le ha vencido! Ha perdido.')
                juegoEnCurso = False
            else:
                if tableroEstaCompleto(elTablero):
                    dibujarTablero(elTablero)
                    print('¡Es un empate!')
                    break
                else:
                    turno = 'La jugadora'

    print('¿Desea volver a jugar? (sí/no)?')
    if not input().lower().startswith('s'):
        break
