## Videojuego

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
