# 12 El sistema de coordenadas cartesianas

![Imagen de ciencia](https://inventwithpython.com/invent4thed/images/00016.jpeg)

Este capítulo repasa algunos conceptos matemáticos simples que usará en el resto de este libro. En juegos bidimensionales (2D), los gráficos en la pantalla pueden moverse a la izquierda o derecha y arriba o abajo. Estos juegos necesitan una forma de traducir un lugar en la pantalla a enteros con los cuales el programa pueda lidiar. 

Acá es donde el *sistema de coordenadas Cartesianas* entra. Las *coordenadas* son números que representan un punto específico en la pantalla. Estos números pueden ser almacenados como enteros en las variables de sus programas. 

---
Temas cubiertos en este capítulo:

* Sistema de coordenadas Cartesianas
* Eje X y eje Y
* Números negativos
* Píxeles
* La propiedad conmutativa de la suma
* Valores absolutos y la función `abs()`
---

## Cuadrículas y coordenadas cartesianas

Una manera común de referirse a un lugar específicos en un tablero de ajedrez es marcando cada fila y columna con letras y números. La Figura 12-1 muestra un tablero de ajedrez que tiene cada fila y columna marcada.

![](https://inventwithpython.com/es/12_files/image002.png)
*Figura 12-1: Un ejemplo de tablero de ajedrez con un caballo negro en (a,4) y un caballo blanco en (e,6).*

Una coordinada para un espacio en el tablero de ajedrez es una combinación de una fila y una columna. En ajedrez, la ficha del caballo luce como una cabeza de caballo.  El caballo blanco en la Figura 12-1 está localizado en el punto (e,6) ya que está en la columna e y en la fila 6, y el caballo negro está localizado en el punto (a, 4) porque está en la columna a y en la fila 4. 

Puede pensar en un tablero de ajedrez como un sistema de coordenadas Cartesiano. Al utilizar una etiqueta para las filas y una etiqueta para las columnas, usted puede dar una coordenada que es para un, y únicamente un, espacio en el tablero. Si usted ha aprendido sobre sistemas de coordenadas Cartesianas en sus clase de matemática, usted sabrá que los números son utilizados para tanto las filas como las columnas. Un tablero de ajedrez usando coordenadas numéricas se vería como en la Figura 12-2.

Los números yeando a la izquierda y la derecha a lo largo de las columnas son parte del *eje X*. Los números yendo arriba y abajo a lo largo del las filas son parte del *eje Y*. Las coordenadas son siempre son descritas con la coordinada X primero, seguida de la coordenada Y. En la Figura 12-2, la coordenada X para el caballo blanco es 5 y la coordenada Y es 6, de modo que el caballo blanco está ubicado en la coordenada (5, 6) y no en la (6, 5). De manera similar, el caballo negro está localizado en la coordenada (1, 4), no en la (4, 1),  ya que la coordenada X del caballo negro es 1 y la su coordenada Y es 4.

![](https://inventwithpython.com/es/12_files/image003.png)
*Figura 12-2: El mismo tablero de ajedrez pero con coordenadas numéricas para tanto las filas como las columnas*

Note que para que el caballo negro se mueva a la posición del caballo blanco, el caballo negro debe moverse dos espacios hacia arriba y cuatro espacios a la derecha. Pero usted no necesita mirar el tablero para descubrir esto. Si usted sabe que el caballo blanco está ubicado en (5, 6) y el caballo negro está ubicado en (1, 4), usted puede usar una resta para descubrir esta información. 

Reste la coordenada X del caballo negro a la coordenada X del caballo blanco: 5 - 1 = 4. El caballo negro se tiene que mover a lo largo del eje X por cuatro espacios. Ahora reste la coordenada Y del caballo negro a la coordenada Y del caballo blanco: 6 - 4 = 2. El caballo negro se tiene que mover a lo largo del eje Y por dos espacios.

Haciendo alguna matemática con los números de las coordenadas, usted puede descubrir las distancias entre dos coordenadas.

## Números negativos

Las coordenadas cartesianas también usan *números negativos, números* que son menos que cero. Un signo de menos en frente de un número muestra que es negativo: -1 es menos que 0. Y -2 es menos que -1. Pero 0 en sí mismo no es positivo ni negativo. En la Figura 12-3, usted puede ver los números positivos incrementando hacia la derecha y los números negativos decrementando hacia la izquierda en una línea numérica. 

![](https://inventwithpython.com/es/12_files/image004.png)
*Figura 12-3: una línea numérica con números positivos y negativos.*

La línea numérica es útil para ver la resta y la suma. Usted puede pensar en la expresión 4 + 3 como el caballo blanco iniciando en la posición 4 y moviéndose 3 espacios a la derecha. Como puede ver en la Figura 12-4, el caballo blanco finaliza en la posición 7. Esto tiene sentido porque, 4 + 3 es 7.

![](https://inventwithpython.com/es/12_files/image005.png)
*Figura 12-4: Mover el caballo blanco a la derecha suma a la coordenada.*

Usted resta al mover el caballo blanco a la izquierda. De modo que si la expresión es 4 - 6, el caballo blanco inicia en la posición 4 y se mueve 6 espacios a la izquierda, como se muestra en la Figura 12-5.

![](https://inventwithpython.com/es/12_files/image006.png)
*Figura 12-5: Mover el caballo blanco a la izquierda resta a la coordenada.*

El caballo blando finaliza en la posición -2. Eso quiere decir que 4 - 6 igual -2. 

Si usted suma o resta un número negativo, el caballo blanco se mueve en la dirección *opuesta* que cuando lo hace con números positivos. Si usted suma un número negativo, el caballo se mueve a la *izquierda*. Si usted resta un número negativo, el caballo se mueve a la *derecha*. La expresión -1 - (-4) sería igual a 3, como se muestra en la Figura 12-6. Note que -1 - (-4) tiene la misma respuesta que -1 + 4. 

![](https://inventwithpython.com/invent4thed/images/00101.jpeg)
*Figura 12-6: El caballo inicia en -1 y se mueve a la derecha 4 espacios.*

Usted puede pensar en el eje X como una línea numérica. Añada otra línea numérica yendo hacía arriba y abajo para el eje Y. Si usted pone estas dos líneas numéricas juntas, usted tiene un sistema de coordenadas Cartesianas como el de la Figura 12-7.

Sumando un número positivo (o restando un número negativo) movería el caballo hacía arriba en el eje Y o a la derecha en el eje X, y restando un número positivo (o sumando un número negativo) movería el caballo hacía abajo en el eje Y o a la izquierda en el eje X. 

La coordenada (0, 0) en el centro es llamada *origen*. Usted puede haber usado un sistema de coordenadas como este en su clase de matemática. Como está a punto de ver, los sistemas de coordenadas como este tiene mucho pequeños trucos que usted puede usar para que sea más fácil descubrir las coordenadas. 

![](https://inventwithpython.com/es/12_files/image008.png)
*Figura 12-7: Poner dos líneas numéricas juntas crea un sistema de coordenadas Cartesianas.*

## El sistema de coordinadas de una pantalla de computadora

La pantalla de su computadora está hecha de *píxeles*, el punto de color más pequeño que una pantalla puede mostrar. Es común que las pantallas de computadora usen sistemas de coordenadas que tienen el origen (0, 0) en la esquina superior izquierda y que incrementa yendo hacia abajo y a la derecha. Usted puede ver esto en la Figura 12-8, la cual muestra una computadora portátil con una pantalla con resolución que es de 1920 píxeles de ancho y 1080 píxeles de alto. 

No hay coordenadas negativas. La mayoría de gráficos por computadora usan este sistema de coordenadas para los píxeles en la pantalla, y usted lo usará en este libro de juegos. Para programar, es importante saber cómo trabaja el sistema de coordenadas, tanto el modo utilizado para las matemáticas como el modo utilizado para las pantallas de computadora. 

![](https://inventwithpython.com/es/12_files/image013.jpg)

*Figura 12-8: El sistema de coordenadas Cartesianas en una pantalla de computadora.*

## Trucos matemáticos

Restar y sumar números negativos es fácil cuando usted tiene una recta numérica frente a usted. Eso también puede ser sencillo sin una recta numérica. Acá hay tres trucos para ayudarle a sumar y restar números negativos por su cuenta. 

### Truco 1: Un menos se come un signo de suma a su izquierda

Cuando usted ve un signo de menos con un signo de suma a su izquierda, usted puede reemplazar el signo de suma con el signo de resta. Imagine el signo de menos "comiéndose" el signo de suma a su izquierda. La respuesta seguirá siendo la misma, porque sumar un valor negativo es lo mismo que restar un valor positivo. De modo que 4 + -2 y 4 - 2 ambos evalúan a 2, como puede ver acá:

![](https://inventwithpython.com/invent4thed/images/00008.jpeg)

### Truco 2: Dos restas se combinan en una suma

Cuando usted ve dos signos de resta uno al lado del otro, sin un número entre ellos, estos se pueden combinar en un signo de suma. La respuesta seguirá siendo la misma, porque restar un valor negativo es lo mismo que sumar un valor positivo:

![](https://inventwithpython.com/invent4thed/images/00017.jpeg)

### Truco 3: Dos número negativos sumados se pueden intercambiar de posición

Usted siempre puede intercambiar los números en la suma. Esta es la *propiedad conmutativa de la suma*. Eso significa que hacer un intercambio como 6 + 4 por 4 + 6 no cambiará la respuesta, como puede ver cuando usted cuenta las cajas en la Figura 12-9.

![](https://inventwithpython.com/invent4thed/images/00027.jpeg)

*Figura 12-9: La propiedad conmutativa de la suma le permite intercambiar números.*

Digamos que usted está sumando un número negativo y un número positivo, como -6 + 8. Debido a que está sumando números, usted puede intercambiar el orden de los números sin cambiar la respuesta. Esto significa que -6 + 8 es lo mismo que 8 + -6. Luego usted mira el 8 + -6, usted observa que el signo de resta se puede comer el signo de suma a su izquierda, y el problema se convierte en 8 -6 = 2, como usted puede ver acá:

![](https://inventwithpython.com/es/12_files/image012.png)

Usted ha reorganizado el problema para que ahora sea más sencillo de resolver sin utilizar una calculadora o computadora.

## Valores absolutos y la función `abs()`

El *valor absoluto* de un número es el número sin el signo de menos enfrente. Por lo tanto, los números positivos no cambian, pero los números negativos se convierten en positivos. Por ejemplo, el valor absoluto de -4 es 4. El valor absoluto de -7 es 7. El valor absoluto de 5 (el cual ya es positivo) es justo 5.

Usted puede hallar la distancia entre dos objetos restándole sus posiciones y tomando el valor absoluto de la diferencia. Imagine que el caballo blanco está en la posición 4 y el caballo negro en la posición -2. La distancia sería 6, como 4 - -2 es 6, y el valor absoluto de 6 es 6.

Eso funciona sin importar que cuál es el orden los números. Por ejemplo -2 -4 (eso es, dos negativo menos cuatro) es -6, y el valor absoluto de -6 es también 6. 

La función de Python `abs()` retorna el valor absoluto de un entero. Ingrese lo siguiente en la «shell» interactiva:

~~~Python
>>> abs(-5)
5
>>> abs(42)
42
>>> abs(-10.5)
10.5
~~~

El valor absoluto de -5 es 5. El valor absoluto de un número positivo es justo el número, así el valor absoluto de 42 es 42. Inclusive números con decimales tienen un valor absoluto, así que el valor absoluto de -10.5 es 10.5.

## Resumen

La mayoría de la programación no requiere comprender mucha matemática. Hasta este capítulo, hemos estado haciéndolo  con simples sumas y multiplicaciones. 

Los sistemas de coordenadas cartesianas se necesitan para describir dónde está localizado una cierta posición en un área bidimensional. Las coordenadas tienen dos números: la coordenada X y la coordenada Y.  El eje X va de izquierda a derecha, el eje Y va de arriba a abajo. En la pantalla de una computadora, el origen está en la esquina superior izquierda y las coordenadas incrementan yendo de derecha y hacía abajo. 

Los tres trucos matemáticos que aprendió en este capítulo hacen sencillo sumar enteros negativos y positivos. El primer truco es que el signo de menos se comerá el signo de suma a su izquierda. El segundo truco es que dos signos de resta contiguos se combinarán en un signo de suma. El tercer truco es que usted puede intercambiar la posición de los números que está sumando. 

El resto de los juegos de este libro usan estos conceptos porque tienen áreas bidimensionales en ellos. Todos los juegos gráficos requieren comprender cómo trabajan las coordenadas Cartesianas. 

[Previo: Capítulo 11: Panecillos](capitulo11.md) | [Siguiente: Capítulo 13: Búsqueda del tesoro con sonar ](capitulo13.md)

