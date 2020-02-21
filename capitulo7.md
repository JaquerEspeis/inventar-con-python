# 7 Diseñando el juego ahorcado con diagramas de flujo

![Imagen de ciencia](https://inventwithpython.com/invent4thed/images/00016.jpeg)

En este capítulo usted va a diseñar el juego ahorcado.
Este juego es más complicado que los juegos anteriores, pero también es más divertido.
Como este juego es avanzado, primero vamos a planearlo creando un diagrama de flujo en este capítulo.
En el capítulo 8, nosotras escribiremos el código para el juego Ahorcado.

***
Temas cubiertos en este capítulo:
* Arte ASCII
* Diseñando programas con diagramas de flujo
***

## Cómo jugar Ahorcado

Ahorcado es un juego para dos personas en el que una jugadora piensa en una palabra y después dibuja en una página una línea por cada letra de la palabra.
La otra jugadora debe intentar adivinar las letras que pueden estar en la palabra.

Si la segunda jugadora adivina la letra de forma correcta, la primera jugadora escribe la letra en el espacio en blanco apropiado.
Pero si la segunda jugadora se equivoca en la letra, entonces la primera jugadora dibuja una parte del cuerpo de una persona ahorcada.
Para ganar el juego, la segunda jugadora tiene que adivinar todas las letras de la palabra antes de que la persona ahorcada sea dibujada completamente.

## Ejecución de ejemplo de Ahorcado

Aquí hay un ejemplo de lo que la jugadora podría ver cuando ella ejecuta el programa de Ahorcado, programa que vamos a escribir en el capítulo 8.
El texto que la jugadora ingresa está en negrita.

***

A H O R C A D 0
<pre>
   +---+
     |
     |
     |
    ===


Letras falladas:
_ _ _
Adivine la letra.
**a**
  +---+
      |
      |
      |
     ===
Letras falladas:
_ a _
Adivine la letra.
**o**
  +---+
  O   |
      |
      |
     ===
Letras falladas: o
_ a _
Adivine la letra.
**r**
  +---+
  O   |
  |   |
      |
     ===
Letras falladas: or
_ a _
Adivine la letra.
**t**
  +---+
  O   |
  |   |
      |
     ===
Letras falladas: or
_ a t
Adivine la letra.
**a**
Usted ya intentó con esa letra. Intente nuevamente.
Adivine la letra.
**c**
¡Sí! ¡La palabra secreta es «cat» (gato)! ¡Usted ha ganado!
¿Le gustaría jugar nuevamente (sí o no)?
**no**
</pre>
***

## Arte ASCII

Los gráficos para Ahorcado son caracteres del teclado impresas en la pantalla.
Este tipo de gráficos son llamados Arte ASCII (pronunciado áski), el cual es un tipo de precursor del emoji.
Acá está un gato dibujado en arte ASCII:

![Imagen de un gato dibujado en ASCII](https://inventwithpython.com/invent4thed/images/00080.jpeg)

Los dibujos para el juego de Ahorcado se verán así en arte ASCII:

***
<pre>
 +---+    +---+    +---+    +---+    +---+    +---+    +---+

      |    O   |    O   |    O   |    O   |    O   |    O   |
      |        |    |   |   /|   |   /|\  |   /|\  |   /|\  |
      |        |        |        |        |   /    |   / \  |
     ===      ===      ===      ===      ===      ===      ===
</pre>
***

## Diseñando un programa con un diagrama de flujo

Este juego es un poco más complicado que los otros que hemos visto hasta el momento.
Tomemos un momento para pensar cómo poner todo junto.
Primero usted va a crear un diagrama de flujo (como el que está en la Figura 5-1 en la página 47 para el juego del Dragón) para ayudar a visualizar que hará este programa.

Como discutimos en el Capítulo 5, un diagrama de flujo es un diagrama que muestra una serie de pasos como cajas conectadas con flechas.
Cada caja representa un paso, y cada flecha muestra los posibles pasos.
Ponga su dedo en la caja de Inicio («Start») del diagrama de flujo y siga el flujo del programa siguiendo las flechas de las las caja hasta que llegue a la caja de Final («End»).
Usted solo puede moverse de una caja a la otra siguiendo la dirección de la fecha. Usted nunca puede ir hacia atrás, a menos que haya una flecha en dirección hacia atrás, como en la caja del «Player already guessed this letter».

Figura 7-1 es un diagrama de flujo completo para Ahorcado

![Imagen del diagrama de flujo](https://inventwithpython.com/invent4thed/images/00081.jpeg)

Claro, usted no tiene que hacer un diagrama de flujo; usted podría solo empezar a escribir código.
Pero, muy a menudo una vez que inicie a programar, usted pensará en las cosas que deben ser agregadas o cambiadas.
Usted podría terminar eliminando un montón de su código, lo cual podría ser una pérdida completa de esfuerzo.
Para evitar esto, es mejor planear cómo el programa va a funcionar antes de empezar escribirlo.

## Creando un Diagrama de flujo

Su diagrama de flujo no necesita verse como el que está en la figura 7-1. Siempre y cuando usted entienda el diagrama de flujo, será muy útil cuando empiece a escribir código.
Usted puede empezar creando un diagrama de flujo solamente con una caja de INICIO y una caja de FINAL, como es mostrado en la figura 7-2.

Ahora piense en qué pasará cuando usted juegue Ahorcado.
Primero, la computadora piensa en una palabra secreta.
Después el jugador adivina las letras.
Agregue las cajas para estos eventos, como está mostrado en la figura 7-3.
Las nuevas cajas en cada diagrama de flujo tienen una línea intermitente.

![Imagen de Inicio y Final en el diagrama de flujo](https://inventwithpython.com/invent4thed/images/00083.jpeg)

Figura 7-2: Empiece su diagrama de flujo con una caja de INICIO y una caja de FINAL.

![Imagen del diagrama de flujo](https://inventwithpython.com/invent4thed/images/00084.jpeg)

Figura 7-3: Dibuje los dos primeros pasos de Ahorcado como cajas con descripciones.

Pero el juego no termina luego de que la jugadora adivina la letra.
El programa necesita revisar si la letra está en la palabra secreta.

## Ramificando desde una Caja del diagrama de flujo

Hay dos posibilidades: La letra está en la palabra o no.
 Usted va a añadir dos cajas nuevas en el diagrama de flujo, una por cada caso.
Esto crea una rama en el diagrama de flujo, como está mostrado en la figura 7-4.
![Imagen del diagrama de flujo](https://inventwithpython.com/invent4thed/images/00087.jpeg)

Figura 7-4: La rama tiene dos flechas que van hacia cajas separadas.

Si la letra no está en la palabra secreta, revise si la jugadora ha adivinado todas las letras y ha ganado el juego.
Si la letra no está en la palabra secreta, revise si el ahorcado está completo y la jugadora ha perdido.
Agregue cajas para esos casos también.

El diagrama de flujo ahora se ve como en la figura 7-5.

![Imagen del diagrama de flujo](https://inventwithpython.com/invent4thed/images/00089.jpeg)

Figura 7-5 : Después de la rama, los pasos continúan en caminos separados.

No se necesita una flecha desde la caja «Letter is in secret word» hacia la caja «Player ran out of guesses and loses», porque es imposible para la jugadora perder si acaba de adivinar de forma correcta.
También es imposible para la jugadora ganar si acaban de adivinar de forma incorrecta, entonces no es necesario dibujar una flecha en esa tampoco.

## Terminando o reiniciando el juego

Una vez que la jugadora ha ganado o perdido, pregúnteles si desean jugar de nuevo con una nueva palabra secreta. Si la jugadora no quiere jugar de nuevo, el programa termina; de otra forma, el programa continua y piensa en una palabra secreta nueva.
Esto se muestra en la figura 7-6.
![Imagen del diagrama de flujo](https://inventwithpython.com/invent4thed/images/00091.jpeg)

Figura 7-6: La rama del diagrama de flujo después de preguntarle a la jugadora si quiere jugar nuevamente.

## Adivinando de nuevo

El diagrama de flujo se ve casi completo, pero aún nos faltan una cuantas cosas.
Por ejemplo, la jugadora no adivina una letra solo una vez; ellas constantemente adivinan letras hasta que ganen o pierdan.
Dibuje dos nuevas flechas como se muestra en el figura 7-7.

¿Qué pasa si la jugadora adivina la misma letra otra vez?
En lugar de contar esta letra de nuevo, permítales adivinar una letra diferente.
Esta nueva caja se muestra en la Figura 7-8.

![Imagen del diagrama de flujo](https://inventwithpython.com/invent4thed/images/00092.jpeg)

Figura 7-7: Las flechas intermitentes muestran que la jugadora puede volver a adivinar.

![Imagen del diagrama de flujo](https://inventwithpython.com/invent4thed/images/00094.jpeg)

Figura 7-8: Agregue un nuevo paso en caso de que la jugadora adivine una letra que ya haya adivinado.

Si la jugadora adivina la misma letra dos veces, el diagrama de flujo conduce de nuevo a la caja de «Pregunte a la jugadora por una letra».

## Ofreciendo retroalimentación a la jugadora

La jugadora necesita saber cómo le está yendo en el juego.
El programa deber mostrarle el dibujo de la persona Ahorcada y la palabra secreta (con los espacios en blanco de las letras que aún no ha adivinado).
Estas pistas visuales les permiten a ellas ver de cerca si están ganando o perdiendo el juego.

Esta información es actualizada cada vez que la jugadora adivina una letra.
Agregue una caja de «Mostrar el dibujo y el espacio en blanco al jugadora» en el diagrama de flujo entre la caja de «Imagine una palabra secreta» y la caja de «Pregúntele a la jugadora una letra», como se muestra en la Figura 7-9.

![Imagen del diagrama de flujo](https://inventwithpython.com/invent4thed/images/00095.jpeg)

Figura 7-9: Agregue una caja de «Muestre el dibujo y los espacios en blanco a la jugadora» para darle retroalimentación.

¡Eso se ve bien! El diagrama de flujo mapea completamente el orden de todo lo que puede pasar en el juego de Ahorcado.
Cuando usted diseña sus propios juegos, un diagrama de flujo puede ayudarle a recordar todo el código que necesita escribir.

## Resumen

Podría verse  que es un montón de trabajo bosquejar el diagrama de flujo sobre el primer programa.
Después de todo, las personas quieren jugar juegos, ¡no ver diagramas de flujo!
Pero es mucho más fácil hacer cambios e identificar problemas pensando cómo el programa va a funcionar antes de empezar a escribirlo.

Si usted salta a escribir el código primero, puede descubrir problemas que requieran que cambie código que ya ha sido escrito, perdiendo tiempo y esfuerzo.
Además, cada vez que cambie su código, usted corre el riesgo de crear nuevos errores al cambiar muy poquito o mucho.
Es mucho más eficiente conocer qué es lo que quiere construir antes de construirlo.
Ahora que tenemos un diagrama de flujo, ¡vamos a crear el programa Ahorcado en el capítulo 8!

[Previo: Capítulo 6: Usando el depurador](capitulo6.md) | [Siguiente: Capítulo 8: Escribiendo el código del ahorcado](capitulo8.md)
