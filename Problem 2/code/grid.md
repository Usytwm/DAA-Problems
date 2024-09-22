## Grid

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
Dada una matriz de nxn con k secciones rectangulares pintadas de negro y la posibilidad de pintar de blanco secciones rectangulares de cualquier dimension (hxw) con un costo min(h, w), cual es el menor costo necesario para que todas las celdas queden pintadas de blanco de nuevo.

Primero resolvamos una instancia mas sencilla del problema, donde inicialmente no hay k secciones enteras pintadas de negro, sino t celdas individuales pintadas de negro.

El costo de las operaciones tal y como fue definido cumple las siguientes propiedades:
1- Es optimo en cuanto a costo pintar secciones de tamanho (h, w) con max(h, w) = n. Esto se debe a que si max(h, w) < n, el costo seria el mismo que de haber tomado max(h, w) = n, pero nunca estariamos accediendo a mas celdas negras.
2- Sea S una seccion, y sean S1, S2, ..., Si subsecciones contiguas de S, obtenidas de dividir a S a lo largo de su dimension mas pequenha. Entonces el costo de pintar de blanco por separado a cada una de las subsecciones es el mismo de pintar S en una sola operacion.
Particularmente, dividir una seccion a lo largo de la menor de sus dimensiones en subsecciones cuya menor dimension tiene longitud 1, y luego pintar cada una de estas subsecciones por separado tiene el mismo costo que haber pintado toda la seccion en una sola operacion y alcanza el mismo numero de casillas negras.
Uniendo ambas propiedades llegamos a que es optimo solo pintar secciones de tamanho (1, n) o (n, 1); o sea, solo pintar filas o columnas. Luego, podemos redefinir el problema como:
Dada una matriz de nxn con k celdas pintadas de negro, cual es el minimo numero de filas o columnas que debemos pintar de blanco para que toda la matriz quede de color blanco.

Solo nos interesara considerar pintar de blanco las filas o columnas que contienen al menos una celda negra. Sea C el conjunto de tales filas o columnas. Nos interesa encontrar el menor subconjunto de C tal que incluya todas las celdas negras.
Ademas no nos interesa el dato de las dimensiones de la matriz ya que como sea siempre operamos sobre filas o columnas enteras, ni nos interesan las celdas blancas puesto que a la vez que una celda es convertida en blanco no es posible modificar su estado mediante ninguna operacion.
Entonces podemos redefinir el problema de una manera mas comoda como:

Dados t puntos en una grilla y el conjunto C de filas y columnas que contienen al menos un punto, cual es el subconjunto de C de menor tamanho que aun contiene a todos los t puntos dentro de si?

Llamemos subconjunto bueno de C a aquellos subconjuntos tales que para todo punto de la grilla, en C existe al menos una fila o columna que lo contiene. Verificar si un subconjunto es bueno tiene complejidad O(t), pues implica comprobar punto a punto.

Una primera solucion de fuerza bruta seria tomar como espacio de busqueda el espacio de los subconjuntos de C, y recorrerlo en orden creciente de tamanho de los subconjuntos, hasta encontrar un subconjunto bueno.

El conjunto C tiene a lo mas 2t elementos, ya que a lo mas t filas diferentes y t columnas diferentes pueden contener puntos.

Luego la complejidad de esta primera solucion, es O(2^(2t)\*t), ya que existen 2^(2t) subconjuntos de C y probar cada uno es O(t)

Sea S un subconjunto bueno, notemos que anhadir filas y columnas a S no hace que deje de ser bueno, por tal motivo es posible anhadir filas y columnas a S hasta llegar a C, sin pasar en ningun momento por un subconjunto que no sea bueno. Analogamente, para todo subconjunto bueno S, es posible alcanzarlo partiendo de C y realizando una secuencia de eliminaciones de elementos de C sin que ninguno de los subconjuntos intermedios por los que transitemos deje de ser bueno. Por tal motivo, podemos presentar esta segunda solucion

