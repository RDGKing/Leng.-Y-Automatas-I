### Ejercicio 3.1

Construya el diagrama de transición del AFD a partir de la tabla:

| δ     | 0    | 1    |
|-------|------|------|
| →*q0  | q2   | q1   |
| q1    | q1   | q2   |
| q2    | q1   | q3   |
| q3    | q3   | q1   |

<p align="center">
  <img src= photos/image1.png width = 250>
</p>

### Ejercicio 3.2

Para los siguientes ejercicios, construya el diagrama de transición del AFD que acepta a cada uno de los lenguajes sobre el alfabeto Σ = { a, b }:

a) El lenguaje donde toda cadena tiene exactamente dos bs.

<p align="center">
  <img src= photos/image2.png width = 120>
</p>

b) El lenguaje de las cadenas no vacías, donde toda a está entre dos bs.

<p align="center">
  <img src= photos/image3.png width = 300>
</p>

c) El lenguaje donde toda cadena contiene el sufijo aba.
<p align="center">
  <img src= photos/image4.png width = 240>
</p>

d) El lenguaje donde ninguna cadena contiene las 
subcadenas aa ni bb.

<p align="center">
  <img src= photos/image5.png width = 220>
</p>

e) El lenguaje donde toda cadena contiene la subcadena baba.

<p align="center">
  <img src= photos/image6.png width = 270>
</p>

f) El lenguaje donde toda cadena contiene por separado a las cadenas ab y ba.

<p align="center">
  <img src= photos/image7.png width = 240>
</p>

g) Toda cadena es de longitud impar y contiene una cantidad par de as.
<p align="center">
  <img src= photos/image8.png width = 240>
</p>

#### Conclusion
En conclusión, los autómatas finitos deterministas son una herramienta esencial en la teoría de la computación para representar y procesar lenguajes regulares. Los AFN nos permiten hacer representaciones de diversos lenguajes a través de diagramas de transición. Por lo tanto, considero que es muy importante comprenderlos para lograr modelar diferentes estructuras del lenguaje de forma correcta, lo que nos permitirá resolver problemas informáticos.