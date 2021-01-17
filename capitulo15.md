# 15 Reversi

![Imagen de ciencia](https://inventwithpython.com/invent4thed/images/00016.jpeg)

En este capítulo, haremos un juego de Reversi, también conocido como Othello. Este juego de tablero para dos jugadoras es jugado en una cuadrícula, así que usaremos un sistema de coordenadas Cartesianas con coordenadas X y Y. Nuestra versión del juego tendrá una IA de computadora que es más avanzada que nuestra IA del Tres en línea del capítulo 10. De hecho, esta IA es tan buena que muy probablemente le ganará en casi todas las partidas que juegue. (¡Yo he perdido todas las veces que jugué contra ella!).

---

Temas cubiertos en este capítulo:

* Cómo jugar Reversi
* La función `bool()`
* Simulando movimientos en un tablero de Reversi
* Programando la IA de Reversi

---



## Cómo jugar Reversi

Reversi tiene un tablero de 8x8 y fichas que son negras a un lado y blancas en el otro (nuestro juego utilizará símbolos O y X en cambio). El tablero inicial se ve como en la Figura 15-1.

![](https://inventwithpython.com/invent4thed/images/00015.jpeg)

*Figura 15-1: El tablero inicial de Reversi tiene dos fichas blancas y dos fichas negras.*

Dos jugadoras intercambian turnos colocando fichas del color que han elegido --negro o blanco-- en el tablero. Cuando una jugadora coloca una ficha en el tablero, cualquiera de las fichas de la oponente que esté entre la ficha recién colocada y las otras del color de la jugadora serán volteadas.  Por ejemplo, cuando la jugadora blanca coloca una nueva ficha en el espacio (5, 6) , como se muestra en la Figura 15-2, la ficha negra en (5, 5) está entre dos fichas blancas, así que se volteará a color blanco, como en la Figura 15-3. El objetivo del juego es terminar como más fichas de su color que las del color de la oponente.

![](https://inventwithpython.com/invent4thed/images/00024.jpeg)

*Figura 15-2 La jugadora blanca coloca una nueva ficha.*



![](https://inventwithpython.com/invent4thed/images/00034.jpeg)

*Figura 15-3: El movimiento de la blanca ha causado que una de las fichas negras se voltee.*

La negra podría efectuar un movimiento similar a continuación, colocando una ficha negra en (4, 6), el cual voltearía la ficha blanda en (4, 5). Esto resulta en un tablero que se mira como el de la Figura 15-4.

![](https://inventwithpython.com/invent4thed/images/00044.jpeg)

*Figura 15-4: La negra ha colocado una nueva ficha, convirtiendo una de las fichas blancas.*



Las fichas en todas las direcciones son volteadas siempre y cuando estén entre la nueva ficha de la jugadora y una ficha existente de ese color. En la Figura 15-5, la blanca coloca una ficha en (3, 6) y voltea de vuelta fichas en dos direcciones (marcadas por las líneas). El resultado se muestra en la Figura 15-6.

Cada jugadora puede rápidamente voltear muchas fichas en el tablero en uno o dos movimientos. Las jugadoras deben siempre realizar movimientos que les permita voltear al menos una ficha. El juego termina cuando ninguna jugadora pueda realizar un movimiento o el tablero esté completamente lleno. La jugadora con más fichas de su color gana.

![](https://inventwithpython.com/invent4thed/images/00054.jpeg)

*Figura 15-5: El segundo movimiento de la blanca en (3, 6) convertirá dos fichas de la negra.*



![](https://inventwithpython.com/invent4thed/images/00063.jpeg)

*Figura 15-6: El tablero después del segundo movimiento de la blanca.*

La IA que haremos para este juego mirará cualquier movimiento que pueda realizar en una esquina del tablero. Si no hay movimientos disponibles en las esquinas del tablero, la computadora seleccionará el movimiento que le genere la mayor cantidad de fichas.



## Una ejecución de ejemplo de Reversi



Esto es lo que la jugadora ve cuando ella ejecuta el programa Reversi. El texto que ingresa la jugadora se muestra entre asteriscos. 

~~~Python
¡Bienvenida a Reversi!
¿Desea ser las fichas X o O?
**x**
Las fichas de la jugadora comenzarán.
  12345678
 +--------+
1|        |1
2|        |2
3|        |3
4|   XO   |4
5|   OX   |5
6|        |6
7|        |7
8|        |8
 +--------+
  12345678
Usted: 2 puntos. Computadora: 2 puntos.
Ingrese su jugada, "salir" para finalizar el juego, o "pistas" para activar/desactivar las pistas.
**53**
  12345678
 +--------+
1|        |1
2|        |2
3|    X   |3
4|   XX   |4
5|   OX   |5
6|        |6
7|        |7
8|        |8
 +--------+
  12345678
Usted: 4 puntos. Computadora: 1 puntos.
Presione ENTER para ver la jugada de la computadora.
---recortado---
  12345678
 +--------+
1|OOOOOOOO|1
2|XXXXXOXX|2
3|XXXOOOXX|3
4|XOOOXOOX|4
5|XOOXOOOX|5
6|XOXXXOXX|6
7|XOOOOOXX|7
8|XOOOOOOO|8
 +--------+
  12345678
X obtuvo 28 puntos. O obtuvo 36 puntos.
Usted perdió. La computadora la venció por 8 puntos.
¿Quiere jugar de nuevo? (si o no)
**no**
~~~



Como usted puede ver, la IA es muy buena en vencerme, 36 a 28. Para ayudar a la jugadora, programaremos el juego para que brinde pistas. La jugadora podrá ingresar `pista` como su movimiento, lo cual activará y desactivará el modo de pistas. Cuando el modo pistas está activado, todos los posibles movimientos que la jugadora puede realizar se mostrarán en el tablero como puntos (.), como así:

~~~Python
  12345678
 +--------+
1|        |1
2|        |2
3|        |3
4|   XO.  |4
5|   OO   |5
6|   .O.  |6
7|        |7
8|        |8
 +--------+
  12345678
~~~



Como usted puede ver, la jugadora se puede mover en (4, 2), (5, 3), (4, 6), o (6, 6) basándose en las pistas que se muestra en el tablero. 



## Código fuente para Reversi

Reversi es un mamut de programa comparado con nuestro juegos previos. ¡Es casi de 300 líneas de largo!. Pero no se preocupe: muchas de estas son comentarios o líneas en blanco para acomodar el código y hacerlo mas legible. 

![](https://inventwithpython.com/invent4thed/images/00020.jpeg)



Como con nuestros otros programas, primero crearemos varias funciones para llevar a cabo tareas relacionadas con el Reversi, que serán invocadas por la sección principal. Aproximadamente las primeras 250 líneas de código son estas funciones auxiliares, y las últimas 30 líneas de código implementan el juego de Reversi en sí mismo. 

Si usted obtiene errores después de ingresar este código, compárelo con el del libro con la herramienta diff en línea disponible en: https://www.nostarch.com/inventwithpython#diff.

*reversi.py*

~~~Python
  1. # Reversi: un clone de Othello/Reversegam
  2. import random
  3. import sys
  4. ANCHO = 8 # El tablero tiene 8 espacios de ancho.
  5. ALTO = 8 # El tablero tiene 8 espacios de alto.
  6. def dibujarTablero(tablero):
  7.     # Imprime el tablero pasado a esta función. Retorna None.
  8.     print('  12345678')
  9.     print(' +--------+')
 10.     for y in range(ALTO):
 11.         print('%s|' % (y+1), end='')
 12.         for x in range(ANCHO):
 13.             print(tablero[x][y], end='')
 14.         print('|%s' % (y+1))
 15.     print(' +--------+')
 16.     print('  12345678')
 17. 
 18. def obtenerNuevoTablero():
 19.     # Crea un nuevo tablero, una estructura de datos de tablero vacío.
 20.     tablero = []
 21.     for i in range(ANCHO):
 22.         tablero.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
 23.     return tablero
 24. 
 25. def esJugadaVálida(tablero, ficha, iniciox, inicioy):
 26.     # Retorna False si la jugada de la jugadora en iniciox, inicioy es inválida.
 27.     # Si es una jugada válida, retorna una lista de espacios que pasarían a ser de la jugadora si moviera ahí.
 28.     if tablero[iniciox][inicioy] != ' ' or not estáEnTablero(iniciox, inicioy):
 29.         return False
 30. 
 31.     if ficha == 'X':
 32.         otraFicha = 'O'
 33.     else:
 34.         otraFicha = 'X'
 35. 
 36.     fichasAVoltear = []
 37.     for direcciónx, direccióny in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
 38.         x, y = iniciox, inicioy
 39.         x += direcciónx # Primer paso en la dirección x
 40.         y += direccióny # Primer paso en la dirección y
 41.         while estáEnTablero(x, y) and tablero[x][y] == otraFicha:
 42.             # Se mantienen moviendose en esa dirección x & y.
 43.             x += direcciónx
 44.             y += direccióny
 45.             if estáEnTablero(x, y) and tablero[x][y] == ficha:
 46.                 # Hay fichas para voltear. Vaya en la dirección opuesta hasta que alcance el espacio original, registrando todas las fichas en el camino.
 47.                 while True:
 48.                     x -= direcciónx
 49.                     y -= direccióny
 50.                     if x == iniciox and y == inicioy:
 51.                         break
 52.                     fichasAVoltear.append([x, y])
 53. 
 54.     if len(fichasAVoltear) == 0: # Si no se voltearon fichas, este no es un movimiento válido.
 55.         return False
 56.     return fichasAVoltear
 57. 
 58. def estáEnTablero(x, y):
 59.     # Devuelve True si las coordenadas se encuentran dentro del tablero.
 60.     return x >= 0 and x <= ANCHO - 1 and y >= 0 and y <= ALTO - 1
 61. 
 62. def obtenerTableroConJugadasVálidas(tablero, ficha):
 63.     # Retorna un nuevo tablero con puntos marcando las movidas válidas que la jugadora puede realizar.
 64.     copiaDeTablero = obtenerCopiaTablero(tablero)
 65. 
 66.     for x, y in obtenerJugadasVálidas(copiaDeTablero, ficha):
 67.         copiaDeTablero[x][y] = '.'
 68.     return copiaDeTablero
 69. 
 70. def obtenerJugadasVálidas(tablero, ficha):
 71.     # Retorna una lista de listas [x,y] de jugadas válidas para la jugadora y tablero dades.
 72.     jugadasVálidas = []
 73.     for x in range(ANCHO):
 74.         for y in range(ALTO):
 75.             if esJugadaVálida(tablero, ficha, x, y) != False:
 76.                 jugadasVálidas.append([x, y])
 77.     return jugadasVálidas
 78. 
 79. def obtenerPuntajeTablero(tablero):
 80.     # Determina el puntaje contando las fichsa. Retorna un diccionario con las llaves 'X' y 'O'.
 81.     puntajex = 0
 82.     puntajeo = 0
 83.     for x in range(ANCHO):
 84.         for y in range(ALTO):
 85.             if tablero[x][y] == 'X':
 86.                 puntajex += 1
 87.             if tablero[x][y] == 'O':
 88.                 puntajeo += 1
 89.     return {'X':puntajex, 'O':puntajeo}
 90. 
 91. def ingresarFichaDeJugadora():
 92.     # Permite a la juadora elegir qué ficha quiere mover.
 93.     # Retorna una lista con la ficha de la jugadora como primer elemento y la de la computadora como segundo.
 94.     ficha = ''
 95.     while not (ficha == 'X' or ficha == 'O'):
 96.         print('¿Desea ser las fichas X o O?')
 97.         ficha = input().upper()
 98. 
 99.     # El primer elemento en la lista es la ficha de la jugadora, el segundo elemento es la de la computadora.
100.     if ficha == 'X':
101.         return ['X', 'O']
102.     else:
103.         return ['O', 'X']
104. 
105. def quiénComienza():
106.     # Al azar elige qué jugadora inicia.
107.     if random.randint(0, 1) == 0:
108.         return 'computadora'
109.     else:
110.         return 'jugadora'
111. 
112. def hacerJugada(tablero, ficha, iniciox, inicioy):
113.     # Coloca la ficha sobre el tablero en iniciox, inicioy y convierte cualquier ficha de la oponente.
114.     # Retorna False si esta movida es inválida; True si es válida.
115.     fichasAVoltear = esJugadaVálida(tablero, ficha, iniciox, inicioy)
116. 
117.     if fichasAVoltear == False:
118.         return False
119. 
120.     tablero[iniciox][inicioy] = ficha
121.     for x, y in fichasAVoltear:
122.         tablero[x][y] = ficha
123.     return True
124. 
125. def obtenerCopiaTablero(tablero):
126.     # Crea un duplicado de la lista del tablero y la retorna.
127.     copiaDeTablero = obtenerNuevoTablero()
128. 
129.     for x in range(ANCHO):
130.         for y in range(ALTO):
131.             copiaDeTablero[x][y] = tablero[x][y]
132. 
133.     return copiaDeTablero
134. 
135. def esEsquina(x, y):
136.     # Retorna True si la posición está en una de las cuatro esquinas.
137.     return (x == 0 or x == ANCHO - 1) and (y == 0 or y == ALTO - 1)
138. 
139. def obtenerJugadaJugadora(tablero, fichaJugadora):
140.     # Permite a la jugadora ingresar su movimiento.
141.     # Retorna la movida como [x, y] (o retorna la cadena 'pistas' o 'salir').
142.     CIFRAS1A8 = '1 2 3 4 5 6 7 8'.split()
143.     while True:
144.         print('Ingrese su jugada, "salir" para finalizar el juego, o "pistas" para activar/desactivar las pistas.')
145.         movida = input().lower()
146.         if movida == 'salir' or movida == 'pistas':
147.             return movida
148. 
149.         if len(movida) == 2 and movida[0] in CIFRAS1A8 and movida[1] in CIFRAS1A8:
150.             x = int(movida[0]) - 1
151.             y = int(movida[1]) - 1
152.             if esJugadaVálida(tablero, fichaJugadora, x, y) == False:
153.                 continue
154.             else:
155.                 break
156.         else:
157.             print('Esa no es una jugada válida. Ingrese la columna (1-8) y luego la fila (1-8).')
158.             print('Por ejemplo, 81 coresponde a la esquina superior derecha.')
159. 
160.     return [x, y]
161. 
162. def obtenerJugadaComputadora(tablero, fichaComputadora):
163.     # Dado un tbalero y una ficha de la computadora, determina dónde
164.     # jugar y retorna la movida como una lista [x, y].
165.     movidasPosibles = obtenerJugadasVálidas(tablero, fichaComputadora)
166.     random.shuffle(movidasPosibles) # Ordena al azar el orden de las jugadras posibles.
167. 
168.     # Siempre juega en una esquna si está disponible.
169.     for x, y in movidasPosibles:
170.         if esEsquina(x, y):
171.             return [x, y]
172. 
173.     # Busca la movida de mayor puntaje posible.
174.     mejorPuntaje = -1
175.     for x, y in movidasPosibles:
176.         copiaDeTablero = obtenerCopiaTablero(tablero)
177.         hacerJugada(copiaDeTablero, fichaComputadora, x, y)
178.         puntaje = obtenerPuntajeTablero(copiaDeTablero)[fichaComputadora]
179.         if puntaje > mejorPuntaje:
180.             mejorJugada = [x, y]
181.             mejorPuntaje = puntaje
182.     return mejorJugada
183. 
184. def mostrarPuntajes(tablero, fichaJugadora, fichaComputadora):
185.     puntajes = obtenerPuntajeTablero(tablero)
186.     print('Usted: %s puntos. Computadora: %s puntos.' % (puntajes[fichaJugadora], puntajes[fichaComputadora]))
187. 
188. def jugarJuego(fichaJugadora, fichaComputadora):
189.     mostrarPistas = False
190.     turno = quiénComienza()
191.     print('Las fichas de la ' + turno + ' comenzarán.')
192. 
193.     # Limpia el tablero y coloca la piezas iniciales.
194.     tablero = obtenerNuevoTablero()
195.     tablero[3][3] = 'X'
196.     tablero[3][4] = 'O'
197.     tablero[4][3] = 'O'
198.     tablero[4][4] = 'X'
199. 
200.     while True:
201.         jugadasVálidasJugadora = obtenerJugadasVálidas(tablero, fichaJugadora)
202.         jugadasVálidasComputadora = obtenerJugadasVálidas(tablero, fichaComputadora)
203. 
204.         if jugadasVálidasJugadora == [] and jugadasVálidasComputadora == []:
205.             return tablero # Nadie se puede mover, así que el juego terminará.
206. 
207.         elif turno == 'jugadora': # Turno de la jugadora
208.             if jugadasVálidasJugadora != []:
209.                 if mostrarPistas:
210.                     tableroJugadasVálida = obtenerTableroConJugadasVálidas(tablero, fichaJugadora)
211.                     dibujarTablero(tableroJugadasVálida)
212.                 else:
213.                     dibujarTablero(tablero)
214.                 mostrarPuntajes(tablero, fichaJugadora, fichaComputadora)
215. 
216.                 movida = obtenerJugadaJugadora(tablero, fichaJugadora)
217.                 if movida == 'salir':
218.                     print('¡Gracias por jugar!')
219.                     sys.exit() # Termina el programa.
220.                 elif movida == 'pistas':
221.                     mostrarPistas = not mostrarPistas
222.                     continue
223.                 else:
224.                     hacerJugada(tablero, fichaJugadora, movida[0], movida[1])
225.             turno = 'computadora'
226. 
227.         elif turno == 'computadora': # turno de la computadora
228.             if jugadasVálidasComputadora != []:
229.                 dibujarTablero(tablero)
230.                 mostrarPuntajes(tablero, fichaJugadora, fichaComputadora)
231. 
232.                 input('Presione ENTER para ver la jugada de la computadora.')
233.                 movida = obtenerJugadaComputadora(tablero, fichaComputadora)
234.                 hacerJugada(tablero, fichaComputadora, movida[0], movida[1])
235.             turno = 'jugadora'
236. 
237. 
238. 
239. print('¡Bienvenida a Reversi!')
240. 
241. fichaJugadora, fichaComputadora = ingresarFichaDeJugadora()
242. 
243. while True:
244.     tableroFinal = jugarJuego(fichaJugadora, fichaComputadora)
245. 
246.     # Muestra el puntaje final.
247.     dibujarTablero(tableroFinal)
248.     puntajes = obtenerPuntajeTablero(tableroFinal)
249.     print('X obtuvo %s puntos. O obtuvo %s puntos.' % (puntajes['X'], puntajes['O']))
250.     if puntajes[fichaJugadora] > puntajes[fichaComputadora]:
251.         print('¡Usted venció la computadora por %s puntos! ¡Felicidades!' % (puntajes[fichaJugadora] - puntajes[fichaComputadora]))
252.     elif puntajes[fichaJugadora] < puntajes[fichaComputadora]:
253.         print('Usted perdió. La computadora la venció por %s puntos.' % (puntajes[fichaComputadora] - puntajes[fichaJugadora]))
254.     else:
255.         print('¡El juego finalizó empatado!')
256. 
257.     print('¿Quiere jugar de nuevo? (si o no)')
258.     if not input().lower().startswith('s'):
259.         break
~~~



## Importando módulos y estableciendo constantes

Como con nuestros otros juegos, comenzamos este programa importando módulo:

~~~Python
  1. # Reversi: un clone de Othello/Reversegam
  2. import random
  3. import sys
  4. ANCHO = 8 # El tablero tiene 8 espacios de ancho.
  5. ALTO = 8 # El tablero tiene 8 espacios de alto.
~~~

La línea 2 importa el módulo `random` por sus funciones `randint()` y `choice()`. La línea 3 importa el módulo `sys` por su función `exit()`.

Las líneas 4 y 5 establecen dos constantes, `ANCHO`y `ALTO`, las cuales son usadas para establecer el tablero de juego. 



## La estructura de datos del tablero de juego

Descubramos la estructura de datos del tablero. Esta estructura de datos es una lista de listas, justo como la del juego del capítulo 13 la Búsqueda del tesoro con sonar.  La lista de listas es creada de modo que `tablero[x][y]` representará el caracter en el espacio localizado en la posición `x` en el eje X (de izquierda a derecha) y la posición `y` en el eje Y (de arriba a abajo).

Este caracter puede ser un `' '` (un espacio representando una posición vacía), un `'.'` (un punto representando un posible movimiento en modo pistas), o una `'X'` o `'O'` (letras representando fichas). Cuando usted vea un parámetro llamado `tablero`, se refiere a este tipo de estructura de datos de lista de listas. 

Es importante hacer la nota de que mientras las coordenadas X y Y para el tablero de juego se mantengan entre 1 y 8, lo índices de la estructura de datos lista se mantendrán entre 0 y 7. Nuestro código necesitará algunos ajustes pequeños para conseguir esto. 

### Dibujando la estructura de datos del tablero en la pantalla

La estructura de datos del tablero es un valor de lista de Python, pero necesitamos una manera más tuanis de presentarla en la pantalla. La función `dibujarTablero()` toma una estructura de datos de tablero y la despliega en pantalla para que la jugadora sepa dónde están ubicadas las fichas:

~~~Python
  6. def dibujarTablero(tablero):
  7.     # Imprime el tablero pasado a esta función. Retorna None.
  8.     print('  12345678')
  9.     print(' +--------+')
 10.     for y in range(ALTO):
 11.         print('%s|' % (y+1), end='')
 12.         for x in range(ANCHO):
 13.             print(tablero[x][y], end='')
 14.         print('|%s' % (y+1))
 15.     print(' +--------+')
 16.     print('  12345678')
~~~

La función `dibujarTablero()` imprime el tablero de juego actual basado en la estructura de datos en `tablero`.

La línea 8 es ejecutada la primera llamada a la función `print()` para cada tablero, y esta imprime las etiquetas para los ejes X a lo largo de la parte superior del tablero. La línea 9 imprime la línea superior horizontal del tablero. El ciclo `for` en la línea 10 se enciclará ocho veces, una por cada fila. La línea 11 imprime la etiqueta para el eje Y en la parte izquierda del tablero, y esta tiene un argumento de palabra clave `end=''` para no imprimir nada en vez de una línea nueva.

Esto es así porque otro ciclo en la línea 12 (el cual también se encicla ocho veces, una para cada columna en la fila) imprime cada posición a lo largo con una X, O, . o espacio en blanco dependiendo de qué esté almacenado en `tablero[x][y]`. En la línea 13, la llamada a la función `print()` dentro de este ciclo también tiene un argumento de palabra clave `end=''` para que el caracter de cambio de línea no se imprima. Esto producirá una única línea en la pantalla que se verá como `'1|XXXXXXXX|1'` (si cada valor de `tablero[x][y]` es una 'X').

Después de finalizar la ejecución del ciclo interno, la función `print()` es llamada en las líneas 15 y 16 para imprimir la línea horizontal inferior y las etiquetas del eje X.

Cuando el ciclo `for` en la línea 13 imprime la columna ocho veces, este forma el tablero completo:

~~~Python
  12345678
 +--------+
1|XXXXXXXX|1
2|XXXXXXXX|2
3|XXXXXXXX|3
4|XXXXXXXX|4
5|XXXXXXXX|5
6|XXXXXXXX|6
7|XXXXXXXX|7
8|XXXXXXXX|8
 +--------+
  12345678
~~~

Por supuesto, en vez de X, algunos espacios del tablero podrían ser la otra marca de la jugadora (O), un punto (.) si el modo pistas está encendido, o un espacio en blanco para posiciones vacías.

### Creando una nueva estructura de datos

La función `obtenerTablero()` desplegará una estructura de datos de tablero en la pantalla, pero también necesitamos una forma de crear estas estructuras de datos. La función `obtenerNuevoTablero()` retorna una lista de ocho listas, con cada lista conteniendo ocho cadenas `' '` que representarán un tablero vacío sin movimientos:

~~~Python
 18. def obtenerNuevoTablero():
 19.     # Crea un nuevo tablero, una estructura de datos de tablero vacío.
 20.     tablero = []
 21.     for i in range(ANCHO):
 22.         tablero.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
 23.     return tablero
~~~

La línea 20 crea la lista que contienen las listas internas. El ciclo `for` añade ocho listas internas a esta lista. Estas listas internas tienen ocho cadenas para representar ocho espacios vacíos en el tablero. En conjunto, este código crea un tablero con 64 espacios vacíos -- un tablero vacío de Reversi.



## Comprobando si un movimiento es válido

Dada la estructura de datos del tablero, la ficha de la jugadora y las coordenadas X y Y para la movida de la jugadora, la función `esJugadaVálida()` debería retornar `True`si las reglas del juego Reversi permiten un movimiento a esas coordenadas, y `Falso` si no lo permiten. Para que un movimiento sea válido, este debe estar en el tablero y además voltear al menos una de las fichas de la oponente. 

Esta función utiliza varias coordenadas X y Y en el tablero, así las variables `iniciox` e `inicioy` mantienen el rastro de las coordenadas X y Y de la movida original. 

~~~Python
 25. def esJugadaVálida(tablero, ficha, iniciox, inicioy):
 26.     # Retorna False si la jugada de la jugadora en iniciox, inicioy es inválida.
 27.     # Si es una jugada válida, retorna una lista de espacios que pasarían a ser de la jugadora si moviera ahí.
 28.     if tablero[iniciox][inicioy] != ' ' or not estáEnTablero(iniciox, inicioy):
 29.         return False
 30. 
 31.     if ficha == 'X':
 32.         otraFicha = 'O'
 33.     else:
 34.         otraFicha = 'X'
 35. 
 36.     fichasAVoltear = []
~~~

La línea 28 comprueba si las coordenadas X y Y está en el tablero de juego y si el espacio está vacío utilizando la función `estáEnTablero()` (la cual definiremos más adelante en este programa). Esta función se asegura que ambas coordinadas X y Y estén entre 0 y el `ANCHO` o `ALTO` del tablero menos 1.

La ficha de la jugadora (ya sea jugadora humana o la computadora jugando) está en`ficha`, pero esta función necesitará saber con qué ficha juega la oponente. Si la ficha de la jugadora es X, entonces obviamente la ficha de la jugadora es O, y viceversa. Usamos el enunciado `if-else` en las líneas 31 a 34 para esto. 

Finalmente, si las coordenadas X y Y dadas representan un movimiento válido, `esJugadaVálida()` retorna una lista de todas las fichas de la oponente que serán volteadas por este movimiento. Nosotros creamos una lista vacía nueva, `fichasAVoltear`, que usaremos para almacenar todas las coordenadas de las fichas. 

### Comprobando cada una de las ocho direcciones

Para que un movimiento sea válido, necesita voltear al menos una de ficha de la oponente por medio de encerrar la nueva ficha de la jugadora actual con una de las fichas viejas de la jugadora. Esto significa que la nueva ficha debe estar próxima a una de las fichas de la oponente. 

El ciclo ` for`en la línea 37 itera a través de una lista de listas que representan las direcciones que el programa compruebará para las fichas de oponente:

~~~Python
 37.     for direcciónx, direccióny in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
~~~

El tablero de juego es un sistema de coordenadas Cartesianas con direcciones X y Y. Hay ocho direcciones a comprobar: arriba, abajo, izquierda, derecha y las cuatro direcciones diagonales. Cada una de las listas de dos elementos en la línea 37 es usada para comprobar una de estas direcciones. El programa revisa una dirección sumando al primer valor en la lista de dos elementos a la coordenada X y el segundo valor a la coordenada Y.

Debido a que las coordenadas X aumentan conforme usted va a la derecha, usted puede comprobar la dirección derecha al sumarle 1 a la coordenada X. Así a la lista `[1, 0]` le suma 1 a la coordenada X y 0 a la coordenada Y. Comprobar la dirección izquierda es lo opuesto: usted debe restar 1 (eso es sumar -1) de la coordenada X.

Pero para comprobar en diagonal, usted necesita sumar o restar de ambas coordenadas. Por ejemplo, sumando 1 a la coordenada X y sumando -1 a la coordenada Y resultaría en comprobar la dirección de la diagonal arriba a la derecha. 

La Figura 15-7 muestra un diagrama que hace más sencillo recordar cuál lista de dos elementos representa cuál dirección.


![](https://inventwithpython.com/invent4thed/images/00074.jpeg)

*Figura 15-7: Cada lista de dos elementos representa una de las ocho direcciones.*

El ciclo `for` en la línea 37 itera a través de cada una de las listas de dos elementos de modo que cada dirección es comprobada. Dentro del ciclo `for`, las variables `x` y `y` son establecidas a los mismos valores de `iniciox` e `inicioy`, respectivamente, usando asignación múltiple en la línea 38. Las variables `direccionx` y `direcciony` son establecidas con los valores en una de las listas de dos elementos y cambian las variables `x` y `y` correspondientemente a la dirección que está siendo comprobada en esa iteración del ciclo `for`:

~~~Python
 37.     for direcciónx, direccióny in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
 38.         x, y = iniciox, inicioy
 39.         x += direcciónx # Primer paso en la dirección x
 40.         y += direccióny # Primer paso en la dirección y
~~~

Las variables `iniciox` e `inicioy` se mantendrán iguales para que el programa pueda recordar de qué espacio inició.

Recuerde, para que un movimiento sea válido, este debe estar a la vez en el tablero y contiguo a una ficha de la otra jugadora. (De lo contrario,  no hay ninguna ficha de la oponente para voltear, y un movimiento debe voltear al menos una ficha para ser válido.) La línea 41 comprueba esta condición, y si esta no es `True`, la ejecución regresa al enunciado `for`para comprobar la siguiente dirección.

~~~Python
 41.         while estáEnTablero(x, y) and tablero[x][y] == otraFicha:
 42.             # Se mantienen moviendose en esa dirección x & y.
 43.             x += direcciónx
 44.             y += direccióny
~~~

Pero si el primer espacio comprobado si tiene una ficha de la oponente, entonces el programa debe comprobar si hay más fichas de la oponente en esa dirección hasta que llegue a una ficha de la jugadora o al final del tablero. La siguiente ficha en la misma dirección es comprobada usando `direccionx` y `direcciony` de nuevo para hacer de X y Y las siguientes coordenadas a comprobar. Así el programa cambia X y Y en las líneas 43 y 44.

### Encontrando si hay fichas a voltear

Luego, comprobamos si hay fichas adyacentes que pueden ser volteadas.

~~~Python
 45.             if estáEnTablero(x, y) and tablero[x][y] == ficha:
 46.                 # Hay fichas para voltear. Vaya en la dirección opuesta hasta que alcance el espacio original, registrando todas las fichas en el camino.
 47.                 while True:
 48.                     x -= direcciónx
 49.                     y -= direccióny
 50.                     if x == iniciox and y == inicioy:
 51.                         break
 52.                     fichasAVoltear.append([x, y])

~~~

El enunciado `if` en la línea 45 comprueba si una coordenada está ocupada por una ficha de la propia jugadora. Esta ficha marcará el final del encierro realizado por las fichas de la jugadora encerrando las fichas de la oponente. También tenemos que registrar las coordenadas de todas las fichas de la oponente que deben ser volteadas.

El ciclo `while`mueve `x` y `y`en reversa en la línea 48 y 49. Hasta que `x`y `y`estén de vuelta en las posiciones original `inciox` e `inicioy`, `direccionx`y `direcciony`son restadas de `x`y `y`, y cada posición `x` y `y` es añadida a la lista `fichasAVoltear`. Cuando `x` y `y`hallan alcanzado la posición `iniciox`e `inicioy`, la línea 51 romperá la ejecución para salir del ciclo. Como la posición original `iniciox` e `inicioy` son un espacio vacío (nos aseguramos que este era el caso en las líneas 28 y 29), la condición del ciclo `while`en la línea 41 será `False`. El programa se moverá a la línea 37, y el ciclo `for`comprueba la siguiente dirección. 

El ciclo `for` hace todo esto en todas las ocho direcciones. Después que este ciclo está finalizado, la lista `fichasAVoltear`contendrá las coordenadas X y Y de todas las fichas de nuestra oponente que serán volteadas si la jugadora se mueve a `inciox`e `inicioy`. Recuerde, la función `esMovidaVálida()` está solo comprobando si el movimiento original es válido;  no está haciendo el cambio permanente en la estructura de datos del tablero de juego. 

Si ninguna de las ocho direcciones termina volteando al menos una dicha de la oponente, entonces `fichasAVoltear`será una lista vacía:

~~~Python
 54.     if len(fichasAVoltear) == 0: # Si no se voltearon fichas, este no es un movimiento válido.
 55.         return False
 56.     return fichasAVoltear
~~~

Esto es un signo de que este movimiento no es válido y `esMovidaVálida()`debe retornar `False`. En otro caso, `esMovidaVálida()`retorna `fichasAVoltear`.

## Comprobando coordenadas válidas

La función `estáEnTablero()`es llamada desde `esMovidaVálida()`. Esta simplemente comprueba si unas coordenadas X y Y dadas está en el tablero. Por ejemplo, una coordenada X de 4 y una coordenada Y de 9999 no estará en el tablero dado que las coordenadas Y solo llegan hasta 7, lo cual es igual que `ANCHO -1` o `ALTO - 1`.

~~~Python
 58. def estáEnTablero(x, y):
 59.     # Devuelve True si las coordenadas se encuentran dentro del tablero.
 60.     return x >= 0 and x <= ANCHO - 1 and y >= 0 and y <= ALTO - 1
~~~

Llamar esta función es un atajo para la expresión booleana en la línea 27 que comprueba si ambas X y Y está entre 0 y el `ANCHO`o `ALTO` restado por 1, lo cual es 7. 

### Obteniendo una lista con todas las movidas válidas

Ahora creemos en modo pistas que muestre un tablero con todas las movidas posibles marcadas en él. La función `obtenerTableroConJugadasVálidas()` retorna una estructura de datos de tablero de juego que tienen puntos (.) en todos los espacios que son movidas válidas:

~~~Python
 62. def obtenerTableroConJugadasVálidas(tablero, ficha):
 63.     # Retorna un nuevo tablero con puntos marcando las movidas válidas que la jugadora puede realizar.
 64.     copiaDeTablero = obtenerCopiaTablero(tablero)
 65. 
 66.     for x, y in obtenerJugadasVálidas(copiaDeTablero, ficha):
 67.         copiaDeTablero[x][y] = '.'
 68.     return copiaDeTablero
~~~

Esta función crea un duplicado de la estructura de datos del juego `tablero` llamada `copiaDeTablero` (retornada por `obtenerCopiaTablero()`en la línea 64) en vez de modificar la que es pasada en el parámetro `tablero`. La línea 66 llama a `obtenerJugadasVálidas()` para obtener una lista de las coordenadas X y Y con todos los movimientos legales que una jugadora puede realizar. La copia del tablero es marcada con puntos en esos espacios y retornada. 

La función `obtenerJugadasVálidas` retorna una lista de listas de dos elementos. Las listas de dos elementos tienen las coordenadas X y Y para todos los movimientos válidos para una `ficha`dada para la estructura de datos de tablero pasada como parámetro `tablero`:

~~~Python
 70. def obtenerJugadasVálidas(tablero, ficha):
 71.     # Retorna una lista de listas [x,y] de jugadas válidas para la jugadora y tablero dades.
 72.     jugadasVálidas = []
 73.     for x in range(ANCHO):
 74.         for y in range(ALTO):
 75.             if esJugadaVálida(tablero, ficha, x, y) != False:
 76.                 jugadasVálidas.append([x, y])
 77.     return jugadasVálidas
~~~

Esta función usa ciclos anidados (en líneas 73 y 74) para comprobar si cada coordenada X y Y (las 64) llamado `esJugadaVálida()` en ese espacio y comprobando si retorna `False` o una lista de posibles movidas (en ese caso la movida es válida). Cada coordenada X y Y válida es añadida a la lista en `jugadasVálidas`.


### Llamando la función `bool()`

Usted habrá notado que el programa comproba si `esJugadaVálida()`en la línea 75 retorna `False` aún cuando esta función retorna una lista. Para entender cómo funciona esto, usted necesita aprender un poco más sobre Booleanos y la función `bool()`. 

La función `bool()`es similar a las funciones `int()`o `str()`. Esta retorna una forma booleana del valor pasado a ella. 

La mayoría de los tipos de datos tienen una forma que es considerada como el valor `False`para ese tipo de dato. Cualquier otro valor es considerado `True`. Por ejemplo, el entero `0`, el número de punto flotante `0.0`, una cadena vacía, una lista vacía, y un diccionario vacío son considerados como `False` cuando son usados como una condición para un enunciado `if`o un ciclo. Todos los otro valores son `True`. Ingrese lo siguiente en la «shell» interactiva:

~~~Python
>>> bool(0)
False
>>> bool(0.0)
False
>>> bool('')
False
>>> bool([])
False
>>> bool({})
False
>>> bool(1)
True
>>> bool('Hello')
True
>>> bool([1, 2, 3, 4, 5])
True
>>> bool({'spam':'cheese', 'fizz':'buzz'})
True
~~~

Las condiciones son automáticamente interpretadas como valores Booleanos. Esto es por lo que la condición de la línea 75 funciona correctamente. La llamada a la función `esJugadaVálida()` retornará ya sea un valor Booleano de `False`o una lista no vacía. 

Si usted imagina que la condición completa es colocada dentro de la llamada a `bool()`, entonces la condición `False`de la línea 75 se convierte en `bool(False)`(lo cual, por supuesto, se evalúa a `False`). Y una condición de lista no vacía colocada como parámetro en `bool()` retornará `True`.

## Obteniendo el puntaje del juego de tablero

La función `obtenerPuntajeTablero()` usa ciclos anidados `for`para comprobar todas las 64 posiciones del tablero y ver las fichas de qué jugador (si es que hay) está en el:

~~~Python
 79. def obtenerPuntajeTablero(tablero):
 80.     # Determina el puntaje contando las fichsa. Retorna un diccionario con las llaves 'X' y 'O'.
 81.     puntajex = 0
 82.     puntajeo = 0
 83.     for x in range(ANCHO):
 84.         for y in range(ALTO):
 85.             if tablero[x][y] == 'X':
 86.                 puntajex += 1
 87.             if tablero[x][y] == 'O':
 88.                 puntajeo += 1
 89.     return {'X':puntajex, 'O':puntajeo}
~~~

Para cada ficha X, el código incrementa `puntajex` en la línea 86. Para cada ficha O, el código incrementa `puntajeo` en la línea 88. La función entonces retorna `puntajex` y `puntajeo` en un diccionario.

## Obteniendo la elección de la ficha de la jugadora

La función `ingresarFichaDeJugadora()` pregunta a la jugadora cuál ficha quiere ser, ya sea X o O:

~~~Python
 91. def ingresarFichaDeJugadora():
 92.     # Permite a la juadora elegir qué ficha quiere mover.
 93.     # Retorna una lista con la ficha de la jugadora como primer elemento y la de la computadora como segundo.
 94.     ficha = ''
 95.     while not (ficha == 'X' or ficha == 'O'):
 96.         print('¿Desea ser las fichas X o O?')
 97.         ficha = input().upper()
 98. 
 99.     # El primer elemento en la lista es la ficha de la jugadora, el segundo elemento es la de la computadora.
100.     if ficha == 'X':
101.         return ['X', 'O']
102.     else:
103.         return ['O', 'X']
~~~

El ciclo `for`se mantendrá enciclado hasta que la jugdaora ingrese X o O en mayúscula o minúscula. La función `ingresarFichaDeJugadora()` entonces retorna una lista de dos elementos, donde la ficha elegida por la jugadora es el primer elemento y la ficha de la computadora es el segundo. Luego, la línea 241 llama a `ingresarFichaDeJugadora()` y usa asignación múltiple para poner estos dos elementos retornados en variables. 

## Determinando quien va primero

La función `quiénComienza()` selecciona aleatoriamente quién inicia y retorna ya sea la cadena `computadora`o `jugadora`:

~~~Python
105. def quiénComienza():
106.     # Al azar elige qué jugadora inicia.
107.     if random.randint(0, 1) == 0:
108.         return 'computadora'
109.     else:
110.         return 'jugadora'
~~~



## Colocando la ficha en el tablero

La función `hacerJugada()`es llamada cuando la jugadora quiere colocar la ficha en el tablero y voltear otra fichas según las reglas del Reversi:

~~~Python
112. def hacerJugada(tablero, ficha, iniciox, inicioy):
113.     # Coloca la ficha sobre el tablero en iniciox, inicioy y convierte cualquier ficha de la oponente.
114.     # Retorna False si esta movida es inválida; True si es válida.
115.     fichasAVoltear = esJugadaVálida(tablero, ficha, iniciox, inicioy)
~~~

Esta función modifica en este lugar la estructura de datos `tablero` que se pasó. Los cambios realizados a la variable `tablero` (debido a que es una referencia a una lista) será realizados en el alcance global. 

La mayoría del trabajo es realizado por `esJugadaVálida()` en la línea 115, la cual retorna una lista de coordenadas X y Y (en una lista de dos elementos)  de las fichas que necesitan ser volteadas. Recuerde, si los argumentos `iniciox`e `inicioy`apuntan a una movida inválida, `esjugadaVálida()` retornará el valor booleano `False`, lo cual es comprobado en la línea 117:

~~~Python
117.     if fichasAVoltear == False:
118.         return False
119. 
120.     tablero[iniciox][inicioy] = ficha
121.     for x, y in fichasAVoltear:
122.         tablero[x][y] = ficha
123.     return True

~~~

Si el valor de retorno de `esJugadaVálida()` (ahora almacenada en `fichasAVoltear`) es `False`, entonces `hacerJugada()`también retornará `False`en la línea 118.

En caso contrario, `esJugadaVálida()` retornará una lista de espacios en el tablero para poner las fichas ( la cadena `'X'` o` 'O'` en la casilla). La línea 120 establece el espacio al que la jugadora ha movido. El ciclo `for`de la línea 121  establece todas fichas que están en `fichasAVoltear`.


## Copiando la estructura de datos del tablero

La función `obtenerCopiaTablero()`es diferente de `obtenerNuevoTablero()`. La función `obtenerNuevoTablero()` crea una estructura de datos de tablero de juego vacía que tiene sólo espacios en blanco y las cuatro fichas iniciales. `obtenerCopiaTablero()` crea una estructura de datos del tablero vacía pero luego copia todas las posiciones en el parámetros `tablero` con un ciclo anidado. La IA usa la función `obtenerCopiaTablero()` de modo que pueda hacer cambios en la copia del tablero de juego  sin cambiar el tablero real de juego. Esta técnica fue usada en el Tres en línea del capítulo 10. 

~~~Python
125. def obtenerCopiaTablero(tablero):
126.     # Crea un duplicado de la lista del tablero y la retorna.
127.     copiaDeTablero = obtenerNuevoTablero()
128. 
129.     for x in range(ANCHO):
130.         for y in range(ALTO):
131.             copiaDeTablero[x][y] = tablero[x][y]
132. 
133.     return copiaDeTablero
~~~

Una llamada a `obtenerNuevoTablero()` establece `copiaDeTablero`como una estructura de datos limpia. Luego los dos ciclos `for` anidados copian cada una de las 64 fichas del `tablero` a la estructura de datos del tablero duplicado `copiaDeTablero`.



## Determinando si un espacio es una esquina

La función `esEsquina()`retorna `True`si las coordenadas están en un espacio esquinero (0,0), (7,0), (0,7) o (7,7):

~~~Python
135. def esEsquina(x, y):
136.     # Retorna True si la posición está en una de las cuatro esquinas.
137.     return (x == 0 or x == ANCHO - 1) and (y == 0 or y == ALTO - 1)
~~~

En caso contrario, `esEsquina()` retorna `False`. Usaremos esta función más adelante para la IA. 



## Obteniendo la movida de la jugadora

La función `obtenerJugadaJugadora()` es llamada para permitir a la jugadora ingresar las coordenadas de su próximo movimiento (y comprobar si la jugada es válida). La jugadora también puede ingresar `pistas` para encender el modo (si está apagado) o apagarlo (si está encendido). Finalmente, la jugadora pueden ingresar `salir` para salir del juego. 

~~~Python
139. def obtenerJugadaJugadora(tablero, fichaJugadora):
140.     # Permite a la jugadora ingresar su movimiento.
141.     # Retorna la movida como [x, y] (o retorna la cadena 'pistas' o 'salir').
142.     CIFRAS1A8 = '1 2 3 4 5 6 7 8'.split()
~~~

La variable constante `CIFRAS1A8` es la lista `['1', '2', '3', '4', '5', '6', '7', '8']`. La función `obtenerJugadaJugadora()` usa `CIFRAS1A8` un par de veces, y esta constante es más legible que la el valor completo de la lista. Usted no puede usar el método `isdigit()`porque esto permitiría que 0 y 9 puedan ser ingresados, los cuales no son coordenadas válidas en el tablero de 8x8.

El ciclo `while` se mantiene iterando hasta que la jugadora ingrese un movimiento válido:

~~~Python
143.     while True:
144.         print('Ingrese su jugada, "salir" para finalizar el juego, o "pistas" para activar/desactivar las pistas.')
145.         movida = input().lower()
146.         if movida == 'salir' or movida == 'pistas':
147.             return movida
~~~

La línea 146 comprueba si la jugadora quiere salir o cambiar el estado del modo de pistas, y la línea 147 retorna la cadena `salir` o `pistas`, respectivamente. El método `lower()` es llamado en la cadena retornada por `input()` para que la jugadora pueda ingresar `PISTAS` o `Salir` y aún así el comando sea entendido. 

El código que llamó a `obtenerJugadaJugadora()` manejará que hacer si la jugadora quiere salir o cambiar el modo de pistas. Si la jugadora ingresa coordenadas para moverse, el enunciado `if` en la línea 149 comprueba si la movida es válida:

~~~Python
149.         if len(movida) == 2 and movida[0] in CIFRAS1A8 and movida[1] in CIFRAS1A8:
150.             x = int(movida[0]) - 1
151.             y = int(movida[1]) - 1
152.             if esJugadaVálida(tablero, fichaJugadora, x, y) == False:
153.                 continue
154.             else:
155.                 break
~~~

El juego espera que la jugadora haya ingresado las coordenadas X y Y de su movida como dos números sin nada entre ellos. La línea 149 primero comprueba que el tamaño de la cadena que la jugadora ingreso sea 2. Después de eso, también comprueba que ambos `movida[0]` (el primer caracter en la cadena) y `movida[1])` (el segundo caracter en la cadena) sean cadenas que existan en `CIFRAS1A8`.

Recuerde que la estructura de datos del tablero de juego tiene índices de 0 a 7, no de 1 a 8. El código imprime de 1 a 9 cuando el tablero se despliega en `dibujarTablero()` porque quienes no sean programadoras están acostumbrados a números que comienzan en 1 en vez de 0. Así que para convertir las cadenas en `movida[0]` y `movida[1]` a enteros, las líneas 150 y 151 restan 1 de `x `y `y`. 

Incluso si la jugadora ha ingresado una movida correcta, el código necesita comprobar que la movida es permitida por las reglas del Reversi. Esto es realizado por la función `esJugadaVálida()`, a la cual es pasada la estructura de datos del tablero, la ficha de la jugadora y las coordenadas X y Y del movimiento. 

Si  `esJugadaVálida()` retorna `False`, se ejecuta el enunciado `continue` en la línea 153. La ejecución entonces irá de vuelta al inicio del ciclo `while`y preguntará a la jugadora por una movida válida de nuevo. En otro caso, la jugadora habrá ingresado una movida válida, y la ejecución romper el ciclo `while` para salir. 

Si la condición del enunciado `if` en la línea 149 fue `False`, entonces la jugadora no ingresó una movida válida. Las líneas 157 y 158 le instruyen en cómo ingresar correctamente movidas:

~~~Python
156.         else:
157.             print('Esa no es una jugada válida. Ingrese la columna (1-8) y luego la fila (1-8).')
158.             print('Por ejemplo, 81 coresponde a la esquina superior derecha.')
~~~

Después de todo, la ejecución se mueve de regreso al enunciado `while`en la línea 143, porque la línea 158 no es solo la última línea en el bloque `else` sino que es la última línea en el bloque `while`. El ciclo `while` se mantendrá enciclado hasta que la jugadora ingrese una movida válida. Si la jugadora ingresa una coordenada X y Y, la línea 160 se ejecutará:

~~~Python
160.     return [x, y]
~~~

Finalmente, si la línea 160 se ejecuta, `obtenerJugadaJugadora()` retorna una lista de dos elementos con las coordenadas X y Y de la movida válida de la jugadora.



## Obteniendo la movida de la computadora

La función `obtenerJugadaComputadora()`es dónde el algoritmo de IA es implementado:

~~~Python
162. def obtenerJugadaComputadora(tablero, fichaComputadora):
163.     # Dado un tbalero y una ficha de la computadora, determina dónde
164.     # jugar y retorna la movida como una lista [x, y].
165.     movidasPosibles = obtenerJugadasVálidas(tablero, fichaComputadora)
~~~

Normalmente usted usa los resultados de `obtenerJugadasVálidas()` para el modo pistas, el cual imprimirá . en el tablero para mostrar a la jugadora todas las movidas potenciales que puede realizar. Pero si `obtenerJugadasVálidas()` es llamada con la ficha de IA de la computadora (en `fichaComputadora`), esta también encontrará todas las posibles movidas que la `computadora` puede hacer. La IA seleccionará la mejor movida de la lista. 

Primero, la función `random.shuffle()` ordenará aleatoriamente la movidas en la lista `movidasPosibles`:

~~~Python
166.     random.shuffle(movidasPosibles) # Ordena al azar el orden de las jugadras posibles.
~~~

Queremos desordenar la lista`movidasPosibles` porque esto hará la IA menos predecible; caso contrario, la jugadora podría solo memorizarse las movidas necesarias para ganar porque las respuestas de la computadora serían siempre las mismas. Veamos el algoritmo. 



### Haciendo estrategia con movidas a esquinas

Las movidas a esquinas son una buena idea en Reversi porque una vez que una ficha ha sido colocada en una esquina, nunca podrá ser volteada. El ciclo de la línea 169 itera por cada movida en `movidasPosibles` Si alguna de estas es a una esquina, el programa retornará ese espacio como la movida de la computadora:

~~~Python
168.     # Siempre juega en una esquna si está disponible.
169.     for x, y in movidasPosibles:
170.         if esEsquina(x, y):
171.             return [x, y]
~~~

Ya que `movidasPosibles()` es una lista de dos elementos, usaremos asignación múltiple en el ciclo `for`para establecer `x` y `y`. Si `movidasPosibles` contiene múltiple movidas a las esquinas, la primera siempre será usada. Pero ya que `movidasPosibles` fue ordenada de manera aleatoria en la línea 166, que movida a una esquina que esté de primera es aleatoria. 

### Obteniendo una lista de las movidas con mayor puntaje

Si no hay movimientos a una esquina, el programa se enciclará a través de la lista completa de posibles movimientos y buscará cuál resultado resulta en el mayor puntaje. Luego `mejorJugada` se establecida con la movida de mayor puntaje que el código ha encontrado hasta ese momento, y `mejorPuntaje` es establecida  al puntaje de la mejor movida. Esto es repetido hasta que la jugada posible con mayor puntaje es encontrada. 

~~~Python
173.     # Busca la movida de mayor puntaje posible.
174.     mejorPuntaje = -1
175.     for x, y in movidasPosibles:
176.         copiaDeTablero = obtenerCopiaTablero(tablero)
177.         hacerJugada(copiaDeTablero, fichaComputadora, x, y)
178.         puntaje = obtenerPuntajeTablero(copiaDeTablero)[fichaComputadora]
179.         if puntaje > mejorPuntaje:
180.             mejorJugada = [x, y]
181.             mejorPuntaje = puntaje
182.     return mejorJugada
~~~

La línea 174 primera establece `mejoPuntaje` a -1 para que la primera movida que el código revisa sea establecida como la primera `mejorJugada`. Esto garantiza que `mejorJugada` se establezca con alguna de las movidas de `movidasPosibles` cuando esta retorne. 

En la línea 175, el ciclo `for` establece `x` y `y`con cada movida en `movidasPosibles`. Antes de simular una movida, la línea 176 hace un duplicado de la  estructura de datos del tablero de juego llamando a `obtenerCopiaTablero()`. Usted querrá una copia que pueda modificar sin cambiar la estructura de datos del tablero de juego real almacenada en la variable `tablero`.

Luego la línea 177 llama a `hacerJugada()`, pasándole el tablero duplicado (almacenado en `copiaTablero`) en vez del tablero real. Esto simulará lo que ocurriría en el tablero real si esa movida se hiciera. La función `hacerJugada()` manejará colocar la ficha de la computadora y voltear las fichas de la jugadora en el tablero duplicado. 

La línea 178 llama a `obtenerPuntajeTablero()` con el tablero duplicado, lo cual retorna un diccionario donde las llaves son `'X'` y `'O'`, y los valores son los puntajes. Cuando el código en el ciclo encuentra una movida que puntúa mayor que `mejorPuntaje`, las línea 179 a 181 almacenarán esa movida y puntaje como los nuevos valores en `mejorPuntaje` y `mejorJugada`. Luego de que `movidasPosibles` ha sido iterada completamente, `mejorJugada`será retornado. 

Por ejemplo, digamos que `obtenerMejorPuntaje()` retorna el diccionario `{'X':22, 'O':8}` y la `fichaComputadora` es `'X'`. Entonces `obtenerMejorPuntaje(copiaTablero)[fichaComputadora]` evaluaría a `{'X':22, 'O':8}['X']`, lo cual entonces evaluaría a 22. Si 22 es mayor que `mejorPuntaje`, `mejorPuntaje` es establecido con `22`, y `mejorMovida`es establecido con los actuales valores de `x`y `y`.

Para cuando este ciclo `for` termine, usted puede estar seguro que `majorPuntaje` es el mayor puntaje posible que una movida puede obtener, y esa movida está almacenada en `mejorMovida`.

Aún cuando el código siempre elija la primera en la lista de estas movidas, la elección parece ser aleatoria porque la lista fue ordenada de forma aleatoria en la línea 166. Esto se asegura que la IA no será predecible cuando haya más de un mejor movimiento. 



## Imprimiendo los marcadores en la pantalla

La función `mostrarPuntajes()` llama a la función `obtenerPuntajeTablero()` y luego imprime los marcadores de la jugadora y la computadora:

~~~Python
184. def mostrarPuntajes(tablero, fichaJugadora, fichaComputadora):
185.     puntajes = obtenerPuntajeTablero(tablero)
186.     print('Usted: %s puntos. Computadora: %s puntos.' % (puntajes[fichaJugadora], puntajes[fichaComputadora]))
~~~

Recuerde que `obtenerPuntajeTablero()` retorna un diccionario con las llaves 'X' y 'O' y los valores de los marcadores para los jugadores 'X' y 'Y'.

Esas son todas las funciones para el juego de Reversi, el código en la función `jugarJuego()` implementa el juego actual y llama estas funciones según se necesiten. 



## Iniciando el juego

La función `jugarJuego()` llama las funciones previas que hemos escrito para jugar un juego:

~~~Python
188. def jugarJuego(fichaJugadora, fichaComputadora):
189.     mostrarPistas = False
190.     turno = quiénComienza()
191.     print('Las fichas de la ' + turno + ' comenzarán.')
192. 
193.     # Limpia el tablero y coloca la piezas iniciales.
194.     tablero = obtenerNuevoTablero()
195.     tablero[3][3] = 'X'
196.     tablero[3][4] = 'O'
197.     tablero[4][3] = 'O'
198.     tablero[4][4] = 'X'
~~~

A la función `jugarJuego()` se le pasan las cadenas 'X' o 'O' como `fichaJugadora` y `fichaComputadora`.  La jugadora que irá primero es determinada por la línea 190. La variable `turno` contiene la cadena `'computadora'` o `'jugadora'` para mantener registro de quien es el turno de juego. La línea 194 crea una estructura de datos de tablero de juego vacía, mientras que las líneas 195 a 198 establecen las cuatro fichas iniciales en el tablero. El juego ahora está listo para iniciar. 



### Comprobando un estancamiento

Antes de obtener el turno de la jugadora o computadora, necesitamos comprobar si incluso es posible para alguna de las dos moverse. Si no, entonces el juego está en un estancamiento y debería terminar. (Si solo uno de los lados tiene movidas válidas, el turno salta a la otra jugadora.)

~~~Python
200.     while True:
201.         jugadasVálidasJugadora = obtenerJugadasVálidas(tablero, fichaJugadora)
202.         jugadasVálidasComputadora = obtenerJugadasVálidas(tablero, fichaComputadora)
203. 
204.         if jugadasVálidasJugadora == [] and jugadasVálidasComputadora == []:
205.             return tablero # Nadie se puede mover, así que el juego terminará.
~~~

La línea 200 es el ciclo principal para correr los turnos de la jugadora y la computadora. Mientras este ciclo siga dando vueltas, el juego continuará. Pero antes de correr estos turnos, las líneas 201 y 202 comprueban si cualquier lado puede hacer una movida  obteniendo una lista de movidas válidas. Si ambas de estas listas son vacías, entonces ninguna jugadora puede hacer una movida. La línea 205 sale de la función `jugarJuego()` al retornar un tablero final, finalizando el juego. 



### Corriendo el turno de la jugadora

Si el juego no está estancado, el programa determinará si es el turno de la jugadora revisando si `turbo` está establecido con `jugadora`:

~~~Python
207.         elif turno == 'jugadora': # Turno de la jugadora
208.             if jugadasVálidasJugadora != []:
209.                 if mostrarPistas:
210.                     tableroJugadasVálida = obtenerTableroConJugadasVálidas(tablero, fichaJugadora)
211.                     dibujarTablero(tableroJugadasVálida)
212.                 else:
213.                     dibujarTablero(tablero)
214.                 mostrarPuntajes(tablero, fichaJugadora, fichaComputadora)
~~~

La línea 207 comienza un bloque `elif` que contiene el código que se ejecuta si es el turno de la jugadora. (El bloque `elif` que inicia en la línea 227 contiene el código para el turno de la computadora.)

Todo este código se ejecutará sólo si la jugadora tiene una movida válida, lo cual fue determinado por la línea 208 al comprobar que `jugadasVálidasJugadora`no está vacía. Desplegamos el tablero en la pantalla al llamar a `dibujarTablero()` en la línea 211 o 213.

Si el modo pistas está activado (esto es, `mostrarPistas` es `True`), entonces la estructura de datos del tablero deberá mostrar . en cada espacio válido para que la jugadora pueda mover, lo cual es logrado con la función `obtenerTableroConJugadasVálidas()`. Se le pasa una estructura de datos del tablero de juego y retorna una copia que también contiene puntos (.). La línea 211 pasa este tablero a la función `dibujarTablero()`.

Si el modo pistas está apagado, entonces la línea 213 pasa `tablero` a `dibujarTablero()` en cambio. 

Después de imprimir el tablero de juego a la jugadora, usted también querrá imprimir el marcador actual al llamar a `mostrarPuntajes()` en la línea 214. 

Luego, la jugadora necesitará ingresar su movida. La función `obtenerJugadaJugadora()` maneja esto, y su valor retornado es una lista de dos elementos de las coordenadas X y Y de la movida de la jugadora:

~~~Python
216.                 movida = obtenerJugadaJugadora(tablero, fichaJugadora)
~~~

Cuando definimos `obtenerJugadaJugadora()` nosotras nos aseguramos de que la jugada de la jugadora es válida. 

La función `obtenerJugadaJugadora()` podría haber retornado las cadenas `pistas` o `salir` en vez de una movida en el tablero. Las líneas 217 a 222 manejan estos casos:

~~~Python
217.                 if movida == 'salir':
218.                     print('¡Gracias por jugar!')
219.                     sys.exit() # Termina el programa.
220.                 elif movida == 'pistas':
221.                     mostrarPistas = not mostrarPistas
222.                     continue
223.                 else:
224.                     hacerJugada(tablero, fichaJugadora, movida[0], movida[1])
225.             turno = 'computadora'
~~~

Si la jugadora ingresa `salir` como su movida, entonces `obtenerJugadaJugadora()`retornará la cadena `salir`. En este caso, la línea 219 llama a `sys.exit()` para terminar el programa. 

Si la jugadora ingresa `pistas` como su movida, entonces `obtenerJugadaJugadora()`retornará la cadena pistas. En este caso, usted quiere encender el modo pistas (si estaba apagado) o apagarlo (si estaba encendido). 

El enunciado de asignación `mostrarPistas = not mostrarPistas` en la línea 221 maneja ambos casos, porque `not False` se evalúa a `True` y `not True` se evalúa a `False`. Luego el enunciado `continue` mueve la ejecución al inicio del ciclo (`turno` no ha cambiado, así que se mantendrá el turno de la jugadora). 

En caso contrario, si la jugadora no ingresa salir o no cambia el modo pistas, la línea 225 llama a `hacerJugada()` para hacer la jugada en el tablero. 

Finalmente, la línea 225 establece `turno`a `computadora`. El flujo de ejecución salta al bloque `else` y alcanza el final del bloque `while`, de modo que la ejecución salta hacia atrás al enunciado `whle` en la línea 200.  Esta vez, sin embargo, será el turno de la computadora. 



### Ejecutando el turno de la computadora

Si la variable `turno` contiene la cadena `computadora`, entonces el código para el turno de la computadora se ejecutará. Este es similar al código del turno de la jugadora, con pocos cambios:

~~~Python
227.         elif turno == 'computadora': # turno de la computadora
228.             if jugadasVálidasComputadora != []:
229.                 dibujarTablero(tablero)
230.                 mostrarPuntajes(tablero, fichaJugadora, fichaComputadora)
231. 
232.                 input('Presione ENTER para ver la jugada de la computadora.')
233.                 movida = obtenerJugadaComputadora(tablero, fichaComputadora)
234.                 hacerJugada(tablero, fichaComputadora, movida[0], movida[1])
~~~



Después de imprimir el tablero con `dibujarTablero()`, el programa también imprime el marcador actual con una llamada a `mostrarPuntajes()` en la línea 230. 

La línea 232 llama a `input()`para pausar el *script* de modo que la jugadora pueda mirar al tablero. Esto es muy similar a como se usó el `input()` para pausar el programa de Chistes del capítulo 4. En vez de usar una llamada a `print()`para imprimir una cadena antes de llamar a `input()`, usted puede hacer lo mismo pasándole la cadena a imprimir a `input()`.

Después de que la jugadora a visto el tablero y presionado ENTER, la línea 233 llama a `obtenerJugadaComputadora()`para obtener las coordenadas X y Y del siguiente movimiento de la computadora. Estas coordenadas son almacenadas en las variables `x` y `y` usando asignación múltiple. 

Finalmente, `x`y `y`, junto con la estructura de datos del tablero de juego y la ficha de la computadora, son pasadas a la función `hacerJugada()`. Esto coloca la ficha de la computadora en el tablero de juego en `tablero` para reflejar la movida de la computadora. La llamada de la línea 233 a `obtenerJugadaComputadora()`obtiene la movida de la computadora (y la almacena en las variables `x`y `y`). La llamada a `hacerJugada()` en la línea 234 hace la movida en el tablero.

Luego, la línea 235 establece la variable `turno` a `jugadora`:

~~~Python
235.             turno = 'jugadora'
~~~

No hay más código en el bloque `while`después de la línea 235, así que le ejecución regresa al enunciado `while` en la línea 200.



## El ciclo de juego

Esas son todas las funciones que haremos para Reversi. Iniciando en la línea 239, la parte principal del programa ejecuta un juego al llamar a `jugarJuego()`, pero también muestra el marcador final y pregunta si la jugadora quiere jugar de nuevo:

~~~Python
239. print('¡Bienvenida a Reversi!')
240. 
241. fichaJugadora, fichaComputadora = ingresarFichaDeJugadora()
~~~

El programa comienza dando la bienvenida a la jugadora en la línea 239 y preguntándole si quiere ser *X* o *O*. La línea 241 usa el truco de asignación múltiple para establecer `fichaJugadora` y `fichaComputadora` con los dos valores retornados por `ingresarFichaDeJugadora()`. 

El bucle `while` en la línea 243 ejecuta cada juego:

~~~Python
243. while True:
244.     tableroFinal = jugarJuego(fichaJugadora, fichaComputadora)
245. 
246.     # Muestra el puntaje final.
247.     dibujarTablero(tableroFinal)
248.     puntajes = obtenerPuntajeTablero(tableroFinal)
249.     print('X obtuvo %s puntos. O obtuvo %s puntos.' % (puntajes['X'], puntajes['O']))
250.     if puntajes[fichaJugadora] > puntajes[fichaComputadora]:
251.         print('¡Usted venció la computadora por %s puntos! ¡Felicidades!' % (puntajes[fichaJugadora] - puntajes[fichaComputadora]))
252.     elif puntajes[fichaJugadora] < puntajes[fichaComputadora]:
253.         print('Usted perdió. La computadora la venció por %s puntos.' % (puntajes[fichaComputadora] - puntajes[fichaJugadora]))
254.     else:
255.         print('¡El juego finalizó empatado!')
~~~

Este comienza llamando a `jugarJuego()`. Esta llamada a función no retorna hasta que el juego haya finalizado. La estructura de datos del tablero retornada por `jugarJuego()`será pasada a `obtenerPuntajeTablero()` para contar las fichas *X* y *O* para determinar el marcador final. La línea 249 muestra el marcador final.

Si hay más fichas de la jugadora que de la computadora, la línea 251 felicita a la jugadora por haber ganar. Si la computadora ganó, la línea 253 le dice a la jugadora que perdió. En caso contrario, la línea 255 le dice a la jugadora que el juego a quedado empatado.



## Preguntando a la jugadora si quiere jugar de nuevo

Después de finalizado el juego, la jugadora es preguntada por si quiere jugar de nuevo:

~~~Python
257.     print('¿Quiere jugar de nuevo? (si o no)')
258.     if not input().lower().startswith('s'):
259.         break
~~~

Si la jugadora no ingresa una respuesta que comience con la letra `s`, como `sí` o `SÍ` o `S`, entonces la condición en la línea 258 evalúa a `True`, y la línea 259 rompe el ciclo  `while` que inició en la línea 243, lo cual finaliza el juego. En caso contrario, este ciclo `while`naturalmente se enciclará, y `jugarJuego()` es llamada de nuevo para iniciar el siguiente juego. 



## Resumen

La IA de Reversi puede verse invencible, pero no es porque la computadora sea más inteligente que nosotros; ¡es solo que es más rápida! la estrategia que sigue es sencilla: mueva a la esquina si puede, en caso contrario haga el movimiento que voltearála mayoría de fichas. Un humano podría hacer eso, pero le tomará un rato calcular cuántas fichas volteará en cada posible movimiento válido. Para la computadora, calcular este número es sencillo. 

Este juego es similar a la Búsqueda del tesoro con sonar porque hace uno de una cuadrícula para el tablero. También es como el Tres en línea porque hay una IA que planea cuál es el mejor movimiento a realizar por parte de la computadora. Este capítulo introdujo solo uno nuevo concepto: que las listas vacías, las hileras vacías y el entero 0 evalúan a `False` en el contexto de una condición. A parte de eso, ¡este juego usó conceptos de programación que usted ya sabía!

En el capítulo 16, usted aprenderá cómo hacer con IA que la computadora juegue contra ella misma.



[Previo: Capítulo 14: Código del César ](capitulo14.md) | [Siguiente: Capítulo 16: Simulación de IA de Reversi ](capitulo16.md)