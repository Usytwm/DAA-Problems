def calculate_expected_gain(n, cofre_values):
    # Ordenamos los valores de los cofres de mayor a menor
    cofre_values.sort(reverse=True)

    # Iteramos para cada valor de k (el número de trampas) de 1 a n
    for k in range(1, n + 1):
        total_gain = 0  # Inicializamos la ganancia total en 0
        j = 0  # Este contador se usa para multiplicar por el coeficiente

        # Iteramos sobre los cofres en intervalos de tamaño k
        for i in range(0, n, k):
            # Calculamos la ganancia del intervalo [i, i + k] (sin usar sumas acumuladas)
            interval_sum = sum(cofre_values[i : min(n, i + k)])
            total_gain += j * interval_sum
            j += 1  # Incrementamos el coeficiente para el siguiente intervalo

        # Dividimos la ganancia total entre n para obtener el valor esperado
        expected_gain = total_gain
        print(f"Ganancia esperada para k = {k}: {expected_gain}")


# Ejemplo de uso
n = 8
cofre_values = [10, 4, 3, 6, 5, 10, 7, 5]

calculate_expected_gain(n, cofre_values)
