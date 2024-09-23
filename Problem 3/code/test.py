import matplotlib.pyplot as plt
import random
import math

from approximate_solution import greedy_dominating_set
from exact_solution import find_minimum_dominating_set


MAX_GRAPH_SIZE = 100


# Generar grafos aleatorios
def generate_random_graph(num_nodos, probabilidad_conexion=0.5):
    grafo = {i: [] for i in range(num_nodos)}
    for i in range(num_nodos):
        for j in range(i + 1, num_nodos):
            if random.random() < probabilidad_conexion:
                grafo[i].append(j)
                grafo[j].append(i)
    return grafo


# Comparación de soluciones
def compare_solutions(num_grafos, probabilidad_conexion=0.5):
    exact_solution_sizes = []
    approximate_solution_sizes = []
    max_degrees = []

    for _ in range(num_grafos):
        # Generar grafo aleatorio
        num_nodos = random.randint(1, MAX_GRAPH_SIZE)
        graph = generate_random_graph(num_nodos, probabilidad_conexion)

        print(f"Grafo {_ + 1} de {num_grafos} con {num_nodos}:")

        # Calcular la solución exacta y la aproximada
        exact_solution = find_minimum_dominating_set(graph)
        approximate_solution = greedy_dominating_set(graph)

        # Obtener el nodo con mayor degree
        max_degree = max(len(neighbors) for neighbors in graph.values())

        # Guardar los resultados
        solution_size = len(exact_solution)
        approx_size = len(approximate_solution)
        exact_solution_sizes.append(solution_size)
        approximate_solution_sizes.append(approx_size)
        max_degrees.append(max_degree)

        # Verificar la condición teórica
        n = len(graph)
        if (
            not solution_size
            <= approx_size
            <= math.ceil(math.log(max_degree + 2)) * solution_size
            <= math.ceil(math.log(n) + 1) * solution_size
        ):
            raise Exception(
                f"Test failed for graph {_ + 1}. Solution size: {solution_size}, Approximation size: {approx_size}, Max degree: {max_degree}"
            )

        # Imprimir información del grafo actual

        print(f"  - Tamaño de la solución exacta: {solution_size}")
        print(f"  - Tamaño de la solución aproximada: {approx_size}")
        print(f"  - Grado máximo del grafo: {max_degree}")
        print()

    # Graficar los resultados
    plot_results(
        num_grafos, exact_solution_sizes, approximate_solution_sizes, max_degrees
    )


# graficar los resultados
def plot_results(
    num_grafos, exact_solution_sizes, approximate_solution_sizes, max_degrees
):
    x = list(range(1, num_grafos + 1))  # Eje X: número de grafo

    # Primer gráfico: Comparación de las soluciones exactas y aproximadas
    plt.figure(figsize=(10, 6))
    plt.plot(x, exact_solution_sizes, label="Solución Exacta", color="blue")
    plt.plot(
        x,
        approximate_solution_sizes,
        label="Solución Aproximada",
        color="green",
    )

    # Calcular el valor máximo entre las soluciones exactas y aproximadas
    max_value = max(max(exact_solution_sizes), max(approximate_solution_sizes))
    plt.ylim(0, max_value * 1.5)  # Expandir un 20% por encima del máximo

    plt.title("Comparación de soluciones exactas y aproximadas")
    plt.xlabel("Número de grafo")
    plt.ylabel("Tamaño del conjunto dominante")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Segundo gráfico: Comparación del logaritmo del grado máximo y la diferencia entre aproximada y exacta
    aprox = [approx for approx in approximate_solution_sizes]

    # Calcular el logaritmo de los grados máximos
    log_max_degrees = [
        math.ceil(math.log(degree + 2)) * exact_solution_sizes[index]
        for index, degree in enumerate(max_degrees)
    ]

    # Gráfico de logaritmo del grado máximo y diferencias entre aproximada y exacta
    plt.figure(figsize=(10, 6))
    plt.plot(
        x,
        log_max_degrees,
        label="Log(Grado Máximo) * Solucion Exacta",
        color="orange",
    )
    plt.plot(x, aprox, label=" Solucion Aproximada", color="red")

    # Calcular el valor máximo entre logaritmo de grados y solución aproximada
    max_value_log = max(max(log_max_degrees), max(aprox))
    plt.ylim(0, max_value_log * 1.5)  # Expandir un 20% por encima del máximo

    plt.title(
        "Logaritmo del Grado Máximo y diferencia entre soluciones aproximadas y exactas"
    )
    plt.xlabel("Número de grafo")
    plt.ylabel("Valor")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    compare_solutions(150, 0.4)
