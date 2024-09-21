# El Algoritmo Greedy Tiene un Factor de Aproximación de $ O(\log n) $ para el Conjunto Dominante

## Introducción

El **problema del conjunto dominante** se define en teoría de grafos como sigue: dado un grafo $ G = (V, E) $, encontrar el subconjunto mínimo $ D \subseteq V $ tal que cada vértice en $ V $ es miembro de $ D $ o es adyacente a al menos un miembro de $ D $. Este problema es **NP-difícil**, por lo que utilizamos algoritmos de aproximación para encontrar soluciones cercanas al óptimo en tiempo polinomial.

El **algoritmo greedy (codicioso)** es una heurística simple que selecciona en cada paso el vértice que domina el mayor número de vértices no dominados. Nuestro objetivo es demostrar que este algoritmo tiene un factor de aproximación de $ O(\log n) $ respecto al tamaño del conjunto dominante mínimo.

---

## Descripción del Algoritmo Greedy para el Conjunto Dominante

El algoritmo procede de la siguiente manera:

1. **Inicialización**:
   - Sea $ D = \emptyset $, el conjunto dominante (inicialmente vacío).
   - Sea $ U = V $, el conjunto de vértices no dominados (inicialmente todos los vértices).

2. **Iteración**:
   - Mientras $ U \neq \emptyset $:
     - Para cada vértice $ v \in V $, calcular:
       $$
       s(v) = |N[v] \cap U|
       $$
       donde $ N[v] = \{v\} \cup N(v) $ es el conjunto cerrado de vecinos de $ v $.
     - Seleccionar el vértice $ v^* $ que maximiza $ s(v) $:
       $$
       v^* = \arg\max_{v \in V} s(v)
       $$
     - Agregar $ v^* $ al conjunto dominante:
       $$
       D = D \cup \{v^*\}
       $$
     - Actualizar el conjunto de vértices no dominados:
       $$
       U = U \setminus N[v^*]
       $$

3. **Finalización**:
   - Devolver $ D $ como el conjunto dominante aproximado.

---

## Análisis del Factor de Aproximación $ O(\log n) $

Queremos demostrar que:
$$
|D| \leq \text{OPT} \cdot \ln n
$$
donde:
- $ |D| $ es el tamaño del conjunto dominante obtenido por el algoritmo greedy.
- $ \text{OPT} $ es el tamaño del conjunto dominante mínimo.
- $ n = |V| $ es el número de vértices del grafo.

### Definiciones Iniciales

- Sea $ D^* $ un conjunto dominante óptimo de tamaño $ k = |D^*| = \text{OPT} $.
- Sea $ U_t $ el conjunto de vértices no dominados al inicio de la iteración $ t $.
- Sea $ n_t = |U_t| $.

### Paso 1: Cota Inferior del Número de Vértices Dominados en Cada Iteración

En cada iteración, el algoritmo selecciona un vértice $ v^* $ que domina el máximo número de vértices no dominados.

**Afirmación**: Existe al menos un vértice $ v \in D^* $ tal que:
$$
s(v) \geq \frac{n_t}{k}
$$

**Demostración de la Afirmación**:

- Cada vértice en $ U_t $ debe ser dominado por al menos un vértice en $ D^* $.
- La suma total de los valores $ s(v) $ para $ v \in D^* $ es al menos $ n_t $:
  $$
  \sum_{v \in D^*} s(v) \geq n_t
  $$
- Por el principio del promedio:
  $$
  \frac{1}{k} \sum_{v \in D^*} s(v) \geq \frac{n_t}{k}
  $$
- Por lo tanto, existe al menos un $ v \in D^* $ tal que:
  $$
  s(v) \geq \frac{n_t}{k}
  $$
- Dado que el algoritmo greedy elige el $ v^* $ que maximiza $ s(v) $, tenemos:
  $$
  s(v^*) \geq \frac{n_t}{k}
  $$

### Paso 2: Reducción Proporcional de Vértices No Dominados

Después de seleccionar $ v^* $, el número de vértices no dominados se reduce en al menos $ \frac{1}{k} $ del total actual:

- Actualizamos $ U_{t+1} $:
  $$
  U_{t+1} = U_t \setminus N[v^*]
  $$
- El número de vértices no dominados en la siguiente iteración es:
  $$
  n_{t+1} = n_t - s(v^*) \leq n_t - \frac{n_t}{k} = n_t \left(1 - \frac{1}{k}\right)
  $$
- Por lo tanto:
  $$
  n_{t+1} \leq n_t \left(1 - \frac{1}{k}\right)
  $$

### Paso 3: Cota del Número de Iteraciones

Queremos encontrar $ T $ tal que $ n_T \leq 1 $ (todos los vértices han sido dominados).

Aplicando la reducción sucesivamente:
$$
n_T \leq n \left(1 - \frac{1}{k}\right)^T
$$

Para que $ n_T \leq 1 $:
$$
n \left(1 - \frac{1}{k}\right)^T \leq 1
$$

Tomando logaritmos naturales en ambos lados:
$$
\ln \left( n \left(1 - \frac{1}{k}\right)^T \right) \leq 0
$$

