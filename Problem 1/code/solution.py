"""
Complejidad Temporal: O(n^2)
"""


def expected_value(c: list[int]) -> list[float]:
    n = len(c)

    # Ordenar los cofres en orden descendente
    c.sort(reverse=True)  # * O(n log n)

    result = []

    # Cálculo de las respuestas para cada k
    for k in range(1, n + 1):  # * O(n) iteraciones
        total_gain = 0
        j = 0
        for i in range(0, n, k):  # * O(n) iteraciones
            interval_sum = sum(c[i : min(n, i + k)])
            total_gain += j * interval_sum
            j += 1
        expected_gain = total_gain / n
        result.append(expected_gain)
        # print(f"Ganancia esperada para k = {k}: {total_gain}/{n} = {expected_gain}")

    # * O(n log n) + O(n) * O(n) = O(n^2) en total
    return result


if __name__ == "__main__":
    c = list(map(int, input().split()))
    result = expected_value(c)
