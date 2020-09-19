# 14 Código del César

![Imagen de ciencia](https://inventwithpython.com/invent4thed/images/00016.jpeg)

El programa en este capítulo no es realmente un juego, pero si es divertido sin duda. Este podrá convertir español normal a un código secreto. El programa también podrá convertir códigos secretos de vuelta en español convencional. Solo alguien que conozca la clave a los códigos secretos podrá entender los mensajes. 

Debido a que este programa manipula texto para convertirlo en mensajes secretos, aprenderá varias funciones nuevas y métodos para manipular cadenas. También aprenderá  cómo los programas puede hacer matemática con cadenas de testo como si fueran números. 

---

Temas cubiertos en este capítulo:

* Criptografía y cifrados
* Texto cifrado, texto plano, claves y símbolos
* Encriptar y desencriptar
* El Cifrado César
* El método de cadena `find()`
*  Análisis criptográfico
* La técnica de fuerza bruta

---

## Criptografía y encriptación

La ciencia de escribir códigos secretos se llama *criptografía*. Por miles de años la criptografía ha permitido el envío de mensajes secretos que sólo el emisor y el receptor podían entender, incluso si alguien capturase al mensajero y leyese el mensaje codificado. Un sistema secreto de codificación se llama *cifrado*. El cifrado que usa el programa de este capítulo se llama *cifrado César*.

En criptografía, llamamos *texto plano* al mensaje que queremos mantener en secreto. Digamos que tenemos un mensaje en texto plano que se ve como este:

~~~
Hay una pista detrás del librero. 
~~~

Convertir el texto plano en el mensaje codificado se llama *encriptar* el texto plano. El texto plano se encripta en *texto cifrado*. El texto cifrado se ve como letras aleatorias, de modo que no podemos comprender cómo era el texto plano original solo mirando el texto cifrado. Acá está el ejemplo anterior encriptado en texto cifrado:

~~~
OhF Buh wpzAh klAyáz kls spiylyv.
~~~

Si conoce el cifrado utilizado para encriptar el mensaje, puede *desencriptar* el texto cifrado de vuelta a texto plano. (Desencriptación es lo opuesto a encriptación).

Muchos cifradores usan *claves*, que son valores secretos que le permiten desencriptar textos cifrados que fueron encriptados con un cifrador específico. Piense en el cifrados como un cerrojo de una puerta. Usted solo puede abrir con una llave particular. 

Si usted está interesado en escribir programas criptográficos, usted puede leer mi libro *Hacking Secret Ciphers with Python*. Es libre de descargarlo desde [http://inventwithpython.com/hacking/](https://inventwithpython.com/hacking/).

## Cómo funciona el cifrado Cesar

El cifrado César fue uno de los primeros cifrados inventados. En este cifrado, usted encripta un mensaje reemplazando cada letra en el con una letra "desplazada". En criptografía, las letras encriptadas se llaman *símbolos* porque pueden ser letras, número o cualquier otro signo. Si usted desplaza la letra A en un espacio, obtendrá la letra B. Si usted desplaza la letra A dos espacios, obtendrá la letra C. La Figura 14-1 muestra algunas letras desplazadas tres espacios.

![image](https://inventwithpython.com/invent4thed/images/00109.jpeg)

*Figura 14-1: Un cifrado César desplazando letras tres espacios. Acá, B se convierte en E.*

Para obtener cada letra desplazada, dibuje una fila de cajas con cada letra del alfabeto. Luego dibuje una segunda fila de cajas bajo la primera, pero comience sus letras con un cierto número de espacios después. Cuando llegue al final de las letras del alfabeto, comience de nuevo en la A. La Figura 14-2 muestra un ejemplo con las letras desplazadas tres espacios. 

![image](https://inventwithpython.com/invent4thed/images/00000.jpeg)

*Figura 14-2: El alfabeto completo desplazado tres espacios.*

El número de espacios que usted desplace sus letras (entre 1 y 26) es la clave en el cifrado César. A no ser que usted conozca la llave (el número usado para encriptar el mensaje), no será capaz de desencriptar el código secreto. El ejemplo en la Figura 14-2 muestra las traducciones de cada letra para la clave 3.

*Nota: Si bien existen 26 posibles llaves, Encriptar su mensaje con 26 resultará en un texto crifrado que será exactamente igual al texto plano.*

Si usted encripta la palabra en texto plano "Jaquer" con una llave de 3, entonces:

* La letra "J” se convierte en “M”.
* La letra “a” se convierte en “d”.
* La letra “q” se convierte en “t”.
* La letra “u” se convierte en “x”.
* La letra “e” se convierte en “h”.
* La letra “r” se convierte en “u”.

El texto cifrado de "Jaquer" con clave 3 se convierte en “Mdtxhu”. Para desencriptar “Mdtxhu” con la la clave 3, vamos de las cajas de abajo de vuelta a las de la fila superior.

Si usted quisiera incluir letras minúsculas diferenciadas de las letras mayúsculas, entonces añada otras 26 cajas a las que ya tiene y complételas con las 26 letras minúsculas. Ahora con una clave de 3, la letra Y se convierte en b, cómo se muestra en la figura 14-3.

![image](https://inventwithpython.com/invent4thed/images/00006.jpeg)

*Figura 14-3: El alfabeto completo, ahora incluyendo letras minúsculas, desplazadas por tres espacios.*

El cifrado funciona de la misma forma que como lo hacía con solo letras mayúsculas. De hecho, si usted quiere usar letras de otro alfabeto, usted puede escribir cajas con esas letras para crear su cifrado.

## Ejecución de ejemplo del cifrado César

Acá hay una ejecución de ejemplo de un programa que encripta mensajes utilizando el cifrado César:

~~~python
¿Desea encriptar o desencriptar un mensaje?
**encriptar**
Ingrese su mensaje:
**He aquí el origen de las antiguas historias del país llamado Quiché.**
Ingrese el número de clave (1-52)
**13**
Su texto traducido es:
Ur nDHí ry BEvtrA qr ynF nAGvtHnF uvFGBEvnF qry CníF yynznqB dHvpué.
~~~

Ahora ejecute el programa y desencripte el texto que acaba de encriptar:

~~~Python
¿Desea encriptar o desencriptar un mensaje?
**desencriptar**
Ingrese su mensaje:
**Ur nDHí ry BEvtrA qr ynF nAGvtHnF uvFGBEvnF qry CníF yynznqB dHvpué.**
Ingrese el número de clave (1-52)
**13**
Su texto traducido es:
He aquí el origen de las antiguas historias del país llamado Quiché.
~~~

Si usted no desencripta con la clave correcta, el texto no se desencriptará correctamente:

~~~Python
¿Desea encriptar o desencriptar un mensaje?
**desencriptar**
Ingrese su mensaje:
**Ur nDHí ry BEvtrA qr ynF nAGvtHnF uvFGBEvnF qry CníF yynznqB dHvpué.**
Ingrese el número de clave (1-52)
**15**
Su texto traducido es:
Fc Yosí cj mpgecl bc jYq YlrgesYq fgqrmpgYq bcj nYíq jjYkYbm Osgafé.
~~~

## Código fuente del cifrado César

Ingrese este código fuente para el programa del cifrado César y luego guárdelo el archivo como *cifrado.py*.

Si obtiene errores luego de ingresar este código, compare el código que digitó con el código del libro utilizando la herramienta en línea *diff* en *https://www.nostarch.com/inventwithpython#diff* .

![image](https://inventwithpython.com/invent4thed/images/00020.jpeg)

*cifrado.py*

~~~Python
 1. # Cifrado Cesar
 2. SÍMBOLOS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
 3. TAM_MAX_CLAVE = len(SÍMBOLOS)
 4. 
 5. def obtenerModo():
 6.     while True:
 7.         print('¿Desea encriptar o desencriptar un mensaje?')
 8.         modo = input().lower()
 9.         if modo in ['encriptar', 'e', 'desencriptar', 'd']:
10.             return modo
11.         else:
12.             print('Ingrese "encriptar" o "e" o "desencriptar" o "d".')
13. 
14. def obtenerMensaje():
15.     print('Ingrese su mensaje:')
16.     return input()
17. 
18. def obtenerClave():
19.     clave = 0
20.     while True:
21.         print('Ingrese el número de clave (1-%s)' % (TAM_MAX_CLAVE))
22.         clave = int(input())
23.         if (clave >= 1 and clave <= TAM_MAX_CLAVE):
24.             return clave
25. 
26. def obtenerMensajeTraducido(modo, mensaje, clave):
27.     if modo[0] == 'd':
28.         clave = -clave
29.     traducido = ''
30. 
31.     for símbolo in mensaje:
32.         índiceSímbolo = SÍMBOLOS.find(símbolo)
33.         if índiceSímbolo == -1: # Símbolo no encontrado en SÍMBOLOS.
34.             # Solo añada este símbolo sin cambios.
35.             traducido += símbolo
36.         else:
37.             # Encripta o desencripta.
38.             índiceSímbolo += clave
39. 
40.             if índiceSímbolo >= len(SÍMBOLOS):
41.                 índiceSímbolo -= len(SÍMBOLOS)
42.             elif índiceSímbolo < 0:
43.                 índiceSímbolo += len(SÍMBOLOS)
44. 
45.             traducido += SÍMBOLOS[índiceSímbolo]
46.     return traducido
47. 
48. modo = obtenerModo()
49. mensaje = obtenerMensaje()
50. clave = obtenerClave()
51. print('Su texto traducido es:')
52. print(obtenerMensajeTraducido(modo, mensaje, clave))
~~~

## Estableciendo el largo máximo de la clave

Los proceso de encriptación y desencriptación son el reverso uno del otro, pero comparten buena parte del mismo código. Veamos cómo funciona cada línea:

~~~python
 1. # Cifrado Cesar
 2. SÍMBOLOS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
 3. TAM_MAX_CLAVE = len(SÍMBOLOS)
~~~

`TAM_MAX_CLAVE` es una constante que almacena el largo de `SÍMBOLOS (52)`. Esta constante, nos recuerda que en el programa, la clave usada en el cifrado debe estar siempre entre 1 y 52. 

## Decidiendo si encriptar o desencriptar el mensaje

La función `obtenerModo()` permite a la usuaria decidir si quiere usar el programa en el modo de encriptar o desencriptar:

```Python
 5. def obtenerModo():
 6.     while True:
 7.         print('¿Desea encriptar o desencriptar un mensaje?')
 8.         modo = input().lower()
 9.         if modo in ['encriptar', 'e', 'desencriptar', 'd']:
10.             return modo
11.         else:
12.             print('Ingrese "encriptar" o "e" o "desencriptar" o "d".')
```

La línea 8 llama a `input()` para permitir a la usuaria ingresar el modo que desea. El método `lower()` entonces es llamado en esa cadena para retornar una versión en minúscula de la misma cadena. El valor retornado por `input().lower()` is almacenado en `modo`. La condición de la sentencia `if` comprueba si la cadena almacenada en `modo` existe en la lista `['encriptar', 'e', 'desencriptar', 'd']`.

Esta función retornará la cadena en `modo` siempre y cuando modo sea igual a `encriptar`, `e`, `desencriptar` o `d`. En adelante, `obtenerModo()` retornará la cadena ` modo`. Si la usuaria ingresa algo que no sea `encriptar`, `e`, `desencriptar` o `d`, entonces el bucle `while` le preguntará de nuevo. 

## Obteniendo el mensaje de la jugadora

La función `obtenerMensaje()` simplemente obtiene el mensaje a encriptar o desencriptar de la usuaria y lo retorna:

~~~python
14. def obtenerMensaje():
15.     print('Ingrese su mensaje:')
16.     return input()
~~~

La llamada a `input()` es combinada con el `return` de modo que solo usamos una línea en vez de dos.

## Obteniendo la clave de la jugadora

La función `obtenerClave()` le permite a la jugadora ingresar la clave que usará para encriptar o desencriptar el mensaje:

~~~Python
18. def obtenerClave():
19.     clave = 0
20.     while True:
21.         print('Ingrese el número de clave (1-%s)' % (TAM_MAX_CLAVE))
22.         clave = int(input())
23.         if (clave >= 1 and clave <= TAM_MAX_CLAVE):
24.             return clave
~~~

El bucle `while` asegura que la función se mantendrá en en el bucle hasta que la jugadora ingrese una clave válida. Una clave válida acá es una entre los valores enteros de 1 y 52 (recuerde que `TAM_MAX_CLAVE` es 52 porque hay 52 caracteres en la variable `SÍMBOLOS`). La función `obtenerClave()` retorna esta clave. La línea 22 establece `clave` a la versión entera de lo que la usuaria haya ingresado, así `obtenerClave()` retorna un entero.

## Encriptando o desencriptando el mensaje

La función `obtenerMensajeTraducido()` realiza el encriptado y desencriptado:

~~~Python
26. def obtenerMensajeTraducido(modo, mensaje, clave):
27.     if modo[0] == 'd':
28.         clave = -clave
29.     traducido = ''
~~~

Tiene tres parámetros:

**modo** Esta establece en la función el modo de encriptación o el modo desencriptación.

**mensaje** Esta es el texto plano (o texto cifrado) que será encriptado (o desencriptado).

**clave** Esta es la clave usada en el cifrado.

La línea 27 comprueba si la primera letra en la variable `modo` es la cadena `d`. Si es así, entonces el programa está en modo desencriptado. La única diferencia entre el modo desencriptación y encriptación es que en modo desencriptación, la clave es establecida a la versión negativa de sí misma. Por ejemplo, si la `clave` es el entero 22, entonces el modo desencriptación la establece en `-22`. La razón es explicada en "Encriptando o desencriptando cada letra" en la página 205.

La variable `traducida` contendrá la cadena del resultado: ya sea el texto cifrado (si usted está encriptando) o texto plano (si usted está desencriptando). La variable comienza como una cadena vacía y los caracteres encriptados o desencriptados se concatenarán al final de ella. Antes de que podamos comenzar a concatenar caracteres en `traducida`, sin embargo, necesitamos encriptar o desencriptar el texto, lo que haremos en el resto de `obtenerMensajeTraducido()`.

## Encontrando las cadenas pasadas con el método de cadena `find()`

Con el objetivo de desplazar las letras para encriptar o desencriptar, primero necesitamos convertirlas en números. El número de cada letra en la cadena `SÍMBOLOS` será el índice donde esta aparece. Como la letra `A`está en  `SÍMBOLOS[0]`, el número `0` representará la A mayúscula. Si quisieramos encriptarla con la clave `3`, nosotros simplemente usaremos `0 + 3` para obtener el índice de la letra encriptada: `SÍMBOLOS[3]` o `'D'`.

Usaremos el método de cadena `find()`, el cual encuentra la primera ocurrencia de una cadena pasada, en la cadena en la cual se llama el método. Ingrese lo siguiente en la «shell» interactiva:

~~~Python
>>> '¡Hola mundo!'.find('H')
1
>>> '¡Hola mundo!'.find('o')
2
>>> '¡Hola mundo!'.find('mun')
6
~~~

`'¡Hola mundo!'.find('¡')` retorna `0` porque el signo `¡` es encontrado en en el primer índice de la cadena `¡Hola mundo!`. Recuerde, los índices comienzan en `0` y no en `1`. El código `¡Hola mundo!'.find('o')` retorna 2 porque la `'o'` minúscula es encontrada por primera vez en la palabra `Hola`.  El método `find()` deja de mirar luego de hallar la primera ocurrencia, de modo que la segunda `'o'` en la palabra `mundo` no importa. Usted también puede encontrar cadenas con más de un caracter. La cadena `'mun'` es encontrada iniciando en el índice `6`.

Si la cadena pasada no puede ser encontrada, el método `find()` retorna `-1`:

~~~Python
>>> '¡Hola mundo!'.find('xyz')
-1
~~~

Volvamos al programa de cifrado César. La línea 31 es un bucle `for` que itera sobre cada caracter en la cadena `mensaje`:

~~~Python
31.     for símbolo in mensaje:
32.         índiceSímbolo = SÍMBOLOS.find(símbolo)
33.         if índiceSímbolo == -1: # Símbolo no encontrado en SÍMBOLOS.
34.             # Solo añada este símbolo sin cambios.
35.             traducido += símbolo
~~~

El método `find()` es usado en la línea 32 para obtener el índice de la cadena en `símbolo`. Si `find()` retorna `-1`, el caracter en `símbolo` simplemente será añadido a la cadena `traducido` sin ningún cambio. Esto significa que cualquier caracter que no sea parte del alfabeto, como comas y puntos, no será cambiado.

## Encriptando o desencriptando cada letra

Una vez que haya encontrado el número de índice de la letra, agregar la clave al número actuará como desplazamiento y le dará el índice de la letra encriptada.

La línea 38 hace esta suma para obtener la letra encriptada (o desencriptada):

~~~Python
37.             # Encripta o desencripta.
38.             índiceSímbolo += clave
~~~

Recuerde que en la línea 28, hicimos negativo el valor entero de  la `clave` para desencriptar. El código que suma la clave ahora la restará, ya que sumar un número negativo es lo mismo que una resta. 

Sin embargo, si esta suma (o resta, si la `clave` es negativa) provoca que `índiceSímbolo` vaya más allá del último índice de `SÍMBOLOS`, necesitaremos volver a comenzar en el inicio de la lista en `0`. Esto es manejado por la sentencia `if` comenzando en la línea 40:

~~~Python
40.             if índiceSímbolo >= len(SÍMBOLOS):
41.                 índiceSímbolo -= len(SÍMBOLOS)
42.             elif índiceSímbolo < 0:
43.                 índiceSímbolo += len(SÍMBOLOS)
44. 
45.             traducido += SÍMBOLOS[índiceSímbolo]
~~~

La línea 40 comprueba si `índiceSímbolo` ha sobrepasado el último índice al compararlo con el largo de la cadena `SÍMBOLOS`. Si lo ha sobrepasado, la línea 41 resta el largo de `SÍMBOLOS` de `índiceSímbolo`. Si `índiceSímbolo` ahora es negativo, entonces el índice tiene que volver a comenzar  en el otro lado de la cadena `SÍMBOLOS`. La línea 42 comprueba si el valor de `índiceSímbolo` es negativo después de sumar la clave de encriptación. Si es así, la línea 43 suma el largo de `SÍMBOLOS` a `índiceSímbolo`.

La variable `índiceSímbolo` ahora contiene el índice del símbolo correctamente encriptado o desencriptado. `SÍMBOLO[índiceSímbolo]` apuntará al caracter para éste índice, y este caracter es añadido al final de `traducida` en la línea 45. 

La ejecución del bucle regresa a la línea 31 para repetir esto para el siguiente caracter en `mensaje`. Una vez que el bucle está finalizado, la función retorna la cadena encriptada (o desencriptada) en `traducido` en la línea 46. 

~~~Python
46.     return traducido
~~~

La última línea en la función `obtenerMensajeTraducido()` retorna la cadena `traducido`. 



## Iniciando el programa

El inicio del programa llama a cada una de las funciones definidas previamente para obtener el `modo`, `mensaje` y `clave` de la usuaria:

~~~Python
48. modo = obtenerModo()
49. mensaje = obtenerMensaje()
50. clave = obtenerClave()
51. print('Su texto traducido es:')
52. print(obtenerMensajeTraducido(modo, mensaje, clave))
~~~

Estos tres valores son pasado a `obtenerMensajeTraducido()` cuyo valor de retorno (la cadena `traducido`) es impresa a la usuaria.

---

# Expandiendo los símbolos

Si usted quiere encriptar números, espacios y signos de puntuación, solo añádalos a la cadena `SÍMBOLOS` en la línea 2. Por ejemplo, usted podría tener su programa de cifrado encriptando números, espacios y signos de puntuación al cambiar la línea 2 de la siguiente forma:

~~~Python
2. `SÍMBOLOS` = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 1234567890!@#$%^&*()'
~~~

Note que la cadena `SÍMBOLOS` tiene un caracter de espacio después de la `z` minúscula.

Si quisiera, usted puedría incluso añadir más caracteres a esta lista. Y usted no necesita modificar el resto del programa, ya que todas las líneas de código que requieren de la lista de caracteres símplemente utilizan la constante `SÍMBOLOS`.

Sólo asegúrese de que cada caracter aparezca sólo una vez en la cadena. También, usted necesitará desencriptar su mensaje con la misma cadena de `SÍMBOLOS` con la cual fue encriptado. 

---

## La técnica de fuerza bruta

Esa es el cifrado César como un todo. Sin embargo, mientras este cifrado puede engañar a algunas personas que no entienden de criptografía, esta no mantendrá un mensaje secreto de alguien que sabe de *análisis criptográfico*. Mientras la criptografía es la ciencia de hacer códigos, el análisis criptográfico es la ciencia de romper códigos. 

Todo el punto de la criptografía es asegurarnos de que si alguien obtiene el mensaje encriptado, esta persona no pueda descubrir el texto original.

Pretendamos que somos quien rompe el código y todo lo que tenemos este este texto encriptado:

~~~
LwCjBA uiG vwB jm xtmiAivB, jCB kmzBiqvBG qA ijACzl.
~~~

*Fuerza bruta* es la técnica de tratar cada posible clave hasta que usted encuentre la correcta. Debido a que hay solo 52 claves posibles, será fácil para un analista criptográfico escribir un programa jaquer para desencriptar con cada clave posible. Entonces podrán ver cuál es la clave que desencripta en español plano. Añadamos la característica de fuerza bruta  al programa.

## Añadiendo modo de fuerza bruta

Primero, cambie las líneas 7, 9 y 12, la cuales están en la función `obtenerModo()`, para que se vean como las siguientes:

~~~Python
 5. def obtenerModo():
 6.     while True:
 7.         print('¿Desea encriptar, desencriptar o aplicar fuerza bruta a un mensaje?')
 8.         modo = input().lower()
 9.         if modo in ['encriptar', 'e', 'desencriptar', 'd', 'fuerza', 'f']:
10.             return modo
11.         else:
12.             print('Ingrese "encriptar" o "e", "desencriptar" o "d" o "fuerza" o "f".')
~~~

Este código permitirá a la usuaria seleccionar fuerza bruta como un modo.

A continuación, haga los siguiente cambios en la parte principal del programa:

~~~Python
48. modo = obtenerModo()
49. mensaje = obtenerMensaje()
50. if modo[0] != 'f':
51.     clave = obtenerClave()
52. print('Su texto traducido es:')
53. if modo[0] != 'f':
54.     print(obtenerMensajeTraducido(modo, mensaje, clave))
55. else:
56.     for clave in range(1, TAM_MAX_CLAVE + 1):
57.         print(clave, obtenerMensajeTraducido('desencriptar', mensaje, clave))
~~~

Si la usuaria no está en modo fuerza bruta, se le preguntará por una clave, la llamada original a `obtenerMensajeTraducido()` se realizada, y la cadena traducida es impresa.

Sin embargo, si la usuaria está en modo fuerza bruta, entonces el bucle de `obtenerMensajeTraducido()` itera de 1 hasta `TAM_MAX_CLAVE` (el cual es 52). Recuerde que la función `range()` retorna una lista de enteros de hasta, pero sin incluir, el segundo parámetro, la razón por la cual necesitamos sumar `+ 1`. El programa entonces imprimirá cada posible traducción del mensaje (incluyendo el número de clave utilizado en la traducción).

Acá hay un ejemplo de la ejecución de este programa modificado:

~~~Python
¿Desea encriptar, desencriptar o aplicar fuerza bruta a un mensaje?
fuerza
Ingrese su mensje:
IAí, xCmA, Bwlw Am ikijó xizi twA lmt YCqkpé, yCm pwG Am ttiui aivBi KzCH.
Su texto traducido es:
1 Hzí, wBlz, Avkv zl hjhió whyh svz kls XBpjoé, xBl ovF zl sshth ZhuAh JyBG.
2 Gyí, vAky, zuju yk gighó vgxg ruy jkr WAoiné, wAk nuE yk rrgsg Ygtzg IxAF.
3 Fxí, uzjx, ytit xj fhfgó ufwf qtx ijq Vznhmé, vzj mtD xj qqfrf Xfsyf HwzE.
4 Ewí, tyiw, xshs wi egefó teve psw hip Uymglé, uyi lsC wi ppeqe Werxe GvyD.
5 Dví, sxhv, wrgr vh dfdeó sdud orv gho Txlfké, txh krB vh oodpd Vdqwd FuxC.
6 Cuí, rwgu, vqfq ug cecdó rctc nqu fgn Swkejé, swg jqA ug nncoc Ucpvc EtwB.
7 Btí, qvft, upep tf bdbcó qbsb mpt efm Rvjdié, rvf ipz tf mmbnb Tboub DsvA.
8 Así, pues, todo se acabó para los del Quiché, que hoy se llama Santa Cruz.
9 zrí, otdr, sncn rd ZbZaó oZqZ knr cdk Pthbgé, ptd gnx rd kkZlZ RZmsZ Bqty.
10 yqí, nscq, rmbm qc YaYZó nYpY jmq bcj Osgafé, osc fmw qc jjYkY QYlrY Apsx.
11 xpí, mrbp, qlal pb XZXYó mXoX ilp abi NrfZeé, nrb elv pb iiXjX PXkqX zorw.
12 woí, lqao, pkZk oa WYWXó lWnW hko Zah MqeYdé, mqa dku oa hhWiW OWjpW ynqv.
--recortado--
~~~

Después de mirar cada fila, usted puede ver que el octavo mensaje no es sin sentido si no que es texto plano en Español. El análisis criptográfico puede deducir que la clave original para el texto encriptado tiene que haber sido 8. El método de fuerza bruta habría sido difícil de realizar en los días de Julio César y el Imperio Romano, pero hoy tenemos computadoras que rápidamente pueden probar millones o inclusive miles de millones de claves en un corto tiempo. 

*nota de la traducción:* el código de cifrado modificado para añadir fuerza bruta se encuentra en el archivo [cifrado2.py](código/cifrado2.py). 

# Resumen

La computadoras son buenas haciendo matemática. Cuando creamos un sistema para traducir alguna pieza de información a números (como lo hacemos con texto y ordinales o con espacio y sistemas de coordenadas), los programas computacionales pueden procesar estos número rápidamente y eficientemente. Una buena parte de escribir programas es descubrir cómo representar la información que usted quiere manipular como valores que Python pueda comprender.

Mientra que nuestro programa de cifrado César puede encriptar mensajes que los mantendrán secretos de personas que tienen que descubrirlos utilizando papel y lápiz, el programa no los mantendrá secretos de persona que conozcan cómo hacer que las computadoras procesen información. (Nuestro modo de fuerza bruta prueba esto.)

En el capítulo 15, crearemos un Reversegam (también conocido como Reversi o Otelo). La IA que juega este juego es mucho más avanzada que la IA que jugaba Tres en línea en el capítulo 10. De hecho, ¡es tan buena que muchas veces usted no le podrá ganar!

[Previo: Capítulo 13: Búsqueda del tesoro con sonar ](capitulo13.md) | [Siguiente: Capítulo 15:  El juego Reversegam ](capitulo15.md)

