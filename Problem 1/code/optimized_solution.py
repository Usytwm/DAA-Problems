"""
Complejidad Temporal: O(n log n)
"""


def expected_value_optimized(c: list[int]) -> list[float]:
    n = len(c)

    # Ordenar los cofres en orden descendente
    c.sort(reverse=True)  # * O(n log n)

    # Sumas acumuladas (prefix sums)
    pr = [0]
    for i in range(n):  # * O(n)
        pr.append(pr[-1] + c[i])

    result = []

    # Cálculo de las respuestas para cada k
    for k in range(1, n + 1):  # * O(n) iteraciones
        total_gain = 0
        j = 0
        for i in range(0, n, k):  # * n/k iteraciones => O(n/k) = O(log n)
            total_gain += j * (pr[min(n, i + k)] - pr[i])
            j += 1
        expected_gain = total_gain / n
        result.append(expected_gain)
        # print(f"Ganancia esperada para k = {k}: {total_gain}/{n} = {expected_gain}")
    # * O(n log n) + O(n) * O(log n) = O(n log n) en total
    return result


if __name__ == "__main__":
    c = list(map(int, input().split()))
    result = expected_value_optimized(c)
