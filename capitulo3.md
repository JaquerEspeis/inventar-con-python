# 3 Adivine el número

![Matraz de Erlenmeyer](https://inventwithpython.com/invent4thed/images/00016.jpeg "Matraz de Erlenmeyer")

En este capítulo va a hacer un juego de Adivine el número. La computadora
pensará un número secreto entre 1 y 20 y le pedirá a la usuaria que lo adivine.
Después de cada intento, la computadora le dirá a la usuaria si el número es
muy alto o muy bajo. La usuaria gana si puede adivinar el número en tres seis
intentos.

Este es un buen juego para escribir en código porque cubre muchos conceptos de
programación en un programa corto. Aprenderá cómo convertir valores a
diferentes tipos de datos y cuándo necesita hacerlo. Ya que este programa es
un juego, a partir de ahora llamaremos *jugadora* a la usuaria.

***
Temas cubiertos en este capítulo:

* Sentencias `import`
* Módulos
* La función `randint()`
* Sentencias `for`
* Bloques
* Las funciones `str()`, `int()` y `float()
* Booleanos
* Operadores de comparación
* Condiciones
* La diferencia entre `=` y `==`
* Sentencias `if`
* Sentencias `break`
***

## Ejecución de ejemplo de Adivine el número

Aquí está cómo se ve para la jugadora cuando se ejecuta el juego de Adivine el
número. Los valores que ingresa la jugadora están marcados en negrita.

***
<pre>
¡Hola! ¿Cuál es su nombre?
<b>Alberto</b>
Bueno Alberto, estoy pensando un número entre 1 y 20.
Trate de adivinarlo.
<b>10</b>
El valor es muy alto.
Trate de adivinarlo.
<b>20</b>
El valor es muy bajo.
Trate de adivinarlo.
<b>4</b>
¡Buen trabajo, Alberto! ¡Adivinó mi número en 3 intentos!
</pre>
***

## Código fuente de Adivine el número

Abra una nueva ventana en el editor de archivos haciendo clic en
**Archivo > Nueva ventana**. En la ventana en blanco que aparece, escriba el
código fuente y guárdelo como *guess.py*. Luego ejecute el programa presionando
F5.

![Pingüino recordando usar Python 3](https://inventwithpython.com/invent4thed/images/00020.jpeg "Pingüino recordando usar Python 3")

Cuando escriba este código en el editor de archivos, asegúrese de poner
atención a los espacios al frente de las líneas. Algunas líneas necesitan ser
indentadas a cuatro u ocho espacios.

Si obtiene errores después de escribir este código, compare el código que
escribió con el código del libro en la herramienta de diff en línea en
[https://www.nostarch.com/inventwithpython#diff](https://www.nostarch.com/inventwithpython#diff).

*guess.py*
***
<pre>
 1. # This is a Guess the Number game.
 2. import random
 3.
 4. guessesTaken = 0
 5.
 6. print('¡Hola! ¿Cuál es su nombre?')
 7. myName = input()
 8.
 9. number = random.randint(1, 20)
10. print('Bueno, ' + myName + ', estoy pensando un número entre 1 y 20.')
11.
12. for guessesTaken in range(6):
13.     print('Trate de adivinarlo.') # Cuatro espacios al frente de «print»
14.     guess = input()
15.     guess = int(guess)
16.
17.     if guess < number:
18.         print('El valor es muy bajo.') # Ocho espacios al frente de «print»
19.
20.     if guess > number:
21.         print('El valor es muy alto.')
22.
23.     if guess == number:
24.         break
25.
26. if guess == number:`
27.     guessesTaken = str(guessesTaken + 1)
28.     print('¡Buen trabajo, ' + myName + '! ¡Adivinó mi número en ' +
          guessesTaken + ' intentos!')
29.
30. if guess != number:
31.     number = str(number)
32.     print('Nop. El número que estaba pensando era ' + number + '.')
</pre>
***

## Importando el módulo random

Veamos a las dos primeras líneas de este programa:

***
<pre>
1. # This is a Guess the Number game.
2. import random
</pre>
***

La primera línea es un comentario, que vio en el Capítulo 2. Recuerde que
Python ignorará todo lo que esté después del carácter `#`. El comentario aquí
sólo nos recuerda qué es lo que hace este programa.

La segunda línea es una sentencia `import`. Recuerde, las sentencias son
instrucciones que ejecutan una acción pero no evalúan a un valor, como hacen
las expresiones. Ya vio la sentencia de asignación, que almacena un valor en
una variable.

Aunque Python incluye muchas funciones incorporadas, algunas funciones se
escriben en programas aparte llamados *módulos*. Puede usar estas funciones
importando sus módulos en su programa, con una sentencia `import`.

La línea 2 importa el módulo `random` de forma que el programa pueda llamar la
función `randint()`. Esta función traerá un número aleatorio para que la
jugadora adivine.

Ahora que ha importado el módulo `random`, necesitará establecer algunas
variables que su programa usará más adelante.

La línea 4 crea una nueva variable llamada `guessesTaken` (intentos, en
español):

***
<pre>
4. guessesTaken = 0
</pre>
***

En esta variable almacenará el número de intentos que la jugadora ha hecho. Ya
que la jugadora no ha hecho ningún intento en este punto del programa, almacene
el entero `0` aquí.

***
<pre>
6. print('¡Hola! ¿Cuál es su nombre?')
7. myName = input()
</pre>
***

Las líneas 6 y 7 son las mismas que las líneas del programa Hello World en el
Capítulo 2. Las programadoras por lo general reusan código de otros programas
para ahorrarse trabajo.

La línea 6 es una función que llama a `print()`. Recuerde que esta función es
como un miniprograma dentro de su programa. Cuando un programa llama una
función, este ejecuta ese miniprograma. El código dentro de `print()` muestra
en la pantalla la cadena de caracteres que le pasó como argumento.

La línea 7 le permite a la jugadora escribir su nombre y lo almacena en la
variable `myName` (miNombre, en español). Recuerde, la cadena de caracteres
podría no ser realmente el nombre de la jugadora; es sólo cualquier cadena de
caracteres que la jugadora escriba. Las computadoras son tontas y siguen las
instrucciones, sin importar qué.

## Generación de números aleatorios con la función random.randint()

Ahora que sus otras variables están establecidas, puede usar la función del
módulo `random` (aleatorio, en español) para establecer el número secreto de la
computadora:

***
<pre>
9. number = random.randint(1, 20)
</pre>
***

La línea 9 llama a una nueva función llamada `randint()` (por «random integer»,
entero aleatorio en español) y almacena el valor que devuelve en `number`
(número, en español). Recuerde que las llamadas a función pueden ser parte de
expresiones porque estas evalúan a un valor.

La función `randint()` es brindada por el módulo `random`, de forma que debe
llamarla con `random.randint()` (¡no olvide el punto!) para decirle a Python
que la función `randint()` está en el módulo `random`.

`randint()` devolverá un entero aleatorio entre dos argumentos enteros que le
pase (e incluyéndolos). La línea 9 pasa `1` y `20`, separados por comas, entre
los paréntesis que siguen al nombre de función. El entero aleatorio que
`randint()` devuelve se almacena en una variable llamada `number`--este es el
número secreto que la jugadora intentará adivinar.

Sólo por un momento, vuelva a la consola interactiva y escriba
**`import random`** para importar el módulo `random`. Luego, escriba
**`random.randint(1, 20)`** para ver a qué evalúa la función. Esta devuelve un
entero entre `1` y `20`. Repita el código de nuevo, y la llamada a la función
devolverá otro entero. La función `readint()` devuelve un entero aleatorio cada
vez, justo como tirar un dado resultará en un número aleatorio cada vez. Por
ejemplo, escriba lo siguiente en la consola interactiva. Es probable que el
resultado que obtendrá cuando llame a la función `randint()` sea diferente
(¡después de todo es aleatorio!).

***
<pre>
>>> <b>import random</b>
>>> <b>random.randint(1, 20)</b>
12
>>> <b>random.randint(1, 20)</b>
18
>>> <b>random.randint(1, 20)</b>
3
>>> <b>random.randint(1, 20)</b>
18
>>> <b>random.randint(1, 20)</b>
7
</pre>
***

También puede intentar diferentes rangos de números cambiando los argumentos.
Por ejemplo, escriba **`random.randint(1, 4)`** para obtener sólo enteros entre
`1` y `4` (incluyendo a ambos `1` y `4`). O trate
**`random.randint(1000, 2000)`** para obtener enteros entre `1000` y `2000`.

Escriba este código en la consola interactiva y vea los números que obtiene:

***
<pre>
>>> <b>random.randint(1, 4)</b>
3
>>> <b>random.randint(1000, 2000)</b>
1294
</pre>
***

Puede cambiar el código del juego un poco para hacer que el juego se comporte
diferente. En nuestro código original, usamos un entero entre `1` y `20`:

***
<pre>
 9. number = random.randint(1, 20)
10. print('Bueno, ' + myName + ', estoy pensando un número entre 1 y 20.')
</pre>
***

Pruebe en vez de eso cambiar el rango de enteros a `(1, 100`).

