# Videojuego

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

# Solucion del Problema

## Definimos el valor esperado

El problema se trata de minimizar el **valor esperado** de las ganancias del jugador, dado que comienza en una habitación aleatoria. El valor esperado de las ganancias se puede definir como:

$$
E = \frac{\text{suma total de ganancias sobre todas las posiciones}}{n}
$$

Donde $ n $ es el número total de habitaciones (o cofres). Como estamos buscando minimizar este valor esperado, es equivalente a **minimizar la suma total de ganancias**, ya que $n$ es constante. **Por lo tanto, reformulamos el problema como la minimización de la suma total de las ganancias**.

---

## Rotación y distribución de cofres regulares y trampas

Para simplificar el análisis, **rotamos las habitaciones** de tal forma que la última habitación siempre contenga una trampa. Esto no cambia la naturaleza del problema, pero facilita la distribución de cofres regulares y trampas en el análisis.

Supongamos que tenemos $k$ trampas. Entonces, las habitaciones se distribuyen en $k$ grupos, donde cada grupo contiene $ \text{cnt}_i $ cofres regulares seguidos de una trampa. Los $ \text{cnt}_i $ satisfacen la siguiente restricción:

$$
\begin{array}{c}
\text{cnt}_i \geq 0 \quad \text{y} \quad \sum_{i=1}^{k} \text{cnt}_i = n - k
\end{array}
$$


Esto significa que los $n - k$ cofres regulares se distribuyen en los $k$ intervalos entre las trampas.

## Ejemplo:

Supongamos que tenemos $ n = 10 $ habitaciones y $ k = 3 $ trampas. El jugador comienza en una habitación aleatoria, y las trampas están distribuidas. Los valores de los cofres son los siguientes:

### Lista de habitaciones con cofres y trampas:
[100, 200, **Trampa**, **Trampa**, 50, 300, **Trampa**, 500, 400, **Trampa**]


### Distribución de intervalos:

$$
\underbrace{\text{100, 200}}_{\text{cnt}_1 = 2} \quad
\underbrace{\text{Trampa, Trampa}}_{\text{cnt}_2 = 0} \quad
\underbrace{\text{50, 300}}_{\text{cnt}_3 = 2} \quad
\underbrace{\text{500, 400}}_{\text{cnt}_4 = 2}
$$

### Restricción de los intervalos:

Tenemos que:

$$
\sum_{i=1}^{\text{k}=4} \text{cnt}_i = n - k = 10 - 4 = 6
$$
Y, efectivamente:

$$
\text{cnt}_1 = 2, \quad \text{cnt}_2 = 0, \quad \text{cnt}_3 = 2, \quad \text{cnt}_4 = 2
$$

Por lo tanto, los cofres regulares se distribuyen entre las trampas como sigue:

- Intervalo 1 tiene 2 cofres (valores 100 y 200), seguido de una trampa.
- Intervalo 2 es vacío, ya que hay dos trampas seguidas sin cofres regulares.
- Intervalo 3 tiene 2 cofres (valores 50 y 300), seguido de una trampa.
- Intervalo 4 tiene 2 cofres (valores 500 y 400), seguido de una trampa.


---
## Coeficientes y secuencias de ganancias

El **coeficiente** de un cofre $ c $ es el número de veces que el jugador puede recoger ese cofre desde las distintas posiciones iniciales de un intervalo antes de caer en una trampa. En un intervalo con $ \text{cnt}_i $ cofres regulares, el **último cofre** del intervalo puede ser recogido $ \text{cnt}_i $ veces, el penúltimo $ \text{cnt}_i - 1 $ veces, y así sucesivamente, essto debido a la naturaleza del juego de avanzar a la siguiente habitacion si no me encuentro un cofre Trampa.

Cada cofre tiene un coeficiente que refleja cuántas veces puede ser recogido dependiendo de su proximidad a la trampa. Los cofres más cercanos a la trampa tienen coeficientes más altos, ya que son alcanzables desde más posiciones iniciales. Esto significa que, cuanto más cerca esté el cofre de la siguiente trampa, mayor es su contribución potencial a las ganancias totales del jugador.

La **suma total de ganancias** en un intervalo se puede expresar como:

$$
\sum_{j=1}^{\text{cnt}_i} j \cdot v_j
$$

Donde $ v_j $ es el valor del $ j $-ésimo cofre del intervalo. Este cálculo asegura que los cofres más valiosos y cercanos a la trampa contribuyen más a las ganancias, ya que tienen mayores coeficientes. 

Esto se debe a que el número de veces que un cofre puede ser recogido depende directamente de su posición en relación con la trampa: los cofres más cercanos a la trampa pueden ser recogidos desde más posiciones iniciales. Al multiplicar el valor de cada cofre por su coeficiente, estamos sumando el impacto real de cada cofre en las ganancias totales, reflejando cómo su posición y valor combinan para maximizar o minimizar las ganancias en el intervalo.

