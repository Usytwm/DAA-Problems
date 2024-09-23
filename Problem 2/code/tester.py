import random
import time

from matplotlib import pyplot as plt
from brute_force import main as brute_force_main
from final_solution import main as final_solution_main
from uncompressed_solution import main as uncompresed_solution_main


def generate_random_test_case(n, m):
    sections = []
    for i in range(m):
        x1 = random.randint(1, n)
        y1 = random.randint(1, n)
        x2 = random.randint(x1, n)
        y2 = random.randint(x2, n)
        sections.append((x1, y1, x2, y2))
    return sections


def correctness_test(implementation, n, m, other_implementation=None):
    sections = generate_random_test_case(n, m)
    flow_value = implementation(sections)
    flow_value_brute = (
        brute_force_main(sections)
        if other_implementation is None
        else other_implementation(sections)
    )
    return flow_value == flow_value_brute


def speed_test(implementation, n, m):
    sections = generate_random_test_case(n, m)
    start_time = time.time()
    implementation(sections)
    end_time = time.time()
    return end_time - start_time


# Realizar los tests para diferentes tamaños de n y m y guardar los tiempos
def run_tests_time():
    ns = [10, 12, 13, 14, 15]  # Valores de n pequeños para brute_force
    ns_large = [
        10 * 2,
        2 * 10**2,
        3 * 10**2,
        4 * 10**2,
        5 * 10**2,
    ]  # Valores de n grandes para las otras implementaciones
    m = 50  # Valor de m significativamente más pequeño que n

    brute_force_times = []
    final_solution_times_ns = []
    uncompresed_solution_times_ns = []
    final_solution_times = []
    uncompresed_solution_times = []

    # Test para fuerza bruta
    for n in ns:
        print(f"Testing brute force for n = {n}, m = {n//5}")
        time_taken = speed_test(brute_force_main, n, n // 5)
        brute_force_times.append(time_taken)
        print(f"Brute force took {time_taken:.2f} seconds.")

        print(f"Testing final solution for n = {n}, m = {n//5}")
        time_taken = speed_test(final_solution_main, n, n // 5)
        final_solution_times_ns.append(time_taken)
        print(f"Final solution took {time_taken:.2f} seconds.")

        print(f"Testing uncompresed solution for n = {n}, m = {n//5}")
        time_taken = speed_test(uncompresed_solution_main, n, n // 5)
        uncompresed_solution_times_ns.append(time_taken)
        print(f"Uncompresed solution took {time_taken:.2f} seconds.")

    # Test para las otras soluciones con valores grandes de n
    for n in ns_large:
        print(f"Testing final solution for n = {n}, m = {m}")
        time_taken = speed_test(final_solution_main, n, m)
        final_solution_times.append(time_taken)
        print(f"Final solution took {time_taken:.2f} seconds.")

        print(f"Testing uncompresed solution for n = {n}, m = {m}")
        time_taken = speed_test(uncompresed_solution_main, n, m)
        uncompresed_solution_times.append(time_taken)
        print(f"Uncompresed solution took {time_taken:.2f} seconds.")

    # Graficar los tiempos para las primeras 3 implementaciones
    plt.figure(figsize=(12, 8))

    # Para brute force y las versiones con ns
    plt.plot(ns, brute_force_times, label="Brute Force", color="red")
    plt.plot(
        ns, final_solution_times_ns, label="Final Solution (Small n)", color="green"
    )
    plt.plot(
        ns,
        uncompresed_solution_times_ns,
        label="Uncompresed Solution (Small n)",
        color="blue",
    )

    plt.xlabel("Tamaño de n (pequeño)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Comparación de tiempos de ejecución (n pequeño)")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Graficar los tiempos para las siguientes 2 implementaciones
    plt.figure(figsize=(12, 8))

    # Para final_solution y uncompresed_solution con ns_large
    plt.plot(
        ns_large,
        final_solution_times,
        label="Final Solution",
        marker="x",
        color="green",
    )
    plt.plot(
        ns_large,
        uncompresed_solution_times,
        label="Uncompresed Solution",
        marker="s",
        color="blue",
    )

    plt.xlabel("Tamaño de n (grande)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Comparación de tiempos de ejecución (n grande)")
    plt.legend()
    plt.grid(True)
    plt.show()


def run_test_correctness():
    for n in range(1, 100):
        m = round(n * 0.1)  # Calcular m como el 10% de n, redondeado
        try:
            assert correctness_test(
                final_solution_main, n, m, uncompresed_solution_main
            ), f"Test failed for final_solution_main and uncompresed_solution_main with n={n}, m={m}"
        except AssertionError as e:
            print(e)
            print(f"Test failed for n = {n}, m = {m}")

    print("All tests passed (until failure)!")


if __name__ == "__main__":
    run_tests_time()
    run_test_correctness()