***
<pre>
 9. number = random.randint(1, <b>100</b>)
10. print('Bueno, ' + myName + ', estoy pensando un número entre 1 y <b>100</b>.')
</pre>
***

Ahora la computadora pensará un entero entre `1` y `100` en vez de entre `1` y
`20`. Cambiar la línea 9 cambiará el rango del número aleatorio, pero recuerde
también cambiar la línea 10 para que el juego le diga a la jugadora del nuevo
rango en lugar del viejo.

Puede usar la función `randint()` siempre que quiera agregar aleatoriedad a
sus juegos. Usará aleatoriedad en mucho juegos. (Piense cuántos juegos usan un
dado).

## Dando la bienvenida a la jugadora

Después de que la computadora asigna un número aleatorio a `number`, le da la
bienvenida a la jugadora:

10. print('Bueno, ' + myName + ', estoy pensando un número entre 1 y 20.')

En la línea 10, `print()` le da la bienvenida a la jugadora llamándola por su
nombre y le dice que la computadora está pensando un número aleatorio.

A primera vista, puede parecer como que hay más de un argumento de cadena de
caracteres en la línea 10, pero examínela con más cuidado. El operador `+`
entre las tres cadenas de caracteres las concatena en una sola cadena. Y esa
cadena es el argumento que se pasa a `print()`. Si lo ve con más detenimiento,
verá que las comas están dentro de las comillas y son parte de las cadenas de
caracteres.