Representemos los subconjuntos de C como vertices de un grafo, y establezcamos una arista entre cada par de vertices tales que uno puede ser generado a partir del otro con la eliminacion de solo un elemento. Comenzando en el nodo correspondiente al propio conjunto C, realicemos un DFS, deteniendonos cada vez que el nodo a visitar no sea bueno. Luego el DFS realizara O(numero de subconjuntos buenos) operaciones. Cuantos subconjuntos buenos hay?

Tomemos el caso en que todos los puntos se encuentran ubicados a lo largo de una sola fila. Entonces habra t columnas diferentes. Luego habra 2^t subconjuntos de C que contienen a la fila en cuestion y por tanto son buenos; ademas sera bueno el conjunto que contiene a todas las columas pero no a la fila. Luego en este caso habria 2^t + 1 conjuntos buenos. Como podemos apreciar, esta solucion es tambien exponencial. (Falta probar rigurosamente que es O(2^t\*t))

Cada punto se encuentra solo en una fila y una columna. Cada fila y cada columna tienen en comun a lo mas un punto. O sea, los puntos establecen una relacion entre las filas y las columnas. Formalmente:
Una relacion binaria entre dos conjuntos A y B es un subconjunto de su producto cartesiano. Los puntos son un subconjunto del producto cartesiano entre las filas y las columnas.
Luego, probemos crear un grafo G, donde a cada fila y a cada columna corresponde un vertice, y solo existen aristas ente aquellos nodos representantes de filas y columnas que tienen un punto en su interseccion.
Notemos que con esta representacion nuestro roblema se reduce al minimum vertex cover. El problema del minimum vertex cover se define como dado un grafo, encontrar el menor subconjunto de los vertices (filas o columnas en nuestro problema), necesarios para que todas las aristas del grafo (puntos en nuestro problema), tengan al menos uno de sus dos extremos incluido.
El problema del minimum vertex cover es NP completo; pero en grafos bipartitos tiene una solucion polinomica, derivada del Teorema de Konig que enuncia que en grafos bipartitos el minimum vertex cover tiene el mismo tamanho que el maximum matching.
Luego, hemos reducido el problema a calcular el maximum matching del grafo generado.
El algoritmo de Hopcroft-Karp computa el maximum matching de un grafo bipartito en O(|E|sqrt(|V|)) y el algoritmo de Dinic, del cual Hopcroft-Karp es una particularizacion, lo hace e O(|E||V|). Notemos que para el grafo que hemos creado se cumple que |V| = t y |E| = 2*t, por lo que la complejidad de nuestro algoritmo seria O(t*root(t)) si usamos Hopcroft-Karp y O(t^2) si usamos Dinic. No obstante notemos que a su vez t es O(n^2), puesto que una seccion pintada de negro puede contener hasta n^2 celdas en su interior. Luego, la complejidad de nuestro algoritmo seria O(n^4). Esta complejidad nos permitiria solo trabajar con valores de n hasta un poco mas grandes que 100.

