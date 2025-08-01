# cantidad de caminos en una grilla de 20x20
# algo3 vibes

from math import comb
import time
N = 20


def caminos(i, j):

    if i == 1 and j == 1:
        return 2

    if i == 1:
        return 1 + caminos(i, j-1)

    if j == 1:
        return 1 + caminos(i-1, j)

    else:
        return caminos(i-1, j) + caminos(i, j-1)


# piensa cami piensa, programacion dinamica


N = 20

# Versión original (muy lenta para N=20)

# O(2^N)


def caminos_recursivo(i, j):
    if i == 1 and j == 1:
        return 2
    if i == 1:
        return 1 + caminos_recursivo(i, j-1)
    if j == 1:
        return 1 + caminos_recursivo(i-1, j)
    else:
        return caminos_recursivo(i-1, j) + caminos_recursivo(i, j-1)


# como estoy recalculando varias veces lo mismo, usamos una matriz!!

# O(N^2)
def caminos_matriz(n):
    # matriz con resultados previos
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # cantidad de caminos para 1x1
    dp[1][1] = 2

    # los bordes solo suman 1 posible camino mas
    for j in range(2, n + 1):
        dp[1][j] = 1 + dp[1][j-1]

    for i in range(2, n + 1):
        dp[i][1] = 1 + dp[i-1][1]

    # no estoy en ningun borde
    for i in range(2, n + 1):
        for j in range(2, n + 1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[n][n]


print(caminos_matriz(N))