---
## Balanceo de los intervalos

Cuando tenemos dos intervalos de cofres con diferentes tamaños, podemos **mejorar** la distribución de las ganancias moviendo cofres del intervalo más grande al más pequeño. Esto ayuda a minimizar el total de ganancias del jugador, ya que los coeficientes de los cofres cambian dependiendo del intervalo al que pertenecen.

El concepto clave es que los **coeficientes** afectan la suma total de ganancias: un cofre en el intervalo más grande tiene un coeficiente más alto (y por lo tanto contribuye más a la suma total de ganancias), mientras que si movemos ese cofre al intervalo más pequeño, su coeficiente será más bajo, lo que reducirá las ganancias totales.

### Demostración del balanceo:

1. **Identificar los intervalos más grande y más pequeño**:
   - Supongamos que el intervalo más grande tiene $ y $ cofres, y el más pequeño tiene $ x $ cofres, donde $ x \leq y - 2 $.
   - Queremos reducir esta diferencia moviendo un cofre del intervalo más grande al más pequeño.

2. **Secuencias de coeficientes**:
   - En el intervalo más pequeño ($ x $), los cofres tienen los coeficientes $[1, 2, \dots, x]$.
   - En el intervalo más grande ($ y $), los cofres tienen los coeficientes $[1, 2, \dots, y]$.
   - La contribución a las ganancias está dada por $ \sum_{j=1}^{x} j \cdot v_j $ para el intervalo pequeño y $ \sum_{j=1}^{y} j \cdot v_j $ para el grande.

3. **Mover un cofre del intervalo más grande al más pequeño**:
   - Antes del movimiento, el último cofre del intervalo grande tiene un coeficiente $ y $, y el último cofre del intervalo pequeño tiene un coeficiente $ x $.
   - Si movemos el cofre del intervalo grande al pequeño, el coeficiente de ese cofre baja de $ y $ a $ x + 1 $. Esto significa que el cofre ahora se recoge menos veces, **reduciendo la suma total de ganancias**.
   
4. **Justificación matemática**:
   - La secuencia de coeficientes en el intervalo más pequeño, después de mover el cofre, será $[1, 2, \dots, x, x + 1]$.
   - La secuencia en el intervalo más grande será $[1, 2, \dots, y - 1]$.
   - Al reducir el coeficiente más alto de $ y $ a $ x + 1 $, hemos logrado una reducción efectiva en la suma total de ganancias, ya que el cofre valioso del intervalo más grande se recoge menos veces. Esto **minimiza** el impacto de ese cofre en las ganancias totales.

### Demostración:

Cuando movemos un cofre del intervalo grande al intervalo pequeño, la contribución de ese cofre a la suma total de ganancias cambia, ya que su **coeficiente** cambia. 

- **Antes del movimiento**: El cofre $ v_j $ está en el intervalo grande, donde su coeficiente es $ y $, por lo que su contribución a las ganancias es $ v_j \times y $.
- **Después del movimiento**: El cofre se mueve al intervalo pequeño, donde su nuevo coeficiente es $ x + 1 $, lo que significa que su contribución ahora es $ v_j \times (x + 1) $.

La **reducción en las ganancias** es la diferencia entre la contribución original y la nueva contribución:

$$
\Delta \text{Ganancia} = v_j \times (y - (x + 1))
$$

Donde:
- $ v_j $ es el valor del cofre ($ v_j \geq 0$).
- $ y $ es el coeficiente en el intervalo grande ($ x \leq y - 2 $).
- $ x + 1 $ es el nuevo coeficiente en el intervalo pequeño ($ x > 0$) .

Este resultado muestra que al mover un cofre del intervalo más grande al más pequeño, estamos disminuyendo su coeficiente, lo que significa que el cofre se recogerá menos veces, y por lo tanto, su contribución total a las ganancias se reducirá. La fórmula $ v_j \times (y - (x + 1)) $ refleja precisamente cuánto disminuyen las ganancias cuando el cofre es movido.

Si la diferencia entre $ y $ y $ x + 1 $ es grande, la reducción en las ganancias será mayor, por lo cual mover cofres de intervalos grandes a pequeños es una estrategia efectiva para minimizar las ganancias totales.

### ¿Por qué sucede esto?

Cuando la diferencia entre los tamaños de los intervalos es mayor o igual a 2 (es decir, $ x \leq y - 2 $), siempre existe la posibilidad de **mejorar** la distribución de cofres moviendo uno del intervalo más grande al más pequeño. Esto se debe a que los coeficientes de los cofres en el intervalo más grande son más altos, lo que aumenta las ganancias totales del jugador. Al mover el cofre al intervalo más pequeño, el coeficiente baja, lo que disminuye la contribución de ese cofre a las ganancias totales.

