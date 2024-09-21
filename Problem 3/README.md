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

Cada vértice $u \in V$ se puede clasificar en función de si está siendo vigilado o no por un guardián.
Si cada vértice se encuentra inicialmente en estado no vigilado, se desea encontrar un subconjunto $D \subseteq V$ de k vértices tal que:

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
Dado un grafo no dirigido $G = (V,E)$, un subconjunto de vértices $D \subseteq V$ se llama conjunto dominante si para cada vértice $u \in V \setminus D$ hay un vértice $v \in D$ tal que $(u,v) \in E$.

El numero de dominancia de G se define como $Y(G) := \min \{|S| : S \text{ es un conjunto dominante de } G\}$

Probar si $Y(G) \leq k$ para un grafo dado y una entrada $k$ es un problema de decisión NP-Completo.

## Demostrando que es NP-Completo

### Definición

Un problema de decisión es NP-Completo si:

1. Está en NP.
2. Todo problema de NP es reductible al problema dado en un tiempo polinómico.

### Procedimiento

La condición uno se prueba demostrando que una condición candidata para el problema se puede verificar en tiempo polinómico.

La condición dos se puede probar reduciendo al problema dado algún problema NP-Completo conocido, la reducción debe ser en tiempo polinómico.

### Idea general de la demostración

1. Demostramos que una solución candidata del problema puede verificarse en tiempo polinómico.
2. Luego el problema está en NP y se cumple la condición uno.
3. Presentamos el problema de cobertura de vértices(Vertex Cover Problem), uno de los 21 problemas NP-completos de Karp.
4. Demostramos que existe una reducción en tiempo polinómico del problema del mínimo conjunto dominante al problema de cobertura de conjuntos.
5. Por tanto se cumple la condición dos.

Luego el problema es NP-Completo

### Pasos 1 y 2

Sea el problema de si un grafo $G = (V,E)$ tiene un conjunto dominante S, |S| = k. Podemos verificar una solución potencial en tiempo polinómico.

Verificar si el conjunto de vértices $S$ forma un conjunto dominante:
Para cada vértice $v \in V \setminus  S$:

- Verificar si v esta conectado a algún vértice en $S$
- Si se encuentra alguna conexión faltante, la solución es incorrecta

Esta verificación puede realizarse en tiempo $O(V+E)$ por lo que el problema esta en NP.

### Paso 3

Una **cobertura de vértices** $V'$ de un grafo $G = (V, E)$ es un subconjunto de $V$ tal que, si $(u, v) \in E$, entonces $u \in V'$ o $v \in V'$. Es decir, es un subconjunto de vértices $V'$ donde cada arista de $E$ tiene al menos uno de sus extremos en él.

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

# Otra solucion

# Reducción del problema de **Dominating Set** al problema de **Vertex Cover**

**Introducción:**

El objetivo es demostrar una reducción polinomial del problema de _Dominating Set_ al problema de _Vertex Cover_. Esto significa que, dada una instancia de _Dominating Set_, podemos transformarla en una instancia de _Vertex Cover_ de tal manera que la solución al segundo problema nos proporcione una solución al primero.

---

**Definiciones:**

- **Dominating Set (Conjunto Dominante):**
  Dado un grafo no dirigido $G = (V, E)$ y un entero $k$, el problema pregunta si existe un subconjunto $D \subseteq V$ de tamaño a lo sumo $k$ tal que cada vértice $v \in V$ es miembro de $D$ o es adyacente a al menos un vértice en $D$.

- **Vertex Cover (Cobertura de Vértices):**
  Dado un grafo no dirigido $G = (V, E)$ y un entero $k$, el problema pregunta si existe un subconjunto $C \subseteq V$ de tamaño a lo sumo $k$ tal que cada arista $(u, v) \in E$ tiene al menos uno de sus extremos en $C$.

---

**Construcción de la Reducción:**

