import random
print('Lanzaré una moneda 1000 veces. Adivina cuantas veces caerá Escudo. (Presiona enter para comenzar)')
input()
lanzamientos = 0
escudos = 0
while lanzamientos < 1000:
    if random.randint(0, 1) == 1:
        escudos = escudos + 1
    lanzamientos = lanzamientos + 1
    
    if lanzamientos == 900:
        print('900 lanzamientos y hubo ' + str(escudos) + ' escudos.')

    if lanzamientos == 100:
        print('En 100 lanzamientos, escudo salió ' + str(escudos) + ' veces.')

    if lanzamientos == 500:
        print('La mitad de los lanzamientos y escudo salió ' + str(escudos) + ' veces.')

print()
print('De 1000 lanzamientos, al final escudo salió ' + str(escudos) + ' veces!')
print('¿Estuviste cerca?')