No obstante busquemos aprovechar la forma en que fueron dispuestas en secciones las celdas negras, intentemos realizar una compresion
Si bien las k secciones pueden abarcar n filas, solo existiran 2*k filas frontera (que son la primera o la ultima de una seccion). Luego, podemos agrupar a todas las filas en 2*k rangos. El i-esimo rango abarcara a todas las filas entre la i-esima fila frontera (incluida) y la fila frontera i+1 (excluida).
Podemos realizar la operacion analoga con las columnas.
Dos celdas que compartan rango en cuanto a fila y en cuanto a columna estan pintadas de la misma manera. Esto se debe a que si estan pintadas de color diferente, una de ellas estara dentro de una de las secciones pintadas iniciales, mientras que la otra esta fuera de cualquier seccion pintada. Pero si una esta adentro y la otra afuera entre ellas debe haber una fila frontera, y si hubiera una fila frontera, ya sea horizontal o vertical entre ellas entonces no compartirian el rango de fila o de columna respectivamente.
Sea una seccion compuesta unicamente por celdas que comparten rango de fila y columna. Realizar la operacion de pintar todo un rango de filas o de pintar todo un rango de columnas, nunca provocara que en la seccion aparezcan celdas de colores diferentes (nuevamente porque esto implicaria la presencia de una frontera dentro de la seccion).
Luego cada seccion compuesta por celdas que comparten rango de fila y de columna, es monocromatica respecto a las operacions sobre rangos enteros de filas o de columnas, analogamente a como las celdas individuales son monocromaticas respecto a las operaciones sobre filas o columnas.
Luego, podemos crear a partir del problema original una nueva grilla donde cada fila o columna corresponde a un rango de filas o columnas, y cada celda corresponde a una seccion de celdas del problema original que comparten rango de filas y de columnas. Esta nueva grilla, en lugar de tener dimensiones nxn, tiene dimensiones kxk, con lo cual hemos dejado a la variable n correr libre, sin restricciones.
No obstante aun falta un detalle para poder resolver el problema. En esta nueva grilla el costo de eliminar una fila o una columna es la longitud del rango al que representa. Luego el problema no sera precisamente encontrar el subconjunto de menor tamanho (sino el de menor costo) de las filas y las columnas tales que contengan dentro de si a todas las celdas negras de la grilla.
Si realizamos la misma representacion en forma de grafo, asignandole un vertice a cada fila o columna, y una arista entre cada fila y cada columna; y ademas asignamos a cada vertice un costo, el de eliminar la fila o columna correspondiente; entonces el problema se reduce a encontrar el Minmum Cost Vertex Cover, que no es lo mismo que el Minimum Vertex Cover.
El problema del Minimum Cost Vertex Cover es una generalizacion del problema del Minimum Vertex Cover y al igual que este ultimo, es NP completo, pero existe una solucion en tiempo polinomial para el.
La solucion en tiempo polinomial parte de la generalizacion del teorema de Konig a grafos ponderados, que es el Teorema de Evergenys [insertar referencia].
El Teorema de Evergenys en esencia afirma que el costo del Minimum Cost Vertex Cover es igual al peso Maximum Weigth Matching de un grafo equivalente.
Luego, solo nos queda transformar el grafo que tenemos donde estan ponderados los vertices, en un grafo donde las aristas tengan asignadas una capacidad y sea posible computar el flujo maximo. Para ello sencillamente dividiremos a cada vertice original en dos vertices, y colocaremos una arista entre ellos con capacidad igual al costo del vertice original. Para las demas aristas colocaremos capacidad infinita.
Finalmente podemos calcular el flujo maximo. Para ello podemos escoger entre el algoritmo de Edmons-Karp y el de Dinic. El algoritmo de Edmons-Karp es cuadratico con respecto a la cantidad de aristas mientras que el de Dinic lo es con respecto a la cantidad de vertices. El grafo sobre el cual aplicaremos el flujo maximo tiene en el peor caso 2*2k vertices resultantes de duplicar cada uno de los 2k vertices iniciales, y otros 2 vertices (la fuente y el sumidero). El numero de aristas en ese mismo caso sera de k + 2*k + 2*k (k aristas, una por cada celda negra), 2*k por las aristas internas de cada vertice que en el peor de los casos son 2k vertices y 2\*k por las aristas que llevan de cada vertice ya sea a la fuente o al sumidero del flujo. Luego tendremos 4k + 2 vertices y 5k aristas. Por tanto debe ser mejor el algoritmo de Dinic
En resumen:
1- Comprimimos la grilla original
2- Transformamos en un grafo la nueva grilla
3- Alistamos el grafo para computarlo su maximum flow
4- Usamos el algoritmo de Dinic para obtener la respuestaS