## Sentencias de control de flujo

En capítulos anteriores, la ejecución del programa empezó en la instrucción de
más arriba del programa y se movió directo hacia abajo, ejecutando cada
instrucción en orden. Pero con las sentencias `for`, `if`, `else` y `break` se
puede hacer un ciclo de ejecución o saltar instrucciones con base en
condiciones. Este tipo de sentencias son *sentencias de control de flujo*,
porque cambian el flujo de la ejecución del programa conforme se mueve
alrededor de su programa.

### Usando ciclos para repetir código

La línea 12 es una sentencia `for`, que indica el inicio de un ciclo `for`:

***
<pre>
12. for guessesTaken in range(6):
</pre>
***

Los *ciclos* le permiten ejecutar código una y otra vez. La línea 12 repetirá
el código seis veces. Una sentencia `for` empieza con la palabra clave `for`,
seguida de un nuevo nombre de variable, la palabra clave `in`, una llamada a
la función `range()` que especifica el número de ciclos que debería hacer y
dos puntos. Vamos por unos cuantos conceptos adicionales para que pueda
trabajar con ciclos.

## Agrupando con bloques

Muchas líneas de código se pueden agrupar juntas en un *bloque*. Cada línea en
un bloque de código empieza con por lo menos el número de espacios de la
primera línea en el bloque. Usted puede notar dónde empieza y termina el bloque
viendo el número de espacios al frente de las líneas. Esta es la *indentación*
de la línea.

Los programas de Python típicamente usan cuatro espacios *adicionales* de
indentación para empezar un bloque. Cualquier línea siguiente que esté
indentada por la misma cantidad es parte del bloque. El bloque termina cuando
hay una línea de código con la *misma indentación que antes* de que el bloque
empezara. También puede haber bloques dentro de otros bloques. La Figura 3-1
muestra un diagrama de código con los bloques resaltados y numerados.