Dada una instancia del problema de _Dominating Set_, es decir, un grafo $G = (V, E)$ y un entero $k$, construiremos una instancia del problema de _Vertex Cover_, es decir, un grafo $G' = (V', E')$ y un entero $k'$, siguiendo los pasos:

1. **Creación de vértices en $G'$:**

   - Para cada vértice $v \in V$, agregamos dos vértices en $V'$: uno llamado $v$ y otro llamado $v'$.

2. **Creación de aristas en $G'$:**

   - Para cada arista $(u, v) \in E$:
     - Agregamos aristas $(u, v)$ y $(u', v')$ en $E'$.
   - Para cada vértice $v \in V$:
     - Agregamos una arista $(v, v')$ en $E'$.

3. **Definición de $k'$:**
   - Establecemos $k' = k + |V|$.

---

**Ejemplo de Construcción:**

Supongamos un grafo simple $G$ con tres vértices $V = \{a, b, c\}$ y aristas $E = \{(a, b), (b, c)\}$. Construimos $G'$ de la siguiente manera:

- **Vértices de $G'$:** $V' = \{a, b, c, a', b', c'\}$.
- **Aristas de $G'$:**
  - $(a, b), (a', b')$ (de $E$).
  - $(b, c), (b', c')$ (de $E$).
  - $(a, a'), (b, b'), (c, c')$ (conexiones entre cada vértice y su copia).

---

**Demostración de Correctitud:**

**(⇒) Si existe un Conjunto Dominante de tamaño $k$ en $G$, entonces existe una Cobertura de Vértices de tamaño $k'$ en $G'$.**

- Sea $D \subseteq V$ un conjunto dominante en $G$ de tamaño $k$.
- Construimos $C = D \cup \{v' \mid v \in V\}$.
- Entonces, $C \subseteq V'$ y su tamaño es $k' = k + |V|$.
- **Cobertura de aristas:**
  - Las aristas $(v, v')$ están cubiertas porque $v' \in C$.
  - Las aristas originales $(u, v)$ están cubiertas porque al menos uno de $u$ o $v$ está en $D \subseteq C$ (debido a que $D$ es dominante).
  - Las aristas $(u', v')$ están cubiertas porque $u', v' \in C$.

**(⇐) Si existe una Cobertura de Vértices de tamaño $k'$ en $G'$, entonces existe un Conjunto Dominante de tamaño $k$ en $G$.**

- Sea $C \subseteq V'$ una cobertura de vértices en $G'$ de tamaño $k'$.
- Observamos que para cubrir las aristas $(v, v')$, al menos uno de $v$ o $v'$ debe estar en $C$.
- Como hay $|V|$ pares $(v, v')$, y $k' = k + |V|$, al menos $|V|$ vértices de la forma $v$ o $v'$ están en $C$.
- Sin pérdida de generalidad, asumimos que todos los $v'$ están en $C$ (si no, podemos intercambiarlos con sus respectivos $v$ sin aumentar el tamaño de $C$).
- Los $k$ vértices restantes en $C$ deben provenir de $V$.
- Sea $D = C \cap V$.
- **Dominancia en $G$:**
  - Para cada $v \in V$, si $v \in D$, entonces está dominado.
  - Si $v \notin D$, entonces su correspondiente $v' \in C$. Para cubrir la arista $(v', u')$ en $G'$, donde $(v, u) \in E$, $u'$ o $v'$ deben estar en $C$. Como $v' \in C$, y $v'$ solo está conectado a $v$ y a los $u'$, esto implica que $u \in D$ para algún vecino $u$ de $v$.
  - Por lo tanto, $v$ está dominado por $u \in D$.

---

** en conclusión:**

Hemos demostrado que existe una reducción en tiempo polinomial del problema de _Dominating Set_ al problema de _Vertex Cover_. Esta reducción preserva las soluciones, lo que significa que resolver el problema de _Vertex Cover_ en el grafo $G'$ nos proporciona una solución al problema de _Dominating Set_ en el grafo original $G$.