Simplificando:
$$
\ln n + T \ln \left(1 - \frac{1}{k}\right) \leq 0
$$

Utilizando la desigualdad $ \ln(1 - x) \leq -x $ para $ 0 < x < 1 $:
$$
\ln \left(1 - \frac{1}{k}\right) \leq -\frac{1}{k}
$$

Entonces:
$$
\ln n - T \left( \frac{1}{k} \right ) \leq 0
$$

Despejando $ T $:
$$
T \geq k \ln n
$$

### Paso 4: Conclusión Sobre el Tamaño del Conjunto Dominante

El número de iteraciones $ T $ es igual al tamaño del conjunto dominante obtenido:
$$
|D| = T \leq k \ln n = \text{OPT} \cdot \ln n
$$

---

## Conclusión

Hemos demostrado que el algoritmo greedy para el problema del conjunto dominante produce un conjunto $ D $ cuyo tamaño está acotado por:
$$
|D| \leq \text{OPT} \cdot \ln n
$$

Esto significa que el algoritmo tiene un factor de aproximación de $ O(\log n) $ respecto al tamaño del conjunto dominante mínimo.

---

## Resumen de Fórmulas Clave

1. **Cota Inferior del Número de Vértices Dominados**:
   $$
   s(v^*) \geq \frac{n_t}{k}
   $$

2. **Reducción del Número de Vértices No Dominados**:
   $$
   n_{t+1} \leq n_t \left(1 - \frac{1}{k}\right)
   $$

3. **Cota del Número de Iteraciones**:
   $$
   T \geq k \ln n
   $$

4. **Factor de Aproximación**:
   $$
   |D| \leq \text{OPT} \cdot \ln n
   $$

---

## Notas Adicionales

- **Propiedades Monótonas y Submodulares**: La función que mide el número de vértices dominados es monótona creciente y submodular, lo que justifica el uso del algoritmo greedy.

- **Importancia Práctica**: Este resultado es valioso en aplicaciones donde es esencial encontrar soluciones cercanas al óptimo en tiempo razonable, como en redes de sensores, diseño de redes y otras áreas de optimización combinatoria.

---

## Referencias

- **Libros y Artículos**:
  - Vazirani, V. V. (2001). *Approximation Algorithms*. Springer.
  - Nemhauser, G. L., Wolsey, L. A., & Fisher, M. L. (1978). *An analysis of approximations for maximizing submodular set functions—II*. Mathematical Programming, 14(1), 265-294.

- **Conceptos Clave**:
  - **Funciones Submodulares**: Funciones que exhiben rendimientos decrecientes.
  - **Algoritmos Greedy**: Algoritmos que toman decisiones óptimas locales con la esperanza de encontrar una solución globalmente óptima o cercana al óptimo.

---

## Ejemplo Ilustrativo

Supongamos un grafo sencillo donde queremos aplicar el algoritmo greedy para encontrar un conjunto dominante.

- **Grafo**:

  - Vértices: $ V = \{1, 2, 3, 4, 5\} $
  - Aristas:
    - $ 1 $ está conectado con $ 2 $ y $ 3 $
    - $ 2 $ está conectado con $ 1 $ y $ 4 $
    - $ 3 $ está conectado con $ 1 $
    - $ 4 $ está conectado con $ 2 $ y $ 5 $
    - $ 5 $ está conectado con $ 4 $

- **Aplicación del Algoritmo Greedy**:

  - **Iteración 1**:
    - Vértices no dominados: $ U = \{1, 2, 3, 4, 5\} $
    - Calculamos $ s(v) $ para cada $ v $:
      - $ s(1) = |\{1, 2, 3\} \cap U| = 3 $
      - $ s(2) = |\{2, 1, 4\} \cap U| = 3 $
      - $ s(3) = |\{3, 1\} \cap U| = 2 $
      - $ s(4) = |\{4, 2, 5\} \cap U| = 3 $
      - $ s(5) = |\{5, 4\} \cap U| = 2 $
    - Seleccionamos $ v^* = 1 $ (puede ser cualquiera con $ s(v) = 3 $)
    - Actualizamos $ D = \{1\} $ y $ U = U \setminus N[1] = \{4, 5\} $

  - **Iteración 2**:
    - Vértices no dominados: $ U = \{4, 5\} $
    - Calculamos $ s(v) $ para cada $ v $:
      - $ s(4) = |\{4, 2, 5\} \cap U| = 2 $
      - $ s(5) = |\{5, 4\} \cap U| = 2 $
    - Seleccionamos $ v^* = 4 $
    - Actualizamos $ D = \{1, 4\} $ y $ U = U \setminus N[4] = \emptyset $

- **Resultado**:
  - Conjunto dominante aproximado: $ D = \{1, 4\} $
  - Supongamos que el conjunto dominante mínimo es $ D^* = \{2, 5\} $ con $ |D^*| = 2 $
  - Comprobamos la cota:
    $$
    |D| = 2 \leq 2 \ln 5 \approx 2 \times 1.6094 = 3.2188
    $$
    Lo cual es coherente con nuestra demostración.

---
