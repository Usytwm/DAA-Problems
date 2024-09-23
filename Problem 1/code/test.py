import random
import matplotlib.pyplot as plt
import time


from optimized_solution import expected_value_optimized
from solution import expected_value


def test_performance():
    test_cases = [
        [10**6] * 10**5,  # large input all same
        [random.randint(1, 10**6) for _ in range(10**5)],  # large input random values
        list(range(10**5, 0, -1)),  # descending sorted
        [10**9] * 10**5,  # extremely large values
        [10**9 if i % 2 == 0 else 1 for i in range(10**5)],  # alternating high low
    ]

    for index, c in enumerate(test_cases, start=1):
        print(f"Testing case {index} with {len(c)} elements.")
        # Test optimized version
        start_time = time.time()
        result_optimized = expected_value_optimized(c.copy())
        end_time = time.time()
        print(f"Optimized version took {end_time - start_time:.2f} seconds.")

        # Test normal version
        start_time = time.time()
        result_normal = expected_value(c.copy())
        end_time = time.time()
        print(f"Normal version took {end_time - start_time:.2f} seconds.")

        # Verify results are the same
        assert result_optimized == result_normal, "Results differ between versions!"
        print("Results are identical between both versions.\n")


def test_performance_and_collect_results(
    num_tests, initial_size=100, max_size=2 * 10**4
):
    print(
        f"Iniciando {num_tests} tests con tamaños de entrada aumentando de {initial_size} hasta {max_size}..."
    )
    times_optimized = []
    times_normal = []
    input_sizes = []  # Guardar el tamaño de entrada de cada test

    # Determinar el incremento del tamaño en cada iteración
    size_increment = (max_size - initial_size) // num_tests

    for i in range(num_tests):
        print(f"Test {i + 1} de {num_tests}...")
        # Calcular el tamaño de entrada para esta iteración
        input_size = initial_size + i * size_increment
        input_sizes.append(input_size)  # Guardar el tamaño de entrada

        # Generar caso de prueba aleatorio para este tamaño de entrada
        test_case = [random.randint(1, 10**6) for _ in range(input_size)]

        # Medir tiempo para la versión optimizada
        start_time = time.time()
        expected_value_optimized(test_case.copy())
        end_time = time.time()
        times_optimized.append(end_time - start_time)

        # Medir tiempo para la versión normal
        start_time = time.time()
        expected_value(test_case.copy())
        end_time = time.time()
        times_normal.append(end_time - start_time)

        # Mostrar progreso cada 1000 iteraciones
        if (i + 1) % 1000 == 0:
            print(f"{i + 1} tests completados con tamaño de entrada {input_size}...")

    print("\n--- Resultados finales ---")
    print(f"Tiempo total versión optimizada: {sum(times_optimized):.2f} segundos.")
    print(f"Tiempo total versión normal: {sum(times_normal):.2f} segundos.")
    print(
        f"Tiempo promedio versión optimizada: {sum(times_optimized)/num_tests:.4f} segundos."
    )
    print(
        f"Tiempo promedio versión normal: {sum(times_normal)/num_tests:.4f} segundos."
    )

    # Graficar los resultados de los tiempos
    plt.figure(figsize=(10, 6))
    plt.plot(
        input_sizes,
        times_optimized,
        label="Optimized",
        color="blue",
        markersize=2,
    )
    plt.plot(input_sizes, times_normal, label="Normal", color="red", markersize=2)
    plt.xlabel("Tamaño de entrada")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Comparación de tiempos de ejecución: Optimizado vs Normal")
    plt.legend()
    plt.grid(True)
    plt.show()

    return input_sizes, times_optimized, times_normal


if __name__ == "__main__":
    # test_performance()
    num_tests = 250  # Número de tests a ejecutar
    initial_size = 100  # Tamaño inicial de la entrada

    input_sizes, times_optimized, times_normal = test_performance_and_collect_results(
        num_tests,
        initial_size,
    )