---
<!-- ## Asignación óptima de cofres regulares

Después de balancear los intervalos, el siguiente paso es asignar los cofres regulares de manera **óptima**. El objetivo es minimizar las ganancias esperadas del jugador.

### Proceso de asignación:
1. **Ordenar los cofres por valor**: Para minimizar las ganancias, es importante colocar los cofres más valiosos en las posiciones con los coeficientes más bajos, es decir, donde el jugador tendrá menos oportunidades de recogerlos. Esto se hace ordenando los valores de los cofres en **orden no creciente** (de mayor a menor). La razón detrás de esto es simple: si los cofres más valiosos se recogen menos veces, contribuyen menos a las ganancias totales.

2. **Asignar los valores a los coeficientes**: Luego de ordenar los cofres, los cofres más valiosos se asignan a los **coeficientes más bajos**. Por ejemplo, el cofre con el mayor valor se asigna a la posición donde su coeficiente es más bajo (cerca de una trampa). Esto minimiza su impacto en la suma total de ganancias.

### Justificación matemática:

Si se distribuyen los cofres de manera diferente (por ejemplo, asignando un cofre valioso a una posición con un coeficiente alto), se podría **mejorar** esa disposición moviendo cofres más valiosos a posiciones con coeficientes más bajos, lo que automáticamente reduciría las ganancias totales. Por eso, ordenar los cofres de mayor a menor valor y asignarlos a los coeficientes más bajos es la manera **óptima** de proceder.

---

## Probabilidades y valor esperado

El valor esperado de las ganancias se relaciona directamente con las **probabilidades** de recoger cofres desde una posición inicial aleatoria. Dado que el jugador comienza en una habitación aleatoria, cada habitación tiene la misma probabilidad de ser elegida.

Para un cofre $ v_j $ en una posición $ j $-ésima dentro de un intervalo con $ \text{cnt}_i $ cofres, la probabilidad de recoger ese cofre desde una posición inicial aleatoria es:

$$
P(\text{recoger } v_j) = \frac{j}{n}
$$

Donde:
- $ j $ es el número de veces que se puede recoger el cofre $ v_j $ antes de llegar a una trampa.
- $ n $ es el número total de habitaciones.

El **valor esperado** de las ganancias del jugador se puede calcular sumando las contribuciones de cada cofre, ponderadas por su coeficiente y su valor:

$$
E = \sum_{i=1}^{k} \sum_{j=1}^{\text{cnt}_i} \frac{j \cdot v_j}{n}
$$

### ¿Por qué se minimizan las ganancias con este enfoque?

El enfoque de asignar los cofres más valiosos a las posiciones con coeficientes más bajos asegura que se minimice la contribución de esos cofres a la suma total de ganancias, dado que las probabilidades de recogerlos son menores en esas posiciones.

---

## Complejidad y optimización

El cálculo de la asignación óptima tiene una complejidad de $ O(n \log n) $ debido a la necesidad de ordenar los cofres por su valor. Sin embargo, una vez que los cofres están ordenados y asignados, el cálculo de las ganancias se puede optimizar utilizando **sumas acumuladas** o **sumas prefix**, lo que reduce el costo computacional a $ O(n) $ para cada $ k $.

### Optimización con sumas prefix:

- Las **primeras $ k $ posiciones** están multiplicadas por 0 (ya que no se recogen cofres).
- Las **segundas $ k $ posiciones** están multiplicadas por 1.
- Y así sucesivamente.

Si el número de habitaciones $ n $ no es divisible por $ k $, el último bloque tiene una longitud menor que $ k $, lo que se puede manejar fácilmente con las sumas acumuladas.

Por lo tanto, la complejidad total de calcular las ganancias esperadas es $ O(n \log n) $, que se deriva de sumar el tiempo de ordenación y la optimización mediante sumas prefix.

---

## Conclusión:

El valor esperado de las ganancias se minimiza al seguir estos pasos:
1. **Balancear los intervalos** moviendo cofres de intervalos grandes a pequeños.
2. **Asignar los cofres más valiosos** a las posiciones con los coeficientes más bajos, minimizando su impacto en las ganancias.
3. **Utilizar sumas acumuladas (prefix sums)** para calcular las ganancias de manera eficiente.

Este enfoque permite calcular las ganancias con una complejidad total de $ O(n \log n) $, asegurando que el jugador tenga las menores ganancias posibles. -->
## Asignación óptima de cofres regulares

Después de balancear los intervalos, el siguiente paso es asignar los cofres regulares de manera **óptima**. El objetivo es minimizar las ganancias esperadas del jugador.

