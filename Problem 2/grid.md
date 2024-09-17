Introduccion

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
del milenio que lo volviera millonario. Pero, ¿sería usted capaz de resolverlo  
también?

Definicion del Problema

Dada una matriz de ceros y unos, de tamanho $n \times n$, a la cual podemos realizar la siguiente operacion: Seleccionar una submatriz de $h \times w$ y convertir todos sus elementos a 0 con un costo del minimo entre $h$ y $w$. Encontrar el menor costo necesario para convertir la matriz a todo 0.

Para reducir a esta definicion tuvimos en cuenta que al no haber restricciones sobre los valores que pueden tomar las tuplas de las secciones a pintar de negro, algunas de tales secciones perfectamente pudieran corresponder a un solo cuadrado de la cuadricula, de manera que no podemos extraer ninguna propiedad especial acerca de la forma en que quedara pintada la cuadricula por el metodo para pintarla. Luego, el problema solo podemos comenzar a abordarlo una vez pintada la cuadricula.

Redefiniendo las operaciones para el problema

Aprovechando que el costo de las operaciones esta definido solo por la menor de las dimensiones del cuadrante sobre el cual se realiza, todas las operaciones que realizaremos tendran por dimension mayor n, nos costaran lo mismo, pero alcanzaran el mayor espacio posible para ese costo.

El costo de realizar una operacion en una seccion de dimension (c, n) es equivalente a realizar c operaciones en las secciones de (1, n) definidas por las filas componentes de la seccion original.
Como ademas, la cantidad de operaciones es irrelevante, solo importando el costo, las operaciones que realizaremos tendran por menor dimensdion 1 y por mayor dimension a n; o sea, realizaremos operaciones exclusivamente sobre cuadrantes constituidos por una sola fila o columna, sin afectar el costo.

Luego podemos redefinir el problema

Redefinicion del problema

Dada una matriz de ceros y unos de tamanho $n \times n$, debemos seleccionar el menor numero de columnas o filas, tales que todos los unos de la matriz se encuentren en alguna de las filas o columnas seleccionadas.

Primer enfoque
Un primer enfoque seria partiendo del conjunto C de filas y columnas de la matriz que contienen al menos un valor 1, recorrer todos sus subconjuntos, del de menor al de mayor tamanho, comprobando si cumplen que contienen a todos los unos de la matriz y quedarnos con el primero que lo cumpla. Esta solucion de fuerza bruta tiene en el peor de los casos, cuando cada uno se encuentra en columnas y filas diferentes de la matriz de los demas unos complejidad O(2^k\*k), puesto que el conjunto C tendria k elementos y por tanto 2^k subconjuntos, y para cada uno de ellos habria que comprobar si contiene a cada uno de los k unos en la matriz.

Exploremos otras formas de representacion del problema
Creemos un grafo con los nodos f1, f2, ..., fn, c1, c2, ..., cn; cada uno de los cuales se refieren a una fila o columna de la matriz. Colocaremos una arista entre dos nodos fi y ci si el elemento en la interseccion de la fila fi y la columna ci es un uno. Con esta representacion el problema de encontrar el menor numero de filas o columnas tales que para todo uno de la matriz este se encuentra en una fila o columna del conjunto, se reduce al problema de encontrar el minimum vertex cover del grafo anteriormente mencionado; puesto que los nodos son filas y el problema del minimum vertex cover consiste en encontrar el conjunto mas pequenho de nodos tales que todas las aristas (en nuestro caso los unos de la matriz), tienen al menos uno de sus extremos dentro de este conjunto.

Luego, hemos redefinido el problema a encontrar la longitud del minimum vertex cover del grafo definido. El problema del minimum vertex cover es NP completo. Sin embargo, por el teorema de Konig, en grafos bipartitos el tamanho del minimum vertex cover es igual al tamanho del maximum matching. Por tal razon, para el caso particular de los grafos bipartitos el problema del minimum vertex cover puede resolverse de manera polinomica, al igual que el problema del maximum matching.

Luego hemos reducido el problema a encontrar la longitud del maximum matching del grafo definido previamente.
Para encontrar el maximum matching de un grafo bipartito podemos usar el algoritmo de Hopcroft-Karp.
