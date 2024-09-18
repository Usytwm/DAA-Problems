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

Formalizando
Dada una matriz de nxn con k celdas pintadas de negro y la posibilidad de pintar secciones rectangulares de cualquier dimension (hxw) con un costo min(h, w), cual es el menor costo necesaria para que todas las celdas queden pintadas de blanco de nuevo

Notemos que esta formalizacion ignora que las celdas inicialmente en la declaracion del problema eran blancas y que nosotros mismos debemos colorear las negras. Esto no aporta ninguna informacion relevante.

El costo de las operaciones tal y como fue definido cumple las siguientes propiedades:
1- Es optimo en cuanto a costo pintar secciones de tamanho (h, w) con max(h, w) = n. Esto se debe a que si max(h, w) < n, el costo seria el mismo que de haber tomado max(h, w) = n, pero nunca estariamos accediendo a mas celdas negras.
2- Es optimo en cuanto a costo pintar solo secciones de tamanho (h, w) con min(h, w) = 1. Esto se debe a que cualquier seccion de dimensiones (h, w) con min(h, w) = k, puede ser descompuesta en k subsecciones de dimensiones (h', w') con min(h', w') = 1. Pintar cada una de las subsecciones por separado tendria el mismo costo y permitiria acceder a la misma cantidad de celdas que pintar la seccion original de un solo golpe. (Cualquier otra forma de descomponer o pintar la seccion hubiera costado mas).
Uniendo ambas propiedades llegamos a que es optimo solo pintar secciones de tamanho (1, n) o (n, 1); o sea, solo pintar filas o columnas. Luego, podemos redefinir el problema como:

Dada una matriz de nxn con k celdas pintadas de negro, cual es el minimo numero de filas o columnas que debemos pintar de blanco para que toda la matriz quede de color blanco.

Solo nos interesara considerar pintar de blanco las filas o columnas que contienen al menos una celda negra. Sea C el conjunto de tales filas o columnas. Nos interesa encontrar el menor subconjunto de C tal que incluya todas las celdas negras.
Ademas no nos interesa el dato de las dimensiones de la matriz ya que como sea siempre operamos sobre filas o columnas enteras, ni nos interesan las celdas blancas puesto que a la vez que una celda es convertida en blanco no es posible modificar su estado mediante ninguna operacion.
Entonces podemos redefinir el problema de una manera mas comoda como:

Dados k puntos en una grilla y el conjunto C de filas y columnas que contienen al menos un punto, cual es el subconjunto de C de menor tamanho que aun contiene a todos los k puntos dentro de si?

Llamemos subconjunto bueno de C a aquellos subconjuntos tales que para todo punto de la grilla, en C existe al menos una fila o columna que lo contiene. Verificar si un subconjunto es bueno tiene complejidad O(k), pues implica comprobar punto a punto.

Una primera solucion de fuerza bruta seria tomar como espacio de busqueda el espacio de los subconjuntos de C, y recorrerlo en orden creciente de tamanho de los subconjuntos, hasta encontrar un subconjunto bueno.

El conjunto C tiene a lo mas 2k elementos, ya que a lo mas k diferentes y k columnas diferentes pueden contener puntos.

Luego la complejidad de esta primera solucion, es O(2^(2k)\*k), ya que existen 2^(2k) subconjuntos de C y probar cada uno es O(k)

Sea S un subconjunto bueno, notemos que anhadir filas y columnas a S no hace que deje de ser bueno, por tal motivo es posible anhadir filas y columnas a S hasta llegar a C, sin pasar en ningun momento por un subconjunto que no sea bueno. Analogamente, para todo subconjunto bueno S, es posible alcanzarlo partiendo de C y realizando una secuencia de eliminaciones de elementos de C sin que ninguno de los subconjuntos intermedios por los que transitemos deje de ser bueno. Por tal motivo, podemos presentar esta segunda solucion

Representemos los subconjuntos de C como vertices de un grafo, y establezcamos una arista entre cada par de vertices tales que uno puede ser generado a partir del otro con la eliminacion de solo un elemento. Comenzando en el nodo correspondiente al propio cconjunto C, realicemos un DFS, deteniendonos cada vez que el nodo a visitar no sea bueno. Luego el DFS realizara O(numero de subconjuntos buenos) operaciones. Cuantos subconjuntos buenos hay?

Tomemos el caso en que todos los puntos se encuentran ubicados a lo largo de una sola fila. Entonces habra k columnas diferentes. Luego habra 2^k subconjuntos de C que contienen a la fila en cuestion y por tanto son buenos; ademas sera bueno el conjunto que contiene a todas las columas pero no a la fila. Luego en este caso habria 2^k + 1 conjuntos buenos. Como podemos apreciar, esta solucion es tambien exponencial. (Falta probar rigurosamente que es O(2^k\*k))

Cada punto se encuentra solo en una fila y una columna. Cada fila y cada columna tienen en comun a lo mas un punto. O sea, los puntos establecen una relacion entre las filas y las columnas. Formalmente:
Una relacion binaria entre dos conjuntos A y B es un subconjunto de su producto cartesiano. Los puntos son un subconjunto del producto cartesiano entre las filas y las columnas.
Luego, probemos crear un grafo G, donde a cada fila y a cada columna corresponde un vertice, y solo existen aristas ente aquellos nodos representantes de filas y columnas que tienen un punto en su interseccion.
Notemos que con esta representacion nuestro roblema se reduce al minimum vertex cover. El problema del minimum vertex cover se define como dado un grafo, encontrar el menor subconjunto de los vertices (filas o columnas en nuestro problema), necesarios para que todas las aristas del grafo (puntos en nuestro problema), tengan al menos uno de sus dos extremos incluido.
El problema del minimum vertex cover es NP completo; pero en grafos bipartitos tiene una solucion polinomica, derivada del Teorema de Konig que enuncia que en grafos bipartitos el minimum vertex cover tiene el mismo tamanho que el maximum matching.
Luego, hemos reducido el problema a calcular el maximum matching del grafo generado.
Usaremos el algoritmo de Hopcroft-Karp. Este algoritmo es el mas eficiente de los existentes para calcular maximum matching en grafos bipartitos dispersos, como es el caso del grafo G.
