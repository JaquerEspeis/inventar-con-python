# Cifrado Cesar
SÍMBOLOS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
TAM_MAX_CLAVE = len(SÍMBOLOS)

def obtenerModo():
    while True:
        print('¿Desea encriptar, desencriptar o aplicar fuerza bruta a un mensaje?')
        modo = input().lower()
        if modo in ['encriptar', 'e', 'desencriptar', 'd', 'fuerza', 'f']:
            return modo
        else:
            print('Ingrese "encriptar" o "e", "desencriptar" o "d" o "fuerza" o "f".')

def obtenerMensaje():
    print('Ingrese su mensaje:')
    return input()

def obtenerClave():
    clave = 0
    while True:
        print('Ingrese el número de clave (1-%s)' % (TAM_MAX_CLAVE))
        clave = int(input())
        if (clave >= 1 and clave <= TAM_MAX_CLAVE):
            return clave

def obtenerMensajeTraducido(modo, mensaje, clave):
    if modo[0] == 'd':
        clave = -clave
    traducido = ''

    for símbolo in mensaje:
        índiceSímbolo = SÍMBOLOS.find(símbolo)
        if índiceSímbolo == -1: # Símbolo no encontrado en SÍMBOLOS.
            # Solo añada este símbolo sin cambios.
            traducido += símbolo
        else:
            # Encripta o desencripta.
            índiceSímbolo += clave

            if índiceSímbolo >= len(SÍMBOLOS):
                índiceSímbolo -= len(SÍMBOLOS)
            elif índiceSímbolo < 0:
                índiceSímbolo += len(SÍMBOLOS)

            traducido += SÍMBOLOS[índiceSímbolo]
    return traducido

modo = obtenerModo()
mensaje = obtenerMensaje()
if modo[0] != 'f':
    clave = obtenerClave()
print('Su texto traducido es:')
if modo[0] != 'f':
    print(obtenerMensajeTraducido(modo, mensaje, clave))
else:
    for clave in range(1, TAM_MAX_CLAVE + 1):
        print(clave, obtenerMensajeTraducido('desencriptar', mensaje, clave))