### Proceso de asignación:
1. **Unión de coeficientes**: Después de definir todos los $ \text{cnt}_i $ (los tamaños de cada intervalo), debemos unir todas las secuencias de coeficientes desde los diferentes intervalos. Esto nos da una secuencia que abarca todas las posiciones posibles donde los cofres pueden ser asignados. Los coeficientes de cada intervalo forman secuencias $ [1, 2, \dots, \text{cnt}_i] $ para cada $ i $. Una vez que unimos estas secuencias de coeficientes, obtenemos la secuencia global de coeficientes $ \bigcup_{i=1}^{n-k} [1, 2, \dots, \text{cnt}_i] $.

2. **Ordenar los cofres por valor**: Para minimizar las ganancias, es importante colocar los cofres más valiosos en las posiciones con los coeficientes más bajos, es decir, donde el jugador tendrá menos oportunidades de recogerlos. Esto se hace ordenando los valores de los cofres en **orden no creciente** (de mayor a menor). La razón detrás de esto es simple: si los cofres más valiosos se recogen menos veces, contribuyen menos a las ganancias totales.

3. **Asignar los valores a los coeficientes**: Después de unir y ordenar los coeficientes de los intervalos, se asignan los cofres en función de esta secuencia. Los cofres con mayor valor se colocan en los coeficientes más bajos. Esto garantiza que los cofres más valiosos se recojan menos veces y, por lo tanto, **minimicen las ganancias**.

### Justificación matemática:

Si los cofres se distribuyen de manera diferente (por ejemplo, asignando un cofre valioso a una posición con un coeficiente alto), se podría **mejorar** esa disposición moviendo cofres más valiosos a posiciones con coeficientes más bajos, lo que automáticamente reduciría las ganancias totales. Por eso, ordenar los cofres de mayor a menor valor y asignarlos a los coeficientes más bajos es la manera **óptima** de proceder.

### Complejidad:

La unión y ordenación de los cofres y los coeficientes tiene una complejidad de $ O(n^2) $ en el peor de los casos, pero este proceso puede mejorarse con técnicas adicionales que reducirán el tiempo de cálculo.

---

## Probabilidades y valor esperado

El valor esperado de las ganancias está relacionado directamente con las **probabilidades** de recoger cofres desde una posición inicial aleatoria. Dado que el jugador comienza en una habitación aleatoria, cada habitación tiene la misma probabilidad de ser elegida.

Para un cofre $ v_j $ en una posición $ j $-ésima dentro de un intervalo con $ \text{cnt}_i $ cofres, la probabilidad de recoger ese cofre desde una posición inicial aleatoria es:

$$
P(\text{recoger } v_j) = \frac{j}{n}
$$

Donde:
- $ j $ es el número de veces que se puede recoger el cofre $ v_j $ antes de llegar a una trampa.
- $ n $ es el número total de habitaciones.

El **valor esperado** de las ganancias del jugador se puede calcular sumando las contribuciones de cada cofre, ponderadas por su coeficiente y su valor:

$$
E = \sum_{i=1}^{k} \sum_{j=1}^{\text{cnt}_i} \frac{j \cdot v_j}{n}
$$

### ¿Por qué se minimizan las ganancias con este enfoque?

El enfoque de asignar los cofres más valiosos a las posiciones con coeficientes más bajos asegura que se minimice la contribución de esos cofres a la suma total de ganancias, dado que las probabilidades de recogerlos son menores en esas posiciones.

---

## Complejidad y optimización

El cálculo de la asignación óptima tiene una complejidad de $ O(n \log n) $ debido a la necesidad de ordenar los cofres por su valor. Sin embargo, una vez que los cofres están ordenados y asignados, el cálculo de las ganancias se puede optimizar utilizando **sumas acumuladas** o **sumas prefix**, lo que reduce el costo computacional a $ O(n) $ para cada $ k $.

### Optimización con sumas prefix:

- Las **primeras $ k $ posiciones** están multiplicadas por 0 (ya que no se recogen cofres).
- Las **segundas $ k $ posiciones** están multiplicadas por 1.
- Y así sucesivamente.

Si el número de habitaciones $ n $ no es divisible por $ k $, el último bloque tiene una longitud menor que $ k $, lo que se puede manejar fácilmente con las sumas acumuladas.

Por lo tanto, la complejidad total de calcular las ganancias esperadas es $ O(n \log n) $, que se deriva de sumar el tiempo de ordenación y la optimización mediante sumas prefix.

---

## Conclusión:

El valor esperado de las ganancias se minimiza al seguir estos pasos:
1. **Balancear los intervalos** moviendo cofres de intervalos grandes a pequeños.
2. **Asignar los cofres más valiosos** a las posiciones con los coeficientes más bajos, minimizando su impacto en las ganancias.
3. **Utilizar sumas acumuladas (prefix sums)** para calcular las ganancias de manera eficiente.

Este enfoque permite calcular las ganancias con una complejidad total de $ O(n \log n) $, asegurando que el jugador tenga las menores ganancias posibles.
