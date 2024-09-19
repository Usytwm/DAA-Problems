# El secreto de la Isla

En el corazón del vasto océano azul, existe una isla tropical conocida como La Isla de Coba, un lugar de exuberante vegetación y antigua sabiduría. La tribu que habita en esta isla ha vivido en armonía con la naturaleza durante siglos, guiados por un consejo de ancianos que custodian el equilibrio entre los habitantes de la isla y sus recursos.

Sin embargo, una nueva generación de líderes debe ser elegida, y para ello, los ancianos han planteado un desafío ancestral. Los aspirantes al consejo deben descubrir un grupo selecto de **guardianes**, quienes, colocados en puntos estratégicos de la isla, podrían vigilar a todos los aldeanos sin dejar a ninguno sin supervisión directa o indirecta.

La isla tiene una serie de aldeas unidas entre ellas por caminos. El reto es encontrar un grupo de guardianes tan pequeño como sea posible, de modo que cada aldea esté bajo la protección directa de un guardián, o al menos, esté conectada a una aldea donde se haya asignado un guardián.

Los jóvenes líderes deben resolver este desafío para mostrar su valía. Con cada nueva selección de guardianes, la estabilidad de la isla se estremece. El futuro de La Isla de Coba depende de que uno de los jóvenes (como tú) encuentre esta distribución óptima de guardianes y se convierta en el próximo jefe absoluto.


# Solución del Problema
## Definición del problema
El problema se representa mediante un grafo $G = (V,E)$ donde:
- V = {conjunto de aldeas}.
- E = {conexiones entre las aldeas}.

Cada vértice $u ∈ V$ se puede clasificar en función de si está siendo vigilado o no por un guardián.
Si cada vértice se encuentra inicialmente en estado no vigilado, se desea encontrar un subconjunto $D ⊆ V$ de k vértices tal que:
- Cada vértice del subconjunto pasa a estado vigilado.
- Cada vértice adyacente a un vértice del subconjunto - pasa a estado vigilado.
- Tras los pasos 1 y 2, no quedan vértices no vigilados en el grafo.
- k sea mínimo 

## Generalización del problema
Eliminando las particularidades del problema(aldeas, guardianes, etc.) tenemos que:
Dado un grafo G = (V,E), debemos encontrar el subconjunto de vértices D con la menor cantidad de vértices posible, tal que cada vértice de V pertenece a D o es adyacente a al menos un vértice de D.

Al problema anterior se le denomina problema del conjunto dominante(dominating set problem), un problema NP-completo.

## Dominating Set Problem
Formalmente, el conjunto dominante se define como:
Dado un grafo no dirigido $G = (V,E)$, un subconjunto de vértices $D ⊆ V$ se llama conjunto dominante si para cada vértice $u ∈ V \ D$ hay un vértice $v ∈ D$ tal que $(u,v) ∈ E$.
El numero de dominancia de G se define como $Y(G) :=$ min{|S| : S es un conjunto dominante de G}

Probar si $Y(G) <= k$ para un grafo dado y una entrada k es un problema de decisión NP-Completo.


## Demostrando que es NP-Completo
### Definición
Un problema de decisión es NP-Completo si:

1) Está en NP.
2) Todo problema de NP es reductible al problema dado en un tiempo polinómico.

### Procedimiento
La condición uno se prueba demostrando que una condición candidata para el problema se puede verificar en tiempo polinómico.

La condición dos se puede probar reduciendo al problema dado algún problema NP-Completo conocido, la reducción debe ser en tiempo polinómico.

### Idea general de la demostración
1) Demostramos que una solución candidata del problema puede verificarse en tiempo polinómico.
2) Luego el problema está en NP y se cumple la condición uno.
3) Presentamos el problema de cobertura de vértices(Vertex Cover Problem), uno de los 21 problemas NP-completos de Karp.
4) Demostramos que existe una reducción en tiempo polinómico del problema del mínimo conjunto dominante al problema de cobertura de conjuntos.
5) Por tanto se cumple la condición dos.

Luego el problema es NP-Completo

### Pasos 1 y 2

Sea el problema de si un grafo G = (V,E) tiene un conjunto dominante S, |S| = k. Podemos verificar una solución potencial en tiempo polinómico.

Verificar si el conjunto de vértices S forma un conjunto dominante:
Para cada vértice $v ∈ V \ S$: 
- Verificar si v esta conectado a algún vértice en S
- Si se encuentra alguna conexión faltante, la solución es incorrecta

Esta verificación puede realizarse en tiempo O(V+E) por lo que el problema esta en NP.

### Paso 3
Una cobertura de vértices V’ de un grafo G = (V,E) es un subconjunto de V tal que (u,v) pertenece E => u pertenece V’ V v pertenece V’, es decir, es un subconjunto de vértices V’ donde cada arista de E tiene al menos uno de sus extremos en el.

### Pasos 4 y 5
Dada una instancia del problema de Vertex Cover:
- Teniendo un grafo $G = (V, E)$ y un número entero k, buscar si hay un conjunto de vértices $V_c$ de tamaño k que cubra todas las aristas.

Se construye una nueva instancia del problema de conjunto dominante:
- Sea G’ subgrafo de G tal que para cada arista (u,v) en E, se agrega un nuevo vértice $w_{uv}$ a V’ conectado a ambos vértices u y v.

Luego se tiene que si G tiene una cobertura de vértices $V_c$ de tamaño k:
El conjunto $V_c$ forma un conjunto dominante en G’
Cada vértice $w_{uv}$ es dominado por al menos uno de sus dos vértices incidentes en Vc
Por lo tanto, G’ tiene un conjunto dominante de tamaño k.

Si G’ tiene un conjunto dominante D de tamaño k:
Los vértices originales de G forman una cobertura de vértices en G.
Cada arista (u,v) debe tener al menos un vértice D conectado a u o v
Por lo tanto, D forma una cobertura de vértices en G de tamaño máximo k

Por tanto, podemos reducir un problema de cobertura de vértices a uno de conjunto dominante.

Como Vertex Cover es un problema NP-Completo, todo problema NP se puede reducir a un problema Vertex Cover, luego todo problema NP se puede reducir a un problema Dominating Set.  