![Ejemplo de bloques y su indentación](https://inventwithpython.com/invent4thed/images/00053.jpeg "Ejemplo de bloques y su indentación")

Figura 3-1: Un ejemplo de bloques y su indentación. Los puntos grises
representan espacios.

En la Figura 3-1, la línea 12 no tiene indentación y no está dentro de ningún
bloque. La línea 13 tiene una indentación de cuatro espacios. Ya que esta línea
está indentada más que la línea siguiente, aquí inicia un nuevo bloque. Cada
línea que sigue a esta con la misma cantidad de indentación o más se considera
parte del bloque (1). Si Python encuentra otra línea con menos indentación
que la primera línea del bloque, el bloque ha terminado. Las líneas en blanco
se ignoran.

La línea 18 tiene una indentación de ocho espacios, que empieza el bloque (2).
Este bloque está *dentro* del bloque (1). Pero la siguiente línea, línea 20,
está indentada sólo cuatro espacios. Porque la indentación se ha reducido, se
sabe que el bloque (2) de la línea 18 ha terminado, y porque la línea 20 tiene
la misma indentación que la línea 13, se sabe que está en el bloque (1).

La línea 21 aumenta la indentación a ocho espacios de nuevo, entonces otro
nuevo bloque dentro del bloque ha empezado: el bloque (3). En la línea 23,
salimos del bloque (3), y en la línea 24 entramos al último bloque dentro de
un bloque, el bloque (4). Ambos bloques (1) y (4) terminan en la línea 24.

## Haciendo un ciclo con sentencias for

Las sentencias for marcan el inicio de un ciclo. Los ciclos ejecutan el mismo
código de forma repetida. Cuando la ejecución alcanza una sentencia for, entra
al bloque que le sigue a la sentencia. Después de ejecutar todo el código en
este bloque, la ejecución se mueve de vuelta al inicio del bloque para ejecutar
el código de nuevo.

Escriba lo siguiente en la consola interactiva:

***
<pre>
>>> <b>for i in range(3):
    print('¡Hola! i tiene un valor de', i)</b>

¡Hola! i tiene un valor de 0
¡Hola! i tiene un valor de 1
¡Hola! i tiene un valor de 2
</pre>
***

Note que después de escribir `for i in range(3):` y presionar ENTER, la consola
interactiva no mostró otro «prompt» `>>>` porque está esperando que escriba un
bloque de código. Presione ENTER de nuevo después de la última instrucción para
decirle a la consola interactiva que ya terminó de escribir el bloque de código.
(Esto aplica sólo cuando está trabajando en la consola interactiva. Cuando
escriba archivos *.py* en el editor de archivos, no necesita insertar una
línea en blanco.)

Veamos el ciclo `for` en la línea 12 de *guess.py*:

***
<pre>
12. for guessesTaken in range(6):
13.     print('Trate de adivinarlo.') # Cuatro espacios al frente de «print»
14.     guess = input()
15.     guess = int(guess)
16.
17.     if guess < number:
18.         print('El valor es muy bajo.') # Ocho espacios al frente de «print»
19.
20.     if guess > number:
21.         print('El valor es muy alto.')
22.
23.     if guess == number:
24.         break
25.
26. if guess == number:
</pre>
***

En Adivine el número, el bloque `for` empieza en la sentencia `for` en la línea
12, y la primera línea después del bloque `for` es la línea 26.

Una sentencia `for` siempre tiene dos puntos (`:`) después de la condición. Las
sentencias que terminan con dos puntos esperan un nuevo bloque en la línea
siguiente. Esto se ilustra en la Figura 3-2.

![El flujo de ejecución del ciclo for](https://inventwithpython.com/invent4thed/images/00055.jpeg "El flujo de ejecución del ciclo for")

Figura 3-2: El flujo de ejecución del ciclo for.

La Figura 3-2 muestra cómo fluye la ejecución. La ejecución entrará al bloque
`for` en la línea 13 y seguirá hacia abajo. Una vez que el programa alcanza el
final del bloque `for`, en lugar de seguir hacia abajo a la siguiente línea, la
ejecución hace un ciclo de vuelta al inicio del bloque `for` en la línea 13.
Hace esto seis veces por la llamada a la función `range(6)` en la sentencia
`for`. Cada vez que la ejecución pasa por el ciclo se llama una *iteración*.

Piense en la sentencia `for` como decir, «Ejecute el código del siguiente
bloque un cierto número de veces».

## Obteniendo el número de la jugadora

Las líneas 13 y 14 le preguntan a la jugadora que adivine cuál es el número
secreto, y le permite escribir su número:

***
<pre>
13.     print('Trate de adivinarlo.') # Cuatro espacios al frente de «print»
14.     guess = input()
</pre>
***

El número que la jugadora escribe se almacena en la variable llamada «guess»
(adivinanza, en español).

## Convirtiendo valores con las funciones `int()`, `float()` y `str()`

La línea 15 llama a una nueva función llamada `int()`:

***
<pre>
15.     guess = int(guess)
</pre>
***

La función `int()` toma un argumento y devuelve el valor del argumento como
un entero. Escriba lo siguiente en la consola interactiva para ver cómo la
función `int()` funciona:

***
<pre>
>>> <b>int('42')</b>
42
</pre>
***

La llamada a `int('42')` devolverá el valor entero `42`.

***
<pre>
>>> <b>3 + int('2')</b>
5
</pre>
***

La línea `3 + int('2')` muestra una expresión que usa el valor devuelto por
`int()` como parte de una expresión. Se evalúa al valor entero `5`:

![Ejecución de la expresión 3 + int('2')](https://inventwithpython.com/invent4thed/images/00057.jpeg "Ejecución de la expresión 3 + int('2')")

Aunque puede pasar una cadena de caracteres a `int()`, no se puede pasar
cualquier cadena de caracteres. Pasar `'cuarenta-y-dos'` a `int()` va a
resultar en un error:

***
<pre>
>>> <b>int('cuarenta-y-dos')</b>
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int('cuarenta-y-dos')
ValueError: invalid literal for int() with base 10: 'cuarenta-y-dos'
</pre>
***

La cadena de caracteres que pase a `int()` debe estar formada por números. En
Adivine el número, obtenemos el número de la jugadora usando la función
`input()`. Recuerde que la función `input()` siempre devuelve una *cadena de
caracteres* del texto que la jugadora escribió. Si la jugadora escribe `5`,
La función `input()` devolverá la cadena de caracteres con valor `'5'`, no el
entero con valor `5`. Pero necesitamos comparar el número de la jugadora con
el entero más tarde, y Python no puede usar los operadores de comparación `<` y
`>` para comparar una cadena de caracteres y un valor entero:

***
<pre>
>>> <b>4 < '5'</b>
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    4 < '5'
TypeError: unorderable types: int() < str()
</pre>
***

Entonces, necesitamos convertir la cadena de caracteres a un entero:

***
<pre>
14.     guess = input()
15.     guess = int(guess)
</pre>
***

En la línea 14 asignamos a la variable `guess` el valor de la cadena de
caracteres de cualquier número que la jugadora escribió. En la línea 15
sobreescribimos el valor de la cadena de caracteres en `guess` por un valor
entero devuelto por `int()`. El código `int(guess)` devuelve un nuevo valor
entero basado en la cadena de caracteres brindada, y `guess =` asigna ese
nuevo valor a `guess`. Esto le permite más adelante en el programa escribir
código que compare si `guess` es más grande, más pequeña o igual al número
secreto en la variable `number`.

Las funciones `float()` y `str()` devolverán de forma similar versiones
flotantes o de cadenas de caracteres de los argumentos que se les pasan.
Escriba lo siguiente en la consola interactiva:

***
<pre>
>>> <b>float('42')</b>
42.0
>>> <b>float(42)</b>
42.0
</pre>
***

Cuando la cadena de caracteres `'42`' o el entero `42` se pasan a `float()`,
el flotante `42.0` es devuelto.

Ahora trate usando la función `str()`:

***
<pre>
>>> <b>str(42)</b>
'42'
>>> <b>str(42.0)</b>
'42.0'
</pre>
***

Cuando el entero `42` se pasa a `str()`, la cadena de caracteres `'42'` es
devuelta. Pero cuando el flotante `42.0` se pasa a `str()`, la cadena de
caracteres `42.0` es devuelta.

Usando las funciones `int()`, `float` y `str` puede tomar el valor de un
tipo de datos y devolverlo como un valor de un tipo diferente.

## El tipo de datos booleano

Cada valor en Python pertenece a un tipo de datos. Los tipos de datos que
hemos introducido hasta ahora son enteros, flotantes, cadenas de caracteres y
ahora booleanos. El tipo de datos *booleano* tiene sólo dos valores: `True`
(verdadero, en español) o `False` (falso, en español). Los valores booleanos
deben ser escritos con una T y F mayúsculas, y el resto del valor del nombre
en minúscula.

Los valores booleanos se pueden almacenar en variables, como cualquier otro
tipo de datos:

***
<pre>
>>> <b>spam = True</b>
>>> <b>eggs = False</b>
</pre>
***

En este ejemplo, establece el valor de `spam` a `True` y el valor de `eggs` a
`False`. Recuerde usar la primera letra en mayúscula.

Los valores booleanos (llamados *bools* para hacerlo más corto) se usan con
operadores de comparación para formar condiciones. Cubriremos los operadores
de comparación primero y luego recorreremos las condiciones.

### Operadores de comparación

Los operadores de comparación comparan dos valores y evalúan a un valor
booleanos `True` o `False`. La Tabla 3-1 lista todos los operadores de
comparación.

Tabla 3-1: Operadores de comparación

|Operador | Operación         |
|---------|-------------------|
| `<`     | Menor que         |
| `>`     | Mayor que         |
| `<=`    | Menor o igual que |
| `>=`    | Mayor o igual que |
| `==`    | Igual que         |
| `!=`    | No igual que      |

Ya ha leído sobre los operadores matemáticos `+`, `-`, `*` y `/`. Como
cualquier operador, los operadores de comparación combinan valores para
formar expresiones como `guessesTaken < 6`

La línea 17 del programa de Adivine el número usa el operador de comparación
menor que:

***
<pre>
17.     if guess < number:
</pre>
***

Pronto discutiremos sentencias `if` en más detalle; por ahora, veamos la
expresión que sigue a la palabra clave `if` (la parte de `guess < number`).
Esta expresión contiene dos valores (los valores en las variables `guess` y
`number` conectados por un operadora (el `<`, o signo de menor que).

### Revisando condiciones `True` o `False`

Una *condición* es una expresión que combina dos valores con un operador de
comparación (tal como `<` o `>`) y evalúa a un valor booleano. Una condición
es sólo otro nombre para una expresión que evalúa a `True` o `False`. Un lugar
en el que usamos condiciones es en las sentencias `if`.

Por ejemplo, la condición `guess < number` en la línea 17 pregunta, «¿Es el
valor almacenado en `guess` menor que el valor almacenado en `number`?» Si es
así, entonces la condición evalúa a `True`. Si no, la condición evalúa a
`False`.

Digamos que `guess` almacena el entero `10` y `number` almacena el entero `16`.
Porque `10` es menor que `16`, esta condición evalúa al valor booleano `True`.
La evaluación se vería como así:

![Ejecución de la expresión guess < number](https://inventwithpython.com/invent4thed/images/00058.jpeg "Ejecución de la expresión guess < number")

### Experimentando con booleanos, operadores de comparación y condiciones

Escriba las siguientes expresiones en la consola interactiva para ver sus
resultados booleanos:

***
<pre>
>>> <b>0 < 6</b>
True
>>> <b>6 < 0</b>
False
</pre>
***

La condición `0 < 6` devuelve el valor booleano `True` porque el número - es
menor que el número `6`. Pero, porque `6` no es menor que `0`, la condición
`6 < 0` evalúa a `False`.

Note que `10 < 10` evalúa a `False` porque el número `10` no es menor que el
número `10`:

***
<pre>
>>> <b>10 < 10</b>
False
</pre>
***

Los valores son los mismos. Si Alice tuviera la misma estatura que Bob, no
diríamos que Alice es más alta que Bob, ni que Alice es más baja que Bob.
Ambas sentencias serían falsas.

Ahora, escriba estas expresiones en la consola interactiva:

***
<pre>
>>> <b>10 == 10</b>
True
>>> <b>10 == 11</b>
False
>>> <b>11 == 10</b>
False
>>> <b>10 != 10</b>
False
</pre>
***

En este ejemplo, `10` es igual a `10`, entonces `10 == 10` evalúa a `True`.
Pero `10` no es igual a `11`, entonces `10 == 11` es `False`. Incluso si
invertimos el orden, `11` sigue siendo diferente a `10`, entonces `11 == 10` es
`False`. Finalmente, `10` es igual a `10`, entonces `10 != 10` es `False`.

También puede evaluar sentencias de cadenas de caracteres con operadores de
comparación:

***
<pre>
>>> <b>'Hola' == 'Hola'</b>
True
>>> <b>'Adiós' != 'Hola'</b>
True
>>> <b>'Hola' == 'HOLA'</b>
False
</pre>
***

`'Hola'` es igual a `'Hola'`, entonces `'Hola' == 'Hola'` es `True`. `'Adiós'`
no es igual a `'Hola'`, entonces `'Adiós' != 'Hola'` también es `True`.

Note que la última línea evalúa a `False`. Letras mayúsculas y minúsculas no
son iguales en Python, entonces `'Hola'` no es igual a `'HOLA'`.

Las cadenas de caracteres y valores enteros nunca van a ser iguales entre sí.
Por ejemplo, escriba lo siguiente en la consola interactiva:

***
<pre>
>>> <b>42 == 'Hola'</b>
False
>>> <b>42 != '42'</b>
True
</pre>
***

En el primer ejemplo, `42` es un entero y `'Hola'` es una cadena de caracteres;
entonces los valores no son iguales y la expresión evalúa a `False`. En el
segundo ejemplo, la cadena de caracteres `'42'` aun no es un entero, entonces
la expresión «el entero `42` no es igual a la cadena de caracteres `'42'`»
evalúa a `True`.

### La diferencia entre = y ==

Tenga cuidado de no confundir el operador de asignación, `=`, y el operador de
comparación igual que, `==`. El signo de igual, `=`, se usa en las sentencias
de asignación para almacenar un valor en una variable, mientras que el doble
signo de igual, `==`, se usa en expresiones para ver si dos valores son
iguales. Es fácil usar uno accidentalmente cuando la idea es usar el otro.

Podría ayudarle recordar que ambos el operador de comparación igual que, `==`,
y el operador de comparación no igual que, `!=`, tienen dos caracteres.

## Sentencias if

La línea 17 es una sentencia `if`:

***
<pre>
17.     if guess < number:
18.         print('El valor es muy bajo.') # Ocho espacios al frente de «print»
</pre>
***

El bloque de código que sigue a la sentencia `if` ejecutará si la condición de
la sentencia `if` evalúa a `True`. Si la condición es `False`, el código en el
bloque `if` será saltado. Usando sentencias `if` se puede hacer que el programa
ejecute cierto código sólo cuando uno quiere.

La línea 17 revisa si el número de la jugadora es menor que el número secreto
de la computadora. Si es así, entonces la ejecución se mueve adentro del bloque
`if` en la línea 18 e imprime un mensaje diciéndole a la jugadora que su
intento fue muy bajo.

La línea 20 revisa si el número de la jugadora es mayor que el número secreto:

***
<pre>
20.     if guess > number:
21.         print('El valor es muy alto.')
</pre>
***

Si esta condición es *True*, entonces la llamada a la función `print()` le dirá
a la jugadora que su número es muy alto.

## Saliendo de los ciclos temprano con la sentencia break

La sentencia `if` en la línea 23 revisa si el número que la jugadora adivinó es
igual al número secreto. Si lo es, el programa ejecuta la sentencia `break` en
la línea 24:

***
<pre>
23.     if guess == number:
24.         break
</pre>
***

Una sentencia `break` le dice a la ejecución que salte inmediatamente afuera
del bloque `for` a la primera línea después del final del bloque `for`. La
sentencia `break` se encuentra sólo dentro de ciclos, como en un bloque `for`.

## Revisando si la jugadora ganó

El bloque `for` termina en la siguiente línea de código sin indentación, que es
la línea 26:

***
<pre>
26. if guess == number:
</pre>
***

La ejecución sale del bloque `for` ya sea porque ha hecho el ciclo seis veces
(cuando la jugadora se queda sin intentos) o porque se ha ejecutado la
sentencia `break` en la línea 24 (cuando la jugadora adivina el número de forma
correcta).

La línea 26 revisa si la jugadora adivinó de forma correcta. Si es así, la
ejecución entra en el bloque `if` en la línea 27:

***
<pre>
27.     guessesTaken = str(guessesTaken + 1)
28.     print('¡Buen trabajo, ' + myName + '! ¡Adivinó mi número en ' +
          guessesTaken + ' intentos!')
</pre>
***

Las líneas 27 y 28 ejecutan sólo si la condición el la sentencia `if` en la
línea 26 es `True` (esto es, si la jugadora adivinó de forma correcta el
número de la computadora).

La línea 27 llama a la función `str()`, que devuelve la forma de cadena de
caracteres de `guessesTaken + 1` (ya que la función `range` va de 0 a 5, en
lugar de 1 a 6). La linea 28 concatena cadenas de caracteres para decirle a la
jugadora que ha ganado y cuántos intentos le tomó. Sólo valores de cadenas de
caracteres se pueden concatenar a otras cadenas de caracteres. Esta es la razón
por la que la línea 27 tuvo que cambiar `guessesTaken + 1` a la forma de cadena
de caracteres. De otra forma, tratar de concatenar una cadena de caracteres con
un entero causaría que Python muestre un error.

## Revisando si la jugadora perdió

Si la jugadora se quedó sin intentos, la ejecución irá a esta línea de código:

***
<pre>
30. if guess != number:
</pre>
***

La línea 30 usa el operador de comparación no igual que `!=` para revisar si el
último intento de la jugadora no es igual al número secreto. Si esta condición
evalúa a `True`, la ejecución se mueve dentro del bloque `if` de la línea 31.

Las líneas 31 y 32 están dentro de un bloque `if`, ejecutando sólo si la
condición en la línea 30 es `True`:

***
<pre>
31.     number = str(number)
32.     print('Nop. El número que estaba pensando era ' + number + '.')
</pre>
***

En este bloque, el programa le dice a la jugadora cuál era el número secreto.
Esto requiere concatenar cadenas de caracteres, pero `number` almacena un valor
entero. La línea 31 sobreescribe `number` con una cadena de caracteres, de
forma que pueda se concatenado a las cadenas de caracteres `Nop. El número que
estaba pensando era ` y `.` en la línea 32.

En este punto, la ejecución ha llegado al final del código y el programa
termina. ¡Felicidades! ¡Acaba de programar su primer juego real!

Puede ajustar la dificultad del juego cambiando el número de intentos que la
jugadora tiene. Para darle a la jugadora sólo cuatro intentos, cambie el
código en la línea 12:

***
<pre>
12. for guessesTaken in range(<b>4</b>):
</pre>
***

Al pasar `4` a `range()`, se asegura que el código dentro del ciclo ejecute
cuatro veces en lugar de seis. Esto hace el juego mucho más difícil. Para hacer
el juego más fácil, pase un entero más grande a llamada a la función `range()`.
Esto causará que el ciclo ejecute algunas veces *más* y acepte *más* intentos
de la jugadora.

## Resumen

Programar es sólo la acción de escribir código para programas--esto es, crear
programas que puedan ser ejecutados por una computadora.

Cuando vea a alguien usando un programa de computadora (por ejemplo, jugando su
juego de Adivine el número), todo lo que ve es un poco de texto apareciendo en
la pantalla. El programa decide qué texto mostrar en la pantalla (la *salida*
del programa) basado en sus instrucciones y en el texto que la jugadora escribe
con el teclado (la *entrada* del programa). Un programa es solo una colección
de instrucciones que actúan sobre la entrada de la usuaria.

Hay algunos tipos de instrucciones:

* **Expresiones** son valores conectados por operadores. Las expresiones son
  evaluadas a un único valor. Por ejemplo, `2 + 2` evalúa a `4`, o `'Hello' +
  ' ' + 'World'` evalúa a `'Hello World'`. Cuando las expresiones están al lado
  de las palabras claves `if` y `for` también se les puede llamar
  *condiciones*.

* **Sentencias de asignación** almacenan valores en variables para que pueda
  recordar los valores más adelante en el programa.

* **Las sentencias `if`, `for` y `break`** son sentencias de control de flujo
  que pueden hacer que la ejecución salte instrucciones, haga ciclos sobre
  instrucciones, o se salgan de un ciclo `for`. Las llamadas a funciones
  también pueden cambiar el flujo de la ejecución saltando a instrucciones
  dentro de una función.

* **Las funciones `print()` e `input()`** muestran texto en la pantalla o lo
  obtienen del teclado. Las instrucciones que tratan con la *entrada* y
  *salida* del programa se llaman *I/O* (por «input/output» en ingles,
  pronunciado ai ou).

Eso es todo--sólo esas cuatro cosas. Por supuesto, hay muchos detalles por
aprender acerca de estos cuatro tipos de instrucciones. En capítulos más
adelante leerá sobre más tipos de datos y operadores, más sentencias de control
de flujo, y muchas otras funciones que vienen con Python. Hay también
diferentes tipos de I/O más allá del texto, como la entrada de un ratón y la
salida de sonido y gráficos.

[Previo: Capítulo 2: Escribiendo programas](capitulo2.md) | [Siguiente: Capítulo 4: Un programa que cuenta chistes](capitulo4.md)
