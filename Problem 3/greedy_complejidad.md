# Factor de Aproximación del Algoritmo Greedy de $ O(\log n) $ para el Conjunto Dominante

El objetivo es demostrar que el **Algoritmo Greedy** proporciona una aproximación de $ \ln(\Delta) $, donde $ \Delta $ es el grado máximo del grafo (es decir, el nodo con más vecinos).

### Contexto del Problema

Estamos resolviendo el problema del **Conjunto Dominante** en un grafo, donde queremos seleccionar un subconjunto de nodos tal que:

- Cada nodo en el grafo esté cubierto directamente (pertenezca al conjunto) o tenga un vecino que esté en el conjunto.
- El objetivo es minimizar el tamaño de este conjunto dominante.

### Idea del Algoritmo Greedy

El **Algoritmo Greedy** selecciona nodos de forma ávida, eligiendo siempre el nodo que cubre más nodos no cubiertos en cada paso, hasta que todos los nodos estén cubiertos. El objetivo es probar que este proceso nos da una solución que es, como máximo, $ \ln(\Delta) $ veces más grande que la solución óptima.

### Análisis Amortizado: Distribución del Costo

#### ¿Qué significa el análisis amortizado?

Cuando seleccionamos un nodo para el conjunto dominante, en lugar de asignar todo el costo de esa selección a ese nodo, distribuimos el costo entre todos los **nodos no cubiertos** que ese nodo acaba de cubrir.

Por ejemplo:

- Si seleccionamos un nodo $ v $ y este cubre a 5 nodos no cubiertos (incluyéndose a sí mismo si también estaba sin cubrir), asignamos una fracción del costo de $ \frac{1}{5} $ a cada uno de esos 5 nodos.

### Descomposición del grafo en estrellas

Supongamos que tenemos una solución óptima al problema, es decir, un conjunto dominante $ S^* $. Sabemos que en $ S^* $, cada nodo que no pertenece al conjunto dominante tiene un vecino que sí pertenece. Esto nos permite dividir el grafo en **"estrellas"**, donde:

- Cada estrella tiene un **nodo dominante** de $ S^* $ como "centro".
- Los **nodos no cubiertos** por otros están "conectados" a este centro.

El costo de la solución óptima es cubrir 1 estrella por cada nodo en $ S^* $, lo que significa que el costo de cubrir todos los nodos de la estrella es 1.

#### Ejemplo de cómo se ve una estrella en un grafo:
```bash
  o        <- Nodo central (dominador)
 /|\
o o o     <- Nodos no cubiertos (vecinos del nodo central)
```


En este ejemplo:

- El nodo central $ o $ (dominador) está en el conjunto dominante $ S^* $.
- Los nodos conectados debajo son **nodos no cubiertos** que dependen del nodo central para estar cubiertos en el grafo.

### Costo amortizado del algoritmo greedy

En el **Algoritmo Greedy**, seleccionamos nodos basándonos en cuántos nodos no cubiertos pueden ser cubiertos en cada paso.

- Sea $ v $ el nodo dominante de una estrella en la solución óptima $ S^* $.
- Sea $ w(v) $ el número de nodos no cubiertos en la estrella de $ v $.

Cuando el algoritmo greedy selecciona un nodo, cubre a $ w(v) $ nodos, y asigna una fracción del costo de $ \frac{1}{w(v)} $ a cada uno de los nodos cubiertos. Esto se hace porque si $ v $ puede cubrir muchos nodos, el costo se reparte entre todos ellos.

Una vez que un nodo ha sido cubierto, no recibe más costos.

### Peor caso y costo total
En el peor caso, el algoritmo greedy selecciona nodos uno a uno, cubriendo un nodo en cada paso. El costo total que recibe cada nodo en una estrella es la suma de fracciones de costo, como:

$$
\sum_{i=1}^{\delta(v) + 1} \frac{1}{i} = \frac{1}{\delta(v)+1} + \frac{1}{\delta(v)} + \dots + \frac{1}{2} + \frac{1}{1} = H(\delta(v) + 1),
$$

donde $ H(\delta(v) + 1) $ es la **función armónica**, que se comporta asintóticamente como:

$$
H(\delta(v) + 1) \approx \ln(\delta(v) + 1) + O(1),
$$

donde $ \delta(v) $ es el número de vecinos del nodo $ v $, y por tanto $ H(\delta(v) + 1) $ se aproxima a $ \ln(\Delta) $, siendo $ \Delta $ el grado máximo en el grafo.

s### Conclusión

El costo amortizado total por estrella en el peor caso es aproximadamente $ \ln(\Delta) $. Esto significa que el número de nodos en el conjunto dominante calculado por el **Algoritmo Greedy** es como máximo $ \ln(\Delta) $ veces mayor que el tamaño del conjunto dominante óptimo.

Por lo tanto, el algoritmo proporciona una aproximación de $ \ln(\Delta) $ para el problema del conjunto dominante.

### En resumen:

- El algoritmo selecciona nodos que cubren más nodos no cubiertos en cada paso.
- El costo de seleccionar un nodo se distribuye entre todos los nodos que cubre.
- El análisis muestra que el costo total es $ \ln(\Delta) $, lo que demuestra que el algoritmo es una buena aproximación al conjunto dominante óptimo.
