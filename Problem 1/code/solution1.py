def main():
    n = int(input())
    c = list(map(int, input().split()))

    # Ordenar los cofres en orden descendente
    c.sort(reverse=True)

    # Sumas acumuladas (prefix sums)
    pr = [0]
    for i in range(n):
        pr.append(pr[-1] + c[i])

    # Cálculo de las respuestas para cada k
    for k in range(1, n + 1):
        ans = 0
        j = 0
        for i in range(0, n, k):
            ans += j * (pr[min(n, i + k)] - pr[i])
            j += 1
        # Dividir por n
        print(ans / n, end=" ")

    print()


if __name__ == "__main__":
    main()
