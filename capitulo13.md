# 13 Búsqueda del tesoro con sonar

![Imagen de ciencia](https://inventwithpython.com/invent4thed/images/00016.jpeg)

El juego de la búsqueda del tesoro con sonar en este capítulo es el primero que hace uso del sistema de coordenadas Cartesianas del que usted aprendió en el capítulo 12. Este juego también utiliza estructura de datos, que es solo una manera elegante para decir que tiene valores de lista que contienen otras listas y variables complejas similares. Al tiempo que los juegos que usted programe se hacer más complicados, usted necesitará organizar sus datos en estructuras de datos. 

En el juego de este capítulo, la jugadora deja caer un dispositivo sonar en varios lugares en el océano para localizar cofres de tesoro hundidos. *Sonar* es una tecnología que las embarcaciones utilizan para localizar objetos bajo el mar. Los dispositivos sonar en este juego le dirán a la jugadora que tan lejos está el cofre de tesoro más cerano, pero no en cuál dirección. Pero colocando múltiples dispositivos sonar, la jugadora podrá descubrir la ubicación del cofre de tesoro. 

---

Temas cubiertos en este capítulo:

* Estructuras de datos
* El teorema de Pitágoras
* El método `remove()` de lista
* El método `isdigit()` de cadena
* La función `sys.exit()`

---

Hay 3 cofres para recoger, y la jugadora tiene sólo 20 dispositivos de sonar para usar para descubrirlos. Imagine que usted no pudiera ver el cofre de tesoro en la Figura 13-1. Debido a que cada dispositivo de sonar puede encontrar únicamente la distancia desde el cofre, no la dirección del cofre, el tesoro podría estar en cualquier lugar del círculo alrededor del dispositivo de sonar. 

![](https://inventwithpython.com/invent4thed/images/00047.jpeg)

*Figura 13-1: El círculo del dispositivo de sonar toca el cofre de tesoro (oculto).*

Pero múltiples dispositivos de sonar trabajando juntos pueden achicar la ubicación del cofre hasta las coordenadas exactas donde los círculos se intersecan (ver Figura 13-2). 

![](https://inventwithpython.com/invent4thed/images/00056.jpeg)

*Figura 13-2: Combinando múltiples círculos se muestra dónde podrían estar escondidos los cofres de tesoro.*

## Ejecución de ejemplo de la Búsqueda del tesoro con sonar

Acá está lo que la usuaria ve cuando ejecuta el programa de la Búsqueda del tesoro con sonar. El texto que la jugadora ingresa está mostrado entre asteriscos. 

~~~shell
S O N A R !

¿Le gustaría ver las instrucciones? (si/no)
**no**
             1         2         3         4         5
   012345678901234567890123456789012345678901234567890123456789

 0 ~~~~``````~```~~`~~~`~~~~~~~`~```````~```~`~````~```~~````~~ 0
 1 ~~~```~~~~```~~~`~~~~`~~`````~~``~~~```~`~~`~~```~`~~~``~~`~ 1
 2 ``~~~`~~``~~`~`~~~`~~~~~`~~```````~``~~~````~`~~~~~~````~~`~ 2
 3 ~``~```~``~`~`~``~```~`~`~~```~~`~~~~````~~``~`~`~```~~``~~~ 3
 4 ~~~`~~~~`~```~~~~~``~```~``~~~~``~~~``````~~`~~~`````~`~~~~~ 4
 5 ``~~`~``~`~`~`~`~~~~`~`~`~~~``~~~~~~`~```~`~~``~~``~~`~``~~` 5
 6 ~~~~~`~~~`~``~`~~~`~~`~~``~`~~~~``~~`````~~``~``~`~~`~`~~~`` 6
 7 ~`~`````~`~~`~~`~~~~``~````~~~`~~````~~````~`~~~~~```~`~~~~~ 7
 8 ``~~`~~~~```~`~~~``~~~~`~~~~``~~`~~~`~`~```~`~`~`~````~````` 8
 9 ~`~`~~~`````~`~`~~~~`~```~`~~`~~```````~``~`~```~````~`~~``~ 9
10 ```~~``~~``~~~`~~~~``~~~````~`~`~`~~`~~~`~~`~`~~`````~``~~~~ 10
11 ```~``~~~~```~~~``~~~~`````~`~~~~`~`~```~`~~~``````~`~``~~`~ 11
12 `~`~``~~`~``~`~`~~~~`~~`~~~~`~`~~~~~`~`~``~~~`````~~`~``~``~ 12
13 ~~`~~`~`~``~~`~``~``~~~~``~~`~```~~~``~``~~~~`~````~``~~~``~ 13
14 ~```````~~~````````~`~~`~``~`````~~~``~~~~~`~~```~~`~~``~~~~ 14

 012345678901234567890123456789012345678901234567890123456789
             1         2         3         4         5
Usted tiene 20 dispositivo(s) de sonar restantes. 3 cofre(s) de tesoro restantes.
¿Dónde quiere dejar caer el siguiente dispositivo sonar? (0-59 0-14) (o ingrese salir)
**30 5**
             1         2         3         4         5
   012345678901234567890123456789012345678901234567890123456789

 0 ~~~~``````~```~~`~~~`~~~~~~~`~```````~```~`~````~```~~````~~ 0
 1 ~~~```~~~~```~~~`~~~~`~~`````~~``~~~```~`~~`~~```~`~~~``~~`~ 1
 2 ``~~~`~~``~~`~`~~~`~~~~~`~~```````~``~~~````~`~~~~~~````~~`~ 2
 3 ~``~```~``~`~`~``~```~`~`~~```~~`~~~~````~~``~`~`~```~~``~~~ 3
 4 ~~~`~~~~`~```~~~~~``~```~``~~~~``~~~``````~~`~~~`````~`~~~~~ 4
 5 ``~~`~``~`~`~`~`~~~~`~`~`~~~``X~~~~~`~```~`~~``~~``~~`~``~~` 5
 6 ~~~~~`~~~`~``~`~~~`~~`~~``~`~~~~``~~`````~~``~``~`~~`~`~~~`` 6
 7 ~`~`````~`~~`~~`~~~~``~````~~~`~~````~~````~`~~~~~```~`~~~~~ 7
 8 ``~~`~~~~```~`~~~``~~~~`~~~~``~~`~~~`~`~```~`~`~`~````~````` 8
 9 ~`~`~~~`````~`~`~~~~`~```~`~~`~~```````~``~`~```~````~`~~``~ 9
10 ```~~``~~``~~~`~~~~``~~~````~`~`~`~~`~~~`~~`~`~~`````~``~~~~ 10
11 ```~``~~~~```~~~``~~~~`````~`~~~~`~`~```~`~~~``````~`~``~~`~ 11
12 `~`~``~~`~``~`~`~~~~`~~`~~~~`~`~~~~~`~`~``~~~`````~~`~``~``~ 12
13 ~~`~~`~`~``~~`~``~``~~~~``~~`~```~~~``~``~~~~`~````~``~~~``~ 13
14 ~```````~~~````````~`~~`~``~`````~~~``~~~~~`~~```~~`~~``~~~~ 14

 012345678901234567890123456789012345678901234567890123456789
             1         2         3         4         5
El sonar no ha detectado nada. Todos los cofres de tesoro están fuera del alcance del dispositivo.
Usted tiene 19 dispositivo(s) de sonar restantes. 3 cofre(s) de tesoro restantes.
¿Dónde quiere dejar caer el siguiente dispositivo sonar? (0-59 0-14) (o ingrese salir)
**30 12**
             1         2         3         4         5
   012345678901234567890123456789012345678901234567890123456789

 0 ~~~~``````~```~~`~~~`~~~~~~~`~```````~```~`~````~```~~````~~ 0
 1 ~~~```~~~~```~~~`~~~~`~~`````~~``~~~```~`~~`~~```~`~~~``~~`~ 1
 2 ``~~~`~~``~~`~`~~~`~~~~~`~~```````~``~~~````~`~~~~~~````~~`~ 2
 3 ~``~```~``~`~`~``~```~`~`~~```~~`~~~~````~~``~`~`~```~~``~~~ 3
 4 ~~~`~~~~`~```~~~~~``~```~``~~~~``~~~``````~~`~~~`````~`~~~~~ 4
 5 ``~~`~``~`~`~`~`~~~~`~`~`~~~``X~~~~~`~```~`~~``~~``~~`~``~~` 5
 6 ~~~~~`~~~`~``~`~~~`~~`~~``~`~~~~``~~`````~~``~``~`~~`~`~~~`` 6
 7 ~`~`````~`~~`~~`~~~~``~````~~~`~~````~~````~`~~~~~```~`~~~~~ 7
 8 ``~~`~~~~```~`~~~``~~~~`~~~~``~~`~~~`~`~```~`~`~`~````~````` 8
 9 ~`~`~~~`````~`~`~~~~`~```~`~~`~~```````~``~`~```~````~`~~``~ 9
10 ```~~``~~``~~~`~~~~``~~~````~`~`~`~~`~~~`~~`~`~~`````~``~~~~ 10
11 ```~``~~~~```~~~``~~~~`````~`~~~~`~`~```~`~~~``````~`~``~~`~ 11
12 `~`~``~~`~``~`~`~~~~`~~`~~~~`~X~~~~~`~`~``~~~`````~~`~``~``~ 12
13 ~~`~~`~`~``~~`~``~``~~~~``~~`~```~~~``~``~~~~`~````~``~~~``~ 13
14 ~```````~~~````````~`~~`~``~`````~~~``~~~~~`~~```~~`~~``~~~~ 14

 012345678901234567890123456789012345678901234567890123456789
             1         2         3         4         5
El sonar no ha detectado nada. Todos los cofres de tesoro están fuera del alcance del dispositivo.
Usted tiene 18 dispositivo(s) de sonar restantes. 3 cofre(s) de tesoro restantes.
¿Dónde quiere dejar caer el siguiente dispositivo sonar? (0-59 0-14) (o ingrese salir)
**15 9**
             1         2         3         4         5
   012345678901234567890123456789012345678901234567890123456789

 0 ~~~~``````~```~~`~~~`~~~~~~~`~```````~```~`~````~```~~````~~ 0
 1 ~~~```~~~~```~~~`~~~~`~~`````~~``~~~```~`~~`~~```~`~~~``~~`~ 1
 2 ``~~~`~~``~~`~`~~~`~~~~~`~~```````~``~~~````~`~~~~~~````~~`~ 2
 3 ~``~```~``~`~`~``~```~`~`~~```~~`~~~~````~~``~`~`~```~~``~~~ 3
 4 ~~~`~~~~`~```~~~~~``~```~``~~~~``~~~``````~~`~~~`````~`~~~~~ 4
 5 ``~~`~``~`~`~`~`~~~~`~`~`~~~``X~~~~~`~```~`~~``~~``~~`~``~~` 5
 6 ~~~~~`~~~`~``~`~~~`~~`~~``~`~~~~``~~`````~~``~``~`~~`~`~~~`` 6
 7 ~`~`````~`~~`~~`~~~~``~````~~~`~~````~~````~`~~~~~```~`~~~~~ 7
 8 ``~~`~~~~```~`~~~``~~~~`~~~~``~~`~~~`~`~```~`~`~`~````~````` 8
 9 ~`~`~~~`````~`~3~~~~`~```~`~~`~~```````~``~`~```~````~`~~``~ 9
10 ```~~``~~``~~~`~~~~``~~~````~`~`~`~~`~~~`~~`~`~~`````~``~~~~ 10
11 ```~``~~~~```~~~``~~~~`````~`~~~~`~`~```~`~~~``````~`~``~~`~ 11
12 `~`~``~~`~``~`~`~~~~`~~`~~~~`~X~~~~~`~`~``~~~`````~~`~``~``~ 12
13 ~~`~~`~`~``~~`~``~``~~~~``~~`~```~~~``~``~~~~`~````~``~~~``~ 13
14 ~```````~~~````````~`~~`~``~`````~~~``~~~~~`~~```~~`~~``~~~~ 14

 012345678901234567890123456789012345678901234567890123456789
             1         2         3         4         5
Tesoro detectado a una distancia de 3 del dispositivo de sonar.
Usted tiene 17 dispositivo(s) de sonar restantes. 3 cofre(s) de tesoro restantes.
¿Dónde quiere dejar caer el siguiente dispositivo sonar? (0-59 0-14) (o ingrese salir)
**15 12**
             1         2         3         4         5
   012345678901234567890123456789012345678901234567890123456789

 0 ~~~~``````~```~~`~~~`~~~~~~~`~```````~```~`~````~```~~````~~ 0
 1 ~~~```~~~~```~~~`~~~~`~~`````~~``~~~```~`~~`~~```~`~~~``~~`~ 1
 2 ``~~~`~~``~~`~`~~~`~~~~~`~~```````~``~~~````~`~~~~~~````~~`~ 2
 3 ~``~```~``~`~`~``~```~`~`~~```~~`~~~~````~~``~`~`~```~~``~~~ 3
 4 ~~~`~~~~`~```~~~~~``~```~``~~~~``~~~``````~~`~~~`````~`~~~~~ 4
 5 ``~~`~``~`~`~`~`~~~~`~`~`~~~``X~~~~~`~```~`~~``~~``~~`~``~~` 5
 6 ~~~~~`~~~`~``~`~~~`~~`~~``~`~~~~``~~`````~~``~``~`~~`~`~~~`` 6
 7 ~`~`````~`~~`~~`~~~~``~````~~~`~~````~~````~`~~~~~```~`~~~~~ 7
 8 ``~~`~~~~```~`~~~``~~~~`~~~~``~~`~~~`~`~```~`~`~`~````~````` 8
 9 ~`~`~~~`````~`~3~~~~`~```~`~~`~~```````~``~`~```~````~`~~``~ 9
10 ```~~``~~``~~~`~~~~``~~~````~`~`~`~~`~~~`~~`~`~~`````~``~~~~ 10
11 ```~``~~~~```~~~``~~~~`````~`~~~~`~`~```~`~~~``````~`~``~~`~ 11
12 `~`~``~~`~``~`~1~~~~`~~`~~~~`~X~~~~~`~`~``~~~`````~~`~``~``~ 12
13 ~~`~~`~`~``~~`~``~``~~~~``~~`~```~~~``~``~~~~`~````~``~~~``~ 13
14 ~```````~~~````````~`~~`~``~`````~~~``~~~~~`~~```~~`~~``~~~~ 14

 012345678901234567890123456789012345678901234567890123456789
             1         2         3         4         5
Tesoro detectado a una distancia de 1 del dispositivo de sonar.
Usted tiene 16 dispositivo(s) de sonar restantes. 3 cofre(s) de tesoro restantes.
¿Dónde quiere dejar caer el siguiente dispositivo sonar? (0-59 0-14) (o ingrese salir)
**15 13**
             1         2         3         4         5
   012345678901234567890123456789012345678901234567890123456789

 0 ~~~~``````~```~~`~~~`~~~~~~~`~```````~```~`~````~```~~````~~ 0
 1 ~~~```~~~~```~~~`~~~~`~~`````~~``~~~```~`~~`~~```~`~~~``~~`~ 1
 2 ``~~~`~~``~~`~`~~~`~~~~~`~~```````~``~~~````~`~~~~~~````~~`~ 2
 3 ~``~```~``~`~`~``~```~`~`~~```~~`~~~~````~~``~`~`~```~~``~~~ 3
 4 ~~~`~~~~`~```~~~~~``~```~``~~~~``~~~``````~~`~~~`````~`~~~~~ 4
 5 ``~~`~``~`~`~`~`~~~~`~`~`~~~``X~~~~~`~```~`~~``~~``~~`~``~~` 5
 6 ~~~~~`~~~`~``~`~~~`~~`~~``~`~~~~``~~`````~~``~``~`~~`~`~~~`` 6
 7 ~`~`````~`~~`~~`~~~~``~````~~~`~~````~~````~`~~~~~```~`~~~~~ 7
 8 ``~~`~~~~```~`~~~``~~~~`~~~~``~~`~~~`~`~```~`~`~`~````~````` 8
 9 ~`~`~~~`````~`~3~~~~`~```~`~~`~~```````~``~`~```~````~`~~``~ 9
10 ```~~``~~``~~~`~~~~``~~~````~`~`~`~~`~~~`~~`~`~~`````~``~~~~ 10
11 ```~``~~~~```~~~``~~~~`````~`~~~~`~`~```~`~~~``````~`~``~~`~ 11
12 `~`~``~~`~``~`~1~~~~`~~`~~~~`~X~~~~~`~`~``~~~`````~~`~``~``~ 12
13 ~~`~~`~`~``~~`~1`~``~~~~``~~`~```~~~``~``~~~~`~````~``~~~``~ 13
14 ~```````~~~````````~`~~`~``~`````~~~``~~~~~`~~```~~`~~``~~~~ 14

 012345678901234567890123456789012345678901234567890123456789
             1         2         3         4         5
Tesoro detectado a una distancia de 1 del dispositivo de sonar.
Usted tiene 15 dispositivo(s) de sonar restantes. 3 cofre(s) de tesoro restantes.
¿Dónde quiere dejar caer el siguiente dispositivo sonar? (0-59 0-14) (o ingrese salir)
**16 12**
             1         2         3         4         5
   012345678901234567890123456789012345678901234567890123456789

 0 ~~~~``````~```~~`~~~`~~~~~~~`~```````~```~`~````~```~~````~~ 0
 1 ~~~```~~~~```~~~`~~~~`~~`````~~``~~~```~`~~`~~```~`~~~``~~`~ 1
 2 ``~~~`~~``~~`~`~~~`~~~~~`~~```````~``~~~````~`~~~~~~````~~`~ 2
 3 ~``~```~``~`~`~``~```~`~`~~```~~`~~~~````~~``~`~`~```~~``~~~ 3
 4 ~~~`~~~~`~```~~~~~``~```~``~~~~``~~~``````~~`~~~`````~`~~~~~ 4
 5 ``~~`~``~`~`~`~`~~~~`~`~`~~~``X~~~~~`~```~`~~``~~``~~`~``~~` 5
 6 ~~~~~`~~~`~``~`~~~`~~`~~``~`~~~~``~~`````~~``~``~`~~`~`~~~`` 6
 7 ~`~`````~`~~`~~`~~~~``~````~~~`~~````~~````~`~~~~~```~`~~~~~ 7
 8 ``~~`~~~~```~`~~~``~~~~`~~~~``~~`~~~`~`~```~`~`~`~````~````` 8
 9 ~`~`~~~`````~`~X~~~~`~```~`~~`~~```````~``~`~```~````~`~~``~ 9
10 ```~~``~~``~~~`~~~~``~~~````~`~`~`~~`~~~`~~`~`~~`````~``~~~~ 10
11 ```~``~~~~```~~~``~~~~`````~`~~~~`~`~```~`~~~``````~`~``~~`~ 11
12 `~`~``~~`~``~`~XX~~~`~~`~~~~`~X~~~~~`~`~``~~~`````~~`~``~``~ 12
13 ~~`~~`~`~``~~`~X`~``~~~~``~~`~```~~~``~``~~~~`~````~``~~~``~ 13
14 ~```````~~~````````~`~~`~``~`````~~~``~~~~~`~~```~~`~~``~~~~ 14

 012345678901234567890123456789012345678901234567890123456789
             1         2         3         4         5
¡Ha encontrado un cofre de tesoro hundido!
Usted tiene 14 dispositivo(s) de sonar restantes. 2 cofre(s) de tesoro restantes.
¿Dónde quiere dejar caer el siguiente dispositivo sonar? (0-59 0-14) (o ingrese salir)
--recortado--
~~~

## Código fuente para la Búsqueda del tesoro con sonar

Ingrese el siguiente código fuente en un nuevo archivo y guárdelo como *sonar.py*. Luego ejecútelo presionando F5 (o FN-F5 en OSX). Si usted obtiene errores después de ingresar este código, compare el código que usted digitó con el código del libro con la herramienta en línea diff en *https://www.nostarch.com/inventwithpython#diff*. 

![](https://inventwithpython.com/invent4thed/images/00020.jpeg)

*sonar.py*

~~~python
  1. # Búsqueda del tesoro con sonar
  2. 
  3. import random
  4. import sys
  5. import math
  6. 
  7. def obtenerNuevoTablero():
  8.     # Crea una nueva estructura de datos para un tablero de 60x15.
  9.     tablero = []
 10.     for x in range(60): # La lista principal es una lista de 60 listas.
 11.         tablero.append([])
 12.         for y in range(15): # Cada lista en la lista principal tiene 15 cadenas de un solo caracter.
 13.             # Usa diferentes caracteres para el oceáno para hacerlo más fácil de leer.
 14.             if random.randint(0, 1) == 0:
 15.                 tablero[x].append('~')
 16.             else:
 17.                 tablero[x].append('`')
 18.     return tablero
 19. 
 20. def dibujarTablero(tablero):
 21.     # Dibuja la estructura de datos del tablero
 22.     LineaDigitosDecenas = '    ' # Espacio inicial para los números a lo largo del lado izquierdo del tablero
 23.     for i in range(1, 6):
 24.         LineaDigitosDecenas += (' ' * 9) + str(i)
 25. 
 26.     # Imprime los númerosa lo largo del borde superior del tablero.
 27.     print(LineaDigitosDecenas)
 28.     print('   ' + ('0123456789' * 6))
 29.     print()
 30. 
 31.     # Imprimir cada una de las 15 líneas
 32.     for fila in range(15):
 33.         # Números de un solo dígito deben ser precedidos por un espacio extra
 34.         if fila < 10:
 35.             espacioExtra = ' '
 36.         else:
 37.             espacioExtra = ''
 38. 
 39.         # Crea la cadena para esta cadena en el tablero.
 40.         filaTablero = ''
 41.         for columna in range(60):
 42.             filaTablero += tablero[columna][fila]
 43. 
 44.         print('%s%s %s %s' % (espacioExtra, fila, filaTablero, fila))
 45. 
 46.     # Imprime los números a lo largo del borde inferior del tablero.
 47.     print()
 48.     print(' ' + ('0123456789' * 6))
 49.     print(LineaDigitosDecenas)
 50. 
 51. def obtenerCofresAleatorios(numCofres):
 52.     # Crea una lista de estructuras de datos de cofre (listas de dos elementos enteros con coordenadas x, y)
 53.     cofres = []
 54.     while len(cofres) < numCofres:
 55.         nuevoCofre = [random.randint(0, 59), random.randint(0, 14)]
 56.         if nuevoCofre not in cofres: # Asegúrese que el cofre no esté ya incluido ahí.
 57.             cofres.append(nuevoCofre)
 58.     return cofres
 59. 
 60. def estaEnTablero(x, y):
 61.     # Retorna verdadero (True) si las coordenadas están en el tablero; de lo contrario falso (False).
 62.     return x >= 0 and x <= 59 and y >= 0 and y <= 14
 63. 
 64. def realizarMovida(tablero, cofres, x, y):
 65.     # Cambia la estructura de datos tablero agregándole un caracter de dispositivo sonar. Elimina los cofres de la lista de cofres a medida que son encontrados.
 66.     # Retorna falso si este es un movimiento inválido.
 67.     # En caso contrario, retorna la cadena con el resultado de esta movida
 68.     menorDistancia = 100 # Cualquier cofre estará a una distancia menor que 100.
 69.     for cx, cy in cofres:
 70.         distancia = math.sqrt((cx - x) * (cx - x) + (cy - y) * (cy - y))
 71. 
 72.         if distancia < menorDistancia: # Queremos el cofre más cercano.
 73.             menorDistancia = distancia
 74. 
 75.     menorDistancia = round(menorDistancia)
 76. 
 77.     if menorDistancia == 0:
 78.         # ¡xy está directametne sobre un cofre!
 79.         cofres.remove([x, y])
 80.         return '¡Ha encontrado un cofre de tesoro hundido!'
 81.     else:
 82.         if menorDistancia < 10:
 83.             tablero[x][y] = str(menorDistancia)
 84.             return 'Tesoro detectado a una distancia de %s del dispositivo de sonar.' % (menorDistancia)
 85.         else:
 86.             tablero[x][y] = 'X'
 87.             return 'El sonar no ha detectado nada. Todos los cofres de tesoro están fuera del alcance del dispositivo.'
 88. 
 89. def ingresarMovidaJugadora(movidasPrevias):
 90.     # Permite a la jugadora ingresr su movida. Retorna una lista con dos elementos enteros con las coordenadas xy.
 91.     print('¿Dónde quiere dejar caer el siguiente dispositivo sonar? (0-59 0-14) (o ingrese salir)')
 92.     while True:
 93.         movida = input()
 94.         if movida.lower() == 'salir':
 95.             print('¡Gracias por jugar!')
 96.             sys.exit()
 97. 
 98.         movida = movida.split()
 99.         if len(movida) == 2 and movida[0].isdigit() and movida[1].isdigit() and estaEnTablero(int(movida[0]), int(movida[1])):
100.             if [int(movida[0]), int(movida[1])] in movidasPrevias:
101.                 print('Ya usted se movió ahí.')
102.                 continue
103.             return [int(movida[0]), int(movida[1])]
104. 
105.         print('Ingrese un número del 0 al 59, un espacio, luego un número del 0 al 14.')
106. 
107. def mostrarInstrucciones():
108.     print('''Instrucciones:
109. Usted es la capitana de El Simón, un buque cazador de tesoros. Su misión actual
110. es utilizar dispositivos de sonar para encontrar tres cofres con tesoros, hundidos en el
111. fondo del océano. Pero usted solo tiene sonares baratos que encuentran distancia, no dirección.
112. 
113. Ingrese las coordenadas para soltar un dispositivo de sonar. El mapa del océano será
114. marcado con cuán distante está el cofre más próximo, o una X si está más allá del alcance del
115. dispositivo de sonar. Por ejemplo las marcas C son donde están los cofres. El dispositivo de sonar
116. muestra un 3 porque el cofre más cercano está a 3 espacios.
117. 
118.                     1         2         3
119.           012345678901234567890123456789012
120. 
121.         0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
122.         1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
123.         2 `~`C``3`~~~~`C`~~~~`````~~``~~~`` 2
124.         3 ````````~~~`````~~~`~`````~`~``~` 3
125.         4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4
126. 
127.           012345678901234567890123456789012
128.                     1         2         3
129. (En el juego real, los cofres no serán visibles en el océano.)
130. 
131. Presione enter para continuar...''')
132.     input()
133. 
134.     print('''Cuando suelta un dispositivo de sonar directamente en un cofre, lo recoge y los otros
135.     dispositivos de sonar se actualizan para mostrar qué tan lejos está el siguiente cofre más cercano. Los cofres
136.     están más allá del alcance del dispositivo de sonar a la izquierda, por lo que muetra una X.
137. 
138.                     1         2         3
139.           012345678901234567890123456789012
140. 
141.         0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
142.         1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
143.         2 `~`X``7`~~~~`C`~~~~`````~~``~~~`` 2
144.         3 ````````~~~`````~~~`~`````~`~``~` 3
145.         4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4
146. 
147.           012345678901234567890123456789012
148.                     1         2         3
149. 
150. Los cofres de tesoro no se mueven. Los dispositivos de sonar pueden detectar cofres de
151. tesoro a una distancia de hasta 9 espacios. Intente recoger los 3 cofres antes de quedarse sin
152. dispositivos de sonar. ¡Buena suerte!
153. 
154. Presione enter para continuar...''')
155.     input()
156. 
157. 
158. 
159. print('S O N A R !')
160. print()
161. print('¿Le gustaría ver las instrucciones? (si/no)')
162. if input().lower().startswith('s'):
163.     mostrarInstrucciones()
164. 
165. while True:
166.     # Configuración del Juego
167.     dispositivosSonar = 20
168.     elTablero = obtenerNuevoTablero()
169.     losCofres = obtenerCofresAleatorios(3)
170.     dibujarTablero(elTablero)
171.     movidasPrevias = []
172. 
173.     while dispositivosSonar > 0:
174.         # Mostrar el estado de los dispositivos sonar y cofres
175.         print('Usted tiene %s dispositivo(s) de sonar restantes. %s cofre(s) de tesoro restantes.' % (dispositivosSonar, len(losCofres)))
176. 
177.         x, y = ingresarMovidaJugadora(movidasPrevias)
178.         movidasPrevias.append([x, y]) # debemos registrar todas las movidas para que los dispositivos sonar puedan ser actualizados.
179. 
180.         resultadoMovida = realizarMovida(elTablero, losCofres, x, y)
181.         if resultadoMovida == False:
182.             continue
183.         else:
184.             if resultadoMovida == '¡Ha encontrado un cofre de tesoro hundido!':
185.                 # Actualiza todos los dispositivos sonar presentes en el mapa
186.                 for x, y in movidasPrevias:
187.                     realizarMovida(elTablero, losCofres, x, y)
188.             dibujarTablero(elTablero)
189.             print(resultadoMovida)
190. 
191.         if len(losCofres) == 0:
192.             print('¡Ha encontrado todos los cofres del tesoro! ¡Felicitaciones y buena partida!')
193.             break
194. 
195.         dispositivosSonar -= 1
196. 
197.         if dispositivosSonar == 0:
198.             print('Nos hemos quedado sin dispositivos sonar! ¡Ahora tenemos que dar la vuelta y dirigirnos')
199.             print('de regreso a casa dejando tesoros en el mar! Juego terminado.')
200.             print('    Los cofres restantes estaban aquí:')
201.             for x, y in losCofres:
202.                 print('    %s, %s' % (x, y))
203. 
204. print('¿Quiere jugar de nuevo? (sí o no)')
205. if not input().lower().startswith('s'):
206.     sys.exit()
~~~

## Diseñando el programa

Antes de intentar comprender el código fuente, juegue el juego unas cuantas veces para aprender qué es lo que está ocurriendo. El juego de búsqueda del tesoro con sonar usa listas de listas y otras variables complicadas, llamadas *estructuras de datos*. Las estructuras de datos almacenan acomodos de valores para representar algo. Por ejemplo, en el capítulo 10, la estructura de datos de un tablero de Tres en línea era una lista de cadenas. La cadena representó una X, una O o un espacio vacío, y el índice de la cadena en la lista representó el espacio en el tablero. El juego de búsqueda del tesoro con sonar tendrá estructuras de datos similares para las ubicaciones de los tesoros y los dispositivos de sonar. 

## Importando el módulo random, sys y math

En el inicio del programa, importamos el módulo `random`, `sys` y `math`:

~~~Python
  1. # Búsqueda del tesoro con sonar
  2. 
  3. import random
  4. import sys
  5. import math
~~~

El módulo `sys` contiene la función `exit()`, la cual termina el programa inmediatamente. Ninguna de las líneas de código después de la llamada a `sys.exit()` correrá; el programa solo se detiene como si hubiera llegado al final. Esta función es usada más adelante en el programa.

El módulo `math` contiene la función `sqrt()`, que es usada para encontrar la raíz cuadrada de un número. La mate detrás de las raíces cuadradas es explicada en "Encontrando el cofre de tesoro más cercano" en la página 186.

## Creando un nuevo tablero de juego

El inicio de cada juego nuevo requiere de una nueva estructura de datos `tablero`, la cual es creada por `obtenerNuevoTablero()`. El tablero del juego de búsqueda del tesoro con sonar es un océano de arte ASCII con coordenadas X y Y alrededor. 

Cuando usamos la estructura de datos `tablero`, queremos poder acceder a su sistema de coordenadas en el mismo modo que accedemos a coordenadas Cartesianas. Para hacer eso, usaremos una lista de listas para llamar cada coordenada en el tablero como esto: `tablero[x][y]`. La coordenada X va primero que la coordenada Y, para obtener la cadena en la coordenada (26, 12), usted debe acceder a `tablero[26][12]` , no a `tablero[12][26]`.

~~~Python
  7. def obtenerNuevoTablero():
  8.     # Crea una nueva estructura de datos para un tablero de 60x15.
  9.     tablero = []
 10.     for x in range(60): # La lista principal es una lista de 60 listas.
 11.         tablero.append([])
 12.         for y in range(15): # Cada lista en la lista principal tiene 15 cadenas de un solo caracter.
 13.             # Usa diferentes caracteres para el oceáno para hacerlo más fácil de leer.
 14.             if random.randint(0, 1) == 0:
 15.                 tablero[x].append('~')
 16.             else:
 17.                 tablero[x].append('`')
~~~

La estructura de datos `tablero` es una lista de cadenas. La primera lista representa las coordenadas X. Dado que el tablero del juego es de 60 caracteres de ancho, la primera lista necesita contener 60 listas. En la línea 10, creamos un bucle `for` que añadirá 60 listas vacías a esta.

Pero `tablero` es más que una lista de 60 listas vacías. Cada una de las 60 listas representa una coordenada X del tablero de juego. Hay 15 filas en el tablero, así que cada una de estas 60 listas tiene que contener 15 cadenas. La línea 12 es otro bucle `for` para añadir 15 cadenas de un caracter que representan el océano. 

El océano será un puñado de cadenas `'~'` y  ``'`'``  seleccionadas aleatoriamente. Los caracteres de tilde ( ~ ) y el retroceso ( \` ), localizados cerca de la tecla ENTER en su teclado, serán usados para las olas del océano. Para determinar cuál caracter usar, las líneas 14 a 17 aplican esta lógica: si el valor de retorno de `random.randint()` es 0, añada la cadena `'~'`; en caso contrario, añada la cadena  ``'`'``. Esto le dará al océano una aleatoria apariencia chiva. 

Para un ejemplo más pequeño, si `tablero` se estableciera a ``[['~', '~', '`'], [['~', '~', '`'], [['~', '~', '`'], ['~', '`', '`'], ['`', '~', '`']]`` entonces el tablero que  dibujó se vería como este:

~~~ 
​~~~~`
​~~~`~
`````
~~~

Finalmente, la función retorna el valor en la variable `tablero` en la línea 18.

~~~Python
 18.     return tablero
~~~

## Dibujando el tablero de juego

A continuación definiremos el método `dibujarTablero()` que llamamos cuando queremos dibujar un nuevo tablero:

~~~Python
 20. def dibujarTablero(tablero):
~~~

El tablero de juego completo con coordenadas a lo largo de los bordes se observa como este:

~~~
             1         2         3         4         5
   012345678901234567890123456789012345678901234567890123456789
 0 ~~~`~``~~~``~~~~``~`~`~`~`~~`~~~`~~`~``````~~`~``~`~~```~`~` 0
 1 `~`~````~~``~`~```~```~```~`~~~``~~`~~~``````~`~``~~``~~`~~` 1
 2 ```~~~~`~`~~```~~~``~````~~`~`~~`~`~`~```~~`~``~~`~`~~~~~~`~ 2
 3 ~~~~`~~~``~```~``~~`~`~~`~`~~``~````~`~````~```~`~`~`~`````~ 3
 4 ~```~~~~~`~~````~~~~```~~~`~`~`~````~`~~`~`~~``~~`~``~`~``~~ 4
 5 `~```~`~`~~`~~~```~~``~``````~~``~`~`~~~~`~~``~~~~~~`~```~~` 5
 6 ``~~`~~`~``~`````~````~~``~`~~~~`~~```~~~``~`~`~~``~~~```~~~ 6
 7 ``~``~~~~~~```~`~```~~~``~`~``~`~~~~~~```````~~~`~~`~~`~~`~~ 7
 8 ~~`~`~~```~``~~``~~~``~~`~`~~`~`~```~```~~~```~~~~~~`~`~~~~` 8
 9 ```~``~`~~~`~~```~``~``~~~```~````~```~`~~`~~~~~`~``~~~~~``` 9
10 `~~~~```~`~````~`~`~~``~`~~~~`~``~``~```~~```````~`~``~````` 10
11 ~~`~`~~`~``~`~~~````````````````~~`````~`~~``~`~~~~`~~~`~~`~ 11
12 ~~`~~~~```~~~`````~~``~`~`~~``````~`~~``~```````~~``~~~`~~`~ 12
13 `~``````~~``~`~~~```~~~~```~~`~`~~~`~```````~~`~```~``~`~~~~ 13
14 ~~~``~```~`````~~`~`~``~~`~``~`~~`~`~``~`~``~~``~`~``~```~~~ 14
   012345678901234567890123456789012345678901234567890123456789
             1         2         3         4         5
~~~

El dibujado en la función `dibujarTablero()` tiene cuatro pasos:

1. Crear una variable cadena de la línea con 1, 2, 3, 4 y 5 espaciados ampliamente. Estos números marcan las coordenadas para 10, 20, 30, 40 y 50 en eje X.
2. Usar esa cadena para desplegar las coordenadas del eje X a través de la parte superior de la pantalla.
3. Imprimir cada fila del océano con las coordenadas del eje Y en ambos lados de la pantalla.
4. Imprimir el eje X otra vez en la parte inferior. Teniendo coordenadas en  todos los bordes hace más sencillo ver dónde colocar un dispositivo de sonar.

## Dibujando las coordenadas X a través de la parte superior del tablero

La primera parte de `dibujarTablero()` imprime el eje X en la parte superior del tablero. Debido a que quremos que cada parte del tablero sea par, cada etiqueta de coordenada puede tomar solo un espacio para un caracter. Cuando la numeración de las coordenadas alcanza 10, hay dos dígitos para cada número, así que ponemos los números en la posición de las decenas en una línea separada, como se muestra en la figura 13-3. El eje X está organizado de tal modo que la primera línea muestra la posición de los dígitos en las decenas y la segunda línea muestra los dígitos de las unidades.

![](/home/james/Jaqueando/inventar-con-python/images/00065.png)

*Figura 13-3: El espaciado usado para imprimir el tope del tablero de juego.*

Líneas 22 a 24 crean la cadena para la primera línea del tablero, la cual es la parte de las decenas del eje X:

~~~Python
 21.     # Dibuja la estructura de datos del tablero
 22.     lineaDigitosDecenas = '    ' # Espacio inicial para los números a lo largo del lado izquierdo del tablero
 23.     for i in range(1, 6):
 24.         lineaDigitosDecenas += (' ' * 9) + str(i)
~~~

Los números marcando las posiciones de las decenas en la primera línea todos llevan 9 espacios entre ellos, y hay 13 espacios adelante del 1. Las líneas 22 a 24 crean una cadena con esta línea y la almacenan en la variable nombrada `lineaDigitosDecenas`:

~~~Python
 26.     # Imprime los númerosa lo largo del borde superior del tablero.
 27.     print(lineaDigitosDecenas)
 28.     print('   ' + ('0123456789' * 6))
 29.     print()
~~~

Para imprimir los números a través del borde superior del tablero de juego, primero imprima el contenido de la variable `lineaDigitosDecenas`. Luego, en la siguiente línea, imprima tres espacios (de modo que esta fila se alinea correctamente), y luego imprima la cadena `'0123456789'` seis veces `('0123456789' * 6)`.

## Dibujando el océano

Las líneas 32 a 44 imprimen cada fila con las olas del océano, incluyendo los números a los lados para etiquetar el eje Y:

~~~Python
 31.     # Imprimir cada una de las 15 líneas
 32.     for fila in range(15):
 33.         # Números de un solo dígito deben ser precedidos por un espacio extra
 34.         if fila < 10:
 35.             espacioExtra = ' '
 36.         else:
 37.             espacioExtra = ''
~~~

El bucle `for` imprime las líneas 0 a 14, incluyendo los números de fila en ambos lados del tablero.

Pero tenemos el mismo problema de que tuvimos con el eje X. Los números con solo un dígito (como 0, 1, 2 y así sucesivamente) ocupan solo un espacio cuando se imprimen, pero los números de dos dígitos (como 10, 11 y 12) ocupan dos espacios. Las filas no se alinearán si las coordenadas tienen diferentes tamaños. El tablero se vería así:

~~~
8 ~~`~`~~```~``~~``~~~``~~`~`~~`~`~```~```~~~```~~~~~~`~`~~~~` 8
9 ```~``~`~~~`~~```~``~``~~~```~````~```~`~~`~~~~~`~``~~~~~``` 9
10 `~~~~```~`~````~`~`~~``~`~~~~`~``~``~```~~```````~`~``~````` 10
11 ~~`~`~~`~``~`~~~````````````````~~`````~`~~``~`~~~~`~~~`~~`~ 11
~~~

La solución es sencilla: añada un espacio adelante de todos los dígitos de un dígito. Las líneas 34 a 37 establecen la variable `espacioExtra`  ya sea con un espacio o una cadena vacía. La variable `espacioExtra` se imprime siempre, pero tiene un caracter de espacio solo para los números de fila de un único dígito. En caso contrario, es una cadena vacía. De esta forma, todas las columnas se alinearán cuando las imprima. 

## Imprimiendo una fila en el océano

El parámetro `tablero` es una estructura de datos para la totalidad de olas del océano. Las líneas 39 a 44 leen la variable `tablero` e imprimen una sola fila:

~~~Python
 39.         # Crea la cadena para esta cadena en el tablero.
 40.         filaTablero = ''
 41.         for columna in range(60):
 42.             filaTablero += tablero[columna][fila]
 43. 
 44.         print('%s%s %s %s' % (espacioExtra, fila, filaTablero, fila))
~~~

En la línea 40, `filaTablero` comienza como una cadena vacía. El bucle `for` en la línea 32 establece la variable `fila` para la fila actual del océano de olas a imprimir. Dentro del bucle de la línea 41 hay otro bucle `for` que itera sobre cada columna de la fila actual. Creamos `filaTablero` al concatenar `tablero[columna][fila]` en este bucle, lo cual significa concatenando `tablero[0][fila], tablero[1][fila], tablero[2][fila]`, y así sucesivamente hasta `tablero[59][fila]`. Esto es porque la fila contiene 60 caracteres, desde el índice 0 hasta el índice 59. 

El bucle `for` en la línea 41 itera sobre los enteros 0 a 59. En cada iteración, el siguiente caracter en la estructura de datos del tablero es copiado al final de `filaTablero`. Para el momento en el que el bucle esté finalizado, `filaTablero` tendrá la fila completa con olas de arte ASCII. La cadena en `filaTablero` es entonces impresa junto con el número de fila en la línea 44.

## Dibujando las coordenadas X a través de la parte inferior del tablero

Las líneas 46 a 49 son similares a las líneas 26 a 29:

~~~Python
 46.     # Imprime los números a lo largo del borde inferior del tablero.
 47.     print()
 48.     print(' ' + ('0123456789' * 6))
 49.     print(LineaDigitosDecenas)
~~~



Estas líneas imprimen las coordenadas X en la parte inferior del tablero.

## Creando los cofres de tesoro aleatoriamente

El juego decide aleatoriamente dónde están los cofres de tesoro. Los cofres de tesoro están representados como una lista de listas con dos enteros. Estos dos enteros son la coordenada X y la coordenada Y de un cofre. Por ejemplo, si la estructura de datos del cofre fuera `[[2, 2], [2, 4], [10, 0]]`, entonces esto significaría que habrían tres cofres de tesoro, uno en (2, 2), otro en (2, 4) y un tercero en (10,0).

La función `obtenerCofresAleatorios()` crea un cierto número de estructuras de datos de cofres en coordenadas asignadas aleatoriamente:

~~~Python
 51. def obtenerCofresAleatorios(numCofres):
 52.     # Crea una lista de estructuras de datos de cofre (listas de dos elementos enteros con coordenadas x, y)
 53.     cofres = []
 54.     while len(cofres) < numCofres:
 55.         nuevoCofre = [random.randint(0, 59), random.randint(0, 14)]
 56.         if nuevoCofre not in cofres: # Asegúrese que el cofre no esté ya incluido ahí.
 57.             cofres.append(nuevoCofre)
 58.     return cofres
~~~

El parámetro `numCofres` le dice a la función cuántos cofres de tesoro generar. El bucle `while` de la línea 54 iterará hasta que a todos los cofres se les haya asignado coordenadas. Dos números enteros aleatorios son seleccionados para las coordenadas en la línea 55. Las coordenadas X pueden estar en cualquier lugar entre 0 y 59, y las coordenadas Y puede estar en cualquier punto desde el 0 hasta el 14. La expresión `[random.randint(0, 59), random.randint(0, 14)]` evaluará a un valor de lista como `[2,2]` o `[2,4]` o `[10,0]`. Si estas coordenadas no existen en la lista de `cofres`, serán añadidas a `cofres` en la línea 57.

## Determinando si un movimiento es válido

Cuando la jugadora ingresa una coordenada X y Y para indicar donde ella quiere dejar caer un dispositivo de sonar, necesitamos estar seguros de que los números son válidos. Como se mencionó anteriormente, hay dos condiciones para que un movimiento sea válido: la coordenada X debe estar entre 0 y 59, y la coordenada Y debe estar entre 0 y 14.

La función `estaEnTablero()` usa una simple expresión con operadores `and` para combinar estas condiciones en una expresión y para asegurarse que cada parte de la expresión sea verdadera (`True`):

~~~Python
 60. def estaEnTablero(x, y):
 61.     # Retorna verdadero (True) si las coordenadas están en el tablero; de lo contrario falso (False).
 62.     return x >= 0 and x <= 59 and y >= 0 and y <= 14
~~~

Debido a que estamos usando el operador booleano  `and`, si alguno de las coordenadas es inválida, entonces la expresión completa evaluará a falso (`False`).

## Ubicando una movida en el tablero

En el juego de búsqueda del tesoro con sonar, el tablero de juego es actualizado para desplegar el número que representa la distancia del dispositivo de sonar al cofre de tesoro más cercano. Así cuando la jugadora hace una movida al darle al programa la coordenada X y Y, el tablero cambia a partir de las posiciones de los cofres de tesoro. 

~~~Python
 64. def realizarMovida(tablero, cofres, x, y):
 65.     # Cambia la estructura de datos tablero agregándole un caracter de dispositivo sonar. Elimina los cofres de la lista de cofres a medida que son encontrados.
 66.     # Retorna falso si este es un movimiento inválido.
 67.     # En caso contrario, retorna la cadena con el resultado de esta movida
~~~

La función `realizarMovida()` toma cuatro parámetros: la estructura de datos del tablero de juego, la estructura de datos de los cofres de tesoro, la coordenada X y la coordenada Y. La función `realizarMovida()` retornará un valor de cadena describiendo que pasó en respuesta al movimiento:

* Si la coordenada cae directamente sobre un cofre de tesoro, `realizarMovida()` retornará `'¡Ha encontrado un cofre de tesoro hundido!'`.
* Si la coordenada está en una distancia de 9 o menos de un cofre, `realizarMovida()` retornará `'Tesoro detectado a una distancia de %s del dispositivo de sonar.'` (donde % es reemplazado por la distancia entera).
* En caso contrario, `realizarMovida()` retornará `'El sonar no ha detectado nada. Todos los cofres de tesoro están fuera del alcance del dispositivo.'`.

Dadas las coordenadas de dónde la jugadora quiere dejar caer el dispositivo de sonar y una lista de coordenadas X y Y para los cofres de tesoro, usted necesitará un algoritmo para descubrir cuál cofre de tesoro está más cerca.

### Encontrando el cofre de tesoro más cercano

Las líneas 68 a 75 son el algoritmo para determinar cuál cofre de tesoro está más cerca del dispositivo de sonar. 

~~~Python
 68.     menorDistancia = 100 # Cualquier cofre estará a una distancia menor que 100.
 69.     for cx, cy in cofres:
 70.         distancia = math.sqrt((cx - x) * (cx - x) + (cy - y) * (cy - y))
 71. 
 72.         if distancia < menorDistancia: # Queremos el cofre más cercano.
 73.             menorDistancia = distancia
~~~

Los parámetros `x` y `y` son enteros (digamos `3` y `5`), y juntos representan la ubicación en el tablero de juego donde la jugadora adivinó. La variable `cofres` tendrá un valor como `[[5, 0], [0, 2], [4, 2]]`, que representa la ubicación de los tres cofres de tesoro. La Figura 13-4 ilustra este valor.

Para encontrar la distancia entre el dispositivo de sonar y el cofre de tesoro, necesitaremos hacer alguna matemática para encontrar la distancia entre dos coordenadas X y Y. Digamos que ubicamos el dispositivo de sonar en (3,5) y que queremos encontrar la distancia al cofre de tesoro en (4, 2).

![](https://inventwithpython.com/invent4thed/images/00077.jpeg)

*Figura 13-4: El cofre de tesoro representado por ` [[5, 0], [0, 2], [4, 2]]`.*

Para encontrar la distancia entre dos conjuntos de coordenadas X y Y, usaremos el *teorema de Pitágoras*. Este teorema aplica para *triángulos rectos*, triángulos en los que un ángulo es de 90 grados, el mismo tipo de ángulo que usted encuentra en un rectángulo. El teorema de Pitágoras dice que el lado diagonal del triángulo puede ser calculado a partir de los largos de los lados horizontal y vertical. La Figura 13-5 muestra un triángulo recto dibujado entre el dispositivo de sonar en (3,5) y el cofre de tesoro en (4,2).

![](https://inventwithpython.com/invent4thed/images/00088.jpeg)

*Figura 13-5: El tablero con un triángulo recto dibujado sobre el dispositivo de sonar y el cofre de tesoro.*

 El teorema de Pitágoras es *a² + b² = c²*, en donde *a* es el largo del lado horizontal, *b* es el largo del lado vertical, y *c* es el largo del lado diagonal, o la *hipotenusa*. Estos largos son *al cuadrado*, lo cual quiere decir que el número es multiplicado por sí mismo. "Descuadrar" un número se llama a encontrar la *raíz cuadrada* del  número, como haremos para obtener *c* de *c²*.

Usemos el teorema de Pitágoras para encontrar la distancia entre el dispositivo de sonar en (3,5) y el cofre de tesoro (4,2):

1. Para encontrar *a*, reste la segunda coordenada X, 4, de la primera coordenada X, 3: `3 - 4 = -1`. 
2. Para encontrar *a²*, multiplique *a* por *a*: `-1 x -1= 1`.  (Un número negativo por un número negativo es siempre un número positivo.)
3. Para encontrar *b*, reste la segunda coordenada Y, 2, de la primera coordenada Y, 5: `5 - 2 = 3`.
4. Para encontrar *b²*, multiplique *b* por *b*: `3 x 3 = 9`.
5. Para encontrar *c²*, sume *a²* y *b²*: `1 + 9 = 10`.
6. Para encontrar *c* desde *c²*, usted tiene que encontrar la raíz cuadrada de *c²*.

El módulo `math` que importamos en la línea 5 tiene una función de raíz cuadrada llamada `sqrt()`. Ingrese lo siguiente en la «shell» interactiva:

~~~Python
>>> import math
>>> math.sqrt(10)
3.1622776601683795
>>> 3.1622776601683795 * 3.1622776601683795
10.000000000000002
~~~

Note que multiplicar una raíz cuadrada por sí misma produce el cuadrado del número. (El `2` extra al final del `10` es por una inesquivable ligera imprecisión en la función `sqrt()`.)

Al pasar *c²* a `sqrt()`, podemos adivinar que el dispositivo de sonar está a 3,16 unidades de distancia del cofre del tesoro. El juego lo redondeará hacia abajo a 3.

Veamos las líneas 68 a 70 de nuevo:

~~~Python
 68.     menorDistancia = 100 # Cualquier cofre estará a una distancia menor que 100.
 69.     for cx, cy in cofres:
 70.         distancia = math.sqrt((cx - x) * (cx - x) + (cy - y) * (cy - y))
~~~

El código dentro del bucle `for` de la línea 69 calcula la distancia para cada cofre. La línea 68 da a `menorDistancia` la imposible larga distancia de 100 al inicio del bucle de modo que por lo menos uno de los cofres de tesoro que usted encontrará será puesto en `menorDistancia` in la línea 73. Como `cx -x` representa la distancia horizontal *a* entre el cofre y el dispositivo sonar, `(cx - x) * (cx - x)` es la *a²* de nuestro cálculo del teorema de Pitágoras. Este es sumado a `cy - y) * (cy - y)`, el *b²*. Esta suma es *c²* y es pasado a `sqrt()` para obtener la distancia entre el cofre y el dispositivo de sonar.

Queremos encontrar la distancia entre el dispositivo de sonar y el cofre más cercano, así que si esta distancia es menor que la distancia menos, esta será guardada como la nueva distancia menor en la línea 73:

~~~Python
 72.         if distancia < menorDistancia: # Queremos el cofre más cercano.
 73.             menorDistancia = distancia
~~~

Para el momento en el que el bucle `for` haya finalizado, usted sabrá que `distanciaMenor` contiene la distancia más cercana entre el dispositivo sonar y todos los cofres de tesoro en el juego.

### Eliminando valores con el método de lista `remove()`

El método de lista `remove()` remueve la primera ocurrencia de un valor que calce con el que se le haya pasado como argumento. Por ejemplo, ingrese lo siguiente en la «shell» interactiva:

~~~Python
>>> x = [42, 5, 10, 42, 15, 42]
>>> x.remove(10)
>>> x
[42, 5, 42, 15, 42]
~~~

El valor `10` se ha removido de la la lista `x`. 

Ahora ingrese lo siguiente en la «shell» interactiva:

~~~Python
>>> x = [42, 5, 10, 42, 15, 42]
>>> x.remove(42)
>>> x
[5, 10, 42, 15, 42]
~~~

Note que solo el primer valor `42` fue removido y el segundo y tercero siguen ahí. El método `remove()` remueve la primera, y solo la primera, ocurrencia del valor que usted le pase. 

Si usted intenta remover un valor que no está en la lista, obtendrá un error:

~~~Python
>>> x = [5, 42]
>>> x.remove(10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
~~~

Como el método `append()`, el método `remove()` es llamado en una lista y no retorna una lista (`list`).  Usted querrá utilizar código como `x.remove(42)`, no `x = x.remove(42)`.

Volvamos a encontrar las distancias entre el dispositivo de sonar y los cofres de tesoro en el juego. La única vez que la `menorDistancia` es igual a 0 es cuando las coordenadas X y Y del dispositivo de sonar son las mismas que las coordenadas X y Y del cofre de tesoro. Esto quiere decir que la jugadora ha adivinado correctamente la ubicación de un cofre de tesoro.

~~~Python
 77.     if menorDistancia == 0:
 78.         # ¡xy está directametne sobre un cofre!
 79.         cofres.remove([x, y])
 80.         return '¡Ha encontrado un cofre de tesoro hundido!'
~~~

Cuando esto ocurre, el programa remueve esta lista de dos enteros de la estructura de datos `cofres` con el método `remove()` de `list` . Luego la función retorna `'¡Ha encontrado un cofre de tesoro hundido!'`.

Pero si la `menorDistancia` no es `0`, la jugadora no adivinó la ubicación exacta de un cofre de tesoro, y el bloque `else` comenzando en la línea 81 se ejecuta:

~~~Python
 81.     else:
 82.         if menorDistancia < 10:
 83.             tablero[x][y] = str(menorDistancia)
 84.             return 'Tesoro detectado a una distancia de %s del dispositivo de sonar.' % (menorDistancia)
 85.         else:
 86.             tablero[x][y] = 'X'
 87.             return 'El sonar no ha detectado nada. Todos los cofres de tesoro están fuera del alcance del dispositivo.'
~~~

Si la distancia del dispositivo de sonar al cofre de tesoro es menor de 10, la línea 83 marca el tablero con la versión cadena de `menorDistancia`. Si no, el tablero es marcado con una `'X'`. De esta forma, la jugadora sabe qué tan cerca está cada dispositivo de sonar del cofre del tesoro. Si la jugadora ve un 0, sabrá que está bastante largo. 

## Obteniendo la movida de la jugadora

La función `ingresarMovidaJugadora()` recolecta la coordenada X y Y del siguiente movimiento de la jugadora:

~~~Python
 89. def ingresarMovidaJugadora(movidasPrevias):
 90.     # Permite a la jugadora ingresr su movida. Retorna una lista con dos elementos enteros con las coordenadas xy.
 91.     print('¿Dónde quiere dejar caer el siguiente dispositivo sonar? (0-59 0-14) (o ingrese salir)')
 92.     while True:
 93.         movida = input()
 94.         if movida.lower() == 'salir':
 95.             print('¡Gracias por jugar!')
 96.             sys.exit()
~~~

El parámetro `movidasPrevias` es una lista de dos enteros de los lugares donde previamente la jugadora puso un dispositivo de sonar. Esta información será usada de modo que la jugadora no coloque otro dispositivo de sonar donde ya ha dejado uno.

El bucle `while` se mantendrá preguntando a la jugadora por su siguiente movida hasta que ingrese coordenadas para un lugar donde no haya ya un dispositivo de sonar. La jugadora puede también ingresar `'salir'` para salir del juego. En ese caso, la línea 96 llama la función `sys.exit()` para terminar el programa inmediatamente. 

Asumiendo que la jugadora no ha ingresado `salir`, el código comprueba que la entrada sea dos enteros separados por un espacio. La línea 98 llama al método `split()` en `movida` como el nuevo valor de `movida`:

~~~Python
 98.         movida = movida.split()
 99.         if len(movida) == 2 and movida[0].isdigit() and movida[1].isdigit() and estaEnTablero(int(movida[0]), int(movida[1])):
100.             if [int(movida[0]), int(movida[1])] in movidasPrevias:
101.                 print('Ya usted se movió ahí.')
102.                 continue
103.             return [int(movida[0]), int(movida[1])]
104. 
105.         print('Ingrese un número del 0 al 59, un espacio, luego un número del 0 al 14.')
~~~

Si la jugadora ingresa un valor como `'1 2 3'`, entonces la lista retornada por `split()` será `['1', '2', '3']`. En ese caso, la expresión `len(movida) == 2` será `False` (la lista en `movida` debería ser sólo de dos números porque representa una coordenada), y la expresión completa sería evaluada inmediatamente a `False`. Python no comprueba el resto de la expresión debido a la evaluación en corto circuito (que fue descrita en " Evaluación de corto circuito", en la página 139).

Si el largo de la lista es `2`, entonces los dos valores estarán en el índice `movida[0]` y `movida[1]`. Para comprobar si esos valores son dígitos numéricos (como `'2'` o `'17'`), usted puede usar una función como `sonSoloDigitos()` de "Comprobando si una cadena tiene solo números" en la página 158. Pero Python ya tiene un método que hace esto.

El método de cadena `isdigit()` retorna `True` si la cadena consiste únicamente de números. En caso contrario, retorna `False`. Ingrese lo siguiente en la «shell» interactiva:

~~~Python
>>> '42'.isdigit()
True
>>> 'forty'.isdigit()
False
>>> ''.isdigit()
False
>>> 'hello'.isdigit()
False
>>> x = '10'
>>> x.isdigit()
True
~~~

Ambos `movida[0].isdigit()`y `movida[1].isdigit()` deben ser `True`para que la condición completa sea `True`. La parte final en la condición de la línea 99 llama a la función `estaEnTablero()` para comprobar si la coordenada X y Y existe en el tablero.

Si la condición completa es `True`, la línea 100 comprueba si la movida existe en la lista `movidasPrevias`. Si existe, entonces el sentencia `continue` de la línea 102 causa que la ejecución regrese al inicio del bucle `while` en la línea 92 y luego pregunte a la jugadora por una movida de nuevo. Si no existe, la línea 103 retorna una lista de dos enteros con las coordenadas X y Y.

## Imprimiendo las instrucciones del juego para la jugadora

La función `mostrarInstrucciones()` son un par de llamadas a `print()` que imprimen cadenas de múltiples líneas:

~~~Python
107. def mostrarInstrucciones():
108.     print('''Instrucciones:
109. Usted es la capitana de El Simón, un buque cazador de tesoros. Su misión actual
--recortado--
154. Presione enter para continuar...''')
155.     input()
~~~

La función `input()` le da el chance a la jugadora de presionar ENTER antes de imprimir la siguiente cadena. Esto es porque la ventana del IDLE solo puede mostrar un poco de texto a la vez, y no queremos que la jugadora tenga que desplazarse hacia arriba para leer el inicio del texto. Después que la jugadora presiona ENTER, la función retorna a la línea que llamó a la función. 

## El ciclo de juego

Ahora que hemos ingresado todas las funciones que nuestro programa tendrá, ingresemos la parte principal del juego. La primera cosa que la jugadora ve después de correr el programa es el título del juego impreso por la línea 159. Esta es la parte principal del programa, la cual comienza al ofrecerle a la jugadora instrucciones y luego configurando las variables que el juego utilizará.

~~~Python
159. print('S O N A R !')
160. print()
161. print('¿Le gustaría ver las instrucciones? (si/no)')
162. if input().lower().startswith('s'):
163.     mostrarInstrucciones()
164. 
165. while True:
166.     # Configuración del Juego
167.     dispositivosSonar = 20
168.     elTablero = obtenerNuevoTablero()
169.     losCofres = obtenerCofresAleatorios(3)
170.     dibujarTablero(elTablero)
171.     movidasPrevias = []
~~~

La expresión `input.lower().startswith('s')` le permite a la jugadora solicitar las instrucciones, y esta evalúa a `True` si la jugadora ingresa una cadena que comienza con `'s'` o `'S'`. Por Ejemplo (la letra 's' es cambiada por una 'y' en la imagen de ejemplo):

![](https://inventwithpython.com/invent4thed/images/00099.jpeg)

Si la condición es `True`, `mostrarInstrucciones()` es llamado en la línea 163. En caso contrario, el juego comienza. Varias variables son establecidas y configuradas en las líneas 167 a 171; estas son descritas en la Tabla 13-1.

**Tabla 13-1:** *Variables usadas en el ciclo principal del juego.*

| Variable            | descripción                                                  |
| ------------------- | ------------------------------------------------------------ |
| `dispositivosSonar` | El número de dispositivos de sonar (y turnos) que la jugadora tiene restantes. |
| `elTablero`         | La estructura de datos del tablero utilizada para este juego. |
| `losCofres`         | La lista de estructuras de datos de cofres. `obtenerCofresAleatorios()` retorna una lista de tres cofres de tesoro localizadas aleatoriamente en el tablero. |
| `movidasPrevias`    | Una lista de todas las movidas X y Y que la jugadora ha hecho en el juego. |

Vamos a utilizar estas variables pronto, así que ¡Asegúrese de revisas sus descripciones antes de avanzar!

### Mostrando el estado del juego para la jugadora

El bucle `while` de la línea 173 se ejecuta mientras la jugadora tenga dispositivos de sonar restantes e imprime un mensaje indicándole cuantos dispositivos de sonar y cofres de tesoros le restan:

~~~Python
173.     while dispositivosSonar > 0:
174.         # Mostrar el estado de los dispositivos sonar y cofres
175.         print('Usted tiene %s dispositivo(s) de sonar restantes. %s cofre(s) de tesoro restantes.' % (dispositivosSonar, len(losCofres)))
~~~

Después de imprimir cuantos dispositivos quedan, el bucle `while` continúa su ejecución.

### Manejando la movida de la jugadora

La línea 177 es también parte del bucle `while` y usa asignación múltiple para asignar a las variables `x` y `y` la lista de dos elementos representando las coordenadas de la movida de la jugadora, retornada por `ingresarMovidaJugadora()`. Le pasaremos las `movidasPrevias`  de modo que el código de `ingresarMovidaJugadora()` se pueda asegurar que la jugadora no está repitiendo una jugada previa.

~~~Python
177.         x, y = ingresarMovidaJugadora(movidasPrevias)
178.         movidasPrevias.append([x, y]) # debemos registrar todas las movidas para que los dispositivos sonar puedan ser actualizados.
179. 
180.         resultadoMovida = realizarMovida(elTablero, losCofres, x, y)
181.         if resultadoMovida == False:
182.             continue
~~~

Las variables `x` y `y` son luego añadidas al final de la lista `jugadasPrevias`. La variable `jugadasPrevias` es una lista de coordenadas X y Y con cada movimiento que la jugadora haga en este juego. Esta lista es usada luego en el programa en las líneas 177 y 186.

Las variables `x`, `y`, `elTablero` y `losCofres` son todas pasadas a la función `realizarMovida()` en la línea 180. Esta función hace las modificaciones necesarias para colorar un dispositivo de sonar en el tablero.

Si `realizarMovida()` retorna `False`, entonces hubo un problema con los valores de  `x` y `y ` pasados. El sentencia `continue` envía la ejecución atrás al inicio del bucle `while` en la línea 173 para preguntar a la jugadora por las coordenadas X y Y de nuevo.

### Encontrando un cofre de tesoro hundido

Si `realizarMovida()` no retorna `False`, retorna una cadena con el resultado de esa movida. Si esa cadena es `'¡Ha encontrado un cofre de tesoro hundido!'`, entonces todos los dispositivos de sonar en el tablero deberían ser actualizados para detectar el siguiente cofre más cercano en el tablero:

~~~Python
183.         else:
184.             if resultadoMovida == '¡Ha encontrado un cofre de tesoro hundido!':
185.                 # Actualiza todos los dispositivos sonar presentes en el mapa
186.                 for x, y in movidasPrevias:
187.                     realizarMovida(elTablero, losCofres, x, y)
188.             dibujarTablero(elTablero)
189.             print(resultadoMovida)
~~~

Las coordenadas X y Y de todos los dispositivos de sonar están en `movidasPrevias`. Iterando sobre `movidasPrevias`en la línea 186, usted podrá pasar todas las coordenadas X y Y a la función `realizarMovida()`de nuevo para redibujar los valores en el tablero. Debido a que el programa no imprime ningún texto nuevo acá, la jugadora no se da cuenta que el programa está rehaciendo todas las movidas previas. Solo parece que el tablero se actualiza por sí mismo. 

### Comprobando si la jugadora ganó

Recuerde que la función `realizarMovida()` modifica la lista de `losCofres` que usted le envió. Debido a que `losCofres ` es una lista, cualquier cambio que se haga dentro de la función, persistirá después de que la función retorne de la ejecución. La función `realizarMovida()` remueve elementos de `losCofres` cuando los cofres de tesoro son encontrados, así eventualmente (si la jugadora se mantiene adivinando correctamente) todos los cofres de tesoro habrán sido removidos. (Recuerde, por "cofre de tesoro" queremos decir una lista de dos elementos de las coordenadas X y Y dentro de la lista `losCofres`.)

~~~Python
191.         if len(losCofres) == 0:
192.             print('¡Ha encontrado todos los cofres del tesoro! ¡Felicitaciones y buena partida!')
193.             break
~~~

Cuando todos los cofres de tesoro han sido encontrados en el tablero y removidos de `losCofres`, la lista `losCofres` tiene un largo de `0`. Cuando eso ocurre, el código despliega un mensaje de felicitaciones a la jugadora y luego ejecuta un sentencia `break` para romper y salir del bucle `while`. La ejecución luego continuará en la línea 197, la primera línea luego del bloque `while`.

### Comprobando si la jugadora perdió

La linea 195 es la última línea del bucle `while` que inició en la línea 173.

~~~Python
195.         dispositivosSonar -= 1
~~~

El programa decrementa la variable `dispositivosSonar` porque la jugadora ha usado uno de los dispositivos de sonar. Si la jugadora se mantiene fallando la ubicación de los cofres de tesoro, eventualmente `dispositivosSonar` será reducida a 0. Después de esta línea, la ejecución salta de nuevo a la línea 173 de modo que pueda reevaluar la condición de la sentencia `while` (la cual es `dispositivosSonar > 0`).

Si `dispositivosSonar` es `0`, entonces la condición será `False` y la ejecución continuará fuera del bloque `while ` en la línea 197. Pero hasta entonces, la condición se mantendrá `True` y la jugadora se podrá mantenerse adivinando:

~~~Python
197.         if dispositivosSonar == 0:
198.             print('Nos hemos quedado sin dispositivos sonar! ¡Ahora tenemos que dar la vuelta y dirigirnos')
199.             print('de regreso a casa dejando tesoros en el mar! Juego terminado.')
200.             print('    Los cofres restantes estaban aquí:')
201.             for x, y in losCofres:
202.                 print('    %s, %s' % (x, y))
~~~

La línea 197 es la primera línea fuera del bucle `while`. Cuando la ejecución llega a este punto, el juego ha terminado. Si `dispositivosSonar` es `0`, usted sabe que la jugadora se ha quedado sin dispositivos sonar antes de encontrar todos los cofres y perdió.

Las líneas 198 a 200 le dirán a la jugadora que ha perdido. El bucle `for` en la línea 201 irá por los cofres de tesoro restantes en `losCofres` y desplegará su ubicación para que la jugadora pueda ver dónde estaban los cofres de tesoro que buscaba.

### Terminando el programa con la función `sys.exit()`

Gane o pierda, el programa le permitirá a la jugadora decidir si quiere mantenerse jugando. Si la jugadora no ingresa "si" o "S" o ingresa otra cadena que no inicie con la letra *s*, entonces `not input().lower().startswith('s')` evaluará a `True` y la función `sys.exit()` es ejecutada. Esto causa que el programa termine. 

~~~Python
204. print('¿Quiere jugar de nuevo? (sí o no)')
205. if not input().lower().startswith('s'):
206.     sys.exit()
~~~

De otro modo, la ejecución saltará de nuevo al inicio del bucle `while` en la línea 165 y un nuevo juego comienza.

## Resumen

¿Recuerda cómo nuestro juego de Tres en línea numeró los espacios en el tablero de Tres en línea del 1 al 9? Este tipo de sistema de coordenadas podría estar bien para un tablero con menos de 10 espacios. ¡Pero el tablero de la búsqueda del tesoro con sonar tiene 900 espacios! El sistema de coordenadas Cartesianas sobre el que aprendimos en el capítulo 12 realmente hace que todos esos espacios sean manejables, especialmente cuando nuestro juego necesita encontrar la distancia entre dos puntos en el tablero.

Las ubicaciones en juegos que usan sistemas de coordenadas Cartesianas pueden ser almacenadas en una lista de listas en las cuales el primer índice es la coordenada X y el segundo índice es la coordenada Y. Esto hace más sencillo de acceder a una coordenada usando `tablero[x][y]`.

Estas estructuras de datos (como las que usted usó para el océano y las ubicaciones de los cofres de tesoro) hacen posible representar conceptos complejos como datos, y sus programas de juegos se convierten mayoritariamente en modificar estas estructuras de datos. 

En el siguiente capítulo, vamos a representar letras como números. Al representar texto como número, debemos llevar a cabo operaciones matemáticas en ellos para encriptar o desencriptar mensajes secretos. 

[Previo: Capítulo 10: Panecillos ](capitulo10.md) | [Siguiente: Capítulo 14: Código del César ](capitulo14.md)