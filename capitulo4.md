# 4 Un programa que cuenta Chistes

![Matraz de Erlenmeyer](https://inventwithpython.com/invent4thed/images/00016.jpeg "Matraz de Erlenmeyer")

Este capítulo le cuenta algunos chistes a las personas usuarias y les demuestra algunas maneras avanzadas de usar cadenas de caracteres usando la función `print()`. La mayoría de los juegos en este libro tendrán un texto simple de entrada y salida. La entrada es escrita por la usuaria usando el teclado y la salida es el texto mostrado en la pantalla.


***
Temas cubiertos en este capítulo:
* Caracteres de escape
* Uso de comillas simples y dobles para manejo de cadenas de caracteres
* Uso del argumento palabra clave «end» de la función `print()` para evitar nuevas lineas
***

Ya aprendió cómo mostrar una salida de texto simple usando la función `print()`. Ahora vamos a profundizar y veremos cómo las cadenas de caracteres y `print()` funcionan en Python.

## Ejecución de ejemplo de Chistes

Esto es lo que la usuaria ve cuando ejecuta el programa Chistes:

***
<pre>
¿Qué sale de la cruza entre un mono y un pato?
¡Un monopatín!
¿Porqué vuelan los pájaros pa'l sur?
¡Porque caminando tardarían muchísimo!
¿En qué se parecen una familia, un bombero y un barco?
No sé... ¿en qué se parecen?
En que el bombero y el barco tienen casco.
¿Y la familia? -Bien, gracias.
</pre>

***

## Código fuente del programa chistes

Abra una nueva ventana de edición de archivos haciendo clic en **Archivo->Nueva Ventana**. En la nueva ventana que aparece, agregue el código fuente y guardelo como chistes.py. Luego corra el programa presionando F5.

![Python 3](https://inventwithpython.com/invent4thed/images/00060.jpeg "Python3")

Si obtiene errores después de escribir este código, compárelo con el código del libro con la herramienta diff en línea en http://invpy.com/es/diff/chistes.

***
<pre>
<b>chistes.py</b>

 1. print('¿Qué sale de la cruza entre un mono y un pato?')
 2. input()
 3. print('¡Un monopatín!')
 4. print()
 5. print('¿Porqué vuelan los pájaros pa\'l sur?')
 6. input()
 7. print('¡Porque caminando tardarían muchísimo!')
 8. print()
 9. print('¿En qué se parecen una familia, un bombero y un barco?')
10. input()
11. print("No sé... ¿en qué se parecen?")
12. input()
13. print('En que el bombero y el barco tienen casco.')
14. input()
15. print('¿Y la familia?', end='')
16. print(' -Bien, gracias.')
</pre>

***

## ¿Cómo funciona el código?
Empecemos por ver las primeras cuatro líneas de código:
***
<pre>
 1. print('¿Qué sale de la cruza entre un mono y un pato?')
 2. input()
 3. print('¡Un monopatín!')
 4. print()
</pre>

***

Las líneas de la 1 a la 3 usan las llamadas a la función `print()` para preguntar y responder al primer chiste. No se quiere que la usuaria lea de inmediato la respuesta del chiste, por lo que se usa una llamada a la función `input()` después del primer `print()`. De esta manera la usuaria leerá la primera línea del chiste, presionará INTRO, y luego leerá la respuesta.

La persona usuaria podría escribir una cadena de caracteres y presionar INTRO, pero esa cadena de caracteres no estará siendo almacenada en ninguna variable. El programa tan solo la olvidará y se moverá a la siguiente línea de código.

La última llamada a la función `print()` no tiene argumento de cadena de caracteres. Esto le indica al programa que solo imprima una línea en blanco. Las líneas en blanco son útiles para evitar que el texto quede unido.

## Caracteres de escape

Las líneas de la 5 a la 8 imprimen la pregunta y la respuesta del siguiente chiste:
***
<pre>
 5. print('¿Porqué vuelan los pájaros pa\'l sur?')
 6. input()
 7. print('¡Porque caminando tardarían muchísimo!')
 8. print()
</pre>

***

En la línea 5 hay una barra invertida justo antes de la comilla simple (note que `\` es una barra invertida y que `/` es barra inclinada). Esta barra invertida indica que la letra que se encuentra justo después es un «carácter de escape» . Un *carácter de escape* le permite imprimir caracteres especiales que son difíciles o imposibles de ingresar al código fuente, como la comilla simple en una cadena de caracteres que empieza y termina con comillas simples.
En este caso, si no incluimos la barra invertida, la comilla simple en `pa\'l` se hubiera interpretado como el final de la cadena de caracteres. Pero esta comilla necesita ser parte de la cadena de caracteres. La comilla simple con escape le indica a Python que debe incluir la comilla simple en la cadena de caracteres.

Ahora, ¿cómo se podría mostrar una barra invertida? Si se ejecuta la siguiente línea de código desde una consola, no funcionaría:

Vaya de su programa chistes.py hacia la consola interactiva y escriba esta sentencia `print()`:

***
<pre>
<b>>>> print('Ellas se fueron volando en un helicóptero verde\turquesa.')</b>
Ellas se fueron volando en un helicóptero verde    urquesa.
</pre>

***

Esta instrucción no imprimió la barra invertida porque la `t` en `turquesa` fue interpretada como un carácter de escape debido a que estaba después de una barra invertida. El carácter de escape `\t` simula la presión de la tecla TAB del teclado.

Esta línea le dará la salida correcta:

***
<pre>
<b>>>> print('Ella se fueron volando en un helicóptero verde\\turquesa.')</b>
Ellas se fueron volando en un helicóptero verde\turquesa.
</pre>

***

De esta manera el `\\` es un carácter de barra invertida y no hay un `\t` que intepretar como un TAB.


La tabla 4-1 es una lista de algunos caracteres de escape en Python, incluyendo `\n`, que es el carácter de escape de nueva línea que ha usado antes.

**Tabla 4-1:** Caracteres de Escape

|Carácter de escape | Lo que imprime |
|---------|----------------|
| `\\`     | Barra invertida (\)           |
| `\'`     | Comilla simple (')          |
| `\"`     | Comilla doble (") |
| `\n`     | Nueva línea       |
| `\t`     | Tabulador       |

Existen más caracteres de escape en Python, pero estos son los caracteres que más probablemente va a necesitar durante la creación de juegos.

## Comillas Simples y Dobles
Mientras todavía estamos en una consola interactiva, veamos un poco más a fondo a las comillas. Las cadenas de caracteres no siempre tienen que estar entre comillas simples en Python. También se pueden poner entre comillas dobles. Estas dos líneas imprimen la misma cosa:
***
<pre>
<b>>>> print('Hola Mundo')</b>
Hola Mundo
<b>>>> print("Hola Mundo")</b>
Hola Mundo
</pre>

***

Pero no se pueden mezclar las comillas simples con las dobles. Esta siguiente línea va le dará un error porque usa ambas comillas al mismo tiempo:

***
<pre>
<b>>>> print('Hola mundo")</b>
SyntaxError: EOL while scanning single-quoted string
</pre>

***

Personalmente prefiero usar comillas simples para no tener que mantener presionada la tecla SHIFT para escribirlas. Son más fáciles de escribir y a Python no le importa cuál de las dos usemos.

También note que al igual que necesita la barra invertida `\'`, para tener una comilla simple en una cadena de caracteres encerrada entre comillas simples, también va a necesitar la barra invertida `\"` para poder tener comillas dobles en una cadena de caracteres encerrada por comillas dobles. Veamos este ejemplo:

***
<pre>
<b>>>> print('Le pedí prestado el carro a Pedro pa\'ir al pueblo. Él dijo, "Seguro."')</b>
Le pedí prestado el carro a Pedro pa'ir al pueblo. Él dijo, "Seguro."
</pre>

***

Se usan comillas simples para encerrar a una cadena de caracteres, por lo que es necesario agregar una barra invertida antes de la comilla simple en `pa'ir`. Pero las comillas dobles en `"Seguro"` no necesitan una barra invertida. El intérprete de Python tiene inteligencia suficiente para saber que si una cadena de caracteres comienza con un tipo de comillas, el otro tipo de comillas no significa que la cadena de caracteres está terminada.

Ahora veamos este otro ejemplo:

***
<pre>
<b>>>> print("Ella dijo, \"No puedo creer que lo dejaste llevarse el carro pa'l pueblo\"")</b>
Ella dijo, "No puedo creer que lo dejaste llevarse el carro pa'l pueblo"
</pre>

La cadena de caracteres está encerrada entre comillas dobles, por lo que es necesario agregar barras invertidas para toda las comillas dobles que se encuentren dentro de la cadena de caracteres. No es necesario escapar la comilla simple usada en `pa'l.

Para resumir, en las cadenas de caracteres de comilla simple, no es necesario escapar las comillas dobles pero es necesario escapar las comillas simples, y en las cadenas de caracteres de comilla doble, no es necesario escapar las comillas simples pero sí las comillas dobles.

***

## El parámetro de palabra clave `end` de la función print()

Ahora regresemos al archivo chistes.py y veamos las líneas de la 9 a las 6:

***
<pre>
 9. print('¿En qué se parecen una familia, un bombero y un barco?')
10. input()
11. print("No sé... ¿en qué se parecen?")
12. input()
13. print('En que el bombero y el barco tienen casco.')
14. input()
15. print('¿Y la familia?', end='')
16. print(' -Bien, gracias.')
</pre>

***

¿Notó del segundo parámetro en la función `print()` de la línea 15?. Normalmente, `print()` añade una nueva línea al final de la cadena de caracteres que imprime. Por esta razón, una función `print()` en blanco tan solo imprimirá una nueva línea. Pero la función `print()` tiene la opción de un segundo parámetro (que tiene nombre `end` (fin en inglés)).

Recuerde que un argumento es un valor que se le pasa a una llamada a función. La cadena en blanco que se le pasa a la función `print()` se llama *argumento de palabra clave*. El `end` que se encuentra en el `end=''` se llama *parámetro de palabra clave*. Para pasar un argumento de palabra clave a este parámetro de palabra clave, debe escribir la palabra `end=` al antes de este.
Cuando ejecutamos esta sección de código, la salida sería:

***
<pre>
¿En qué se parecen una familia, un bombero y un barco?
No sé... ¿en qué se parecen?
En que el bombero y el barco tienen casco.
¿Y la familia? -Bien, gracias.
</pre>

***

Pasando una cadena de caracteres en blanco usando `end`, la función `print()` no añadirá una nueva linea al final de la cadena de caracteres, en lugar de esto añadirá una cadena de caracteres en blanco. Por esta razón ' `-Bien, gracias.'` aparece junto a la línea anterior, en lugar de en una nueva línea. No hubo una nueva línea después de que fue imprimida la cedena de caracteres `'¿Y la familia?'`.

## Resumen

Este capítulo explora las diferentes formas en las que se puede usar la función `print()`. Los caracteres de escape se usan para los caracteres que son difíciles o imposibles de escribir en el código usando el teclado. Si quiere usar caracteres especiales como parte de una cadena de caracteres, debe usar una barra invertida (`\`) seguida de una sola letra para el carácter de escape. Por ejemplo, `\n` sería una nueva línea. Para incluir una barra invertida en una cadena de caracteres, deberá usar el carácter de escape `\\`.

La función `print()` añade automáticamente un carácter de una nueva línea al final de la cadena de caracteres que se pasa para imprimir en pantalla. La mayor parte del tiempo, es un atajo útil. Pero a veces no quieres un carácter de una nueva línea al final. Para cambiar esto, puedes pasar el argumento de palabra clave `end` con una cadena de caracteres en blanco. Por ejemplo, para imprimir `spam` en la pantalla sin un carácter de una nueva línea, podría hacer el llamado `print('spam', end='')`.

[Previo: Capítulo 3: Adivine el número](capitulo3.md) | [Siguiente: Capítulo 5: Reino de Dragones](capitulo5.md)
