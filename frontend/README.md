# Respuestas del cuestionario

## Vue no detecta cambios dentro de objetos reactivos de la forma que esperarías. ¿Cómo podrías observar un cambio en una propiedad anidada?

En caso de no detectar cambios en propiedades anidades de manera automática utilizaría "watch()"" especificando la ruta completa a la propiedad dentro de una función ya que "watch()" permite escuchar cambios en propiedades específicas dentro de "reactive()".

## watch() permite escuchar cambios en propiedades específicas dentro de reactive(), explica cómo funciona.

La función "watch()" en Vue 3 se usa para observar cambios en valores reactivos y ejecutar una función cuando ocurren. Se pueden observar valores primitivos, propiedades específicas de un objeto reactivo o incluso realizar una reacción cuando cambia cualquier valor dentro de un objeto.

## ¿Cómo harías que un watch() detecte cambios en stock dentro de un array de productos?

Para observar cambios en stock dentro de un array de productos reactivo, se debe utilizar "watch()" con una función que recorra el array y observe la propiedad de stock.

