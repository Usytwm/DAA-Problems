# Diseño y Análisis de Algoritmos

| Nombre                     | Grupo | Github                                       |
| -------------------------- | ----- | -------------------------------------------- |
| Brián Ameht Inclán Quesada | C411  | [@Usytwm](https://github.com/Usytwm)         |
| Davier Sanchez Bello       | C412  | [@DavierSB](https://github.com/DavierSB)     |
| Maykol Luis Martínez Rodríguez | C412 | [@MaykolLuisMa](https://github.com/MaykolLuisMa) |


Este repositorio contiene una colección de problemas y sus soluciones para la asignatura de **Diseño y Análisis de Algoritmos** de la carrera Ciencias de la Computacion. Cada problema incluye una descripción detallada, una demostración de la solución en formato PDF y el código fuente correspondiente.

## Estructura del Repositorio

- **Problema 1 (Videojuego)/**

  - [Instrucciones y Descripción del Problema](./Problem%201/README.md)
  - [Informe de la Solución (PDF)](./Problem%201/Videojuego.pdf)
  - [Solución](./Problem%201/code/solution.py) $O(n^2)$
  - [Solución Optimizada](./Problem%201/code/optimized_solution.py) $O(n \log n)$

- **Problema 2 (Grid)/**

  - [Instrucciones y Descripción del Problema](./Problem%202/README.md)
  - [Informe de la Solución (PDF)](./Problem%202/Grid.pdf)
  - [Solución por Fuerza Bruta](./Problem%202/code/brute_force.py) $O(2^{2n} \cdot n)$
  - [Solución Optimizada sin Comprimir](./Problem%202/code/uncompressed_solution.py) $O(n^5)$
  - [Solución Optimizada Comprimida](./Problem%202/code/final_solution.py) $O(m^5)$

- **Problema 3 (El secreto de la Isla)/**
  - [Instrucciones y Descripción del Problema](./Problem%203/README.md)
  - [Informe de la Solución (PDF)](./Problem%203/El%20secreto%20de%20la%20Isla.pdf)
  - [Solución](./Problem%203/code/exact_solution.py) $O(2^{n} \cdot n^2)$
  - [Solución Aproximada](./Problem%203/code/approximate_solution.py) $O(n^2)$ $ \ln(\Delta) -aproximación$
  <!-- - [Solución Optimizada](./Problem%203/code/optimized_exact_solution.py) -->

- **[Informe](Informe.pdf)**

## Descripción de los Problemas

1. ## Videojuego:

   Estás creando un nivel para un videojuego. El nivel consiste en $n$ habitaciones dispuestas en un círculo. Las habitaciones están numeradas del $1$ al $n$. Cada habitación contiene exactamente una salida: completar la $j$-ésima habitación te permite pasar a la $(j+1)$-ésima habitación (y completar la $n$-ésima habitación te permite pasar a la $1$-era habitación).

   Se te da la descripción del multiconjunto de $n$ cofres: el $i$-ésimo cofre tiene un valor de tesoro $c_i$.

   Cada cofre puede ser de uno de dos tipos:

   - cofre normal — cuando un jugador entra en una habitación con este cofre, recoge el tesoro y procede a la siguiente habitación;
   - cofre trampa — cuando un jugador entra en una habitación con este cofre, el cofre se lo come vivo, y él pierde.

   El jugador comienza en una habitación aleatoria, con cada habitación teniendo la misma probabilidad de ser elegida. Las ganancias del jugador son iguales al valor total de los tesoros que haya recogido antes de perder.

   Se te permite elegir el orden en que los cofres se colocan en las habitaciones. Para cada $k$ de $1$ a $n$, coloca los cofres en las habitaciones de tal manera que:

   - cada habitación contenga exactamente un cofre;
   - exactamente $k$ cofres sean trampas;
   - el valor esperado de las ganancias del jugador sea el mínimo posible.

   Ten en cuenta que para cada $k$ la colocación se elige de manera independiente.

   Se puede ver que está en la forma de $\frac{P}{Q}$ donde $P$ y $Q$ son enteros no negativos y $Q≠0$.

2. ## Grid:

   Un día iba Maykol por su facultad cuando ve un cuadrado formado por $n \times n$  
   cuadraditos de color blanco. A su lado, un mensaje ponía lo siguiente: "Las  
   siguientes tuplas de la forma $(x_1, y_1, x_2, y_2)$ son coordenadas para pintar de  
   negro algunos rectángulos. (coordenadas de la esquina inferior derecha y superior  
   izquierda)" Luego se veían $k$ tuplas de cuatro enteros. Finalmente decía:  
   "Luego de tener el cuadrado coloreado de negro en las secciones pertinentes, su  
   tarea es invertir el cuadrado a su estado original. En una operación puede seleccionar  
   un rectángulo y pintar todas sus casillas de blanco. El costo de pintar  
   de blanco un rectángulo de $h \times w$ es el mínimo entre $h$ y $w$. Encuentre el costo  
   mínimo para pintar de blanco todo el cuadrado."

   En unos 10 minutos Maykol fue capaz de resolver el problema. Desgraciadamente  
   esto no es una película y el problema de Maykol no era un problema  
   del milenio que lo volviera millonario. Pero, ¿sería usted capaz de resolverlo también?

3. ## El secreto de la Isla:

   En el corazón del vasto océano azul, existe una isla tropical conocida como La Isla de Coba, un lugar de exuberante vegetación y antigua sabiduría. La tribu que habita en esta isla ha vivido en armonía con la naturaleza durante siglos, guiados por un consejo de ancianos que custodian el equilibrio entre los habitantes de la isla y sus recursos.

   Sin embargo, una nueva generación de líderes debe ser elegida, y para ello, los ancianos han planteado un desafío ancestral. Los aspirantes al consejo deben descubrir un grupo selecto de **guardianes**, quienes, colocados en puntos estratégicos de la isla, podrían vigilar a todos los aldeanos sin dejar a ninguno sin supervisión directa o indirecta.

   La isla tiene una serie de aldeas unidas entre ellas por caminos. El reto es encontrar un grupo de guardianes tan pequeño como sea posible, de modo que cada aldea esté bajo la protección directa de un guardián, o al menos, esté conectada a una aldea donde se haya asignado un guardián.

   Los jóvenes líderes deben resolver este desafío para mostrar su valía. Con cada nueva selección de guardianes, la estabilidad de la isla se estremece. El futuro de La Isla de Coba depende de que uno de los jóvenes (como tú) encuentre esta distribución óptima de guardianes y se convierta en el próximo jefe absoluto.

   Cada problema está documentado en su propio directorio, con un archivo README que proporciona una descripción detallada del problema y la solución. Además, se incluye un archivo PDF con la demostración de la solución y el código fuente correspondiente.
